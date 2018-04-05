function out = signum(net, bipolar)
  if(bipolar)
    out = (net>=0) - (net<0);
  else
    out = net>=0;
  endif
endfunction