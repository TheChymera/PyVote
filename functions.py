def beta_binomial(n,k,a,b,mp=False):
	if mp:
		import mpmath
		p = mp_comb(n,k) * mpmath.beta(k+a, n-k+b) / mpmath.beta(a,b)
	else:
		from scipy.special import beta
		from scipy.misc import comb
		p = comb(n,k) * beta(k+a, n-k+b) / beta(a,b)
	return p

def mp_comb(N,k):
	"""
	The number of combinations of N things taken k at a time, with
	multiprecision floating-point output.
	This is often expressed as "N choose k".
	Parameters
	----------
	N : int, ndarray
		Number of things.
	k : int, ndarray
		Number of elements taken.
	Returns
	-------
	val : int,
		The total number of combinations, with floating-point
		multiprecision.
	Notes
	-----
	- Array arguments accepted only for exact=False case.
	- If k > N, N < 0, or k < 0, then a 0 is returned.
	Examples
	--------
	>>> n = 80000
	>>> k = 40000
	>>> mp_comb(n, k)
	7.0802212521852e+24079
	"""
	import mpmath
	vals = mpmath.factorial(N)/(mpmath.factorial(k)*mpmath.factorial(N-k))
	return vals