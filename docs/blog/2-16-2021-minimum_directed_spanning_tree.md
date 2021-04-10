有向图的最小生成树，国内一般也称作“最小树形图”。这篇文章基本上是一个翻译，但有所简略，详见[^1]。

# 基本定义

!!! quote "定义"

    令 $G=(V,E,w)$ 为一个边有权的有向图。其中 $w:E\to\mathbb{R}$ 为一个函数定义了边权。令 $r\in V$ 。一个 $G$ 的有向图生成树（简称为 DST ）以 $r$ 为根为 $G$ 的子图 $T$ 满足其无向的版本为一棵树且包含了所有从 $r$ 到任意 $V$ 中的节点（ vertex ）的路径。花销 $w(T)$ 为所有边的花销之和，即 $w(T)=\sum_{e\in T}w(e)$ 。一个以 $r$ 为根的有向图的最小生成树（ MDST ）为以 $r$ 为根的 DST 中花销最小的。一个有向图包含了一棵以 $r$ 为根的 DST 当且仅当 $G$ 中所有点都能从 $r$ 到达。而这个性质是可以被简单的在线性时间测试的。

!!! quote "引理 1.1"

    下列条件是等价的

    - $T$ 为一棵以 $r$ 为根的 DST 。
    - $r$ 在 $T$ 中的入度为零，其余 $T$ 中节点的入度为一，且 $T$ 是无环的。
    - $r$ 在 $T$ 中的入度为零，其余 $T$ 中节点的入度为一，且从 $r$ 有路径到其余任何 $T$ 中的节点。

上述引理容易证明，假设 $r$ 能到其余 $T$ 中的任何节点，那么意味着 $r$ 的出度至少为一，因为其余所有点的入度都为一，肯定不能存在环，否则至少有一个除了 $r$ 之外的节点的入度是大于一的。

在 $T$ 中我们说一个节点 $u$ 是 $v$ 的后代当且仅当有一条路径从 $v$ 到 $u$ 。根据 引理 1.1 我们马上有推论：

!!! quote "推论 1.2"

    令 $T$ 为以 $r$ 为根的 DST 。令 $(u,v)\in E$ 为一条不在 $T$ 中的边且 $v\neq r$ 并且在 $T$ 中 $u$ 不是 $v$ 的后代。令 $(u',v)$ 为在 $T$ 中进入 $v$ 的唯一的一条边。那么 $T\cup \\{(u,v)\\}\setminus \\{(u',v)\\}$ 也是一棵 DST 。

上面推论很显然，因为我们知道从 $r$ 出发的 DST 能到达任何节点，那么也一定能到达 $u$ 点。

# Edmonds 的算法

令 $G=(V,E,w)$ 且 $r\in V$ 并且假设 $G=(V,E)$ 存在以 $r$ 为根的 DST 。令 $F$ 为 $n-1$ 条其余节点花销最小的入边。如果我们足够幸运， $F$ 是无环的，那么根据 引理 1.1 他是一棵 DST 且为 MDST 。而一般 $F$ 包含“若干个”环。

令 $C$ 为一个环不包含 $r$ 但包含了所有花销最小的入边。显然 MDST 不能包含 $C$ 中的所有边，但我们说有一个 MDST 包含了 $C$ 中除了某一条边之外的所有边。

!!! quote "引理 4.1"

    令 $G=(V,E,w)$ 为一个边有权的有向图且令 $r\in V$ 。令 $C$ 为一个 $G$ 中的有向圈包含了所有除了 $r$ 之外花销最小的入边。那么存在一个 MDST 包含了 $C$ 中除了某一条边之外的所有边。

