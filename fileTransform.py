import fangUtil
import sys

def filetransform(inpath):
    in_fh = fangUtil.FileHelper(inpath)

    strlist = []

    line = in_fh.open().readline()
    while line:
        nl = fangUtil.StringUtil.filter(line, '\r\n')
        nl = fangUtil.StringUtil.wrap(nl, '\'')
        nl += '\r\n'
        strlist.append(nl)
        line = in_fh.readline()

    in_fh.close()
    in_fh.open('w')
    in_fh.writelines(strlist)
    in_fh.close()
    return strlist

if __name__ == '__main__':
    filetransform(sys.argv[1])