import tm1637

import time

from datetime import datetime

from time import sleep

 

# Define the CLK and DIO pins

CLK = 4 # GPIO pin for the clock (CLK)

DIO = 5 # GPIO pin for the data (DIO)

 

# Initialize the display

display = tm1637.TM1637(clk=CLK, dio=DIO)

 

# Set brightness (optional, range 0-7)

display.brightness(7)

 

def display_time():

    while True:

        # Get current time

        now = datetime.now()

        # Extract hours and minutes

        hour = now.hour

        minute = now.minute

        # Display time in HH:MM format

        display.numbers(hour, minute)

        

        # Wait for a minute before updating again

        time.sleep(60)

 

# Start displaying the time

display_time()
