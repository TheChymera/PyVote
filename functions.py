def beta_binomial(k,n,a,b,mp=False):
	if mp:
		import mpmath
		p = mp_comb(n,k) * mpmath.beta(k+a, n-k+b) / mpmath.beta(a,b)
	else:
		from scipy.special import beta
		from scipy.misc import comb
		p = comb(n,k) * beta(k+a, n-k+b) / beta(a,b)
	return p

def mp_comb(N,k):
	import mpmath
	vals = mpmath.factorial(N)/(mpmath.factorial(k)*mpmath.factorial(N-k))
	return vals
