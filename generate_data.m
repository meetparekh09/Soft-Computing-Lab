function generate_data()
  x = [];
  v = [-1; 1];
  p = [1/2; 1/2];
  for i = 1:500
    x = [x; discrete_rnd(v, p) discrete_rnd(v, p)];
  endfor
  x = [x -1.*ones(size(x, 1), 1)];
  save data.mat x;
endfunction