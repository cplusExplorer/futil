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
    def __init__(self,optMap, usage_func):
        self.__usage_func = usage_func
        self.__optMap = optMap

    def generate(self,argv):
        "generate a map between option and value"
        optcmd = self.__getoptcmd()
        # try to get opts
        try:
            opts, args = getopt.getopt(argv, optcmd)
        except getopt.GetoptError:
            self.__usage_func()
            sys.exit(-1)
        # get opt
        optlist = self.__getoptList()
        keys = self.__optMap.keys()
        paramMap = {}
        for opt, arg in opts:
            index = optlist.index(opt)
            paramMap[self.__optMap[keys[index]]] = arg
        return paramMap


    def __getoptcmd(self):
        "get option cmd through optMap"

        keys = self.__optMap.keys()
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


class FileLineWrapper:

    def __init__(self, path, symbol):
        self.__path = path
        self.__symbol = symbol

    def generate(self):
        lineList = []
        fh = FileHelper(self.__path)
        fh.open()

        s = self.__symbol;
        line = fh.readline()
        while line:
            lineList.append(line)
            line = fh.readline()
        return  lineList
