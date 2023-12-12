import tkinter  as tk


#ana ekran
pencere_1 = tk.Tk()
pencere_1.geometry('1500x786+10+0')
pencere_1.configure(bg="red")
pencere_1.title("Chat")








ceviri="bot"# simdilik ekna yaz

    
yazı = tk.Label(text=ceviri, bg="black", fg="green", font="verdana 10 bold", justify="right", )#font="verdana 15 bold
yazı.place(x=80, y=10, width=1350, height=100)



# Kullanıcı giriş kutusu
user_input = tk.Entry(pencere_1, width=100, bg="green", fg="black", font="bold 15")
user_input.pack(side="bottom" )


# Sohbet logları için metin alanı
chat_log = tk.Text(pencere_1, width=137, height=38, bg="red",font="bold 11", state= "disabled")
chat_log.pack(side="bottom")

"""
initial_message = "Bot: Merhaba! Size nasıl yardımcı olabilirim?(Uygulamaya ilk girişiniz ise /yardım komutunu yazın.)\n"
chat_log.insert(tk.END, initial_message)"""

pencere_1.mainloop()