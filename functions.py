def mp_beta_binomial(k,n,a,b):
	from scipy.special import beta
	from scipy.misc import comb
	import mpmath
	p = comb(n,k) * mpmath.beta(k+a, n-k+b) / mpmath.beta(a,b)
	return p

def mp_comb(n,k):
	from numpy import asarray
	k,N = asarray(k), asarray(N)
	cond = (k <= N) & (N >= 0) & (k >= 0)
	vals = binom(N, k)
	if isinstance(vals, np.ndarray):
	    vals[~cond] = 0
	elif not cond:
	    vals = np.float64(0)
	return vals
