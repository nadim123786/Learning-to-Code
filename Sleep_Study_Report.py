from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("C:\Windows\System32\sleepstudy-report.html")

rows = driver.find_elements_by_xpath("//*[@id='summary-table']/tbody/tr")
a = (len(rows))
for i in range (1,a):
    states = driver.find_element_by_xpath("//*[@id='summary-table']/tbody/tr[{}]/td[4]".format(i)).text
    if "Abnormal Shutdown" in states:
        driver.find_element_by_xpath("//*[@id='summary-table']/tbody/tr[{}]/td[4]".format(i)).click()
        driver.find_element_by_xpath("/html/body/a[{}]/div[3]/h1".format(i)).click()
        table_rows = len(driver.find_elements_by_xpath("/html/body/a[4]/div[3]/div/table/tbody/tr"))
        table_cols = len(driver.find_elements_by_xpath("/html/body/a[4]/div[3]/div/table/tbody/tr[1]/td"))
        for r in range(1,table_rows+1):
            for c in range(1,table_cols+1):
                value = driver.find_element_by_xpath("/html/body/a[4]/div[3]/div/table/tbody/tr[{}]/td[{}]".format(r,c)).text
                print(value,end="       ")
            print()