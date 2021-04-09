MathJax = { tex: {inlineMath: [['$', '$']], displayMath: [['$$', '$$']]} };
(function() {
  var style = document.createElement('style');
  style.type = 'text/css';
  style.innerHTML = '.MathJax {outline:0;}'; // 设置 MathJax 边框宽度
  document.head.appendChild(style);
})();