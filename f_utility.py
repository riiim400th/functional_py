def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def call(fn: function, key): 
    """example:
    id_slide = call(lambda x: x+10000, 'id')
    capitalize_name = call(lambda x: x.title(), 'username')
    username_modify_to_test = call(lambda x: '__test__.' + x, 'username')
    """
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))
    return apply_fn

def pipe_f(input_data: list,list_f: list): 
    from functools import reduce
    """example:
    pipe_f(datadict,  [f1,
                        f2, 
                        f3])
    """
    return reduce(lambda f_data, f: map(f,f_data), list_f, input_data)

