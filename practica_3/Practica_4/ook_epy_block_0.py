import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """Este bloque toma una fuente aleatoria con un filtrado interpolado recibiendo dos parametros iniciales fc y samp_rate junto con un bloque con un valor constante iniciado en 0; la siguiente parte del bloque describe la funcion de trabajo que recibe los valores determinados anteriormente y entrega una señal modulada en fase y en cuadratura:"""

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])


