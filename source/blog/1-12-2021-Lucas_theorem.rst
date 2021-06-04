====================
Lucas 定理及其推广
====================

Lucas 定理
--------------------

**Lucas 定理**
   对于一个素数 :math:`p` 和非负整数 :math:`n,k` ，有

   .. math::
      :label: Lucas' theorem

      \binom{n}{k}\equiv\binom{n\bmod{p}}{k\bmod{p}}\binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}\pmod{p}

   其中 :math:`\lfloor \cdot \rfloor` 表示整数部分， :math:`\binom{n}{k}=\frac{n(n-1)\cdots (n-k+1)}{k!}` 。

**推论**
   将 :math:`n,k` 表示为 :math:`p` 进制为

   .. math::
      n&=a_{r}p^{r}+\cdots +a_{1}p+a_{0}

      k&=b_{r}p^{r}+\cdots +b_{1}p+b_{0}

   那么

   .. math:: \binom{n}{k}\equiv \prod_{i=0}^{r}\binom{a_{i}}{b_{i}}\pmod{p}

**证明**

   考虑

   .. math::
      \binom{n}{k}&=\frac{n(n-1)\cdots (n-k+1)}{k!}

      &=\left(\frac{n}{k}\right)\left(\frac{n-1}{k-1}\right)\cdots \left(\frac{n-k+1}{1}\right)

   令 :math:`n=ap+b,k=cp+d` 且 :math:`b,d\lt p` ，那么

   .. math::
      \left(\frac{ap+b}{cp+d}\right)\cdots \left(\frac{ap+b-d+1}{cp+1}\right)\equiv
      \left(\frac{b}{d}\right)\cdots \left(\frac{b-d+1}{1}\right)

      \equiv\binom{n\bmod{p}}{k\bmod{p}}\pmod{p}

   注意上式为 :math:`\binom{n}{k}\pmod{p}` 的前 :math:`k\bmod{p}=d` 项的乘积，还剩下 :math:`k-d` 项为

   .. math::
      \left(\frac{n-d}{cp}\right)\left(\frac{n-d-1}{cp-1}\right)\cdots \left(\frac{n-k+1}{1}\right)=\binom{n-d}{cp}

   也就是 :math:`cp` 项，将这 :math:`cp` 项分为 :math:`c` 组，每一组的分子和分母都是连续的 :math:`p` 项，显然分子和分母中都各有一项是 :math:`p` 的倍数，而其余项的乘积在模 :math:`p` 意义下同余于 :math:`(p-1)!` 可以让剩下的分子分母相互抵消。这指导我们只需关注这 :math:`c` 项的分子分母，而这几项分别为

   .. math::
      \left(\frac{\lfloor(n-d)/p\rfloor \cdot p}{cp}\right)\left(\frac{(\lfloor(n-d)/p\rfloor -1) \cdot p}{(c-1)p}\right)\cdots \left(\frac{(\lfloor (n-d)/p\rfloor -c+1)\cdot p}{p}\right)

   即

   .. math:: \binom{\lfloor (n-d)/p\rfloor}{\lfloor k/p\rfloor}

   注意当 :math:`d=k\bmod{p}\leq n\bmod{p}` 时，上式等于

   .. math::
      \binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}

   而当 :math:`k\bmod{p}\gt n\bmod{p}` 时，我们知道从组合意义上 :math:`n` 个物品中不可能选取多于 :math:`n` 个物品

   .. math:: \binom{n\bmod{p}}{k\bmod{p}}=0

   :eq:`Lucas' theorem` 得证。当 :math:`m` 远小于 :math:`p` 时，可以直接通过公式计算而非预处理，这时候处理 :math:`p` 较大的情况成为可能。

