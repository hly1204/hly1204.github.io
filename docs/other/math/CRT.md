把中国剩余定理的代码补全。这里仅讨论 $\mathbb{Z}$ 。

## 两两合并

在 [这里](../../blog/12-23-2020-multipoint_evaluation_and_interpolation.md) 稍微讲了一些，对于整数也是一样的。考虑已知关于 $A$ 的同余方程组

$$\begin{cases}A\equiv a_1\pmod{M_1}\\A\equiv a_2\pmod{M_2}\end{cases}$$

若 $\gcd(M_1,M_2)=1$ 那么存在整数 $k_1,k_2$ 满足

$$A=a_1+k_1M_1=a_2+k_2M_2\implies a_1\equiv a_2+k_2M_2\pmod{M_1}$$

可用 [扩展欧几里得算法](extended_Euclidean_algorithm.md) 中的函数求出

$$k_2\equiv (a_1-a_2)M_2^{-1}\pmod{M_1}$$

代入 $k_2$ 在模 $M_1$ 下的值发现满足方程组，可求出 $A\bmod (M_1M_2)$ 。

!!! note "python 代码"

    ```python
    def crt2(a: int, m1: int, b: int, m2: int) -> (int, int):
        # m1 与 m2 互素
        # a >= 0 且 b >= 0
        a, b, x = a % m1, b % m2, inv_mod(m1, m2)
        return (m2 + b - a % m2) * x % m2 * m1 + a, m1 * m2
    ```

## 同时合并及 Garner 算法

见[^1]，其中 Garner 算法更适合预处理后使用中国剩余定理用模若干不同素数的余数来表示一个大整数（值域小于所有素数的乘积）然后快速合并出答案。

## 中国剩余定理的推广

上面的方法仅适用于模数互素的情况，否则我们依然考虑上述关于 $A$ 的同余方程组，此时令 $d=\gcd(M_1,M_2)$ 那么假设存在整数 $k_1,k_2$ 满足

$$A=k_1M_1+a_1=k_2M_2+a_2\implies k_1M_1-k_2M_2=a_2-a_1\tag{1}$$

我们用 [扩展欧几里得算法](extended_Euclidean_algorithm.md) 中的函数求出 $x,y$ 满足 $xM_1+yM_2=d$ 。

我们有

$$\begin{cases}k_1M_1/d\equiv (a_2-a_1)/d\pmod{(M_2/d)}\\xM_1/d\equiv 1\pmod{(M_2/d)}\end{cases}$$

那么

$$k_1\equiv x(a_2-a_1)/d\pmod{(M_2/d)}$$

!!! warning ""

    若 $d\nmid (a_2-a_1)$ 则无解，因为在 $(1)$ 中后一个等式左侧显然是 $d$ 的倍数，而右侧若不是则不满足 $k_1,k_2$ 为整数的假设。

可求出 $A\bmod{(M_1M_2/d)}$ 。

!!! note "python 代码"

    ```python
    def generalized_crt2(a: int, m1: int, b: int, m2: int) -> (int, int):
        # m1 和 m2 不必互素
        # a >= 0 且 b >= 0
        a, b = a % m1, b % m1
        d, x, y = exgcd(m1, m2)
        bma = b - a
        if bma % d != 0:
            return -1, -1
        t, y = m2 // d, bma // d
        res = x * y % t
        if res < 0:
            res += t
        return res * m1 + a, m1 * t
    ```

[^1]: [Alfred J. Menezes, Paul C. van Oorschot and Scott A. Vanstone. Handbook of Applied Cryptography.](http://cacr.uwaterloo.ca/hac/)
