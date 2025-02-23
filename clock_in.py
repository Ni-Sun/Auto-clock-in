import time
import subprocess
import logger
import logging
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

from selenium.common.exceptions import WebDriverException

def init_logger():
    level = logging.INFO
    log = logger.get_logger()
    return log

log = init_logger()


def Use_Chrome():
    """使用 Chrome 浏览器（改进版）"""
    try:
        options = ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')

        # 使用 Selenium Manager 自动管理驱动
        service = webdriver.ChromeService()
        browser = webdriver.Chrome(
            service=service,
            options=options
        )
        return browser
    except WebDriverException as e:
        log.error(f"Chrome 启动失败: {str(e)}")
        return None


def Use_Edge():
    """使用 Edge 浏览器（改进版）"""
    try:
        options = EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')

        # 使用 Selenium Manager 自动管理驱动
        service = webdriver.EdgeService()
        browser = webdriver.Edge(
            service=service,
            options=options
        )
        return browser
    except WebDriverException as e:
        log.error(f"Edge 启动失败: {str(e)}")
        return None

# 关闭腾讯文档客户端请求
def Close_TXWD(browser):
    try:
        element = browser.find_element(by=By.XPATH,value="//div[contains(text(), '忽略')]")
        element.click()
        log.info('Close_TXWD: successful')
    except:
        log.error('Close_TXWD: failed')

# QQ登录
def QQ_login(browser):
    try:
        element = browser.find_element(by=By.XPATH, value='//span[contains(text(),"QQ登录")]')
        element.click()
        log.info('QQ_login: successful')
    except:
        log.error('QQ_login: failed')

# 服务协议 和 隐私政策
def Accept_the_agreement1(browser):
    try:
        element = browser.find_element(by=By.XPATH, value='//div[contains(text(),"同意")]')
        element.click()
        log.info('Accept_the_agreement1: successful')
    except:
        log.error('Accept_the_agreement1: failed')

# 我已阅读并接受腾讯文档的 服务协议 和 隐私政策
def Accept_the_agreement2(browser):
    try:
        element = browser.find_element(by=By.XPATH, value='//div[@class="dui-checkbox dui-checkbox-normal dui-checkbox-tick" and @data-dui-1-10-0="dui-checkbox dui-checkbox-normal dui-checkbox-tick"]//div[contains(text(),"我已阅读并接受腾讯文档的")]')
        element.click()
        log.info('Accept_the_agreement2: successful')
    except:
        log.error('Accept_the_agreement2: failed')

# 下次自动登录
def Automatically_log_in_next_time(browser):
    try:
        element = browser.find_element(by=By.XPATH, value='//div[@class="dui-checkbox dui-checkbox-normal dui-checkbox-tick" and @data-dui-1-10-0="dui-checkbox dui-checkbox-normal dui-checkbox-tick"]//div[contains(text(),"下次自动登录")]')
        element.click()
        log.info('Automatically_log_in_next_time: successful')
    except:
        log.error('Automatically_log_in_next_time: failed')

# 点击头像登录
def Click_avatar_to_login(browser):
    try:
        iframe1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe')))
        browser.switch_to.frame(iframe1)

        iframe2 = browser.find_element(by=By.XPATH, value='//iframe')
        browser.switch_to.frame(iframe2)

        cnt = 2
        flag = False
        while cnt and not flag:
            cnt -= 1
            try:
                element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@id,'img_out_') and @uin and @class='img_out_focus']")))
                element.click()
                time.sleep(4)
                flag = Check_login_successful(browser)
            except:
                continue

        browser.switch_to.parent_frame()
        browser.switch_to.parent_frame()
        if flag:
            log.info('Click_avatar_to_login: successful')
        else:
            log.error('Click_avatar_to_login: failed')
    except:
        log.error('Click_avatar_to_login: failed')


# 检查是否登录成功
def Check_login_successful(browser):
    flag = True
    try:
        element = browser.find_element(by=By.XPATH,value="//span[contains(@id,'img_out_') and @uin and @class='img_out_focus']")
        flag = False
    except:
        pass

    try:
        element = browser.find_element(by=By.XPATH,value="//div[contains(text(),'快捷登录')]")
        flag = False
    except:
        pass

    return flag

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

# 再填一份(测试用)
def Fill_out_another(browser):
    try:
        element = browser.find_element(by=By.XPATH,value="//div[contains(text(), '再填一份')]")
        element.click()
        log.info('Fill_out_another: successful')
        time.sleep(2)
    except:
        log.error('Fill_out_another: failed')

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

        log.info('Fill_out_the_form: successful')
    except:
        log.error('Fill_out_the_form: failed')

# 提交
def Submit(browser):
    try:
        element1 = browser.find_element(by=By.XPATH,value="//button[@type='button' and contains(text(),'提交')]")
        element1.click()

        element2 = browser.find_element(by=By.XPATH,value="//div[@class='dui-button-container' and contains(text(), '确认')]")
        element2.click()
        log.info('Submit: successful')
        return True
    except:
        log.error('Submit: failed')
        return False



# 自动打卡, 参数为打卡网址
def Auto(url):
    browser = None
    try:
        if browser == None:
            browser = Use_Chrome()
        if browser == None:
            browser = Use_Edge()

        if browser == None:
            log.error('No browser available')
            return

        browser.implicitly_wait(2)  # 隐式等待2s
        browser.set_window_rect(500, 0, 800, 900)
        browser.get(url)

        Close_TXWD(browser)
        Log_in(browser)
        Fill_out_another(browser)
        Fill_out_the_form(browser)
        if not Submit(browser):
            # time.sleep(6000)
            raise subprocess.CalledProcessError

    except subprocess.CalledProcessError as se:
        log.error(f"关键操作失败: {str(se)}")
        # raise  # 重新抛出给上层处理
    except Exception as e:
        log.error(f"运行时异常: {str(e)}")
        # raise
    finally:
        if browser:
            browser.close()


if __name__ == '__main__':
    # 要写全, 不能写短网址
    url1 = 'https://docs.qq.com/form/page/DQldIUWVYVGVjUnpZ'  # 每日晚归打卡 Su
    url2 = 'https://docs.qq.com/form/page/DQnJha1RkamNCSHNX'  # 每日晚归打卡 YourSun
    Auto(url2)
