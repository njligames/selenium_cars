from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

CHROMEDRIVER_PATH = '/Users/jamesfolk/Downloads/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )
driver.get("https://www.ebay.com/sch/Cars-Trucks/6001/i.html?LH_ItemCondition=3000%7C1000%7C2500&_fosrp=1&_fspt=1&_sadis=100&_stpos=11755&LH_PrefLoc=99&_ipg=200&rt=nc")

parentElement = driver.find_element_by_css_selector('ul#ListViewInner')
elementList = parentElement.find_elements_by_xpath("li[@class='sresult lvresult clearfix li']")

i = 0
hrefs = []
while i < len(elementList):
    href = elementList[i].find_element_by_css_selector('h3.lvtitle').find_element_by_css_selector('a.vip').get_attribute('href')
    hrefs.append(href)
    i += 1





# driver.get("https://www.ebay.com/sch/Cars-Trucks/6001/i.html?LH_ItemCondition=3000%7C1000%7C2500&_fosrp=1&_fspt=1&_sadis=100&_stpos=11755&LH_PrefLoc=99&_pgn=2&_skc=200")
# driver.get("https://www.ebay.com/sch/Cars-Trucks/6001/i.html?LH_ItemCondition=3000%7C1000%7C2500&_fosrp=1&_fspt=1&_sadis=100&_stpos=11755&LH_PrefLoc=99&_pgn=3&_skc=400")
# driver.get("https://www.ebay.com/sch/Cars-Trucks/6001/i.html?LH_ItemCondition=3000%7C1000%7C2500&_fosrp=1&_fspt=1&_sadis=100&_stpos=11755&LH_PrefLoc=99&_pgn=4&_skc=600")












print(hrefs)

driver.get_screenshot_as_file("capture.png")
driver.close()

