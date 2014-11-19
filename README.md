#PyVote

Python script with command line functionality that displays the probability of a 2-candidate popular election being decided by one vote.
Predictions are based on either a series of forecasts, a beta (or normal) probability density function for outcomes, or a fixed outcome probability.

##Installation

####On [Gentoo Linux](http://en.wikipedia.org/wiki/Gentoo_linux) and [Derivatives](http://en.wikipedia.org/wiki/Category:Gentoo_Linux_derivatives):

PyVote is available in the [Portage](http://en.wikipedia.org/wiki/Portage_(software)) *[chymerc overlay](https://github.com/TheChymera/chymeric)* as **[app-misc/pyvote](https://github.com/TheChymera/chymeric/tree/master/app-misc/RTbatch)**.
Just run the following command:

```
emerge pyvote
```

*If you are not yet using this overlay, it can be enabled with just two commands, as seen in [the README](https://github.com/TheChymera/chymeric).*

###Dependencies:

####Mandatory:
* [**numpy**](http://en.wikipedia.org/wiki/NumPy) - in Portage as **dev-python/numpy**
* [**mpmath**](http://mpmath.org/) - in Portage as **dev-python/mpmath**

##Usage
Run the script either as `1vote_cli` (if installed globally), or as `./1vote_cli.py` from the containing folder:
```
1vote_cli.py [-h] [-t THRESHOLD] [-b BETA BETA]
			[-f FORECASTS [FORECASTS ...]] [-n NORMAL NORMAL]
			[-p PROBABILITY] [-d] [-v]
			population
```

Example:
```
RTbatch_cli 10000000 -f 0.519 0.55 0.492 0.53 0.515
```

##Arguments

```
positional arguments:
  population            The projected population turnout.

optional arguments:
  -h, --help            show this help message and exit
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold needed for reference candidate to win
  -b BETA BETA, --beta BETA BETA
                        Beta distribution parameters: alpha and beta.
  -f FORECASTS [FORECASTS ...], --forecasts FORECASTS [FORECASTS ...]
                        List with polling forecasts.
  -n NORMAL NORMAL, --normal NORMAL NORMAL
                        Normal distribution fitted to forecast data: mean and
                        standard deviation
  -p PROBABILITY, --probability PROBABILITY
                        Fixed forecast (not recommended)
  -d, --diagnostic      Display beta function plot for diagnostic purposes
  -v, --verbose         Make output verbose
```

---
Released under the GPLv3 license.
Project led by Horea Christian (address all correspondence to: h.chr@mail.ru)
