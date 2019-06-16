from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException



from hover_tests import hover_tests
from scroll_tests import scroll_tests
from click_tests import click_tests
from aspect_tests import aspect_tests
from const import TIME_OUT, CHROME_DRIVER, FIREFOX_DRIVER, URL






def main():
    # my website


    # 
    # 
    # Chrome Tests
    # 
    # 
    try:
        chr_driver = webdriver.Chrome(executable_path="./web_drivers/"+CHROME_DRIVER)
    except WebDriverException:
        print("Driver not found in web_drivers?")

        # gets which website
    chr_driver.get(URL)
    try:
        chr_driver.set_page_load_timeout(TIME_OUT)
    except TimeoutException:
        print("WebPage '"+URL+"' took too much time! (>"+str(TIME_OUT)+")")


    # Tests:
    hover_tests(chr_driver)
    scroll_tests(chr_driver)
    click_tests(chr_driver)
    aspect_tests(chr_driver)

    # Tests for future implimentation:
    #     click all buttons (requires reset)
    #     scrolling down and rapid scrolling
    #     window frame change for UI break?

    chr_driver.close()

    # 
    # 
    # firefox Tests
    # 
    # 
    # fir_driver = webdriver.Firefox(executable_path='./web_drivers/geckodriver')

    # 
    # 
    # int. explor. Tests
    # 
    # 
    # iex_driver = webdriver.Ie()

    # fir_driver.set_page_load_timeout(10)
    # iex_driver.set_page_load_timeout(10)





if __name__ == '__main__':
    main()