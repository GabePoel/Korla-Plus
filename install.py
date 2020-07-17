import os
import sys

home = os.path.expanduser("~")
insdir = os.getcwd()
tardir = os.path.join(home, ".local", "share", "icons")

def link(name):
    #if not os.path.exists(os.path.join(tardir, name)):
        #os.makedirs(os.path.join(tardir, name))
    os.system("ln -sf '" + os.path.join(insdir, name) + "' " + tardir)

def move(name):
    os.system("mvdir '" + os.path.join(insdir, name) + "' " + tardir)
    
themes = ["korla-plus", "korla-plus-light", "korla-plus-light-panel", "korla-plus-pgrey"]

if len(sys.argv) == 1:
    raise ValueError("No input provided.\nPlease specify either 'link' or 'move'.")
for theme in themes:
    if sys.argv[1] == "link":
    	if not os.path.exists(tardir):
            os.mkdir(tardir)
        link(theme)
    elif sys.argv[1] == "move":
        if not os.path.exists(tardir):
            os.mkdir(tardir)
        move(theme)
    else:
        raise ValueError("Invalid input provided.\nPlease specify either 'link' or 'move'.")
