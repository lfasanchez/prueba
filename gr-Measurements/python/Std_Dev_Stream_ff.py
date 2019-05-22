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

import numpy, cmath, os
from gnuradio import gr
from operator import itemgetter
#vec=numpy.empty(4)

class Std_Dev_Stream_ff(gr.sync_block):
    """
    docstring for block Std_Dev_Stream_ff
    """
    def __init__(self, Size):
        self.Size=Size
        gr.sync_block.__init__(self,
            name="Std_Dev_Stream_ff", in_sig=["float32"], out_sig=["float32"])


    def set_Size(self,new_val):
        self.Size = new_val
        self.vec = [None] * self.Size

    def work(self, input_items, output_items):
        p = 0
	self.set_Size(self.Size)
        in0 = input_items[0]
        out = output_items[0]

        while p < self.Size:
	    #print (self.vec[p])	
            self.vec[p] = input_items[0][p]
            p = p + 1
	#print (self.vec[0])
	p = 0
        out[:]=numpy.std(self.vec)
        return p

