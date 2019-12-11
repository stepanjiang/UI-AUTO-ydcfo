# -*- coding:utf-8 -*-
"""客户列表信息"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Cost_select_list(Base):
    """获取第一排的div"""
    customer_list =(By.XPATH,"//div[contains(@id,'columntablecostIncomeGrid')]/*")
    def get_cost_list(self,column_name):
        table_column_elements = self.driver.find_elements(*Cost_select_list.customer_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)

    def cost_list_code(self):
        location = self.get_cost_list("单号")
        print("//div[contains(@id,'contenttablecostIncomeGrid')]/div[@id='row0costIncomeGrid']/div[" + str(location + 1) + "]/div/a")
        self.driver.find_element(By.XPATH,"//div[contains(@id,'contenttablecostIncomeGrid')]/div[@id='row0costIncomeGrid']/div[" + str(location + 1) + "]/div/a").click()
        time.sleep(2)
