function plot_and_gate()
  x = [-1:0.1:2];
  y = 1.5 - x;
  tx = [1];
  ty = [1];
  fx = [0 0 1];
  fy = [0 1 0];
  plot(fx, fy, 'o', 'markersize', 10, tx, ty, 'x', 'color', 'r', 'markersize', 10, x, y, 'color', 'k');
endfunction