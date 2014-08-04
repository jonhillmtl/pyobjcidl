import os
import sys
from optparse import OptionParser
from plyer import Plyer

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('pyobjcidl', 'templates'))

DEFAULT_PY_DEST_DIR = './py/'
DEFAULT_OBJC_DEST_DIR = './objc/'

def main():
	parser = OptionParser()
	parser.add_option("", "--source-file", dest="sourcefile", help="", metavar="SOURCEFILE")
	parser.add_option("", "--source-dir", dest="sourcedir", help="", metavar="SOURCEDIR")
	parser.add_option("", "--py-dest-dir", dest="pydestdir", help="", metavar="PYDESTDIR", default=DEFAULT_PY_DEST_DIR)
	parser.add_option("", "--objc-dest-dir", dest="objcdestdir", help="", metavar="OBJCDESTDIR", default = DEFAULT_OBJC_DEST_DIR)
	(options, args) = parser.parse_args()
	
	# TODO checkarguments
	if options.sourcefile is None and options.sourcedir is None:
		print "You must specify one of --source-file or --source-dir"
		exit()
		
	if options.sourcefile and options.sourcedir:
		print "You may only specify one of --source-file or --source-dir"
		exit()
			
	# TODO check directories exist
	if options.sourcefile:
		poidlgen(options.sourcefile, options.pydestdir, options.objcdestdir)
	
	if options.sourcedir:
		for root, dirs, files in os.walk(options.sourcedir):
			for f in files:
				if f.endswith('.poidl'):
					sourcefile = os.path.join(root, f)
					poidlgen(sourcefile, options.pydestdir, options.objcdestdir)
			
def output(template, plyer, dest):
	f = open(dest, 'w+')
	f.write(template.render(plyer=plyer).replace('\n\n\n', '\n\n').replace('\n\n', '\n'))
	f.close()
	
def output_py(plyer, base, objcdir):
	dest = "%s.h" % (os.path.join(objcdir, base))
	print("****** Generated %s" % dest)
	template = env.get_template('/objc/file.objctmp')
	output(template, plyer, dest)
	
def output_objc(plyer, base, objcdir):
	dest = "%s.py" % (os.path.join(objcdir, base))
	print("****** Generated %s" % dest)
	template = env.get_template('/py/file.pytmp')
	output(template, plyer, dest)
	
def poidlgen(sourcefile, pydestdir, objcdestdir):
	plyer = Plyer()
	plyer.clear()
	
	print("*** Generating for %s" % sourcefile)
	
	sf = open(sourcefile, 'r')
	plyer.feed(sf.read())
	sf.close()
	
	if plyer.errors > 0:
		print "errors in input file %s" % sourcefile
		quit()
		
	base = os.path.basename(sourcefile)
	base = os.path.splitext(base)[0]
	output_py(plyer, base, pydestdir)
	output_objc(plyer, base, objcdestdir)

if __name__ == "__main__":
	main()
