# 如何构建这个博客

不知道以什么开头，就以这个为第一篇博客吧。

在[^1]和[^2]中，我使用了 python 安装了相关的软件，并按照这两个网站上的提示进行配置和运行。

目前的 `mkdocs.yml` 文件设置为（可能不全）

??? note "mkdocs.yml"

    ```yaml
    site_name: hly1204 的博客

    repo_url: https://github.com/hly1204/hly1204.github.io # 仓库 url

    repo_name: hly1204/hly1204.github.io # 仓库名

    nav:
        - 主页: index.md
        - 文章:
            - 如何构建这个博客: how_to_build_this_blog.md

    theme:
      name: material # 主题名，必须，否则为默认
      language: zh
      direction: ltr # 从左到右
      palette:
          primary: indigo # 主题颜色
          scheme: default # 亮色主题
          accent: indigo # 超链接的颜色
      features:
          - navigation.tabs # 有上方的标签
          - header.autohide # 自动收起
      icon:
          repo: fontawesome/solid/trash # 右上角仓库的标志

    extra_javascript:
        - javascripts/load_MathJax.js # 加载 MathJax
        - javascripts/highlight.pack.js # 加载代码高亮
        - javascripts/load_highlight.js
        - javascripts/MathJax/es5/tex-chtml.js

    extra_css:
        - stylesheets/github.css # 代码高亮的样式

    extra:
        social: # 右下角的
          - icon: fontawesome/brands/github
            link: https://github.com/hly1204
            name: hly1204 on github

    markdown_extensions:
        - toc:
            permalink: "&para;"
            baselevel: 2
    ```

其中 `load_MathJax.js` 为

!!! note "load_MathJax.js"
    
    ```javascript
    MathJax = { tex: {inlineMath: [['$', '$']], displayMath: [['$$', '$$']]} };
    (function() {
      var style = document.createElement('style');
      style.type = 'text/css';
      style.innerHTML = '.MathJax {outline:0;}'; // 设置 MathJax 边框宽度
      document.head.appendChild(style);
    })();
    ```

`highlight.pack.js` 为从[^3]下载的文件，仅包括了 cpp 等部分语法的高亮，这也是为什么下方的 javascript 代码没有高亮。

`MathJax` 文件夹里为[^4]仓库中的文件（很幸运的是他们是开源的），而

`load_highlight.js` 为

!!! note "load_highlight.js"
    
    ```javascript
    (function() {
      hljs.highlightAll();
    })();
    ```

这样的好处就是，可以只编写很容易书写的 Markdown 文件，用 mkdocs 来生成对应的 html 文件，并且有很漂亮的排版，这比我原先自己所写的 html 文件高明到不知道哪里去了。

# 需要注意的问题

在 Markdown 中的 $\LaTeX$ 公式换行需要打四个反斜杠才行。以及一些可能出现问题的情况，大部分是转义字符的问题。

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

[^1]: [MkDocs](https://www.mkdocs.org/)
[^2]: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
[^3]: [highlight.js](https://highlightjs.org/)
[^4]: [MathJax Github](https://github.com/mathjax/MathJax)
