"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
import math
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, fm_dev=25e3, Fs = 200e3):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Custom FM Demodulator',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.float32]
        )
        self.fm_dev = fm_dev
        self.Fs = Fs
        self.last_angle = 0

    def work(self, input_items, output_items):    
        for i in range(0, len(input_items[0])):
            angle = np.angle(input_items[0][i])
            angle_change = angle - self.last_angle
            if angle_change > math.pi:
                angle_change -= 2 * math.pi
            elif angle_change < -math.pi:
                angle_change += 2 * math.pi
            self.last_angle = angle
            output_items[0][i] = angle_change * self.Fs / (2 * math.pi * self.fm_dev)
        
        return len(output_items[0])
