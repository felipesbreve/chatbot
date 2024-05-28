from tkinter import * # Tk, Label, Text, Scrollbar, Entry, END, NORMAL, DISABLED, Button
from chat import get_response, bot_name

BG_GRAY = '#ABB2B9'
BG_COLOR = '#17202A'
TEXT_COLOR = '#EAECEE'

FONT = 'Helvetica 14'
FONT_BOLD = 'Helvetica 13 bold'

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()
    
    def _setup_main_window(self):
        self.window.title('Chat')
        self.window.resizable(width = False, height = False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # Head Label
        head_label = Label(self.window, bg = BG_COLOR, fg = TEXT_COLOR, text = "Bem vindo", font = FONT_BOLD, pady = 10)
        head_label.place(relwidth=1)

        # Tiny Divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1,rely=0.07, relheight=0.012)

        # Text Wiget
        self.text_wiget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg = TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_wiget.place(relheight=0.745, relwidth = 1, rely=0.08)
        self.text_wiget.configure(cursor='arrow', state=DISABLED)

        # Scrollbar
        scrollbar = Scrollbar(self.text_wiget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_wiget.yview)

        # Bottom Label
        bottom_label = Label(self.window, bg = BG_GRAY, height=80)
        bottom_label.place(relwidth = 1, rely=0.825)

        # Message Entry Box
        self.msg_entry = Entry(bottom_label, bg = '#2C3E50', fg = TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind('<Return>', self._on_enter_pressed)

        # Send Button
        send_button = Button(bottom_label, text = "Enviar", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "Você: ")

    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        new_msg = f'{sender}: {msg}\n\n'
        self.text_wiget.configure(state=NORMAL)
        self.text_wiget.insert(END, new_msg)
        self.text_wiget.configure(state=DISABLED)

        response_msg = f'{bot_name}: {get_response(msg)}\n\n'
        self.text_wiget.configure(state=NORMAL)
        self.text_wiget.insert(END, response_msg)
        self.text_wiget.configure(state=DISABLED)

        self.text_wiget.see(END)



if __name__ == "__main__":
    app = ChatApplication()
    app.run()