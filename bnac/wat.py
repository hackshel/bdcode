import threading
import time
import os
import subprocess


def get_process( process_name ):
    cmd = 'ps -ef |grep '+ process_name +' | grep -v "grep" '
    p = subprocess.Popen( cmd , stdout=subprocess.PIPE, stderr=subprocess.PIPE ,shell=True)
    result = p.communicate()[0]
    #print p.returncode
    if p.returncode == 0 :
        return True
    else:
        return False


def cmd_restart( python_path ,home, cmd ,username , password ):

    #cmd = python_path +' '+home + cmd + '.py' +  ' start'
    cmd = python_path + ' '+home + cmd + '.py ' + username +' '+ password + ' >/dev/null 2>&1 &'
    p = subprocess.Popen( cmd , stdout=subprocess.PIPE, stderr=subprocess.PIPE ,shell=True)
    result = p.communicate()[0]
    if p.returncode == 0 :
        return True,cmd +' is restart ...'
    else:
        return False , cmd + ' not restart ...'

def main( ppath ,home_path, args ,username , password ):

    for arg in args:
        state = get_process( arg )
        if state == False:
            stat , msg = cmd_restart( ppath ,home_path, arg ,username ,password )
        else:
            stat , msg = True, 'nothing to do ...'
    return stat , msg

if __name__ == "__main__":

    home_path = '/usr/local/bnac/'

    python_path = '/usr/bin/python2.7'

    cmds = [ 'bnac' ]

    stat , msg = main( python_path , home_path , cmds ,'wangxiaochen02' , 'ithelp@123!')

    print msg
