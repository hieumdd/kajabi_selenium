from selenium import webdriver

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument('--no-sandbox')
CHROME_OPTIONS.add_argument('--window-size=1920,1080')
CHROME_OPTIONS.add_argument('--headless')
CHROME_OPTIONS.add_argument('--disable-gpu')
DRIVER = webdriver.Chrome(chrome_options=CHROME_OPTIONS)


def main(request):
    DRIVER.get('https://google.com')
    DRIVER.save_screenshot('data/test.png')
    DRIVER.quit()
    return "ok"
