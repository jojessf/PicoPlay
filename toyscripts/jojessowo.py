#!/OwO/
# depends - neopixel.py ( blaz-r's ) lib
#     e.g.: mpremote fs cp neopixel.py :neopixel.py 
from neopixel import Neopixel
import array, time
pixels = Neopixel(32, 0, 0, "GRB")


pixels[0:32] = (0,0,0)        # <- all off 

pixels[0:4] = (1,0,0)
pixels[4:8] = (0,1,0)
pixels[8:12] = (0,0,1)
pixels[12:16] = (1,1,0)
pixels[16:20] = (0,1,1)
pixels[20:24] = (1,0,1)
pixels[24:28] = (2,1,0)
pixels[28:32] = (0,1,2)

pixels.show()
time.sleep_ms(100)

pixels[0:32] = (0,0,0)        # <- all off 
pixels.show()


for loop in range (0,10240,1):

   ## [dot] snakin it
   step=5
   lastpixid=0
   for qy in range(0,8,1):
      for qx in range(0,8,1):
         e = 0
         px=qx
         py=qy
         if qy > 3:
            py = 7 - qy
         if qy%2==1: 
            e = 1 
            px=8-qx-1
         pixid = (py * 8) + px
         # print("qx:"+str(qx)+", qy:"+str(qy)+", px:"+str(px)+", pixid:"+str(pixid)+", e:"+str(e));
         pixels[lastpixid]  = (1,0,1)
         pixels.show()
         time.sleep_ms(step)
         pixels[pixid]  = (8,0,4)
         pixels.show()
         time.sleep_ms(step)
         pixels[lastpixid]  = (0,0,0)
         pixels.show()
         time.sleep_ms(step)
         pixels[pixid]  = (0,0,0)
         pixels.show()
         lastpixid=pixid
   
   ## dancin' dots
   step = 25
   for qx in range(0,8,1):
      for qy in range(0,8,1):
         e = 0
         px=qx
         py=qy
         if qy > 3:
            py = 7 - qy
         if qy%2==1: 
            e = 1 
            px=8-qx-1
         pixid = (py * 8) + px
         # print("qx:"+str(qx)+", qy:"+str(qy)+", px:"+str(px)+", pixid:"+str(pixid)+", e:"+str(e));
         pixels[pixid]  = (0,1,2)
         pixels.show()
         time.sleep_ms(step)
         pixels[pixid]  = (0,0,0)
         pixels.show()

   # snakin it
   step=5
   lastpixid=0
   lastPX = [0,0,0]
   lastX4 = [0,0,0]
   for qy in range(0,8,1):
      for qx in range(0,8,1):
         px=qx
         py=qy
         if qy > 3:
            py = 7 - qy
         if qy%2==1:
            px=8-qx-1
         pixid = (py * 8) + px
         
         zixid = (py * 8) + px
         lastPX.append(pixid)
         clearpix = lastPX.pop(0);
         pixels[clearpix] = (0,0,0)
         for dpixid in lastPX:
            pixels[zixid]   = (4,2,2)  # ZZZ
            pixels[dpixid]  = (0,1,2) # tail col 
            if dpixid == pixid:
               pixels[dpixid]  = (12,0,1) # head col 
            pixels.show()
            time.sleep_ms(step)
            pixels[zixid]   = (0,0,0)  # ZZZ


print("UwU")