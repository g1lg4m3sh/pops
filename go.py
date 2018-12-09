import urllib.request
import os
import sys
import time
import subprocess
from shutil import copyfile

def getResponseCode(url):
    conn = urllib.request.urlopen(url)
    return conn.getcode()

currpath = os.getcwd()
workspace = currpath + "/panda-ops"
panda = "git clone https://github.com/bigpandaio/ops-exercise.git"
mypanda = "git clone https://github.com/g1lg4m3sh/pops.git"
build = "docker-compose build"
up = "docker-compose up"
picsfile = "pandapics.tar.gz"
health = "http://127.0.0.1:3000/health"

print('Attemting to download pandapics.tar.gz... Please wait.')
urllib.request.urlretrieve("https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz", 'pandapics.tar.gz')

if os.path.isfile('./' + picsfile):
    print('Download successful!')
else:
    print('Download failed, aborting.')

print ("The current working directory is %s" % currpath)

try:  
    os.mkdir(workspace)
except OSError:  
    print ("Creation of the directory %s failed" % workspace)
else:  
    print ("Successfully created the directory %s " % workspace)

os.chdir(workspace)
try:
    os.system(panda)
except OSError:
    print ("Failed to clone bigpanda ops-exercise.")
else:
    print ("Successfully cloned bigpanda ops-exercise.")

try:
    os.system(mypanda)
except OSError:
    print ("Failed to clone docker-compose from repository.")
else:
    print ("Successfully cloned docker-compose from repository.")

try:
    os.mkdir(workspace + "/ops-exercise/public/images")
except OSError:
    print ("Creation of images directory failed")
else:
    print ("Successfully created images directory")

print('Extracting pictures...')
import tarfile
tar = tarfile.open(currpath + "/" + picsfile)
tar.extractall(path="./ops-exercise/public/images", members=None)
tar.close()

print('Placing fetched docker-compose.yml in place...')
copyfile('./pops/docker-compose.yml', './ops-exercise/docker-compose.yml')

os.chdir(workspace + "/ops-exercise")

print('Executing docker-compose build...')
os.system(build)

print('Executing docker-compose up in background...')
os.system(up + " -d")

print('Sleeping for 15 seconds allowing db and app to load.')
time.sleep(10)

print('Checking health response code...')
response = getResponseCode(health)

if response==200:
    print('Success!, response code is ', response)
else:
    print('Did not receive response code 200, aborting and killing containers!')
    os.system('docker-compose kill')
