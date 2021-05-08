把中国剩余定理的代码补全。这里仅讨论 $\mathbb{Z}$ 。

## 两两合并

在 [这里](../../blog/12-23-2020-multipoint_evaluation_and_interpolation.md) 稍微讲了一些，对于整数也是一样的。考虑已知关于 $A$ 的同余方程组

$$\begin{cases}A\equiv a_1\pmod{M_1}\\A\equiv a_2\pmod{M_2}\end{cases}$$

若 $\gcd(M_1,M_2)=1$ 那么存在整数 $k_1,k_2$ 满足

$$A=a_1+k_1M_1=a_2+k_2M_2\implies a_1\equiv a_2+k_2M_2\pmod{M_1}$$

可用 [扩展欧几里得算法](extended_Euclidean_algorithm.md) 中的函数求出

$$k_2\equiv (a_1-a_2)M_2^{-1}\pmod{M_1}$$

代入 $k_2$ 在模 $M_1$ 下的值发现满足方程组，可求出 $A\bmod (M_1M_2)$ 。

!!! note "python 代码"

    ```python
    def crt2(a: int, m1: int, b: int, m2: int) -> (int, int):
        # m1 与 m2 互素
        # a >= 0 且 b >= 0
        a, b, x = a % m1, b % m2, inv_mod(m1, m2)
        return (m2 + b - a % m2) * x % m2 * m1 + a, m1 * m2
    ```

## 同时合并

见 [多点求值和插值](../../blog/12-23-2020-multipoint_evaluation_and_interpolation.md) 。

## Garner 算法

Garner 算法可以通过给出的一个模意义下的表示 $v(x)=(v_1,v_2,\dots,v_t)$ 快速确定 $x$ 其中 $0\leq x\lt M$ 且 $v_i=x\bmod m_i$ 其中 $m_1,m_2,\dots ,m_t$ 两两互素（证明略，稍作分析发现本质就是上述两两合并的方法，若前缀积不溢出可简单维护前缀积而不用第二层迭代）。

!!! note "Garner 算法实现 CRT"

    $$\begin{array}{ll}
    \textbf{INPUT}\text{: a positive integer }M=\prod_{i=1}^tm_i\gt 1\text{, with }\gcd(m_i,m_j)\text{ for all }i\neq j \\
    \text{ and modular representation }v(x)=(v_1,v_2,\dots ,v_t)\text{ of }x\text{ for the }m_i\text{.} \\
    \textbf{OUTPUT}\text{: the integer }x\text{ in radix }b\text{ representation.} \\
    \qquad \text{For }i\text{ from }2\text{ to }t\text{ do the following:} \\
    \qquad \qquad C_i\gets 1\text{.} \\
    \qquad \qquad \text{For }j\text{ from }1\text{ to }(i-1)\text{ do the following:} \\
    \qquad \qquad \qquad u\gets m_j^{-1}\bmod{m_i}\text{.} \\
    \qquad \qquad \qquad C_i\gets u\cdot C_i\bmod{m_i}\text{.} \\
    \qquad u\gets v_1, x\gets u\text{.} \\
    \qquad \text{For }i\text{ from }2\text{ to }t\text{ do the following:} \\
    \qquad \qquad u\gets (v_i-x)C_i\bmod{m_i}\text{.} \\
    \qquad \qquad x\gets x+u\cdot \prod_{j=1}^{i-1}m_j\text{.} \\
    \qquad \text{Return}(x)\text{.}
    \end{array}$$

!!! note "该算法的优势"

    传统的 CRT 算法需要对 $M$ 取模，而这里不需要，若 $M$ 固定，则前半部分可以当做预处理。

!!! note "两个模数时的特殊情况"

    可以发现和上述两两合并一样。

稍作修改可以使其保留精度的同时结果对一个小模数取模，但合并的时间和空间会增加（目前不知道是否有更好的方法），因为为了避免使用“大整数”类不得不计算对于每个前缀积的模每个小模数的情况，并维护后面过程中 $x$ 模 $m_i$ 的值。

