import numpy as np

def monte_carlo_integration(func, x1, x2, n= 10000000):
    subsets = np.arange(0,n+1,n/10)
    u = np.zeros(n)
    for i in range(10):
        st = int(subsets[i])
        end = int(subsets[i+1])
        u[st:end] = np.random.uniform(low=i/10,high=(i+1)/10,size=end-st)
    np.random.shuffle(u)
    u_func = func(x1+(x2-x1)*u)

    return ((x2-x1)/n)* u_func.sum()
    