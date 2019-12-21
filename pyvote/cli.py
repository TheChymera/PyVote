__author__ = "Horea Christian"

import argh
from pyvote.utils.votes import one

def main():
	argh.dispatch_commands([one])

if __name__ == '__main__':
	main()
