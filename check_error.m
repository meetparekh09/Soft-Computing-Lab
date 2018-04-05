function err = check_error(x, w, o)
  net = (x*w>=0);
  out = o>=0;
  err = sum(net - out);