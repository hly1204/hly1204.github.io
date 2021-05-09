重新学习了一下线性递推，叉姐的 PPT 的解释感觉非常漂亮。

## 常系数齐次线性递推序列

我们关注这样一个常系数齐次线性递推序列（下简称递推序列）如

$$u_{n+d}=c_{d-1}u_{n+d-1}+\cdots +c_0u_n,\quad n\geq 0$$

我们说这样一个递推是 $d$ 阶的。对于 $N\geq 0$ ，求 $u_N$ 最简便的处理方式是将其转换为矩阵的形式如：

$$\underbrace{\begin{bmatrix}
u_{n}\\u_{n+1}\\\vdots\\u_{n+d-1}
\end{bmatrix}}_{\mathbf{v}_{n}}=\underbrace{\begin{bmatrix}
&1&&\\
&&\ddots&\\
&&&1\\
c_{0}&c_{1}&\cdots&c_{d-1}
\end{bmatrix}}_{\mathbf{M}}\times\underbrace{\begin{bmatrix}
u_{n-1}\\u_{n}\\\vdots\\u_{n+d-2}
\end{bmatrix}}_{\mathbf{v}_{n-1}},\quad n\geq 1$$

若这个递推序列是在 $\mathbb{R}$ 上，不难发现在 $\mathbb{R}^{d\times d}$ 上关于 $\mathbf{v}$ 这个向量的递推阶为 $1$ ，通常采用的方法是矩阵快速幂。

不难发现 $\mathbf{v}$ 可以描述成一个线性组合为

$$\mathbf{v}_{n+d}=\sum_{i=0}^{d-1}c_i\mathbf{v}_{n+i}$$

进一步的可以写成

$$\mathbf{M}^d\mathbf{v}_n=\sum_{i=0}^{d-1}c_i\mathbf{M}^i\mathbf{v}_n$$

我们可以找到一个多项式 $\Gamma(x)=x^d-\sum_{i=0}^{d-1}c_ix^i$ 满足 $\Gamma(\mathbf{M})=0$ 。

令 $g(x)=g_0+g_1x+\cdots +g_{d-1}x^{d-1}=x^N\bmod{\Gamma(x)}$ 那么 $g(\mathbf{M})=\mathbf{M}^N$ ，也就是我们将 $\mathbf{M}^N$ 描述为了一个线性组合如

$$\mathbf{M}^N\mathbf{v}_0=\sum_{i=0}^{d-1}g_i\mathbf{M}^i\mathbf{v}_0\implies \mathbf{v}_N=\sum_{i=0}^{d-1}g_i\mathbf{v}_i$$

观察 $\mathbf{v}_i$ 的第一行我们不难得出答案。

!!! note "可能的优化"
    
    计算 $x^N\bmod{\Gamma(x)}$ 不难让我们联想到计算模奇素数平方根的 Cipolla 算法，其实质也为一个二阶的递推，这里我们是否可以利用 Montgomery reduction 的思想进行一些优化呢，毕竟只需要其余数。

## 新的算法

学习论文[^1]与[^2]中的解读后我们得到了一个常数更小的实现且无需直接的幂级数倒数算法和多项式取模，实现更为简便。我们将递推序列使用生成函数表示如

$$F(x)=\sum_{n\geq 0}u_nx^n$$

且令 $Q(x)=1-c_{d-1}x-\cdots -c_0x^d$ 为 $\Gamma(x)$ 系数翻转后的多项式，那么能找到一个多项式 $P(x)$ 满足

$$F(x)=\frac{P(x)}{Q(x)}$$

注意这里 $F(x)$ 为形式幂级数而 $P(x)$ 和 $Q(x)$ 为多项式。而 $F(x)$ 的前 $d$ 项和 $Q(x)$ 都是已知的，我们观察求 $P(x)$ 的过程有

$$P(x)=Q(x)F(x)$$

而其中

$$[x^n]\left(Q(x)F(x)\right)=u_n-\sum_{i=1}^{d}c_{d-i}u_{n-i}=0, \quad n\geq d$$

也就是说虽然 $P(x)$ 是一个多项式而非形式幂级数，但有理函数 $P(x)/Q(x)$ 已经包含了 $F(x)$ 的所有信息！我们只需消耗一次多项式乘法就能得到 $P(x)$ 。

接下来我们考虑一个变形使得分母为一个偶函数且令 $V(x^2)=Q(x)Q(-x)$ 和 $U(x)=P(x)Q(-x)$ 并将 $U(x)$ 分为了两部分为 $U(x)=U_e(x^2)+x\cdot U_o(x^2)$ 下标 $e$ 表示 even 而 $o$ 表示 odd 。

$$F(x)=\frac{P(x)Q(-x)}{Q(x)Q(-x)}=\frac{U_e(x^2)}{V(x^2)}+x\cdot \frac{U_o(x^2)}{V(x^2)}$$

