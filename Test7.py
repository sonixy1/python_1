import sys

intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None] * 8

if __name__ == "__main__":
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

    print('int형의 데이터 크기', sys.getsizeof(intVar))
    print('float형의 데이터 크기', sys.getsizeof(floatVar))
    print('bool형의 데이터 크기', sys.getsizeof(boolVar))
    print('str형의 데이터 크기', sys.getsizeof(strVar))
    print('list형의 데이터 크기', sys.getsizeof(listVar))
    print('tuple형의 데이터 크기', sys.getsizeof(tupleVar))
    print('dictionary형의 데이터 크기', sys.getsizeof(dictVar))
    print('set형의 데이터 크기', sys.getsizeof(setVar))