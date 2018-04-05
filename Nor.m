function val = Nor(X)
  weights = [-1; -1];
  net = (X * weights);
  val = net >= 0;