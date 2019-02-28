#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itunes

itunes.volume.change(10)
print("volume: %s" % itunes.volume.get())

itunes.volume.change(0)
print("volume: %s" % itunes.volume.get())
