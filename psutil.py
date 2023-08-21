import psutil
import time

print(psutil.cpu_times())

while True:
    print(psutil.cpu_times())

    time.sleep(5)
