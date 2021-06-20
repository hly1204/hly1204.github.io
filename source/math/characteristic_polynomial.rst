:Date: 2021-1-6
:Author: hly1204

===================
特征多项式
===================

特征多项式的定义
----------------------
对于矩阵 :math:`\mathbf{A}\in\mathbb{C}^{n\times n}` ，我们说 :math:`\mathbf{A}` 的特征多项式 [#char]_ 为

.. math::
   p(\lambda)=\det(\lambda \mathbf{I}-\mathbf{A})=\lambda ^{n}+c_{1}\lambda ^{n-1}+\cdots +c_{n-1}\lambda +c_{n}

其中 :math:`\mathbf{I}\in\mathbb{C}^{n\times n}` 为一个单位矩阵， :math:`c_{1}=-\operatorname{trace}(\mathbf{A})` 且 :math:`c_{n}=(-1)^n\det(\mathbf{A})` 写成行列式形式即

.. math::
   p(\lambda)=
   \begin{vmatrix}
   \lambda -a_{11}&-a_{12}&-a_{13}&\cdots & -a_{1(n-1)}&-a_{1n}

   -a_{21}&\lambda -a_{22}&-a_{23}&\cdots & -a_{2(n-1)}&-a_{2n}

   -a_{31}&-a_{32}&\lambda -a_{33}&\cdots & -a_{3(n-1)}&-a_{3n}

   \vdots & \vdots & \vdots & \ddots & \vdots & \vdots

   -a_{(n-1)1}&-a_{(n-1)2}&-a_{(n-1)3}&\cdots & \lambda -a_{(n-1)(n-1)}&-a_{(n-1)n}

   -a_{n1}&-a_{n2}&-a_{n3}&\cdots & -a_{n(n-1)}&\lambda -a_{nn}
   \end{vmatrix}

.. note::
   注意到有的地方定义特征多项式为 :math:`p(\lambda)=\det(\mathbf{A}-\lambda \mathbf{I})` 没有本质区别，但我们使用上述定义，因为得到的多项式一定为首一的 [#mon]_ 。

.. rubric:: 脚注

.. [#mon] monic
.. [#char] characteristic polynomial

Cayley-Hamilton 定理
----------------------
对于上述定义中的 :math:`\mathbf{A}` 和其特征多项式 :math:`p(\lambda )` 有

.. math::
   p(\mathbf{A})&=\mathbf{A}^n+c_1\mathbf{A}^{n-1}+\cdots +c_{n-1}\mathbf{A}+c_n\mathbf{I}

   &=\mathbf{O}

其中 :math:`\mathbf{O}\in\mathbb{C}^{n\times n}` 为零矩阵，可简写为 :math:`0` 。

所以特征多项式也是零化多项式。而零化多项式中次数最小的首一多项式为其最小多项式。

.. note::
   特征多项式不是唯一的零化多项式 [#zero]_ ，最小多项式 [#min]_ 一定是特征多项式的因式。

.. rubric:: 脚注

.. [#zero] annihilating polynomial
.. [#min] minimal polynomial

矩阵的逆元
------------------------
对于上述定义中的矩阵，一般我们用 Gauss-Jordan 消元法对分块矩阵 :math:`\begin{bmatrix}\mathbf{A}&\mathbf{I}\end{bmatrix}` 进行初等变换得到 :math:`\begin{bmatrix}\mathbf{I}&\mathbf{A}^{-1}\end{bmatrix}` 则得到了一个解。

上述 Cayley-Hamilton 定理也提示我们一种额外的方法。对于上述矩阵 :math:`\mathbf{A}` 有

.. math::
   \mathbf{A}^n+c_1\mathbf{A}^{n-1}+\cdots +c_{n-1}\mathbf{A}+c_n\mathbf{I}=0

   \implies
   -c_n\mathbf{I}=\mathbf{A}^n+c_1\mathbf{A}^{n-1}+\cdots +c_{n-1}\mathbf{A}

   \implies
   -c_n\mathbf{A}^{-1}=\mathbf{A}^{n-1}+c_1\mathbf{A}^{n-2}+\cdots +c_{n-1}\mathbf{I}

而矩阵的逆元存在 iff 其行列式不为零，这里 :math:`(-1)^nc_n=\det(\mathbf{A})` 。

LeVerrier 方法
----------------------
第一个实用的计算特征多项式的方法是由 LeVerrier 在 1840 年提出的，基于 Newton 恒等式 [#newton]_ 。

.. math::
   c_1&=-\operatorname{trace}(\mathbf{A}),

   c_k&=-\frac{1}{k}\operatorname{trace}(\mathbf{A}^k+c_1\mathbf{A}^{k-1}+\cdots +c_{k-1}\mathbf{A}),\quad 2\leq k\leq n

其中 Newton 恒等式可以用递归的方式表示如

.. math::
   c_k=-\frac{1}{k}\operatorname{trace}(\mathbf{A}\mathbf{B}_{k-1}),
   \quad \text{where}\quad \mathbf{B}_1=\mathbf{A}+c_1\mathbf{I},
   \quad \mathbf{B}_k=\mathbf{A}\mathbf{B}_{k-1}+c_k\mathbf{I}

其证明可以参考 `wiki`_ ，我们直接实现该算法的时间是 :math:`O(n^4)` 。

.. _wiki: https://en.wikipedia.org/wiki/Faddeev%E2%80%93LeVerrier_algorithm

.. rubric:: 脚注

.. [#newton] Newton's identities 

相似变换
----------------------
设矩阵 :math:`\mathbf{A}\in\mathbb{C}^{n\times n}` ，我们说 :math:`\mathbf{A}'` 与 :math:`\mathbf{A}` 相似当 :math:`\mathbf{A}'` 可被写作

.. math:: \mathbf{A}'=\mathbf{PA}\mathbf{P}^{-1}

其中 :math:`\mathbf{A}',\mathbf{P},\mathbf{P}^{-1}\in\mathbb{C}^{n\times n}` ，此时 :math:`\mathbf{A'}` 与 :math:`\mathbf{A}`
有相同的特征多项式和行列式，行列式的证明只需考虑 :math:`\begin{cases}\vert \mathbf{AB}\vert =\vert \mathbf{A} \vert \vert \mathbf{B} \vert \\\vert \mathbf{B}^{-1}\vert=\vert \mathbf{B}\vert ^{-1}\end{cases}` ，而对于特征多项式，有

.. math::
   \vert \lambda \mathbf{I}-\mathbf{A}'\vert &=\vert \lambda \mathbf{I}-\mathbf{PA}\mathbf{P}^{-1}\vert

   &=\vert \mathbf{P}\lambda\mathbf{I}\mathbf{P}^{-1}-\mathbf{PA}\mathbf{P}^{-1}\vert

   &=\vert \mathbf{P}(\lambda\mathbf{I}\mathbf{P}^{-1}-\mathbf{A}\mathbf{P}^{-1})\vert

   &=\vert \mathbf{P}\vert \vert \lambda\mathbf{I}-\mathbf{A}\vert \vert \mathbf{P}^{-1} \vert

   &=\vert \lambda \mathbf{I}-\mathbf{A}\vert

虽然矩阵乘法没有交换律，但是其行列式有，另外 :math:`\mathbf{A}'=\mathbf{P}^{-1}\mathbf{AP}` 是一样的。

像这样由 :math:`\mathbf{A}` 到 :math:`\mathbf{A}'` 的变换我们称为相似变换 [#sim]_ 。

.. rubric:: 脚注

.. [#sim] similarity transformation

La Budde 方法 [#ref1]_ 
----------------------
上 Hessenberg 矩阵
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
上 Hessenberg 矩阵 :math:`\mathbf{H}\in\mathbb{C}^{n\times n},n\gt 2` 是形如

.. math::
   \mathbf{H}=
   \begin{bmatrix}
   \alpha_{1}&h_{12}&\dots&\dots&h_{1n}

   \beta_{2}&\alpha_{2}&h_{23}&&\vdots

   &\ddots &\ddots & \ddots &\vdots

   & &\ddots &\ddots & h_{(n-1)n}

   &&& \beta_{n}& \alpha_{n}
   \end{bmatrix}

的矩阵。其中 :math:`\beta` 形成的对角线我们称为次对角线 [#subdiag]_ 。

.. rubric:: 脚注

.. [#subdiag] subdiagonal

---------------

La Budde 方法可用来在 :math:`O(n^3)` 计算矩阵 :math:`\mathbf{A}` 的特征多项式，其分为两个步骤。

1. 将 :math:`\mathbf{A}` 进行（正交）相似变换为上 Hessenberg 矩阵 :math:`\mathbf{H}` 。
2. 计算连续主子矩阵 :math:`\mathbf{H}_i` [#leadprin]_ 的特征多项式。

我们令 :math:`p_0(\lambda)=1` 且 :math:`\mathbf{I}_k` 表示 :math:`k\times k` 的单位矩阵，有

.. math::
   \mathbf{H}_1=
   \begin{bmatrix}
   \alpha_1
   \end{bmatrix},\quad
   p_1(\lambda)=\det(\lambda \mathbf{I_1}-\mathbf{H}_1)=\lambda -\alpha_1

.. math::
   \mathbf{H}_2=
   \begin{bmatrix}
   \alpha_1&h_{12}

   \beta_2&\alpha_2
   \end{bmatrix},\quad
   p_2(\lambda)=\det(\lambda\mathbf{I}-\mathbf{H}_2)=(\lambda-\alpha_2)p_1(\lambda)-\beta_2h_{12}p_0(\lambda)

在计算行列式时我们一般选择按零最多的行或列余子式展开 [#cofacexp]_ ，所谓余子式即删除了当前选择的元素所在行和列之后的矩阵，在这里我们选择按最后一行进行展开，有

.. math::
   p_3(\lambda)&=
   \det(\lambda\mathbf{I}_3-\mathbf{H}_3)
   
   &=\begin{vmatrix}
   \lambda-\alpha_1&-h_{12}&-h_{13}

   -\beta_2&\lambda-\alpha_2&-h_{23}

   &-\beta_3&\lambda-\alpha_3
   \end{vmatrix}

   &=(\lambda-\alpha_3)\cdot (-1)^{3+3}p_2(\lambda)-\beta_3\cdot (-1)^{3+2}
   \begin{vmatrix}
   \lambda-\alpha_1&-h_{13}

   -\beta_2&-h_{23}
   \end{vmatrix}

   &=(\lambda-\alpha_3)p_2(\lambda)-\beta_3(h_{23}p_1(\lambda)+\beta_2h_{13}p_0(\lambda))

观察后发现，对于 :math:`2\leq i\leq n` 有

.. math::
   p_i(\lambda)=(\lambda-\alpha_i)p_{i-1}(\lambda)-
   \sum_{m=1}^{i-1}h_{i-m,i}
   \left(
   \prod_{j=i-m+1}^{i}\beta_j
   \right)
   p_{i-m-1}(\lambda)

直接计算上式消耗 :math:`O(n^3)` 的时间。若该上 Hessenberg 矩阵还是三对角矩阵 [#tri]_ ，我们有更快的算法 [#ref1]_ 。

.. note::
   :math:`0\times 0` 矩阵的行列式为 :math:`1` 是 well-defined 的，并不是特殊情况。谢谢 hos\-lyric 指出这点！

.. rubric:: 脚注

.. [#ref1] Rizwana Rehman, Ilse C.F. Ipsen. `La Budde's Method for Computing Characteristic Polynomials <https://ipsen.math.ncsu.edu/ps/charpoly3.pdf>`_.
.. [#leadprin] leading principal submatrix :math:`\mathbf{H}_i` 指只保留前 :math:`i` 行和列的子矩阵
.. [#cofacexp] cofactor expansion 
.. [#tri] tridiagonal matrix

用 Gauss 消元作相似变换
----------------------------
一般 La Budde 方法使用 Hessenberg 分解，即 Householder 矩阵来进行正交相似变换 [#ref2]_ ，其具有数值稳定性，但为了简便我们使用 Gauss 消元法 [#ref3]_ 。

一般的高斯消元并不是直接的相似变换，我们在这里假设只作行变换，也就是

1. 将第 :math:`i` 行的 :math:`k` 倍加到第 :math:`j` 行，其中 :math:`i\neq j` 且 :math:`k\neq 0` 。
2. 交换两行。
3. 将第 :math:`i` 行乘以 :math:`k` 倍。

令 :math:`\mathbf{M}_{ab}` 表示矩阵 :math:`\mathbf{M}` 第 :math:`a` 行，第 :math:`b` 列的元素。

第一个操作其等价于左乘了一个形如 :math:`\mathbf{I}_n+\mathbf{M}` 的矩阵，其中 :math:`\mathbf{M}_{ij}=k` 其余都为零，我们右乘他的逆即 :math:`\mathbf{I}_n-\mathbf{M}` 即可。

第二个操作作用于矩阵 :math:`\mathbf{A}` 等价于使其左乘一个排列矩阵（即单位矩阵交换了对应两行），而排列矩阵的逆为其自身，我们右乘他即交换对应的两列，这个操作也用来选主元。

.. note::
   我们只对次对角线以下的部分作上述变换。

.. rubric:: 脚注

.. [#ref2] G\. H\. Golub and C\. F\. Van Loan, Matrix Computations, The Johns Hopkins University Press, Baltimore, third ed., 1996.
.. [#ref3] `Reduction of a General Matrix to Hessenberg Form <http://www.phys.uri.edu/nigh/NumRec/bookfpdf/f11-5.pdf>`_.

常系数齐次线性递推
-----------------------------
我们关注这样一个常系数齐次线性递推序列（简称递推序列）如

.. math::
   u_{n+d}=c_{d-1}u_{n+d-1}+\cdots +c_0u_n,\quad n\geq 0

我们说这样一个递推是 :math:`d` 阶的。对于 :math:`N\geq 0` ，求 :math:`u_N` 最简单的处理方式是将其转换为矩阵的形式如：

.. math::
   \underbrace{
   \begin{bmatrix}
   u_{n}
   
   u_{n+1}
   
   \vdots
   
   u_{n+d-1}
   \end{bmatrix}
   }_{\mathbf{v}_{n}}=
   \underbrace{
   \begin{bmatrix}
   &1&&

   &&\ddots&

   &&&1

   c_{0}&c_{1}&\cdots&c_{d-1}
   \end{bmatrix}
   }_{\mathbf{M}}\times
   \underbrace{
   \begin{bmatrix}
   u_{n-1}
   
   u_{n}
   
   \vdots
   
   u_{n+d-2}
   \end{bmatrix}
   }_{\mathbf{v}_{n-1}},\quad n\geq 1

若这个递推序列是在 :math:`\mathbb{R}` 上，不难发现在 :math:`\mathbb{R}^{d\times d}` 上关于 :math:`\mathbf{v}` 这个向量的递推阶为一，通常采用的方法是矩阵快速幂。

发现 :math:`\mathbf{v}` 可以描述成一个线性组合为

.. math:: \mathbf{v}_{n+d}=\sum_{i=0}^{d-1}c_i\mathbf{v}_{n+i}

进一步的可以写成

.. math:: \mathbf{M}^d\mathbf{v}_n=\sum_{i=0}^{d-1}c_i\mathbf{M}^i\mathbf{v}_n

我们可以找到一个多项式 :math:`\Gamma(x)=x^d-\sum_{i=0}^{d-1}c_ix^i` 满足 :math:`\Gamma(\mathbf{M})=0` 。

令 :math:`g(x)=g_0+g_1x+\cdots +g_{d-1}x^{d-1}=x^N\bmod{\Gamma(x)}` 那么 :math:`g(\mathbf{M})=\mathbf{M}^N` ，也就是我们将 :math:`\mathbf{v}_N` 描述为了一个线性组合如

.. math::
   \mathbf{M}^N\mathbf{v}_0=\sum_{i=0}^{d-1}g_i\mathbf{M}^i\mathbf{v}_0\iff \mathbf{v}_N=\sum_{i=0}^{d-1}g_i\mathbf{v}_i

观察 :math:`\mathbf{v}_i` 的第一行我们不难得出答案。这被称为 Fiduccia 算法。

上述 :math:`\Gamma(\lambda)=\det(\lambda \mathbf{I}_d-\mathbf{M})` 也就是其特征多项式。

我们不难将矩阵的特征多项式与线性递推联系起来 [#mori]_ 以及得到更快求矩阵幂次的算法 [#mike]_ ，而求出矩阵的最小多项式我们可以采用随机化的 Berlekamp-Massey 算法。

.. rubric:: 脚注

.. [#mori] Alin Bostan, Ryuhei Mori. `A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence <https://arxiv.org/abs/2008.08822>`_.
.. [#mike] Mike Paterson. `On the Number of Nonscalar Multiplications Necessary to Evaluate Polynomials <https://www.researchgate.net/publication/220617048_On_the_Number_of_Nonscalar_Multiplications_Necessary_to_Evaluate_Polynomials>`_.

Berkowitz 方法 [#marsh]_
----------------------------------
这是一种没有除法的计算特征多项式的算法，但在这里不会被提及。

+------------+----------------+--------+---------------+
| 算法       | 时间           | 适用   | 评论          |
+============+================+========+===============+
| Berkowitz  | :math:`O(n^4)` | 交换环 | 矩阵-向量乘法 |
|            |                |        |               |
|            |                |        | 无除法        |
+------------+----------------+--------+---------------+
| Hessenberg | :math:`O(n^3)` | 域     | 分解、递推    |
|            |                |        |               |
|            |                |        | 一些除法      |
+------------+----------------+--------+---------------+

.. rubric:: 脚注

.. [#marsh] Marshall Law. `Computing Characteristic Polynomials of Matrices of Structured Polynomials <http://summit.sfu.ca/system/files/iritems1/17301/etd10125_.pdf>`_.