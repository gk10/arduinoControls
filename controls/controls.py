import pyfirmata
import time
import keyboard



board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

val = 0
tempVal = 0
maxRange = 1000
minRange = 0

while True:
    
    analog_value = analog_input.read()
    val = 0
    if analog_value is None:
        print("is null")
        
    else:
        val = analog_value
        print("not null")
        if val > 0.5:
            print("GREATER")
            keyboard.press_and_release('a')
         
       # keyboard.press_and_release('q')
    

    print(val)
    
    # if float(val) > float(tempVal+2):
    #     print("test")
    time.sleep(0.1)
    tempVal = val
