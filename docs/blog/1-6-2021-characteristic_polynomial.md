学习了一下怎样求特征多项式，没有额外记号可以认为是 $n\times n$ 的方阵。
一般认为 $\deg(0)=-\infty$ 。

## 特征多项式的定义

!!! quote "定义"

    对于矩阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$ ，我们说 $\mathbf{A}$ 的特征多项式为

    $$
    p(\lambda)=\det(\lambda \mathbf{I}-\mathbf{A})=\lambda ^{n}+c_{1}\lambda ^{n-1}+\cdots +c_{n-1}\lambda +c_{n}
    $$

其中 $\mathbf{I}\in\mathbb{R}^{n\times n}$ 为一个单位矩阵， $c_{1}=-\operatorname{tr}(\mathbf{A})$ 且 $c_{n}=\det(\mathbf{A})$ （ $\operatorname{tr}(\mathbf{A})$ 为矩阵对角线元素的和，又称为矩阵的迹（ trace ）），写成行列式形式即

$$
p(\lambda)=
\begin{vmatrix}
\lambda -a_{11}&a_{12}&a_{13}&\cdots & a_{1(n-1)}&a_{1n}\\
a_{21}&\lambda -a_{22}&a_{23}&\cdots & a_{2(n-1)}&a_{2n}\\
a_{31}&a_{32}&\lambda -a_{33}&\cdots & a_{3(n-1)}&a_{3n}\\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots\\
a_{(n-1)1}&a_{(n-1)2}&a_{(n-1)3}&\cdots & \lambda -a_{(n-1)(n-1)}&a_{(n-1)n}\\
a_{n1}&a_{n2}&a_{n3}&\cdots & a_{n(n-1)}&\lambda -a_{nn}\\
\end{vmatrix}
$$

!!! note ""

    注意到有的地方定义特征多项式为 $p(\lambda)=\det(\mathbf{A}-\lambda \mathbf{I})$ 没有本质区别，但我们使用上述定义，因为得到的多项式一定为首一的。

## 相似变换

设矩阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$ ，我们说 $\mathbf{A}'$ 与 $\mathbf{A}$ 相似当 $\mathbf{A}'$ 可被写作

$$
\mathbf{A}'=\mathbf{PA}\mathbf{P}^{-1}
$$

其中 $\mathbf{A}',\mathbf{P},\mathbf{P}^{-1}\in\mathbb{R}^{n\times n}$ ，此时 $\mathbf{A'}$ 与 $\mathbf{A}$
有相同的特征多项式和行列式，行列式的证明很简单，只需考虑 $\begin{cases}\vert \mathbf{AB}\vert =\vert
\mathbf{A} \vert \vert \mathbf{B} \vert \\\vert \mathbf{B}^{-1}\vert=1/\vert \mathbf{B}\vert \end{cases}$
即可，而对于特征多项式，有

$$
\begin{aligned}
\vert \lambda \mathbf{I}-\mathbf{A}'\vert &=\vert \lambda \mathbf{I}-\mathbf{PA}\mathbf{P}^{-1}\vert \\
&=\vert \mathbf{P}\lambda\mathbf{I}\mathbf{P}^{-1}-\mathbf{PA}\mathbf{P}^{-1}\vert \\
&=\vert \mathbf{P}(\lambda\mathbf{I}\mathbf{P}^{-1}-\mathbf{A}\mathbf{P}^{-1})\vert \\
&=\vert \mathbf{P}\vert \vert \lambda\mathbf{I}-\mathbf{A}\vert \vert \mathbf{P}^{-1} \vert \\
&=\vert \lambda \mathbf{I}-\mathbf{A}\vert
\end{aligned}
$$

显然 $\mathbf{A}'=\mathbf{P}^{-1}\mathbf{AP}$ 是一样的。 $\square$ 

## 上海森堡矩阵

!!! quote "定义"

    对于上海森堡矩阵 $\mathbf{H}\in\mathbb{R}^{n\times n},n\gt 2$ 是形如

    $$
    \mathbf{H}=
    \begin{bmatrix}
    \alpha_{1}&h_{12}&\dots&\dots&h_{1n}\\
    \beta_{2}&\alpha_{2}&h_{23}&&\vdots \\
    &\ddots &\ddots & \ddots &\vdots \\
    & &\ddots &\ddots & h_{(n-1)n}\\
    &&& \beta_{n}& \alpha_{n}
    \end{bmatrix}
    $$

    的矩阵。

其中，如果 $\beta_{i}\neq 0$ 对于 $\forall i\in\{2,\dots ,n\}$ 成立，那么我们说这是一个 unreduced 的海森堡矩阵， $\beta_{i}$ 形成的对角线我们称为子对角线（ subdiagonal ）。

## La Budde 方法

如果我们想计算一个上海森堡矩阵的特征多项式，那要方便得多。在[^1]中指出 La Budde 方法为连续计算前面所有的主子矩阵（ leading principal submatrices ，这里指只保留前 $k$ 行和 $k$ 列的子矩阵） $\mathbf{H}_{i}$ 的特征多项式。

我们记 $\mathbf{H}_{i}$ 的特征多项式为 $p_{i}(\lambda)=\det(\lambda \mathbf{I}-\mathbf{H}_{i})$ 对于 $1\leq i\leq n$ ，其中 $p(\lambda)=p_{n}(\lambda)$ 这指导我们递归的计算

$$
p_{0}(\lambda)=1,\quad p_{1}(\lambda)=\lambda -\alpha_{1}
$$

