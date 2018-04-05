function perceptron_learning_exp()
  generate_data();
  gen_and_output();
  gen_or_output();
  gen_nand_output();
  gen_nor_output();
  load data.mat;
  load and_output.mat;
  w = perceptron(x, o);
  disp("Performing perceptron learning for and logic");
  disp("Weight values are :");
  disp(w);
  disp("error is :");
  disp(check_error(x, w, o));
  load or_output.mat;
  w = perceptron(x, o);
  disp("Performing perceptron learning for or logic")
  disp("Weight values are :"), disp(w)
  disp("error is :"), disp(check_error(x, w, o))
  load nand_output.mat;
  w = perceptron(x, o);
  disp("Performing perceptron learning for nand logic")
  disp("Weight values are :"), disp(w)
  disp("error is :"), disp(check_error(x, w, o))
  load nor_output.mat;
  w = perceptron(x, o);
  disp("Performing perceptron learning for and logic")
  disp("Weight values are :"), disp(w)
  disp("error is :"), disp(check_error(x, w, o))
endfunction