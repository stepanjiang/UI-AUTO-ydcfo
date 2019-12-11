# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from Element_Location.Quick_element.Draft_common_new import *
from Element_Location.Login_element.login_info_element import *
from Element_Location.Main_interface.main_element import *
class logins(unittest.TestCase):
    def setUp(self):
        print("开始")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 设置浏览器大小：全屏
        url = "https://ceshi.ydcfo.com"
        self.driver.get(url)
        Login_bizgo(self.driver).set_username("Combined_ALL")
        Login_bizgo(self.driver).set_password("123456")
        Login_bizgo(self.driver).click_sign()
        time.sleep(6)
        remove = '$("#xiaonengkefu").remove()'  # 清空小能助手
        self.driver.execute_script(remove)
    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
        print("结束")
    def test01_quick_sales_new(self):
        print("新建快捷开单case")
        elemt = Base(self.driver)
        Homepage(self.driver).sales_line()
        time.sleep(1)
        QuickSD_basic_location(self.driver).set_quickSD_basic_new()#切换到快捷开单
        QuickSD_basic_location(self.driver).set_quickSD_basic_info("100","50")#输入快捷开单数据
        QuickSD_basic_location(self.driver).set_check_Amount_money()#校验金额是否正确
        QuickSD_basic_location(self.driver).set_quickSD_check()#保存的时候校验
        time.sleep(1)



    def test02_quick_sales_info(self):
        elemt = Base(self.driver)
        Homepage(self.driver).sales_line()
        time.sleep(1)
        QuickSD_basic_location(self.driver).set_quickSD_basic_new()  # 切换到快捷开单
        quicksd_code = self.driver.find_element(*QuickSD_basic_location.quickSD_code).get_attribute("value")  # 获取快捷开单单号
        print(quicksd_code)
        self.driver.find_element(*QuickSD_basic_location.quickSD_customer_input).click()  # 点击客户名称输入框
        time.sleep(2)
        self.driver.find_element(*QuickSD_basic_location.quickSD_customer_input).send_keys(Keys.DOWN)  # 点击客户名称输入框
        time.sleep(1)
        self.driver.find_element(*QuickSD_basic_location.quickSD_customer_input).send_keys(Keys.ENTER)  # 点击客户名称输入框
        time.sleep(2)
        #self.driver.find_element(*QuickSD_basic_location.quickSD_picture).send_keys(r"E:\Combined_ALL_new\PC自动化图片及截图\使用附件\图1.jpg")  # 上传快捷开单图片
        time.sleep(2)
        QuickSD_basic_location(self.driver).save_intelligence_save()#智能记录提交

    def test03_XXXX_XX(self):
        print("删除或禁用产case")

if __name__ == "__main__":
    unittest.main()
