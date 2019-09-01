import subprocess
p=subprocess.Popen( [r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",r"C:\Users\Tsinghua-yincheng\Desktop\SZday8\seleniumTest\4.png","last"],
                    stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
file=open("last.txt","r")
print(file.read())