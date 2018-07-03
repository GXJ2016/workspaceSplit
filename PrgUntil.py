__author__ = 'Administrator'
import os


def scanFile(path, filelist):
    pathall = os.listdir(path)
    for itempath in pathall:
        if os.path.isdir(path + '/' + itempath):
            scanFile(path + '/' + itempath, filelist)
        elif os.path.isfile(path + '/' + itempath):
            filelist.append(path + '/' + itempath)
        else:
            pass


def testEntry():
    testfile = "./"
    testfilelist = []
    scanFile(testfile, testfilelist)
    print(testfilelist)


if __name__ == '__main__':
    testEntry()
else:
    pass
