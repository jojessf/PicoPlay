# UwU
import array, time
from machine import ADC, Pin

# YE: 
# * pico H 34 /GP28/ADC2  => 1k ohm => DAC {L}
# * pico H 33  ===========> DAC {GND}
 
# adc31 = ADC(Pin(26))
# adc32 = ADC(Pin(27))
adc34 = ADC(Pin(28))

lastDIN = [0,0,0,0,0]

stats = {0:0,1:0,2:0,3:0}


while True:
    # print("31/BCK:"+str(adc31.read_u16())+",    32/LCK:"+str(adc32.read_u16())+",    \t34/DIN:"+str(adc34.read_u16()) )
    
    a2d = adc34.read_u16()
    a2d = int(a2d/1024)
    
    lastDIN.append(a2d)
    DINl = len(lastDIN);
    DIMSUM = 0
    LATHI  = 0
    if DINl > 24:
      clrDIN = lastDIN.pop(0);
      DINl -= 1
    for z in range(0,DINl,1):
      DIMSUM = DIMSUM + lastDIN[z]
      if lastDIN[z] > LATHI:
         LATHI = lastDIN[z]
    DIMSUM = int(DIMSUM / DINl)
    LATVI = LATHI - DIMSUM
    LATVI = LATVI - 3  # without diode 
    if LATVI < 0:
      LATVI = 0
    if LATVI >= 4:
      LATVI = 3

    stats[LATVI]+=1
    print("a")
    print(stats)
    # print(LATVI)
    time.sleep_ms(25)
    
    
    # print("DIN:"+str(a2d))
    # print("DIN:"+str(a2d) + ", DimSum:" + str(DIMSUM))
    # print("DimSum:" + str(DIMSUM))
    # print("DimSum:" + str(DIMSUM) + ", LATHI:" + str(LATHI))
    # print("DimSum:" + str(DIMSUM) + ", LATHI:" + str(LATHI) + ", LATVI:" + str(LATVI))
    # print("LATVI:" + str(LATVI))
    # NAH: * pico H 31  => 1k ohm => DAC {BCK}
    # NAH: * pico H 32  => 1k ohm => DAC {LCK}
    # NAH: * pico H 34  => 1k ohm => DAC {DIN}  # I2C is kinda a pain to sniff, relies on shared CLK between primary/replica