证明：令 $T$ 为 $G$ 在 $r$ 的 MDST 。令 $v_1$ 为一个 $C$ 上的节点且在 $T$ （注意这里的“在 $T$ 中”是很关键的）中 $r$ 到 $v_1$
的路径上不经过其他任何节点。（一定会存在至少一个这样的节点即从 $r$ 出发最近的节点“之一”）令 $v_1,v_2,\dots,v_k$ 为 $C$ 上的节点且按照他们出现的顺序。如果 $(v_1,v_2),(v_2,v_3),\dots ,(v_{k-1},v_k)\in T$ 那么结束了。因为前面提到 $T$ 包含了除了 $C$ 中一条边之外的所有边，那么 $T=C\cup \\{(r,v_1)\\}\setminus \\{(v_k,v_1)\\}$ 。但是如果 $(v_1,v_2),\dots ,(v_{i-1},v_i)\in T$ 但是 $(v_i,v_{i+1})\notin T$ 在某个 $i\lt k$ 。令 $(u,v_{i+1})\in T$ 为 $v_{i+1}$ 在 $T$ 中的入边。 $v_i$ 在 $T$ 中的祖先有 $T$ 上 $r$ 到 $v_1$ 上的节点和 $C$ 上 $v_1,v_2,\dots ,v_{i-1}$ 。因此 $v_i$ 不是 $v_{i+1}$ 的后代。通过 推论 1.2 有 $T'=T\cup \\{(v_i,v_{i+1})\\}\setminus \\{(u,v_{i+1})\\}$ 也是一棵以 $r$ 为根的 DST 。因为 $(v_i,v_{i+1})$ 为 $v_{i+1}$ 入边中花销最小的，我们有 $w(v_i,v_{i+1})\leq w(u,v_{i+1})$ 因此 $w(T')\leq w(T)$ 。因此 $T'$ 也是以 $r$ 为根的 MDST 。至此我们可以构造以 $r$ 为根的 MDST 包含将 $C$ 中除了 $(v_k,v_1)$ 之外的所有边。

假设 $C$ 包含了所有花销最小的入边。我们知道可以 MDST 包含了 $C$ 中的所有边除了某一条，但是是哪条呢？我们应该丢弃哪条？ Edmonds 给出了一个优雅的解决方法。我们收缩环 $C$ 为一个超级节点，记 $\overline G$ 为收缩后的图，并更新收缩后的所有入边，在收缩后的图中递归的找到一棵以 $r$ 为根的 MDST $\overline T$ 。如果边 $\overline e\in \overline T$ 在 $\overline G$ 中为 $C$ 的入边，而收缩前这条边为 $e=(u,v)$ 是环 $C$ 中的 $v$ 的入边。我们将 $C$ 中除了 $v$ 的入边之外的所有边都加入 $\overline T$ 中，我们会在后文说明这就是原图 $G$ 的 MDST 。接下来我们将这个实现形式化并证明其正确性。

令 $C$ 为 $G$ 中的一个环并令 $\overline G=G/C$ 为收缩 $C$ 之后的图。形式化的，如果 $C$ 为边 $(v_1,v_2),\dots ,(v_{k-1},v_k),(v_k,v_1)$ 组成，那么 $\overline G$ 中包含的点集为 $V\cup \\{c\\}\setminus \\{v_1,\dots ,v_k\\}$ 即环 $C$ 由超级节点 $c$ 替代。而边集 $\overline E=\\{\overline e\neq (c,c)\mid e\in E\\}$ 其中若 $e=(u,v)$ 那么 $\overline e=(\overline u,\overline v)$ （注意 $(c,c)$ 的自环被移除，但是重边会被保留）。通过上述记号，我们确认了对于 $\overline E$ 中的每条边是由 $E$ 中如何变化而来的，并且假设 $\overline E\subseteq E$ 。

在图 $G$ 的以 $r$ 为根的 DSTs 包含了 $C$ 中除了某条边之外的所有边和 $\overline G$ 的以 $r$ 为根的 DSTs 之间有一个很自然的一对一的联系。如果 $T$ 为以 $r$ 为根的 DST 且 $T\cap C=C\setminus \\{e\\}$ ，那么 $\overline T=T\setminus (C\setminus \\{e\\})$ 为 $\overline G$ 以 $r$ 为根的 DST 。相反的，如果 $\overline T$ 是 $\overline G$ 以 $r$ 为根的 DST ，我们可以“展开”它为 DST ，记为 $G$ 的 $\exp(\overline T)$ 。令 $e\in \overline E$ 为 $\overline T$ 中 $c$ 的入边。如果 $e=(u,v)$ 其中 $v\in C$ ，令 $e'=(u',v)$ 为 $C$ 中 $v$ 的入边。我们令

