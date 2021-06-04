===================
特征多项式
===================

:Date: 2021-1-6
:Author: hly1204
:Status: 待补充

特征多项式的定义
----------------------
对于矩阵 :math:`\mathbf{A}\in\mathbb{R}^{n\times n}` ，我们说 :math:`\mathbf{A}` 的特征多项式为

.. math::
   p(\lambda)=\det(\lambda \mathbf{I}-\mathbf{A})=\lambda ^{n}+c_{1}\lambda ^{n-1}+\cdots +c_{n-1}\lambda +c_{n}

其中 :math:`\mathbf{I}\in\mathbb{R}^{n\times n}` 为一个单位矩阵， :math:`c_{1}=-\operatorname{tr}(\mathbf{A})` 且 :math:`c_{n}=\det(\mathbf{A})` 写成行列式形式即

.. math::
   p(\lambda)=
   \begin{vmatrix}
   \lambda -a_{11}&a_{12}&a_{13}&\cdots & a_{1(n-1)}&a_{1n}

   a_{21}&\lambda -a_{22}&a_{23}&\cdots & a_{2(n-1)}&a_{2n}

   a_{31}&a_{32}&\lambda -a_{33}&\cdots & a_{3(n-1)}&a_{3n}

   \vdots & \vdots & \vdots & \ddots & \vdots & \vdots

   a_{(n-1)1}&a_{(n-1)2}&a_{(n-1)3}&\cdots & \lambda -a_{(n-1)(n-1)}&a_{(n-1)n}

   a_{n1}&a_{n2}&a_{n3}&\cdots & a_{n(n-1)}&\lambda -a_{nn}
   \end{vmatrix}

.. note::
   注意到有的地方定义特征多项式为 :math:`p(\lambda)=\det(\mathbf{A}-\lambda \mathbf{I})` 没有本质区别，但我们使用上述定义，因为得到的多项式一定为首一的。