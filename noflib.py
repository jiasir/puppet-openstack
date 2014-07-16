#!/usr/bin/env python

import os
import subprocess


def execute_get_output(*command):
    """Execute and return stdout."""
    devnull = open(os.devnull, 'w')
    command = map(str, command)
    proc = subprocess.Popen(command, close_fds=True,
                            stdout=subprocess.PIPE, stderr=devnull)
    devnull.close()
    stdout = proc.communicate()[0]
    return stdout.strip()


def execute(*command):
    """Execute without returning stdout."""
    devnull = open(os.devnull, 'w')
    command = map(str, command)
    subprocess.call(command, close_fds=True, stdout=devnull, stderr=devnull)
    devnull.close()