!!! note "Garner 算法的修改"

    $$\begin{array}{ll}
    \textbf{INPUT}\text{: a positive integer }p\text{ and a positive integer }M=\prod_{i=1}^tm_i\gt 1\text{, with }\gcd(m_i,m_j)\text{ for all }i\neq j \\
    \text{ and modular representation }v(x)=(v_1,v_2,\dots ,v_t)\text{ of }x\text{ for the }m_i\text{.} \\
    \textbf{OUTPUT}\text{: }(x\bmod{M})\bmod{p}\text{.} \\
    \qquad \text{For }i\text{ from }2\text{ to }t\text{ do the following:} \\
    \qquad \qquad C_i\gets 1\text{.} \\
    \qquad \qquad \text{For }j\text{ from }1\text{ to }(i-1)\text{ do the following:} \\
    \qquad \qquad \qquad u\gets m_j^{-1}\bmod{m_i}\text{.} \\
    \qquad \qquad \qquad C_i\gets u\cdot C_i\bmod{m_i}\text{.} \\
    \qquad u\gets v_1, x\gets u\bmod{p}\text{.} \\
    \qquad \text{For }i\text{ from }2\text{ to }t\text{ do the following:} \\
    \qquad \qquad x_i\gets u\bmod{m_i}\text{.} \\
    \qquad \text{For }i\text{ from }2\text{ to }t\text{ do the following:} \\
    \qquad \qquad u\gets (v_i-x_i)C_i\bmod{m_i}\text{.} \\
    \qquad \qquad \text{For }k\text{ from }(i+1)\text{ to }t\text{ do the following:} \\
    \qquad \qquad \qquad x_k\gets \left(x_k+u\cdot \prod_{j=1}^{i-1}m_j\right)\bmod{m_k}\text{.} \\
    \qquad \qquad x\gets \left(x+u\cdot \prod_{j=1}^{i-1}m_j\right)\bmod{p}\text{.} \\
    \qquad \text{Return}(x)\text{.}
    \end{array}$$

实现后的代码可通过一些测试。

- [ ] 实现 Garner 算法合并不互素的同余方程并将结果对一个固定小模数取模

!!! warning "关联算法"

    不难发现所谓的一般的中国剩余定理算法（由高斯提出）也就是拉格朗日插值算法，我们可以称其为拉格朗日中国剩余算法（我也不明白为何不称为高斯算法），而 Garner 算法过程中也恰好给出了一个“混合模数”的表示，实际上就是牛顿插值算法，也称为牛顿中国剩余算法。

## 中国剩余定理的推广

上面的方法仅适用于模数互素的情况，否则我们依然考虑上述关于 $A$ 的同余方程组，此时令 $d=\gcd(M_1,M_2)$ 那么假设存在整数 $k_1,k_2$ 满足

$$A=k_1M_1+a_1=k_2M_2+a_2\implies k_1M_1-k_2M_2=a_2-a_1\tag{1}$$

我们用 [扩展欧几里得算法](extended_Euclidean_algorithm.md) 中的函数求出 $x,y$ 满足 $xM_1+yM_2=d$ 。

我们有

$$\begin{cases}k_1M_1/d\equiv (a_2-a_1)/d\pmod{(M_2/d)}\\xM_1/d\equiv 1\pmod{(M_2/d)}\end{cases}$$

那么

$$k_1\equiv x(a_2-a_1)/d\pmod{(M_2/d)}$$

!!! warning ""

    若 $d\nmid (a_2-a_1)$ 则无解，因为在 $(1)$ 中后一个等式左侧显然是 $d$ 的倍数，而右侧若不是则不满足 $k_1,k_2$ 为整数的假设。

可求出 $A\bmod{(M_1M_2/d)}$ 。

!!! note "python 代码"

    ```python
    def generalized_crt2(a: int, m1: int, b: int, m2: int) -> (int, int):
        # m1 和 m2 不必互素
        # a >= 0 且 b >= 0
        a, b = a % m1, b % m2
        d, x, y = exgcd(m1, m2)
        bma = b - a
        if bma % d != 0:
            return -1, -1
        t, y = m2 // d, bma // d
        res = x * y % t # 取模运算导致 res 在 python 中默认为非负的
        return res * m1 + a, m1 * t
    ```

[^1]: [Alfred J. Menezes, Paul C. van Oorschot and Scott A. Vanstone. Handbook of Applied Cryptography.](http://cacr.uwaterloo.ca/hac/)
