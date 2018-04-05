function plot_or_gate()
  x = [-1:0.1:2];
  y = 0.5 - x;
  tx = [0 1 1];
  ty = [1 0 1];
  fx = [0];
  fy = [0];
  plot(fx, fy, 'o', 'markersize', 10, tx, ty, 'x', 'color', 'r', 'markersize', 10, x, y, 'color', 'k');
endfunction