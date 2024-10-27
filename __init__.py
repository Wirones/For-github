
from tkinter import *
from tkinter import filedialog
from tkinter import Button
from tkinter import Label
import os
import io
from summarizer import *
from summarizer import Summarizer

tkinter = Tk()
tkinter.title("Суммаризатор")
tkinter.geometry("400x300")
tkinter.resizable()

def elements_tkinter():
    tkinter_button_open_file = Button(text="Открыть файл",command=open_file)
    tkinter_button_open_file.pack()
    tkinter_button_open_file = Button(text="Сохранить файл",command=save_file)
    tkinter_button_open_file.pack()

def open_file():
    filepath_open_file = filedialog.askopenfilename()
    with io.open(filepath_open_file, 'r',encoding='utf-8') as f:
        global starting_initial_data
        starting_initial_data = f.read() #Входные данные
    Label_open_file = Label(text="Ожидание обработки файла")
    Label_open_file.pack()
    work_summarizer()
    Label_save_file = Label(text="Файл готов")
    Label_save_file.pack()

def save_file():
    filepath_save_file = filedialog.asksaveasfilename()
    folder_path = os.path.dirname(filepath_save_file) 
    if not os.path.exists(folder_path): 
        os.makedirs(folder_path)
    with open(filepath_save_file, 'w') as file: 
        file.write(full) #Выходные данные в файле
    

def work_summarizer(): 
    model = Summarizer()  #Импорт бибилиотеки суммиризатора
    result = model(starting_initial_data, min_length=60) #Результат суммиризатора
    global full #Опрееделение глоабльной функции для функции save_file 
    full = ''.join(result) #Добавление результата в строку
    global Label_save_file
    
def main():   
    elements_tkinter() 
main()

tkinter.mainloop()