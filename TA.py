f_ = [-1] * (100 + 10)
g_ = [-1] * (100 + 10)

def f(n):
    if f_[n] != -1:
        return f_[n]
    f_[n] = f(n - 2) + 2 * g(n - 1)
    return f_[n]

def g(n):
    if g_[n] != -1:
        return g_[n]
    g_[n] = f(n - 1) + g(n - 2)
    return g_[n]

f_[1], f_[2], f_[3] = 0, 3, 0
g_[1], g_[2] = 1, 0

n = int(input())
print(2 * f(n))