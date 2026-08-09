import shutil
import os
import datetime
def backup_file(source, destination):
    today= datetime.date.today()
    backup_path =os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_path.replace('.tar.gz', ' '), 'gztar', source)
source="C:\\Users\\singh\\OneDrive\\Documents\\DEVOPS\\pthon"
destination="C:\\Users\\singh\\OneDrive\\Documents\\DEVOPS\\pthon\\backup"
backup_file(source, destination)