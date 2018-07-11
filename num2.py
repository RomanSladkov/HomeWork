from builtins import ValueError

import logging
import numpy
import site
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=u'result.log')

def Errors(num):

    if num == 1:
        print("Error: in file many space")
        logging.critical(u'Error: in file many space\n')
    elif num == 2:
        print("Error! empty string")
        logging.critical('Error! empty string\n')
    elif num == 3:
        print("Error! wrong number")
        logging.critical(u'Error! wrong number\n')
    elif num == 4:
        print("Error: file error")
        logging.critical(u'Error: file error\n')
    elif num == 5:
        print("Error: matrix must be > 1")
        logging.critical(u'Error: matrix must be > 1\n')
    elif num == 5:
        print("Error: program can't take answer ")
        logging.critical(u"Error: program can't take answer\n")
    quit()

print('Enter name of file ', end='')
nameFile = input()

try:
    file = open(nameFile)
except IOError as error:
    print(str(error))
else:
    with file:
        line = file.readline()
        try:
            MatrixLen = int(line)
        except ValueError:
            Errors(3)
        if MatrixLen < 1:
            Errors(5)
        arr: object = numpy.zeros((MatrixLen, MatrixLen))
        arr1 = numpy.zeros((MatrixLen))
        print(arr)
        buf = ""
        i: int = 0
        j: int = 0
        while True:
            c = file.read(1)
            if not c:
                if i == MatrixLen:
                    Errors(2)
                try:
                    arr1[i] = float(buf)
                except ValueError:
                    Errors(3)
                print("End of file")
                break
            elif (c == ' ') or (c == '\n'):
                if (buf != ""):
                    if c == ' ':
                        if j == MatrixLen:
                            Errors(1)
                        try:
                            arr[i, j] = float(buf)
                        except ValueError:
                            Errors(3)
                    else:
                        if i == MatrixLen:
                            Errors(2)
                        try:
                            arr1[i] = float(buf)
                        except ValueError:
                            Errors(3)
                    if c == ' ':
                        j = j + 1
                        buf = ""
                    if c == '\n':
                        i = i + 1
                        j = 0
                        buf = ""
            elif (c.isdigit()) or (c == '-') or (c == '.'):
                buf = buf + c
            else:
                Errors(4)
    print(arr)
    print(arr1)

    try:
        print(numpy.linalg.solve(arr, arr1))
    except ValueError:
        Errors(6)
    a = ""
    a = str(numpy.linalg.solve(arr, arr1))

    logging.info(u'- date, program running')
    logging.info("Answer: " + a + "\n")