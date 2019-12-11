# -*- coding:utf-8 -*-
"""销售单产品信息表"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Sales_dimension(Base):
    """获取第一排的div"""
    Sales_dimension_list =(By.XPATH,"//div[contains(@id,'columntable') and contains(@id,'SaleOrder_grid')]/*")
    """组合信息的元素定位"""
    def get_column_by_name(self,column_name):
        table_column_elements = self.driver.find_elements(*Sales_dimension.Sales_dimension_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)

    """销售单页面产品数据"""

    # 定位产品名称
    def Product_gridname(self, Product_name_value, row=1):
        location = self.get_column_by_name("产品")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridname')]/input").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridname')]/input").send_keys(Product_name_value)
        time.sleep(1)
        for i in range(2):
            self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridname')]/input").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品规格定位
    def Product_gridspec(self, Product_spec_value, row=1):
        location = self.get_column_by_name("规格型号")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridspecId')]/input").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridspecId')]/input").send_keys(Product_spec_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridspecId')]/input").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品颜色定位
    def Product_gridcolor(self, Product_color_value, row=1):
        location = self.get_column_by_name("颜色")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridcolorId')]/input").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridcolorId')]/input").send_keys(Product_color_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridcolorId')]/input").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品重量定位
    def Product_gridweight(self, Product_weight_value, row=1):
        location = self.get_column_by_name("重量")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridweight')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridweight')]").send_keys(Product_weight_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridweight')]").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品总箱数定位
    def Product_gridcartons(self, Product_cartons_value, row=1):
        location = self.get_column_by_name("总箱数")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridcartons')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridcartons')]").send_keys(Product_cartons_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridcartons')]").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品每箱数量定位
    def Product_grideachCarton(self, Product_eachCarton_value, row=1):
        location = self.get_column_by_name("每箱数量")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_grideachCarton')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_grideachCarton')]").send_keys(Product_eachCarton_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_grideachCarton')]").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品总数量定位
    def Product_griddisplayQty(self, Product_displayQty_value, row=1):
        global displayqty
        location = self.get_column_by_name("总数量")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayQty')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayQty')]").send_keys(Product_displayQty_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayQty')]").send_keys(Keys.ENTER)
        time.sleep(1)
        displayqty = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取总数量
        print("总数量:"+displayqty)
        time.sleep(1)


        #产品单价定位
    def Product_SDprice(self, Product_SDprice_value, row=1):
        location = self.get_column_by_name("单价")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridoriginalPrice')]/input").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridoriginalPrice')]/input").send_keys(Product_SDprice_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridoriginalPrice')]/input").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品折扣定位
    def Product_gridDiscount(self, Product_discount_value, row=1):
        location = self.get_column_by_name("折扣")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddiscount_view')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddiscount_view')]").send_keys(Product_discount_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddiscount_view')]").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品折扣价定位
    def Product_gridunitPrice(self, Product_unitPrice_value, row=1):
        location = self.get_column_by_name("折后价")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridunitPrice')]/input").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridunitPrice')]/input").send_keys(Product_unitPrice_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridunitPrice')]/input").send_keys(Keys.ENTER)
        time.sleep(1)

        # 产品长定位
    def Product_gridlong(self, Product_long_value, row=1):
        location = self.get_column_by_name("长")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridextent')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridextent')]").send_keys(Product_long_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridextent')]").send_keys(Keys.ENTER)
        time.sleep(1)

        # 产品宽定位
    def Product_gridwidth(self, Product_width_value, row=1):
        location = self.get_column_by_name("宽")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridwidth')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridwidth')]").send_keys(Product_width_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridwidth')]").send_keys(Keys.ENTER)
        time.sleep(1)

        # 产品高定位
    def Product_gridheight(self, Product_height_value, row=1):
        location = self.get_column_by_name("高")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridheight')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridheight')]").send_keys(Product_height_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridheight')]").send_keys(Keys.ENTER)
        time.sleep(1)

        # 产品送货数量定位
    def Product_Delivery_quantity(self, row=1):
        location = self.get_column_by_name("送货数量")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayDeldQty')]").clear()
        time.sleep(1)
        deliver = int(displayqty)/2#转换成int计算总数量除于2填写送货数量
        deliver_quantity = str(deliver)#转换成str类型填写
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayDeldQty')]").send_keys(deliver_quantity)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayDeldQty')]").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品本次送货数量定位
    def Product_this_Delivery_quantity(self, row=1):
        location = self.get_column_by_name("本次送货")
        # print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayDelyQtyNow')]").clear()
        time.sleep(1)
        deliver = int(displayqty) / 2  # 转换成int计算总数量除于2填写送货数量
        deliver_quantity = str(deliver)  # 转换成str类型填写
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayDelyQtyNow')]").send_keys(deliver_quantity)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_griddisplayDelyQtyNow')]").send_keys(Keys.ENTER)
        time.sleep(1)

        # 产品备注定位
    def Product_gridremark(self, Product_remark_value, row=1):
        location = self.get_column_by_name("备注")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridremark')]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridremark')]").send_keys(Product_remark_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridremark')]").send_keys(Keys.ENTER)
        time.sleep(1)

        #产品供应商定位
    def Product_gridvendor(self, row=1):
        location = self.get_column_by_name("供应商")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridsupplierId')]/input").send_keys(Keys.DOWN)
        time.sleep(1)
        for i in range(2):
            self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridsupplierId')]/input").send_keys(Keys.ENTER)
        time.sleep(1)

    # 产品进价定位
    def Product_gridPDprice(self,Product_PDprice_value ,row=1):
        location = self.get_column_by_name("进价")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridpurchasePrice')]/input").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridpurchasePrice')]/input").send_keys(Product_PDprice_value)
        time.sleep(1)
        for i in range(2):
            self.driver.find_element(By.XPATH,"//*[contains(@id,'dropdownlistContenttemplateeditor') and contains(@id,'SaleOrder_gridpurchasePrice')]/input").send_keys(Keys.ENTER)
        time.sleep(1)

        #采购箱数
    def Product_gridpurchaseQty(self,  row=1):
        location = self.get_column_by_name("采购箱数")
        #print("//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        purchaseqty = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")#获取采购总数量
        print("自动生成采购箱数:"+purchaseqty)
        if purchaseqty==displayqty:
            print("采购箱数和总数量一致")
        else:
            print("采购箱数不一致:" + purchaseqty+"，手动改为一致")
            self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridpurchaseQty')]").clear()
            time.sleep(1)
            self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridpurchaseQty')]").send_keys(displayqty)
            time.sleep(1)
            self.driver.find_element(By.XPATH,"//*[contains(@id,'textboxeditor') and contains(@id,'SaleOrder_gridpurchaseQty')]").send_keys(Keys.ENTER)
            time.sleep(1)
            editpurchaseqty = self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'SaleOrder_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").get_attribute("innerHTML")  # 获取采购总数量
            print("修改后采购箱数："+editpurchaseqty)


        #产品列表右滑
    def Product_Scroll_bar_right(self):
        for i in range(2):
            self.driver.find_element(By.XPATH,"//*[contains(@id,'jqxScrollAreaDownhorizontalScrollBar') and contains(@id,'SaleOrder_grid')]")


