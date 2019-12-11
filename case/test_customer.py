# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
import unittest
import time
from common.Base import Base
from Element_Location.Login_element.login_info_element import *
from Element_Location.Main_interface.main_element import *
from Element_Location.Customer_element.customer_info_new import *
from Element_Location.Address_element.address_info_new import *
from Element_Location.Customer_element.customer_info_edit import *
from ALL_info.Customer_all_info.customer_info_list import *
from Element_Location.Customer_element.customer_info_delete import *
class Costmoer_case(unittest.TestCase):
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
    def test01_customer_new(self):
        print("客户新建case")
        elemt = Base(self.driver)
        Homepage(self.driver).customer_line()
        time.sleep(2)
        Customer_basic_location(self.driver).set_customer_basic_info("new"+Random_chinese) #填写客户信息
        Customer_basic_location(self.driver).set_customer_class_info("newcls"+Random_chinese) #填写客户分类
        Customer_basic_location(self.driver).new_address_button()#点击新建客户地址按钮
        Address_basic_location(self.driver).set_address_basic_info("客户新增地址备注！！！")#填写地址信息
        elemt.screenshot("客户新增地址截图")  # 截图
        Address_basic_location(self.driver).address_basic_info_save()#保存地址
        Customer_basic_location(self.driver).new_customer_info_save()#保存客户
        Customer_basic_location(self.driver).new_customer_info_check()#校验保存成功


    def test02_customer_edit_list(self):
        print("修改客户从列表点击编辑case")
        elemt = Base(self.driver)
        Homepage(self.driver).customer_line()
        time.sleep(2)
        Customer_basic_location(self.driver).set_customer_basic_info("list_info"+Random_chinese) #填写客户信息
        Customer_basic_location_edit(self.driver).set_customer_basic_info_edit()#获取客户名称
        Customer_basic_location(self.driver).new_customer_info_save()#保存客户
        Customer_basic_location(self.driver).new_customer_info_check()#校验保存成功
        Customer_basic_location_edit(self.driver).set_customer_basic_select()#搜索客户名
        Customer_select_list(self.driver).customer_list_edit()#点击客户操作编辑按钮
        time.sleep(2)
        Customer_basic_location_edit(self.driver).edit_customer_basic_info("edit_list"+Random_chinese)#编辑客户信息
        Customer_basic_location_edit(self.driver).edit_customer_class_basic_info("editcls_list"+Random_chinese)#编辑客户分类
        Customer_basic_location_edit(self.driver).edit_address_button()#点击编辑地址按钮
        Address_basic_location(self.driver).set_address_basic_info("客户列表页面进入修改地址备注！！！")#填写地址信息
        elemt.screenshot("客户列表页面修改地址截图")  # 截图
        Address_basic_location(self.driver).address_basic_info_save()#保存地址
        Customer_basic_location_edit(self.driver).edit_customer_info_save()#保存客户
        Customer_basic_location_edit(self.driver).edit_customer_info_check()#校验保存成功

    def test03_customer_edit_info(self):
        print("修改客户从客户详情点击编辑case")
        elemt = Base(self.driver)
        Homepage(self.driver).customer_line()
        time.sleep(2)
        Customer_basic_location(self.driver).set_customer_basic_info("info"+Random_chinese) #填写客户信息
        Customer_basic_location_edit(self.driver).set_customer_basic_info_edit()#获取客户名称
        Customer_basic_location(self.driver).new_customer_info_save()#保存客户
        Customer_basic_location(self.driver).new_customer_info_check()#校验保存成功
        Customer_basic_location_edit(self.driver).set_customer_basic_select()#搜索客户名
        Customer_select_list(self.driver).customer_list_name()#点击客户名称按钮
        time.sleep(2)
        Customer_basic_location_edit(self.driver).edit_customer_info()#点击客户详情页面编辑
        Customer_basic_location_edit(self.driver).edit_customer_basic_info("edit_info"+Random_chinese)#编辑客户信息
        Customer_basic_location_edit(self.driver).edit_customer_class_basic_info("editcls_info"+Random_chinese)#编辑客户分类
        Customer_basic_location_edit(self.driver).edit_address_button()#点击编辑地址按钮
        Address_basic_location(self.driver).set_address_basic_info("客户信息页面进入修改地址备注！！！")#填写地址信息
        elemt.screenshot("客户详情页面修改地址截图")  # 截图
        Address_basic_location(self.driver).address_basic_info_save()#保存地址
        Customer_basic_location_edit(self.driver).edit_customer_info_save()#保存客户
        Customer_basic_location_edit(self.driver).edit_customer_info_check()#校验保存成功


    def test04_customer_delete_list(self):#列表页面操作删除
        print("从客户列表删除case")
        elemt = Base(self.driver)
        Homepage(self.driver).customer_line()
        time.sleep(2)
        Customer_basic_location(self.driver).set_customer_basic_info("delete_list" + Random_chinese)  # 填写客户信息
        Customer_basic_location_edit(self.driver).set_customer_basic_info_edit()  # 获取客户名称
        Customer_basic_location(self.driver).new_customer_info_save()  # 保存客户
        Customer_basic_location(self.driver).new_customer_info_check()  # 校验保存成功
        Customer_basic_location_edit(self.driver).set_customer_basic_select()  # 搜索客户名
        elemt.screenshot("客户列表页面搜索结果截图")
        Customer_select_list(self.driver).customer_list_delete()  # 点击客户操作删除按钮
        Customer_basic_location_delete(self.driver).windos_delete_or_disable_customer()#校验是禁用还是删除
        elemt.screenshot("客户列表页面删除后截图")

    def test05_customer_delete_info(self):#客户详情页面删除
        print("从客户信息删除case")
        elemt = Base(self.driver)
        Homepage(self.driver).customer_line()
        time.sleep(2)
        Customer_basic_location(self.driver).set_customer_basic_info("delete_info" + Random_chinese)  # 填写客户信息
        Customer_basic_location_edit(self.driver).set_customer_basic_info_edit()  # 获取客户名称
        Customer_basic_location(self.driver).new_customer_info_save()  # 保存客户
        Customer_basic_location(self.driver).new_customer_info_check()  # 校验保存成功
        Customer_basic_location_edit(self.driver).set_customer_basic_select()  # 搜索客户名
        Customer_select_list(self.driver).customer_list_name()#点击进入客户详情
        time.sleep(2)
        Customer_basic_location_delete(self.driver).customer_info_delete()#点击进入客户信息删除
        Customer_basic_location_delete(self.driver).windos_delete_or_disable_customer()  # 校验是禁用还是删除
        elemt.screenshot("客户详情页面删除后截图")





if __name__ == "__main__":
    unittest.main()
