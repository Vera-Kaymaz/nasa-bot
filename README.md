# nasa-bot
NASA Open Science 101 course follow bot system
# 🚀 NASA Open Science 101 - Registration Tracker & Bot

Bu proje, **NASA Open Science 101** kursunun kayıt ("Apply / Register") butonunun aktifleştiğini anlık olarak takip etmek ve bildirim almak amacıyla başlatılmış bir otomasyon çalışmasıdır.

🔗 **Takip Edilen Sayfa:** [NASA STEM Gateway - Open Science 101](https://stemgateway.nasa.gov/s/course-offering/a0BSJ0000049ih3/open-science-101)

---

## 🛠️ Denenen Yöntemler ve Karşılaşılan Süreçler

Kayıtları kaçırmamak adına süreç boyunca 4 farklı yöntem denenmiş ve tecrübe edilmiştir:

### 1. Yerel Python Scripti + Telegram Botu (Lokal Çalıştırma)
* **Yöntem:** Python (`requests`, `BeautifulSoup`, `python-telegram-bot`) kullanılarak sayfa içeriğini tarayan ve buton aktifleştiğinde kişisel Telegram hesabıma bildirim atan bir bot yazıldı.
* **Sonuç:** Kod başarıyla çalıştı ve Telegram entegrasyonu sağlandı. Ancak scriptin çalışması için kişisel bilgisayarın 7/24 açık kalması gerekiyordu.

### 2. PythonAnywhere (Bulut Sunucu)
* **Yöntem:** Bilgisayar kapalıyken de takibin sürmesi için kod PythonAnywhere üzerine taşındı.
* **Sonuç / Engel:** Platformun ücretsiz planında (Free Tier) *Always-on Tasks* ve *Scheduled Tasks* özelliklerinin kısıtlanmış/ücretli olması sebebiyle 7/24 kesintisiz çalıştırma hedefine ulaşılamadı.

### 3. Render.com (Background Worker)
* **Yöntem:** Kodu Dockerize ederek (`Dockerfile` ve `requirements.txt` eklenerek) Render altyapısında 7/24 ücretsiz bir Background Worker olarak çalıştırmak hedeflendi.
* **Sonuç / Engel:** Güncel platform politikaları nedeniyle ücretsiz plan kısıtlamalarına takılındı.

### 4. Telegram Web Alert Botları (Nihai Çözüm) 💡
* **Yöntem:** Sunucu ve altyapı kısıtlamalarını aşmak adına doğrudan Telegram ekosistemindeki hazır web izleme servisleri (`@VisualPingBot` / `@WebpageChangesBot`) devreye sokuldu.
* **Sonuç:** NASA'nın kayıt sayfası ilgili bota tanımlandı. Sayfadaki DOM/metin değişikliklerini arka planda sıfır maliyetle izleyen ve değişiklik anında anlık bildirim atan sistem başarıyla kuruldu.

---

## 📌 Özet ve Kazanımlar
Bu süreçte:
- Python ile web scraping ve Telegram Bot API entegrasyonu deneyimlendi.
- Asenkron programlama (`asyncio`) ve hata yönetimi uygulandı.
- Bulut sunucuların (PythonAnywhere, Render) güncel ücretsiz plan kısıtlamaları ve Docker konfigürasyonları tecrübe edildi.
- Karşılaşılan altyapı engellerine karşı alternatif, pratik ve sürdürülebilir çözümler üretildi.
