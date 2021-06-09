:Date: 2021-4-10
:Author: hly1204

===================
快速 Fourier 变换
===================
让我们关注在环 :math:`R` 上的运算。

Classical radix-2 FFT
--------------------------
在 Bernstein 的论文中也称为 original radix-2 FFT ，这里使用标题的称呼。该算法最早由 Gauss 提出后由 Cooley 和 Tukey 重新发表。

最早由 Fiduccia 发现 classical radix-2 FFT 实际上可以用下式表示

.. math::
   :label: classical2fft

   R[x]/(x^{2m}-b^2)&\to R[x]/(x^m-b)

   &\times R[x]/(x^m+b)

输入为 :math:`f\bmod(x^{2m}-b^2)` 计算 :math:`f_Y=f\bmod{(x^m-b)}` 和 :math:`f_Z=f\bmod{(x^m+b)}` 。在这里这样的取模运算是很简单的。我们将输入分为大小为 :math:`m` 的两部分

即 :math:`f\bmod{(x^{2m}-b^2)}=f_B+f_A\cdot x^m` ，其中 :math:`f_B=(f\bmod{(x^{2m}-b^2)})\bmod{x^m}` 。

那么 :math:`f_Y=b\cdot f_A+f_B` 且 :math:`f_Z=-b\cdot f_A+f_B` 。我们可以使用矩阵表示这一过程如

.. math::
   \begin{bmatrix}
   f_Y
   
   f_Z
   \end{bmatrix}
   =
   \begin{bmatrix}
   b&1
   
   -b&1
   \end{bmatrix}
   \begin{bmatrix}
   f_A
   
   f_B
   \end{bmatrix}

一些工程师经常把这个变换画成一个图然后称为“蝶形操作”。而 classical radix-2 FFT 就是不停应用直到最后模一个线性的多项式，也就等价于求得点值。

注意到只需要 :math:`2b` 是可逆的那么上述算法就是可逆的，把上面的过程倒过来，也就是做一个求和和差分再乘以 :math:`(2b)^{-1}` 也可以得到答案（大多数时候我们会将这里每一步的 :math:`2` 累积到最后处理）。

Twisted radix-2 FFT
---------------------------

Split-radix FFT
---------------------------

Classical radix-3 FFT
---------------------------
我们考虑映射

.. math::
   R[x]/(x^{3m}-b^3)&\to R[x]/(x^m-b)

   &\times R[x]/(x^m-\omega b)

   &\times R[x]/(x^m-\omega^2b)

这个式子看起来就希望令 :math:`\omega^3=1` 且 :math:`\omega \neq 1` ，根据欧拉公式我们有

.. math::
   \omega=
   \exp(2\pi\mathrm{i}/3)=
   \cos \frac{2\pi}{3}+\mathrm{i}\sin\frac{2\pi}{3}=
   -\frac{1}{2}+\frac{\sqrt{3}}{2}\mathrm{i}
   
此时 :math:`1+\omega +\omega ^2=0` 。

代入后发现 :math:`\prod_{0\leq i\leq 2}(x^m-\omega^ib)=(x^{3m}-b^3)` 。

Twisted radix-3 FFT
---------------------------

Classical radix-4 FFT
---------------------------

Twisted radix-4 FFT
---------------------------

.. rubric:: 脚注

.. [#m3] Daniel J. Bernstein. `Multidigit Multiplication For Mathematicians <https://www.researchgate.net/publication/2370542_Multidigit_Multiplication_For_Mathematicians>`_.
.. [#todd] Todd Mateer. `Fast Fourier Transform Algorithms with Applications <http://cr.yp.to/f2mult/mateer-thesis.pdf>`_.