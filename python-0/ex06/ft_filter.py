def ft_filter(fun, iter):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of \
iterable for which function(item)
is true. If function is None, return the items that are true."""
    res = []
    for i in iter:
        if fun is None and i:
            res.append(i)
        elif fun is not None and fun(i) is True:
            res.append(i)
    return res


print(ft_filter.__doc__)
