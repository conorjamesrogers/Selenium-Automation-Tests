from selenium import webdriver
from hover_tests import hover_tests
from scroll_tests import scroll_tests



def main():
    url = "https://conorjamesrogers.github.io/"
    # 
    # 
    # Chrome Tests
    # 
    # 
    chr_driver = webdriver.Chrome(executable_path='./web_drivers/chromedriver74')

    # gets which website (my website)
    chr_driver.get(url)
    chr_driver.set_page_load_timeout(10)

    # Tests:
    hover_tests(chr_driver)
    scroll_tests(chr_driver)

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