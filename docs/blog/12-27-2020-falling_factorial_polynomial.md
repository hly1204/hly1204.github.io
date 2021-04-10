这里主要是学习了一下下降幂多项式的基础（非常基础的），对于所有多项式，认为属于 $\mathbb{F}_{p}[x]$ ，对于所有形式幂级数，认为属于 $\mathbb{F}_{p}[[x]]$ 。

一般认为 $\deg(0)=-\infty$ 。这篇文章可能会持续的补充一些内容。

## 下降幂多项式

对于 $\exp(x)$ 显然有 $\exp'(x)=\exp(x)$ 也可记作 $\mathrm{e}^{x}$ ，应用麦克劳林公式有

$$\mathrm{e}^{x}=1+\frac{x}{1!}+\frac{x^{2}}{2!}+\cdots =\sum_{i\geq 0}\frac{x^{i}}{i!}$$

看起来与下降幂多项式无关。设下降幂多项式 $A(x)=\sum_{i=0}^{m-1}a_{i}x^{\underline{i}}$ ，其中 $x^{\underline{i}}$ 的角标下有下划线（也有其他表示方法，但这里采用这种），其中

$$x^{\underline{i}}=x(x-1)\cdots (x-i+1)=\frac{x!}{(x-i)!}$$

我们定义算子 $\Delta$ 应用于函数表示 $\Delta(f(x))=f(x+1)-f(x)$ ，那么

$$\begin{aligned}
\Delta(x^{\underline{m}})&=(x+1)^{\underline{m}}-x^{\underline{m}}\\
&=(x+1)x(x-1)\cdots (x-m+2)-x(x-1)\cdots (x-m+1)\\
&=mx(x-1)\cdots (x-m+2)\\
&=mx^{\underline{m-1}}
\end{aligned}$$

可以验证上面的 $m$ 对于整数都是成立的。二项式定理也有下降幂和上升幂的版本。

## 下降幂多项式与连续点值

考虑上述下降幂多项式 $A(x)$ 从 $0$ 开始的连续整数点值的指数生成函数 $C(x)=\sum_{i\geq 0}\frac{A(i)}{i!}x^{i}$ ，我们发现对于 $x^{\underline{m}}$ 的从 $0$ 开始的连续整数点值的指数生成函数为

$$\sum_{i\geq m}\frac{i!}{(i-m)!i!}x^{i}=\sum_{i\geq m}\frac{x^{i}}{(i-m)!}=\mathrm{e}^{x}x^{m}$$

设 $A(x)$ 系数的生成函数为 $D(x)=\sum_{i\geq 0}a_{i}x^{i}$ ，那么 $C(x)=\mathrm{e}^{x}D(x)$ 且 $D(x)=\mathrm{e}^{-x}C(x)$ 。

我们可以在一次多项式乘法的时间将下降幂多项式系数与连续点值间转换。

!!! note "例题 [P5383 普通多项式转下降幂多项式](https://www.luogu.com.cn/problem/P5383)"

    模板题
    
!!! note "例题 [P5393 下降幂多项式转普通多项式](https://www.luogu.com.cn/problem/P5393)"

    模板题，可结合多点求值和插值算法或使用其他分治方法？

## 多项式平移

给出多项式 $A(x)=\sum_{i=0}^{n}a_{i}x^{i}$ 且 $\deg(A(x))=n\gt 0$ ，要求 $A(x+c)$ 的系数，我们在 $c$ 处应用泰勒公式，有

