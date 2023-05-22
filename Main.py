from BackEnd.ChatBot import *
from threading import Thread
from tkinter import messagebox
from DB.db import DB_OPERATION
from retry import retry
from customtkinter import *
set_appearance_mode('system')


def redirect(page, window):
    '''
    Clearing existing page and redirecting to the other page
    '''
    for widget in window.winfo_children(): 
        widget.destroy()
    page(window)


def index_page(window):
    # Window
    window.title('ChatBot')
    window.geometry('900x600')
    window.resizable(False, False)
    window.iconbitmap('chat.ico')

    CTkLabel(window, text='Welcome to ChatBot !', font=('Arial',30)).place(x=320, y=10)
    CTkLabel(window, text='Login To Start Using It 😉', font=('Arial',20)).place(x=350, y=50)

    CTkButton(window, text='LOGIN AS USER', height=50, command=lambda: redirect(user_login_page, window)).place(x=250, y=300)
    CTkButton(window, text='LOGIN AS ADMIN', height=50, command=lambda: redirect(admin_login_page, window)).place(x=500, y=300)

    window.mainloop()


def user_login_page(window):
    # Global variables
    DB = DB_OPERATION()

    # Window settings
    window.title('ChatBot')
    window.geometry('900x600')
    window.resizable(False, False)
    window.iconbitmap('chat.ico')

    CTkButton(window, text='<<', width=20, command=lambda: redirect(index_page, window)).place(x=0, y=0)
    CTkLabel(window, text='USER LOGIN', font=('Arial',30)).place(x=380, y=10)

    CTkLabel(window, text='Username :- ', font=('Arial',20)).place(x=280, y=150)
    USERNAME = CTkEntry(window, placeholder_text='Enter your username...', width=250)
    USERNAME.place(x=410, y=152)
    CTkLabel(window, text='Password :- ', font=('Arial',20)).place(x=280, y=250)
    PASSWORD = CTkEntry(window, placeholder_text='Enter your password...',  show='*', width=250)
    PASSWORD.place(x=410, y=252)

    def check():
        if USERNAME.get() == '' or PASSWORD.get() == '':
            messagebox.showerror('Error', 'Please fill all the information !')
        else:
            if DB.user_check(USERNAME.get(), PASSWORD.get()):
                redirect(chatbot_page, window)
            else:
                messagebox.showerror('Error', 'Wrong Username or Password !')

    CTkButton(window, text='Login', height=35, command=check).place(x=300, y=350)
    CTkButton(window, text='Signup', height=35, command=lambda: redirect(user_signup_page, window)).place(x=500, y=350)

    window.mainloop()


def user_signup_page(window):
    # Global variables
    DB = DB_OPERATION()

    # Window settings
    window.title('ChatBot')
    window.geometry('900x600')
    window.resizable(False, False)
    window.iconbitmap('chat.ico')

    CTkButton(window, text='<<', width=20, command=lambda: redirect(user_login_page, window)).place(x=0, y=0)
    CTkLabel(window, text='USER SIGNUP', font=('Arial',30)).place(x=380, y=10)

    CTkLabel(window, text='Username :- ', font=('Arial',20)).place(x=280, y=150)
    USERNAME = CTkEntry(window, placeholder_text='Enter your username...', width=250)
    USERNAME.place(x=410, y=152)
    CTkLabel(window, text='Password :- ', font=('Arial',20)).place(x=280, y=250)
    PASSWORD = CTkEntry(window, placeholder_text='Enter your password...',  show='*', width=250)
    PASSWORD.place(x=410, y=252)

    def check():
        if USERNAME.get() == '' or PASSWORD.get() == '':
            messagebox.showerror('Error', 'Please fill all the information !')
        else:
            if DB.user_check(USERNAME.get(), PASSWORD.get()):
                messagebox.showerror('Error', 'Username already exist !')
            else:
                if DB.insert_user(USERNAME.get(), PASSWORD.get()):
                    messagebox.showinfo('Success', 'Registered Successfully !')
                    redirect(user_login_page, window)
                else:
                    messagebox.showerror('Error', 'Some error occurred !')

    CTkButton(window, text='Signup', height=35, command=check).place(x=430, y=350)

    window.mainloop()


def admin_login_page(window):
    DB = DB_OPERATION()

    # Window settings
    window.title('ChatBot')
    window.geometry('900x600')
    window.resizable(False, False)
    window.iconbitmap('chat.ico')

    CTkButton(window, text='<<', width=20, command=lambda: redirect(index_page, window)).place(x=0, y=0)
    CTkLabel(window, text='ADMIN LOGIN', font=('Arial',30)).place(x=380, y=10)

    CTkLabel(window, text='Username :- ', font=('Arial',20)).place(x=280, y=150)
    USERNAME = CTkEntry(window, placeholder_text='Enter your username...', width=250)
    USERNAME.place(x=410, y=152)
    CTkLabel(window, text='Password :- ', font=('Arial',20)).place(x=280, y=250)
    PASSWORD = CTkEntry(window, placeholder_text='Enter your password...',  show='*', width=250)
    PASSWORD.place(x=410, y=252)

    def check():
        if USERNAME.get() == '' or PASSWORD.get() == '':
            messagebox.showerror('Error', 'Please fill all the information !')
        else:
            if DB.admin_check(USERNAME.get(), PASSWORD.get()):
                redirect(admin_page, window)
            else:
                messagebox.showerror('Error', 'Wrong Username or Password !')

    CTkButton(window, text='Login', height=35, command=check).place(x=430, y=350)

    window.mainloop()


