# main.py
import requests
from modules.scanner import scan_target
from modules.sqli_detector import check_sql_injection
from modules.xss_detector import check_xss
from utils.report_generator import generate_report

def main():
    print("=== Web Vulnerability Assessment Framework ===")
    target = input("Enter target URL (e.g., http://testphp.vulnweb.com): ").strip()
    s = requests.Session()
    results = []

    # Basic info gathering (keeps previous behavior)
    results.extend(scan_target(target, session=s) if 'scan_target' in globals() else scan_target(target))
    # SQLi & XSS checks (form-aware)
    results.extend(check_sql_injection(s, target))
    results.extend(check_xss(s, target))

    generate_report(target, results)

if __name__ == "__main__":
    main()
