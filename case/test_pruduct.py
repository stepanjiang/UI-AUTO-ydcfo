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
class Product_case(unittest.TestCase):
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
    def test01_product_new(self):
        print("新建产品case")
        elemt = Base(self.driver)
        Homepage(self.driver).product_line()
        time.sleep(2)
        Product_basic_location(self.driver).set_product_basic_info("new"+Random_chinese,"new"+str(sstime),"客户货号"+Random_chinese)#新建产品数据
        elemt.screenshot("产品新建数据")#截图
        Product_basic_location(self.driver).set_product_class_info()#新建产品分类数据
        elemt.js_scroll_end()  # 下移界面
        time.sleep(2)
        Product_dimension(self.driver).initial_inventory("2")  # 期初库存
        Product_dimension(self.driver).inventory_down("1")  # 库存下限
        Product_dimension(self.driver).inventory_top("1000")  # 库存上限
        Product_dimension(self.driver).Quantity_box("10")  # 每箱数量
        Product_dimension(self.driver).long("10")  # 长
        Product_dimension(self.driver).wide("10")  # 宽
        Product_dimension(self.driver).high("10")  # 高
        Product_dimension(self.driver).price1("5")  # 售价1
        Product_dimension(self.driver).price2("10")  # 售价2
        Product_dimension(self.driver).purchase_price1("2")  # 进价1
        Product_dimension(self.driver).purchase_price2("4")  # 进价2
        elemt.screenshot("产品新建维度数据")#截图
        time.sleep(2)
        elemt.js_scroll_top()  # 上移界面
        time.sleep(2)
        Product_dimension(self.driver).new_switch_combination()#切换组合信息
        time.sleep(2)
        Product_combination_location(self.driver).set_prodcut_son_profit_margin("50")#利润率
        Product_combination(self.driver).set_product_son_name("子"+Random_chinese)#子产品名称
        Product_combination(self.driver).combination_picture()#子产品图片
        Product_combination(self.driver).set_product_son_rate("2.2222")#组合比例
        Product_combination(self.driver).set_product_son_weight("1.111111")#重量
        Product_combination(self.driver).set_product_son_qtynumber("1")#每箱数量
        Product_combination(self.driver).set_product_son_price1("10")#售价1
        Product_combination(self.driver).set_product_son_price2("8")#售价2
        Product_combination(self.driver).set_product_son_purchase_price1("6")#进价1
        Product_combination(self.driver).set_product_son_purchase_price2("4")#进价2
        Product_combination(self.driver).set_product_son_purchase_long("10")#长
        Product_combination(self.driver).set_product_son_purchase_wide("10")#宽
        Product_combination(self.driver).set_product_son_high("10")#高
        Product_combination(self.driver).set_product_son_loss("10")#损耗率
        Product_combination(self.driver).set_product_son_copy_bank()#点击复制新增行
        time.sleep(2)
        Product_basic_location(self.driver).new_product_info_save()#保存产品

    def test02_product_edit(self):
        print("修改产品case")
        elemt = Base(self.driver)
        Homepage(self.driver).product_line()
        time.sleep(2)
        Product_basic_location_edit(self.driver).set_product_info_new_name("info"+Random_chinese)#产品页面新增产品
        time.sleep(2)
        Product_basic_location_edit(self.driver).select_product_name()#搜索产品
        time.sleep(1)
        Product_select_list(self.driver).product_list_edit()#点击进入编辑
        time.sleep(1)
        Product_basic_location_edit(self.driver).set_product_class_info_edit("ed"+Random_chinese,"edit" + str(sstime),"ed客户货号"+Random_chinese)#编辑产品数据
        elemt.screenshot("产品修改数据")  # 截图
        time.sleep(2)
        self.driver.find_element(*Product_basic_location_edit.edit_product_name).click()#重新定位位置
        elemt.js_scroll_end()  # 下移界面
        time.sleep(2)
        Product_dimension(self.driver).initial_inventory("2")  # 期初库存
        Product_dimension(self.driver).inventory_down("1")  # 库存下限
        Product_dimension(self.driver).inventory_top("1000")  # 库存上限
        Product_dimension(self.driver).Quantity_box("10")  # 每箱数量
        Product_dimension(self.driver).long("10")  # 长
        Product_dimension(self.driver).wide("10")  # 宽
        Product_dimension(self.driver).high("10")  # 高
        Product_dimension(self.driver).price1("5")  # 售价1
        Product_dimension(self.driver).price2("10")  # 售价2
        Product_dimension(self.driver).purchase_price1("2")  # 进价1
        Product_dimension(self.driver).purchase_price2("4")  # 进价2
        elemt.screenshot("产品修改维度数据")  # 截图
        time.sleep(2)

    def test03_product_delete(self):
        print("删除或禁用产case")
        Homepage(self.driver).product_line()
        time.sleep(2)
        Product_basic_location_edit(self.driver).set_product_info_new_name("delete"+Random_chinese)#产品页面新增产品
        time.sleep(2)
        Product_basic_location_edit(self.driver).select_product_name()#搜索产品
        time.sleep(1)
        Product_select_list(self.driver).product_list_delete()#点击删除产品
        time.sleep(1)
        Product_basic_location_delete(self.driver).windos_delete_or_disable()#判断产品删除或禁用

if __name__ == "__main__":
    unittest.main()
