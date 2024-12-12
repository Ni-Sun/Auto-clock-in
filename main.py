import subprocess

lines=[]
flag = False
try:
    file = open('./data.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    #  第一行为姓名, 第二行为学号(10位)
    if len(lines) >= 2 and len(lines[0]) >= 2 and len(lines[1]) == 10:
        flag = True

except Exception as FileNotFoundError:
    print('error: File Not Found')

if not flag:
    # 输入信息
    print('姓名:')
    name = input()

    id=''
    valid = False
    while not valid:
        valid = True
        print('\n学号:')
        id = input()
        if len(id) != 10:
            valid = False
            print('学号长度为10位!!')
        for ch in id:
            if not ch.isdigit():
                valid = False
                print('学号全部都是数字!!')
                break

    file = open('./data.txt', 'w', encoding='utf-8')
    file.write(name + '\n')
    file.write(id)
    file.close()

try:
    subprocess.run(['./clock_in.exe'], check=True)
    print('自动打卡成功')
except:
    print('自动打卡失败')