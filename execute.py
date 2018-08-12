import subprocess as sub
import os
 
def execute(command, directory):
    # change to the directory in which you want to execute the command.
    os.chdir(directory)
    p = sub.Popen(command, universal_newlines=True, stdout = sub.PIPE, stderr = sub.PIPE)
    output, errors = p.communicate()
    
    os.chdir('.')	
    return output, errors