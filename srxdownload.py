import serial
import fdpexpect
import sys

# You may need to change this 
ser = serial.Serial('/dev/tty.usbserial-00001004', 9600, timeout=1)

PASSWORD='cat'

#ser.write("\n")
#print ser
#print ser.readline()

fh = fdpexpect.fdspawn(ser)
fh.logfile = sys.stdout

fh.sendline("root")
fh.expect("Password:")
fh.sendline(PASSWORD)
fh.expect("%")
fh.sendline("cli")
fh.expect(">")
fh.sendline("set cli screen-length 0")
fh.expect(">")
fh.sendline("show config")
fh.expect("root@")

cfg = open("srx-output.config","w")
cfg.write(fh.before)
cfg.close()

fh.sendline("exit")
fh.expect("%")
fh.sendline("exit")


#fh.interact()
