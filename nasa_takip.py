import time
import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot

# TELEGRAM BİLGİLERİN
TELEGRAM_TOKEN = "...."
CHAT_ID = "...."

# TAKİP EDİLECEK NASA LİNKİ
URL = "https://stemgateway.nasa.gov/s/course-offering/a0BSJ0000049ih3/open-science-101"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

async def send_telegram_msg(text):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=text)

def check_nasa():
    try:
        response = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text().lower()
        
        # Sayfada kayıt/başvuru kelimeleri veya buton değişimi taranır
        if "apply" in page_text or "register" in page_text:
            return True
        return False
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return False

async def main():
    print("NASA Takip Sistemi Başlatıldı! Sayfa kontrol ediliyor...")
    await send_telegram_msg("NASA Open Science 101 takip botu çalışmaya başladı! Kayıtlar açılınca bildirim göndereceğim.")
    
    while True:
        if check_nasa():
            msg = f"ALERT! NASA Open Science 101 kayıtları açılmış olabilir!\nHemen kontrol et: {URL}"
            print(msg)
            await send_telegram_msg(msg)
            break # Bildirim attıktan sonra durur
        
        print("Kayıtlar henüz açılmamış, 10 dakika sonra tekrar bakılacak...")
        await asyncio.sleep(600) # 600 saniye (10 dakika) bekler

if __name__ == "__main__":
    asyncio.run(main())
