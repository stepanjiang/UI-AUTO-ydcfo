# -*- coding:utf-8 -*-
"""产品组合信息"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Element_Location.Product_element.product_son_info_new import *
import time

class Product_select_list(Base):
    """获取第一排的div"""
    Product_list =(By.XPATH,"//div[contains(@id,'contentProdGrid')]/div/div/*")
    def get_productlist_name(self,column_name):
        table_column_elements = self.driver.find_elements(*Product_select_list.Product_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)

            """产品列表页面数据"""
    def product_list_name_info(self):
        # 定位产品名称
        location = self.get_productlist_name("名称")
        print("//div[contains(@id,'contenttableProdGrid')]/div[@id='row0ProdGrid']/div[" + str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttableProdGrid')]/div[@id='row0ProdGrid']/div[" + str(location + 1)+ "]/*").click()
        time.sleep(1)

    def product_list_edit(self):
        # 定位产品操作的编辑按钮
        location = self.get_productlist_name("操作")
        print("//div[contains(@id,'contenttableProdGrid')]/div[@id='row0ProdGrid']/div[" + str(location + 1)+ "]/div/a[1]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttableProdGrid')]/div[@id='row0ProdGrid']/div[" + str(location + 1)+ "]/div/a[1]").click()
        time.sleep(1)

    def product_list_delete(self):
        # 定位产品操作的删除禁用按钮
        location = self.get_productlist_name("操作")
        print("//div[contains(@id,'contenttableProdGrid')]/div[@id='row0ProdGrid']/div[" + str(location + 1) + "]/div/a[2]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttableProdGrid')]/div[@id='row0ProdGrid']/div[" + str(location + 1) + "]/div/a[2]").click()
        time.sleep(1)

