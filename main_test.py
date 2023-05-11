import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '35 5 10 20 40 15'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    number = [35, 5, 10, 20, 40, 15]
    main.bubble(number)
    assert number[0] == 5
    assert number[1] == 10
    assert number[2] == 20
    assert number[3] == 35
    assert number[4] == 15
    assert number[5] == 40
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    main.bubblesort(number)
    assert number == sorted(number)
