"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, fc = 100e3, fm_dev=25e3, fs = 200e3):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Custom FM Modulator',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.fm_dev = fm_dev
        self.fc = fc
        self.fs = fs
        self.phase = 0

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        
        sig_len = len(input_items[0])
        
        df = input_items[0] * self.fm_dev
        f = df + self.fc
        
        for i in range(0, sig_len):
            self.phase = self.phase + 2*np.pi*f[i]/self.fs
            output_items[0][i] = np.cos(self.phase)
        
        return len(output_items[0])
