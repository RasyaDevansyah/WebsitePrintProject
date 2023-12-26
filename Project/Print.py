import os
import subprocess
import win32print
import win32com.client
import sys

#modify printer name and sumatra exe path here
#You must have microsoft word installed
printer_name = win32print.GetDefaultPrinter()
sumatra_EXE_path = 'C:\\Users\\USER\\AppData\\Local\\SumatraPDF\\SumatraPDF.exe'
save_the_files = True


#You can input with either an absolute path to the document "C:\Users\USER\documents\..." 
#or relative path to this folder "uploads\filename.pdf"
if len(sys.argv) == 1:
    print("Usage: python Print.py <file_path>")
    sys.exit(1)
file_to_print = sys.argv[1]


def print_pdf(file_path, printer_name):
    subprocess.run([sumatra_EXE_path, '-print-to', printer_name, file_path], shell=True)

def print_docx(file_path, printer_name):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False

    full_path = file_path if os.path.isabs(file_path) else os.path.join(os.getcwd(), file_path)

    if os.path.exists(full_path):
        doc = word.Documents.Open(full_path)

        word.Application.ActivePrinter = printer_name
        doc.PrintOut()
        doc.Close()
        word.Quit()
    else:
        print(f"File not found: {full_path}")

file_extension = file_to_print.split('.')[-1].lower()
if file_extension == 'pdf' or file_extension == 'txt' or file_extension == 'PDF':
    print_pdf(file_to_print, printer_name)
elif file_extension == 'docx' or file_extension =='doc':
    print_docx(file_to_print, printer_name)
else:
    print(f"Unsupported file type: {file_extension}")

if(save_the_files == False):
    os.remove(file_to_print)
