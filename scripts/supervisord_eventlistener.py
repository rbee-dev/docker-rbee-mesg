import sys
import os
import signal

def write_stdout(s):
    # only eventlistener protocol messages may be sent to stdout
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()

def main():
    while 1:
        # transition from ACKNOWLEDGED to READY
        write_stdout('READY\n')

        # read header line and print it to stderr
        line = sys.stdin.readline()
        write_stderr(line)

        # read event payload and print it to stderr
        #headers = dict([ x.split(':') for x in line.split() ])
        #data = sys.stdin.read(int(headers['len']))
        #write_stderr(data)
	
	selfkill = os.environ['RBEE_AUTOKILL']
	if selfkill == 'true':
		write_stderr('FATAL: Unable to start service, giving up, taking the rest with me\n')
		os.kill(1, signal.SIGINT);
	else:
		write_stderr('WARNING: Unable to start service, but was instructed to keep running anyway\n')
	
	

        # transition from READY to ACKNOWLEDGED
        write_stdout('RESULT 2\nOK')

if __name__ == '__main__':
    main()