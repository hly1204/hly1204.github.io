重新学习了一下线性递推，叉姐的 PPT 的解释感觉非常漂亮。

## 常系数齐次线性递推序列

我们关注这样一个常系数齐次线性递推序列（下简称递推序列）如

$$u_{n+d}=c_{d-1}u_{n+d-1}+\cdots +c_0u_n,\quad n\geq 0$$

我们说这样一个递推是 $d$ 阶的。对于 $N\geq 0$ ，求 $u_N$ 最简便的处理方式是将其转换为矩阵的形式如：

$$\underbrace{\begin{bmatrix}
u_{n}\\u_{n+1}\\\vdots\\u_{n+d-1}
\end{bmatrix}}_{\mathbf{v}_{n}}=\underbrace{\begin{bmatrix}
&1&&\\
&&\ddots&\\
&&&1\\
c_{0}&c_{1}&\cdots&c_{d-1}
\end{bmatrix}}_{\mathbf{M}}\times\underbrace{\begin{bmatrix}
u_{n-1}\\u_{n}\\\vdots\\u_{n+d-2}
\end{bmatrix}}_{\mathbf{v}_{n-1}},\quad n\geq 1$$

若这个递推序列是在 $\mathbb{R}$ 上，不难发现在 $\mathbb{R}^{d\times d}$ 上关于 $\mathbf{v}$ 这个向量的递推阶为 $1$ ，通常采用的方法是矩阵快速幂。

不难发现 $\mathbf{v}$ 可以描述成一个线性组合为

$$\mathbf{v}_{n+d}=\sum_{i=0}^{d-1}c_i\mathbf{v}_{n+i}$$

进一步的可以写成

$$\mathbf{M}^d\mathbf{v}_n=\sum_{i=0}^{d-1}c_i\mathbf{M}^i\mathbf{v}_n$$

我们可以找到一个多项式 $\Gamma(x)=x^d-\sum_{i=0}^{d-1}c_ix^i$ 满足 $\Gamma(\mathbf{M})=0$ 。

令 $g(x)=g_0+g_1x+\cdots +g_{d-1}x^{d-1}=x^N\bmod{\Gamma(x)}$ 那么 $g(\mathbf{M})=\mathbf{M}^N$ ，也就是我们将 $\mathbf{M}^N$ 描述为了一个线性组合如

$$\mathbf{M}^N\mathbf{v}_0=\sum_{i=0}^{d-1}g_i\mathbf{M}^i\mathbf{v}_0\implies \mathbf{v}_N=\sum_{i=0}^{d-1}g_i\mathbf{v}_i$$

观察 $\mathbf{v}_i$ 的第一行我们不难得出答案。

!!! note "可能的优化"
    
    计算 $x^N\bmod{\Gamma(x)}$ 不难让我们联想到计算模奇素数平方根的 Cipolla 算法，其实质也为一个二阶的递推，这里我们是否可以利用 Montgomery reduction 的思想进行一些优化呢，毕竟只需要其余数。

## 新的算法

学习论文[^1]与[^2]中的解读后我们得到了一个常数更小的实现且无需直接的幂级数倒数算法和多项式取模，实现更为简便。我们将递推序列使用生成函数表示如

$$F(x)=\sum_{n\geq 0}u_nx^n$$

且令 $Q(x)=1-c_{d-1}x-\cdots -c_0x^d$ 为 $\Gamma(x)$ 系数翻转后的多项式，那么能找到一个多项式 $P(x)$ 满足

$$F(x)=\frac{P(x)}{Q(x)}$$

注意这里 $F(x)$ 为形式幂级数而 $P(x)$ 和 $Q(x)$ 为多项式。而 $F(x)$ 的前 $d$ 项和 $Q(x)$ 都是已知的，我们观察求 $P(x)$ 的过程有

$$P(x)=Q(x)F(x)$$

而其中

$$[x^n]\left(Q(x)F(x)\right)=u_n-\sum_{i=1}^{d}c_{d-i}u_{n-i}=0, \quad n\geq d$$