def admin_page(window):
    example_context = """
    Type your context here ...

    Example :- This is a conversation between USER and AI. AI is a user friendly machine who talks nicely to user. AI avoids some answers if it's illegal to know and can cause crime.
    """

    # Window settings
    window.title('ChatBot')
    window.geometry('900x600')
    window.resizable(False, False)
    window.iconbitmap('chat.ico')

    CTkLabel(window, text='ADMIN PAGE', font=('Arial',30)).place(x=350, y=10)

    def on_click(event):
        context_text.configure(state=NORMAL)
        context_text.delete('1.0', 'end')

    context_text = CTkTextbox(window, width=700, height=400, wrap='word')
    context_text.place(relx=.5, rely=.5,anchor= CENTER)
    context_text.insert(END, example_context)
    context_text.configure(state=DISABLED)
    context_text.bind('<Button-1>', on_click)

    def tune_ai():
        context = context_text.get('1.0','end')

        with open('prompt_chat.txt', 'w') as file:
            file.write(f'{context}\n<<BLOCK>>')
        
        messagebox.showinfo('Success', 'Tunning AI is done !')

    CTkButton(window, text='Tune AI', command=tune_ai).place(x=400, y=520)

    window.mainloop()


def chatbot_page(window):
    def reset_tabstop(event):
        event.widget.configure(tabs=(event.width-8, "right"))

    def user_chat_append(*args):
        global PROMPT
        chat_area.configure(state=NORMAL) # Making state 'NORMAL' from 'DISABLED (read-only)'
        usr_message = f'\tUSER: {user_message.get()}\n\n' # Takes the user message from text box and formatting it
        chat_area.insert(END, usr_message) # Inserting the value to text area
        CONVERSATION.append(f'USER: {user_message.get()}') # Saving it to the 'CONVERSATION' list
        text_block = '\n'.join(CONVERSATION) # Joining the list values to make text block
        PROMPT = open_file('prompt_chat.txt').replace('<<BLOCK>>',text_block) # Making the prompt to give model
        
        ai_chat_thread = Thread(target=ai_chat_append)
        ai_chat_thread.start()

        user_message.set('') # Setting text box empty
        chat_area.configure(state=DISABLED) # Making state 'DISABLED (read-only)' again

    def ai_chat_append():
        global PROMPT
        PROMPT = PROMPT + '\nAI:' # Adding 'AI' in last
        chat_area.configure(state=NORMAL) # Making state 'NORMAL' from 'DISABLED (read-only)'

        @retry(exceptions=Exception, tries=5, delay=0.2)
        def wrapper():
            try:
                response = GenerateResponse(PROMPT) # Generating response
                ai_message = f'AI: {response}\n\n' # Formatting the response
                chat_area.insert(END, ai_message) # Inserting the value to text area
                CONVERSATION.append(f'AI: {response}') # Saving it to the 'CONVERSATION' list
                chat_area.yview(END) # Scrolling down if it's the end of text area automatically
            except Exception:
                pass
        
        wrapper()
        chat_area.configure(state=DISABLED) # Making state 'DISABLED (read-only)' again

    # GLOBAL variables
    CONVERSATION = list()
    PROMPT = str()

    # Window settings
    window.title('ChatBot')
    window.geometry('900x600')
    window.resizable(False, False)
    window.iconbitmap('chat.ico')

    # UI
    # SETTING READ-ONLY
    ###########################
    chat_area = CTkTextbox(window, height=555, width=891, font=('Arial',15))
    chat_area.place(x=5, y=2)
    chat_area.configure(state=DISABLED)
    ###############################

    # SETTING BOTTOM AREA WITH TEXTBOX AND BUTTON FOR SEND TEXT
    ###############################
    CTkLabel(window, text='YOU:', font=('Arial',15)).place(x=2,y=560)
    user_message = StringVar()
    CTkEntry(window, textvariable=user_message, width=730).place(x=50,y=560)
    CTkButton(window, text='SEND', width=80, command=user_chat_append).place(x=800,y=560)
    ###############################

    chat_area.bind('<Configure>', reset_tabstop)
    window.bind('<Return>',user_chat_append) # Binding 'ENTER' key for send messasge
    window.mainloop()

if __name__ == '__main__':
    window = CTk()
    index_page(window)