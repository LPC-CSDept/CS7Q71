
from functools import reduce
import pandas as pd


def makeList():
    ##################################################
    # Code your program here
    ##################################################
    df = pd.read_excel('students.xls')
    keys = ['id', 'name', 'scores']
    students = []
    for i in range(df.shape[0]):
        scores = list(df.iloc[i][2:])
        values = [df.iloc[i][0], df.iloc[i][1], scores]
        d = (dict(zip(keys, values)))
        students.append(d)
        # print (values)

    return students


def printList(students):
    for student in students:
        for k, v in student.items():
            print(f'{k} -> {v}', end='\t')
        print()


def scorebySubject(students):
    scorelist = []
    keys = ['1st', '2nd', '3rd', '4th']
    for student in students:
        scorelist.append(student['scores'])
    retdict = dict(zip(keys, zip(*scorelist)))
    return retdict


def gt330(x): return sum(x['scores']) > 330


def findStudents(students):
    fobj = filter(gt330, students)
    return list(fobj)


def getAvg(x, y): return x + y


def getAvgList(students):
    retlst = []
    for student in students:
        savg = reduce(getAvg, student['scores']) / len(student['scores'])
        retlst.append(savg)
    return retlst


def main():
    # (1) makeList
    students = makeList()
    # (2) printList
    printList(students)
    # (3) scorebySubject
    retval = scorebySubject(students)
    for k, v in retval.items():
        print(f'{k} -> {v}', end='\t')
    print()
    # (4) findStudents
    retval = findStudents(students)
    printList(retval)
    # (5) getAvgList
    retval = getAvgList(students)
    print(retval)


if __name__ == '__main__':
    main()
