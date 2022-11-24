from CronScheduler import *
import subprocess
import os.path


def test_Create_log():
    Create_Log("1")
    assert os.path.isfile(f'./1.log')

def test_process_creation():
    Processes = {}
    job_id = "1"
    function_name_ = function_1
    frequency = 2
    logger = Create_Log(job_id)
    file_name_ = False
    add_process(Processes,function_name_, frequency, logger,file_name_,job_id)
    assert list(Processes.keys()).__contains__(job_id)
    assert Processes[job_id].is_alive()

def test_logger_creation():
    Loggers = {}
    job_id = "1"
    logger = Create_Log(job_id)
    add_logger(Loggers,logger,job_id)
    assert list(Loggers.keys()).__contains__(job_id)
    assert os.path.isfile(f'./{job_id}.log')