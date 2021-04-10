这里主要是学习了一下多点求值的算法和插值的算法。我还不会转置的算法，转置算法可以参考 [EntropyIncreaser 的洛谷博客](https://www.luogu.com.cn/blog/EntropyIncreaser/solution-p5050) 。

假设 $\deg(0)=-\infty$ 且一切多项式运算都在有限域多项式环 $\mathbb{F}_p[x]$ 上进行，其中 $p$ 为素数。所给点都属于 $\mathbb{F}_{p}$ 。

## 霍纳法则

如果我们需要在单个点 $x_{0}$ 求得多项式 $A(x)$ 的值 $A(x_{0})$ ，那么可以在线性时间内做到，若 $A(x)=\sum_{0\leq i\lt m}a_{i}x^{i}$ ，那么 $A(x_{0})=(\cdots (((a_{m-1}x_{0})+a_{m-2})x_{0}+a_{m-3})x_{0}+\cdots )x_{0}+a_{0}$ 即可，这被称为霍纳法则。

## 传统的多点求值算法

传统的多点求值算法对于 $m$ 个点的集合 $b=\{x_{0},x_{1},\dots ,x_{m-1}\}$ ，考虑构造一棵 subproduct 树（一些论文中也称为 moduli 树）。对于树 $T$ 的叶节点为 $x-x_{j}$ 其中 $j\in\{0,1,\dots, m-1\}$ ，而非叶节点则为孩子节点的乘积（这里不用给出明确的定义，因为我们可以用线段树的方式去构造）。将自底向上构造 subproduct 树的过程称为 uptree 。

而对于多项式 $A(x)$ 在 $b$ 处求值即求 $(A(x_{0}),A(x_{1}),\dots ,A(x_{m-1}))$ ，可以在 subproduct 树自顶向下做多项式取模（余），因为 $A(x_{0})=A(x)\bmod (x-x_{0})$ 且若 $B(x)\mid C(x)$ 那么 $A(x)\bmod B(x)=(A(x)\bmod C(x))\bmod B(x)$ 这一过程称为 downtree 。当递归到叶节点时我们得到了解。

参考[^1]p299 ，如果我们假设 $\deg(A(x))$ 与 $b$ 的大小为同一个级别，那么时间为 $O(m\log^2m)$ 。

## 增量的插值算法

如果考虑中国剩余定理，假设对于多项式 $A(x)$ ，已知 $A(x)$ 经过 $k$ 组点对 $(x_{i},y_{i})$ 其中 $i\in\{0,\dots ,k-1\}$ 且对于 $i\neq j$ 有 $x_{i}\neq x_{j}$ 且 $\deg(A(x))\lt k$ ，我们希望向 $A(x)$ 经过的点对集合中加一组点对 $(x_{k},y_{k})$ 且 $\forall i\in\{0,\dots ,k-1\}$ 有 $x_{k}\neq x_{i}$ 并修改 $A(x)$ 使其经过集合中所有的点对。记修改后为 $A'(x)$ 那么只需考虑

$$\begin{cases}
A'(x)\bmod \prod_{i=0}^{k-1}(x-x_{i})=A(x)\\
A'(x)\bmod (x-x_{k})=y_{k}
\end{cases}$$

那么假设存在 $S(x),T(x)$ 满足

$$S(x)\prod_{i=0}^{k-1}(x-x_{i})+A(x)=T(x)(x-x_{k})+y_{k}$$

$$S(x)\prod_{i=0}^{k-1}(x_{k}-x_{i})+A(x_{k})\equiv y_{k}\pmod{(x-x_{k})}$$

那么求出 $S(x)$ 代入即能求得答案，这样的时间是 $O(k^{2})$ 的。但如果我们从一开始点集为空开始维护乘积，那么添加 $k$ 次的总时间为 $O(k^{2})$ 。

这也指导我们可以用扩展欧几里得算法来合并多个多项式的同余式，且可能存在有更快的算法。回顾中国剩余定理合并关于 $x$ 的同余方程如

$$\begin{cases}
x\equiv a_1\pmod{n_1}\\
x\equiv a_2\pmod{n_2}\\
\vdots \\
x\equiv a_k\pmod{n_k}
\end{cases}$$

当然这里我们假设 $\gcd(n_i,n_j)=1,\forall i\neq j$ ，令 $n=\prod_{1\leq i\leq k}n_i$ 那么

$$x\equiv \sum_{1\leq i\leq k}a_iN_iM_i\pmod{n},\quad N_i=n/n_i,\quad M_i=N_i^{-1}\bmod{n_i}$$

观察到其正确性很显然，即

$$\sum_{1\leq j\leq k}a_jN_jM_j\equiv a_i+\sum_{1\leq j\leq k,j\neq i}a_jN_jM_j\pmod{n_i}$$

而后面的和式中的 $N_j$ 显然为 $n_i$ 的倍数那么后面的和式在模 $n_i$ 意义下同余零。

这样的中国剩余定理当然也能推广到有限域多项式。但个人以为两两合并更简单快速。

!!! note "例题 [拉格朗日插值](https://loj.ac/p/165)"

    上述方法两两合并同余式即可。

## 拉格朗日插值

!!! quote "拉格朗日插值公式"

    对于点集 $\{(x_{i},y_{i})\}$ 其中 $i\in\{0,\dots ,k-1\}$ 且对于 $\forall i\neq j$ 有 $x_{i}\neq x_{j}$ ，拉格朗日插值公式为

    $$A(x)=\sum_{i=0}^{k-1}y_{i}\prod_{j\neq i}\frac{x-x_{j}}{x_{i}-x_{j}}$$

    其中 $A(x)$ 满足 $A(x_i)=y_i$ 对于 $\forall i\in\{0,\dots ,k-1\}$ 都成立。

    ??? note "不严谨的证明"

        拉格朗日插值公式就是中国剩余定理应用于多项式上的结果，考虑合并下列同余方程组：

        $$\begin{cases}
        A(x)\equiv y_0\pmod{(x-x_0)}\\
        A(x)\equiv y_1\pmod{(x-x_1)}\\
        \vdots \\
        A(x)\equiv y_{k-1}\pmod{(x-x_{k-1})}
        \end{cases}$$

        我们也假设对于 $\forall i\neq j$ 有 $x_i\neq x_j$ 且 $A(x)\bmod{(x-a)}=A(a)$ 也很显然。

        设 $N(x)=\prod_{i=0}^{k-1}(x-x_i)$ 和 $N_{i}(x)=N(x)/(x-x_i)$ 及 $M_{i}(x)=N_{i}^{-1}(x)\bmod{(x-x_i)}$ 及

        $$A(x)\equiv \sum_{i=0}^{k-1}y_iN_i(x)M_i(x)\pmod{N(x)}$$

        对于任一 $i$ 有

        $$\sum_{j=0}^{k-1}y_jN_j(x)M_j(x)\equiv y_i+\sum_{0\leq j\lt k,j\neq i}y_jN_j(x)M_j(x)\pmod{(x-x_i)}$$

        后一个和式中显然 $N_j(x)$ 都是 $x-x_i$ 的倍式，那么 $N_j(x)\equiv 0\pmod{(x-x_i)}$ ，也就是都能满足 $A(x_i)=y_i$ 。

        稍加整理得到了

        $$A(x)\equiv \sum_{i=0}^{k-1}y_i\frac{\prod_{j\neq i}(x-x_j)}{\prod_{j\neq i}(x_i-x_j)}\pmod{N(x)}$$

        和公式一致，但是公式省略了后面的模运算和同余符号。 $\square$

设 $M(x)=\prod_{i=0}^{k-1}(x-x_{i})$ ， $s_{i}=\prod_{j\neq i}\frac{1}{x_{i}-x_{j}}$ ，那么我们可以将 $A(x)$ 表示为

$$A(x)=\sum_{i=0}^{k-1}y_{i}s_{i}\frac{M(x)}{x-x_{i}}$$

观察到 $M(x)$ 的导数 $M'(x)=\sum_{i=0}^{k-1}\frac{M(x)}{x-x_{i}}$ 好像无关紧要，只需注意到

$$M'(x_{i})=\lim_{x\to x_{i}}\frac{M(x)-M(x_{i})}{x-x_{i}}=\lim_{x\to x_{i}}\frac{M(x)}{x-x_{i}}=\frac{1}{s_{i}}$$

因此可以通过多点求值来求 $s_{i}$ （加上 $k$ 次的倒数运算）。设 $M_{0}(x)=\prod_{i=0}^{l-1}(x-x_{i})$ ， $M_{1}(x)=\prod_{i=l}^{k-1}(x-x_{i})$  ， $A_{0}(x)=\sum_{i=0}^{l-1}y_{i}s_{i}\frac{M_{0}(x)}{x-x_{i}}$ ， $A_{1}(x)=\sum_{i=l}^{k-1}y_{i}s_{i}\frac{M_{1}(x)}{x-x_{i}}$ ，那么

$$A(x)=A_{0}(x)M_{1}(x)+A_{1}(x)M_{0}(x)$$

叶节点时直接返回 $y_{i}s_{i}$ 分治即可。

!!! note "例题 [P5158 【模板】多项式快速插值](https://www.luogu.com.cn/problem/P5158)"

    上述分治可以通过，但有常数更优秀的算法，即转置算法。

[^1]: J. von zur Gathen and J. Gerhard. Modern computer algebra. Cambridge University Press, 1999.
