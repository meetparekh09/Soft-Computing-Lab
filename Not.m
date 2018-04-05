function val = Not(x)
  weights = [-1];
  net = x * weights;
  val = net >= 0;
endfunction