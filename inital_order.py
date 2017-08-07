# coding=utf-8
import win32con
import win32gui
import sys
import time
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf8')


class inital_order(object):
    @staticmethod
    def inital():
        ff = webdriver.Firefox()
        ff.get('http://192.168.31.99:7385')
        time.sleep(5)
        ff.find_element_by_xpath(".//*[@id='login-view']/table/tbody/tr[1]/td[2]/input").send_keys('18121225109')
        ff.find_element_by_xpath(".//*[@id='login-view']/table/tbody/tr[2]/td[2]/input").send_keys('123456')
        ff.find_element_by_xpath(".//*[@id='login-view']/button").click()
        ff.implicitly_wait(10)
        ff.find_element_by_xpath(".//*[@id='main-container']/div[2]/div/div/div/div[2]/div/div/a[2]").click()  # 订单设置
        time.sleep(5)
        ff.find_element_by_xpath(".//*[@id='orderBoxView-shell']/div/div[1]/div/div/a").click()  # 导入
        ff.find_element_by_xpath(".//*[@id='orderBoxView-shell']/div/div[1]/div/div/ul/li[1]/a").click()  # 普通
        time.sleep(5)
        ff.find_element_by_xpath(".//*[@id='import-dialog']/div/div/div[2]/div/label/span/span/i").click()  # 点击上传文件
        dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'E:\\test\\order\\testOrder.csv')  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        time.sleep(5)
        ff.find_element_by_xpath(".//*[@id='import-dialog']/div/div/div[1]/button").click()  # 关闭文件上传窗口
        time.sleep(5)
        ff.find_element_by_xpath(".//*[@id='sidebar']/div[1]/div[1]/ul/li[3]/a/span").click()  # 排班
        time.sleep(5)
        ff.find_element_by_xpath(".//*[@id='sidebar']/div[1]/div[1]/ul/li[3]/ul/li[2]/a/span").click()  # 订单处理
        time.sleep(5)
        ff.find_element_by_xpath(
            ".//*[@id='orderBoxView-shell']/div/div[2]/table/tbody/tr[1]/td[1]/div/i").click()  # 勾选test001
        ff.find_element_by_xpath(".//*[@id='js-auto-split']/span").click()  # 转为工单
        time.sleep(2)
        ff.find_element_by_xpath(".//*[@id='dialogs-shell']/div[4]/div/div/div[3]/button[2]").click()  # 确定
        time.sleep(5)
        ff.find_element_by_xpath(".//*[@id='sidebar']/div[1]/div[1]/ul/li[3]/ul/li[6]/a/span").click()  # 工序调整
        time.sleep(5)
        ff.find_element_by_xpath(".//*[@id='unitBoxView-shell']/div/div/div/a/button").click()  # 手动排班
        ff.find_element_by_xpath(".//*[@id='tab-496c6237-fd05-4c63-a038-241bbae25bc9']/div[3]/button").click()  # 排在这里
        time.sleep(5)
        ff.save_screenshot("e:\\test.png")
        ff.close()
