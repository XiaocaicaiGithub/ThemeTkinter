from urllib.request import urlretrieve
from inspect import getfile
from os.path import join

def InstallDepend():
    CurrentPath = getfile(InstallDepend)
    CurrentPath = '\\'.join(CurrentPath.split('\\')[0:-1])
    urlretrieve()
