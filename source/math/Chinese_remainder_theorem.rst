:Date: 2021-6-5
:Author: hly1204

===================
中国剩余定理
===================

简介
------------------------
在 :math:`\mathbb{Z}` 中我们关注这样一个关于 :math:`x` 的线性同余方程组

.. math::
   :label: lineq

   \begin{cases}
   x\equiv x_1\pmod{m_1}

   x\equiv x_2\pmod{m_2}

   \vdots

   x\equiv x_n\pmod{m_n}
   \end{cases}

其中 :math:`\forall i\neq j` 有 :math:`\gcd(m_i,m_j)=1` 即两两互素，我们要求满足方程组的最小非负 :math:`x` 。

令 :math:`M=\prod_{1\leq i\leq n}m_i` 。

在抽象代数中我们经常将这个描述成一个映射如

.. math::
   x\bmod{M}\mapsto (x\bmod{m_1},x\bmod{m_2},\dots ,x\bmod{m_n})

也导出了环的同构即

.. math::
   \mathbb{Z}/M\mathbb{Z}
   \cong
   \mathbb{Z}/m_1\mathbb{Z}
   \times
   \mathbb{Z}/m_2\mathbb{Z}
   \times
   \cdots
   \times
   \mathbb{Z}/m_n\mathbb{Z}

这里的 :math:`\times` 符号为直积（或笛卡尔积）。

例如有集合 :math:`A` 和集合 :math:`B` 那么集合 :math:`A\times B=\{(a,b)\mid a\in A\land b\in B\}` 。

Euclid 算法
-----------------------
对于正整数 :math:`a` 和 :math:`b` 我们有 :math:`\gcd(a,b)=\gcd(b,a\bmod{b})` ，这也被称为辗转相除法，当情况为 :math:`\gcd(t,0)` 时得到了解 :math:`\gcd(a,b)=t` ，略。

扩展 Euclid 算法
-----------------------
假设要求关于 :math:`s` 和 :math:`t` 的不定方程的一组解满足 :math:`as+bt=\gcd(a,b)` 也可以使用 Euclid 算法，我们将上述算法使用矩阵描述有

.. math::
   \begin{bmatrix}
   b
   
   a\bmod b
   \end{bmatrix}
   =
   \begin{bmatrix}
   0&1
   
   1&-q
   \end{bmatrix}
   \begin{bmatrix}
   a
   
   b
   \end{bmatrix}

其中 :math:`q=\lfloor a/b\rfloor` ，向下取整符号适用范围有限，否则需要单独定义，一般也称为 Euclid 除法（或带余除法），在一些多项式中也会经常用到 Euclid 除法。

我们所要做的就是模拟矩阵乘法，不停左乘这样一个矩阵，而初始时为一个 :math:`2\times 2` 的单位矩阵，最后有

.. math::
   \begin{bmatrix}
   \gcd(a,b)
   
   0
   \end{bmatrix}
   =
   \begin{bmatrix}
   x_1&x_2
   
   x_3&x_4
   \end{bmatrix}
   \begin{bmatrix}
   a
   
   b
   \end{bmatrix}

其中 :math:`x_1a+x_2b=\gcd(a,b)` 给出了一个 Bézout 等式。

.. literalinclude:: /math/assets/Euclid.py
   :language: py
   :lines: 1-16

需要注意的是在上述求逆元（我们假设逆元存在）代码中解的范围，在 `wiki`_ 中有证明只调整一次是安全的。

.. _wiki: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

多项式的扩展 Euclid 算法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
我们尝试将辗转相除应用于多项式上，假设要求 :math:`S(x)` 和 :math:`T(x)` 满足

.. math:: S(x)A(x)+T(x)B(x)=\gcd(A(x),B(x))

其中 :math:`A(x)` 和 :math:`B(x)` 已知。

如果我们直接计算，那么在辗转相除的过程中多项式的度数可能下降很慢，最坏需要消耗 :math:`O(\deg(A(x))\deg(B(x)))` 的时间。

观察到多项式除法的商仅由他们的高位决定，而商序列的度数之和是线性级别的，这导出了后来的 Half-Euclid 算法，但我们在这里略过。

