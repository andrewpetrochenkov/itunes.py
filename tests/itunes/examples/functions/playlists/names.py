#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itunes
import mac_only

names = itunes.playlists.names()
print(names)
