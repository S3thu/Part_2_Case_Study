from selenium import webdriver


def login_to_linkedin(username, encrypted_password):
    # Create a WebDriver instance
    driver = webdriver.Chrome()  # Adjust the WebDriver based on the browser you are using

    # Navigate to the LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Locate the username and password input fields and submit button
    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    submit_button = driver.find_element_by_css_selector(
        "button[type='submit']")

    # Enter the username and decrypted password into the input fields
    username_field.send_keys(username)
    # Assuming you have a decrypt_password function
    password_field.send_keys(decrypt_password(encrypted_password))

    # Click the submit button to log in
    submit_button.click()

    # Return the WebDriver instance after successful login
    return driver


def get_unread_messages_count(driver):
    # Locate the element that displays the count of unread messages
    messages_element = driver.find_element_by_xpath(
        "//a[@data-test-global-nav-link='messaging']//span")

    # Extract the count value from the element
    messages_count = int(messages_element.text)

    # Return the count of unread messages
    return messages_count


def get_unread_notifications_count(driver):
    # Locate the element that displays the count of unread notifications
    notifications_element = driver.find_element_by_xpath(
        "//a[@data-test-nav-item='notifications']//span")

    # Extract the count value from the element
    notifications_count = int(notifications_element.text)

    # Return the count of unread notifications
    return notifications_count
