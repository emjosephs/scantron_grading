#dat = open('EHJ352 Midterm F2012.dat','r')
dat = open('ehj352apr2015.csv','r')
grades = open('EHJ352_MultChoice_Grades_fixed.txt','w')
stats = open('EHJ352_Question_Stats.txt','w')

#change key as needed
key = "d	e	c	b	c	c	d	a	b	b	d	a	b	c	b	b	a	b	c	e"
#myKey = list(key)
myKey = key.split()
statsList = [0]*len(myKey)
studentList = []

dat.readline()
dat.readline()
for line in dat:
    myEnt = line.rstrip().split(',')
    studentNum = myEnt[4]
    studentLastName = myEnt[5]
    studentFirstName = myEnt[6]
    answers = myEnt[7:]
    correct = 0
    
    #time to grade
    for number,letter in enumerate(answers):
        if letter == myKey[number]:
            #it's correct! add to student's grade
            correct = correct + 1
            #add to stats list
            statsList[number] = statsList[number]+1
        else:
            pass
        
    #add to student list
    studentList.append(correct)
    
    grades.write(studentNum+"    "+studentLastName+"    "+studentFirstName+"	"+str(correct)+"\n")
    
classSize = len(studentList)
classMean = float(sum(studentList))/classSize

stats.write("Class average is    "+str(classMean)+"\n")
for number, question in enumerate(statsList):
    stats.write(str(number+1)+"    "+str(float(question)/classSize)+"\n")
