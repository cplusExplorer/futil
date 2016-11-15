import sys
import getopt


class FileHelper:
    "a File Helper class for easy use Python File I/O"

    def __init__(self, path):
        self.__path = path
        self.__opened = False

    def setFilePath(self, path):
        "set filepath.if the object has set path before,will close and reset file"
        if(self.__opened):
            self.close()
        self.__path = path
        return self

    def open(self, mode='r'):
        "open the file according the path"
        try:
            self.__fo = open(self.__path, mode)
            self.__opened = True
        except IOError:
            raise IOError("can not find the file")
        return self

    def close(self):
        "close the file"
        if(self.__opened):
            self.__fo.close()
        return self

    def readline(self):
        "read one line data from file"
        if(self.__opened):
            return self.__fo.readline()
        else:
            raise IOError('file has not open yet!')
        return self

    def writelines(self, contend):
        "write line into the file"
        try:
            if(self.__opened):
                self.__fo.writelines(contend)
        except IOError:
            raise IOError("Exception:make sure the file can be wirte")
        return self

    def seek(self, offset, whence=0):
        "relocation of reading/writing place of the file"
        if (self.__opened):
            return self.__fo.seek(offset,whence)
        else:
            raise IOError('file has not open yet!')
        return self

    def __del__(self):
        self.close()


class CmdHelper:
    "command line helper class"
    def __init__(self, optDict):
        self.__optDict = optDict

    def generate(self,argv):
        "generate a map between option and value"
        optcmd = self.__getoptcmd()
        # try to get opts
        try:
            opts, args = getopt.getopt(argv, optcmd)
        except getopt.GetoptError:
            self.usage()
            sys.exit(-1)
        # get opt
        optlist = self.__getoptList()
        keys = self.__optDict.keys()
        paramDict = {}
        for opt, arg in opts:
            index = optlist.index(opt)
            paramDict[self.__optDict[keys[index]]] = arg
        return paramDict


    def __getoptcmd(self):
        "get option cmd through optMap"

        keys = self.__optDict.keys()
        optcmd = ''
        for key in keys:
            optcmd += key
        return optcmd;

    def __getoptList(self):
        optlist = []
        optcmd = self.__getoptcmd()
        for letter in optcmd:
            if(letter == ':'):
                pass
            else:
                s = '-' + letter
                optlist.append(s)
        return optlist

    def usage(self):
        nl = '\r\n'
        nb = '    '
        usagestr = 'usage:'+nl
        optlist = self.__getoptList()
        keys = self.__optDict.keys()
        for index in range(len(optlist)):
            usagestr += optlist[index] + nb + self.__optDict[keys[index]]
        usagestr += nl
        print usagestr



class CmdHelper2:
    "command line helper class"
    def __init__(self,func_usage,func_opt,optcmd):
        self.__func_usage = func_usage
        self.__func_opt = func_opt
        self.__optcmd = optcmd

    def dowork(self, argv):
        try:
            opts, args = getopt.getopt(argv, self.__optcmd)
        except getopt.GetoptError:
            self.__func_usage()
            sys.exit(-1)

        self.__func_opt(opts)


class StringUtil:

    @classmethod
    def filter(cls, oldstr, filterstr):
        "filter the bad char of the string"
        nstr = ''
        for letter in oldstr:
            if -1 == filterstr.find(letter):
                nstr += letter
        return nstr

    @classmethod
    def wrap(cls,oldstr,wrapchar):
        "wrap the string with wrapchar"
        nstr =wrapchar + oldstr +wrapchar
        return nstr

    @classmethod
    def list2str(cls,inputlist):
        "transform a string list into a string"
        return ''.join(inputlist)

    @classmethod
    def str2list(cls,inputstr):
        "transform a string into list in every char"
        nl = []
        for letter in inputstr:
            nl.append(letter)
        return nl
    @classmethod
    def strsplit(cls, oldstr, splitchar):
        nl = []
        index = oldstr.find(splitchar)
        flag = 0
        while index != -1:
            flag = 1
            nl.append(oldstr[0:index])
            oldstr = oldstr[index+1:len(oldstr)]
            index = oldstr.find(splitchar)
            if -1 == index and len(oldstr) != 0:
                nl.append(oldstr)
                break
        if flag == 0:
            nl.append(oldstr) # if old string doesn't have splitchar
        return nl


if __name__ == '__main__':
    # 1.test CmdHelper

    print 'test CmdHelp'
    optionDict = {'h': 'help', 'i:': 'inputfile', 'o:': 'outputfile'}
    ch = CmdHelper(optionDict)
    reMap = ch.generate(sys.argv[1:])
    print reMap

    # 2.test CmdHelper2
    print 'test CmdHelp2'

    # 3.test FileHelper


    # 4. test StringFilter
    t = '1234:'
    a = ['1','2','ad']
    print StringUtil.filter(t, ':')
    print StringUtil.wrap(t,'\'')
    print StringUtil.list2str(a)
