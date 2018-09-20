__author__ = 'Administrator'

Prase_Aim = "P.h"

__OUTER_HEADER = "typedef struct"
__OUTER_TAILER_H = "}"
__OUTER_TAILER_E = ";"


def findiner(inar):
    print(inar)
    pass


def findouter(ar):
    outerflag = False
    for ix in ar:

        if ix.strip().startswith(__OUTER_HEADER):
            outerflag = True
        if outerflag and ix.strip().startswith(__OUTER_TAILER_H) and \
                ix.strip().endswith(__OUTER_TAILER_E):
            outerflag = False
            outer_name = ix.split(" ")[-1].strip(";")
            print(outer_name)
        if outerflag:
            findiner(ix)


def entry():
    with open(Prase_Aim, "r") as f:
        context = f.readlines()
        findouter(context)
        f.close()


if __name__ == '__main__':
    entry()
    pass
else:
    pass
