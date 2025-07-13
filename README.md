# 🛡️ WAFalyzer

**WAFalyzer** is a Python-based tool that helps identify Web Application Firewalls (WAFs) by analyzing HTTP response headers. It gives cool hacker-style output and is beginner-friendly!

![banner](https://i.imgur.com/2o6Z8XN.png)

---

## ⚙️ Features

- Detects popular WAFs like Cloudflare, Akamai, AWS WAF, etc.
- Clean and colorful output
- Beginner friendly, easy to run

---

## 🚀 Installation

### 🔻 Clone the repo:
```bash
git clone https://github.com/adityakumawat2005/WAFalyzer.git
cd WAFalyzer

💾 Install dependencies:

# For Kali/Linux users:
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

🧪 Usage

python wafalyzer.py
Then enter a target URL (with http/https). Example:
https://example.com


🧠 How It Works
It scans for the following headers and values:

Server: Cloudflare, Sucuri, AkamaiGHost, etc.

X-CDN: Incapsula, CloudFront, Fastly, etc.

X-Sucuri-ID, X-Mod-Security, CF-RAY, etc.

👨‍💻 Author
Made with ❤️ by Aditya Kumawat


⚠️ Disclaimer
This tool is for educational & ethical use only.
