# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Envolvente Compleja PM
# Author: Estudiantes UIS
# Copyright: UIS
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class EnvolventeComplejaPM(gr.hier_block2):
    def __init__(self, Ac=100e-3, kp=1):
        gr.hier_block2.__init__(
            self, "Envolvente Compleja PM ",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ac = Ac
        self.kp = kp

        ##################################################
        # Blocks
        ##################################################
        self.blocks_transcendental_1 = blocks.transcendental('sin', "float")
        self.blocks_transcendental_0 = blocks.transcendental('cos', "float")
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(Ac)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(kp)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_transcendental_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_transcendental_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self, 0))
        self.connect((self.blocks_transcendental_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_transcendental_1, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_Ac(self):
        return self.Ac

    def set_Ac(self, Ac):
        self.Ac = Ac
        self.blocks_multiply_const_vxx_1.set_k(self.Ac)

    def get_kp(self):
        return self.kp

    def set_kp(self, kp):
        self.kp = kp
        self.blocks_multiply_const_vxx_0.set_k(self.kp)