也就是说虽然 $P(x)$ 是一个多项式而非形式幂级数，但有理函数 $P(x)/Q(x)$ 已经包含了 $F(x)$ 的所有信息！我们只需消耗一次多项式乘法就能得到 $P(x)$ 。

接下来我们考虑一个变形使得分母为一个偶函数且令 $V(x^2)=Q(x)Q(-x)$ 和 $U(x)=P(x)Q(-x)$ 并将 $U(x)$ 分为了两部分为 $U(x)=U_e(x^2)+x\cdot U_o(x^2)$ 下标 $e$ 表示 even 而 $o$ 表示 odd 。

$$F(x)=\frac{P(x)Q(-x)}{Q(x)Q(-x)}=\frac{U_e(x^2)}{V(x^2)}+x\cdot \frac{U_o(x^2)}{V(x^2)}$$

我们发现后式中这两个有理函数的展开中 $x$ 的奇数次幂的系数都是零，那么假设我们需要求 $[x^N]F(x)$ 则只需要递归到其中一侧

$$[x^N]F(x)=\begin{cases}[x^{N/2}]\frac{U_e(x)}{V(x)}&\text{if } N\bmod 2=0 \\
[x^{(N-1)/2}]\frac{U_o(x)}{V(x)}& \text{if }N\bmod 2=1\end{cases}$$

我们需要付出两次度数为 $d$ 的多项式乘法。

!!! note "更细致的优化"

    我们不维护这个有理函数的分子和分母“多项式的形式”，而是维护他们“ DFT 序列的形式”。依然考虑在 [快速傅里叶变换](4-10-2021-FFT.md) 中的算法，我们得到的结果是一个 $f(1),f(-1),f(\mathrm{i}),f(-\mathrm{i}),\dots$ 的一个序列，第一个与第二个，第三个与第四个都是多项式 $f$ 在互为相反数的两个点的点值。我们维护了 $Q(x)$ 的 DFT 序列，那么 $Q(-x)$ 的 DFT 序列无非就是两两交换这些点值！那么很容易求出 $V(x^2)$ 的 DFT 序列，而因为 $V(x^2)$ 是偶函数，那么问题是如何使其变成 $V(x)$ 的 DFT 序列。这依然可以通过观察 DFT 序列得到，因为 $V(\mathrm{i}^2)=V(-1)$ 那么只需要用在 $V(\mathrm{i})$ 位置的点值替代 $V(-1)$ 处的点值即可（因为现在 $V(-1)=V(1)$ 所以 $V(-1)$ 是“没有意义”的），以此类推。但是这样的问题是，该 DFT 序列的长度减少为原先的一半了，于是在这之前我们使用 Twisted FFT 带给我们的方法“倍长 $Q(x)$ 的 DFT 序列”即可，也同时得到了倍长后的 $Q(-x)$ 序列给下面的分子处理使用。

    分子的处理方法也是类似的，首先我们求出 $U(x)$ 的 DFT 序列，之前要倍长 $P(x)$ 的 DFT 序列。对于 $U_e(x^2)=(U(x)+U(-x))/2$ 对应到点值也是一样的计算，这个序列的长度也变为了原先的一半，但我们之前已经倍长过了，可以保留足够信息。

    而 $U_o(x^2)=(U(x)-U(-x))/2x$ 那么对于每个 $U(\zeta)$ 还需要调整为 $U(\zeta)/\zeta$ 。

    通过观察 FFT 算法的分治树也可以得到结论：多项式 $f$ 的 $n\gt \deg(f)$ 长 DFT 序列的和为 $nf(0)$ （可能需要一些证明）。

事实上上述优化在[^1]中有详细描述，但因为我们之前对 FFT 算法已经有过详细分析，不难自己推导出来，不需要借助原论文。

## LSB 与 MSB 算法

