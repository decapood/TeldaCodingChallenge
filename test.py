import subprocess
import time
if __name__ == "__main__":
    subprocess.Popen(["notify-send","Drink!"])
    for i in range(5):
        time.sleep(1)