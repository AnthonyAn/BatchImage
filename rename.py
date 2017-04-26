import os,re

def rename():
	path=os.getcwd()
	filelist=os.listdir(path)
	i=1
	for files in filelist:

		olddir=os.path.join(path,files);
		if os.path.isdir(olddir):
			continue;

		filename=os.path.splitext(files)[0];
		filetype=os.path.splitext(files)[1];

		if(filename=='rename'):
			continue

		if(re.match(r'苏大 ',filename)):
			newdir=os.path.join(path,str(i)+filetype);
			i=i+1
			os.rename(olddir,newdir);

rename();