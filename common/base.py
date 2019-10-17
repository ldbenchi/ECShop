from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
"""打开浏览器"""
def open_browser(browser='chrome'): # 默认打开谷歌浏览器
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser =='firefox':
        driver = webdriver.Firefox()
    elif browser =='ie':
        driver = webdriver.Ie()
    else:
        print("请使用正确的浏览器打开，如：Chrome，Firefox，Ie")
    driver.maximize_window() # 窗口最大化
    return driver

"""封装selenium的基本操作方法"""
class Base:
    # 实例化
    def __init__(self,driver):
        self.driver = driver
    # 打开网址
    def open_url(self,url):
        self.driver.get(url)

    # 时间等待
    @staticmethod
    def time_sleep(time=3): # 赋值3秒
        sleep(time)
    # 后退
    def back(self):
        self.driver.bcak()
    # 刷新
    def refresh(self):
        self.driver.refresh()
    # 隐式等待
    def implicitly_wait(self,time=6):
        self.driver.implicitly_wait()

    # 获取定位元素的属性值
    def get_attribute(self,locator,attribute):
        self.driver.find_element(locator).get_attribute(attribute)

    def get_tag_text(self,locator):
        try:
            text = self.driver.find_element(locator).text
            return text
        except:
            print("标签没有text值")
    # 定位单个元素，如果定位到元素返回元素，否则返回false
    def find_element(self,locator,timeout=8):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except:
            print(f'元素未找到 -> {locator} ')
            return False
        else:
            return element
    # 定位一组元素（多个），如果定位到元素返回元素（list），否则返回False
    def finde_elements(self,locator,timeout=8):
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            print(f'元素未找到 -> {locator}')
            return False
        else:
            return elements
    # 下拉框通过index选择元素
    def selector_by_index(self,locator,index):
        selector = Select(self.find_element(locator)) # 实例化Select
        # 定位元素
        try:
            selector.select_by_index(index)
        except:
            print('下拉框元素未找到')

    # 下拉框通过value选择元素
    def selector_by_value(self,locator,value):
        selector = Select(self.find_element(locator))
        try:
            selector.select_by_value(value)
        except:
            print("下拉框元素未找到")
    # 下拉滚动条
    def scroll(self,to):
        try:
            js = f'window.scrollTo(0,{to})' # 下拉滚动到to(给的参数的位置)
                                          # window.scrollTo(0,0) 上拉到页面顶端0,0位置
            self.driver.execute_script(js)
        except:
            print('下拉滚动条失败')
    # 点击元素(单个)
    def click_element(self,locator,timeout=10):
        element = self.find_element(locator, timeout)
        try:
            element.click()
        except:
            pass
    # 点击元素（一组）多个
    def click_elements(self,locator,timeout):
        elements = self.finde_elements(locator, timeout)
        elements = [i for i in elements]
        for x in elements:
            x.click()
            sleep(3)
            self.back()
            self.refresh()
            sleep(2)

    # 点击单个checkbox
    def click_one_checkbox(self,locator,timeout = 10):
        try:
            element = self.find_element(locator, timeout)
            result = element.is_selected()  # 是否被选中
            if result:
                pass
            else:
                element.click()
        except Exception as e:
            return e
    # 在文本框中输入
    def send_keys(self,locator,text,timeout=10):
        element = self.find_element(locator, timeout)
        try:
            element.clear()
            element.send_keys(text)
        except:
            pass
    # 判断text文本是否为一致
    def is_check_text_element(self,locator,text,timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_elementl(locator, text))
        except:
            print(f'元素没有找到 -> {locator}')
            return False
        else:
            return result
    # 检查元素属性value值和传入的text是否一致
    def check_value_in_element(self,locator,text,timeout=10):
        try:
           result = WebDriverWait(self.driver,timeout).until\
                (EC.text_to_be_present_in_element_value(locator,text))
        except:
            print(f'元素没有找到 -> {locator}')
            return False
        else:
            return result
    # 通过id和name属性进入frame
    def to_frame(self,id_or_name):
        try:
            self.driver.switch_to.frame(id_or_name)
        except:
            print(f'元素未找到 -> {id_or_name}')
    # 通过定位frame标签的方式进入frame
    def to_frame_by_other_attribute(self,locator):
        try:
            self.driver.switch_to.frame(self.find_element(locator,timeout=10))
        except:
            """
                因为调用find_element方法,已经对未找到元素进行异常捕获
                所以在这里如果switch_to.frame发生异常则不显示,避免重复捕获异常
            """
            pass
    # 返回上级frame
    def exit_to_seed_frame(self):
        self.driver.switch_to.parent_frame()
    # 返回最外层frame
    def exit_to_default_frame(self):
        self.driver.switch_to.default_content()
    # 关闭当前窗口
    def close_present_browser(self):
        self.driver.close()
    # 关闭所有窗口
    def close_browser(self):
        self.driver.quit()
