#Task 1
def sequential_map(*args):
    *function, conteins = args
    finall_res = []
    for i in conteins:
        for j in function:
            res = j(i)
        finall_res.append(res)
    return print(finall_res)


#Task 2
def consensus_filter(*args):
    *function, conteins = args
    for f in function:
        conteins = list(filter(f, conteins))
    return conteins


#Task 3
def conditional_reduce(fun_1, fun_2, conteins):
    fiterted_cont = list(filter(fun_1, conteins))
    res = fiterted_cont[0]
    for i in range(1, len(fiterted_cont)):
        res = fun_2(res, fiterted_cont[i])
    return(res)


#Task 4
def func_chain(*args):
    def fun_inside(x):
        for function in args:
            x = function(x)
        return x

    return lambda x: fun_inside(x)



# Task5 bonus

def multiple_partial(*args, **keywords):
    res = list()
    def partial(func, **keywords):
        def newfunc(*fargs, **fkeywords):
            newkeywords = {**keywords, **fkeywords}
            return func(*fargs, **newkeywords)
        return newfunc

    for fun in args:
        new_fun = partial(fun, **keywords)
        res.append(new_fun)
    return res
