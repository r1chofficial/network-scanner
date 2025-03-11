# 🌐 Ağ Tarama ve Anomali Tespiti Projesi

Bu proje, bağlı olduğunuz ağdaki tüm cihazları tarayan ve anomali tespiti yapan bir Python scriptidir. Ağ güvenliği, izleme ve yönetim süreçlerinde kullanılabilir.

---

## 🚀 Özellikler

- **Ağ Tarama:** Bağlı olduğunuz ağdaki tüm cihazları tespit eder.
- **Anomali Tespiti:** Ağ trafiğindeki olağandışı davranışları belirler.
- **Kullanıcı Dostu:** Kolay kurulum ve kullanım.
- **Detaylı Raporlama:** Tarama sonuçlarını görselleştirir.

---

## 🛠️ Nasıl Çalışır?

Proje, `nmap` kütüphanesini kullanarak ağdaki cihazları tarar. Anomaliler, gönderilen byte miktarına göre tespit edilir. Tarama sonuçları, kullanıcıya detaylı bir şekilde sunulur.

---

## 📦 Kurulum

Projeyi kullanmak için aşağıdaki adımları takip edin:

1. **Python'u Kurun:**
   - [Python 3.x](https://www.python.org/downloads/)'i indirin ve kurun.

2. **Gerekli Kütüphaneleri Yükleyin:**
   ```bash
   pip install python-nmap
