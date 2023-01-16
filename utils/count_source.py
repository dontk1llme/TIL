from collections import Counter
from datetime import datetime
import os
import re


def count_problem_source_code():
    problem_solve_code_list = []

    directory_list = [directory for directory in os.listdir("./") if "[" in directory]

    for directory in directory_list:
        code_list = os.listdir(f"./{directory}")

        problem_solve_code_list += code_list

    name_list = [re.findall(r'\[[^)]*\]', code_name) for code_name in problem_solve_code_list]

    name_list = [name[0].replace("[", "").replace("]", "") for name in name_list if len(name) > 0]

    total_code_num = len(name_list)
    
    code_cnt_info = sorted(Counter(name_list).items(), key=lambda x: -x[1])

    return total_code_num, code_cnt_info


def make_count_info(total_code_num, code_cnt_info):
    count_info = f"#### 현재까지 풀어본 총 문제 수 : {total_code_num}개\n"

    for name in code_cnt_info:
        temp = f"- {name[0]} - {name[1]}개\n"
        count_info += temp

    return count_info 


def make_read_me(count_info):
    return f"""## TIL + CODING TEST PRACTICE!
### Since 2023.01.16
#### Python3
{count_info}
#### 아래의 페이지에서 제공하는 문제들로 구성되어 있습니다.
[BaekJoon](https://www.acmicpc.net/)  
[Programmers](https://programmers.co.kr/)  
[Samsung_SW_Academy](https://swexpertacademy.com/main/main.do)  
"""


def update_readme_md():
    total_code_num, code_cnt_info = count_problem_source_code()

    count_info = make_count_info(total_code_num=total_code_num, code_cnt_info=code_cnt_info)

    readme = make_read_me(count_info=count_info)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
