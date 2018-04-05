function plot_nand_gate()
  x = [-1:0.1:2];
  y = 1.5 - x;
  tx = [0 0 1];
  ty = [0 1 0];
  fx = [1];
  fy = [1];
  plot(fx, fy, 'o', 'markersize', 10, tx, ty, 'x', 'color', 'r', 'markersize', 10, x, y, 'color', 'k');
endfunction