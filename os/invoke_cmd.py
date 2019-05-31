import subprocess
import sys
import locale
print(locale.getdefaultlocale())
print(sys.getdefaultencoding())


# subprocess.call(['ping', 'localhost'])
ping = subprocess.Popen(["ping",    "127.0.0.1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, error = ping.communicate()
print(out.decode('cp936').encode('utf8').decode('utf8'))


def runcmd(command):
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="cp936",timeout=9)
    if ret.returncode == 0:
        print("success:",ret)
    else:
        print("error:",ret)


runcmd(["dir","/b"])#序列参数
runcmd(["ping","qq.com"])#序列参数