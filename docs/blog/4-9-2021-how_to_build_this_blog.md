## 如何构建这个博客

不知道以什么开头，就以这个为第一篇博客吧。

我使用了 python 安装了相关的软件，并按照这几个网站[^1][^2]上的提示进行配置和运行。

## 格式

为了方便，这里出现的代码都使用 clang-format 进行格式化，且单行一般不超过 80 个字符（排版限制）。

一般文章的格式为，对不同语言及公式之间加空格，无论在哪里。

## MathJax 风格

在[^5]中提到了很多避免与 Markdown 语言冲突的写法，在我的 Library 中会采用这种写法，但在这里因为 MkDocs 使用 Python 来翻译成 HTML 文件所以不会造成错误。尤其需要注意的是对于集合的两个括号转义，以及下划线，这是经常遇到的。

[^1]: [MkDocs](https://www.mkdocs.org/)
[^2]: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
[^3]: [highlight.js](https://highlightjs.org/)
[^4]: MathJax [Github](https://github.com/mathjax/MathJax)
[^5]: kimiyuki. [MathJax と Markdown で可搬性のある数式を書くには](https://kimiyuki.net/blog/2020/02/19/portable-mathjax-markdown/).