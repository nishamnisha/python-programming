def _make_gen(reader):
    a = reader(1024 * 1024)
    while a:
        yield a
        a = reader(1024*1024)

def rawpycount(filename):
    f = open(filename, 'rb')
    f_gen = _make_gen(f.raw.read)
    return sum( buf.count(a'\n') for buf in f_gen )
