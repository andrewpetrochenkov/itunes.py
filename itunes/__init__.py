#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import runcmd


def _run(args):
    return runcmd.run(["itunes"] + list(args))._raise().out

@public
def kill():
    _run(["kill"])

@public
def pid():
    out = _run(["pid"])._raise().out
    if out:
        return int(out)

@public
def pause():
    _run(["pause"])

@public
def play():
    _run(["play"])

@public
def play_track(track,playlist):
    _run(["play-track",str(track),playlist])

@public
def stop():
    _run(["stop"])

@public
def next():
    _run(["next"])

@public
def prev():
    _run(["prev"])

@public
def playlists():
    out = _run(["playlists"])
    return out.splitlines()


@public
def volume(value=None):
    args = ["volume"]
    if value:
        args.append(str(value))
    out = _run(args)
    if out:
        return int(out)


@public
def mute():
    _run(["mute"])

@public
def unmute():
    _run(["unmute"])

@public
def muted():
    return "true" in _run(["muted"])
