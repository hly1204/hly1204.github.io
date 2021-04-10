## 如何构建这个博客

不知道以什么开头，就以这个为第一篇博客吧。

我使用了 python 安装了相关的软件，并按照这几个网站[^1][^2]上的提示进行配置和运行。

## 格式

为了方便，这里出现的代码都使用 clang-format 进行格式化，且风格为：

!!! note ".clang-format"
    ```
    BasedOnStyle: LLVM
    Standard: Cpp11
    PointerAlignment: Right
    UseTab: Never
    IndentWidth: 2
    AccessModifierOffset: -2
    AllowShortIfStatementsOnASingleLine: true
    AlwaysBreakTemplateDeclarations: false
    AllowShortLoopsOnASingleLine: true
    ColumnLimit: 100
    ```

一般文章的格式为，对不同语言及公式之间加空格，无论在哪里。

[^1]: [MkDocs](https://www.mkdocs.org/)
[^2]: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
[^3]: [highlight.js](https://highlightjs.org/)
[^4]: [MathJax Github](https://github.com/mathjax/MathJax)
