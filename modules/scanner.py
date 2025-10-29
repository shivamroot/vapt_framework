
import requests
from colorama import Fore

def scan_target(url):
    print(Fore.CYAN + "[*] Gathering target info...")
    results = []

    try:
        r = requests.get(url, timeout=5)
        headers = r.headers
        tech_stack = headers.get('Server', 'Unknown')
        print(Fore.GREEN + f"[+] Server Technology: {tech_stack}")

        results.append({
            "vulnerability": "Info Gathering",
            "parameter": "N/A",
            "payload": "N/A",
            "risk": "Low",
            "remediation": f"Server reveals technology: {tech_stack}"
        })

    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")

    return results
