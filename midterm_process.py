import argparse
import sys


parser = argparse.ArgumentParser(description="parses scantron dat files")
parser.add_argument("-d","--dat", type=str, help = "dat file")
parser.add_argument("-g","--grades", type=str, help = "grade output")
parser.add_argument("-s","--stats", type=str, help = "stats output")
parser.add_argument("-k","--key", type=str, help = "keystring")

_args = parser.parse_args()
sys.stderr.write(str(_args)+"\n")


myKey = list(_args.key)
#myKey = key.split()
statsList = [0]*len(myKey)
studentList = []

dat = open(_args.dat, 'r')
grades = open(_args.grades,'w')
stats = open(_args.stats,'w')

for line in dat:
    myEnt = line.rstrip().split()
    studentNumName = myEnt[4]
    try:
        answers = list(myEnt[6])
    except:
	sys.stderr.write(line+"not enough fields")
	sys.exit()
#    print(studentNumName)
#    print(answers)
    correct = 0
    #time to grade
    #for number,letter in enumerate(answers):
    for number in range(0,len(myKey)):
	letter = answers[number]
        if letter == myKey[number]:
            #it's correct! add to student's grade
            correct = correct + 1
            #add to stats list
            statsList[number] = statsList[number]+1
        else:
            pass

    if answers[len(myKey)+1] != "_":
	sys.stderr.write(line)
	sys.stderr.write("key too short")
	sys.exit()      
  
    #add to student list
    studentList.append(correct)
    
    grades.write(studentNumName+"	"+str(correct)+"\n")
    
classSize = len(studentList)
classMean = float(sum(studentList))/classSize

stats.write("Class average is    "+str(classMean)+"\n")
for number, question in enumerate(statsList):
    stats.write(str(number+1)+"    "+str(float(question)/classSize)+"\n")
