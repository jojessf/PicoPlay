#!/OwO/
# depends - neopixel.py ( blaz-r's ) lib
#     e.g.: mpremote fs cp neopixel.py :neopixel.py 

# mpremote fs cp neopixel.py :neopixel.py
# mpremote fs cp pixldac.py :main.py

import array, time
from math import*
from machine import ADC, Pin
from neopixel import Neopixel

# ----------------------------- #
# INTERFACES                    #
# ----------------------------- #
adc2  = ADC(Pin(28))               # ADC2 - Pin34 / GP28 / 
pixels = Neopixel(32, 0, 0, "GRB") # we're using pin1 / GP0 ~ 

# ----------------------------- #
# CONSTANTS
# ----------------------------- #
# step          - ms to sleep between cycles 
# normalDepth   - number of cycles to record for "oscilloscope" normalizer
step          = const(1)
normalDepth   = const(6)
# ----------------------------- #
# yrange - number of pixels (y)
# xrange - number of pixels (x)
yrange   = const(4)  # array pixel q (y) 
xrange   = const(8)  # array pixel q (x)
# ----------------------------- #


lastDIN = [0,0,0,0,0]



# - color table --------------- #
hi=2 # 0-255
lo=1 # 0-255
colz = (
   (hi,0,0) , # red 
   (hi,lo,0), # orn 
   (hi,hi,0), # yel
   # (lo,hi,0), # lig 
   (0,hi,0) , # grn 
   # (0,hi,lo), # grb
   (0,hi,hi), # cyn 
   # (0,lo,hi), # ind
   (0,0,hi) , # blu 
   (lo,0,hi), # vio 
   (hi,0,hi), # mag
   (hi,0,lo)  # mrd
)
colzlen = len(colz) - 1

# ----------------------------- #
colq=0

colxr = [5,9]

loopq=0


stats = {}
for s in range( 0,4,1 ): 
   stats[s] = 0


while 1==1:
   for qx in range(0,8,1):
      loopq = loopq + 1
      if loopq >= 9:
         loopq = 0
      
      # - col 
      if colq > colzlen:
         colq = colq - colzlen - 1
         colq = 0
      col=colz[colq]
      
      # pic color for column ~ alt pixel colors per col
      ci=0
      while ci < len(colxr):
        colxr[ci] = colxr[ci] + 1 
        if colxr[ci] > colzlen:
          colxr[ci] = colxr[ci] - colzlen - 1
        ci += 1
        #print("colq:"+str(colq)+", colx:"+str(colxr[ci]))
      
      # rainbow marquee 
      for qy in range(0,yrange,1):
         pixid = (qy * 8) + qx
         pixels[pixid]  = (col)
         pixels.show()
      
      # -  DAC analog-to-digital ----- #
      a2d = adc2.read_u16()
      a2d = int(a2d/1024)
      lastDIN.append(a2d)
      DINl = len(lastDIN);
      DIMSUM = 0
      LATHI  = 0
      if DINl > normalDepth:
         clrDIN = lastDIN.pop(0);
         DINl -= 1
      for z in range(0,DINl,1):
         DIMSUM = DIMSUM + lastDIN[z]
         if lastDIN[z] > LATHI:
            LATHI = lastDIN[z]
      DIMSUM = int(DIMSUM / DINl)
      LATVI = LATHI - DIMSUM
      LATVI = LATVI -1 # without diode 
      # print(LATVI)
      if LATVI < 0:
         LATVI = 0
      if LATVI >= yrange:
         LATVI = 3
      mewpt = 3 - LATVI
      # -  DAC analog-to-digital ----- #
            
      mewxid = (mewpt * 8 ) + qx
      pixels[mewxid]  = (5,5,5)
      pixels.show()
      
      # sleepy time ~ 
      time.sleep_ms(step)
      colq = colq + 1

print("UwU")