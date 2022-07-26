def test_func(func, in_path="./in.txt", out_path="./out.txt"):
    print("func name:", func.__name__)
    params = func.__annotations__
    if "return" in params.keys():
        params.pop("return")
    with open(in_path) as f:
        input_params = f.readlines()
    out_file = open(out_path, "w")
    for i in range(0, len(input_params), len(params)):
        p = input_params[i:i+len(params)]
        p=[eval(i) for i in p]
        res = func(*p)
        print("input:{} output:{}".format(p,res))
        out_file.write(str(res)+"\n")
    out_file.close()
