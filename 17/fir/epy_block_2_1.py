"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block

    def __init__(self, filter_taps=[0.25, 0.25, 0.25, 0.25]):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Custom FIR filter',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        
        self.filter_taps = filter_taps
        self.N = len(filter_taps)
        self.set_history(self.N)
        
        #Example: The comand set_history(N) appends the first N-1 previous items 
        #to the input buffer (input_items), while the N'th item is the current value. 
        #E.g. if N=4:
        #input_items[0][3] is the beginning of the current input stream.
        #input_items[0][2] is one input older than the current input stream.
        #input_items[0][1] is one input older than input_items[0][2]
        #input_items[0][0] is one input older than input_items[0][1]

    def work(self, input_items, output_items):
        
        #print("length of input vector =" + str(len(input_items[0])))
        #print("length of output vector ="+ str(len(output_items[0])))
        
        for i in range(0, len(output_items[0])):
            output_items[0][i] = 0
            for j in range(0, self.N):
                output_items[0][i] = output_items[0][i] + input_items[0][i + self.N - 1 - j] * self.filter_taps[j]
                 
        return len(output_items[0])
