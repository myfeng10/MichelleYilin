from tkinter import *
import datetime
import random
import a

# 随机样式
num = random.randint(0,len(a.bg_color)-1)
now = datetime.datetime.now()
date = str(now)[:10]
print(date)
# 数据
data={}

def main():
    diary.winfo_children().destroy()
    
def hideLabel(widget):
    widget.pack_forget()

def JumpDiary():
    """diary page"""
    for i in [home_nav,diary_nav]:
        hideLabel(i)
    def remove():
        # show navigation
        home_nav.pack(side=LEFT,anchor='e',expand=True,padx=10,pady=10)
        diary_nav.pack(side=RIGHT,anchor='w',expand=True,padx=10,pady=10)
        # hide diary widget
        for i in [date,agendalabel,thoughtlabel,Check,Agenda_Output,AgendainputText,ThoughtinputText,home]:
            hideLabel(i)

    agen_num=random.randint(0,len(a.agenda_text)-1)
    thought_num=random.randint(0,len(a.thoughts_text)-1)
    now = datetime.datetime.now()
    date_num = str(now)[:10]

    def Output():
        Agenda_Output.delete("1.0", "end") 
        Input = AgendainputText.get("1.0", "end-1c")
        if len(str(Input))==0:
            Input='NONE'
        else:
            Input = Input.split()[0]
        Input2=ThoughtinputText.get("1.0", "end-1c")
        if len(str(Input2))==0:
            Input2='NONE'
        else:
            Input2 = Input2.split()[0]

        data.update({date_num:[Input,Input2]})
        #Agenda_Output.insert(END,str(now)[:19]+'\n')
        #Agenda_Output.insert(END,"Agenda: " +Input+'\n'+"Thoughts: "+Input2)
        print(data)
    
    # construct label
    date = Label(diary,text='- - - - - - - - - - - - - - - '+date_num+'- - - - - - - - - - - - - - - ',font=("Times", "14", "italic",'bold'),bg=a.bg_color[num],fg=a.textcolor)
    agendalabel = Label(diary,text=a.agenda_text[agen_num],
            bd='4', font=("Times", "23", "bold",'italic'), width='40',bg=a.bg_color[num],fg=a.textcolor)
    thoughtlabel = Label(diary,text=a.thoughts_text[thought_num],
            bd='4', font=("Times", "23", "bold",'italic'), width='40',bg=a.bg_color[num],fg=a.textcolor)
    Check = Button(diary,height=2,
                width=4,
                text=a.button_sym[num],border=0,
                command=lambda: Output(),activebackground='pink',activeforeground='pink',background='pink', fg=a.inputfg, font=("Times", "14"))
    home=Button(diary,text="🔙",command=remove)
    Agenda_Output = Text(diary,height=5,width=40, bd='3', bg='#f7f7f7', font=("Times", "18", "bold"))
    # initialize input text
    AgendainputText = Text(diary,height=9,highlightbackground=a.highlightbg[num],highlightcolor=a.highlight_color[num],
                    width=40, bd='3', font=("Times", "18", "bold"),bg=a.inputbg,fg=a.inputfg)
    ThoughtinputText = Text(diary,height=9,highlightbackground=a.highlightbg[num],highlightcolor=a.highlight_color[num],
                    width=40, bd='3', font=("Times", "18", "bold"),bg=a.inputbg,fg=a.inputfg)
    
    # pack

    date.pack(padx=2,pady= 10)
    agendalabel.pack(padx=2, pady=2)
    AgendainputText.pack(padx=5, pady=5)
    thoughtlabel.pack(padx=2, pady=2)
    ThoughtinputText.pack(padx=5, pady=5)
    Check.pack(padx=2, pady=10)
    #Agenda_Output.pack(pady=5)
    home.pack(padx=2, pady=10)


main= Tk()
main.title("WELCOME TO MICHELLE's PAGE")
main.configure(bg=a.bg_color[num])


diary_exist=False

# Label Frame
navigation = Frame(main,background=a.bg_color[num]).pack()
diary = Frame(main).pack()

# navigation button
home_nav = Button(navigation,text="🚩" ,command=main,height=2,width=2)
diary_nav = Button(navigation,text="📖" ,background="black",command=JumpDiary,height=2,width=2)

# pack
home_nav.pack(side=LEFT,anchor='e',expand=True,padx=10,pady=10)
diary_nav.pack(side=RIGHT,anchor='w',expand=True,padx=10,pady=10)


main.mainloop()


