function plot_nor_gate()
  x = [-1:0.1:2];
  y = 0.5 - x;
  tx = [0];
  ty = [0];
  fx = [0 1 1];
  fy = [1 0 1];
  plot(fx, fy, 'o', 'markersize', 10, tx, ty, 'x', 'color', 'r', 'markersize', 10, x, y, 'color', 'k');
endfunction