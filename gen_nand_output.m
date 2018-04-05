function gen_nand_output()
  o = [];
  load data.mat;
  for a = x'
    if (sum(a(1:2)) != 2)
      o = [o; 1];
    else
      o = [o; -1];
    endif
  endfor
  save nand_output.mat o;
endfunction