import argh
import numpy as np

def one_vote(population,
	threshold=0.5,
	ab=[],
	forecasts=[],
	normal=[],
	p=False,
	diagnostic=False,
	verbose=False,
	):

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
		from functions import mp_binom
		victory_pr = mp_binom(np.ceil(population*threshold),population,p)
		if (population*threshold).is_integer():
			# tie probability in case population*threshold is whole:
			tie_pr = mp_binom(population*(1-threshold)+1,population,p)
		elif not (population*threshold).is_integer() and threshold != 0.5:
			# tie probability in case population*threshold is not whole:
			tie_pr = mp_binom(population*(1-threshold),population,p)
		else:
			tie_pr = 0
	elif a and b:
		from functions import beta_binomial
		victory_pr = beta_binomial(np.ceil(population*threshold),population,a,b,multi_precission=True)
		if (population*threshold).is_integer():
			# tie probability in case population*threshold is whole:
			tie_pr = beta_binomial(population*(1-threshold)+1,population,a,b,multi_precission=True)
		elif not (population*threshold).is_integer() and threshold != 0.5:
			# tie probability in case population*threshold is not whole:
			tie_pr = beta_binomial(population*(1-threshold),population,a,b,multi_precission=True)
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

	change_pr = victory_pr+tie_pr
	return change_pr, victory_pr, tie_pr
