from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
import os, sys, datetime
import random
import csv
from tkinter import Tk, Label, filedialog, Button, messagebox
import threading


# current time
currentDateTime = datetime.datetime.now()
currenthour = currentDateTime.hour
currentminute = currentDateTime.minute
currentday = currentDateTime.day
currentyear = currentDateTime.year
currentmonth = currentDateTime.strftime("%b") 

def main():
    # log path in same directory
    getpwd = os.getcwd()
    gpwd = getpwd.replace('\\','/')
    logname = f'/encrypted logs/{currentday}-{currentmonth}-{currentyear}'
    logpath = gpwd + logname
    if not os.path.exists(logpath):
        os.makedirs(logpath)

    labelstatus.config(text='Status: Starting...')
    ## reading creds
    try:
        df = pd.read_csv(f'{csvfilepath}')
        namelist = df['name'].tolist()
        numberlist = df['numbers'].to_list()
        symbols = '@#$'
    except KeyError:
        messagebox.showerror('Enter headers Correctly.', 'Please enter headers correctly in the csv file. (\"numbers\", \"name\")')
    except:
        messagebox.showerror("File Not Selected!!!", "CSV Not selected correctly.")
        
    # read pdf 
    try:
        reader = PdfReader(pdffilepath)
        writer = PdfWriter()
    except:
        messagebox.showerror("File Not Selected!!!", "PDF Not selected correctly.")
    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    csv_file_name = "password-creds.csv"
    if os.path.exists(f"{logpath}/{csv_file_name}"):
        expand = 1
        while True:
            expand += 1
            new_file_name = csv_file_name.split(".csv")[0] + str(expand) + ".csv"
            if os.path.exists(f"{logpath}/{new_file_name}"):
                continue
            else:
                csv_file_name = new_file_name
                break

    with open(f'{logpath}/{csv_file_name}', 'a', encoding='utf-8', newline='\n') as newcsv:
        fieldnames = ['name', 'numbers', 'password', 'pdffilename']
        writer_f = csv.DictWriter(newcsv, fieldnames=fieldnames)
        writer_f.writeheader()

        i = 0 
        while i in range(0, len(namelist)):
            name = str(namelist[i])
            number = str(numberlist[i])
            name = name.lower().replace(' ','')
            name_length = len(name)
            number_length = len(number)
            if name_length >=5:
                fivesyllable = name[:5]
                # print(fivesyllable)
            else:
                fivesyllable = 'users'

            if number_length >= 4:
                fournumberdigit = number[:4]
                # print(fournumberdigit)
            else:
                fournumberdigit = str(random.randint(1000,9999))

            password = f'{fivesyllable[0].upper()}{fivesyllable[1]}{random.choice(symbols)}{fournumberdigit[:2]}{random.choice(symbols)}{fivesyllable[2:4]}{fournumberdigit[2:]}{random.choice(symbols)}{fivesyllable[-1].upper()}'
            # print(password)

            # Add a password to the new PDF
            writer.encrypt(password, use_128bit=True)

            ##################
            file_name = f"{fivesyllable}{fournumberdigit}.pdf"
            if os.path.exists(f"{logpath}/{file_name}"):
                expand = 1
                while True:
                    expand += 1
                    new_file_name = file_name.split(".pdf")[0] + str(expand) + ".pdf"
                    if os.path.exists(f"{logpath}/{new_file_name}"):
                        continue
                    else:
                        file_name = new_file_name
                        break

            # Save the new PDF to a file
            with open(f"{logpath}/{file_name}", "wb") as f:
                writer.write(f)

            writer_f.writerow({'name': namelist[i], 'numbers': number, 'password': password, 'pdffilename' : file_name.split(".pdf")[0]})

            labelstatus.config(text=f"Status: Encrypting {i+1} / {len(namelist)}")
            i += 1
            
    labelstatus.config(text="Status: Finished !")
    messagebox.showinfo("Completed!", "Finished.")
    

def opencsvFile():
    global csvfilepath
    csvfilepath = filedialog.askopenfilename(title="Select Number CSV File",
                                            filetypes= (("CSV Files", "*.csv"),))
    
    labelcfilename = csvfilepath.rsplit('/')
    labelcfilename = labelcfilename[-1]
    labelcsvfilename.config(text=labelcfilename)

def openpdfFile():
    global pdffilepath
    pdffilepath = filedialog.askopenfilename(title="Select PDF File",
                                            filetypes= (("PDF Files", "*.pdf"),))
    
    labelpfilename = pdffilepath.rsplit('/')
    labelpfilename = labelpfilename[-1]
    labelpdffilename.config(text=labelpfilename)

def clearcommand():
    labelpdffilename.config(text='')
    labelcsvfilename.config(text='')


def runthreadcommand():
    threading.Thread(target=main).start()

def mainwindow():                                                             # window body
    global  window, labelpdffilename, labelcsvfilename, labelstatus

    window = Tk()
    window.geometry('600x400')
    window.title('Encrypt Pdf')

    label_choosepdf = Label(window, text='Choose PDF', font=('Times New Roman', 12))
    label_choosepdf.place(relx=0.03, rely=0.1, anchor='nw')
    pdfButton = Button(window, text='Select', command=openpdfFile)
    pdfButton.place(relx=0.25, rely=0.1, anchor='nw')
    labelpdffilename = Label(window, text='', font=('Times New Roman', 11))
    labelpdffilename.place(relx=0.35, rely=0.1, anchor='nw')

    label_select_csvfile = Label(window, text='Credential File', font=('Times New Roman', 12))
    label_select_csvfile.place(relx=0.03, rely=0.20, anchor='nw')
    csvButton = Button(window, text='Select', command=opencsvFile)
    csvButton.place(relx=0.25, rely=0.20, anchor='nw')
    labelcsvfilename = Label(window, text='', font=('Times New Roman', 11))
    labelcsvfilename.place(relx=0.35, rely=0.20, anchor='nw')

    generate_button = Button(window, text='Generate', command=runthreadcommand)
    generate_button.place(relx=0.15, rely=0.33, anchor='nw')
    
    clear_button = Button(window, text='Reset', command=clearcommand)
    clear_button.place(relx=0.35, rely=0.33, anchor='nw')

    labelstatus = Label(window, text='', font=('Times New Roman', 11))
    labelstatus.place(relx=0.25, rely=0.42, anchor='nw')

    window.mainloop()

if __name__ == '__main__':
    mainwindow()



