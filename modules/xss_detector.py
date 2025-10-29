import requests
from bs4 import BeautifulSoup
from colorama import Fore

def check_xss(url):
    print(Fore.CYAN + "[*] Checking for Reflected XSS...")
    results = []
    payload = "<script>alert(1)</script>"

    try:
        r = requests.get(f"{url}?q={payload}", timeout=5)
        if payload in r.text:
            print(Fore.RED + f"[!] XSS Found at: {url}")
            results.append({
                "vulnerability": "Reflected XSS",
                "parameter": "q",
                "payload": payload,
                "risk": "Medium",
                "remediation": "Escape HTML characters and use input sanitization."
            })
    except:
        pass

    return results
