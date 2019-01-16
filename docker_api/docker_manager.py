#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import subprocess, shlex


logging.basicConfig(filename='docker_run.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

docker_cmds_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docker_cmds.txt")


def read_file():
    with open(docker_cmds_path, 'r') as fp:
        return fp.readlines()


def execute_cli(command):
    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    try:
        stdout, stderr = p.communicate()
        return p.returncode, stdout, stderr
    except Exception as e:
        raise e
    finally:
        try:
            p.kill()
        except Exception:
            pass


def main():

    docker_cmds = read_file()

    for cmd in docker_cmds:
        _, stdout, stderr = execute_cli(cmd)
        logging.info(stdout)
        logging.debug(stderr)


if __name__ == '__main__':
    main()
