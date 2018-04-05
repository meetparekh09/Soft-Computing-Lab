function ff_analysis(w1, w2, range, lambda, act1, act2)
  comb_arr = []
  for i=1:size(w1, 2)-1
    comb_arr = [comb_arr range(1):0.1:range(2)];
  endfor
  x = unique(nchoosek(comb_arr, size(w1, 2)-1), 'rows');
  x = [x -1*ones(size(x, 1), 1)];
  net1 = (w1*x')';
  if(act1 == 0)
    o1 = signum(net1, 0);
  elseif(act1 == 1)
    o1 = signum(net1, 1);
  elseif(act1 == 2)
    o1 = sigmoid(net1, lambda, 0);
  else
    o1 = sigmoid(net1, lambda, 1);
  endif
  x2 = [o1 -1*ones(size(o1, 1), 1)];
  net2 = (w2*x2')';
  if(act2 == 0)
    o2 = signum(net2, 0);
  elseif(act2 == 1)
    o2 = signum(net2, 1);
  elseif(act2 == 2)
    o2 = sigmoid(net2, lambda, 0);
  else
    o2 = sigmoid(net2, lambda, 1);
  endif
  plot3(x(:, 1), x(:, 2), o2);
endfunction