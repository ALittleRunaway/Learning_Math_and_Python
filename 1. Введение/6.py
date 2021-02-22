from scipy import constants as const

def lam(U):
    return ((const.c * const.h) / (const.e * U))
print(lam(10))