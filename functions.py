def beta_binomial(k,n,a,b):
	import scipy.special.beta as B
	import
	p = choose(n,k) * B(k+a, n-k+b) / B(a,b)
	return p
