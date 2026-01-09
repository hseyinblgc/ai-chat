Readme is now behind the repo and need to be updated

## open-cli

open-cli, Google GenAI SDK (google-genai) kullanarak sorular gönderip yanıt alabileceğiniz bir Python Qt (PySide6) masaüstü uygulamasıdır.

### Özellikler

- Google Gemini 2.5 Flash modeli ile doğal dil işleme.
- Sohbet balonları içeren modern ve kullanıcı dostu arayüz.
- Kullanıcı ve yapay zeka mesajları için farklı hizalama ve renklendirme.

### Gereksinimler

- Python 3.8 veya üzeri
- pip
- İnternet bağlantısı ve geçerli bir Google GenAI API anahtarı

### Kurulum

1.  (İsteğe bağlı) Sanal ortam oluşturun ve etkinleştirin:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    ```

    Windows PowerShell için:

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

2.  Gerekli paketleri yükleyin:

    ```bash
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```

### API Anahtarı Ayarlama

`reply.py` dosyasındaki `YOUR_API_KEY_HERE` kısmını Google AI Studio'dan aldığınız API anahtarı ile değiştirin:

```python
apikey = genai.Client(api_key="YOUR_API_KEY_HERE")
```

### Çalıştırma

API anahtarını ayarladıktan sonra proje dizininde çalıştırın:

```bash
python main.py
```

- Metin giriş alanına sorunuzu yazın ve "Gönder" butonuna tıklayın veya Enter'a basın.
- Cevaplar sohbet ekranında görünecektir.

### Teknik Detaylar

- **UI Framework:** PySide6 (Qt for Python)
- **AI Modeli:** Google Gemini 2.5 Flash

### Sorun Giderme

- **Uygulama başlamıyorsa:** `PySide6`'nın doğru kurulduğundan emin olun.
- **API hatası alıyorsanız:** API anahtarınızın geçerli ve internet bağlantınızın aktif olduğunu kontrol edin.

![Preview](screenshot/image.png)