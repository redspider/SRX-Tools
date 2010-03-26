import serial
import fdpexpect
import sys

ser = serial.Serial('/dev/tty.usbserial-00001004', 9600, timeout=1)
PASSWORD='cat'

#ser.write("\n")
#print ser
#print ser.readline()

fh = fdpexpect.fdspawn(ser)
fh.logfile = sys.stdout

fh.sendline("root")
opt = fh.expect(["%","Password:"])
if opt != 0:
    fh.sendline(PASSWORD)
fh.expect("%")
fh.sendline("cat <<__EOF__ >upload_config.cfg;")
for l in open(sys.argv[1],"r"):
    fh.expect("\?")
    fh.sendline(l.rstrip().replace("$","\$"))

fh.expect("\?")
fh.sendline("__EOF__")
fh.expect("%")
fh.sendline("cli")
fh.expect(">")
fh.sendline("set cli screen-length 0")
fh.expect(">")
fh.sendline("configure")
fh.expect("#")
fh.sendline("load override upload_config.cfg")
fh.expect("#")
fh.sendline("commit")
fh.expect("#")
fh.sendline("exit")
fh.expect(">")
fh.sendline("exit")
fh.expect("%")
fh.sendline("exit")

#fh.interact()
