import fangUtil
import sys

stuID = 'studentID.txt'
npath = 'name.txt'
ppath = 'phone.txt'


def combine(outpath):
    fh1 = fangUtil.FileHelper(stuID)
    fh2 = fangUtil.FileHelper(npath)
    fh3 = fangUtil.FileHelper(ppath)
    # fh4 = fangUtil.FileHelper(ppath)

    out_fh = fangUtil.FileHelper(outpath)
    out_fh.open('w')

    line1 = fh1.open().readline()
    line2 = fh2.open().readline()
    line3 = fh3.open().readline()
    # line4 = fh4.open().readline()

    while line1:
        nl1 = fangUtil.StringUtil.filter(line1,'\r\n')
        nl2 = fangUtil.StringUtil.filter(line2,'\r\n')
        nl3 = fangUtil.StringUtil.filter(line3,'\r\n')
        # nl4 = fangUtil.StringUtil.filter(line4,'\r\n')

        nl = nl1 + ',' + nl2 + ',' + nl3 + '\r\n'
        out_fh.writelines(nl)

        line1 = fh1.readline()
        line2 = fh2.readline()
        line3 = fh3.readline()
    fh1.close()
    fh2.close()
    fh3.close()
    out_fh.close()

if __name__ == '__main__':
    combine(sys.argv[1])