$$\exp(\overline T)=\overline T\cup (C\setminus \\{e'\\})$$

即 $\exp(\overline T)$ 为将 $C$ 上除了 $e'$ 的所有边加入 $\overline T$ 形成的。那么容易检验 $\exp(\overline T)$ 为 $G$ 以 $r$ 为根的 DST 且包含了 $C$ 中除了某一条边的所有边。也容易检验 $\overline T$ 为 $\overline G$ 的以 $r$ 为根的 DST 且关联 $G$ 的 DST $T$ 那么 $\exp(\overline T)=T$ 。

若 $e=(u,v)\in E$ 为超级节点 $c$ 的入边，我们令 $e_C=(u',v)$ 为 $C$ 中 $v$ 的入边。接下来我们定义一个新的花销函数 $\overline w:E\to \mathbb{R}$ 为

$$\overline w(e)=\begin{cases}w(e)-w(e_C)&\text{if }e\text{ enters }C\\\\w(e)&\text{otherwise}\end{cases}$$

!!! quote "引理 4.2"

    令 $G=(V,E,w)$ 为一个边有权的有向图。令 $r\in V$ 。令 $C$ 为 $G$ 中一个有向环。令 $T$ 为 $G$ 以 $r$ 为根的 DST 满足 $\vert T\cap C\vert =\vert C\vert -1$ 即 $T$ 包含了 $C$ 中除了某条边之外的所有边。且令 $\overline T$ 为 $\overline G=G/C$ 的 DST ，与 $T$ 相关联，那么有
    $$\overline w(\overline T)=w(T)-w(C)$$

证明：假设 $T\cap C=C\setminus \\{e\\}$ 。那么 $\overline T=T\setminus (C\setminus \\{e\\})$ 。令 $e'$ 为 $T$ 中进入 $C$ 的入边（注意 $e$ 和 $e'$ 在 $C$ 为 $C$ 中同一个节点的入边）。那么

$$\begin{aligned}\overline w(\overline T)&=(w(T)-w(C\setminus \\{e\\}))-w(e)\\\\&=w(T)-w(C)\end{aligned}$$

注意 $w(C\setminus \{e\})$ 被减去是因为 $\overline T$ 是由 $T$ 中移除 $C\setminus \\{e\\}$ 形成的。花销 $w(e)$ 被减去是因为 $w(\overline e')=w(e')-w(e)$ 。对于其余边 $e''\in \overline T$ 我们有 $\overline w(e'')=w(e'')$ 。

我们现在有

!!! quote "定理 4.3"

    令 $G=(V,E,w)$ 为一个边有权的有向图。令 $r\in V$ 。令 $C$ 为 $G$ 中一个不包含 $r$ 的有向环且由所有花销最小的入边组成。令 $\overline G=G/C$ 和 $\overline w:E\to \mathbb{R}$ 为前面定义的。令 $\overline T$ 为 $\overline G$ 的以 $r$ 为根的 MDST 且 $\overline w$ 定义如上。那么 $\exp(\overline T)$ 为 $G$ 以 $r$ 为根的 MDST 。

证明：通过 引理 4.1 存在以 $r$ 为根的 MDST $T^\star$ 包含了除了 $C$ 中某条边之外的所有边。令 $\overline{T^\star}$ 为 $\overline G$ 的 DST 关联为 $T^\star$ 。令 $T=\exp(\overline T)$ 。通过 引理 4.2 我们有 $\overline w(\overline T)=w(T)-w(C)$ 且 $\overline w(\overline{T^\star})=w(T^\star)-w(C)$ 。因为 $\overline T$ 为 $\overline G$ 的 MDST ，我们知道 $\overline w(\overline T)\leq \overline w(\overline{T^\star})$ 。因此 $w(T)\leq w(T^\star)$ 且 $T$ 也是为以 $r$ 为根的 MDST 。

这引出了下面这种寻找 MDST 的算法。除了根节点，选择花销最便宜的入边直到形成 DST 那么这也是 MDST ，或者直到形成了一个环 $C$ 。如果环 $C$ 形成了，那么我们收缩这个环并适当调整相关的边权。然后在收缩后的图中找到 MDST 再展开为原图的 MDST 即可。

[^1]: Uri Zwick. Lecture notes on "Analysis of Algorithms": Direcetd Minimum Spanning Tree.
