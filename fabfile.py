from __future__ import with_statement

__author__ = 'cason'

from fabric.api import *

env.hosts = ['localhost']

cmd = local


def hello(who="world"):
    print "Hello {who}!".format(who=who)
    # cmd("mkdir test");
    print cmd("uptime")
    print cmd("hostname")
    result = cmd("ls -l /")
    print result.failed
    # print sudo("ls /")
    # local("rmdir test")


def myHide():
    with hide('running', "stdout"):
        with lcd("~/src"):
            result = local("pwd")
            print "the output of pwd: %s" % result

    print "Now no hiding"
    with lcd("~"):
        # print local("pwd")
        local("pwd")


def myGet():
    with hide():
        get(remote_path="/Users/cason/src/python/server.pem", local_path="./server2.pem")
        local("ls server2.pem")
        # download file from remote server


def myPut():
    put("server2.pem", "/Users/cason/src/python/server3.pem")


def myPrompt():
    # Prompt the user
    port_number = prompt("Which port would you like to use?")
    print port_number
    # Prompt the user with defaults and validation
    port_number = prompt("Which port would you like to use this time:?", default=42, validate=int)
    print port_number


    #
    # # Create a directory (i.e. folder)
    # run("mkdir /tmp/trunk/")
    #
    # # Uptime
    # run("uptime")
    #
    # # Hostname
    # run("hostname")
    #
    # # Capture the output of "ls" command
    # result = run("ls -l /var/www")
    #
    # # Check if command failed
    # result.failed
