from tkinter import  *
from tkinter import messagebox
from textblob import  TextBlob
from tkinter.ttk import Combobox
win=Tk()
win.geometry("500x400")
win.title("Translater")
win.resizable(False, False)
win.configure(bg="#39B7CD")

lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

def text_translate(event = None):
    try:
        word = TextBlob(varname1.get())
        lan = word.detect_language()
        lan_todict = languages.get()
        lan_to = lan_dict[lan_todict]
        word = word.translate(from_lang=lan, to=lan_to)
        label3.configure(text=word)
        varname2.set(word)
    except:
        varname2.set('try another word')

def main_exit():
    exit = messagebox.askyesno('Notification','Do You Want To Exit !.', parent= win)
    if(exit==True):
        win.destroy()


##binding function###

def on_enter1(e):
    entry1['bg'] = '#76D7C4'
def on_leave1(e):
    entry1['bg'] = 'white'

def on_enter2(e):
    entry2['bg'] = '#76D7C4'
def on_leave2(e):
    entry2['bg'] = 'white'

def on_enterbtn1(e):
    btn1['bg'] = '#76D7C4'
def on_leavebtn1(e):
    btn1['bg'] = 'white'

def on_enterbtn2(e):
    btn2['bg'] = '#76D7C4'
def on_leavebtn2(e):
    btn2['bg'] = 'white'

#####combo box or drop down box#####
languages = StringVar()
font_box= Combobox(win, width=13, textvariable=languages, state="readonly")
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300, y=0)

#####ENTRY BOX######
varname1= StringVar()
entry1= Entry(win,width=30, textvariable=varname1, font=('times',16,'italic bold'))
entry1.place(x=150, y=40)

varname2= StringVar()
entry2= Entry(win,width=30, textvariable=varname2, font=('times',16,'italic bold'))
entry2.place(x=150, y=100)

######LABELS########

label1=Label(win, text='Enter Words:', font=('times',14,'italic bold'),bg='#39B7CD')
label1.place(x=5, y= 40)

label2=Label(win, text='Translated: ', font=('times',14,'italic bold'),bg='#39B7CD')
label2.place(x=5, y= 100)

label3=Label(win, text=' ', font=('times',14,'italic bold'),bg='#39B7CD')
label3.place(x=5, y= 260)

#####BUTTONS######
imgbtn1=PhotoImage(file='icons/click.png')
imgbtn2=PhotoImage(file='icons/exit.png')

imgbtn1= imgbtn1.subsample(12, 12)
imgbtn2=imgbtn2.subsample(12, 12)
btn1 = Button(win, text='Click', bd=10,fg='#000033',bg='white',activebackground='red',width=100, font=('times',14,'italic bold'), image=imgbtn1,compound=RIGHT, command=text_translate)
btn1.place(x=50, y=170)

btn2 = Button(win, text='Exit', bd=10,fg='#000033',bg='white',activebackground='red',width=100, font=('times',14,'italic bold'), image=imgbtn2, compound=RIGHT, command= main_exit)
btn2.place(x=280, y=170)
win.bind('<Return>', text_translate)

###BINDING######
entry1.bind('<Enter>',on_enter1)
entry1.bind('<Leave>',on_leave1)

entry2.bind('<Enter>',on_enter2)
entry2.bind('<Leave>',on_leave2)

btn1.bind('<Enter>',on_enterbtn1)
btn1.bind('<Leave>',on_leavebtn1)

btn2.bind('<Enter>',on_enterbtn2)
btn2.bind('<Leave>',on_leavebtn2)

win.mainloop()

