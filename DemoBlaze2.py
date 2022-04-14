# Do the following tasks. NOTE: You can reuse your code from lab 16
#
# In this lab you will add multiple items to the shopping cart (use suggested names below or any other products on the website)
# and delete only the second item from the cart. Your goal is to figure out how to differentiate one Delete link from another.
#
# Using Selenium WebDriver, open the web browser.
# Maximize the browser window.
# Navigate to web page URL - https://www.demoblaze.com/
# Check URL and title are as expected.
# Add item 1 to your shopping cart:
# On the home page, find the Nexus 6 model and click on it.
# On the product page, check Nexus 6 h2 title is displayed. Use assert.
# Click by Add to Cart button. If you'll see an alert at the top, use this command - driver.switch_to.alert.accept()
# Go to Home Page by clicking the site logo or Home menu item
# Add item 2 to your shopping cart:
# On the home page, find the Sony xperia z5  model and click on it.
# On the product page, check Sony xperia z5 h2 title is displayed. Use assert.
# Click by Add to Cart button. If you'll see an alert at the top, use this command - driver.switch_to.alert.accept()
# Go to Home Page by clicking the site logo or Home menu item
# Add item 3  to your shopping cart:
# On the home page, find the Samsung galaxy s6 (or any other) model and click on it.
# On the product page, check Samsung galaxy s6 h2 title is displayed. Use assert.
# Click by Add to Cart button. If you'll see an alert at the top, use this command - driver.switch_to.alert.accept()
# Go to Cart at the top menu and click on it.
# Check all your added items are displayed and click the Delete link only for the second item in the list.
# Your goal is to figure out how to differentiate one Delete link from another.
# Close the browser and display a user-friendly message.
# Notes:
#
# a) Consider using product list[] and loops for repeatable activities i.e. adding an item to the cart, validating the page title,
# validating items on Cart page.
#
# b) Write your code in lab17_your_name.py file and upload it.


import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # add this import for drop down lists
from selenium.webdriver import Keys

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

app = 'Demoblaze'
demo_homepage_url = 'https://www.demoblaze.com/'
demo_homepage_title = 'STORE'
demo_cartpage_url = 'https://www.demoblaze.com/cart.html'
item_list = ['Nexus 6', 'Sony xperia z5', 'Samsung galaxy s6']
item_url_lst = ['https://www.demoblaze.com/prod.html?idp_=3', 'https://www.demoblaze.com/prod.html?idp_=6', 'https://www.demoblaze.com/prod.html?idp_=1']



def setUp():
    print(f'Launch {app} App')
    print(f'--------------------------------------------------')

    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(demo_homepage_url)
    if driver.current_url == demo_homepage_url and driver.title == demo_homepage_title:
        print('HoHoHo! {app} App website launched successfully!')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Homepage title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print('See you next time!')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

def add_shopping_cart():
    if driver.current_url == demo_homepage_url:
        for i in range(len(item_list)):
            inm, iurl = item_list[i], item_url_lst[i]
            driver.find_element(By.LINK_TEXT, inm).click()
            sleep(0.25)

            if driver.current_url == iurl:
                assert driver.current_url == iurl
                assert driver.find_element(By.XPATH, '//h2[contains(., inm)]').is_displayed()
                sleep(0.25)
                print(f'The product page is located.')
                print(inm + 'is displayed successfully!')
            else:
                print(inm + 'is not displayed. Please check your code.')
            driver.find_element(By.XPATH, '//a[contains(., "Add to cart")]').click()
            sleep(0.25)
            driver.switch_to.alert.accept()
            sleep(0.25)
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(0.25)


def check_cart():
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    sleep(0.25)

    if driver.current_url == demo_cartpage_url:
        print(f'Cart page: {demo_cartpage_url} is located.')
        deletecheck = driver.find_element(By.XPATH, f'//td[contains(., inm)]').is_displayed()
        sleep(0.25)
        print(item_list)
        if deletecheck:
            driver.find_element(By.XPATH, f'//td[contains(., item_list[1])]/../td/a[contains(., "Delete")]').click()
            sleep(0.25)
            print(f'*********The product: {item_list[1]} in the cart is deleted successfully!*********')
    else:
        print(f'The product is not found in cart. Please try again.')


setUp()
add_shopping_cart()
check_cart()
tearDown()