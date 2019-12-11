# -*- coding:utf-8 -*-
"""客户列表信息"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Customer_select_list(Base):
    """获取第一排的div"""
    customer_list =(By.XPATH,"//div[contains(@id,'columntablecustomerBizMgttable')]/*")
    def get_customerlist_name(self,column_name):
        table_column_elements = self.driver.find_elements(*Customer_select_list.customer_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)

            """客户列表页面数据"""

        #客户操作新建销售单定位
    def customer_list_new_sales(self):
        location = self.get_customerlist_name("操作")
        print("//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[1]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[1]").click()
        time.sleep(1)

        #客户操作删除定位
    def customer_list_delete(self):
        location = self.get_customerlist_name("操作")
        print("//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[2]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[2]").click()
        time.sleep(1)

        #客户操作编辑定位
    def customer_list_edit(self):
        location = self.get_customerlist_name("操作")
        print("//div[contains(@id,'contentcustomerBizMgttable')]/div[1]/div/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[3]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[3]").click()
        time.sleep(1)

        #客户操作收款定位
    def customer_list_receivables(self):
        location = self.get_customerlist_name("操作")
        print("//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[4]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[4]").click()
        time.sleep(1)

        #客户操作送货定位
    def customer_list_delivery(self):
        location = self.get_customerlist_name("操作")
        print("//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[5]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div/a[5]").click()
        time.sleep(1)

        #客户名称定为
    def customer_list_name(self):
        location = self.get_customerlist_name("客户名称")
        print("//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablecustomerBizMgttable')]/div[@id='row0customerBizMgttable']/div[" + str(location + 1) + "]/div").click()
        time.sleep(1)



