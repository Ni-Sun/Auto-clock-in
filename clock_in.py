import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


start_options = EdgeOptions()
start_options.use_chromium = True
start_options.add_argument('--headless')  # 隐藏浏览器窗口
browser = webdriver.Edge(options=start_options)
browser.implicitly_wait(2)      # 隐式等待2s


# QQ登录
def QQ_login():
    print('QQ_login: ',end='')
    try:        # 点击QQ登录
        # QQ登录
        xpath = '/html/body/div[14]/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/ul/li[2]'
        element = browser.find_element(by=By.XPATH,value=xpath)
        element.click()
        print('successful')
        
    except:
        print('failed')

# 服务协议 和 隐私政策
def Accept_the_agreement1():
    print('Accept_the_agreement1: ', end='')
    try:        # 点击同意
        xpath = '/html/body/div[17]/div/div[4]/button[2]'
        element = browser.find_element(by=By.XPATH,value=xpath)
        element.click()
        print('successful')
    except:
        print('failed')
    

# 我已阅读并接受腾讯文档的 服务协议 和 隐私政策
def Accept_the_agreement2():
    print('Accept_the_agreement2: ',end='')
    try:        # 未勾选"接受协议", 则将其勾选
        xpath = '/html/body/div[14]/div[3]/div/div[2]/div[2]/div/div[2]//div[@class="dui-checkbox dui-checkbox-normal dui-checkbox-tick" and @data-dui-1-9-1="dui-checkbox dui-checkbox-normal dui-checkbox-tick"]'
        element = browser.find_element(by=By.XPATH,value=xpath)
        element.click()
        print('succesful')
    except:
        print('failed')

# 下次自动登录
def Automatically_log_in_next_time():
    print('Automatically_log_in_next_time: ',end='')
    try:        # 未勾选"下次自动登录", 则将其勾选
        xpath = '/html/body/div[14]/div[3]/div/div[2]/div[2]/div/div[3]//div[class="dui-checkbox dui-checkbox-normal dui-checkbox-tick" and @data-dui-1-9-1="dui-checkbox dui-checkbox-normal dui-checkbox-tick"]'
        element = browser.find_element(by=By.XPATH,value=xpath)
        element.click()
        print('successful')
    except:
        print('failed')

# 点击头像登录
def Click_avatar_to_login():
    # iframe1 = browser.find_element(by=By.XPATH,value='/html/body/div[14]/div[3]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/iframe')
    iframe1 = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[14]/div[3]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/iframe")))
    browser.switch_to.frame(iframe1)

    iframe2 = browser.find_element(by=By.XPATH,value='/html/body/div[2]/div[1]/div/iframe')
    browser.switch_to.frame(iframe2)
    print('Avatar:  ', end='')
    try:
        xpath = '/html/body/div[1]/div[4]/div[8]/div/a/span[4]'
        element = browser.find_element(by=By.XPATH,value=xpath)
        element.click()
        print('successful')
        
    except:
        print('failed')
    browser.switch_to.parent_frame()
    browser.switch_to.parent_frame()
    # browser.switch_to.default_content()


# 登录
def Log_in():
    try:        # 未登录,则登录
        print()
        login_button = browser.find_element(by=By.CLASS_NAME,value='dui-button-container')
        login_button.click()

        QQ_login()
        Accept_the_agreement1()
        Accept_the_agreement2()
        Automatically_log_in_next_time()
        Click_avatar_to_login()

        print('Log in: successful')

    except:
        print('Log in: failed')


# 是否定位成功
def locate_successful():
    try:
        element = browser.find_element(by=By.XPATH,value="//div[contains(text(), '删除')]")
        return True
    except:
        return False

# 定位
def locate():
    cnt = 5
    while not locate_successful() and cnt:
        cnt -= 1
        try:
            # 获取定位/正在定位/重新定位
            locate_button = browser.find_element(by=By.XPATH,value="/html/body/div[9]/div/div[3]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]")
            locate_button.click()
            time.sleep(2)
        except:
            continue



def Fill_out_the_form():
    print('Fill_out_the_form2: ',end='')
    try:
        file = open('./data.txt','r',encoding='utf-8')
        lines=file.readlines()
        file.close()

        # 姓名
        element1 = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[9]/div/div[3]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div/textarea")))
        element1.send_keys(lines[0])

        # 学号
        element2 = browser.find_element(by=By.XPATH,value="/html/body/div[9]/div/div[3]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div/textarea")
        element2.send_keys(lines[1])

        # 定位
        locate()

        print('successful')
    except:
        print('failed')

# 提交
def Submit():
    print('Submit: ',end='')
    try:
        element1 = browser.find_element(by=By.XPATH,value="/html/body/div[9]/div/div[3]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div[1]/div[4]/button")
        element1.click()

        element2 = browser.find_element(by=By.XPATH,value="/html/body/div[17]/div/div[4]/button[2]/div")
        element2.click()
        print('successful')
        return True
    except:
        print('failed')
        return False


# 自动打卡
def Auto():
    # 要写全, 不能写短网址
    # url1 = 'https://docs.qq.com/form/page/DQldIUWVYVGVjUnpZ#/fill'
    url = 'https://docs.qq.com/form/page/DZkxiVGJCTkpVTHlq?_t=1728998772250&u=46aa43b6e8ac46d2bef7e827a2a63231#/fill'

    # browser.set_window_rect(950, 0, 950, 2100)
    browser.get(url)

    Log_in()
    Fill_out_the_form()
    if not Submit():
        raise subprocess.CalledProcessError

# 手动操作
def Manual():
    time.sleep(6000)

Auto()
# Manual()

browser.close()