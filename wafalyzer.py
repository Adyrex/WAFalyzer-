import requests
from colorama import Fore, Style
import pyfiglet

# 🛡️ WAF Header Patterns
waf_headers = {
    "Server": ["cloudflare", "AkamaiGHost", "Sucuri/Cloudproxy", "Barracuda", "Edgecast", "F5 BIG-IP", "Imperva", "Safe3WAF", "AWS WAF", "StackPath"],
    "X-CDN": ["Incapsula", "CloudFront", "Fastly"],
    "X-Sucuri-ID": [],
    "X-Azure-Ref": [],
    "X-Request-ID": [],
    "X-WAF-Detected": [],
    "X-Frame-Options": [],
    "X-Powered-By-360wzb": [],
    "X-Distil-CS": [],
    "X-Mod-Security": [],
    "CF-RAY": [],
    "X-Powered-By-Anquanbao": [],
}

# 💥 Banner
def show_banner():
    banner = pyfiglet.figlet_format("WAFalyzer")
    print(Fore.CYAN + banner + Style.RESET_ALL)
    print(Fore.YELLOW + "[+] WAF Detection Tool by Aditya Kumawat" + Style.RESET_ALL)
    print(Fore.MAGENTA + "    GitHub: https://github.com/adityakumawat2005/WAFalyzer-\n" + Style.RESET_ALL)

# 🔍 Scan Function
def detect_waf(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        detected = []

        for header, values in waf_headers.items():
            if header in headers:
                header_value = headers[header].lower()
                if not values:  # just presence check
                    detected.append(header)
                else:
                    for value in values:
                        if value.lower() in header_value:
                            detected.append(f"{header} → {value}")
                            break

        if detected:
            print(Fore.GREEN + f"[✓] WAF Detected at {url}!" + Style.RESET_ALL)
            for d in detected:
                print(Fore.LIGHTGREEN_EX + f" └── {d}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"[x] No known WAF detected at {url}." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}" + Style.RESET_ALL)

# 🚀 Main
if __name__ == "__main__":
    show_banner()
    target = input(Fore.BLUE + "[?] Enter target URL (with http/https): " + Style.RESET_ALL)
    detect_waf(target)
