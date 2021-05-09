节点还是结点，似乎我以前没有太过注意，可能称 node 为节点而 vertex 为结点更恰当，而 edge 为边， arc 为弧是合理的，但是可能不影响理解。

## 向前星存图

在网络流以及一些图论算法中，向前星（ forward star ）[^2]是非常高效的存储方式。若为简单我们可以考虑使用 `std::vector<std::vector<Edge>> g` 来在线的存图，然后对 `g[u]` 遍历访问 $u$ 的出边（有向图的话），但如此一来的话，这个空间由 `std::vector` 来决定了，若要精确控制则需要浪费时间。而向前星无非就是统计结点的出度并将这些边按照结点顺序放在一个数组如 `std::vector<Edge>` 中，后构造一个索引数组表示每个结点出边开始的索引即可，但是需要对图进行离线，然后统一放入，过程实际上类似于后缀数组的 SA-IS 算法中的诱导排序，而空间我们可以精确控制。

## Dinic 算法

!!! note ""

    据说 Dinic 算法（或 Dinitz 算法）原先并非目前流行的写法，目前写法为 Tarjan 简化而来。

这里的 current arc 即当前弧（我有时也叫当前边）的结构可能是 Tarjan 引入的，因为原 Dinic 算法并不是使用这种方式。另外这里不论是单次 DFS 或是多次 DFS 应该仅常数差异。

