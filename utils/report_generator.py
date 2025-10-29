from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

def generate_report(target, results):
    c = canvas.Canvas(f"reports/{target.replace('http://','').replace('/','_')}_report.pdf", pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, f"Vulnerability Assessment Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, f"Target: {target}")
    c.drawString(50, 760, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

    y = 740
    for res in results:
        c.drawString(50, y, f"[{res['vulnerability']}] Risk: {res['risk']}")
        y -= 20
        c.drawString(60, y, f"Parameter: {res['parameter']}")
        y -= 20
        c.drawString(60, y, f"Payload: {res['payload']}")
        y -= 20
        c.drawString(60, y, f"Remediation: {res['remediation']}")
        y -= 30
        if y < 100:
            c.showPage()
            y = 800

    c.save()
