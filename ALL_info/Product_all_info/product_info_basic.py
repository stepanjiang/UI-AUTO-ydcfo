# -*- coding:utf-8 -*-
"""产品信息维度表"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Product_dimension(Base):
    """获取第一排的div"""
    Product_dimension_list =(By.XPATH,"//div[contains(@id,'columntable') and contains(@id,'prod_grid')]/*")
    """组合信息的元素定位"""
    new_product_combination = (By.XPATH,'//*[@id="add"]')#新建页面切换组合信息窗口
    edit_prroduct_combination = (By.XPATH,'//*[@id="edit-combineMessage"]')#编辑页面切换组合信息窗口
    def get_column_by_name(self,column_name):
        table_column_elements = self.driver.find_elements(*Product_dimension.Product_dimension_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)


        """产品页面维度数据填写"""
        #定位期初库存
    def initial_inventory(self, initial_inventory_value, row = 1):
        location =self.get_column_by_name("期初库存")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").send_keys(initial_inventory_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位库存上限
    def inventory_top(self,inventory_top_value, row = 1):
        location = self.get_column_by_name("库存上限")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(inventory_top_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位库存下限
    def inventory_down(self,inventory_down_value, row = 1):
        location = self.get_column_by_name("库存下限")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(inventory_down_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位每箱数量
    def Quantity_box(self,quantity_box_value, row = 1):
        location = self.get_column_by_name("每箱数量")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(quantity_box_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位长
    def long(self,long_value, row = 1):
        location = self.get_column_by_name("长")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(long_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位宽
    def wide(self,wide_value, row = 1):
        location = self.get_column_by_name("宽")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(wide_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位高
    def high(self,high_value, row = 1):
        location = self.get_column_by_name("高")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(high_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位售价1
    def price1(self,price_value1, row = 1):
        location = self.get_column_by_name("售价1")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(price_value1)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位售价2
    def price2(self,price_value2, row = 1):
        location = self.get_column_by_name("售价2")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(price_value2)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位进价1
    def purchase_price1(self,Purchase_value1, row = 1):
        location = self.get_column_by_name("进价1")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Purchase_value1)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #定位进价2
    def purchase_price2(self,Purchase_value2, row = 1):
        location = self.get_column_by_name("进价2")
        print("//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Purchase_value2)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'prod_grid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

        #切换组合信息
    def new_switch_combination(self):
        self.driver.find_element(*Product_dimension.new_product_combination).click()  # 新增切换组合信息
        time.sleep(1)

    def edit_switch_combination(self):
        self.driver.find_element(*Product_dimension.edit_prroduct_combination).click() #修改切换组合信息
        time.sleep(1)











