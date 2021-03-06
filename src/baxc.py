#!/usr/bin/env python2.7
#-*-python-2.7-
####################################################################################
#			BAXC--BAckground Xml Creater
#-----------------------------------------------------------------------------------
# 
# Generates xml code for background slide show of gnome.
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#Or see <http://www.gnu.org/licenses/>.
#
#Authors: Abil N George
####################################################################################
import argparse
import os
import string

#parse processing
def directory(string):
	if os.path.isdir(string):
		return string
	else:
	        raise argparse.ArgumentTypeError("%r is not a directory" %string)
def xmlfile(string):
	if string[-4:]=='.xml':
		return string
	else:
	        raise argparse.ArgumentTypeError("%r is not a xmlfile" %string)


parser = argparse.ArgumentParser(description='BAckground Xml Creater-Create background slide show file for gnome',prog='baxc')
parser.add_argument('-c','--cmd',help='For CmdLine Interface',dest='Cmd',action='store_true',default=False)
parser.add_argument('-t','--time',dest='time',type=int,default=30,help='time duration(default: 30) in min',metavar='Time in min')
parser.add_argument('-i','--interactive',help='for interactive session',dest='action',action='store_true',default=False)
parser.add_argument('-o','--output',dest='path',type=xmlfile,default='background.xml',help='Output file(default value=background.xml)',metavar='Output file')
parser.add_argument('--version', action='version', version='%(prog)s 1.01')
parser.add_argument('-D','--directory',type=directory,default=os.getenv('HOME')+"/Pictures",help='directory location of image files')

args = parser.parse_args()
if args.Cmd is False:
	try:
		#import PyQt4
		from gui import main
		main()
	except ImportError:
		print ('PyQt4 libary is not found\nTry command line Interface')
		parser.print_help()
else:
	#intitializing varables
	path = os.path.abspath(args.directory)+'/'
	outfile=path+args.path
	dirs = os.listdir(path)
	dirs.sort()
	#main program
	import xmlmsg
	from imagepro import *
	x = xmlmsg.xml(path,(args.time)*60.0-5)
	f=open(outfile,'w')
	f.write(x.start)
	for i in dirs:
		if isimage(i):
			askadd(i,args.action,path,f,x)
	f.write("\n<to>"+path+image.start+x.end)
	f.close()
	close(outfile)

