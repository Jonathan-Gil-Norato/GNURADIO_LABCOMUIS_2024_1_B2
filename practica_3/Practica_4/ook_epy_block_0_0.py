import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """Este bloque esta recibiendo dos parametros iniciales de valor flotante de 32 bits; la siguiente parte del bloque describe la funcion de trabajo que recibe los valores determinados anteriormente y entrega la envolvente compleja:"""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(output_items[0])
