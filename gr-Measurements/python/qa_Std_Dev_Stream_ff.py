#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 Luis Felipe Albarracin.
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
from Std_Dev_Stream_ff import Std_Dev_Stream_ff

class qa_Std_Dev_Stream_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data1 = (10,11,12,13)
        src1 = blocks.vector_source_f (src_data1)
        Std = Std_Dev_Stream_ff(3)
        snk1 = blocks.vector_sink_f ()
        self.tb.connect (src1, (Std,0))
        self.tb.connect ((Std,0), snk1)
        self.tb.run ()
        result1_data = snk1.data ()
        #self.assertFloatTuplesAlmostEqual (expected_result1, result1_data, 6)
        #self.assertFloatTuplesAlmostEqual (expected_result2, result2_data, 6)
        print(result1_data)


if __name__ == '__main__':
    gr_unittest.run(qa_Std_Dev_Stream_ff, "qa_Std_Dev_Stream_ff.xml")
