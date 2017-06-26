from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("./chromedriver")
driver.get("http://digikala.com")
productItems = driver.find_elements_by_css_selector(".productItem")
result = open("result.txt",'w')
for i in productItems:
    try:
        oldPrice = i.find_element_by_css_selector(".old-price").get_attribute("innerHTML").split('<', 1)[0]
        finalPrice =  i.find_element_by_css_selector(".final-price").get_attribute("innerHTML").split('<', 1)[0]
        href = i.get_attribute("href")
        result.write('{:<11}  {:<11}  {:<100}'.format(oldPrice,finalPrice,href)+'\n')
    except NoSuchElementException:
        pass
result.close()
driver.quit()
