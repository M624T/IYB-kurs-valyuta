from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def get_exchange_rate(url):
    # Brauzer sozlamalari
    options = Options()
    options.add_argument("--headless")  # Brauzerni ko'rinmas rejimda ishga tushirish
    options.add_argument("--disable-gpu")  # GPU akseleratsiyasini o'chirish
    options.add_argument("--no-sandbox")  # Server uchun (zarurat bo'lsa)

    # WebDriverManager yordamida avtomatik chromedriver o'rnatish
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Saytni ochish
        driver.get(url)

        # Valyuta kursini olish
        usd_kurs = driver.find_element(By.XPATH, '/html/body/div/div/div/div[9]/section/div[1]/div/div/div[2]/div/div/article/table/tbody/tr[1]/td[4]').text
        return usd_kurs  # Kursni qaytarish
    finally:
        driver.quit()  # Brauzerni yopish

# Asosiy dastur
if __name__ == "__main__":
    url = "https://ipakyulibank.uz/physical/valyuta-ayirboshlash/kurslar"
    kurs = get_exchange_rate(url)
    print(f"1 USD = {kurs} UZS")