$$A(x)=A(c)+\frac{A'(c)}{1!}(x-c)+\frac{A''(c)}{2!}(x-c)^{2}+\cdots +\frac{A^{(n)}(c)}{1!}(x-c)^{n}$$

那么 $A(x+c)$ 实际上就是

$$A(x+c)=A(c)+\frac{A'(c)}{1!}x+\frac{A''(c)}{2!}x^{2}+\cdots +\frac{A^{(n)}(c)}{1!}x^{n}$$

而观察 $A^{(t)}(c)$ 发现

$$A^{(t)}(c)=\sum_{i=t}^{n}a_{i}i!\frac{c^{i-t}}{(i-t)!}$$

也能在一次多项式乘法的时间完成。下降幂多项式也可以通过类似的方法平移，能解决 [洛谷例题 3](https://www.luogu.com.cn/problem/P5667) 。

## 斯特林数

斯特林数一般分为两类，我们记 ${n\brace k}$ 为第二类斯特林数， ${n\brack k}$ 为第一类斯特林数。其中，第二类斯特林数的符号有点类似于集合的符号，也叫斯特林子集数，而第一类为斯特林轮换数。下面给出在[^2]中 p215 的一个表格

| $n$ | ${n\brace 0}$ | ${n\brace 1}$ | ${n\brace 2}$ | ${n\brace 3}$ | ${n\brace 4}$ | ${n\brace 5}$ | ${n\brace 6}$ | ${n\brace 7}$ | ${n\brace 8}$ | ${n\brace 9}$ |
|:-:|-|-|-|-|-|-|-|-|-|-|
| 0 | 1 |  |  |  |  |  |  |  |  |  |
| 1 | 0 | 1 |  |  |  |  |  |  |  |  |
| 2 | 0 | 1 | 1 |  |  |  |  |  |  |  |
| 3 | 0 | 1 | 3 | 1 |  |  |  |  |  |  |
| 4 | 0 | 1 | 7 | 6 | 1 |  |  |  |  |  |
| 5 | 0 | 1 | 15 | 25 | 10 | 1 |  |  |  |  |
| 6 | 0 | 1 | 31 | 90 | 65 | 15 | 1 |  |  |  |
| 7 | 0 | 1 | 63 | 301 | 350 | 140 | 21 | 1 |  |  |
| 8 | 0 | 1 | 127 | 966 | 1701 | 1050 | 266 | 28 | 1 |  |
| 9 | 0 | 1 | 255 | 3025 | 7770 | 6951 | 2646 | 462 | 36 | 1 |

先从第二类斯特林数说起， ${n\brace k}$ 表示将 $n$ 个物品分为 $k$ 个非空子集的方案数。注意到上表格中有一个特例，即 ${0\brace 0}=1$ 把 $0$ 件物品分为 $0$ 个非空子集，我们认为只存在一种方法。而对于 $n\gt 0$ 不存在这样的方法，故 ${n\brace 0}=0$ 。下面，我们观察其与下降幂多项式之间非常密切的关系，显然我们有以下等式

$$\begin{aligned}
x^{0}&=x^{\underline{0}}\\
x^{1}&=x^{\underline{1}}\\
x^{2}&=x^{\underline{2}}+x^{\underline{1}}\\
x^{3}&=x^{\underline{3}}+3x^{\underline{2}}+x^{\underline{1}}\\
x^{4}&=x^{\underline{4}}+6x^{\underline{3}}+7x^{\underline{2}}+x^{\underline{1}}
\end{aligned}$$

我们断言对于整数 $n\geq 0$ 有

$$x^{n}=\sum_{k}{n\brace k}x^{\underline{k}}$$

证明可见[^2]p219 ，摘抄如下

考虑使用归纳法，因为有 $x\cdot x^{\underline{k}}=(x-k)x^{\underline{k}}+kx^{\underline{k}}=x^{\underline{k+1}}+kx^{\underline{k}}$ ，那么 $x^{n}=x\cdot x^{n-1}$ 有

$$\begin{aligned}
x\sum_{k}{n-1\brace k}x^{\underline{k}}&=\sum_{k}{n-1\brace k}x^{\underline{k+1}}+\sum_{k}{n-1\brace
k}kx^{\underline{k}}\\
&=\sum_{k}{n-1\brace k-1}x^{\underline{k}}+\sum_{k}{n-1\brace k}kx^{\underline{k}}\\
&=\sum_{k}\left(k{n-1\brace k}+{n-1\brace k-1}\right)x^{\underline{k}}\\
&=\sum_{k}{n\brace k}x^{\underline{k}}
\end{aligned}$$

其中倒数第二步是一个很重要的递归式， ${n-1\brace k}$ 表示将 $n-1$ 个物品划分为 $k$ 个非空子集，现在 ${n\brace k}$ 多了一个物品，那么新物品有两种可能性，可以与其他物品一起放在上一次划分的任意 $k$ 个集合中的一个，或者在单独的一个子集，所以 ${n\brace k}=k{n-1\brace k}+{n-1\brace k-1}$ 。

接下来说第一类斯特林数， ${n\brack k}$ 表示将 $n$ 个物品分为 $k$ 个非空轮换的方案数，所谓轮换我们认为其为一个圈，即

$$[A,B,C,D]=[B,C,D,A]=[C,D,A,B]=[D,A,B,C]$$

但是显然 $[A,B,C,D]\neq [A,C,B,D]$ 。这在子集中我们认为是等价的，但是轮换中认为不等价，即为不同方案。事实上[^2]告诉我们对于整数 $n,k\geq 0$ 有

$${n\brack k}\geq {n\brace k}$$

下面给出在[^2]中 p216 的一个表格

| $n$ | ${n\brack 0}$ | ${n\brack 1}$ | ${n\brack 2}$ | ${n\brack 3}$ | ${n\brack 4}$ | ${n\brack 5}$ | ${n\brack 6}$ | ${n\brack 7}$ | ${n\brack 8}$ | ${n\brack 9}$ |
|:-:|-|-|-|-|-|-|-|-|-|-|
| 0 | 1 |  |  |  |  |  |  |  |  |  |
| 1 | 0 | 1 |  |  |  |  |  |  |  |  |
| 2 | 0 | 1 | 1 |  |  |  |  |  |  |  |
| 3 | 0 | 2 | 3 | 1 |  |  |  |  |  |  |
| 4 | 0 | 6 | 11 | 6 | 1 |  |  |  |  |  |
| 5 | 0 | 24 | 50 | 35 | 10 | 1 |  |  |  |  |
| 6 | 0 | 120 | 274 | 225 | 85 | 15 | 1 |  |  |  |
| 7 | 0 | 720 | 1764 | 1624 | 735 | 175 | 21 | 1 |  |  |
| 8 | 0 | 5040 | 13068 | 13132 | 6769 | 1960 | 322 | 28 | 1 |  |
| 9 | 0 | 40320 | 109584 | 118124 | 67284 | 22449 | 4536 | 546 | 36 | 1 |

我们发现斯特林轮换数有一些特殊的性质，如对于整数 $n\gt 0$ 有 ${n\brack 1}=(n-1)!$ ，这是因为排在首位和排在末位是一样的，那么总共就是 $n-1$ 个位置的全排列。而且也有

$${n\brack n}={n\brace n}=1,{n\brack n-1}={n\brace n-1}={n\choose 2}$$

模仿第二类斯特林数，我们也容易推出其递归的公式为对于 $n\gt 0$ 有 ${n\brack k}=(n-1){n-1\brack k}+{n-1\brack k-1}$ ，这也是因为将一个物品加入一个轮换，那么方案数为这个轮换包含的物品数量，因为这个物品可以插入在原来任意两个物品之间或者首位或末位，而首位和末位是一样的，于是恰好有 $n-1$ 种位置，加上单独为一个轮换的方案即可。

可以通过与第二类斯特林数类似的方法证明

$$x^{\overline{n}}=\sum_{k}{n\brack k}x^{k}$$

因为我们有 $(x+n-1)\cdot x^{k}=x^{k+1}+(n-1)x^{k}$ ，那么 $x^{\overline{n}}$ 等于

$$\begin{aligned}
(x+n-1)x^{\overline{n-1}}&=(x+n-1)\sum_{k}{n-1\brack k}x^{k}\\
&=(n-1)\sum_{k}{n-1\brack k}x^{k}+\sum_{k}{n-1\brack k-1}x^{k}\\
&=\sum_{k}{n\brack k}x^{k}
\end{aligned}$$

!!! note "例题 [第二类斯特林数-行](https://www.luogu.com.cn/problem/P5395)"

    对于多项式 $x^{n}$ 我们只需求得其在 $0,1,\dots ,n$ 的点值的指数生成函数，再乘上 $\mathrm{e}^{-x}$ 就得到了一行（行指上述表格中的一行）的解。在[^1]中指出可以通过筛法在线性的时间求得这 $n+1$ 个点的点值，而我未加思考只使用了快速幂的方法，虽不会成为复杂度的瓶颈，但依然是落了下乘。

!!! note "例题 [第一类斯特林数-行](https://www.luogu.com.cn/problem/P5408)"

    对于多项式 $x^{\overline{n}}$ 我们只需求出其通常幂的表示，显然可以分治。但我们又发现

    $$x^{\overline{n}}=\begin{cases}
    x^{\overline{n/2}}(x+n/2)^{\overline{n/2}}&\text{if }n\text{
    is even}\\
    (x+n-1)x^{\overline{(n-1)/2}}(x+(n-1)/2)^{\overline{(n-1)/2}}&\text{else}
    \end{cases}$$

    这指导我们只需求出 $x^{\overline{\lfloor n/2\rfloor }}$ 的通常幂表示，可以通过多项式平移得到 $(x+\lfloor n/2\rfloor)^{\overline{\lfloor n/2\rfloor}}$ 的通常幂表示。

!!! note "例题 [第二类斯特林数-列](https://www.luogu.com.cn/problem/P5396)"

    这里我们需要引入生成函数，在[^2]中 p294 表格中有

    $$(x^{-1})^{\overline{-m}}=\frac{x^{m}}{(1-x)(1-2x)\cdots (1-mx)}=\sum_{n\geq 0}{n\brace m}x^{n}$$

    如果我们将分母变成 $(x-1)(x-2)\cdots (x-m)$ 那么显然可以用上面的方法计算，最后得到乘积之后再将系数“翻转”即可。另一种方法为使用下面的生成函数

    $$(\mathrm{e}^{x}-1)^{m}=m!\sum_{n\geq 0}{n\brace m}\frac{x^{n}}{n!}$$

    两者可能仅效率不同，都可以得到正确答案。

!!! note "例题 [第一类斯特林数-列](https://www.luogu.com.cn/problem/P5409)"

    与上面同样的，有生成函数

    $$\left(\ln\frac{1}{1-x}\right)^{m}=m!\sum_{n\geq 0}{n\brack m}\frac{x^{n}}{n!}$$

## 有符号斯特林数

注意到上面定义的第一类斯特林数是非负的（因为是在组合意义下的），而在 [Wolfram](https://mathworld.wolfram.com/StirlingNumberoftheFirstKind.html) 上使用的为有符号斯特林数的定义。在 [Library Checker](https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind) 上也采用了相同的定义，但是互相之间可以转换。今天我在群里提问，非常谢谢 EI 和群友教我这个。

[^1]: 罗煜翔. 《具体数学》选讲.
[^2]: 高德纳等. 具体数学.