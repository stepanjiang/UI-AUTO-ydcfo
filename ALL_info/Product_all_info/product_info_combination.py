# -*- coding:utf-8 -*-
"""产品组合信息"""
from common.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Element_Location.Product_element.product_son_info_new import *
import time

class Product_combination(Base):
    """获取第一排的div"""
    Product_dimension_list =(By.XPATH,"//div[contains(@id,'columntable') and contains(@id,'childProductGrid')]/*")
    product_choose_input = (By.XPATH, "//input[@placeholder='请输入或选择产品']")
    save_button = (By.XPATH,'//*[@id="photoModal_saveBtn"]')
    def get_column_by_name(self,column_name):
        table_column_elements = self.driver.find_elements(*Product_combination.Product_dimension_list)
        for table_column_element in table_column_elements:
            if table_column_element.text == column_name:
                return table_column_elements.index(table_column_element)


        """组合信息子产品填写"""

    def set_product_son_name(self, product_son_name, row=1):  # 设置子产品名称
        column = self.get_column_by_name('子产品')
        self.driver.find_element(By.XPATH,"//*[contains(@id, 'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(column + 1) + "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id, 'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(column + 1) + "]/*").click()
        self.driver.find_element(*Product_combination.product_choose_input).clear()
        time.sleep(1)
        self.driver.find_element(*Product_combination.product_choose_input).send_keys(product_son_name)
        time.sleep(1)
        for i in range(2):
            self.driver.find_element(*Product_combination.product_choose_input).send_keys(Keys.ENTER)
            time.sleep(2)
        time.sleep(2)

    def combination_picture(self,  row = 1):
        location =self.get_column_by_name("图片")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(2)
        Product_combination_location(self.driver).set_picture_son()
        time.sleep(1)
        self.driver.find_element(*Product_combination.save_button).click()
        time.sleep(1)

    def set_product_son_rate(self,rate_value,row = 1):
        location =self.get_column_by_name("组合比例")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(rate_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_weight(self,weight_value,row = 1):
        location =self.get_column_by_name("重量")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(weight_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_qtynumber(self,qtynumber_value,row = 1):
        location =self.get_column_by_name("每箱数量")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(qtynumber_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_price1(self,price1_value,row = 1):
        location =self.get_column_by_name("每箱数量")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(price1_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_price2(self,price2_value,row = 1):
        location =self.get_column_by_name("售价2")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(price2_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_purchase_price1(self,purchase_price1_value,row = 1):
        location =self.get_column_by_name("进价1")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(purchase_price1_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_purchase_price2(self,purchase_price2_value,row = 1):
        location =self.get_column_by_name("进价2")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(purchase_price2_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_purchase_long(self,long_value,row = 1):
        location =self.get_column_by_name("长")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(long_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_purchase_wide(self,wide_value,row = 1):
        location =self.get_column_by_name("宽")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(wide_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_high(self,high_value,row = 1):
        location =self.get_column_by_name("高")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(high_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_loss(self,loss_value,row = 1):
        location =self.get_column_by_name("损耗率")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(loss_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_remark(self,remark_value,row = 1):
        location =self.get_column_by_name("备注")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/*").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(remark_value)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/*").send_keys(Keys.ENTER)
        time.sleep(1)

    def set_product_son_delete_bank(self,row = 1):
        location =self.get_column_by_name("操作")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/div/a[1]")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/div/a[3]").click()
        time.sleep(1)

    def set_product_son_copy_bank(self,row = 1):
        location =self.get_column_by_name("操作")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/div/a[2]")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/div/a[2]").click()
        time.sleep(1)

    def set_product_son_new_bank(self,row = 1):
        location =self.get_column_by_name("操作")
        print("//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1)+"')]/div["+str(location + 1)+ "]/div/a[3]")
        self.driver.find_element(By.XPATH,"//*[contains(@id,'contenttable') and contains(@id,'childProductGrid')]/div[contains(@id,'row" + str(row - 1) + "')]/div[" + str(location + 1) + "]/div/a[3]").click()
        time.sleep(1)

