import os #importing a library into the code
import datetime
def run_command(command):
    print(os.system(command))
def get_current_time():
    print(datetime.datetime.now())
run_command("systeminfo") 
run_command("df -h")
get_current_time()