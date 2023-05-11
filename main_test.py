import main
import io
import sys
import re
import math
import types


def test_main_1():
    # captureOut = io.StringIO()
    # sys.stdout = captureOut
    # datastr = '35 5 10 20 40 15'
    # sys.stdin = io.StringIO(datastr)

    # main.main()
    # sys.stdout = sys.__stdout__
    # print('Captured ', captureOut.getvalue())
    # lines = captureOut.getvalue().split('\n')
    # print(lines)

    main.main()
    students = main.makeList()
    assert len(students) == 5
    main.printList(students)

    ret = main.scorebySubject(students)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())


def test_main_2():
    students = main.makeList()
    ret = main.scorebySubject(students)
    assert len(ret) == 4
    assert sum(ret['1st']) == 490
    assert sum(ret['2nd']) == 430
    assert sum(ret['3rd']) == 400
    assert sum(ret['4th']) == 400


def test_main_3():
    students = main.makeList()
    ret = main.findStudents(students)
    assert len(ret) == 3


def test_main_4():
    students = main.makeList()
    ret = main.getAvgList(students)
    assert len(ret) == 5
    assert ret[0] == 77.5