见[^1]中后文的详细分析，上面的算法为 LSB 算法，原文也提供了其 MSB 算法， EI 教了我 MSB 可以认为是上述算法的转置，而 MSB 常数稍大，但可以求出连续 $d$ 项以及加速最初的多项式取模的算法，我也并未深入阅读仅作了尝试的实现。从而也导出了一个更快的计算矩阵幂次的算法（我们寻找矩阵的特征多项式 $\Gamma(x)$ 并求出 $g(x)=x^N\bmod{\Gamma(x)}$ 后计算 $g(\mathbf{M})$ ，注意这里需要用 baby-step-giant-step 算法）。

## 新的幂级数倒数算法（ Graeffe 方法）

学习论文作者的博客[^3]中，若我们想求一个给定幂级数 $Q(x)\in \mathbb{R}[[x]]$ 的倒数

$$\frac{1}{Q(x)}\bmod{x^{2N}}$$

有

$$\begin{aligned}\frac{1}{Q(x)}\bmod{x^{2N}}&=Q(-x)\frac{1}{Q(x)Q(-x)}\bmod{x^{2N}}\\
&=Q(-x)\frac{1}{V(x^2)}\bmod{x^{2N}}\\
&=Q(-x)S(x^2)\bmod{x^{2N}}\end{aligned}$$

那么问题减少为了原先的一半，因为我们只需求出 $S(x)\equiv 1/V(x)\pmod{x^{N}}$ 。

