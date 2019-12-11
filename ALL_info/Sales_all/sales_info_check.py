# -*- coding:utf-8 -*-
"""销售单产品信息表"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Sales_info_check(Base):
    """获取第一排的div"""
    Sales_dimension_list =(By.XPATH,"//div[contains(@id,'columntable') and contains(@id,'SaleOrder_grid')]/*")
    """组合信息的元素定位"""
    def get_column_by_name(self,column_name):
        table_column_elements = self.driver.find_elements(*Sales_info_check.Sales_dimension_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)

    """销售单详情页面产品数据"""
    # 定位产品名称
    def Product_gridname_info(self,  row=1):
        global product_name
        location = self.get_column_by_name("产品")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_name = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取产品名称
        print("产品名称:"+product_name)
        time.sleep(1)
        return product_name

    #产品规格定位
    def Product_gridspec_info(self, row=1):
        global product_spec
        location = self.get_column_by_name("规格型号")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_spec = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取规格型号
        print("产品规格:"+product_spec)
        time.sleep(1)

    #产品颜色定位
    def Product_gridcolor_info(self,  row=1):
        global product_color
        location = self.get_column_by_name("颜色")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_color = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取颜色
        print("产品颜色:"+product_color)
        time.sleep(1)


    #产品重量定位
    def Product_gridweight_info(self,  row=1):
        global product_weight
        location = self.get_column_by_name("重量")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_weight = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取重量
        print("重量:"+product_weight)
        time.sleep(1)

    #产品总箱数定位
    def Product_gridcartons_info(self, row=1):
        global product_cartons
        location = self.get_column_by_name("总箱数")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_cartons = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取总数量
        print("总箱数:"+product_cartons)
        time.sleep(1)

    #产品每箱数量定位
    def Product_grideachCarton_info(self,  row=1):
        global product_eachcaton
        location = self.get_column_by_name("每箱数量")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_eachcaton = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取每箱数量
        print("每箱数量:"+product_eachcaton)
        time.sleep(1)


    #产品总数量定位
    def Product_griddisplayQty_info(self,  row=1):
        global displayqty
        location = self.get_column_by_name("总数量")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        displayqty = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取总数量
        print("总数量:"+displayqty)
        time.sleep(1)


    #产品单价定位
    def Product_SDprice(self, row=1):
        global product_SDprice
        location = self.get_column_by_name("单价")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_SDprice = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取产品单价
        print("产品单价:"+product_SDprice)
        time.sleep(1)

    #产品折扣定位
    def Product_gridDiscount(self, row=1):
        global product_Discount
        location = self.get_column_by_name("折扣")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_Discount = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取产品折扣
        print("产品折扣:"+product_Discount)
        time.sleep(1)


    #产品折后价定位
    def Product_gridunitPrice(self, row=1):
        global product_unitPrice
        location = self.get_column_by_name("折后价")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_unitPrice = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取折后价
        print("产品折后价:"+product_unitPrice)
        time.sleep(1)

    # 产品长定位
    def Product_gridlong(self,  row=1):
        global product_long
        location = self.get_column_by_name("长")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_long = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取产品长
        print("产品长:"+product_long)
        time.sleep(1)


    # 产品宽定位
    def Product_gridwidth(self, row=1):
        global product_width
        location = self.get_column_by_name("宽")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_width = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取产品宽
        print("产品宽:"+product_width)
        time.sleep(1)

    # 产品高定位
    def Product_gridheight(self,  row=1):
        global product_height
        location = self.get_column_by_name("高")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_height = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取产品高
        print("产品高:"+product_height)
        time.sleep(1)


    # 产品送货数量定位
    def Product_Delivery_quantity(self, row=1):
        global product_delivery_quantity
        location = self.get_column_by_name("送货数量")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_delivery_quantity = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取送货数量
        print("产品送货数量:"+product_delivery_quantity)
        time.sleep(1)


    #产品本次送货数量定位
    def Product_this_Delivery_quantity(self, row=1):
        global product_this_delivery_quantity
        location = self.get_column_by_name("本次送货")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_this_delivery_quantity = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取本次送货
        print("本次送货:"+product_this_delivery_quantity)
        time.sleep(1)

    # 产品备注定位
    def Product_gridremark(self,  row=1):
        global product_remark
        location = self.get_column_by_name("备注")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_remark = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取备注
        print("产品备注:"+product_remark)
        time.sleep(1)

    #产品供应商定位
    def Product_gridvendor(self, row=1):
        global product_vendor
        location = self.get_column_by_name("供应商")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_vendor = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取供应商
        print("供应商:"+product_vendor)
        time.sleep(1)

    # 产品进价定位
    def Product_gridPDprice(self,row=1):
        global product_PDprice
        location = self.get_column_by_name("进价")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_PDprice = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取进价
        print("产品进价:"+product_PDprice)
        time.sleep(1)

    #产品采购箱数
    def Product_gridpurchaseQty(self,  row=1):
        global product_purchaseqty
        location = self.get_column_by_name("采购箱数")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_purchaseqty = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取采购总数量
        print("复制新增的采购箱数:"+product_purchaseqty)

    """销售单复制新增后页面产品数据"""

    # 定位产品名称
    def Product_gridname_info_copy(self, row=1):
        global product_name_copy
        location = self.get_column_by_name("产品")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_name_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取产品名称
        print("产品名称:" + product_name_copy)
        time.sleep(1)

    # 产品规格定位
    def Product_gridspec_info_copy(self, row=1):
        global product_spec_copy
        location = self.get_column_by_name("规格型号")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_spec_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取规格型号
        print("产品规格:" + product_spec_copy)
        time.sleep(1)

    # 产品颜色定位
    def Product_gridcolor_info_copy(self, row=1):
        global product_color_copy
        location = self.get_column_by_name("颜色")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_color_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取颜色
        print("产品颜色:" + product_color_copy)
        time.sleep(1)

    # 产品重量定位
    def Product_gridweight_info_copy(self, row=1):
        global product_weight_copy
        location = self.get_column_by_name("重量")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_weight_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取重量
        print("重量:" + product_weight_copy)
        time.sleep(1)

    # 产品总箱数定位
    def Product_gridcartons_info_copy(self, row=1):
        global product_cartons_copy
        location = self.get_column_by_name("总箱数")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_cartons_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取总数量
        print("总箱数:" + product_cartons_copy)
        time.sleep(1)

    # 产品每箱数量定位
    def Product_grideachCarton_info_copy(self, row=1):
        global product_eachcaton_copy
        location = self.get_column_by_name("每箱数量")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_eachcaton_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取每箱数量
        print("每箱数量:" + product_eachcaton_copy)
        time.sleep(1)

    # 产品总数量定位
    def Product_griddisplayQty_info_copy(self, row=1):
        global displayqty_copy
        location = self.get_column_by_name("总数量")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        displayqty_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取总数量
        print("总数量:" + displayqty_copy)
        time.sleep(1)

    # 产品单价定位
    def Product_SDprice_copy(self, row=1):
        global product_SDprice_copy
        location = self.get_column_by_name("单价")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_SDprice_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取产品单价
        print("产品单价:" + product_SDprice_copy)
        time.sleep(1)

    # 产品折扣定位
    def Product_gridDiscount_copy(self, row=1):
        global product_Discount_copy
        location = self.get_column_by_name("折扣")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_Discount_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取产品折扣
        print("产品折扣:" + product_Discount_copy)
        time.sleep(1)

    # 产品折后价定位
    def Product_gridunitPrice_copy(self, row=1):
        global product_unitPrice_copy
        location = self.get_column_by_name("折后价")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_unitPrice_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取折后价
        print("产品折后价:" + product_unitPrice_copy)
        time.sleep(1)

    # 产品长定位
    def Product_gridlong_copy(self, row=1):
        global product_long_copy
        location = self.get_column_by_name("长")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_long_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取产品长
        print("产品长:" + product_long_copy)
        time.sleep(1)

    # 产品宽定位
    def Product_gridwidth_copy(self, row=1):
        global product_width_copy
        location = self.get_column_by_name("宽")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_width_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取产品宽
        print("产品宽:" + product_width_copy)
        time.sleep(1)

    # 产品高定位
    def Product_gridheight_copy(self, row=1):
        global product_height_copy
        location = self.get_column_by_name("高")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_height_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute(
            "innerHTML")  # 获取产品高
        print("产品高:" + product_height_copy)
        time.sleep(1)

    # 产品送货数量定位
    def Product_Delivery_quantity_copy(self, row=1):
        global product_delivery_quantity_copy
        location = self.get_column_by_name("送货数量")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_delivery_quantity_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取送货数量
        print("产品送货数量:" + product_delivery_quantity_copy)
        time.sleep(1)

    # 产品本次送货数量定位
    def Product_this_Delivery_quantity_copy(self, row=1):
        global product_this_delivery_quantity_copy
        location = self.get_column_by_name("本次送货")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_this_delivery_quantity_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取本次送货
        print("本次送货:" + product_this_delivery_quantity_copy)
        time.sleep(1)

    # 产品备注定位
    def Product_gridremark_copy(self, row=1):
        global product_remark_copy
        location = self.get_column_by_name("备注")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_remark_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取备注
        print("产品备注:" + product_remark_copy)
        time.sleep(1)

    # 产品供应商定位
    def Product_gridvendor_copy(self, row=1):
        global product_vendor_copy
        location = self.get_column_by_name("供应商")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_vendor_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取供应商
        print("供应商:" + product_vendor_copy)
        time.sleep(1)

    # 产品进价定位
    def Product_gridPDprice_copy(self, row=1):
        global product_PDprice_copy
        location = self.get_column_by_name("进价")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_PDprice_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取进价
        print("产品进价:" + product_PDprice_copy)
        time.sleep(1)

    # 产品采购箱数
    def Product_gridpurchaseQty_copy(self, row=1):
        global product_purchaseqty_copy
        location = self.get_column_by_name("采购箱数")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        product_purchaseqty_copy = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取采购总数量
        print("复制新增的采购箱数:" + product_purchaseqty_copy)

    def check_copy_sales_info(self):
        if product_name == product_name_copy\
            and product_spec == product_spec_copy \
            and product_color ==product_color_copy \
            and product_weight_copy == product_weight_copy \
            and product_cartons == product_cartons_copy\
            and product_eachcaton == product_eachcaton_copy\
            and displayqty == displayqty_copy\
            and product_SDprice == product_SDprice_copy\
            and product_Discount == product_Discount_copy\
            and product_unitPrice == product_unitPrice_copy\
            and product_long == product_long_copy\
            and product_width == product_width_copy\
            and product_height == product_height_copy\
            and product_remark == product_remark_copy:
            print("数据均相同正确")
            assert product_name == product_name_copy \
                   and product_spec == product_spec_copy \
                   and product_color == product_color_copy \
                   and product_weight_copy == product_weight_copy \
                   and product_cartons == product_cartons_copy \
                   and product_eachcaton == product_eachcaton_copy \
                   and displayqty == displayqty_copy \
                   and product_SDprice == product_SDprice_copy \
                   and product_Discount == product_Discount_copy \
                   and product_unitPrice == product_unitPrice_copy \
                   and product_long == product_long_copy \
                   and product_width == product_width_copy \
                   and product_height == product_height_copy \
                   and product_remark == product_remark_copy
        else:
            print("数据存在不相同")
            print("产品名称:"+product_name,product_name_copy)
            print("产品规格:"+product_spec,product_spec_copy)
            print("产品颜色:"+product_color,product_color_copy)
            print("产品重量:"+product_weight,product_weight_copy)
            print("产品总箱数:"+product_cartons,product_cartons_copy)
            print("产品每箱数量:"+product_eachcaton,product_eachcaton_copy)
            print("产品总数量:"+displayqty,displayqty_copy)
            print("产品单价:"+product_SDprice,product_SDprice_copy)
            print("产品折扣:"+product_Discount,product_Discount_copy)
            print("产品折后价:"+product_unitPrice,product_unitPrice_copy)
            print("产品长度:"+product_long,product_long_copy)
            print("产品宽度:"+product_width,product_width_copy)
            print("产品高度:"+product_height,product_height_copy)
            print("产品备注:"+product_remark,product_remark_copy)
            assert product_name == product_name_copy \
                   and product_spec == product_spec_copy \
                   and product_color == product_color_copy \
                   and product_weight_copy == product_weight_copy \
                   and product_cartons == product_cartons_copy \
                   and product_eachcaton == product_eachcaton_copy \
                   and displayqty == displayqty_copy \
                   and product_SDprice == product_SDprice_copy \
                   and product_Discount == product_Discount_copy \
                   and product_unitPrice == product_unitPrice_copy \
                   and product_long == product_long_copy \
                   and product_width == product_width_copy \
                   and product_height == product_height_copy \
                   and product_remark == product_remark_copy






