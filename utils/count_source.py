from collections import Counter
from datetime import datetime
import os


def count_files():
    files_info = []
    total_file_count = 0
    directory_list = [directory for directory in os.listdir("./") if "[" in directory]
    for directory in directory_list:
        file_list = os.listdir(f"./{directory}")
        file_count = len(file_list)
        temp = [directory, file_count]
        files_info.append(temp)
        total_file_count += file_count
    return files_info, total_file_count
  
  
def make_info(files_info, total_file_count):
    info = f"## Files Count In Folders\nTotal File Count: {total_file_count}\n"
    for directory_files_info in files_info:
        temp = f"- {directory_files_info[0]}: {directory_files_info[1]}\n"
        info += temp
    return info
    


def make_read_me(info):
    return f"""## TIL + CODING TEST PRACTICE!
### Since 2023.01.16
#### Python3
{info}
#### 아래의 페이지에서 제공하는 문제들로 구성되어 있습니다.
[BaekJoon](https://www.acmicpc.net/)  
[Programmers](https://programmers.co.kr/)  
[Samsung_SW_Academy](https://swexpertacademy.com/main/main.do)
"""


def update_readme():
    files_info, total_file_count = count_files()
    info = make_info(files_info, total_file_count)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)