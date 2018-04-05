function gen_or_output()
  o = [];
  load data.mat;
  for a = x'
    if (sum(a(1:2)) >= 0)
      o = [o; 1];
    else
      o = [o; -1];
    endif
  endfor
  save or_output.mat o;
endfunction