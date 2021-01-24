import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PSI20_URL = (
    "https://live.euronext.com/popout-page/getIndexComposition/PTING0200002-XLIS"
)

TABLE_ID = "AwlIndexCompositionTable"

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(PSI20_URL)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, TABLE_ID))
        )

        table = element.get_attribute("outerHTML")

        df = pd.read_html(table)[0]
        df.to_csv("data/psi_20.csv", index=False)
    finally:
        driver.quit()
