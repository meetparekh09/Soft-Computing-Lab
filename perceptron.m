function weight = perceptron(x, o)
  c = 0.1;
  w = [rand(); rand(); rand()];
  for j = 1:100
    for i = 1:size(x, 1)
      net = x(i, :)*w;
      if (net >= 0)
        oi = 1;
      else
        oi = -1;
      endif
      delta = c*(o(i) - oi)*x(i, :);
      w = w + delta';
    endfor
  endfor
  weight = w;
endfunction