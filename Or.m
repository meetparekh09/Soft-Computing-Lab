function val = Or(X)
  weights = [1; 1];
  net = X * weights;
  val = net >= 1;
endfunction