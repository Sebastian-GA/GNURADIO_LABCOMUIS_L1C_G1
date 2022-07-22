# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: CalculoPotenciaComunicaciones
# Author: Sebastian-Esteban
# Copyright: Sebastian-Esteban
# GNU Radio version: 3.10.1.1

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import Modulos_L1C
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal







class Practica3_2(gr.hier_block2, Qt.QWidget):
    def __init__(self, l_vect=1024):
        gr.hier_block2.__init__(
            self, "CalculoPotenciaComunicaciones",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(0, 0, 0),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Parameters
        ##################################################
        self.l_vect = l_vect

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_number_sink_2 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_2.set_update_time(0.10)
        self.qtgui_number_sink_2.set_title("Potencia logaritmica [dBm]")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['[dBm]', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_2.set_min(i, -1)
            self.qtgui_number_sink_2.set_max(i, 1)
            self.qtgui_number_sink_2.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_2.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_2.set_label(i, labels[i])
            self.qtgui_number_sink_2.set_unit(i, units[i])
            self.qtgui_number_sink_2.set_factor(i, factor[i])

        self.qtgui_number_sink_2.enable_autoscale(False)
        self._qtgui_number_sink_2_win = sip.wrapinstance(self.qtgui_number_sink_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_2_win)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title("Potencia Lineal [W]")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['[W]', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_1.set_min(i, -1)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])

        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_1_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Potencia logaritmica [dBW]")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['[dBW]', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.fft_vxx_0 = fft.fft_vfc(1024, True, window.blackmanharris(1024), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, l_vect)
        self.blocks_nlog10_ff_1 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 30)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1/(2*135115.625))
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1024)
        self.Modulos_L1C_SumaVector_0 = Modulos_L1C.SumaVector(l_vect)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.Modulos_L1C_SumaVector_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.Modulos_L1C_SumaVector_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_number_sink_1, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_number_sink_2, 0))
        self.connect((self.blocks_nlog10_ff_1, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))


    def get_l_vect(self):
        return self.l_vect

    def set_l_vect(self, l_vect):
        self.l_vect = l_vect

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

