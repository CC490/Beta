import platform as _platform
import subprocess
import pip, pipenv


#class Project_Install() :

def git(*args):
   return subprocess.check_call(['git'] + list(args))
   

name = _platform.system()
    
    
if name == "Windows" :

   print("win sys")
   git("fetch")
   git("checkout master")
   pip.install(pipenv)
   pip.main(['uninstall', 'virtualenv'])
   pip("uninstall pipenv")
   pip("install pipenv")
   pipenv("sync")
   pipenv("shell")
   pipenv("install --dev")
   git ("add .")
   git("commit -m 'saving environment state.'")
   exit
      
      
elif name == "Darwin" :

   print("MAC sys")
      
      


elif name == "Linux" :

   print("Linux sys")

      


else :
   print("Unknown platform; perform manual installation.")