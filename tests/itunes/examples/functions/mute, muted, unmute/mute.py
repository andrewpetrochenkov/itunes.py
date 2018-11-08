#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itunes
import mac_only

itunes.mute()
print("muted: %s" % itunes.muted())