Lagrange 插值
-----------------------
实际由 Gauss 提出 [#cryp]_ 。回顾线性方程组 :eq:`lineq` ，我们发现

.. math::
   x\equiv
   \sum_{1\leq i\leq n}x_iM_iN_i\pmod{M},
   \quad
   M_i=M/m_i,
   \quad
   N_i=M_i^{-1}\bmod{m_i}

观察到当我们任取一个 :math:`1\leq j\leq n` 时

.. math::
   \sum_{1\leq i\leq n}x_iM_iN_i
   \equiv
   x_j+
   \sum_{1\leq i\leq n\land i\neq j}x_iM_iN_i
   \pmod{m_j}

后面和式中 :math:`M_i` 是 :math:`m_j` 的倍数于是在模 :math:`m_j` 意义下同余于零。

多项式的 Lagrange 插值 [#modalg]_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
我们将上述算法应用于多项式上，问题变为

.. math::
   \begin{cases}
   A(x)\equiv y_1\pmod{(x-x_1)}

   A(x)\equiv y_2\pmod{(x-x_2)}

   \vdots

   A(x)\equiv y_n\pmod{(x-x_n)}
   \end{cases}

合并上述同于方程。

我们也假设对于 :math:`\forall i\neq j` 有 :math:`x_i\neq x_j` 且我们知道 :math:`A(x)\bmod{(x-a)}=A(a)` 。

设 :math:`M(x)=\prod_{1\leq i\leq n}(x-x_i)` 和 :math:`M_{i}(x)=M(x)/(x-x_i)` 及 :math:`N_{i}(x)=M_{i}^{-1}(x)\bmod{(x-x_i)}` 及

.. math::
   A(x)
   \equiv
   \sum_{1\leq i\leq n}
   y_iM_i(x)N_i(x)
   \pmod{M(x)}

与上面同样的，任取 :math:`1\leq j\leq n` 都满足

.. math::
   \sum_{1\leq i\leq n}
   y_iM_i(x)N_i(x)
   \equiv
   y_j+\sum_{1\leq i\leq n\land i\neq j}y_iM_i(x)N_i(x)
   \pmod{(x-x_i)}

后一个和式中显然 :math:`M_j(x)` 都是 :math:`x-x_j` 的倍式，也就是都能满足 :math:`A(x_j)=y_j` 。

稍加整理得到了

.. math::
   A(x)
   \equiv
   \sum_{1\leq i\leq n}
   y_i
   \frac{\prod_{j\neq i}(x-x_j)}{\prod_{j\neq i}
   (x_i-x_j)}
   \pmod{M(x)}

为了方便，我们省略同余符号。

令 :math:`s_i=\prod_{j\neq i}\frac{1}{x_i-x_j}` 那么 :math:`A(x)` 可以表示为

.. math::
   A(x)=
   \sum_{1\leq i\leq n}
   y_is_i\frac{M(x)}{x-x_i}

观察到

.. math::
   M'(x)=\sum_{1\leq i\leq n}
   \frac{M(x)}{x-x_i}

且

.. math::
   M'(x_i)=
   \lim_{x\to x_i}
   \frac{M(x)-M(x_i)}{x-x_i}
   =
   \lim_{x\to x_i}
   \frac{M(x)}{x-x_i}
   =
   \frac{1}{s_i}

结合 FFT 的基本思想（分治取模）即可得到一个快速插值的算法。具体的，我们设

.. math::
   M_a(x)&=\prod_{1\leq i\leq \left\lfloor n/2 \right\rfloor}(x-x_i)

   M_b(x)&=\prod_{\left\lfloor n/2 \right\rfloor \lt i\leq n}(x-x_i)

   A_a(x)&=\sum_{1\leq i\leq \left\lfloor n/2 \right\rfloor}y_is_i\frac{M_a}{x-x_i}

   A_b(x)&=\sum_{\left\lfloor n/2 \right\rfloor \lt i\leq n}y_is_i\frac{M_b}{x-x_i}

那么

.. math:: A(x)=A_a(x)M_b(x)+A_b(x)M_a(x)

目前存在常数更小的算法 [#tell]_ 。

---------------------

.. rubric:: 脚注

.. [#cryp] Alfred J\. Menezes, Paul C\. van Oorschot and Scott A\. Vanstone. `Handbook of Applied Cryptography <http://cacr.uwaterloo.ca/hac/>`_.
.. [#modalg] J\. von zur Gathen and J\. Gerhard. Modern computer algebra. Cambridge University Press, 1999.
.. [#tell] A\. Bostan, G\. Lecerf, and É\. Schost. `Tellegen’s principle into practice <https://specfun.inria.fr/bostan/publications/BoLeSc03.pdf>`_. In Proceedings of ISSAC’03, pages 37–44. ACM Press, 2003.

Newton 插值
-----------------------
与 Lagrange 插值不同，我们不是直接构造出一个解，而是在计算过程中构造“部分解”。

考虑合并两个关于 :math:`x` 的同余方程如

.. math::
   \begin{cases}
   x\equiv x_1\pmod{m_1}

   x\equiv x_2\pmod{m_2}
   \end{cases}

若 :math:`\gcd(m_1,m_2)=1` 那么存在整数 :math:`k_1` 和 :math:`k_2` 满足

.. math::
   x=x_1+k_1m_1=x_2+k_2m_2


   \implies
   x_1\equiv x_2+k_2m_2\pmod{m_1}

可用扩展 Euclid 算法求出

.. math:: k_1\equiv (x_2-x_1)m_1^{-1}\pmod{m_2}

代入 :math:`k_1` 可求出 :math:`x_{12}=x\bmod{m_1m_2}` 。

考虑给上述方程组增加一个 :math:`x\equiv x_3\pmod{m_3}` 那么

.. math:: x=x_{12}+k_{12}m_1m_2=x_3+k_3m_3

那么

.. math::
   k_{12}
   \equiv
   (x_3-x_{12})(m_1m_2)^{-1}
   \pmod{m_3}

如果这个方程组有 :math:`n` 个项目，那么我们可以依次求出 :math:`y` 满足

.. math::
   x\equiv
   x_1+y_1m_1+y_2m_1m_2+\cdots +y_{n-1}\prod_{1\leq i\lt n}m_i
   \quad\left(\bmod{\prod_{1\leq i\leq n}m_i}\right)

.. 上面没办法用 \pmod 了因为括号没法对应大小了

这也被称为 Garner 算法。

而当模数不是两两互素时，我们一般使用两两合并的方法，这里只给出实验性的代码。

.. literalinclude:: /math/assets/Euclid.py
   :language: py
   :lines: 19-29

多项式的 Newton 插值
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Newton 插值结合 FFT 可以做到与 Lagrange 插值一样快速。

但因为之前的文献忘记放哪儿了并且不太清楚实际作用就先不写了。