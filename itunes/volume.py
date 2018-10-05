#!/usr/bin/env python
from public import public
import itunes


@public
def get():
    if itunes.pid():
        return int(itunes.tell('sound volume'))


@public
def change(value):
    itunes.tell('set sound volume to %s' % value)
