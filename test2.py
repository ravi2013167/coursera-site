import csv
import glob
import xlsxwriter
import os
import win32com.client

with open('Test2.csv') as f:
	reader = csv.reader(f)
	c = 0
	k = 0
	count = 0
	flag = 0
	scene = []
	for row in reader:
		c += 1;
		if( c==1):
			x = row
			continue
		if(len(row)==1):
			y = row
			cx = 0
			count += 1
			flag=0
			continue
		if(len(row)>1):
			print(cx)
			flag+=1
			if os.path.isfile(str(count)+'.csv') and flag == 1:
				if (len(str(count)+'.csv') > 0):
					xee = open(str(count) + '.csv', 'w')
					with open(str(count)+'.csv', 'a') as g:
						write = csv.writer(g)
						if(cx==0):
							name = count
							scene.append(name)
							k+=1
							write.writerows([x])
							write.writerows([y])
						cx=1

					with open(str(count)+'.csv', 'a') as f:
						writerr = csv.writer(f)
						writerr.writerows([row])
				else:
					with open(str(count)+'.csv', 'a') as g:
						write = csv.writer(g)
						if(cx==0):
							name = count
							scene.append(name)
							k+=1    
							write.writerows([x]) 
							write.writerows([y])
                                        	cx=1
					with open(str(count)+'.csv', 'a') as f:
						writerr = csv.writer(f)
						writerr.writerows([row])

			else:
				print 'hola'
				with open(str(count)+'.csv', 'a') as g:
					write = csv.writer(g)
					if(cx==0):
						name = count
						scene.append(name)
						k+=1
						write.writerows([x])
						write.writerows([y])
					cx=1
				with open(str(count)+'.csv', 'a') as f:
					writerr = csv.writer(f)
					writerr.writerows([row])

excelfile = xlsxwriter.Workbook('demo.xlsx')
for r in scene:
	worksheet = excelfile.add_worksheet();
        #worksheet.OLEObjects().Add(FileName=str(r)+'.csv', Link=False, DisplayAsIcon=True).Select
	#worksheet.OLEObjects().Add(('A1',  str(r)+'.csv')
excelfile.close()