我们发现后式中这两个有理函数的展开中 $x$ 的奇数次幂的系数都是零，那么假设我们需要求 $[x^N]F(x)$ 则只需要递归到其中一侧

$$[x^N]F(x)=\begin{cases}[x^{N/2}]\frac{U_e(x)}{V(x)}&\text{if } N\bmod 2=0 \\
[x^{(N-1)/2}]\frac{U_o(x)}{V(x)}& \text{if }N\bmod 2=1\end{cases}$$

我们需要付出两次度数为 $d$ 的多项式乘法。

!!! note "更细致的优化"

    我们不维护这个有理函数的分子和分母“多项式的形式”，而是维护他们“ DFT 序列的形式”。依然考虑在 [快速傅里叶变换](4-10-2021-FFT.md) 中的算法，我们得到的结果是一个 $f(1),f(-1),f(\mathrm{i}),f(-\mathrm{i}),\dots$ 的一个序列，第一个与第二个，第三个与第四个都是多项式 $f$ 在互为相反数的两个点的点值。我们维护了 $Q(x)$ 的 DFT 序列，那么 $Q(-x)$ 的 DFT 序列无非就是两两交换这些点值！那么很容易求出 $V(x^2)$ 的 DFT 序列，而因为 $V(x^2)$ 是偶函数，那么问题是如何使其变成 $V(x)$ 的 DFT 序列。这依然可以通过观察 DFT 序列得到，因为 $V(\mathrm{i}^2)=V(-1)$ 那么只需要用在 $V(\mathrm{i})$ 位置的点值替代 $V(-1)$ 处的点值即可（因为现在 $V(-1)=V(1)$ 所以 $V(-1)$ 是“没有意义”的），以此类推。但是这样的问题是，该 DFT 序列的长度减少为原先的一半了，于是在这之前我们使用 Twisted FFT 带给我们的方法“倍长 $Q(x)$ 的 DFT 序列”即可，也同时得到了倍长后的 $Q(-x)$ 序列给下面的分子处理使用。

    分子的处理方法也是类似的，首先我们求出 $U(x)$ 的 DFT 序列，之前要倍长 $P(x)$ 的 DFT 序列。对于 $U_e(x^2)=(U(x)+U(-x))/2$ 对应到点值也是一样的计算，这个序列的长度也变为了原先的一半，但我们之前已经倍长过了，可以保留足够信息。

    而 $U_o(x^2)=(U(x)-U(-x))/2x$ 那么对于每个 $U(\zeta)$ 还需要调整为 $U(\zeta)/\zeta$ 。

    通过观察 FFT 算法的分治树也可以得到结论：多项式 $f$ 的 $n\gt \deg(f)$ 长 DFT 序列的和为 $nf(0)$ （可能需要一些证明）。

事实上上述优化在[^1]中有详细描述，但因为我们之前对 FFT 算法已经有过详细分析，不难自己推导出来，不需要借助原论文。

## LSB 与 MSB 算法

见[^1]中后文的详细分析，上面的算法为 LSB 算法，原文也提供了其 MSB 算法， EI 教了我 MSB 可以认为是上述算法的转置，而 MSB 常数稍大，但可以求出连续 $d$ 项以及加速最初的多项式取模的算法，我也并未深入阅读仅作了尝试的实现。从而也导出了一个更快的计算矩阵幂次的算法（我们寻找矩阵的特征多项式 $\Gamma(x)$ 并求出 $g(x)=x^N\bmod{\Gamma(x)}$ 后计算 $g(\mathbf{M})$ ，注意这里需要用 baby-step-giant-step 算法）。

## 新的幂级数倒数算法（ Graeffe 方法）

学习论文作者的博客[^3]中，若我们想求一个给定幂级数 $Q(x)\in \mathbb{R}[[x]]$ 的倒数

$$\frac{1}{Q(x)}\bmod{x^{2N}}$$

有

$$\begin{aligned}\frac{1}{Q(x)}\bmod{x^{2N}}&=Q(-x)\frac{1}{Q(x)Q(-x)}\bmod{x^{2N}}\\
&=Q(-x)\frac{1}{V(x^2)}\bmod{x^{2N}}\\
&=Q(-x)S(x^2)\bmod{x^{2N}}\end{aligned}$$

那么问题减少为了原先的一半，因为我们只需求出 $S(x)\equiv 1/V(x)\pmod{x^{N}}$ 。

[^1]: [Alin Bostan, Ryuhei Mori. A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence.](https://arxiv.org/abs/2008.08822)
[^2]: [EntropyIncreaser 的洛谷博客](https://www.luogu.com.cn/blog/EntropyIncreaser/solution-p4723)
[^3]: [線形漸化的数列のN項目の計算](https://qiita.com/ryuhe1/items/da5acbcce4ac1911f47a)
