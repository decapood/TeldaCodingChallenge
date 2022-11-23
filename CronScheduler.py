
# import threading
import multiprocessing
import schedule
import time
# import sys
import logging

running_threads = {}


def function_1(logger):
    logger.info("Drink water!")
    return

def function_2(logger):
    logger.info("Drink juice!")
    return

def run_threaded():
    function_name_ = str(input("Please state the name of the method or STOP_JOBID to terminate a job: "))
    if function_name_.split('_')[0] == "STOP":
        running_threads[function_name_.split('_')[1]].terminate()
        return
    job_id = str(input("Please enter a unique job_id: "))
    frequency = int(input("Please input the frequency in seconds: "))
    job_thread = multiprocessing.Process(target=schedule_job,args=(function_name_,frequency,job_id))
    job_thread.start()
    running_threads[job_id] = job_thread

def Create_Log(job_id):
    logger = logging.getLogger(f"{job_id}")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler = logging.FileHandler(f'{job_id}.log', mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def schedule_job(function_name,interval,job_id):
    logger = Create_Log(job_id)
    schedule.every(interval).seconds.do(functions[function_name],logger)
    while 1:
        schedule.run_pending()
        time.sleep(1)

functions = {
    "function_1":function_1,
    "function_2":function_2
}
# file_name = 'Function.py'

if __name__ == '__main__':
    while 1:
        run_threaded()