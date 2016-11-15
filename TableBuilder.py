#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt, sqlite3
from fangUtil import *

optcmd = "hd:c:"

def usage():
    print 'usage:\r\ntest.py -d <database> -c <sqlcmdfile>'

def doworking(opts):
    db_path = ''
    sql_cmd = ''
    for opt,arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-d':
            db_path = arg
        elif opt == '-c':
            sql_cmd = arg
    # working
    conn = sqlite3.connect(db_path)
    sql_cmd = getSqlCmd(sql_cmd)
    conn.execute(sql_cmd)
    conn.commit()
    conn.close()


def getSqlCmd(filepath):
    sqlcmd = ''
    fh = FileHelper(filepath)
    try:
        fh.open()
        line = fh.readline()
        while line:
            sqlcmd += line;
            line = fh.readline()
    finally:
        fh.close()
    return sqlcmd

if __name__ == '__main__':
    ch = CmdHelper2(usage, doworking, optcmd)
    ch.dowork(sys.argv[1:])