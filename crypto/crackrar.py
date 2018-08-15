import subprocess
from subprocess import call


i = 0
with open( "../../../../resources/data/rockyou.txt", "r" ) as f:
    for line in f:
        i += 1
	
	#call(["unrar", "e", "-p" + line[:-1], "important.rar"],stdout=subprocess.PIPE)
	proc = subprocess.Popen(["unrar", "e", "-p" + line[:-1], "important.rar"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	err = proc.stderr.read()
	if not "Checksum error" in err:
            print("WORDLIST", line[:-1])
            output = proc.stdout.read()
            print(output)
            break
