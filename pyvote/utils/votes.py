import argh
import numpy as np

@argh.arg('-f', '--forecasts', nargs='+', type=float)
@argh.arg('-c', '--compact', default=False, action='store_true')
def one(population,
	threshold=0.5,
	ab=[],
	forecasts=[],
	normal=[],
	p=False,
	diagnostic=False,
	compact=True,
	):
	"""Estimate the probability of one vote changing the outcome in a 2-choice election.

	Parameters
	----------

	population : int
		Number of projected voters (taken as exact predictor).
	threshold : float, optional
		Threshold needed for preferred choice to win.
	ab : list, optional
		A list of two floats giving the alpha and beta parameters of a beta probability distribution estimating the votes of the population.
		If this parameter is defined, `forecasts`, `normal`, and `p` must not be defined.
	forecasts : list, optional
		A list of floats giving forecasts for the outcome.
		If this parameter is defined, `ab`, `normal`, and `p` must not be defined.
	normal : list, optional
		A list of two floats giving the mean and standard deviation of a normal probability distribution estimating the votes of the population.
		If this parameter is defined, `ab`, `forecasts`, and `p`  must not be defined.
	p : float, optional
		A float between 0 and 1 giving a fixed probability for the election outcome.
		Usage of this parameter is not recommended as it will model the probability as a binomial distribution with a sharp peak.
		If this parameter is defined, `ab`, `forecasts`, and `p`  must not be defined.
	diagnostic : bool, optional
		Attempt to plot a diagnostic graphic of the outcome probabilities.
	compact : bool, optional
		Return the values as a list.
		If this is set to false, a report is printed in full English sentences instead of returning values.
	"""


	if sum(map(bool,[ab, forecasts, normal, p])) != 1:
		raise ValueError("Please specify one and only one of the 'ab', 'forecasts', 'normal', or 'p' options.")

	population = int(population)

	if ab:
		a, b = ab
	elif forecasts:
		from scipy.stats import beta
		a, b, _, _ = beta.fit(forecasts, floc=0, fscale=1)
	elif normal:
		from pyvote.utils.functions import fit_beta_to_normal
		m, s = normal
		a, b = fit_beta_to_normal(m,s)
	else:
		pass

	if p:
		from pyvote.utils.functions import mp_binom
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
		from pyvote.utils.functions import beta_binomial
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
		plt.xlabel('Preferred Choice Vote Share')
		plt.ylabel('PDF')
		plt.show()

	change_pr = victory_pr+tie_pr

	if compact:
		return change_pr, victory_pr, tie_pr
	else:
		if forecasts:
			forecasts = [str(i) for i in forecasts]
			if len(forecasts)>2:
				forecast_str = ', '.join(forecasts[:-1]) + ', and ' + str(forecasts[-1])
			elif len(forecasts)==2:
				forecast_str = ' and '.join(forecasts)
			elif len(forecasts)==1:
				forecast_str = str(forecast_str[0])
			forecast_str = 'forecasts of {} for the preferred choice'.format(forecast_str)
		elif beta:
			forecast_str = 'a forecast beta distribution for the preferred choice with parameters a={}, and b={}'.format(*ab)
		elif normal:
			forecast_str = "a normal forecast probability density function for the preferred choice with a mean of {} and a standard deviation of {}".format(*normal)
		elif p:
			forecast_str = "a fixed outcome probability for the preferred choice of {}".format(probability)
		print('The probability of a single vote deciding an election with {} voters and {} is {}.'.format(population, forecast_str, change_pr))
		if population & 1 == 0:
			print('As the population is even, this probability is the sum of the probabilities of turning a tie into a victory ({}) and turning a loss into a tie ({}).'.format(victory_pr, tie_pr))
