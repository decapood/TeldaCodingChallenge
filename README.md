# TeldaCodingChallenge

## Brief Explaination + Reasoning
    The task is to implement a functionality in which a user has to provide multiple jobs along with the ID and frequency, and to organize those tasks in a manner that all jobs are executed concurrently. So the approach and methodology was applied as follows:
        1. Shedule a simple function to run with a certain frequency. (Schedule module was used, could be implemented natively too)
        2. Allow the user to have certain implementation, in this part multiple approaches could've been used including but not restricted to:
            - opening a Nano command to let the user implement the functionality then save the file in the required format.
            - Assuming the user has an already existing functionality (python script for example), then use the subprocess module to call this file in the periodical requirements. (chosen approach) (N.B: the funcionality for now only supports python files, but in the future a dictionary with the formats can be used to call the right command for running the file).
        3. Running multiple process concurrently, here there was a choice between multiprocessing and threading libraries, I chose the multiprocessing in case the file already has parallel threads to provide better resources.
        4. Tracking the active processes by storing them in a dictionary with ID as a key in case the user wants to terminate a job, they can just type (STOP_{job_ID}).
        5. The entire code I tried to write it following the best structure I can think of to correctly have test cases that covers main functionalities.
## Usage

1. To run clone the repo in your directory
```bash					
git clone https://github.com/decapood/TeldaCodingChallenge.git
```

2. To start your first run 
```'bash
python3 CronScheduler.py
```

3. You will then be prompted to input the required function as shown below.
### Example run display
![](1.png)
### Example Log display
![](2.png)
    The above
## Possible future improvements
    a. The structure is built in a way that it can support freezing a certain process for a while, terminate, re-execute the job again but only terminate is available.
    b. Warnings and exceptions with explaination can be added to each functionality to keep better track of any future complexities.
    c. The file and code structure is not scalable as it was done as a simple functionality, in an ultimate environment you would have a file for a cron job and a seperate one for scheduling, some more in depth resource allocation depending on the program needed space/CPU usage. 
    d. There is an assumption that no job will fail, so if it fails the whole thread will stop without retrying.
