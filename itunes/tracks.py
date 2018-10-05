#!/usr/bin/env python
from public import public
import itunes


@public
def play(track, playlist):
    itunes.tell('play track "%s" of playlist "%s"' % (track, playlist))
