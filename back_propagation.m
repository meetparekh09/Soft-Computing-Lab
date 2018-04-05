function [v, w] = back_propagation(x, o)
  v = [rand() rand() rand(); rand() rand() rand()];
  w = [rand() rand() rand()];
  for in = x'
    y = sigmoid(v*in, 1, 1);
    y = [y; -1];
    z = sigmoid(w*y, 1, 1);
    del_w = ((o - z).*(1 .- o.^2).*y)./2
    