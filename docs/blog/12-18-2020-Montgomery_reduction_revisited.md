我之前已经在 [LOJ](https://loj.ac/d/2719) 写过一篇关于 Montgomery reduction 的基础的博客了，但是内容有所欠缺，于是在这里重新叙述。

## Montgomery reduction 回顾

如果您了解 Montgomery reduction ，那么这一部分基础的就无需浪费时间阅读了。

!!! quote "定义"

    定义：对于 $N\gt 1$ 选择一个基数 $R$ 与 $N$ 互素且 $R\gt N$ 。令 $R^{-1}$ 和 $N'$ 满足 $0\lt R^{-1}\lt N$ 且 $0\lt N'\lt R$ 且 $RR^{-1}-NN'=1$ 。对于 $T$ 满足 $0\leq T\lt RN$ ，我们将一种快速计算 $TR^{-1}\bmod{N}$ 的算法称为 Montgomery reduction 。

定义中您可能已经注意到 Bézout 等式 $RR^{-1}-NN'=1$ 这告诉我们 $N'\equiv -N^{-1}\pmod{R}$ 。这里将[^1]中算法描述如下

$$\begin{array}{ll}
\textbf{procedure }\operatorname{REDC}(T) \\
\qquad m\gets (T\bmod R)N'\bmod{R} \\
\qquad t\gets (T+mN)/R \\
\qquad \textbf{if }t\geq N\textbf{ then return }t-N \\
\qquad \textbf{else return } t
\end{array}$$

证明：观察到 $TN'\bmod R=TN'+kR$ 对于某个整数 $k$ 成立，那么

$$t=(T+(TN'+kR)N)/R=(T+TN'N+kRN)/R$$

而又因为 $N'N=-1+lR$ 对于某个整数 $l$ 成立，所以

$$t=(T+T(-1+lR)+kRN)/R=lT+kN$$

显然为整数。且因为 $0\leq T\lt RN,0\leq m\lt R$ 所以 $0\leq (T+mN)/R\lt 2N$ 。 $\square$

而在实践中通常选取 $R=2^{32}$ ，那么可以写下如下 C++ 代码

!!! note ""

    ```cpp
    typedef std::uint32_t u32;
    typedef std::uint64_t u64;
    // 预处理 N_p 作为 N' ，类型为 u32 ，模数 N 为奇数
    u32 REDC(u64 T) { return T + u64(u32(T) * N_p) * N >> 32; }
    ```

!!! warning ""

    其中我们没有处理 $t\geq N$ 的情况，这是因为假设选取的 $N\lt 2^{30}$ 此时返回值在 $[0,2N)$ 中，如果我们将两个 $T_{1},T_{2}$ 相乘再进行 REDC ，那么注意 REDC 的输入参数只要求 $[0,RN)$ 中即可，这样可以惰性的进行伪代码最后一步的“修正”过程。

假设我们需要在模奇数 $N$ 意义下对 $0\leq x\lt N$ 和 $0\leq y\lt N$ 计算 $xy\bmod N$，那么通过 $\operatorname{REDC}(x(R^{2}\bmod N))$ 计算 $xR\bmod N$ 再计算 $\operatorname{REDC}(xRy)$ 即可。这提示我们预处理 $R^{2}\bmod N$ 和 $N'$ 即可。

而 $N'$ 可以通过 Hensel lifting （可被视为 $p$-adic variant of Newton's method ）计算，因为 $N$ 为奇数，那么 $N^{-1}\bmod 2=1$ ，使用以下迭代

$$x_{n+1}=x_{n}+x_{n}(1-bx_{n})$$

假设 $x_{n}\equiv b^{-1}\pmod p$ 对于某个 $p$ 成立，那么 $x_{n}b\equiv 1+kp\pmod{p^{2}}$ 对于某个整数 $k$ 成立，那么

$$\begin{aligned}x_{n+1}&=x_{n}(2-bx_{n})\\
&\equiv x_{n}(2-(1+kp))\pmod{p^{2}}\\
&\equiv b^{-1}(1+kp)(1-kp)\pmod{p^{2}}\\
&\equiv b^{-1}(1-k^{2}p^{2})\pmod{p^{2}}\\
&\equiv b^{-1}\pmod{p^{2}}\end{aligned}$$

在这里我们只需将 $p$ 替换为 $2$ 即可。 $\square$

令 $x_{0}=1$ ，第一次迭代为 $x_{1}=x_{0}(2-Nx_{0})$ 这使我们发现 $x_{1}=2-N$ 而不论 $N\equiv 1\pmod{4}$ 或者 $N\equiv 3\pmod{4}$ 都有 $2-N\equiv N\pmod{4}$ 。这指导我们可以写出如下 C++ 代码

!!! note ""

    ```cpp
    u32 x = N * (2 - N * N);
    x *= 2 - N * x;
    x *= 2 - N * x;
    x *= 2 - N * x;
    N_p = -x;
    ```

来快速计算 $N'$ 。

## Hensel 除法

参考[^2]可以给出一个更广义的解释，一般的除法可以认为是消去高位，而 Hensel 除法消去低位。我们可以将一般的除法描述为 MSB （ most significant bit ）除法，而 Hensel 除法为 LSB （ least significant bit ）除法。对于 $A$ 除以 $B$ ，且 $A$ 为一个 $2n$ 字长的（用 $\beta$ 代表一个字长）， $B$ 为 $n$ 字长的。一般的除法商 $Q$ 和余 $R$ 满足 $A=QB+R$ 。而 Hensel 除法的 LSB-商 $Q'$ 和 LSB-余 $R'$ 则满足 $A=Q'B+R'\beta^{n}$ 。 LSB 除法也需要 $\gcd(B,\beta)=1$ （例如上述的 $\beta=2$ 且 $B$ 为奇数）因为 LSB-商被唯一定义为 $Q'=A/B\bmod{\beta^{n}}$ ，其中 $0\leq Q'\lt \beta^{n}$ 。这也唯一定义了 LSB-余 $R'=(A-Q'B)\beta^{-n}$ 其中 $-B\lt R'\lt \beta^{n}$ 。而当仅想要计算余数时， Hensel 除法 也就是我们理解的 Montgomery reduction 。

这里再简要说明一下，例如一般除法可以计算 $A\bmod{B}=QB+R\bmod{B}=R$ ，而 Hensel 除法计算 $A\bmod{B}=Q'B+R'\beta^{n}\bmod{B}=R'\beta^{n}\bmod{B}$ 。那么可以用 $A(\beta^{n}\bmod{B})$ 替代 $A$ 即可。这也是为什么会使用 Montgomery form 保存一个数，直到最后需要时再转换回来。

!!! warning "LSB 与 MSB 的引入"

    这种思想的引入是重要的[^2]，因为一些 MSB 算法存在着对应的 LSB 算法，应用及效率也可能不同，某种程度上是否可以理解为“转置”呢？
    
    | classical (MSB) | $p$-adic (LSB) |
    |:-:|:-:|
    | Euclidean division | Hensel division, Montgomery reduction |
    | Svoboda's algorithm | Montgomery-Svoboda |
    | Euclidean gcd | binary gcd |
    | Newton's method | Hensel lifting |

[^1]: Peter L. Montgomery. Modular Multiplication Without Trial Division, 1985.
[^2]: Richard P. Brent and Paul Zimmermann, Modern Computer Arithmetic, Cambridge Monographs on Computational and Applied Mathematics (No. 18), Cambridge University Press, November 2010, 236 pages
