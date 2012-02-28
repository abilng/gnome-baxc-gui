import os
import string

class image:
	count=0
	extentions=['.jpg','.png','.jpeg']
	start=None


def load(outfile):
	if os.system('gconftool -s \'/desktop/gnome/background/picture_filename\' \''+outfile+'\' -t string 2>/dev/null')== 0:
		pass
	else:
		os.system('GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri \'file://'+outfile+'\' 2>/dev/null')



def close(outfile):
	if image.count==0:
		os.remove(outfile)
#		print ('No jpg image on that dir(or u said \'not to add\')')
	else:
		load(outfile)	
#		print ('\n added'+str(image.count)+'image(s) \noutput file:'+outfile+'\n')
#		print ('load(ed) file by \n')
#		print ('GNOME 3:\" GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri \'file://'+outfile+'\' \"\n')
#		print ('GNOME 2:\" gconftool -s \'/desktop/gnome/background/picture_filename\' \''+outfile+'\' -t string \"\n ')




#finding is-image file
def isimage(i):
	for ext in image.extentions:
		if i.find(ext) == -1:
			pass
		else:
			return True
	return False

def ask_ok(prompt):
	retries=2
	complaint='Yes or no, please!'
	while True:
		ok = str(input(prompt))
		if ok in ('y', 'ye', 'yes','Y'):
			return True
		elif ok in ('n', 'no', 'nop','N', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			image.count=0
			close()
			raise IOError('refusenik user')
		print (complaint)

def add(i,path,f,x):
	if image.count==0:
		image.count=image.count+1
		f.write(x.s1+i+x.s2+i+x.s3)
		image.start=i
	else:
		s0='\n<to>'+path+i+'</to> \n</transition>'
		f.write(s0+x.s1+i+x.s2+i+x.s3)
		image.count=image.count+1

def askadd(i,action,path,ofile,x):
	if action==False :
		add(i,path,ofile,x)
	elif ask_ok('Add '+i+' ?:'):
		add(i)

