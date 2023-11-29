from tkinter import *
from openai import OpenAI
import requests


class ChatBoxApplication:

    def __init__(self):
        self.window = Tk()
        self.main_window()  # you're creating a function.
        self.openai = OpenAI(
            base_url='https://openrouter.ai/api/v1/',
            api_key='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')

    def chat_ai(self, msg = 'Hello'):
        message = self.openai.chat.completions.create(
                        model='openai/gpt-3.5-turbo',
                        messages= [
                            # {'role': 'system', 'message': ''},
                            {'role': 'user', 'content': msg},
                        ]
                    )
        messagex = message.choices[0].message.content
        self._insert_message(messagex, 'AI')

    def run(self):
        # self.chat_ai()
        self.window.mainloop()

    def main_window(self):
        self.window.title("ChatBox")
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.configure(width=470, height=550, bg="black")

        # Head Label
        head = Label(self.window, bg="black", fg="white", text="Your AI",
                     font="Arial 10 bold", pady=10)
        head.place(relwidth=1)

        # line divider
        line = Label(self.window, width=450, bg="yellow")
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #text widget
        #We used the self because we're going to call it somewhereelse and we need to follow the self format.
        self.text_widget = Text(self.window, width=20, height=2, bg="black", fg="white",font="Helvetica 12", padx=15, pady=5, wrap=WORD)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #Scroll Bar
        scrollbar = Scrollbar(self.text_widget)
        # scrollbar.place(relheight=1, relx=0.973)
        scrollbar.configure(command=self.text_widget.yview)

        #Bottom Label
        bottom_label = Label(self.window, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        #Message entry box
        self.msg_entry = Text(bottom_label, bg="Black", fg="white", font="Helvetica 10", insertbackground='white')
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        #self.msg_entry.bind("<Return>",self._on_enter_pressed) #binding the return command to the on pressed function

        #Send Button
        send_button = Button(bottom_label, text="SEND", font="Helvetica 15", width=20, bg="white", fg="black", command=lambda: self._on_enter_pressed())
        send_button.place(relx=0.77, rely=0.008, relheight=0.6, relwidth=0.22)


    def _on_enter_pressed(self):
        msg = self.msg_entry.get('1.0', END) #it will get the input text as a string
        self._insert_message(msg, "You")
        self.chat_ai(msg)

    def _insert_message(self, msg, sender):
        if not msg: #if we hit enter without putting any text in it
            return

        self.msg_entry.delete('1.0', END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)


        self.text_widget.see(END) #We can scroll and always see the last message.
if __name__ == "__main__":
    app = ChatBoxApplication()
    app.run()
