from __future__ import division
__author__ = 'Horea Christian'

def one_vote(N, threshold=0.5, ab=False, forecasts=False, ms=False, p=False, diagnostic=False):
	import numpy as np
	a = False
	pr = False
	if not (ab or forecasts or ms or p):
		raise ValueError("You need to specify either 'ab', 'forecasts', 'ms', or 'p'.")
	if ab:
		a, b = ab
	elif forecasts:
		from scipy.stats import beta
		if a:
			raise ValueError("Please specify only one of the 'ab', 'forecasts', 'ms', and 'p' arguments.")
		a, b, _, _ = beta.fit(forecasts, floc=0, fscale=1)
	elif ms:
		if a:
			raise ValueError("Please specify only one of the 'ab', 'forecasts', 'ms', and 'p' arguments.")
		from functions import fit_beta_to_ms
		m, s = ms
		a, b = fit_beta_to_ms(m,s)
	elif p:
		if a:
			raise ValueError("Please specify only one of the 'ab', 'forecasts', 'ms', and 'p' arguments.")
		from scipy.stats import binom
		pr = binom.pmf(np.ceil(N*threshold),N,p)
		if (N*threshold).is_integer():
			pr += binom.pmf(N*threshold+1,N,p)
	if not pr:
		from functions import beta_binomial
		pr = beta_binomial(np.ceil(N*threshold),N,a,b,mp=True)
		if (N*threshold).is_integer():
			pr += beta_binomial(N*threshold+1,N,a,b,mp=True)

	if diagnostic:
		import matplotlib.pyplot as plt
		x = np.linspace(0,1,1000)
		try:
			plt.style.use('http://chymera.eu/matplotlib/styles/chymeric.mplstyle')
		except ValueError:
			plt.style.use('ggplot')
		plt.axvline(x=threshold, color="#fbb4b9", linewidth=1)
		plt.legend(['percentage\n threshold'], loc='upper right')
		plt.plot(x, beta.pdf(x,a,b))
		plt.xlabel('Reference Candidate Vote Share')
		plt.ylabel('PDF')
		plt.show()

	return pr
