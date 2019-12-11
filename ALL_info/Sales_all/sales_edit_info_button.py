# -*- coding:utf-8 -*-
"""销售单详情页面按钮"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Sales_info_button(Base):
    """销售单详情页面按钮"""
    edit_button = (By.XPATH, "//div[contains(@id,'viewsale')]/button[contains(@id,'viewSO-editBtn')]")#编辑按钮
    copy_button = (By.XPATH, "//div[contains(@id,'viewsale')]/button[contains(@id,'viewSO-copyBtn')]")  # 复制新增单据按钮
    def sales_edit_button(self):
        self.driver.find_element(*Sales_info_button.edit_button).click()#点击编辑按钮
        time.sleep(5)

    def sales_copy_button(self):
        self.driver.find_element(*Sales_info_button.copy_button).click()#点击复制新增单据按钮
        time.sleep(3)

