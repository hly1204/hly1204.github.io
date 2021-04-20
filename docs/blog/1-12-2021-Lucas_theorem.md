学习了一下 Lucas 定理。

## Lucas 定理

!!! quote "Lucas 定理"

    对于一个素数 $p$ 和非负整数 $n,k$ ，有

    $$\binom{n}{k}\equiv\binom{n\bmod{p}}{k\bmod{p}}\binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}\pmod{p}$$

    其中 $\lfloor \cdot \rfloor$ 表示整数部分， $\binom{n}{k}=\frac{n(n-1)\cdots (n-k+1)}{k!}$ 。

!!! quote "推论"

    将 $n,k$ 表示为 $p$ 进制为

    $$n=a_{r}p^{r}+\cdots +a_{1}p+a_{0}$$

    $$k=b_{r}p^{r}+\cdots +b_{1}p+b_{0}$$

    那么

    $$\binom{n}{k}\equiv \prod_{i=0}^{r}\binom{a_{i}}{b_{i}}\pmod{p}$$

证明：由 Lucas 定理推导出推论很自然。考虑

$$\binom{n}{k}=\frac{n(n-1)\cdots (n-k+1)}{k!}=\left(\frac{n}{k}\right)\left(\frac{n-1}{k-1}\right)\cdots \left(\frac{n-k+1}{1}\right)$$

令 $n=ap+b,k=cp+d$ 且 $b,d\lt p$ ，那么

$$\left(\frac{ap+b}{cp+d}\right)\left(\frac{ap+b-1}{cp+d-1}\right)\cdots \left(\frac{ap+b-d+1}{cp+1}\right)\equiv \left(\frac{b}{d}\right)\left(\frac{b-1}{d-1}\right)\cdots \left(\frac{b-d+1}{1}\right)\equiv \binom{n\bmod{p}}{k\bmod{p}}\pmod{p}$$

注意上式为 $\binom{n}{k}\pmod{p}$ 的前 $k\bmod{p}=d$ 项的乘积，还剩下 $k-d$ 项为

$$\left(\frac{n-d}{cp}\right)\left(\frac{n-d-1}{cp-1}\right)\cdots \left(\frac{n-k+1}{1}\right)=\binom{n-d}{cp}$$

也就是 $cp$ 项，将这 $cp$ 项分为 $c$ 组，每一组的分子和分母都是连续的 $p$ 项，显然分子和分母中都各有一项是 $p$ 的倍数，而其余项的乘积在模 $p$ 意义下同余于 $(p-1)!$ 可以让剩下的分子分母相互抵消。这指导我们只需关注这 $c$ 项的分子分母，而这几项分别为

$$\left(\frac{\lfloor(n-d)/p\rfloor \cdot p}{cp}\right)\left(\frac{(\lfloor(n-d)/p\rfloor -1) \cdot p}{(c-1)p}\right)\cdots \left(\frac{(\lfloor (n-d)/p\rfloor -c+1)\cdot p}{p}\right)=\binom{\lfloor (n-d)/p\rfloor}{\lfloor k/p\rfloor}$$

注意当 $d=k\bmod{p}\leq n\bmod{p}$ 时，上式等于

$$\binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}$$

而当 $k\bmod{p}\gt n\bmod{p}$ 时，我们知道从组合意义上 $n$ 个物品中不可能选取多于 $n$ 个物品

$$\binom{n\bmod{p}}{k\bmod{p}}=0$$

$\square$ 。当 $m$ 远小于 $p$ 时，可以直接通过公式计算组合数而非预处理，这时候处理 $p$ 较大的情况成为可能。

## Lucas 定理的推广

下文为[^1]的翻译。

!!! quote "定义 1"

    对于给定一个整数 $n$ 令 $(n!)_{p}$ 表示所有小于等于 $n$ 的不能被 $p$ 整除的整数的乘积。也可以写作 $(n!)_{p}=n!/(\lfloor n/p\rfloor !p^{\lfloor n/p\rfloor})$ 。

