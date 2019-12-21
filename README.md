# PyVote

This package provides a Python module and a Bash interface which can compute the probability of a 2-choice popular election being decided by one vote.
Predictions are based on either a series of forecasts, a beta (or normal) probability density function for outcomes, or a fixed outcome probability.

## Examples

Input:
```
pyvote one 2000000 -f 0.519 0.55 0.492 0.53 0.515
```

Output:
```
The probability of a single vote deciding an election with 2000000 voters and forecasts of 0.519, 0.55, 0.492, 0.53, and 0.515 in favor of the preferred choice is 1.12534199273483e-5.
As the population is even, this probability is the sum of the probabilities of turning a tie into a victory (5.62662750202373e-6) and turning a loss into a tie (5.62679242532457e-6).
```

## Installation

Depending on your preferred package manager you may choose one of the following methods:

#### Portage (e.g. on Gentoo Linux):
PyVote is available via Portage (the package manager of Gentoo Linux, derivative distributions, and installable on [any other Linux distribution](https://wiki.gentoo.org/wiki/Project:Prefix), or BSD) via the [Chymeric Overlay](https://github.com/TheChymera/overlay).
Upon enabling the overlay, the package can be emerged:

````
emerge pyvote
````

Alternatively, the live (i.e. latest) version of the package can be installed along with all of its dependencies without the need to enable to overlay:

```
git clone git@github.com:TheChymera/pyvote.git
cd pyvote/.gentoo
./install.sh
```

#### Python Package Manager (Users):
Python's `setuptools` allows you to install Python packages independently of your distribution (or operating system, even).
This approach is (by design) not particularly powerful in managing dependencies;
as such, given any other alternative, **we do not recommend this approach**:

````
git clone git@github.com:TheChymera/pyvote.git
cd pyvote
python setup.py install --user
````

#### Python Package Manager (Developers):
Python's `setuptools` allows you to install Python packages independently of your distribution (or operating system, even);
it also allows you to install a "live" version of the package - dynamically linking back to the source code.
This permits you to test code (with real module functionality) as you develop it.
This method is sub-par for dependency management (see above notice), but - as a developer - you should be able to manually ensure that your package manager provides the needed packages.

````
git clone git@github.com:TheChymera/pyvote.git
cd pyvote
echo "export PATH=\$HOME/.local/bin/:\$PATH" >> ~/.bashrc
source ~/.bashrc
python setup.py develop --user
````

#### Troubleshooting Manual Installation
If you are getting a `Permission denied (publickey)` error upon trying to clone, you can either:

* [Add an SSH key](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) to your GitHub account.
* Pull via the HTTPS link `git clone https://github.com/IBT-FMI/SAMRI.git`.


### Dependencies:

The most precise specification of the dependency graph can be extracted from the [pyvote ebuild](.gentoo/dev-python/pyvote/pyvote-99999.ebuild).
For manual dependency management and overview you may use the following list:

* [argh](https://github.com/neithere/argh)
* [mpmath](http://mpmath.org/)
* [NumPy](http://www.numpy.org)
