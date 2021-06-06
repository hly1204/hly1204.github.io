:Date: 2021-6-4
:Author: hly1204
:Status: 待补充

=================
如何构造这个博客
=================

简介
------------------

说实话这个东西我也是第一次接触，与 Markdown 语法的简单不同，这里使用 reStructuredText_ 来构造，语法稍复杂但功能却非常丰富。

而构造文档的交给 Sphinx_ 来完成，其中有一些扩展也是 reStructuredText_ 没有的。

很大一部分用法是参考了 `reStructuredText 简介`_ 中的。

我在这里统一采用 3 个空格的缩进。

使用 ``pip install -U sphinx`` 安装 Sphinx 后使用编译命令 ``sphinx-build -b html source build`` 即可。

对于行内代码块，我使用 ````test()```` 前后各两个包裹，对于加粗字体我使用 ``**加粗**`` 表示。

对于术语的英文和参考文献我使用脚注的形式来标注，用 ``.. rubric:: 脚注`` 作为标题，后跟 ``.. [#b] 内容`` 来表示 ``[#b]_`` 的内容，注意前后空格。

这种标注作为一个类似于“标题”的存在但不会被包含到目录中。

代码块示例
----------------

.. code-block:: py
   :linenos:
   :caption: test
   :name: 示例

   def gcd(a, b):
       if a % b == 0:
           return b
       else:
           return gcd(b, a % b)

导入代码文件示例
----------------

.. literalinclude:: ../conf.py
   :linenos:
   :language: py

数学公式示例
----------------
对于关于 :math:`x` 的多项式 :math:`ax^2+bx+c` 其根为

.. math::
   :label: 1

   \frac{-b\pm \sqrt{b^2-4ac}}{2a}

:eq:`1` 是正确的。

表格示例
----------------
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+

.. _reStructuredText: https://docutils.sourceforge.io/rst.html
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _reStructuredText 简介: https://self-contained.github.io/reStructuredText/index.html