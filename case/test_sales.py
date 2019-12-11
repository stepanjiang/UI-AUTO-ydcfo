# -*- coding:utf-8 -*-
from Case_info.Sales_case.sales_case_info import *
import pytest
from selenium import webdriver
import unittest
import time
from common.Base import Base
from Element_Location.Login_element.login_info_element import *
from common.Base import *
from Element_Location.Main_interface.main_element import *
class Sales_case(unittest.TestCase):
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
    def test01_sales_draft_new(self):
        print("新建销售单草稿单case")
        elemt = Base(self.driver)
        Homepage(self.driver).sales_line()
        Sales_info_case(self.driver).sales_new_draft_info()

    def test02_sales_new(self):
        print("新建销售单case")
        elemt = Base(self.driver)
        Homepage(self.driver).sales_line()
        time.sleep(1)
        Sales_info_case(self.driver).sales_new_info()

    def test03_sales_edit(self):
        elemt = Base(self.driver)
        Homepage(self.driver).sales_line()
        time.sleep(1)
        Sales_info_case(self.driver).sales_new_info()
        time.sleep(1)
        Homepage(self.driver).sales_line()
        time.sleep(2)
        Sales_info_case(self.driver).sales_edit_info()
        time.sleep(1)

    def test04_sales_copy(self):
        elemt = Base(self.driver)
        Homepage(self.driver).sales_line()
        time.sleep(1)
        Sales_info_case(self.driver).sales_new_info()
        time.sleep(1)
        Homepage(self.driver).sales_line()
        time.sleep(2)
        Sales_info_case(self.driver).sales_copy_info()



if __name__ == "__main__":
    unittest.main()