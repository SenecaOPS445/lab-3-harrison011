#!/usr/bin/env python3

# Author ID: hiruthayathas

import subprocess

def free_space():
    free = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    oput = free.communicate()
    stdout = oput[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())
