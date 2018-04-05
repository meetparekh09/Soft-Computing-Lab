function plot_xor_gate()
  x = [-1:0.1:2];
  y = 0.5 - x;
  tx = [0 1];
  ty = [1 0];
  fx = [0 1];
  fy = [0 1];
  plot(fx, fy, 'o', 'markersize', 10, tx, ty, 'x', 'color', 'r', 'markersize', 10, x, y, 'color', 'k');
endfunction