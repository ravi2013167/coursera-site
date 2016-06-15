import csv
import glob
import xlsxwriter
import os
#from win32 import win32api
import sys

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
				print ('hola')
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



import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\ravi.jain\\Downloads\\teee.xlsx')
#wb.Application.Run("setA4", '4')

for r in scene:
	ws = wb.Worksheets('Sheet' + str(r))
	ws.Name = 'Scenario - ' + str(r)
	ws.Range(ws.Cells(1,3),ws.Cells(126,3)).Font.Size = 12
	for i in range(1,126):
		if ws.Cells(i,3).Value == 'Test Cases':
			object = ws.OLEObjects().Add(Filename= 'C:\\Users\\ravi.jain\\Downloads\\' + str(r) + '.csv', DisplayAsIcon=True, IconIndex = 0, IconFileName = 'C:\\Users\\ravi.jain\\Downloads\\1463757178_csv.ico', IconLabel = "Scenario - " + str(r) )
			object.IconFileName = 'C:\\Users\\ravi.jain\\Downloads\\1463757178_csv.ico'
			#print (object.IconFileName)
			#print (object.IconLabel)
			object.Height = 60
			object.Width = 60
			object.Shadow = True
			object.Left += 200
			object.IconLabel = 'sd'
			object.Border = 3
			
	'''for i in range(1,5):
		ws.Cells(2,i).Value = i  # Don't do this
	ws.Range(ws.Cells(3,1),ws.Cells(3,4)).Value = [5,6,7,8]
	ws.Range("A4:D4").Value = [i for i in range(9,13)]
	ws.Cells(5,4).Formula = '=SUM(A2:D4)'
	ws.Cells(5,4).Font.Size = 16
	ws.Cells(5,4).Font.Bold = True
	'''
	
	'''for row in rang(1, 10):
		if 'dsa' == ws.Cells(row,6).value:
			print('yes')
			#ws.OLEObjects().Add(Filename= 'C:\\Users\\ravi.jain\\Downloads\\' + str(r) + '.csv', DisplayAsIcon=True, height=100, width=100).Select
	'''	