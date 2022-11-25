import time
import subprocess
if __name__ == "__main__":
    while 1:
        time.sleep(3)
    subprocess.Popen(["notify-send","Eat food!"])