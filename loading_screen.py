import time
import sys



def show_loading_screen(t):

    animation = "01101100"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r " + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > t:  # The animation will last for 10 seconds
            break
    sys.stdout.write("\r01110100 00101110 01101101 01100101 00101111 01110011 01100101 01110110 01100101 01101110 01100100 00110111 01110011 01100101 01110110 01100101 01101110 01100100 \n\n")
