function err = check_error_delta(x, w, o)
  err = sum(sigmoid(x*w) - o)
endfunction