!!! quote "定理 1"

    给定素数 $p$ 的幂次 $p^q$ 和正整数 $n=m+r$ 。在 $p$ 进制下记 $n=n_{0}+n_{1}p+\dots +n_{d}p^{d}$ 且对于每个 $j$ 令 $N_{j}=\lfloor n/p^j\rfloor \bmod{p^q}$ （即 $N_{j}=n_{j}+n_{j+1}+\dots +n_{j+q-1}p^{q-1}$ ）。对于 $m_{j},M_{j},r_{j},R_{j}$ 也同样定义。令 $e_{j}$ 为当将 $m$ 和 $r$ 在 $p$ 进制中相加的在第 $j$ 位数字和之后的“进位”次数。有

    $$\frac{(\pm 1)^{e_{q-1}}}{p^{e_{0}}}\binom{n}{m}\equiv \frac{(N_{0}!)_{p}}{(M_{0}!)_{p}(R_{0}!)_{p}}\frac{(N_{1}!)_{p}}{(M_{1}!)_{p}(R_{1}!)_{p}}\cdots \frac{(N_{d}!)_{p}}{(M_{d}!)_{p}(R_{d}!)_{p}}\pmod{p^q}$$

    其中 $(\pm 1)$ 为 $(-1)$ 除非 $p=2$ 且 $q\geq 3$ 。

下面给出一个需要用到的定理和简单证明

!!! quote "Wilson 定理"

    对于素数 $p$ 有

    $$(p-1)!\equiv -1\pmod{p}$$

    成立。

证明：我们知道在模奇素数 $p$ 意义下对于整数 $1,2,\dots ,p-1$ 都存在逆元且唯一。一个整数逆元的逆元为其自身。对于逆元为自身的情况，我们记 $a^2\equiv 1\pmod{p}\implies(a+1)(a-1)\equiv 0\pmod{p}$ 那么 $a\equiv \pm 1\pmod{p}$ 。否则我们记 $b\equiv a^{-1}\pmod{p}$ 有 $ab\equiv 1\pmod{p}$ 可以将 $\\{2,\dots,p-2\\}$ 分为这样的 $\\{a,b\\}$ 对， $\prod_{i=2}^{p-2}i\equiv 1\pmod{p}$ 。那么 $(p-1)!\equiv 1\cdot (-1)\pmod{p}$ 。在 $p=2$ 时另外讨论即可。 $\square$

Wilson 定理指出 $(p!)_{p}=(p-1)!\equiv -1\pmod{p}$ 且可以被推广到模素数 $p$ 的幂次

!!! quote "引理 1"

    对于给定一个素数幂次 $p^q$ 有

    $$(p^q!)_p\equiv \pm 1\pmod{p^q}$$

    其中 $(\pm 1)$ 与定理 1 中最后一句描述的相同。

证明：与上述证明类似的，只要我们不停在模 $p^q$ 意义下配对每个 $m$ 和它的逆元，那么 $(p^q!)$ 在模 $p^q$ 意义下同余于那些逆元等于自身的元素的乘积，即关于 $m$ 的方程 $m^2\equiv 1\pmod{p^q}$ 的根的乘积，而这两个根分别为 $1$ 和 $p^q-1$ ，除非 $p^q=2$ 时，仅有一根，或者 $p=2$ 且 $q\geq 3$ 时额外的根为 $2^{q-1}\pm 1$ 。 $\square$

!!! quote "推论 1"

    推论 1 ：对于给定素数 $p$ 的幂次 $p^q$ 和 $N_{0}=n\bmod{p^q}$ 有

    $$(n!)_p\equiv (\pm 1)^{\lfloor n/p^q\rfloor}(N_0!)_p\pmod{p^q}$$

    其中 $(\pm 1)$ 与定理 1 中最后一句描述的相同。

证明：将每个下面的 $r$ 记为 $ip^q+j$ 有

$$\begin{aligned}
(n!)_p&=\prod_{r\leq n}'r\\
&=\left(\prod_{i=0}^{\lfloor n/p^q\rfloor -1}\prod_{1\leq j\leq p^q}'(ip^q+j)\right)\left(\prod_{1\leq j\leq
N_0}'(\lfloor n/p^q\rfloor p^q+j)\right)\\
&\equiv ((p^q!)_p)^{\lfloor n/p^q\rfloor}(N_0!)_p\\
&\equiv (\pm 1)^{\lfloor n/p^q\rfloor}(N_0!)_p\pmod{p^q}
\end{aligned}$$

