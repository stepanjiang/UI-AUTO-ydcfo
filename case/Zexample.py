# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from Element_Location.Login_element.login_info_element import *
from Element_Location.Main_interface.main_element import *
from Element_Location.Product_element.product_info_new import *
from ALL_info.Product_all_info.product_info_basic import *
from ALL_info.Product_all_info.product_info_combination import *
from ALL_info.Product_all_info.product_info_list import *
from Element_Location.Product_element.product_info_edit import *
from Element_Location.Product_element.product_list_delete import *
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
    def test01_XXXX_XX(self):
        print("新建产品case")
        elemt = Base(self.driver)


    def test02_XXXX_XX(self):
        print("修改产品case")
        elemt = Base(self.driver)


    def test03_XXXX_XX(self):
        print("删除或禁用产case")

if __name__ == "__main__":
    unittest.main()
