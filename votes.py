from __future__ import division
__author__ = 'Horea Christian'

def one_vote(N, threshold=0.5, ab=False, forecasts=False, normal=False, p=False, diagnostic=False):
	import numpy as np
	if sum(map(bool,[ab, forecasts, normal, p])) != 1:
		raise ValueError("Please specify one and only one of the 'ab', 'forecasts', 'normal', or 'p' options.")

	if ab:
		a, b = ab
	elif forecasts:
		from scipy.stats import beta
		a, b, _, _ = beta.fit(forecasts, floc=0, fscale=1)
	elif normal:
		from functions import fit_beta_to_normal
		m, s = normal
		a, b = fit_beta_to_normal(m,s)
	else:
		pass

	if p:
		from scipy.stats import binom
		victory_pr = binom.pmf(np.ceil(N*threshold),N,p)
		if (N*threshold).is_integer():
			# tie probability in case N*threshold is whole:
			tie_pr = binom.pmf(N*(1-threshold)+1,N,p)
		elif not (N*threshold).is_integer() and threshold != 0.5:
			# tie probability in case N*threshold is not whole:
			tie_pr = binom.pmf(N*(1-threshold),N,p)
		else:
			tie_pr = 0
	elif a and b:
		from functions import beta_binomial
		victory_pr = beta_binomial(np.ceil(N*threshold),N,a,b,mp=True)
		if (N*threshold).is_integer():
			# tie probability in case N*threshold is whole:
			tie_pr = beta_binomial(N*(1-threshold)+1,N,a,b,mp=True)
		elif not (N*threshold).is_integer() and threshold != 0.5:
			# tie probability in case N*threshold is not whole:
			tie_pr = beta_binomial(N*(1-threshold),N,a,b,mp=True)
		else:
			tie_pr = 0
	else:
		pass

	if diagnostic:
		import matplotlib.pyplot as plt
		x = np.linspace(0,1,1000)
		try:
			plt.style.use('http://chymera.eu/matplotlib/styles/chymeric-gnome.mplstyle')
		except ValueError:
			plt.style.use('ggplot')
		plt.axvline(x=threshold, color="#fbb4b9", linewidth=1)
		plt.legend(['percentage\n threshold'], loc='upper right')
		plt.plot(x, beta.pdf(x,a,b))
		plt.xlabel('Reference Candidate Vote Share')
		plt.ylabel('PDF')
		plt.show()

	total_pr = victory_pr+tie_pr
	return total_pr, victory_pr, tie_pr
