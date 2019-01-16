### Script to run docker containers

>1 . Add docker commands to file docker_cmds.txt

Example 
```bash
$ cat docker_cmds.txt 
docker run --rm -d --name mondo-dev mongo
docker run --rm -d --name rabbit-dev rabbitmq
```

>2 . Run script docker_manager.py

Supports Python version 2 and 3 
```bash
$ python docker_manager.py
```
Or
```bash
$ python3 docker_manager.py
```

>3 . Check status of container
```bash
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                                NAMES
0bb91cc50355        rabbitmq            "docker-entrypoint.s…"   About a minute ago   Up About a minute   4369/tcp, 5671-5672/tcp, 25672/tcp   rabbit-dev
9d5bad616224        mongo               "docker-entrypoint.s…"   About a minute ago   Up About a minute   27017/tcp 
```

>4 . To run it on system boot append it to ~/.bashrc 
```bash
/usr/bin/python $abs_path/docker_api/docker_manager.py
```

>5 . Logs are generated on file docker_run.log 


-----------------------------------------------------


Note:

1) --rm flag is necessary as it might fail to run container with exited status