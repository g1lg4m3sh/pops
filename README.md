# pops (Panda Ops)

Ops Task @BigPanda

## Pre-requisites

```bash
[root@localhost]# sestatus
                  SELinux status:                 disabled
[root@localhost]# docker --version
                  Docker version 1.13.1, build 8633870/1.13.1
[root@localhost]# docker-compose --version
                  docker-compose version 1.23.1, build b02f1306
[root@localhost]# git --version
                  git version 1.8.3.1
[root@localhost]# node -v
                  v6.14.3
[root@localhost]# npm -v
                  3.10.10
[root@localhost]# python3.6 -V
                  Python 3.6.6
```

The deployment script was coded using Python 3.6.6 (go.py)

`The script will:`
- Download image resources file from AWS S3 (https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz) and extract it's content to '/public/images'.
- Create, build & run the App + DB using “docker-compose build” & “docker-compose up” command.
- Check the App's health at the end of the deployment flow and will terminate itself and the containers upon anything other than HTTP response code 200.

## Instructions
- For simplicity sake, all you have to do to run it is clone this repository using git clone
```bash
[root@localhost]# git clone https://github.com/g1lg4m3sh/pops.git
Cloning into 'pops'...
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
Unpacking objects: 100% (9/9), done.
remote: Total 9 (delta 1), reused 9 (delta 1), pack-reused 0
```
- cd to cloned directory
```bash
[root@localhost]# cd pops/
```
- Run `go.py`
```bash
[root@localhost pops]# python3.6 go.py
Attemting to download pandapics.tar.gz... Please wait.
Download successful!
The current working directory is /opt/test3/pops
Successfully created the directory /opt/test3/pops/panda-ops
Cloning into 'ops-exercise'...
remote: Enumerating objects: 63, done.
remote: Total 63 (delta 0), reused 0 (delta 0), pack-reused 63
Unpacking objects: 100% (63/63), done.
Successfully cloned bigpanda ops-exercise.
Cloning into 'pops'...
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 1), reused 9 (delta 1), pack-reused 0
Unpacking objects: 100% (9/9), done.
Successfully cloned docker-compose from repository.
Successfully created images directory
Extracting pictures...
Placing fetched docker-compose.yml in place...
Executing docker-compose build...
Building db
Step 1/2 : FROM mongo
Trying to pull repository docker.io/library/mongo ...
latest: Pulling from docker.io/library/mongo
7b8b6451c85f: Pull complete
ab4d1096d9ba: Pull complete
e6797d1788ac: Pull complete
e25c5c290bde: Pull complete
45aa1a4d5e06: Pull complete
b7e29f184242: Pull complete
ad78e42605af: Pull complete
1f4ac0b92a65: Pull complete
55880275f9fb: Pull complete
bd0396c9dcef: Pull complete
28bf9db38c03: Pull complete
3e954d14ae9b: Pull complete
cd245aa9c426: Pull complete
Digest: sha256:0823cc2000223420f88b20d5e19e6bc252fa328c30d8261070e4645b02183c6a
Status: Downloaded newer image for docker.io/mongo:latest
 ---> 525bd2016729
Step 2/2 : ADD users.js /docker-entrypoint-initdb.d/
 ---> 78aedb9bd002
Removing intermediate container b681133a811e
Successfully built 78aedb9bd002
Building app
Step 1/5 : FROM node:alpine
Trying to pull repository docker.io/library/node ...
alpine: Pulling from docker.io/library/node
4fe2ade4980c: Pull complete
136604f124e7: Pull complete
13f341eda658: Pull complete
Digest: sha256:1ea975c6ba5be52074af83445658b060d82fc03bbf70b74137c3e2b5452cee4f
Status: Downloaded newer image for docker.io/node:alpine
 ---> f21b938fb1e6
Step 2/5 : ADD . /opt/app
 ---> 91424ee8cb69
Removing intermediate container f06f3bcbc3ce
Step 3/5 : WORKDIR /opt/app
 ---> 38e0b251235f
Removing intermediate container 1cd6d04ddd30
Step 4/5 : RUN npm install
 ---> Running in b3e134e0a7bf

added 124 packages from 161 contributors and audited 217 packages in 4.761s
found 3 vulnerabilities (2 low, 1 moderate)
  run `npm audit fix` to fix them, or `npm audit` for details
 ---> 2a67cde4a3c2
Removing intermediate container b3e134e0a7bf
Step 5/5 : CMD npm start
 ---> Running in 1a8eef4f0e56
 ---> dcb058e62bfc
Removing intermediate container 1a8eef4f0e56
Successfully built dcb058e62bfc
Executing docker-compose up in background...
Creating ops-exercise_db_1_203dd1d61ff0 ... done
Creating ops-exercise_app_1_97a1d2947ca9 ... done
Sleeping for 15 seconds allowing db and app to load.
Checking health response code...
Success!, response code is  200
```
Receiving the output above means the deployment was successful and the app and db containers will continue working in background.
`if encountering ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] or urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] paste the following code at the end of the import statements in go.py`

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
