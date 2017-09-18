from textstat.textstat import textstat
import argparse
import os
"""
     Given a path to a dir containing chunk folders 
     generate a file for every chunk folder such as:

     chunkname_subjectname avg_lwf avg_fog

     which will be used with another script to combine as new attributes to representation files 
"""
lwf = lambda x: textstat.linsear_write_formula(x)
fog = lambda y: textstat.gunning_fog(y)

def get_chunknames(path):

	for direc in os.listdir(path):
		if os.path.isdir(direc):
			yield direc 

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='USAGE :   python readscorer.py --path <folder contatining chunk folders> ')
	parser.add_argument('-p','--path',help='folder contatining chunk folders',required=True)
	args= vars(parser.parse_args())


