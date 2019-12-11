# -*- coding:utf-8 -*-
"""销售单信息列表"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Sales_list(Base):
    """获取第一排的div"""
    Sales_select_list =(By.XPATH,"//div[contains(@id,'columntablesaleOrderGrid')]/*")
    """组合信息的元素定位"""
    def get_column_by_name(self,column_name):
        table_column_elements = self.driver.find_elements(*Sales_list.Sales_select_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)

    """销售单列表数据"""

    # 销售单搜索单号定位并搜索点击
    def sales_list_code(self,row=1):
        location = self.get_column_by_name("单号")
        list_sales_code = self.driver.find_element(By.XPATH, "//*[contains(@id,'contenttablesaleOrderGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/div/*").get_attribute("innerHTML")
        print("搜索到的单号："+list_sales_code)
        time.sleep(1)
        #print("//*[contains(@id,'contenttablesaleOrderGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/div/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttablesaleOrderGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/div/*").click()
        time.sleep(2)
