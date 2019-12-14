__author__ = "Horea Christian"

import argh
from votes import one_vote

@argh.arg('-f', '--forecasts', nargs='+', type=float)
def one(population,
	threshold=0.5,
	ab=[],
	forecasts=[],
	normal=[],
	p=False,
	diagnostic=False,
	values_only=False,
	):

	population = int(population)

	change, victory, tie = one_vote(population,
		threshold=threshold,
		ab=ab,
		forecasts=forecasts,
		normal=normal,
		p=p,
		diagnostic=diagnostic,
		verbose=not values_only,
		)
	if values_only:
		print(' '.join([change, victory, tie]))
	else:
		if forecasts:
			forecasts = [str(i) for i in forecasts]
			if len(forecasts)>2:
				forecast_str = ', '.join(forecasts[:-1]) + ', and ' + str(forecasts[-1])
			elif len(forecasts)==2:
				forecast_str = ' and '.join(forecasts)
			elif len(forecasts)==1:
				forecast_str = str(forecast_str[0])
			forecast_str = 'forecasts of {} for the reference candidate'.format(forecast_str)
		elif beta:
			forecast_str = 'a forecast beta distribution for the reference candidate of parameters a={}, and b={}'.format(*ab)
		elif normal:
			forecast_str = "a normal forecast probability density function for the reference candidate with a mean of {} and a standard deviation of {}".format(*normal)
		elif p:
			forecast_str = "a fixed outcome probability for the reference candidate of {}".format(probability)
		print('The probability of a single vote deciding an election with {} voters and {} is {}.'.format(population, forecast_str, change))
		if population & 1 == 0:
			print('As the population is even, this probability is the sum of the probability of turning a tie into a victory ({}) or turning a loss into a tie ({}).'.format(victory, tie))


def main():
	argh.dispatch_commands([one])

if __name__ == '__main__':
	main()