$$
p_{i}(\lambda)=(\lambda -\alpha_{i})p_{i-1}(\lambda)-\sum_{m=1}^{i-1}h_{(i-m)i}\beta_{i}\beta_{i-1}\cdots\beta_{i-m+1}p_{i-m-1}(\lambda)
$$

对于 $2\leq i\leq n$ ，实际上计算的是 $\lambda \mathbf{I}-\mathbf{H}_{i}$ 行列式的最后一行的展开。注意到我们也可以从右下角的矩阵开始计算，然后按第一列展开，即与[^4]中的一致。

!!! quote "Householder 矩阵"

    令向量 $\mathbf{v}\in\mathbb{R}^{m}$ 为一个列向量，那么 $m\times m$ 的矩阵 $\mathbf{P}$ 具有以下形式

    $$
    \mathbf{P}=\mathbf{I}-\beta \mathbf{vv}^{\mathrm{T}},\quad \beta =\frac{2}{\mathbf{v}^{\mathrm{T}}\mathbf{v}}
    $$

    被称为 Householder 矩阵。更详细的可以参考 [Wolfram](https://mathworld.wolfram.com/HouseholderMatrix.html) 。


## 海森堡分解

在[^2]中 p378 对于 $\mathbf{A}\in\mathbb{R}^{n\times n}$ ，海森堡分解定义为

$$
\mathbf{U}_{0}^{\mathrm{T}}\mathbf{A}\mathbf{U}_{0}=\mathbf{H},\quad
\mathbf{U}_{0}^{\mathrm{T}}\mathbf{U}_{0}=\mathbf{I}
$$

其中 $\mathbf{U}_{0}$ 可由 Householder 矩阵 $\mathbf{P}_{1},\dots ,\mathbf{P}_{n-2}$ 的乘积来计算。其中 $\mathbf{P}_{k}$ 所扮演的角色为使得子对角线下方的第 $k$ 列变成零，例如

$$
\begin{bmatrix}
\times&\times&\times&\times&\times&\times\\
\times&\times&\times&\times&\times&\times\\
\times&\times&\times&\times&\times&\times\\
\times&\times&\times&\times&\times&\times\\
\times&\times&\times&\times&\times&\times\\
\times&\times&\times&\times&\times&\times\\
\end{bmatrix}
\mathbf{P_{1}}=
\begin{bmatrix}
\times&\times&\times&\times&\times&\times\\
\times&\times&\times&\times&\times&\times\\
0&\times&\times&\times&\times&\times\\
0&\times&\times&\times&\times&\times\\
0&\times&\times&\times&\times&\times\\
0&\times&\times&\times&\times&\times\\
\end{bmatrix}
$$

以此类推，那么最后得到了

$$
(\mathbf{P}_{1}\cdots \mathbf{P}_{k})^{\mathrm{T}}\mathbf{A}(\mathbf{P}_{1}\cdots \mathbf{P}_{k})=\mathbf{H}
$$

为一个海森堡矩阵，而证明我没有理解。[^2]中也提到这样的时间为 $O(n^{3})$ ，那么我们得到了整个算法。

## 高斯消元作为相似变换

只需对于一般的高斯消元稍作修改即可让其变成一个相似变换，我们只对主对角线下方进行选取主元以及交换操作，也就是说只会用主对角线下方的行去消去其他行，这大概是因为在后面“对称”的进行操作时保证不会影响到我们已经变成海森堡矩阵的前几列，对于一次行交换，我们也要交换对应的列，对于一次用 $j$ 行减去 $k$ 倍的 $i$ 行，我们也要加给 $i$ 列 $k$ 倍的 $j$ 列。

学过高斯消元的都知道行变换等价于左乘一个初等矩阵，交换两行相当于左乘一个排列矩阵，而排列矩阵的逆就是它的转置，于是我们右乘一个它的转置即交换对应的两列。而对于将一行加上另一行的倍数，例如对于 $2\times 2$ 的矩阵

$$
\begin{bmatrix}1&0\\k&1\end{bmatrix}
\begin{bmatrix}a&b\\c&d\end{bmatrix}
=
\begin{bmatrix}a&b\\c+ka&d+kb\end{bmatrix}
$$

发现 $\begin{bmatrix}1&0\\k&1\end{bmatrix}^{-1}=\begin{bmatrix}1&0\\-k&1\end{bmatrix}$ 也就是右乘这样一个矩阵，很容易发现这样做的高斯消元即为相似变换。更大的矩阵也是一样的。在[^5]可以找到一份伪代码及相关的解释。

!!! note "例题 [矩阵的特征多项式](https://acm.nflsoj.com/problem/333)"
    
    上述高斯消元及算法可在 $O(n^3)$ 的时间求出。

[^1]: Rizwana Rehman, Ilse C.F. Ipsen. [La Budde's Method for Computing Characteristic Polynomials](https://ipsen.math.ncsu.edu/ps/charpoly3.pdf).
[^2]: G. H. Golub and C. F. Van Loan, Matrix Computations, The Johns Hopkins University Press, Baltimore, third ed., 1996.
[^3]: J. H. Wilkinson, The Algebraic Eigenvalue Problem, Clarendon Press, Oxford, 1965. MR 32 #1894.
[^4]: <https://www.cnblogs.com/ywwyww/p/8522541.html>
[^5]: <http://www.phys.uri.edu/nigh/NumRec/bookfpdf/f11-5.pdf>