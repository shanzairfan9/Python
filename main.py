from selenium import webdriver


def browser():
    driver = webdriver.Chrome(executable_path='../chromeDriver/chromedriver.exe')
    driver.get("https://pulse.10pearls.com/#/login")
    page_title = driver.title
    print(page_title)
    assert "Pulse - 10Pearls" in page_title
    driver.quit()


if __name__ == '__main__':
    browser()