Lucas 定理的推广
--------------------
这篇文章是 [#a]_ 的翻译。

Lucas 定理的推广
~~~~~~~~~~~~~~~~~~~~
**定义 1**
   对于给定一个整数 :math:`n` 令 :math:`(n!)_{p}` 表示所有小于等于 :math:`n` 的不能被 :math:`p` 整除的整数的乘积。也可以写作 :math:`(n!)_{p}=n!/(\lfloor n/p\rfloor !p^{\lfloor n/p\rfloor})` 。

**定理 1**
   给定素数 :math:`p` 的幂次 :math:`p^q` 和正整数 :math:`n=m+r` 。在 :math:`p` 进制下记 :math:`n=n_{0}+n_{1}p+\dots +n_{d}p^{d}` 且对于每个 :math:`j` 令 :math:`N_{j}=\lfloor n/p^j\rfloor \bmod{p^q}` （即 :math:`N_{j}=n_{j}+n_{j+1}+\dots +n_{j+q-1}p^{q-1}` ）。对于 :math:`m_{j},M_{j},r_{j},R_{j}` 也同样定义。令 :math:`e_{j}` 为当将 :math:`m` 和 :math:`r` 在 :math:`p` 进制中相加的在第 :math:`j` 位数字和之后的“进位”次数。有

   .. math::
      :label: theorem 1

      \frac{(\pm 1)^{e_{q-1}}}{p^{e_{0}}}\binom{n}{m}\equiv \frac{(N_{0}!)_{p}}{(M_{0}!)_{p}(R_{0}!)_{p}}\frac{(N_{1}!)_{p}}{(M_{1}!)_{p}(R_{1}!)_{p}}\cdots \frac{(N_{d}!)_{p}}{(M_{d}!)_{p}(R_{d}!)_{p}}\pmod{p^q}

   其中 :math:`(\pm 1)` 为 :math:`(-1)` 除非 :math:`p=2` 且 :math:`q\geq 3` 。

为了证明 :eq:`theorem 1` ，我们给出一个需要用到的定理和简单证明

Wilson 定理
~~~~~~~~~~~~~~~~~~~~
对于素数 :math:`p` 有

.. math:: (p-1)!\equiv -1\pmod{p}

成立。

**证明**
   我们知道在模奇素数 :math:`p` 意义下对于整数 :math:`n\nmid p` 都存在逆元且唯一。一个整数逆元的逆元为其自身。

   对于逆元为自身的情况，我们记 :math:`a^2\equiv 1\pmod{p}\implies(a+1)(a-1)\equiv 0\pmod{p}` 那么 :math:`a\equiv \pm 1\pmod{p}` 。

   否则我们记 :math:`b\equiv a^{-1}\pmod{p}` 有 :math:`ab\equiv 1\pmod{p}` 可以将 :math:`\mathbb{F}_p\setminus\{0,1,p-1\}` 分为这样的 :math:`(a,b)` 对， :math:`\prod_{i=2}^{p-2}i\equiv 1\pmod{p}` 。那么 :math:`(p-1)!\equiv 1\cdot (-1)\pmod{p}` 。

   在 :math:`p=2` 时另外讨论即可。

Wilson 定理指出 :math:`(p!)_{p}=(p-1)!\equiv -1\pmod{p}` 且可以被推广到模素数 :math:`p` 的幂次。

Wilson 定理的推广
~~~~~~~~~~~~~~~~~~~~
对于给定一个素数幂次 :math:`p^q` 有

.. math:: (p^q!)_p\equiv \pm 1\pmod{p^q}

其中 :math:`(\pm 1)` 与 :eq:`theorem 1` 中最后一句描述的相同。

**证明**
   与上述证明类似的，只要我们不停在模 :math:`p^q` 意义下配对每个 :math:`m` 和它的逆元，那么 :math:`(p^q!)` 在模 :math:`p^q` 意义下同余于那些逆元等于自身的元素的乘积。

   即关于 :math:`m` 的方程 :math:`m^2\equiv 1\pmod{p^q}` 的根的乘积，而这两个根分别为 :math:`1` 和 :math:`p^q-1` ，除非 :math:`p^q=2` 时，仅有一根，或者 :math:`p=2` 且 :math:`q\geq 3` 时额外的根为 :math:`2^{q-1}\pm 1` 。

**推论 1**
   对于给定素数 :math:`p` 的幂次 :math:`p^q` 和 :math:`N_{0}=n\bmod{p^q}` 有

   .. math::
      :label: corollary 1

      (n!)_p\equiv (\pm 1)^{\lfloor n/p^q\rfloor}(N_0!)_p\pmod{p^q}

   其中 :math:`(\pm 1)` 与 :eq:`theorem 1` 中最后一句描述的相同。

**推论 1 的证明**
   将每个下面的 :math:`r` 记为 :math:`ip^q+j` 有

   .. math::
      (n!)_p&=\prod_{r\leq n\land r\nmid p}r

      &=\left(\prod_{i=0}^{\lfloor n/p^q\rfloor -1}\prod_{1\leq j\leq p^q\land j\nmid p}(ip^q+j)\right)\left(\prod_{1\leq j\leq
      N_0\land j\nmid p}(\lfloor n/p^q\rfloor p^q+j)\right)

      &\equiv ((p^q!)_p)^{\lfloor n/p^q\rfloor}(N_0!)_p

      &\equiv (\pm 1)^{\lfloor n/p^q\rfloor}(N_0!)_p\pmod{p^q}

-------------------

**Legendre 定理**
   Legendre 在 1808 年展示了准确的 :math:`p` 的多少幂次整除 :math:`n!` 为

   .. math:: \nu_p(n!)=\sum_{i\geq 1}\lfloor n/p^i\rfloor

**Legendre 定理的证明**
   :math:`n!=p^{\nu(n!)}c` 其中 :math:`p\nmid c` 。这很显然，考虑 :math:`n!=1\times 2\times \cdots \times n` 而其中能被 :math:`p` 整除的项为 :math:`p\times 2p\times\cdots\times\lfloor n/p\rfloor p=\lfloor n/p\rfloor !p^{\lfloor n/p\rfloor}` 那么有 :math:`\nu_p(n!)=\lfloor n/p\rfloor +\nu_p(\lfloor n/p\rfloor !)` 。

将 :math:`n` 在 :math:`p` 进制下记为 :math:`n=n_0+n_1p+\cdots +n_dp^d` 我们定义一个每一位数的和的函数 :math:`\sigma(n)=\sigma_p(n):=n_0+n_1+\cdots +n_d` 。那么

.. math:: \nu_p(n!)=(n-\sigma_p(n))/(p-1)

考虑证明 :math:`\nu_p(n!)=(n-\sigma_p(n))/(p-1)` ，当 :math:`n\lt p` 时该式为零显然成立。而

.. math:: n_0=n-p\lfloor n/p\rfloor =\sigma_p(n)-\sigma_p(\lfloor n/p\rfloor)

代入上面得到的递归式中有

.. math::
   \nu_p(\lfloor n/p\rfloor !)+\lfloor n/p\rfloor &=(\lfloor n/p\rfloor -\sigma_p(\lfloor
   n/p\rfloor))/(p-1)+\lfloor n/p\rfloor

   &=(\lfloor n/p\rfloor -(\sigma_p(n)-n_0))/(p-1)+\lfloor n/p\rfloor

   &=(\lfloor n/p\rfloor +(p-1)\lfloor n/p\rfloor -\sigma_p(n)+n_0)/(p-1)

   &=((n-n_0)-\sigma_p(n)+n_0)/(p-1)

   &=(n-\sigma_p(n))/(p-1)

   &=\nu_p(n!)

令 :math:`r=n-m` 且将 :math:`n,m` 和 :math:`r` 转换为 :math:`p` 进制表示（即 :math:`n=\sum_{i=0}^dn_ip^i` 且 :math:`m` 和 :math:`r` 也一样如此表示）。如果在 :math:`p` 进制下将 :math:`m` 与 :math:`r` 相加在第 :math:`j` 位产生了“进位”，令 :math:`\epsilon_j=1` 否则 :math:`\epsilon_j=0` （包括 :math:`\epsilon_{-1}=0` ）。我们借由上式推导出下面的

Kummer 定理
~~~~~~~~~~~~~~~~~~~~
:math:`p` 的多少次幂整除二项式系数 :math:`\binom{n}{m}` 为 :math:`m` 与 :math:`n-m` 在 :math:`p` 进制下相加所需要的“进位”次数。

**证明**
   对于每个 :math:`j\geq 0` 我们可以简单的发现

   .. math:: n_j=m_j+r_j+\epsilon_{j-1}-p\epsilon_j

   而

   .. math::
      \nu_p\left(\frac{n!}{m!r!}\right)=\nu_p(n!)-\nu_p(m!)-\nu_p(r!)=\frac{\sigma_p(m)+\sigma_p(r)-\sigma_p(n)}{p-1}


   通过定义我们知道

   .. math::
      \nu_p\left(\frac{n!}{m!r!}\right)=\sum_{j=0}^d\frac{m_j+r_j-n_j}{p-1}=\frac{p\epsilon_0+\sum_{j=0}^d(p\epsilon_j-\epsilon_{j-1})}{p-1}=\sum_{j=0}^{d-1}\epsilon_j

   即“进位”的次数。

类似的我们有对于 :math:`j\geq 1`

.. math:: \lfloor n/p^j\rfloor -\lfloor m/p^j\rfloor -\lfloor r/p^j\rfloor =\epsilon_{j-1}

很显然。

-------------------

通过在 :eq:`theorem 1` 中的定义，对于 :math:`j\geq 0` 我们有

.. math::
   \lfloor n/p^j\rfloor !/(p^{\lfloor n/p^{j+1}\rfloor}\lfloor n/p^{j+1}\rfloor !)=(\lfloor n/p^j\rfloor !)_p\equiv (\pm 1)^{\lfloor n/p^{j+q}\rfloor}(N_j!)_p\pmod{p^q}

通过 :eq:`corollary 1` ，将所有 :math:`j\geq 0` 的同余式相乘得到了

**命题 1**
    对于任何整数 :math:`n` 和素数幂次 :math:`p^q` ，我们有

    .. math::
      n!\Big/p^{\sum_{j\geq 1}\lfloor n/p^j\rfloor}\equiv (\pm 1)^{\sum_{j\geq q}\lfloor n/p^j\rfloor}\prod_{j\geq 0}(N_j!)_p\pmod{p^q}
    
    其中 :math:`(\pm 1)` 与 :eq:`theorem 1` 中最后一句描述的相同。

至此 :eq:`theorem 1` 得证。

任意模数二项卷积
--------------------
对于一个数列 :math:`\langle a\rangle =a_{0},a_{1},\dots ,a_{n}` 和 :math:`\langle b\rangle =b_{0},b_{1},\dots ,b_{m}` 设多项式 :math:`A(x)=\sum_{i=0}^n\frac{a_i}{i!}x^i` 和 :math:`B(x)=\sum_{i=0}^m\frac{b_i}{i!}x^i` 和

.. math:: C(x)=A(x)B(x)=\sum_{i=0}^{n+m}\frac{c_i}{i!}x^i

为了保证边界情况，我们认为对于 :math:`\forall i\gt n` 有 :math:`a_{i}=0` ， :math:`b_{i}` 同理。显然，根据一般的多项式乘法我们有

.. math:: \frac{c_k}{k!}=\sum_{i=0}^k\frac{a_i}{i!}\frac{b_{k-i}}{(k-i)!}

那么

.. math:: c_k=\sum_{i=0}^k\frac{k!}{i!(k-i)!}a_ib_{k-i}=\sum_{i=0}^k\binom{k}{i}a_ib_{k-i}

这也是二项卷积名称的由来。而我们知道当 :math:`i\gt k` 和 :math:`i\lt 0` 时二项式系数 :math:`\binom{k}{i}=0` 所以可以直接写作

.. math:: c_k=\sum_{i}\binom{k}{i}a_ib_{k-i}

因为合数可以通过中国剩余定理来进行合并，所以只需考虑如何求在模一个素数幂次 :math:`p^q` 意义下的 :math:`C(x)` 的系数。这里与上面不同的是 :math:`n,m` 的范围不大（因为需要考虑卷积的时间），可以预处理出 :math:`n!/p^{\nu_p(n!)}\pmod{p^q}` 。我们令 :math:`\hat{a}_k=a_k\cdot (k!/p^{\nu_p(k!)})^{-1}\pmod{p^q}` 那么

.. math:: \hat{c}_k=\sum_{i=0}^kp^{\nu_p(k!)-\nu_p((k-i)!)-\nu_p(i!)}\hat{a}_i\hat{b}_{k-i}\pmod{p^q}

剩下是分析可以进行运算的范围，包括上文内容也是参考 [#b]_ 中的。注意需要求出 :math:`\hat{c}_k` 在模“NTT 模数”的意义下，然后进行合并，此时没有除法。

参考文献
--------------------

.. [#a] Andrew Granville. `Arithmetic Properties of Binomial Coefficients I: Binomial Coefficients modulo prime powers <http://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/binomial.html>`_.
.. [#b] Entropy Increaser. `任意模数二项卷积 <https://blog.csdn.net/EI_Captain/article/details/107456608>`_.