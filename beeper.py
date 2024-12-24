import os

frequency = 2500 # Adjust frequency for desired pitch (Hz)
duration = 1000 # Adjust duration for beep length (milliseconds)

def beep():
    os.system(f"beep -f {frequency} -l {duration}")