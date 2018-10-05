#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import applescript


@public
def tell(code):
    return applescript.tell.app("iTunes", code)._raise().out