在引理 1 中一样， $\prod'$ 表示不能被 $p$ 整除的整数的乘积。

!!! quote "Legendre"

    Legendre 在 1808 年展示了准确的 $p$ 的多少幂次整除 $n!$ 为

    $$\nu_p(n!)=\sum_{i\geq 1}\lfloor n/p^i\rfloor$$

也就是说 $n!=p^{\nu(n!)}c$ 其中 $p\nmid c$ 。这很显然，考虑 $n!=1\times 2\times \cdots \times n$ 而其中能被 $p$ 整除的项为 $p,2p,\dots,\lfloor n/p\rfloor p=\lfloor n/p\rfloor !p^{\lfloor n/p\rfloor}$ 那么有 $\nu_p(n!)=\lfloor n/p\rfloor +\nu_p(\lfloor n/p\rfloor !)$ 。

将 $n$ 在 $p$ 进制下记为 $n=n_0+n_1p+\cdots +n_dp^d$ 我们定义一个每一位数的和的函数 $\sigma(n)=\sigma_p(n):=n_0+n_1+\cdots +n_d$ 。那么

$$\nu_p(n!)=(n-\sigma_p(n))/(p-1)$$

考虑证明 $\nu_p(n!)=(n-\sigma_p(n))/(p-1)$ ，当 $n\lt p$ 时该式为零显然成立。而

$$n_0=n-p\lfloor n/p\rfloor =\sigma_p(n)-\sigma_p(\lfloor n/p\rfloor)$$

代入上面得到的递归式中有

$$\begin{aligned}
\nu_p(\lfloor n/p\rfloor !)+\lfloor n/p\rfloor &=(\lfloor n/p\rfloor -\sigma_p(\lfloor
n/p\rfloor))/(p-1)+\lfloor n/p\rfloor \\
&=(\lfloor n/p\rfloor -(\sigma_p(n)-n_0))/(p-1)+\lfloor n/p\rfloor \\
&=(\lfloor n/p\rfloor +(p-1)\lfloor n/p\rfloor -\sigma_p(n)+n_0)/(p-1) \\
&=((n-n_0)-\sigma_p(n)+n_0)/(p-1) \\
&=(n-\sigma_p(n))/(p-1) \\
&=\nu_p(n!)
\end{aligned}$$

$\square$

令 $r=n-m$ 且将 $n,m$ 和 $r$ 转换为 $p$ 进制表示（即 $n=\sum_{i=0}^dn_ip^i$ 且 $m$ 和 $r$ 也一样如此表示）。如果在 $p$ 进制下将 $m$ 与 $r$ 相加在第 $j$ 位产生了“进位”，令 $\epsilon_j=1$ 否则 $\epsilon_j=0$ （包括 $\epsilon_{-1}=0$ ）。我们借由上式推导出

!!! quote "Kummer 定理"

    $p$ 的多少次幂整除二项式系数 $\binom{n}{m}$ 为 $m$ 与 $n-m$ 在 $p$ 进制下相加所需要的“进位”次数。

证明：对于每个 $j\geq 0$ 我们可以简单的发现

$$n_j=m_j+r_j+\epsilon_{j-1}-p\epsilon_j$$

而

$$\nu_p\left(\frac{n!}{m!r!}\right)=\nu_p(n!)-\nu_p(m!)-\nu_p(r!)=\frac{\sigma_p(m)+\sigma_p(r)-\sigma_p(n)}{p-1}$$

通过定义我们知道

$$\nu_p\left(\frac{n!}{m!r!}\right)=\sum_{j=0}^d\frac{m_j+r_j-n_j}{p-1}=\frac{p\epsilon_0+\sum_{j=0}^d(p\epsilon_j-\epsilon_{j-1})}{p-1}=\sum_{j=0}^{d-1}\epsilon_j$$

即“进位”的次数。 $\square$

类似的我们有对于 $j\geq 1$

$$\lfloor n/p^j\rfloor -\lfloor m/p^j\rfloor -\lfloor r/p^j\rfloor =\epsilon_{j-1}$$

