import sys
try:
    import PyPDF2
except Exception as e:
    print('MISSING_PYPDF2')
    sys.exit(2)
from pathlib import Path
p = Path(r"C:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\learn-edu\Class_5_Mathematics_English_Medium-Term_3-2024_Edition-www.tntextbooks.in.pdf")
if not p.exists():
    print('MISSING_PDF')
    sys.exit(3)
text = []
with open(p,'rb') as f:
    reader = PyPDF2.PdfReader(f)
    for i,page in enumerate(reader.pages, start=1):
        try:
            t = page.extract_text() or ''
        except Exception as e:
            t = ''
        print(f'--PAGE-START--{i}--')
        print(t)
        print(f'--PAGE-END--{i}--')

