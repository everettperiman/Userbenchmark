import os.path
import time

"server_response"

file_path_results = "C:\\Users\\evere\\AppData\\Local\\Temp\\UserBenchMarkTemp\\rawresults.dat"
file_path_server = "C:\\Users\\evere\\AppData\\Local\\Temp\\UserBenchMarkTemp\\server_response"

file_path = file_path_server
final_path = "C:\\Users\\evere\\Downloads\\data.txt"

while not os.path.exists(file_path):
    time.sleep(0)

if os.path.isfile(file_path):
    os.rename(file_path,final_path)
else:
    raise ValueError("%s isn't a file!" % file_path)