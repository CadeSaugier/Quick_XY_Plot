#This program will plot 2D histograms corresponding to each .xyz file input in seperate plots with equally sized bins.
#Program use: Python3 quick_xyz_plot.py file1.xy file2.xy file3.xy ...
#Program by: Cade Saugier, INPP EAL Ohio University.

import sys
from matplotlib import pyplot

#Build Main
def main():
	print('\n~~~~~~~~~~ QUICK XYZ PLOT ~~~~~~~~~~\n')
	
	###Get Arguments
	args = sys.argv[1:]
	
	###Build Data Sets
	fileName=[]
	dataMatrix=[]
	
	###Open Files and Pull Data
	for i in args:
		print('->Opening File '+i)
		try:
			dataFile=open(i,'r')
		except:
			print('-->File Read Error!')
			continue
		if i[-4:]!='.xyz':
			print('-->File Not .xyz Format!')
			continue
		#Get Name
		hit=0
		adj=0
		for k in range(len(i)):
			if i[k]=='/':
				hit=k
				adj=1
		fileName+=[i[hit+adj:]]
		#Get Data
		dataMatrix+=[pull3(dataFile)]
		#Close File
		dataFile.close()
	
	###Plot Data
	print('\n')
	for i in range(len(fileName)):
		print('--> Plotting Data '+fileName[i])
		pyplot.matshow(dataMatrix[i])
		pyplot.title('Quick_XYZ_Plot  '+fileName[i])
		pyplot.xlabel('X Bin (unitless)')
		pyplot.ylabel('Y Bin (unitless)')
		pyplot.tick_params(bottom=True,top=False,labelbottom=True,labeltop=False)
		pyplot.gca().invert_yaxis()
			
	##Display Plot
	pyplot.show()
	
	print('\n--> Done! ^_^\n')
	exit()



############# FUNCTION LIST #############
def pull3(data):
	#Pull X, Y, and Z Data
	read=data.readlines()
	x=[]
	y=[]
	z=[]
	for i in range(len(read)):
		space1=0
		space2=0
		for j in range(len(read[i])):
			if read[i][j]==' ' and space1==0:
				space1=j
			elif read[i][j]==' ' and space1!=0:
				space2=j
		y+=[int(read[i][:space1])]
		x+=[int(read[i][space1+1:space2])]
		z+=[int(read[i][space2+1:])]
	xSize=max(x)
	ySize=max(y)
	if 0 in x:
		xSize+=1
	if 0 in y:
		ySize+=1
	mat=[]
	for i in range(xSize):
		mat+=[[]]
		for j in range(ySize):
			mat[i]+=[0]
	k=0
	for i in range(xSize):
		for j in range(ySize):
			mat[i][j]+=z[k]
			k+=1
	return mat


#Run Main
main()
