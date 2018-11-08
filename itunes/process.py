#!/usr/bin/env python
import os
import public
import itunes


@public.add
def activate():
    itunes.tell('activate')


@public.add
def kill():
    os.popen("kill %s &> /dev/null" % pid())


@public.add
def pid():
    for l in os.popen("ps -ax").read().splitlines():
        if "/Applications/iTunes.app" in l and "iTunesHelper" not in l:
            return int(list(filter(None, l.split(" ")))[0])


@public.add
def quit():
    itunes.tell("quit")
