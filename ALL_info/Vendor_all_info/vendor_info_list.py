# -*- coding:utf-8 -*-
"""供应商列表信息"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Vendor_select_list(Base):
    """获取第一排的div"""
    vendor_list =(By.XPATH,"//div[contains(@id,'columntablesupplierstable')]/*")
    def get_vendorlist_name(self,column_name):
        table_column_elements = self.driver.find_elements(*Vendor_select_list.vendor_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)

            """供应商列表页面数据"""

        #供应商操作新建销售单定位
    def vendor_list_new_sales(self):
        location = self.get_vendorlist_name("操作")
        print("//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[1]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[1]").click()

        #供应商操作删除定位
    def vendor_list_delete(self):
        location = self.get_vendorlist_name("操作")
        print("//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[2]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[2]").click()

        #供应商操作编辑定位
    def vendor_list_edit(self):
        location = self.get_vendorlist_name("操作")
        print("//div[contains(@id,'contentsupplierstable')]/div[1]/div/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[3]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[3]").click()

        #供应商操作收款定位
    def vendor_list_receivables(self):
        location = self.get_vendorlist_name("操作")
        print("//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[4]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[4]").click()

        #供应商操作送货定位
    def vendor_list_delivery(self):
        location = self.get_vendorlist_name("操作")
        print("//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[5]")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div/a[5]").click()

    def vendor_list_name(self):
        location = self.get_vendorlist_name("供应商名称")
        print("//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablesupplierstable')]/div[@id='row0supplierstable']/div[" + str(location + 1) + "]/div").click()



