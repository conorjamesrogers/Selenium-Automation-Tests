from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import random





def wheel_element(element, deltaY = 120, offsetX = 0, offsetY = 0):
    error = element._parent.execute_script("""
        var element = arguments[0];
        var deltaY = arguments[1];
        var box = element.getBoundingClientRect();
        var clientX = box.left + (arguments[2] || box.width / 2);
        var clientY = box.top + (arguments[3] || box.height / 2);
        var target = element.ownerDocument.elementFromPoint(clientX, clientY);

        for (var e = target; e; e = e.parentElement) {
          if (e === element) {
            target.dispatchEvent(new MouseEvent('mouseover', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
            target.dispatchEvent(new MouseEvent('mousemove', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
            target.dispatchEvent(new WheelEvent('wheel',     {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY, deltaY: deltaY}));
            return;
          }
        }    
        return "Element is not interactable";
        """, element, deltaY, offsetX, offsetY)
    if error:
        raise WebDriverException(error)

# Big Scrolling-- can be tricky due to use of 'scroll magic' library
def scroll_tests(driver):
    print("scroll test")
    try:
        # box_list = driver.find_elements(By.)

        # page = driver.find_element_by_id("section-web")
        # page.send_keys(Keys.PAGE_DOWN)

        # wheel_element(page, -1000)

        # e=driver.execute_script("window.scrollBy(0,-1000)")

        scroll_height = driver.execute_script("return document.body.scrollHeight")
        scroll_height_red = scroll_height/50
        # print(scroll_height)

        # silly for loop just for my own visual that it's scrolling
        for i in range(1,49):
            driver.execute_script("scrollBy(0,"+str(scroll_height_red)+")")
            time.sleep(.05)

        for i in range(1,49):
            driver.execute_script("scrollBy(0,(-1*"+str(scroll_height_red)+"))")
            time.sleep(.05)

        print("erratic scroll test")

        for i in range(1,49):
            random_int = random.randint(-400,500)
            driver.execute_script("scrollBy(0,"+str(random_int)+")")
            time.sleep(.05)



        # element = driver.find_element(By.XPATH,"//*[@id='portfolio'")
        # scroll_actions = ActionChains(driver)
        # scroll_actions.move_to_element(element).perform()

        
    except:
        raise WebDriverException()
        # print("scroll except")
        driver.close()
   







    # driver.close() 

