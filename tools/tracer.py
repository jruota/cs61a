def tracer(f):
    def inner_tracer(*args):
        print("TRACER Calling", f, "with", args)
        res = f(*args)
        print("TRACER Returning from", args, "->", res)
        return res
    return inner_tracer
