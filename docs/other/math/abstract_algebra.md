这是我学习抽象代数基础的一些笔记。非常不完善，暂时不放出来了。

## 一些记号

对于使用 $\exists !$ 表示唯一存在。

令 $S$ 和 $T$ 为两个集合。

- $S\times T =\{(a,b)\mid a\in S,b\in T\}$ 。我们定义这样一个新的集合为 $S$ 和 $T$ 的直积（或笛卡尔积）。
- 没有任何元素的集合为空集，记作 $\emptyset$ 。当 $S\cap T=\emptyset$ 时我们说 $S$ 和 $T$ 是不相交的。而两个不相交集合的并经常记作 $S\coprod T$ 。

!!! quote "定义"

    一个从 $S$ 到 $T$ 的映射（或函数） $f$ 是给在 $S$ 中的每个元素分配一个 $T$ 中 **唯一** 的元素。我们用下面的记号来表示这种信息。

    $$\begin{aligned}f:&S\to T\\
    &x\mapsto f(x)\end{aligned}$$

!!! quote "定义"

    令 $S$ 和 $T$ 为两个集合，且 $f:S\to T$ 为一个映射。

    1. 我们说 $S$ 为 $f$ 的域（ domain ）且 $T$ 为 $f$ 的陪域（ codomain ）。
    2. 若 $S=T$ 且 $f(x)=x,\forall x\in S$ 我们说 $f$ 是一个 identity 映射，记作 $f=\operatorname{Id}_S$ 。
    3. 若 $f(x)=f(y)\implies x=y,\forall x,y\in S$ 那么我们说 $f$ 是单射（ injective ）。
    4. 若 $y\in T$ 存在 $x\in S$ 满足 $f(x)=y$ 那么我们说 $f$ 是满射（ surjective ）。
    5. 若 $f$ 既是单射又是满射，我们说 $f$ 是双射（ bijective ）。这意味着 $f$ 使得 $S$ 和 $T$ 中的元素一一对应。

    观察到若 $R,S,T$ 为集合且 $g:R\to S$ 和 $f:S\to T$ 那么我们可以使其复合得到一个新的函数 $f\circ g:R\to T$ 。注意仅当 $f$ 的域包含于 $g$ 的陪域时才可能。