??? note "洛谷例题 [P4238 【模板】多项式乘法逆](https://www.luogu.com.cn/problem/P4238)"

    代码可能比较老，如果以后更新这里未必会更新，该算法常数大约与未优化的牛顿迭代相当。

    ```cpp
    #ifndef LOCAL
    #define NDEBUG
    #endif
    #include <algorithm>
    #include <cassert>
    #include <cstring>
    #include <functional>
    #include <initializer_list>
    #include <iostream>
    #include <memory>
    #include <queue>
    #include <random>
    #include <vector>

    std::uint64_t get_len(std::uint64_t n) { // if n=0, boom
      return --n, n |= n >> 1, n |= n >> 2, n |= n >> 4, n |= n >> 8, n |= n >> 16, n |= n >> 32, ++n;
    }

    template <typename Mint> std::pair<const Mint *, const Mint *> init(int n) {
      static int lim = 0;
      static constexpr Mint G(Mint::get_pr());
      static Mint ROOT[1 << 20], IROOT[1 << 20];
      if (lim == 0) {
        ROOT[0] = IROOT[0] = 1;
        ROOT[1 << 19] = G.pow(Mint::get_mod() - 1 >> 21),
                  IROOT[1 << 19] = G.pow(Mint::get_mod() - 1 - (Mint::get_mod() - 1 >> 21));
        for (int i = 18; i != -1; --i)
          ROOT[1 << i] = ROOT[1 << i + 1] * ROOT[1 << i + 1],
                    IROOT[1 << i] = IROOT[1 << i + 1] * IROOT[1 << i + 1];
        lim = 1;
      }
      while ((lim << 1) < n) {
        for (int i = lim + 1, e = lim << 1; i < e; ++i)
          ROOT[i] = ROOT[i - lim] * ROOT[lim], IROOT[i] = IROOT[i - lim] * IROOT[lim];
        lim <<= 1;
      }
      return {ROOT, IROOT};
    }

    template <typename Mint> void dft(int n, Mint x[], const Mint *ROOT) {
      for (int j = 0, l = n >> 1; j != l; ++j) {
        Mint u = x[j], v = x[j + l];
        x[j] = u + v, x[j + l] = u - v;
      }
      for (int i = n >> 1; i >= 2; i >>= 1) {
        for (int j = 0, l = i >> 1; j != l; ++j) {
          Mint u = x[j], v = x[j + l];
          x[j] = u + v, x[j + l] = u - v;
        }
        for (int j = i, l = i >> 1, m = 1; j != n; j += i, ++m) {
          Mint root = ROOT[m];
          for (int k = 0; k != l; ++k) {
            Mint u = x[j + k], v = x[j + k + l] * root;
            x[j + k] = u + v, x[j + k + l] = u - v;
          }
        }
      }
    }

    template <typename Mint> void idft(int n, Mint x[], const Mint *ROOT) {
      for (int i = 2; i < n; i <<= 1) {
        for (int j = 0, l = i >> 1; j != l; ++j) {
          Mint u = x[j], v = x[j + l];
          x[j] = u + v, x[j + l] = u - v;
        }
        for (int j = i, l = i >> 1, m = 1; j != n; j += i, ++m) {
          Mint root = ROOT[m];
          for (int k = 0; k != l; ++k) {
            Mint u = x[j + k], v = x[j + k + l];
            x[j + k] = u + v, x[j + k + l] = (u - v) * root;
          }
        }
      }
      Mint iv(Mint(n).inv());
      for (int j = 0, l = n >> 1; j != l; ++j) {
        Mint u = x[j] * iv, v = x[j + l] * iv;
        x[j] = u + v, x[j + l] = u - v;
      }
    }

    template <typename Mint> void dft(int n, Mint x[]) { dft(n, x, init<Mint>(n).first); }

    template <typename Mint> void idft(int n, Mint x[]) { idft(n, x, init<Mint>(n).second); }

    template <typename Mint> std::vector<Mint> inv_helper_func(std::vector<Mint> Q) {
      int n = Q.size();
      if (n == 1) return {Q[0].inv()};
      // Q(x)Q(-x)=V(x^2)
      // 递归求 1/V(x) 的前 n/2 项，还原出 1/V(x^2) 的前 n 项，与 Q(-x) 卷积截取前 n 项即可
      Q.resize(n << 1, 0);
      dft(n << 1, Q.data());
      std::vector<Mint> V(n << 1);
      for (int i = 0, j = 0; i != n << 1; i += 2) V[j++] = Q[i] * Q[i ^ 1];
      idft(n, V.data());
      V.resize(n >> 1);
      auto S = inv_helper_func(V);
      S.resize(n << 1, 0);
      dft(n, S.data());
      std::vector<Mint> res(n << 1);
      for (int i = 0; i != n << 1; ++i) res[i] = Q[i ^ 1] * S[i >> 1];
      idft(n << 1, res.data());
      res.resize(n);
      return res;
    }

    template <typename Mint> std::vector<Mint> inv(std::vector<Mint> x) {
      int n = x.size(), len = get_len(n);
      x.resize(len);
      auto res = inv_helper_func(x);
      return res.resize(n), res;
    }

    template <std::uint32_t P> struct ModInt32 {
    public:
      using i32 = std::int32_t;
      using u32 = std::uint32_t;
      using i64 = std::int64_t;
      using u64 = std::uint64_t;
      using m32 = ModInt32;

    private:
      u32 v;

      static constexpr u32 get_r() {
        u32 iv = P * (2U - P * P);
        return iv *= 2U - P * iv, iv *= 2U - P * iv, iv * (P * iv - 2U);
      }
      static constexpr u32 r = get_r(), r2 = -u64(P) % P;
      static_assert((P & 1) == 1);
      static_assert(-r * P == 1);
      static_assert(P < (1 << 30));
      static constexpr u32 pow_mod(u32 x, u64 y) {
        u32 res = 1;
        for (; y != 0; y >>= 1, x = u64(x) * x % P)
          if (y & 1) res = u64(res) * x % P;
        return res;
      }
      static constexpr u32 reduce(u64 x) { return x + u64(u32(x) * r) * P >> 32; }
      static constexpr u32 norm(u32 x) { return x - (P & -(P - 1 - x >> 31)); }

    public:
      static constexpr u32 get_mod() { return P; }
      static constexpr u32 get_pr() {
        u32 tmp[32] = {}, cnt = 0;
        const u32 phi = P - 1;
        u32 m = phi;
        for (u32 i = 2; i * i <= m; ++i)
          if (m % i == 0) {
            tmp[cnt++] = i;
            while (m % i == 0) m /= i;
          }
        if (m != 1) tmp[cnt++] = m;
        for (u32 res = 2; res != P; ++res) {
          bool flag = true;
          for (u32 i = 0; i != cnt && flag; ++i) flag &= pow_mod(res, phi / tmp[i]) != 1;
          if (flag) return res;
        }
        return 0;
      }
      ModInt32() = default;
      ~ModInt32() = default;
      constexpr ModInt32(u32 v) : v(reduce(u64(v) * r2)) {}
      constexpr ModInt32(const m32 &) = default;
      constexpr u32 get() const { return norm(reduce(v)); }
      explicit constexpr operator u32() const { return get(); }
      explicit constexpr operator i32() const { return i32(get()); }
      constexpr m32 &operator=(const m32 &) = default;
      constexpr m32 operator-() const {
        m32 res;
        return res.v = (P << 1 & -(v != 0)) - v, res;
      }
      constexpr m32 inv() const {
        i32 x1 = 1, x3 = 0, a = get(), b = P;
        while (b != 0) {
          i32 q = a / b, x1_old = x1, a_old = a;
          x1 = x3, x3 = x1_old - x3 * q, a = b, b = a_old - b * q;
        }
        return m32(x1 + P);
      }
      constexpr m32 &operator+=(const m32 &rhs) {
        return v += rhs.v - (P << 1), v += P << 1 & -(v >> 31), *this;
      }
      constexpr m32 &operator-=(const m32 &rhs) { return v -= rhs.v, v += P << 1 & -(v >> 31), *this; }
      constexpr m32 &operator*=(const m32 &rhs) { return v = reduce(u64(v) * rhs.v), *this; }
      constexpr m32 &operator/=(const m32 &rhs) { return this->operator*=(rhs.inv()); }
      friend m32 operator+(const m32 &lhs, const m32 &rhs) { return m32(lhs) += rhs; }
      friend m32 operator-(const m32 &lhs, const m32 &rhs) { return m32(lhs) -= rhs; }
      friend m32 operator*(const m32 &lhs, const m32 &rhs) { return m32(lhs) *= rhs; }
      friend m32 operator/(const m32 &lhs, const m32 &rhs) { return m32(lhs) /= rhs; }
      friend bool operator==(const m32 &lhs, const m32 &rhs) { return norm(lhs.v) == norm(rhs.v); }
      friend bool operator!=(const m32 &lhs, const m32 &rhs) { return norm(lhs.v) != norm(rhs.v); }
      friend std::istream &operator>>(std::istream &is, m32 &rhs) {
        return is >> rhs.v, rhs.v = reduce(u64(rhs.v) * r2), is;
      }
      friend std::ostream &operator<<(std::ostream &os, const m32 &rhs) { return os << rhs.get(); }
      constexpr m32 pow(i64 y) const {
        m32 res(1), x(*this);
        for (; y != 0; y >>= 1, x *= x)
          if (y & 1) res *= x;
        return res;
      }
    };

    int main() {
    #ifdef LOCAL
      std::freopen("..\\in", "r", stdin), std::freopen("..\\out", "w", stdout);
    #endif
      std::ios::sync_with_stdio(false);
      std::cin.tie(0);
      using mint = ModInt32<998244353>;
      int n;
      std::cin >> n;
      std::vector<mint> a(n);
      for (auto &i : a) std::cin >> i;
      for (auto i : inv(a)) std::cout << i << ' ';
      return 0;
    }
    ```

[^1]: [Alin Bostan, Ryuhei Mori. A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence.](https://arxiv.org/abs/2008.08822)
[^2]: [EntropyIncreaser 的洛谷博客](https://www.luogu.com.cn/blog/EntropyIncreaser/solution-p4723)
[^3]: [線形漸化的数列のN項目の計算](https://qiita.com/ryuhe1/items/da5acbcce4ac1911f47a)
