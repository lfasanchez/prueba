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

import numpy as np
import string
import pmt
import struct
from gnuradio import gr
from gnuradio import digital

Size=0

class Std_Dev_PMT(gr.sync_block):
    """
    docstring for block Std_Dev_PMT
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="Std_Dev_PMT",
            in_sig=[],
            out_sig=[])
	self.message_port_register_in(pmt.intern("in"))
	self.message_port_register_out(pmt.intern("out"))
	self.set_msg_handler(pmt.intern("in"), self.StdDev)  #Funcion que se activa cuando llega el PMT



    def StdDev(self,msg_pmt):
		# veficcación del formato PMT
	if pmt.is_blob(msg_pmt):
		blob = msg_pmt
		#print "is blob"
	elif pmt.is_pair(msg_pmt):
		blob = pmt.cdr(msg_pmt)

	else:
		print "Formato desconocido" 
		return

	vec =pmt.cdr(msg_pmt) #se toma del diccionario en formato pmt la llave
	#print "sin convertir",vec,vec.__class__
        vecp=pmt.to_python(vec) #se convierte de pmt a vector en python
        self.d_Std=np.array(vecp) # se crea una variable que se pueda mmanipular
	Std1 = np.std(self.d_Std) # se calcula la desviación estandar del vector que llego
	#print (self.d_Std)
	#print (Std1)
	Std12 = float(Std1)
	#print (Std12)
	#Stdv = pmt.from_float(Std12) #se convierte a float el valor obtenido
	Stdv1 = pmt.make_f32vector(1, Std12) # se crea un vector de tipo PMT para despues ser interpretado por el  bloque PDU to Tagged Stream; debe ser "1" en el primer argumento o no funciona.
	self.message_port_pub(pmt.intern("out"), pmt.cons( pmt.PMT_NIL, Stdv1)); #se envia el PMT en vector por el puerto de salida





