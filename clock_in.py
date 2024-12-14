import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import service
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 使用Chrome浏览器
def Use_Chrome():
    try:
        start_options = ChromeOptions()
        start_options.use_chromium = True
        start_options.add_argument('--headless')  # 隐藏浏览器窗口
        browser = webdriver.Chrome(options=start_options)
        return browser
    except:
        return None


# 使用Edge浏览器
def Use_Edge():
    try:
        start_options = EdgeOptions()
        start_options.use_chromium = True
        start_options.add_argument('--headless')  # 隐藏浏览器窗口
        browser = webdriver.Edge(options=start_options)
        return browser
    except:
        return None


# 关闭腾讯文档客户端请求
def Close_TXWD(browser):
    print('\nClose_TXWD: ',end='')
    try:
        element = browser.find_element(by=By.XPATH,value="//div[contains(text(), '忽略')]")
        element.click()
        print('successful')
    except:
        print('failed')

# QQ登录
def QQ_login(browser):
    print('QQ_login: ',end='')
    try:        # 点击QQ登录
        element = browser.find_element(by=By.XPATH,value='//span[contains(text(),"QQ登录")]')
        element.click()
        print('successful')
        
    except:
        print('failed')

# 服务协议 和 隐私政策
def Accept_the_agreement1(browser):
    print('Accept_the_agreement1: ', end='')
    try:        # 点击同意
        element = browser.find_element(by=By.XPATH,value='//div[contains(text(),"同意")]')
        element.click()
        print('successful')
    except:
        print('failed')
    

# 我已阅读并接受腾讯文档的 服务协议 和 隐私政策
def Accept_the_agreement2(browser):
    print('Accept_the_agreement2: ',end='')
    try:        # 未勾选"接受协议", 则将其勾选
        element = browser.find_element(by=By.XPATH,value='//div[@class="dui-checkbox dui-checkbox-normal dui-checkbox-tick" and @data-dui-1-10-0="dui-checkbox dui-checkbox-normal dui-checkbox-tick"]//div[contains(text(),"我已阅读并接受腾讯文档的")]')
        element.click()
        print('succesful')
    except:
        print('failed')

# 下次自动登录
def Automatically_log_in_next_time(browser):
    print('Automatically_log_in_next_time: ',end='')
    try:        # 未勾选"下次自动登录", 则将其勾选
        element = browser.find_element(by=By.XPATH,value='//div[@class="dui-checkbox dui-checkbox-normal dui-checkbox-tick" and @data-dui-1-10-0="dui-checkbox dui-checkbox-normal dui-checkbox-tick"]//div[contains(text(),"下次自动登录")]')
        element.click()
        print('successful')
    except:
        print('failed')

# 点击头像登录
def Click_avatar_to_login(browser):
    iframe1 = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//iframe')))
    browser.switch_to.frame(iframe1)

    iframe2 = browser.find_element(by=By.XPATH,value='//iframe')
    browser.switch_to.frame(iframe2)
    print('Avatar:  ', end='')
    try:
        # <span id="img_out_xxxxxx" uin="xxxxxx" type="4" class="img_out_focus"></span>
        element = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//span[contains(@id,'img_out_') and @uin and @class='img_out_focus']")))
        element.click()
        print('successful')
        time.sleep(4)
        
    except:
        print('failed')
    browser.switch_to.parent_frame()
    browser.switch_to.parent_frame()
    # browser.switch_to.default_content()


# 登录
def Log_in(browser):
    try:        # 未登录,则登录
        login_button = browser.find_element(by=By.XPATH,value='//div[contains(text(), "登录腾讯文档")]')
        login_button.click()

        QQ_login(browser)
        Accept_the_agreement1(browser)
        Accept_the_agreement2(browser)
        Automatically_log_in_next_time(browser)
        Click_avatar_to_login(browser)

    except:
        pass

# 再填一份
def Fill_out_another(browser):
    print('Fill_out_another: ',end='')
    try:
        element = browser.find_element(by=By.XPATH,value="//div[contains(text(), '再填一份')]")
        element.click()
        print('successful')
        time.sleep(2)
    except:
        print('failed')

# 是否定位成功
def locate_successful(browser):
    try:
        element = browser.find_element(by=By.XPATH,value="//div[contains(text(), '删除')]")
        return True
    except:
        return False

# 定位
def locate(browser):
    cnt = 5
    while not locate_successful(browser) and cnt:
        cnt -= 1
        try:
            locate_button = browser.find_element(by=By.XPATH,value="//div[contains(text(), '获取定位') or contains(text(), '重新定位')]")
            locate_button.click()
            time.sleep(2)
        except:
            continue


def Fill_out_the_form(browser):
    print('Fill_out_the_form2: ',end='')
    try:
        file = open('./data.txt','r',encoding='utf-8')
        lines=file.readlines()
        file.close()

        textareas = WebDriverWait(browser,5).until(EC.presence_of_all_elements_located((By.XPATH,"//textarea[@placeholder='请输入']")))
        # 姓名
        textareas[0].send_keys(lines[0])
        # 学号
        textareas[1].send_keys(lines[1])
        # 定位
        locate(browser)

        print('successful')
    except:
        print('failed')

# 提交
def Submit(browser):
    print('Submit: ',end='')
    try:
        element1 = browser.find_element(by=By.XPATH,value="//button[@type='button' and contains(text(),'提交')]")
        element1.click()

        element2 = browser.find_element(by=By.XPATH,value="//div[@class='dui-button-container' and @data-dui-1-9-1='dui-button-container' and contains(text(), '确认')]")
        element2.click()
        print('successful')
        return True
    except:
        print('failed')
        return False



# 自动打卡
def Auto():
    browser = Use_Chrome() if Use_Chrome() != None else Use_Edge()
    if browser == None:
        print('No browser available')
        return
    browser.implicitly_wait(2)  # 隐式等待2s

    # 要写全, 不能写短网址
    url1 = 'https://docs.qq.com/form/page/DQldIUWVYVGVjUnpZ#/fill'      # 每日晚归打卡(test)
    url = 'https://docs.qq.com/form/page/DZkxiVGJCTkpVTHlq?_t=1728998772250&u=46aa43b6e8ac46d2bef7e827a2a63231#/fill'   # 每日晚归打卡
    browser.set_window_rect(950, 0, 950, 2100)
    browser.get(url1)

    Close_TXWD(browser)
    Log_in(browser)
    Fill_out_another(browser)
    Fill_out_the_form(browser)
    if not Submit(browser):
        time.sleep(6000)
        raise subprocess.CalledProcessError

    # time.sleep(6000)
    browser.close()


if __name__ == '__main__':
    Auto()
