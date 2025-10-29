import requests
from colorama import Fore

payloads = ["' OR '1'='1", '" OR "1"="1', "' UNION SELECT NULL--"]

def check_sql_injection(url):
    print(Fore.CYAN + "[*] Checking for SQL Injection...")
    results = []

    for payload in payloads:
        try:
            test_url = f"{url}?id={payload}"
            r = requests.get(test_url, timeout=5)
            if any(err in r.text.lower() for err in ["sql", "syntax", "mysql", "odbc"]):
                print(Fore.RED + f"[!] SQLi Found: {test_url}")
                results.append({
                    "vulnerability": "SQL Injection",
                    "parameter": "id",
                    "payload": payload,
                    "risk": "High",
                    "remediation": "Use prepared statements and parameterized queries."
                })
        except:
            pass

    return results
