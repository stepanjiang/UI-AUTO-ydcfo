# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
import unittest
import time
from common.Base import Base
from Element_Location.Login_element.login_info_element import *
from Element_Location.Main_interface.main_element import *
from Element_Location.Vendor_element.vendor_info_new import *
from Element_Location.Address_element.address_info_new import *
from Element_Location.Vendor_element.vendor_info_edit import *
from ALL_info.Vendor_all_info.vendor_info_list import *
from Element_Location.Vendor_element.vendor_info_delete import *
class Vendor_case(unittest.TestCase):
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
    def test01_vendor_new(self):
        print("新建供应商case")
        elemt = Base(self.driver)
        Homepage(self.driver).vendor_line()
        time.sleep(2)
        Vendor_basic_location(self.driver).set_vendor_basic_info("new"+Random_chinese)#填写供应商信息
        Vendor_basic_location(self.driver).set_vendor_class_info("newclas"+Random_chinese)#填写供应商分类
        Vendor_basic_location(self.driver).new_address_button()  # 点击新建供应商地址按钮
        Address_basic_location(self.driver).set_address_basic_info("客户新增地址备注！！！")  # 填写地址信息
        elemt.screenshot("供应商新增地址截图")  # 截图
        Address_basic_location(self.driver).address_basic_info_save()  # 保存地址
        Vendor_basic_location(self.driver).new_vendor_info_save()  # 保存供应商
        Vendor_basic_location(self.driver).new_vendor_info_check()  # 校验保存成功
        

    def test02_vendor_edit_list(self):
        print("修改供应商从列表点击编辑case")
        elemt = Base(self.driver)
        Homepage(self.driver).vendor_line()
        time.sleep(2)
        Vendor_basic_location(self.driver).set_vendor_basic_info("list_info" + Random_chinese)  # 填写供应商信息
        Vendor_basic_location_edit(self.driver).set_vendor_basic_info_edit()#获取供应商名称
        Vendor_basic_location(self.driver).new_vendor_info_save()#保存供应商
        Vendor_basic_location(self.driver).new_vendor_info_check()#校验保存成功
        Vendor_basic_location_edit(self.driver).set_vendor_basic_select()#搜索供应商名
        Vendor_select_list(self.driver).vendor_list_edit()#点击供应商操作编辑按钮
        time.sleep(2)
        Vendor_basic_location_edit(self.driver).edit_vendor_basic_info("edit_list"+Random_chinese)#编辑供应商信息
        Vendor_basic_location_edit(self.driver).edit_vendor_class_basic_info("editcls"+Random_chinese)#编辑供应商分类
        Vendor_basic_location_edit(self.driver).edit_address_button()#点击编辑地址按钮
        Address_basic_location(self.driver).set_address_basic_info("供应商修改地址备注！！！")#填写地址信息
        elemt.screenshot("供应商修改地址截图")  # 截图
        Address_basic_location(self.driver).address_basic_info_save()#保存地址
        Vendor_basic_location_edit(self.driver).edit_vendor_info_save()#保存供应商
        Vendor_basic_location_edit(self.driver).edit_vendor_info_check()#校验保存成功

    def test03_vendor_edit_info(self):
        print("修改供应商从供应商详情点击编辑case")
        elemt = Base(self.driver)
        Homepage(self.driver).vendor_line()
        time.sleep(2)
        Vendor_basic_location(self.driver).set_vendor_basic_info("info" + Random_chinese)  # 填写供应商信息
        Vendor_basic_location_edit(self.driver).set_vendor_basic_info_edit()  # 获取供应商名称
        Vendor_basic_location(self.driver).new_vendor_info_save()  # 保存供应商
        Vendor_basic_location(self.driver).new_vendor_info_check()  # 校验保存成功
        Vendor_basic_location_edit(self.driver).set_vendor_basic_select()  # 搜索供应商名
        Vendor_select_list(self.driver).vendor_list_name()  # 点击供应商名称按钮
        time.sleep(2)
        Vendor_basic_location_edit(self.driver).edit_vendor_info()#点击供应商详情页面编辑按钮
        Vendor_basic_location_edit(self.driver).edit_vendor_basic_info("edit_info" + Random_chinese)  # 编辑供应商信息
        Vendor_basic_location_edit(self.driver).edit_vendor_class_basic_info("editcls" + Random_chinese)  # 编辑供应商分类
        Vendor_basic_location_edit(self.driver).edit_address_button()  # 点击编辑地址按钮
        Address_basic_location(self.driver).set_address_basic_info("供应商修改地址备注！！！")  # 填写地址信息
        elemt.screenshot("供应商修改地址截图")  # 截图
        Address_basic_location(self.driver).address_basic_info_save()  # 保存地址
        Vendor_basic_location_edit(self.driver).edit_vendor_info_save()  # 保存供应商
        Vendor_basic_location_edit(self.driver).edit_vendor_info_check()  # 校验保存成功



    def test04_vendor_delete_list(self):#列表页面操作删除
        print("从供应商列表删除case")
        elemt = Base(self.driver)
        Homepage(self.driver).vendor_line()
        time.sleep(2)
        Vendor_basic_location(self.driver).set_vendor_basic_info("delete_list" + Random_chinese)  # 填写供应商信息
        Vendor_basic_location_edit(self.driver).set_vendor_basic_info_edit()  # 获取供应商名称
        Vendor_basic_location(self.driver).new_vendor_info_save()  # 保存供应商
        Vendor_basic_location(self.driver).new_vendor_info_check()  # 校验保存成功
        Vendor_basic_location_edit(self.driver).set_vendor_basic_select()  # 搜索供应商名
        elemt.screenshot("供应商列表页面搜索后截图")
        Vendor_select_list(self.driver).vendor_list_delete()  # 点击供应商操作删除按钮
        Vendor_basic_location_delete(self.driver).windos_delete_or_disable_vendor()  # 校验是禁用还是删除
        elemt.screenshot("供应商列表页面删除后截图")
        
    def test05_vendor_delete_info(self):#供应商详情页面删除
        print("从供应商信息里删除case")
        elemt = Base(self.driver)
        Homepage(self.driver).vendor_line()
        time.sleep(2)
        Vendor_basic_location(self.driver).set_vendor_basic_info("delete_info" + Random_chinese)  # 填写供应商信息
        Vendor_basic_location_edit(self.driver).set_vendor_basic_info_edit()  # 获取供应商名称
        Vendor_basic_location(self.driver).new_vendor_info_save()  # 保存供应商
        Vendor_basic_location(self.driver).new_vendor_info_check()  # 校验保存成功
        Vendor_basic_location_edit(self.driver).set_vendor_basic_select()  # 搜索供应商名
        Vendor_select_list(self.driver).vendor_list_name()  # 点击进入供应商详情
        time.sleep(2)
        Vendor_basic_location_delete(self.driver).vendor_info_delete()  # 点击进入供应商信息删除
        Vendor_basic_location_delete(self.driver).windos_delete_or_disable_vendor()  # 校验是禁用还是删除
        elemt.screenshot("供应商详情页面删除后截图")



if __name__ == "__main__":
    unittest.main()
