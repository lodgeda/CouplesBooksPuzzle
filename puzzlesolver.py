# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

x,y,z,i = 0,0,0,0

# These two variables are going to hold the stacks of operations that I'm performing so I can back up 
StepW = [] #this is the woman row, which is 1-9
StepE = [] #this is the everything else row, 10-22


OriginalProblem = [
['HisName', 'Hername', 'LastName', 'BookBrought', 'BookLeft', 'Color', 'Car','Jerb'],
['','Daniella', 'Black','','','','','','Shop-Assistants'],
['Otto','Irene','','','','','','Accountants'],
['','Veronica', 'Dvorak','','','Blue','',''],
['Owen', 'Victoria','','','','Brown','',''],
['Stan','Hannah','Horricks','','','White','',''],
['','Jenny','Smith','','','','Wartburg', 'Warehouse Managers'],
['Alexander', 'Monica','','','Grandfather Joseph','','',''],
['','Pamela','','Grandfather Joseph','','','Renault',''],
['Matthew','','','Gabriela','','Pink','',''],
['','','','SeaDog','','Fiat','Red',''],
['','','','','WeWereFive','','Trabant',''],
['','','Cermak','ShedStoat','','','','TicketCollectors'],
['','','Kuril','','Slovako','','','Doctors'],
['Paul','','','','','Green','',''],
['Rick','','','Slovako','','','Ziglui',''],
['','','','Dame','Gabriella','','',''],
['','','','','','Violet','Dacia',''],
['','','','','Dame','','','Teachers'],
['','','','','','','Moskovic', 'Farmers'],
['Robert','','','ModernComedy','','Yellow','',''],
['','','Swain','','','','','Shoppers'],
['','','','ModernComedy','','','Skoda','']
] 

#This matrix will be malleable as the problem is being solved.  The only difference is that this matrix has a 1 to begin each row, which indicates in 
#use, or 0 if the row has already been combined
WorkingProblem = [
[1,'HisName', 'Hername', 'LastName', 'BookBrought', 'BookLeft', 'Color', 'Car','Jerb'],
[1,'','Daniella', 'Black','','','','','','Shop-Assistants'],
[1,'Otto','Irene','','','','','','Accountants'],
[1,'','Veronica', 'Dvorak','','','Blue','',''],
[1,'Owen', 'Victoria','','','','Brown','',''],
[1,'Stan','Hannah','Horricks','','','White','',''],
[1,'','Jenny','Smith','','','','Wartburg', 'Warehouse Managers'],
[1,'Alexander', 'Monica','','','Grandfather Joseph','','',''],
[1,'','Pamela','','Grandfather Joseph','','','Renault',''],
[1,'Matthew','','','Gabriela','','Pink','',''],
[1,'','','','SeaDog','','Fiat','Red',''],
[1,'','','','','WeWereFive','','Trabant',''],
[1,'','','Cermak','ShedStoat','','','','TicketCollectors'],
[1,'','','Kuril','','Slovako','','','Doctors'],
[1,'Paul','','','','','Green','',''],
[1,'Rick','','','Slovako','','','Ziglui',''],
[1,'','','','Dame','Gabriella','','',''],
[1,'','','','','','Violet','Dacia',''],
[1,'','','','','Dame','','','Teachers'],
[1,'','','','','','','Moskovic', 'Farmers'],
[1,'Robert','','','ModernComedy','','Yellow','',''],
[1,'','','Swain','','','','','Shoppers'],
[1,'','','','ModernComedy','','','Skoda','']
] 

# <codecell>

print OriginalProblem

# <codecell>

#so the clues provided in the problem give a 8 categories by 23 clues matrix, with the final result being a 8 categories by 8 couples matrix

# <codecell>

len(OriginalProblem)

# <codecell>

def RowsMatch(row1, row2):
    dorowsmatch = True
    for i in range(1,8):
        if WorkingProblem[row1][i] != '':
            if WorkingProblem[row2][i] != '':
                dorowsmatch = False
    return dorowsmatch

def RowAvailable(row1):
    return WorkingProblem[row1][0]

# <codecell>

def CombineRows(fromrow,torow):
    for i in range(1,8):
        if WorkingProblem[fromrow][i] != '':
            WorkingProblem[torow][i] = WorkingProblem[fromrow][i]
    WorkingProblem[fromrow][0] = 0
    
def PuzzleSolved():
    for i in range(9,22):
        if WorkingProblem[i][0] == 1:
            return False
    return True

def UnCombineRows(MainRow,SplitRow):
    for i in range(1,8):
        if WorkingProblem[SplitRow][i] != '':
            WorkingProblem[MainRow][i] = ''
    WorkingProblem[SplitRow][0] = 1
    
def PrintWorkingProblem():
    for x in range(0,23):
        print x, WorkingProblem[x][0], WorkingProblem[x][1], WorkingProblem[x][2],  WorkingProblem[x][3], WorkingProblem[x][4], WorkingProblem[x][5], WorkingProblem[x][6], WorkingProblem[x][7], WorkingProblem[x][8]
    for x in range(0,len(StepW)):
        print StepW[x], ", ", StepE[x]

# <codecell>

for i in range(1,9):
    for j in range(10,22):
        #i is the row with the woman, and j is the row with everything else.  All j rows will eventually be consolidated into i rows
        
        if RowAvailable(j):
            if (RowsMatch(i,j) == True):
                CombineRows(j,i)
                StepW.append(i)
                StepE.append(j)

#Now that the steps are full, see if the puzzle was solved
if PuzzleSolved() != True:
    #so the puzzle is not solved, back up steps and try other solns
    
    
    
else:
    Print "Puzzle Solved!!"

# <codecell>

len(StepW)

# <codecell>

PrintWorkingProblem()


# <codecell>


# <codecell>

WorkingProblem[1], WorkingProblem[2], StepsFrom, StepsTo

