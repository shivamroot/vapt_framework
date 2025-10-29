from modules.scanner import scan_target
from modules.sqli_detector import check_sql_injection
from modules.xss_detector import check_xss
from modules.lfi_detector import check_lfi
from utils.report_generator import generate_report

def main():
    print("=== Web Vulnerability Assessment Framework ===")
    target = input("Enter target URL (e.g., http://testphp.vulnweb.com): ").strip()

    results = []
    results.extend(scan_target(target))
    results.extend(check_sql_injection(target))
    results.extend(check_xss(target))
    results.extend(check_lfi(target))

    print("\n[+] Generating Report...")
    generate_report(target, results)
    print("[+] Report saved in /reports/")

if __name__ == "__main__":
    main()
