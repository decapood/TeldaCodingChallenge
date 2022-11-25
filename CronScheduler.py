import multiprocessing
# import schedule
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


def add_process(running_processes, file_name, frequency, expected_runtime, logger, job_id):
    job_thread = multiprocessing.Process(target=schedule_call, args=(
        file_name, frequency, expected_runtime, logger))
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
    file_name = str(input(
        "Please state the name of the script you want to run OR STOP_ID to stop a running job: "))
    if file_name.split('_')[0] == "STOP":
        running_processes[file_name.split('_')[1]].terminate()
        Loggers[file_name.split('_')[1]].info("Terminated!")
        return
    job_id = str(input("Please enter a unique job_id: "))
    expected_runtime = int(
        input("Please enter the expected runtime of the job: "))
    frequency = int(input("Please input the frequency in seconds: "))
    logger = Create_Log(job_id)
    add_process(running_processes, file_name, frequency,
                expected_runtime, logger, job_id)
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


# # Schedule a process with the required intervals
def schedule_call(file_name, frequency, expected_runtime, logger):
    while 1:
        logger.info("Job initialized!")
        tok = time.time()
        process = subprocess.Popen(f"exec python3 {file_name}", shell=True)
        start_timer(time.time(), expected_runtime, process, logger)
        time_taken = time.time() - tok
        if not process.poll() is None:
            time_taken = time.time() - tok
            logger.info(f"Job done in {time.time()-tok} seconds!")
        if frequency > expected_runtime:
            time.sleep(frequency-time_taken)

# a parallel job that calculates and terminates the time estimated to run the job
def start_timer(bef_time, time_limit, process, logger):
    while 1:
        if (time.time() - bef_time) > time_limit and (process.poll() is None):
            process.kill()
            logger.info("Time Limit exceeded!")
            # print("job terminated")
            return
        elif process.poll() is not None:
            return

if __name__ == '__main__':
    while 1:
        run_threaded()
