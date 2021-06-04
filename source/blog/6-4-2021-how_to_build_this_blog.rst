=================
如何构造这个博客
=================
说实话这个东西我也是第一次接触，与 Markdown 语法的简单不同，这里使用 reStructuredText_ 来构造，语法稍复杂但功能却非常丰富。

而构造文档的交给 Sphinx_ 来完成，其中有一些扩展也是 reStructuredText_ 没有的。

很大一部分用法是参考了 `reStructuredText 简介`_ 中的。

我在这里统一采用 3 个空格的缩进。

使用 ``pip install -U sphinx`` 安装 Sphinx 后使用编译命令 ``sphinx-build -b html source build`` 即可。

代码块
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

导入代码文件
----------------

.. literalinclude:: ../conf.py
   :linenos:
   :language: py

数学公式
----------------
对于关于 :math:`x` 的多项式 :math:`ax^2+bx+c` 其根为

.. math::
   :label: 1

   \frac{-b\pm \sqrt{b^2-4ac}}{2a}

:eq:`1` 是正确的。

.. _reStructuredText: https://docutils.sourceforge.io/rst.html
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _reStructuredText 简介: https://self-contained.github.io/reStructuredText/index.html