很显然（事实上好像用这一条足以证明 Kummer 定理）。

通过在定理 1 中的定义，对于 $j\geq 0$ 我们有

$$\lfloor n/p^j\rfloor !/(p^{\lfloor n/p^{j+1}\rfloor}\lfloor n/p^{j+1}\rfloor !)=(\lfloor n/p^j\rfloor !)_p\equiv (\pm 1)^{\lfloor n/p^{j+q}\rfloor}(N_j!)_p\pmod{p^q}$$

通过推论 1 ，将所有 $j\geq 0$ 的同余式相乘得到了

!!! quote "命题 1"

    对于任何整数 $n$ 和素数幂次 $p^q$ ，我们有

    $$n!\Big/p^{\sum_{j\geq 1}\lfloor n/p^j\rfloor}\equiv (\pm 1)^{\sum_{j\geq q}\lfloor n/p^j\rfloor}\prod_{j\geq 0}(N_j!)_p\pmod{p^q}$$
    
    其中 $(\pm 1)$ 与定理 1 中最后一句描述的相同。

至此定理 1 得证。 $\square$

!!! note "例题 [P4720 【模板】扩展卢卡斯](https://www.luogu.com.cn/problem/P4720)"
    
    求二项式系数（组合数）模合数，使用上述方法求出模所有素因子的幂次的解后用 CRT 合并答案即可。

## 任意模数二项卷积

对于一个数列 $\langle a\rangle =a_{0},a_{1},\dots ,a_{n}$ 和 $\langle b\rangle =b_{0},b_{1},\dots ,b_{m}$ 设多项式 $A(x)=\sum_{i=0}^n\frac{a_i}{i!}x^i$ 和 $B(x)=\sum_{i=0}^m\frac{b_i}{i!}x^i$ 和

$$C(x)=A(x)B(x)=\sum_{i=0}^{n+m}\frac{c_i}{i!}x^i$$

为了保证边界情况，我们认为对于 $\forall i\gt n$ 有 $a_{i}=0$ ， $b_{i}$ 同理。显然，根据一般的多项式乘法我们有

$$\frac{c_k}{k!}=\sum_{i=0}^k\frac{a_i}{i!}\frac{b_{k-i}}{(k-i)!}$$

那么

$$c_k=\sum_{i=0}^k\frac{k!}{i!(k-i)!}a_ib_{k-i}=\sum_{i=0}^k\binom{k}{i}a_ib_{k-i}$$

这也是二项卷积名称的由来。而我们知道当 $i\gt k$ 和 $i\lt 0$ 时二项式系数 $\binom{k}{i}=0$ 所以可以直接写作

$$c_k=\sum_{i}\binom{k}{i}a_ib_{k-i}$$

因为合数可以通过中国剩余定理来进行合并，所以只需考虑如何求在模一个素数幂次 $p^q$ 意义下的 $C(x)$ 的系数。这里与上面不同的是 $n,m$ 的范围不大（因为需要考虑卷积的时间），可以预处理出 $n!/p^{\nu_p(n!)}\pmod{p^q}$ 。我们令 $\hat{a}_k=a_k\cdot (k!/p^{\nu_p(k!)})^{-1}\pmod{p^q}$ 那么

$$\hat{c}_k=\sum_{i=0}^kp^{\nu_p(k!)-\nu_p((k-i)!)-\nu_p(i!)}\hat{a}_i\hat{b}_{k-i}\pmod{p^q}$$

剩下是分析可以进行运算的范围，包括上文内容也是参考[^2]中的。注意需要求出 $\hat{c}_k$ 在模“NTT 模数”的意义下，然后进行合并，此时没有除法。

!!! note "例题 [二项卷积](https://loj.ac/p/174)"

    使用两个大“ NTT 模数”或者四个“ NTT 模数”分别进行卷积，合并后可以求出模某个素因子的幂次的答案，后对所有素因子的幂次的解都用 CRT 合并。

[^1]: [Andrew Granville. Arithmetic Properties of Binomial Coefficients I: Binomial Coefficients modulo prime powers.](http://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/binomial.html)
[^2]: <https://blog.csdn.net/EI_Captain/article/details/107456608>
