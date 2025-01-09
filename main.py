import os
import time
import clock_in
import logger
import logging
from win11toast import toast


def init_logger():
    level = logging.DEBUG
    log = logger.get_logger(level)
    return log

log = init_logger()

def main():
    lines=[]
    flag = False
    try:
        # 读取信息
        file = open('./data.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

        #  第一行为姓名, 第二行为学号(10位), 第三行为URL
        if len(lines) >= 3 and len(lines[0]) >= 2 and len(lines[1]) == 11:
            flag = True

    except Exception as FileNotFoundError:
        log.error('error: File Not Found')

    if not flag:
        # 输入信息
        log.info('姓名:')
        name = input()

        # 学号
        id=''
        valid = False
        while not valid:
            valid = True
            log.info('\n学号:')
            id = input()
            if len(id) != 10:
                valid = False
                log.warning('学号长度为10位!!')
            for ch in id:
                if not ch.isdigit():
                    valid = False
                    log.warning('学号全部都是数字!!')
                    break

        # 打卡URL
        log.info('\n打卡链接(不要输入短网址):')
        url = input()

        file = open('./data.txt', 'w', encoding='utf-8')
        file.write(name+'\n')
        file.write(id+'\n')
        file.write(url)
        file.close()

    try:
        clock_in.Auto(lines[2])
        log.info('自动打卡成功')

        icon = os.path.abspath('image/icon.ico')
        toast(
            '自动打卡成功',
            app_id = 'Auto Clock In',
            icon = icon,
        )
    except:
        log.error('自动打卡失败')
    # time.sleep(6000)

if __name__ == '__main__':
    main()