???+ note "例题 [最大流](https://loj.ac/p/127)"

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

    template <typename CapacityType> struct MaximumFlowGraph {
    public:
      struct InputEdge {
        int from, to;
        CapacityType cap;
        InputEdge(int from, int to, CapacityType cap)
            : from(from), to(to), cap(cap) {}
        ~InputEdge() = default;
      };

      struct Edge {
        int to;
        CapacityType cap;
      };

      MaximumFlowGraph(int n) : n(n) {}
      ~MaximumFlowGraph() = default;

      void add_directed_edge(int from, int to, CapacityType cap) {
        ie.emplace_back(from, to, cap);
      }

      CapacityType get_max_flow(int s, int t) {
        convert_to_forwardstar();
        CapacityType max_flow = 0;
        const CapacityType CAPACITY_LIM = std::numeric_limits<CapacityType>::max();
        while (create_layer_graph(s, t)) {
          cur_e = idx;
          max_flow += augment(s, CAPACITY_LIM, t);
        }
        return max_flow;
      }

      void convert_to_forwardstar() {
        int m = ie.size() << 1;
        e.resize(m);
        idx.assign(n + 1, 0);
        rev_idx.resize(m);
        for (auto &i : ie) ++idx[i.from], ++idx[i.to];
        for (int i = 0, sum = 0; i != n + 1; ++i)
          sum += idx[i], idx[i] = sum - idx[i];
        for (auto &i : ie) {
          e[idx[i.from]].to = i.to;
          e[idx[i.from]].cap = i.cap;
          e[idx[i.to]].to = i.from;
          e[idx[i.to]].cap = 0;
          rev_idx[idx[i.from]] = idx[i.to];
          rev_idx[idx[i.to]] = idx[i.from];
          ++idx[i.from];
          ++idx[i.to];
        }
        for (int i = n - 1; i > 0; --i) idx[i] = idx[i - 1];
        idx[0] = 0;
      }

      bool create_layer_graph(int s, int t) {
        level.assign(n, -1);
        std::queue<int> q;
        q.push(s);
        level[s] = 0;
        while (!q.empty()) {
          int u = q.front();
          q.pop();
          for (int i = idx[u], i_end = idx[u + 1]; i < i_end; ++i)
            if (e[i].cap > 0 && level[e[i].to] == -1) {
              level[e[i].to] = level[u] + 1;
              q.push(e[i].to);
            }
        }
        return level[t] != -1;
      }

      CapacityType augment(int from, CapacityType bottleneck, int t) {
        if (bottleneck == 0 || from == t) return bottleneck;
        CapacityType max_flow = 0;
        for (int &i = cur_e[from], i_end = idx[from + 1]; i < i_end; ++i) {
          if (level[e[i].to] == level[from] + 1 && e[i].cap > 0) {
            CapacityType flow = augment(e[i].to, std::min(bottleneck, e[i].cap), t);
            if (flow == 0) continue;
            e[i].cap -= flow;
            e[rev_idx[i]].cap += flow;
            max_flow += flow;
            bottleneck -= flow;
            if (bottleneck == 0) break;
          }
        }
        return max_flow;
      }

    private:
      const int n; // n 个 vertex 且编号在 [0,n-1] 范围内
      std::vector<InputEdge> ie;
      std::vector<Edge> e;
      std::vector<int> idx, rev_idx, cur_e, level;
    };

    int main() {
    #ifdef LOCAL
      std::freopen("..\\in", "r", stdin), std::freopen("..\\out", "w", stdout);
    #endif
      std::ios::sync_with_stdio(false);
      std::cin.tie(0);
      int n, m, s, t;
      std::cin >> n >> m >> s >> t;
      MaximumFlowGraph<long long> g(n + 1);
      while (m--) {
        long long u, v, w;
        std::cin >> u >> v >> w;
        g.add_directed_edge(u, v, w);
      }
      std::cout << g.get_max_flow(s, t);
      return 0;
    }
    ```

## 最大标号算法

最大标号的预流推进算法，或者叫推送/重贴标签算法，是一样的。对于 $G=(V,E,u,s,t)$ 其中 $u$ 是容量函数，源汇分别为 $s$ 和 $t$ 。

简单来说需要使得 $V\setminus \{s,t\}$ 的溢出函数为零。

在[^1]中有详细的优化方法，这里仅作一个简要解释。我们将算法分为两个阶段，第一阶段，考虑只推送距离标号小于 $\vert V\vert$ 的结点，这样最后求得最大流的值就是汇的溢出函数，但是网络此时不满足一些约束。第二阶段将标号大于等于 $\vert V\vert$ 的结点的溢出推送回源，但是注意，汇不管了，因为上面说的除了源和汇之外的溢出函数为零。考虑不使用一个极大值放到源，只需要在算法开始时将所有源的出边满流推送出去即可。第二阶段明显比第一阶段更快。

考虑两个启发式操作：

- gap 启发：即在第一阶段的某一时刻对于一个整数 $g\lt \vert V\vert$ 若不存在当前距离标号的结点了，那么标号更高的结点都无法到达汇（标号设置为 $\vert V\vert$ ），注意，这里标号更高的都是非活跃的结点，需要一个数据结构来维护这些，一般为链表的数组，或者链表的链表之类的，比较麻烦（如果全部结点进行一次判断那不如不写）；
- global relabel 启发：考虑在算法开始前计算准确的距离函数，且在每 $\vert V\vert$ 次或 $\vert E\vert /2$ 次重贴标签后进行一次从汇的反向 BFS 来计算准确的距离函数（简言之，周期性执行）。注意这里第一阶段需要从汇反向 BFS 而第二阶段是从源反向 BFS 。

!!! warning ""

    我们很明确所有的推送和重贴标签实际上都是“局部”的操作，而 global relabel 可以说是“全局”的操作。

!!! warning "为什么不用优先队列？"

    在[^3]中我们看到，该算法的瓶颈在于所谓的不饱和推送，所谓饱和就是其容量减去流量已经为零了，则称这条边饱和了，那么这次推送也是饱和的，否则这次推送不饱和，那么很显然不饱和推送导致一个活跃（ active ）的结点变为不活跃，若使用优先队列（优先队列中标号大的在前，每次取出标号最大的）我们要删除队列中的这个结点，而删除操作看起来在没办法做到 $O(1)$ 。

以上几点优化代码中都没有包含，以前写过第二个启发式操作，但是不够精细优化有限。

!!! warning ""

    如果只进行第一阶段，那么最后的剩余网络图是不能用的，只能获取到最大流。

???+ note "例题 [最大流](https://loj.ac/p/127)"

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

    template <typename CapacityType> struct MaximumFlowGraph {
    public:
      struct InputEdge {
        int from, to;
        CapacityType cap;
        InputEdge(int from, int to, CapacityType cap)
            : from(from), to(to), cap(cap) {}
        ~InputEdge() = default;
      };

      struct Edge {
        int to;
        CapacityType cap;
      };

      struct LinkedListNode {
        LinkedListNode *before, *after;
      };

      struct LinkedList {
        LinkedListNode *head;
        LinkedList() : head(new LinkedListNode) {
          head->before = head->after = head;
        }
        ~LinkedList() { delete head; }
        static void extract(LinkedListNode *x) {
          x->before->after = x->after;
          x->after->before = x->before;
          x->before = x->after = nullptr;
        }
        void insert(LinkedListNode *x) {
          x->after = head->after;
          x->before = head;
          x->after->before = x->before->after = x;
        }
        bool is_empty() const { return head->after == head; }
        LinkedListNode *begin() const { return head->after; }
        LinkedListNode *end() const { return head; }
      };

      MaximumFlowGraph(int n) : n(n) {}
      ~MaximumFlowGraph() = default;

      void add_directed_edge(int from, int to, CapacityType cap) {
        ie.emplace_back(from, to, cap);
      }

      CapacityType get_max_flow(int s, int t) {
        convert_to_forwardstar();
        dist.assign(n, 0);
        dist[s] = n;
        excess.assign(n, 0);
        bucket.clear();
        bucket.resize(n << 1);
        auto is_in_bucket = [&](int from) -> bool {
          return (first_node + from)->before != nullptr;
        };
        largest_label = -1;
        first_node = new LinkedListNode[n];
        for (int i = 0; i != n; ++i)
          (first_node + i)->before = (first_node + i)->after = nullptr;
        for (int i = idx[s], i_end = idx[s + 1]; i < i_end; ++i) {
          CapacityType flow = e[i].cap;
          excess[s] -= flow;
          excess[e[i].to] += flow;
          e[i].cap = 0;
          e[rev_idx[i]].cap += flow;
          if (e[i].to != t && excess[e[i].to] > 0 && !is_in_bucket(e[i].to)) {
            bucket[0].insert(first_node + e[i].to);
            largest_label = 0;
          }
        }
        cur_e = idx;
        while (largest_label >= 0) {
          // process-vertex & discharge
          int v = bucket[largest_label].begin() - first_node;
          LinkedList::extract(first_node + v);
          const int next_label = dist[v] - 1;
          for (int &i = cur_e[v], i_end = idx[v + 1]; i < i_end && excess[v] > 0;
               ++i) {
            if (e[i].cap > 0 && dist[e[i].to] == next_label) {
              CapacityType flow = std::min(excess[v], e[i].cap);
              excess[v] -= flow;
              excess[e[i].to] += flow;
              e[i].cap -= flow;
              e[rev_idx[i]].cap += flow;
              if (e[i].to != t && excess[e[i].to] > 0 && !is_in_bucket(e[i].to))
                bucket[next_label].insert(first_node + e[i].to);
            }
          }
          if (excess[v] > 0) {
            int min_label = n << 1;
            for (int i = cur_e[v] = idx[v], i_end = idx[v + 1]; i < i_end; ++i) {
              if (e[i].cap > 0 && dist[e[i].to] < min_label)
                min_label = dist[e[i].to];
            }
            largest_label = dist[v] = min_label + 1;
            bucket[largest_label].insert(first_node + v);
          } else {
            while (largest_label >= 0 && bucket[largest_label].is_empty())
              --largest_label;
          }
        }
        delete[] first_node;
        return excess[t];
      }

      void convert_to_forwardstar() {
        int m = ie.size() << 1;
        e.resize(m);
        idx.assign(n + 1, 0);
        rev_idx.resize(m);
        for (auto &i : ie) ++idx[i.from], ++idx[i.to];
        for (int i = 0, sum = 0; i != n + 1; ++i)
          sum += idx[i], idx[i] = sum - idx[i];
        for (auto &i : ie) {
          e[idx[i.from]].to = i.to;
          e[idx[i.from]].cap = i.cap;
          e[idx[i.to]].to = i.from;
          e[idx[i.to]].cap = 0;
          rev_idx[idx[i.from]] = idx[i.to];
          rev_idx[idx[i.to]] = idx[i.from];
          ++idx[i.from];
          ++idx[i.to];
        }
        for (int i = n - 1; i > 0; --i) idx[i] = idx[i - 1];
        idx[0] = 0;
      }

    private:
      const int n; // n 个 vertex 且编号在 [0,n-1] 范围内
      std::vector<InputEdge> ie;
      std::vector<Edge> e;
      std::vector<int> idx, rev_idx, cur_e, dist;
      std::vector<CapacityType> excess;
      LinkedListNode *first_node;
      std::vector<LinkedList> bucket;
      int largest_label;
    };

    int main() {
    #ifdef LOCAL
      std::freopen("..\\in", "r", stdin), std::freopen("..\\out", "w", stdout);
    #endif
      std::ios::sync_with_stdio(false);
      std::cin.tie(0);
      int n, m, s, t;
      std::cin >> n >> m >> s >> t;
      MaximumFlowGraph<long long> g(n + 1);
      while (m--) {
        long long u, v, w;
        std::cin >> u >> v >> w;
        g.add_directed_edge(u, v, w);
      }
      std::cout << g.get_max_flow(s, t);
      return 0;
    }
    ```

[^1]: Cherkassky, B.V. and Goldberg, A.V. On implementing push-relabel method for the maximum flow problem. Algorithmica 19, 4 (1997), 390410.
[^2]: Ravindra K. Ahuja, Thomas L. Magnanti, and James B. Orlin. Network Flows. Theory, Algorithms, and Applications.
[^3]: <http://www.cs.cornell.edu/~eva/Network.Flow.Algorithms.pdf>