import time


def test_func(func, in_path="./in.txt", out_path="./out.txt"):
    print("func name:", func.__name__)
    params = func.__annotations__
    if "return" in params.keys():
        params.pop("return")
    with open(in_path) as f:
        input_params = f.readlines()
    out_file = open(out_path, "w")
    for i in range(0, len(input_params), len(params)):
        p = input_params[i:i + len(params)]
        p = [eval(i) for i in p]
        res = func(*p)
        print("input:{} output:{}".format(p, res))
        out_file.write(str(res) + "\n")
    out_file.close()


def test_func_batch(func, in_content=""):
    print("func name:", func.__name__)
    params = func.__annotations__
    if "return" in params.keys():
        params.pop("return")
    input_params = in_content.strip().split("\n")
    for i in range(0, len(input_params), len(params)):
        p = input_params[i:i + len(params)]
        p = [eval(i.strip()) for i in p]
        try:
            begin_time = time.time()
            res = func(*p)
            print("input :{} \noutput:{}\nspend :{} ms".format(p, res, (time.time() - begin_time)*1000))
        except Exception as e:
            print("PANIC!!", e)
            print("input :{}".format(p))
        print("-" * 30)
    print("end")
