import tkinter  as tk


#ana ekran
pencere_1 = tk.Tk()
pencere_1.geometry('1500x786+10+0')
pencere_1.configure(bg="red")
pencere_1.title("Chat")


def bot_answer():
    return ceviri


# Mesaj gönderme fonksiyonu
def send_message(message):
    message = user_input.get()
    if message.strip():  # Girilen mesaj boş değilse
        chat_log.config(state=tk.NORMAL)  # Sohbet penceresini düzenlenebilir hale getir
        chat_log.insert(tk.END, "Sen: " + message + "\n")
        cevap = bot_answer()
        chat_log.insert(tk.END, "Bot: " + cevap + "\n")
        chat_log.see(tk.END)
        chat_log.config(state=tk.DISABLED)  # Sohbet penceresini tekrar disabl yap
        chat_log.yview(tk.END)  # Otomatik aşağı kaydırma
        user_input.delete(0, tk.END)  # Mesaj giriş alanını temizle


ceviri="bot"# simdilik ekna yaz

    
yazı = tk.Label(text=ceviri, bg="black", fg="green", font="verdana 10 bold", justify="right", )#font="verdana 15 bold
yazı.place(x=80, y=10, width=1350, height=100)



# Kullanıcı giriş kutusu
user_input = tk.Entry(pencere_1, width=100, bg="green", fg="black", font="bold 15")
user_input.pack(side="bottom" )
user_input.bind("<Return>", send_message)  # Enter tuşuna basın
#user_input.bind("<Return>", bot_answer)  # Enter tuşuna basınca mesajı gönderca mesajı gönder

# Sohbet logları için metin alanı
chat_log = tk.Text(pencere_1, width=137, height=38, bg="red",font="bold 11", state= "disabled")
chat_log.pack(side="bottom")

"""
initial_message = "Bot: Merhaba! Size nasıl yardımcı olabilirim?(Uygulamaya ilk girişiniz ise /yardım komutunu yazın.)\n"
chat_log.insert(tk.END, initial_message)"""

pencere_1.mainloop()