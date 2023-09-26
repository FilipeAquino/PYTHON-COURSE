# type: ignore
from pathlib import Path
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: List[str]) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 50

    options = ()
    browser = make_chrome_browser(*options)

    browser.get("https://sigs.ufrpe.br/sigaa/verTelaLogin.do")
    browser.maximize_window()

    nome = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'user.login')
            )
        )

    password = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'user.senha')
            )
        )
    nome.send_keys('filipe.aquino')
    password.send_keys("Filipe11")
    # sing
    browser.find_element(By.XPATH, '//*[@id="conteudo"]/div[4]/form/table/'
                         'tfoot/tr/td/input').click()

    res = input("qualquer coisa: ")
