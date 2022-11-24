import multiprocessing
import schedule
import time
import subprocess
import os
import logging

# To save processes loggers/identifiers by ID
running_processes = {}
Loggers = {}


# calling an implemented script
def call_file(file_path, logger):
    tok = time.time()
    subprocess.run(f"python3 {os.getcwd()}/{file_path}", shell=True)
    tik = time.time()
    logger.info(
        f"Function called successfuly! \nFunction execution time is {tik-tok} seconds")
    return


# sample function
def function_1(logger):
    logger.info("Drink water!")
    return


# sample function
def function_2(logger):
    logger.info("Drink juice!")
    return


# adding the process along with the id
def add_process(running_processes, function_name_, frequency, logger, file_name_, job_id):
    if file_name_:
        job_thread = multiprocessing.Process(target=schedule_job, args=(
            function_name_, frequency, job_id, logger), kwargs=dict(params=file_name_))
    else:
        job_thread = multiprocessing.Process(
            target=schedule_job, args=(function_name_, frequency, job_id, logger))
    job_thread.start()
    running_processes[job_id] = job_thread
    return


# adding and linking the logger to the process ID
def add_logger(Loggers, logger, job_id):
    logger = Create_Log(job_id)
    Loggers[job_id] = logger
    return


# Main cli tool
def run_threaded():
    function_name_ = str(input(
        "Please state the name of the method/call_file to run a specific script/STOP_JOBID to terminate a job: "))
    file_name_ = False
    if function_name_.split('_')[0] == "STOP":
        running_processes[function_name_.split('_')[1]].terminate()
        Loggers[function_name_.split('_')[1]].info("Terminated!")
        return
    if function_name_ == 'call_file':
        file_name_ = str(input("Please enter the file path: "))
    job_id = str(input("Please enter a unique job_id: "))
    frequency = int(input("Please input the frequency in seconds: "))
    logger = Create_Log(job_id)
    add_process(running_processes, function_name_,
                frequency, logger, file_name_, job_id)
    add_logger(Loggers, logger, job_id)
    return running_processes, Loggers


# Main Log creation
def Create_Log(job_id):
    logger = logging.getLogger(f"{job_id}")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler = logging.FileHandler(f'{job_id}.log', mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


# Schedule a process with the required intervals
def schedule_job(function_name, interval, job_id, logger, params=False):
    if params:
        schedule.every(interval).seconds.do(
            functions[function_name], params, logger)
    else:
        schedule.every(interval).seconds.do(functions[function_name], logger)
    while 1:
        schedule.run_pending()
        time.sleep(1)
    return


functions = {
    "function_1": function_1,
    "function_2": function_2,
    "call_file": call_file
}


if __name__ == '__main__':
    while 1:
        run_threaded()
