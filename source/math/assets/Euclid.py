def exgcd(a: int, b: int):
    # 返回 (gcd(a,b), x, y) 满足 gcd(a,b)=ax+by
    x1, x2, x3, x4 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        x1, x2, x3, x4, a, b = x3, x4, x1 - x3 * q, x2 - x4 * q, b, a - b * q
    return a, x1, x2


def inv_mod(a: int, b: int):
    # 返回 a^{-1} (mod b)
    x1, x3, m = 1, 0, b
    while b != 0:
        q = a // b
        x1, x3, a, b = x3, x1 - x3 * q, b, a - b * q
    return x1 + m if x1 < 0 else x1


def generalized_crt2(a: int, m1: int, b: int, m2: int):
    # m1 和 m2 不必互素
    # a >= 0 且 b >= 0
    a, b = a % m1, b % m2
    d, x, y = exgcd(m1, m2)
    bma = b - a
    if bma % d != 0:
        return -1, -1
    t, y = m2 // d, bma // d
    res = x * y % t  # 取模运算导致 res 在 python 中默认为非负的
    return res * m1 + a, m1 * t


# -- 修改上面内容需要同步修改引用该文件的 rst 文件内容！！！
if __name__ == '__main__':
    print(inv_mod(2, 998244353) * 2 % 998244353)
