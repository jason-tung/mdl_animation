from script import run
import sys
import subprocess

if len(sys.argv) == 2:

    subprocess.Popen(["rm", "-rf", "anim"])
    run(sys.argv[1])
elif len(sys.argv) == 1:
    run(raw_input("please enter the filename of an mdl script file: \n"))
else:
    print "Too many arguments."
