#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
from itunes.helper import tell
from itunes.process import activate, kill, pid, quit
import itunes.playlists
import itunes.tracks
import itunes.volume


@public.add
def pause():
    tell("pause")


@public.add
def play():
    tell("play")


@public.add
def mute():
    tell("set mute to true")


@public.add
def muted():
    return "true" in tell("get mute").out


@public.add
def unmute():
    tell("set mute to false")


@public.add
def stop():
    tell("stop")


@public.add
def next():
    tell("play next track")


@public.add
def prev():
    tell("play previous track")


@public.add
def state():
    return tell("state")
