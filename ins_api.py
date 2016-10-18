import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.instagram.com/explore/tags/sneakers/'
driver = webdriver.Chrome()
driver.get(url)

img_count = 0
image_divs = None


def scroll():
    global img_count
    global image_divs
    image_divs = driver.find_elements_by_xpath("//a[contains(@href, '/p/')]")
    new_img_count = len(image_divs)
    if img_count == new_img_count:
        return False
    else:
        img_count = new_img_count
    print("image count is: %s" % img_count)
    try:
        loadmore = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a._oidfu"))
        )
        if loadmore:
            loadmore.click()
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.2)
    return True


def get_img_info():
    dialog = driver.find_element_by_xpath("//div[@role='dialog']")
    next_button = dialog.find_element_by_xpath("//a[@role='button' and text()='Next']")
    article = dialog.find_element_by_tag_name('article')
    header = article.find_element_by_tag_name('header')
    header_text = header.find_element_by_xpath("//a[contains(@class, 'notranslate')]")
    print(header_text.text)
    next_button.click()


while img_count < 30:
    if not scroll():
        break

image_divs[0].click()
time.sleep(1)

while img_count > 0:
    get_img_info()
    img_count -= 1
