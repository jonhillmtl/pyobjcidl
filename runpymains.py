import os
import sys
import imp
from optparse import OptionParser

def main():
	parser = OptionParser()
	parser.add_option("", "--source-dir", dest="sourcedir", help="", metavar="SOURCEDIR")
	(options, args) = parser.parse_args()

	if options.sourcedir:
		for root, dirs, files in os.walk(options.sourcedir):
			for f in files:
				if f.endswith('.py'):
					sourcefile = os.path.join(root, f)
					mod = imp.load_source(os.path.splitext(f)[0], sourcefile)
					mod.main()
					
if __name__ == "__main__":
	main()
