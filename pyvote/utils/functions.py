def beta_binomial(k,n,a,b,multi_precission=False):
	"""
	Beta binomial function, returning the probability of k successes in n trials (given a p distribution beta of parameters a and b), and supporting multiprecission output.

	Parameters
	----------
	k : int, ndarray
		Successes.
	n : int, ndarray
		Trials.
	a, b : int,ndarray
		Parameters of the beta distribution.
	multi_precission : bool, optional
		Whether or not to use multiprecision floating-point output (default: False).

	Returns
	-------
	p : int,ndarray
		Probability of k successes in n trials.

	Examples
	--------
	>>> n = 80000
	>>> k = 40000
	>>> mp_comb(n, k)
	7.0802212521852e+24079
	"""
	if multi_precission:
		import mpmath as mp
		p = mp_comb(n,k) * mp.beta(k+a, n-k+b) / mp.beta(a,b)
	else:
		from scipy.special import beta
		from scipy.misc import comb
		p = comb(n,k) * beta(k+a, n-k+b) / beta(a,b)
	return p

def mp_comb(N,k):
	"""
	The number of combinations of N things taken k at a time, with multiprecision floating-point output.
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
		The total number of combinations, with floating-point multiprecision.

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
	import mpmath as mp
	val = mp.factorial(N)/(mp.factorial(k)*mp.factorial(N-k))
	return val

def mp_binom(k,n,p):
	"""
	Binomial function, returning the probability of k successes in n trials given the trial success probability p, and supporting multiprecission output.

	Parameters
	----------
	k : int, ndarray
		Successes.
	n : int, ndarray
		Trials.
	p : float,ndarray
		Trial (experiment) success probability.

	Returns
	-------
	val : float,ndarray
		Probability of k successes in n trials.

	Examples
	--------
	>>> k = 10
	>>> n = 10000
	>>> p = 0.9
	>>> mp_binom(k, n, p)
	9.56548769092821e-9958
	"""
	import mpmath as mp
	val = mp_comb(n,k) * mp.power(p,k) * mp.power(1-p,n-k)
	return val

def fit_beta_to_normal(m,s):
	"""
	Calculate the a, b parameters of a beta function using the mean and variance (formula according to http://stats.stackexchange.com/a/12239/32504).

	Parameters
	----------
	m : float, ndarray
		Distribution mean.
	s : float, ndarray
		Distribution standard deviation.

	Returns
	-------
	a,b : float, tuple
		A and b parameters for the equivalent beta distribution.

	Examples
	--------
	>>> m = 0.4
	>>> s = 0.2
	>>> fit_beta_to_normal(m, s)
	(1.9999999999999998, 2.9999999999999996)
	"""
	a = ((1-m) / s**2 - 1 / m) * m**2
	b = a*(1/m - 1)
	return a,b
