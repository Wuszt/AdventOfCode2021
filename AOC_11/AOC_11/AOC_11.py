rows=

defProcess(xy):
ifx<0ory<0ory>=len(rows)orx>=len(rowsy):
return

rowsyx+=1
ifrowsyx==10:
Process(x-1y)
Process(x-1y+1)
Process(x-1y-1)
Process(xy+1)
Process(xy-1)
Process(x+1y)
Process(x+1y+1)
Process(x+1y-1)

file=open("input.txt""r")
forlineinfile:
rows.append(int(x)forxinline.strip())

defTask1():
stepsAmount=1000
flashes=0
foriinrange(stepsAmount):
currentFlashes=0
foryinrange(len(rows)):
forxinrange(len(rows0)):
Process(xy)

foryinrange(len(rows)):
forxinrange(len(rows0)):
ifrowsyx>9:
currentFlashes+=1
rowsyx=0

flashes+=currentFlashes

print("Task1answer:"+str(flashes))

defTask2():
flashes=0
i=0
while(True):
i+=1
currentFlashes=0
foryinrange(len(rows)):
forxinrange(len(rows0)):
Process(xy)

foryinrange(len(rows)):
forxinrange(len(rows0)):
ifrowsyx>9:
currentFlashes+=1
rowsyx=0

ifcurrentFlashes==len(rows)*len(rows0):
print("Task2answer:"+str(i))
return

#Task1()
Task2()