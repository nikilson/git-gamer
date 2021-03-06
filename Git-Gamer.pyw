import os
from os import path
from datetime import datetime
import subprocess
# Checking the default location
# add remote location

home = (path.expanduser("~"))
git_gamer_location = path.join(home, "GitGamer")
current_cwd = os.getcwd()

#hide console
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
""" passing starttupinfo=si argument into subprocess.call function"""
if not (path.isdir(git_gamer_location)):
    os.mkdir(git_gamer_location)
    os.chdir(git_gamer_location)
    subprocess.call('git init -b "main"', startupinfo=si)
    os.chdir(current_cwd)
    with open("git-repo-url.txt", 'r') as url_file:
        remote_url = url_file.readline()
        os.chdir(git_gamer_location)
        subprocess.call(f"git remote add origin {remote_url}", startupinfo=si)
        os.chdir(current_cwd)
        url_file.close()
else:
    os.chdir(git_gamer_location)
    subprocess.call("git pull origin", startupinfo=si)
    os.chdir(current_cwd)
# read location file
def remove_lines(list_path):
    output_list = []
    for line in list_path:
        if "\n" in line:
            line = line.replace('\n', '')
        output_list.append(line)
    return output_list

save_location_file = open("save-location.txt", 'r')

game_name_file = open("game-name.txt", 'r')

save_location_list = save_location_file.readlines()

game_name_list = game_name_file.readlines()

save_location_list = remove_lines(save_location_list)

game_name_list = remove_lines(game_name_list)

for num1 in range(len(save_location_list)):
    temp_loc = save_location_list[num1]
    temp_name = game_name_list[num1]
    temp_path = path.join(git_gamer_location, temp_name)
    if not (path.isdir(temp_path)):
        os.mkdir(temp_path)
    temp_loc = temp_loc + "\\*.*"
    # print(f'copy "{temp_loc}" "{temp_path}"')
    subprocess.call(f'del /Q /S /F "{temp_path}" | cls', shell=True , startupinfo=si)
    subprocess.call(f'xcopy /S /Q /F /Y "{temp_loc}" "{temp_path}"', startupinfo=si)

os.chdir(git_gamer_location)
subprocess.call("git add .", startupinfo=si)

date_time = datetime.now().strftime("%D%M%Y%H%M%S")

subprocess.call(f"git commit -m '{date_time}'", startupinfo=si)
subprocess.call("git push -u origin main", startupinfo=si)