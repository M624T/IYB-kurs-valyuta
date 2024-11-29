from selenium import webdriver
from selenium.webdriver.common.by import By  # By klassini import qilish
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Brauzer sozlamalari
options = Options()
options.add_argument("--headless")  # Brauzerni ko'rinmas rejimda ishga tushirish
options.add_argument("--disable-gpu")  # GPU akseleratsiyasini o'chirish
options.add_argument("--no-sandbox")  # Server uchun (zarurat bo'lsa)

# WebDriverManager yordamida avtomatik yuklash
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Sahifani ochish
    url = "https://ipakyulibank.uz/physical/valyuta-ayirboshlash/kurslar"
    driver.get(url)

    # Valyuta kursini topish
    usd_kurs = driver.find_element(By.XPATH, '/html/body/div/div/div/div[9]/section/div[1]/div/div/div[2]/div/div/article/table/tbody/tr[1]/td[4]').text
    print(f"1 USD = {usd_kurs} UZS")
finally:
    driver.quit()  # Brauzerni yopish
