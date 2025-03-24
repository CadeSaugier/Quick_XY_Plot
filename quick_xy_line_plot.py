#This program will plot line graphs corresponding to each .xy file input in one plot.
#Program use: Python3 quick_xy_line_plot.py file1.xy file2.xy file3.xy ...
#Program by: Cade Saugier, INPP EAL Ohio University.

import sys
from matplotlib import pyplot

#Build Main
def main():
	print('\n~~~~~~~~~~ QUICK XY LINE PLOT ~~~~~~~~~~\n')
	
	###Get Arguments
	args = sys.argv[1:]
	
	###Build Data Sets
	fileName=[]
	dataY=[]
	dataX=[]
	
	###Open Files and Pull Data
	for i in args:
		print('->Opening File '+i)
		try:
			dataFile=open(i,'r')
		except:
			print('-->File Read Error!')
			continue
		if i[-3:]!='.xy':
			print('-->File Not .xy Format!')
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
		binNum , countNum = pull(dataFile)
		dataX+=[binNum]
		dataY+=[countNum]
		#Close File
		dataFile.close()
	
	###Build Plots
	pyplot.figure(1)
	print('\n')
	for i in range(len(fileName)):
		print('--> Plotting Data '+fileName[i])
		pyplot.plot(dataX[i],dataY[i],label=fileName[i])
	print('\n')
	answer=input('--->Y Scale Log? (y/n):')
	if answer=='Y' or answer=='y':
		pyplot.yscale('log')
	answer=input('--->X Scale Log? (y/n):')
	if answer=='Y' or answer=='y':
		pyplot.xscale('log')
	pyplot.title('Quick_XY_Line_Plot')
	pyplot.xlabel('X-Value')
	pyplot.ylabel('Y-Value')
	pyplot.legend()
	pyplot.show()
	
	print('\n--> Done! ^_^\n')
	exit()




############# FUNCTION LIST #############
def pull(data):
	#Pull Bin and Count
	read=data.readlines()
	binnum=[]
	countnum=[]
	for i in range(len(read)):
		l=0
		for k in read[i]:
			if k!=' ':
				l=l+1
			else:
				break
		l=l+1
		binnum+=[float(read[i][:l])]
		countnum+=[float(read[i][l:-1])]
	return [binnum,countnum]


#Run Main
main()
