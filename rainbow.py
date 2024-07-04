#!/OwO/
# depends - neopixel.py ( blaz-r's ) lib
#     e.g.: mpremote fs cp neopixel.py :neopixel.py 


from neopixel import Neopixel
import array, time
pixels = Neopixel(32, 0, 0, "GRB")
# ----------------------------- #
step = 5

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
while 1==1:
   for qx in range(0,8,1):
      if colq > colzlen:
         colq = 0
      col=colz[colq]
      for qy in range(0,4,1):
         pixid = (qy * 8) + qx
         pixels[pixid]  = (col)
         pixels.show()
      time.sleep_ms(step)
      #for qy in range(0,4,1):
      #   pixid = (qy * 8) + qx
      #   pixels[pixid]  = (0,0,0)
      #   pixels.show()
      colq = colq + 1

print("UwU")