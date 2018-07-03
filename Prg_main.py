__author__ = 'Administrator'
import PrgUntil
standardPrgfile = "./Dt_hix/"

def entry():
    # print ("upload to github")
    filelist = []
    PrgUntil.scanFile(standardPrgfile,filelist)
    print (filelist)

if __name__ == '__main__':
    entry()

    print ("prg end")
else:
    pass