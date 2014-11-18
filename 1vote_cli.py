#!/usr/bin/python
__author__ = 'Horea Christian'
import argparse
import votes

parser = argparse.ArgumentParser()
parser.add_argument("population", help="The projected population turnout.", type=int)
parser.add_argument("-t", "--threshold", help="Threshold needed for reference candidate to win", type=float)
parser.add_argument("-b", "--beta", help="Beta distribution parameters: alpha and beta.", nargs=2, type=float)
parser.add_argument("-f", "--forecasts", help="List with polling forecasts.", nargs='+', type=float)
parser.add_argument("-n", "--normal", help="Normal distribution fitted to forecast data: mean and standard deviation", nargs=2, type=float)
parser.add_argument("-p", "--probability", help="Fixed forecast (not recommended)", type=float)
parser.add_argument("-d", "--diagnostics", help="Display beta function plot for diagnostic purposes", action="store_true")
args = parser.parse_args()

if [args.beta, args.forecasts, args.normal, args.probability].count(True) != 1:
	print "Please specify one, and only one of the '--beta'/'-b', '--forecasts'/'-f', '--normal'/'-n', and '--probability'/'-p' options."

print args.population
print args.threshold
print args.beta
print args.forecasts
print args.normal
print args.probability
print args.diagnostics

votes.one_vote(args.population, args.threshold, ab=args.beta, forecasts=args.forecasts, ms=args.do_fullsize, template_name=args.template, mini_width=args.mini_width)
