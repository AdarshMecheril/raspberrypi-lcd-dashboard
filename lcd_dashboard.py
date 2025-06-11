import os
import time
from RPLCD.i2c import CharLCD

# Change to your LCD's address from i2cdetect
lcd = CharLCD('PCF8574', 0x3f)  # Or 0x27

def get_ip():
    ip = os.popen("hostname -I").read().split()[0]
    return ip

def get_cpu_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "").strip()

def get_ram_usage():
    mem = os.popen("free -m").readlines()[1].split()
    used = mem[2]
    total = mem[1]
    return f"{used}/{total} MB"

try:
    while True:
        lcd.clear()
        lcd.write_string("IP: " + get_ip())
        time.sleep(3)

        lcd.clear()
        lcd.write_string("CPU Temp: " + get_cpu_temp())
        time.sleep(3)

        lcd.clear()
        lcd.write_string("RAM Used:")
        lcd.cursor_pos = (1, 0)
        lcd.write_string(get_ram_usage())
        time.sleep(3)

except KeyboardInterrupt:
    lcd.clear()
    print("Dashboard stopped.")
