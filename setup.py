from setuptools import setup, find_packages

packages = find_packages()

setup(
	name="pyvote",
	version="9999",
	description = "Python script suite to model vote impact probabilities.",
	author = "Horea Christian",
	author_email = "chr@chymera.eu",
	url = "https://github.com/TheChymera/pyvote",
	keywords = ["voting", "probabilities", "political economy", "election"],
	classifiers = [],
	install_requires = [
		'argh',
		'mpmath',
		'numpy',
		],
	provides = ["pyvote"],
	packages = packages,
	include_package_data=True,
	extras_require = {
		},
	entry_points = {'console_scripts' : \
			['pyvote = pyvote.cli:main']
		},
	)
