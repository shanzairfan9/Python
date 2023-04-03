from selenium import webdriver
import Rating


def browser():
    driver = webdriver.Chrome(executable_path='../chromeDriver/chromedriver.exe')
    driver.get("https://pulse.10pearls.com/#/login")
    page_title = driver.title
    print(page_title)
    assert "Pulse - 10Pearls" in page_title
    driver.quit()


if __name__ == '__main__':
    userinput = float(input("Enter rating between 0 to 5: "))
    obj = Rating(22)

