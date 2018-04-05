function out = sigmoid(net, lambda, bipolar)
  if(bipolar)
    out = 2./(1+exp(-lambda*net)) - 1;
  else
    out = 1./(1+exp(-lambda*net));
  endif
endfunction