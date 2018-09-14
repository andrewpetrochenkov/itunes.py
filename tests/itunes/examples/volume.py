#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itunes
import tests_os.mac

itunes.volume(10)
volume = itunes.volume()
print(volume)
