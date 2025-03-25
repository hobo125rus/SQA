from selenium import webdriver

class BrowserFactory():
    """
    The BrowserFactory class that defines parameters depending on the browser type.
    
    Methods:
    -----------
    set_browser_type: 
        The function analyzes the given browser type and depending on it returns a set of options 
        corresponding to this browser.
    """
    
    def set_browser_type(browser_type):
        if browser_type == 'firefox':
            firefox_options = webdriver.FirefoxOptions()    
            firefox_options.add_argument("--headless")
            return webdriver.Firefox(options=firefox_options)
        elif browser_type == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--allow-insecure-localhost")
            chrome_options.add_argument("--disable-web-security") 
            return webdriver.Chrome(options=chrome_options)
        else:
            safari_options = webdriver.SafariOptions()
            safari_options.accept_insecure_certs = True
            return webdriver.Safari(options=safari_options)

            
     
   
       
