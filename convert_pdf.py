#Assumes you have blog.alivate.com.au/poppler-windows for windows binaries
#for linux search poppler utils on apt-get
#for mac look into brew - but there is a weird dependency issue
from subprocess import call
import sys

def convert(pdf):
    call(["pdftotext","-layout",pdf])

def clean(name_text):
    to_parse = []
    with open(name_text) as f:
        for line in f:
            line = line.decode("ascii","ignore")
            line = line.replace("\n","")
            line = line.replace("\t","")
            if line != '':
                to_parse.append(line)
    return to_parse

def main(pdf=None):
    if pdf==None:
        pdf = sys.argv[1]
    name_text = pdf.split(".")[0]+".txt"
    if not os.path.exists(name_text):
        convert(pdf)
    cleaned = clean(name_text)
    with open(name_text,"w") as f:
        for line in cleaned:
            f.write(line)
