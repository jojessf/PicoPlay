#!/OwO/
# depends - neopixel.py ( blaz-r's ) lib
#     e.g.: mpremote fs cp neopixel.py :neopixel.py 

# mpremote fs cp neopixel.py :neopixel.py
# mpremote fs cp rainbowsin.py :main.py

from neopixel import Neopixel
import array, time
from math import*
pixels = Neopixel(32, 0, 0, "GRB")
# ----------------------------- #

step     = const(15)
sinrange = const(4)  # array pixel q (y) 
xrange   = const(8)  # array pixel q (x)
ConFs    = const(8000)
ConF     = const(500)

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

# stats = {-2:0,-1:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0 }
stats = {}
for s in range( -5,9,1 ): 
   stats[s] = 0
print(stats)

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
      
      for qy in range(0,sinrange,1):
         pixid = (qy * 8) + qx
         pixels[pixid]  = (col)
         pixels.show()
      
      # placeholder : create a sign wave that dances over our rainbow marquee
      sinful = qx + loopq
      if sinful >= 8:
         sinful = 0
      # mewp is just the y level for the sin wave~ 
      mewpt = 0
      mewp   = int(sin(3*pi*ConF*sinful/ConFs)*(sinrange)/2)+1  # [0-4] 
      mewpt  = int((sin(3*pi*ConF*sinful/ConFs)+1)*(sinrange)/2)+0  # [0-4] 
            
      # stats[mewpt] = stats[mewpt] + 1
      # print(stats)
      mewxid = (mewpt * 8 ) + qx
      pixels[mewxid]  = (5,5,5)
      pixels.show()
      # print("qx:"+str(qx)+", sinful:"+str(sinful)+", mewp:"+str(mewp)+", mewpt:"+str(mewpt))
      
      # sleepy time ~ 
      time.sleep_ms(step)
      colq = colq + 1

print("UwU")