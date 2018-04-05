function val = And(X)
  weights = [1; 1];
  net = X * weights;
  val = net >= 2;
endfunction