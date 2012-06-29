def euclid(n,m):
    """
    an implementation of the euclidean algorithm
    for the computation of gcd(n,m)
    """
    if n < m:
        n, m = m, n
    while n % m != 0:
        n, m = m, n % m
    return m

def extended_euclid(n,m):
    """
    computes a and b such that
    a*n + b*m = 1
    PRECONDITION: gcd(n,m) = 1
    (code taken from wikipedia)
    """
    a, l_a = 1, 0
    b, l_b = 0, 1
    if n < m:
        n, m = m, n
    while n % m != 0:
        q      = n / m
        n, m   = m, n % m
        a, l_a = l_a - q * a, a
        b, l_b = l_b - q * b, b
    return a, b

def mult_invert(a, b):
    """
    computes the multiplicative inverse of a in Z_B^*
    PRECONDITION: gcd(a,b) = 1
    """
    return extended_euclid(a,b)[0] % b
