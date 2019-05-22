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
from Amp_Dist_Zero_py_cf import Amp_Dist_Zero_py_cf

class qa_Amp_Dist_Zero_py_cf (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
	src_data = (1+0.5j,0.5-0.5j);
	#ex_data = (3,3);
	src = blocks.vector_source_c (src_data);
	med = Amp_Dist_Zero_py_cf(); 
	snk = blocks.vector_sink_f ();
	self.tb.connect (src, med);
	self.tb.connect (med, snk);
	self.tb.run ();
	result_data = snk.data();
	#self.assertFloatTuplesAlmostEqual (ex_data, result_data, 1)
	print "result",result_data;
        # check data

if __name__ == '__main__':
    gr_unittest.run(qa_Amp_Dist_Zero_py_cf, "qa_Amp_Dist_Zero_py_cf.xml")
