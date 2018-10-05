#!/usr/bin/env python
from public import public
import itunes


@public
def names():
    return itunes.tell('get name of playlists').split(", ")


@public
def play(playlist_name):
    return itunes.tell('play playlist named "%s"' % playlist_name)
