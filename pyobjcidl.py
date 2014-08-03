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
	    print "Cycle through"
	    pass
	
def output_py(plyer, sourcefile, pydir):
    base = os.path.basename(sourcefile)
    base = os.path.splitext(base)[0]
    
    pydest = "%s.py" % (os.path.join(pydir, base))
    template = env.get_template('/py/file.pytmp')
    pyfile = open(pydest, 'w+')
    pyfile.write(template.render(plyer=plyer))
    pyfile.close()
    
def output_objc(plyer, sourcefile, objcdir):
    pass
    
def poidlgen(sourcefile, pydestdir, objcdestdir):
    plyer = Plyer()
    sf = open(sourcefile, 'r')
    plyer.feed(sf.read())
    output_py(plyer, sourcefile, pydestdir)
    output_objc(plyer, sourcefile, objcdestdir)

if __name__ == "__main__":
	main()
