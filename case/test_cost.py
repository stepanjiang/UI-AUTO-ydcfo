# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from Element_Location.Login_element.login_info_element import *
from Element_Location.Main_interface.main_element import *
from Element_Location.Cost_element.Cost_common_new import *
from ALL_info.Cost_all_info.cost_info_list import *
from Element_Location.Cost_element.Cost_common_edit import *
from Element_Location.Cost_element.Cost_common_delete import *
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
    def test01_income_new(self):
        print("新建费用收入case")
        elemt = Base(self.driver)
        Homepage(self.driver).cost_income_expenditure()
        time.sleep(1)
        Cost_basic_location(self.driver).set_cost_basic_income_new()#新建费用收入
        Cost_basic_location(self.driver).get_cost_code_new("income")#获取单号
        Cost_basic_location(self.driver).set_cost_basic_class_new("新建收入类别"+Random_chinese)#输入费用类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_detailed_new("新建收入明细"+Random_chinese)#输入明细类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_info_new("100","费用收入备注！！！！！！！！！！！")#填写费用收入数据
        elemt.screenshot("新建费用收入数据")
        time.sleep(2)

    def test02_expend_new(self):
        print("新建费用支出case")
        elemt = Base(self.driver)
        Homepage(self.driver).cost_income_expenditure()
        time.sleep(1)
        Cost_basic_location(self.driver).set_cost_basic_expend_new()  # 新建费用支出
        Cost_basic_location(self.driver).get_cost_code_new("expend")  # 获取单号
        Cost_basic_location(self.driver).set_cost_basic_class_new("新建支出类别" + Random_chinese)  # 输入费用类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_detailed_new("新建支出明细" + Random_chinese)  # 输入明细类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_info_new("10", "费用支出备注！！！！！！！！！！！")  # 填写费用支出数据
        elemt.screenshot("新建费用支出数据")
        time.sleep(2)

    def test03_income_edit(self):
        print("修改费用收入case")
        elemt = Base(self.driver)
        """准备数据"""
        Homepage(self.driver).cost_income_expenditure()
        time.sleep(1)
        Cost_basic_location(self.driver).set_cost_basic_income_new()  # 新建费用收入
        Cost_basic_location(self.driver).get_cost_code_new("income")  # 获取单号
        Cost_basic_location(self.driver).set_cost_basic_class_new("新建info收入类别" + Random_chinese)  # 输入费用类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_detailed_new("新建info收入明细" + Random_chinese)  # 输入明细类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_info_new("10", "新建info费用收入备注！！！！！！！！！！！")  # 填写费用收入数据
        elemt.screenshot("修改费用收入新建的数据")
        """列表页面搜索部分"""
        Cost_basic_location_edit(self.driver).get_cost_code_info()#获取保存后详情页面单号
        Homepage(self.driver).cost_income_expenditure()#点击费用收入支出按钮
        time.sleep(1)
        Cost_basic_location_edit(self.driver).set_cost_basic_select_info()#进入费用支出搜索
        time.sleep(1)
        Cost_select_list(self.driver).cost_list_code()#点击搜索到的第一个单号进入详情
        """编辑部分"""
        Cost_basic_location_edit(self.driver).set_cost_basic_info_edit_button()#进入编辑页面点击加号
        Cost_basic_location_edit(self.driver).set_windos_class_info_edit("修改收入类别"+Random_chinese)#输入修改后的类别名称
        Cost_basic_location_edit(self.driver).set_windos_detailed_info_edit("修改收入明细"+Random_chinese)#输入修改后的类别名称
        Cost_basic_location_edit(self.driver).set_cost_basic_info_edit("1000","修改info费用收入备注！！！！！！！！！！！")#修改填写费用收入数据
        time.sleep(1)
        elemt.screenshot("修改费用收入后的数据")
        time.sleep(2)



    def test04_expend_edit(self):
        print("修改费用支出case")
        elemt = Base(self.driver)
        """准备数据"""
        Homepage(self.driver).cost_income_expenditure()
        time.sleep(1)
        Cost_basic_location(self.driver).set_cost_basic_expend_new()  # 新建费用支出
        Cost_basic_location(self.driver).get_cost_code_new("expend")  # 获取单号
        Cost_basic_location(self.driver).set_cost_basic_class_new("新建info支出类别" + Random_chinese)  # 输入费用类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_detailed_new("新建info支出明细" + Random_chinese)  # 输入明细类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_info_new("20", "新建info费用支出备注！！！！！！！！！！！")  # 填写费用支出数据
        elemt.screenshot("修改费用支出新建的数据")
        """列表页面搜索部分"""
        Cost_basic_location_edit(self.driver).get_cost_code_info()  # 获取保存后详情页面单号
        Homepage(self.driver).cost_income_expenditure()  # 点击费用收入支出按钮
        time.sleep(1)
        Cost_basic_location_edit(self.driver).set_cost_basic_select_info()  # 进入费用支出搜索
        time.sleep(1)
        Cost_select_list(self.driver).cost_list_code()  # 点击搜索到的第一个单号进入详情
        """编辑部分"""
        Cost_basic_location_edit(self.driver).set_cost_basic_info_edit_button()  # 进入编辑页面点击加号
        Cost_basic_location_edit(self.driver).set_windos_class_info_edit("修改支出类别" + Random_chinese)  # 输入修改后的类别名称
        Cost_basic_location_edit(self.driver).set_windos_detailed_info_edit("修改支出明细" + Random_chinese)  # 输入修改后的类别名称
        Cost_basic_location_edit(self.driver).set_cost_basic_info_edit("2000", "修改info费用支出备注！！！！！！！！！！！")  # 修改填写费用支出数据
        time.sleep(1)
        elemt.screenshot("修改费用支出后的数据")
        time.sleep(2)

    def test05_income_delete(self):
        print("删除费用收入case")
        elemt = Base(self.driver)
        """准备数据"""
        Homepage(self.driver).cost_income_expenditure()
        time.sleep(1)
        Cost_basic_location(self.driver).set_cost_basic_income_new()  # 新建费用收入
        Cost_basic_location(self.driver).get_cost_code_new("income")  # 获取单号
        Cost_basic_location(self.driver).set_cost_basic_class_new("删除info收入类别" + Random_chinese)  # 输入费用类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_detailed_new("删除info收入明细" + Random_chinese)  # 输入明细类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_info_new("10", "删除info费用收入备注！！！！！！！！！！！")  # 填写费用收入数据
        elemt.screenshot("删除的费用收入新建的数据")
        """列表页面搜索部分"""
        Cost_basic_location_edit(self.driver).get_cost_code_info()  # 获取保存后详情页面单号
        Homepage(self.driver).cost_income_expenditure()  # 点击费用收入支出按钮
        time.sleep(1)
        Cost_basic_location_edit(self.driver).set_cost_basic_select_info()  # 进入费用支出搜索
        time.sleep(1)
        Cost_select_list(self.driver).cost_list_code()  # 点击搜索到的第一个单号进入详情
        Cost_basic_location_delete(self.driver).cost_delete_info() #点击详情页面删除按钮
        Cost_basic_location_delete(self.driver).get_cost_delete_info("费用收入支出校验正确删除截图","费用收入支出提示校验失败截图")

    def test06_expend_delete(self):
        print("删除费用支出case")
        elemt = Base(self.driver)
        """准备数据"""
        Homepage(self.driver).cost_income_expenditure()
        time.sleep(1)
        Cost_basic_location(self.driver).set_cost_basic_expend_new()  # 新建费用支出
        Cost_basic_location(self.driver).get_cost_code_new("expend")  # 获取单号
        Cost_basic_location(self.driver).set_cost_basic_class_new("删除info支出类别" + Random_chinese)  # 输入费用类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_detailed_new("删除info支出明细" + Random_chinese)  # 输入明细类别弹框数据并选择
        Cost_basic_location(self.driver).set_cost_basic_info_new("20", "删除info费用支出备注！！！！！！！！！！！")  # 填写费用支出数据
        elemt.screenshot("删除费用支出新建的数据")
        """列表页面搜索部分"""
        Cost_basic_location_edit(self.driver).get_cost_code_info()  # 获取保存后详情页面单号
        Homepage(self.driver).cost_income_expenditure()  # 点击费用收入支出按钮
        time.sleep(1)
        Cost_basic_location_edit(self.driver).set_cost_basic_select_info()  # 进入费用支出搜索
        time.sleep(1)
        Cost_select_list(self.driver).cost_list_code()  # 点击搜索到的第一个单号进入详情
        Cost_basic_location_delete(self.driver).cost_delete_info()  # 点击详情页面删除按钮
        Cost_basic_location_delete(self.driver).get_cost_delete_info("费用收入支出校验正确删除截图", "费用收入支出提示校验失败截图")

    def test07_delete_list(self):
        print("列表页面循环删除数据")
        elemt = Base(self.driver)
        """准备数据"""
        Homepage(self.driver).cost_income_expenditure()
        time.sleep(2)
        Cost_basic_location_delete(self.driver).cost_list_pagelist_number()#获取页面数据
        time.sleep(1)
        Cost_basic_location_delete(self.driver).get_cost_delete_for()#循环删除


if __name__ == "__main__":
    unittest.main()
