#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from public import public
from itunes.helper import tell
import itunes.playlists
import itunes.tracks
import itunes.volume


@public
def kill():
    _pid = pid()
    if _pid:
        os.popen("kill %s" % _pid)


@public
def quit():
    tell("quit")


@public
def pid():
    for l in os.popen("ps -ax").read().splitlines():
        if "/Applications/iTunes.app" in l and "iTunesHelper" not in l:
            return int(list(filter(None, l.split(" ")))[0])


@public
def pause():
    tell("pause")


@public
def play():
    tell("play")


@public
def mute():
    tell("set mute to true")


@public
def muted():
    return "true" in tell("get mute")


@public
def unmute():
    tell("set mute to false")


@public
def stop():
    tell("stop")


@public
def next():
    tell("play next track")


@public
def prev():
    tell("play previous track")


@public
def state():
    return tell("state")
