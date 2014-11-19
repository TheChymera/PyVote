#!/usr/bin/python
__author__ = 'Horea Christian'
import argparse
import votes

parser = argparse.ArgumentParser()
parser.add_argument("population", help="The projected population turnout.", type=int)
parser.add_argument("-t", "--threshold", help="Threshold needed for reference candidate to win", default=0.5, type=float)
parser.add_argument("-b", "--beta", help="Beta distribution parameters: alpha and beta.", nargs=2, type=float)
parser.add_argument("-f", "--forecasts", help="Polling forecast (repeat flag for multiple forecasts).", type=float, action="append")
parser.add_argument("-n", "--normal", help="Normal distribution fitted to forecast data: mean and standard deviation", nargs=2, type=float)
parser.add_argument("-p", "--probability", help="Fixed forecast (not recommended)", type=float)
parser.add_argument("-d", "--diagnostic", help="Display beta function plot for diagnostic purposes", action="store_true")
parser.add_argument("-v", "--verbose", help="Make output verbose", action="store_true")
args = parser.parse_args()

if sum(map(bool,[args.beta, args.forecasts, args.normal, args.probability])) != 1:
	print "Please specify one, and only one of the '--beta'/'-b', '--forecasts'/'-f', '--normal'/'-n', and '--probability'/'-p' options."

pr,_,_ = votes.one_vote(args.population, args.threshold, ab=args.beta, forecasts=args.forecasts, normal=args.normal, p=args.probability, diagnostic=args.diagnostic)
if args.forecasts:
	forecast_str = "forecasts of"
	for ix, i in enumerate(args.forecasts):
		if ix == len(args.forecasts)-1:
			forecast_str += " and " + str(i)
		else:
			forecast_str += " " + str(i) +","
	forecast_str += " for the reference candidate"
elif args.beta:
	forecast_str = "a forecast beta distribution for the reference candidate of parameters a="+str(args.beta[0])+", and b="+str(args.beta[1])
elif args.normal:
	forecast_str = "a forecast probability density function for the reference candidate with a mean of "+str(args.beta[0])+" and a standard deviation of "+str(args.beta[1])
elif args.probability:
	forecast_str = "a fixed outcome probability for the reference candidate of "+str(args.probability)
if args.verbose:
	print("The probability of a single vote deciding an election with "+str(args.population)+" voters and "+forecast_str+" is "+str(pr))
else:
	print(str(pr))
