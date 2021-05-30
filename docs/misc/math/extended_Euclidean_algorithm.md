扩展欧几里得算法的矩阵解释。考虑在欧几里得整环上运算。

## 矩阵简化

不考虑边界情况的话，我们知道 $\gcd(a,b)=\gcd(b,a\bmod b)$ 是一个递归的过程，尝试用矩阵重写该算法为

$$
\begin{bmatrix}b\\a\bmod b\end{bmatrix}
=
\begin{bmatrix}0&1\\1&-q\end{bmatrix}
\begin{bmatrix}a\\b\end{bmatrix}
$$

其中 $q=\lfloor a/b\rfloor$ ，当然这里向下取整仅适用于整数，若不为整数则需要单独定义。

那么我们所做的无非就是模拟矩阵乘法，不停左乘这样一个在 $\mathbb{Z}^{2\times 2}$ 中的矩阵。而矩阵乘法有结合律，我们可以将所有“余数的矩阵”乘起来得到一个 $2\times 2$ 的矩阵，最后有

$$
\begin{bmatrix}\gcd(a,b)\\0\end{bmatrix}
=
\begin{bmatrix}x_1&x_2\\x_3&x_4\end{bmatrix}
\begin{bmatrix}a\\b\end{bmatrix}
$$

其中 $x_1a+x_2b=\gcd(a,b)$ 给出了一个 Bézout 等式，这也正是扩展欧几里得算法所做的。

!!! note "python 代码（扩展欧几里得）"

    ```python
    def exgcd(a: int, b: int) -> (int, int, int):
        # 返回 (gcd(a,b), x, y) 满足 gcd(a,b)=ax+by
        x1, x2, x3, x4 = 1, 0, 0, 1
        while b != 0:
            q = a // b
            x1, x2, x3, x4, a, b = x3, x4, x1 - x3 * q, x2 - x4 * q, b, a - b * q
        return a, x1, x2
    ```

!!! note "python 代码（逆元）"

    ```python
    def inv_mod(a: int, b: int) -> int:
        # 返回 a^{-1} (mod b)
        x1, x3, m = 1, 0, b
        while b != 0:
            q = a // b
            x1, x3, a, b = x3, x1 - x3 * q, b, a - b * q
        return x1 + m if x1 < 0 else x1
    ```

## 二进制的扩展欧几里得算法

见[^1]的第 14 章。

## 整数及多项式的 HGCD 算法

见[^2]。以后可能会重新写一篇学习 HGCD 算法的笔记，但在这里略过。

[^1]: Alfred J. Menezes, Paul C. van Oorschot and Scott A. Vanstone. [Handbook of Applied Cryptography](http://cacr.uwaterloo.ca/hac/).
[^2]: Chee Keng Yap. [Fundamental Problems in Algorithmic Algebra](http://tomlr.free.fr/Math%E9matiques/Math%20Complete/Algebra/fundamental%20problems%20in%20algorithmic%20algebra%20-%20chee%20keng%20yap.pdf).