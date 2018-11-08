#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itunes
import mac_only

itunes.unmute()
print("muted: %s" % itunes.muted())
