:Date: 2021-6-5
:Author: hly1204
:Status: 待补充

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

例如有集合 :math:`A` 和集合 :math:`B` 那么集合 :math:`A\times B=\{(a,b)\mid a\in A,b\in B\}` 。

Euclid 算法
-----------------------

扩展 Euclid 算法
-----------------------

Lagrange 插值
-----------------------

Newton 插值
-----------------------