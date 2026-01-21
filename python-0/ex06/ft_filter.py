print(filter.__doc__)


def ft_filter(fun, iter):
    """Return an iterator yielding those items of \
iterable for which function(item) is true. If function \
is None, return the items that are true."""
    print("to check:", iter)
    res = []
    for i in iter:
        print("checking ", i)
        if fun is None and i:
            res.append(i)
        elif fun is not None and fun(i) is True:
            res.append(i)
    return res


print(ft_filter.__doc__)
