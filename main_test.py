import main
import io
import sys
import re
import math
import types


def test_main_1():
    main.main()
    students = main.makeList()
    assert len(students) == 5
    main.printList(students)


def test_main_2():
    students = main.makeList()
    ret = main.scorebySubject(students)
    keys = list(ret.keys())
    print(keys)
    assert keys == ['1st', '2nd', '3rd', '4th'], "Key must be ['1st', '2nd', '3rd', '4th'] "
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
