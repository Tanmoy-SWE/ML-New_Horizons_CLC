CGPA = [3.58, 2.67, 3.01, 3.23, 2.76, 2.99]
ExCurr = ['High','High','Low','High','Low','Low']
IELTS = ['Low', 'High', 'High', 'Low', 'High', 'High']
Job = ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']

catCGPA = []
for i in range(0, len(CGPA)):
    if CGPA[i] >= 3.5:
        catCGPA.append('High')
    elif CGPA[i] < 3.5 and CGPA[i] >= 3.0:
        catCGPA.append('Mid')
    else :
        catCGPA.append('Low')
print(catCGPA)

cg = 'Low'
cgcnt = 0
extraC = 'High'
excnt = 0
IELTSscore = 'High'
IELTScnt = 0
jobYes = 'Yes'
jobcnt = 0
for i in range(0, len(CGPA)):
    if catCGPA[i] == cg and Job[i]=='Yes':
        print('HIIII')
        cgcnt = cgcnt + 1
    if ExCurr[i] == extraC and Job[i]=='Yes':
        excnt = excnt + 1
    if IELTS[i] == IELTSscore and Job[i]=='Yes':
        IELTScnt = IELTScnt + 1
    if Job[i] == jobYes:
        jobcnt = jobcnt + 1

print(cgcnt, excnt, IELTScnt)
ProbCG = cgcnt / jobcnt
ProbEx = excnt / jobcnt
ProbIelts = IELTScnt / jobcnt
ProbJobYes = jobcnt / len(Job)
ProbJobNo = 1 - ProbJobYes

print("CG->Low, Extracurricular->High, IELTS->High")
print("If Yes, probability :",ProbCG*ProbEx*ProbIelts*ProbJobYes)

