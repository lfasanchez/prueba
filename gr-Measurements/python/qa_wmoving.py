#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 xxx.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from wmoving import wmoving
from gnuradio import analog
from math import cos,sin

import  cmath, os, time

class qa_wmoving (gr_unittest.TestCase):
    two_pi = cmath.pi * 2
    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def _get_output(self, input, alpha):
        inv = blocks.vector_source_f(input)
        avg = wmoving(alpha=alpha)
        ouv = blocks.vector_sink_f()

        self.tb.connect(inv, avg)
        self.tb.connect(avg, ouv)
        self.tb.run()

        return ouv.data()
    def test_001_t (self):
        inp = [15,7,0,9,0,1,0,1,0,1]
        output = self._get_output(input=inp, alpha=0.5)

        if os.getenv("DEBUG_WMA"):
            os.write(2, "%s\n%s\n" % (inp, output))

        x=inp[0]
        for (i,v) in enumerate(inp):
            x = 0.5*x + 0.5*v
            self.assertAlmostEqual(output[i], x, delta=0.0001)

if __name__ == '__main__':
    x = os.getenv("TEST_PREFIX")

    if not x:
        x = "test_"

    gr_unittest.TestLoader.testMethodPrefix = x
    gr_unittest.main ()
