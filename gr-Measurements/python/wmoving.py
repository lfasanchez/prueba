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


import numpy, cmath, os
from gnuradio import gr
from operator import itemgetter

class wmoving(gr.sync_block):
    """
    weighted moving average
    """

    def __init__(self, alpha=0.5, samples=False):
        """
        Create the block
        Args:
        alpha: the weight of new information (vs the weight ov the average)
            avg = ( alpha * new ) + ( (1 - alpha) * avg )
        samples:
            alpha = (samples * (samples+1.0))/2.0
            avg = ( alpha * new ) + ( (1 - alpha) * avg )
        If both alpha and samples are given as arguments, samples overrides whatever
        is set for alpha.
        """

        if samples:
            self.set_samples(samples)

        else:
            self.set_alpha(alpha)

        self._first = True

        gr.sync_block.__init__(self, "wmoving_average", ["float32"], ["float32"])

    def set_alpha(self,alpha):
        self._alpha = numpy.float128(alpha) # promote some greater precision by invoking numpy with a big width
        self._beta  = (1 - alpha)

    def set_samples(self,samples):
        self.set_alpha( numpy.float128(2) / (1 + samples) )

    def work(self, input_items, output_items):
        p = 0

        if self._first and len(input_items[0]):
            self._avg = input_items[0][p]
            output_items[0][p] = self._avg
            p = 1
            self._first = False;

        while p < len(input_items[0]):
            self._avg = self._alpha * input_items[0][p] + self._beta * self._avg
            output_items[0][p] = self._avg
            p = p + 1

        if os.getenv("DEBUG_WMA"):
            os.write(2, "alpha=%f; avg=%f\n" % (self._alpha, self._avg))

        return p

