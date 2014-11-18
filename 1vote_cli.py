#!/usr/bin/python
__author__ = 'Horea Christian'
import argparse
import votes

parser = argparse.ArgumentParser()
parser.add_argument("population", help="The projected population turnout.", type=int)
parser.add_argument("-t", "--threshold", help="Threshold needed for reference candidate to win", default=0.5, type=float)
parser.add_argument("-b", "--beta", help="Beta distribution parameters: alpha and beta.", nargs=2, type=float)
parser.add_argument("-f", "--forecasts", help="List with polling forecasts.", nargs='+', type=float)
parser.add_argument("-n", "--normal", help="Normal distribution fitted to forecast data: mean and standard deviation", nargs=2, type=float)
parser.add_argument("-p", "--probability", help="Fixed forecast (not recommended)", type=float)
parser.add_argument("-d", "--diagnostic", help="Display beta function plot for diagnostic purposes", action="store_true")
args = parser.parse_args()

if sum(map(bool,[args.beta, args.forecasts, args.normal, args.probability])) != 1:
	print "Please specify one, and only one of the '--beta'/'-b', '--forecasts'/'-f', '--normal'/'-n', and '--probability'/'-p' options."

pr = votes.one_vote(args.population, args.threshold, ab=args.beta, forecasts=args.forecasts, normal=args.normal, p=args.probability, diagnostic=args.diagnostic)
