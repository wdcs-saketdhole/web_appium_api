from selenium import webdriver


def get_browser(browser_name):
    if browser_name == 'chrome':
        return webdriver.Chrome()
    elif browser_name == 'firefox':
        return webdriver.Firefox()
    elif browser_name == 'safari':
        return webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

