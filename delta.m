function weights = delta(x, o)
  c = 0.1;
  w = [rand(); rand(); rand()];
  for j = 1:100
    for i = 1:size(x, 1)
      oi = sigmoid(x(i, :)*w, 1, 1);
      grad = (1/2)*(1 - oi^2);
      del_w = c*(o(i) - oi)*grad*x(i, :);
      w = w + del_w';
    endfor
  endfor
  weights = w;
endfunction