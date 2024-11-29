# Valyuta Kurslarini Olish Dasturi
=====================================

Bu Python dasturi selenium kutubxonasidan foydalanib, Ipak Yo'li Bankining valyuta kurslarini olish uchun ishlatiladi. Dasturdan foydalangan holda, kerakli valyuta kursini veb-sahifadan olishingiz mumkin.

## Dastur Tavsifi

Ushbu dastur Ipak Yo'li Bankining rasmiy saytidan (https://ipakyulibank.uz/physical/valyuta-ayirboshlash/kurslar) valyuta kurslarini olish uchun yaratilgan. Dastur headless rejimida ishlaydi, ya'ni brauzer ko‘rinmas tarzda ishlaydi.

## Talablar

Dastur ishlashi uchun quyidagi Python kutubxonalari o‘rnatilgan bo‘lishi kerak:

*   selenium: veb-sahifalarni avtomatlashtirish.
*   webdriver-manager: chromedriverni avtomatik o‘rnatish va boshqarish.

## Kutubxonalarni o‘rnatish

Dastur uchun kerakli kutubxonalarni o‘rnatish uchun quyidagi komandani bajarishingiz kerak:

```bash
pip install selenium webdriver-manager
```

## Dasturdan Foydalanish

### 1. Dasturda URL manzilini o‘rnatish

Dasturda valyuta kurslarini olish uchun kerakli URL manzilini url o'zgaruvchisiga yozib qo‘ying. Misol uchun:

```python
url = "https://ipakyulibank.uz/physical/valyuta-ayirboshlash/kurslar"
```

### 2. Valyuta kursini olish va ekranga chiqarish

Valyuta kursini olish va uni ekranga chiqarish uchun quyidagi kodni ishlatishingiz mumkin:

```python
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Brauzer sozlamalari
options = Options()
options.add_argument("--headless")  # Brauzerni ko'rinmas rejimda ishga tushirish
options.add_argument("--disable-gpu")  # GPU akseleratsiyasini o'chirish
options.add_argument("--no-sandbox")  # Server uchun (zarurat bo'lsa)

# WebDriverManager yordamida avtomatik chromedriver o'rnatish
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL manzilini yozish
url = "https://ipakyulibank.uz/physical/valyuta-ayirboshlash/kurslar"

try:
    # Saytni ochish
    driver.get(url)

    # 1 USD kursini olish
    usd_kurs = driver.find_element(By.XPATH, '/html/body/div/div/div/div[9]/section/div[1]/div/div/div[2]/div/div/article/table/tbody/tr[1]/td[4]').text
    print(f"1 USD = {usd_kurs} UZS")

finally:
    driver.quit()  # Brauzerni yopish
```

### 3. Asosiy dastur

Agar siz dasturdan faqat kursni olishni istasangiz, quyidagi kodni ishga tushirishingiz mumkin:

```python
if __name__ == "__main__":
    url = "https://ipakyulibank.uz/physical/valyuta-ayirboshlash/kurslar"
    # Skriptni ishga tushirish
    kurs = get_exchange_rate(url)
    print(f"1 USD = {kurs} UZS")
```

## Xatoliklarni Tuzatish

*   chromedriverni topa olmayapti: Agar chromedriver to‘g‘ri o‘rnatilmagan bo‘lsa, webdriver-manager kutubxonasidan foydalaning.
*   selenium xatoliklari: seleniumning to‘g‘ri versiyasini o‘rnatganingizga ishonch hosil qiling.

## Qo‘shimcha

Dastur headless rejimida ishlaydi, ya'ni brauzer ko‘rinmas holatda ishlaydi. Bu serverda ishlatish uchun qulaydir.
Agar siz valyuta kurslarini muntazam ravishda olishni xohlasangiz, cron job orqali avtomatlashtirish mumkin.