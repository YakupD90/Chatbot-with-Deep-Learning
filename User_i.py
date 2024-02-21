from transformers import AutoModelForQuestionAnswering , AutoTokenizer,  AutoModel
from transformers import BertTokenizer, BertForQuestionAnswering, AdamW
import tkinter  as tk
#import pandas as pd
import torch

qa_input=[{'cevap':""" İstanbul Türkiye’nin en tarihi ve en kadim şehirlerinden biridir.
            İstanbul, ülkenin yedi coğrafik bölgesinden biri olan Marmara Bölgesi’nde bulunmaktadır.
            İstanbul, Asya ve Avrupa’yı birleştiren bir boğaz üzerinde kuruludur.
            İstanbul, Karadeniz ve Marmara Denizi arasında iki yakasının da yarım ada şeklinde bulunduğu bir şehirdir.
            İstanbul iki bin yıllık tarihiyle birçok medeniyete başkentlik etmiş bir şehir olarak kozmopolit bir yapıdadır.
            İstanbul, dört mevsimin yaşandığı ender şehirlerden biri olarak yedi tepe üzerine kurulu ve şimdilerde geniş ve mümbit arazilerin konutlarla dolduğu bir şehirdir.
            İstanbul’da hizmet alanları oldukça gelişmiştir. Ulaşım, eğitim, sağlık alanında imkanlar fazladır.
            İstanbul’da 18 milyona yakın insan yaşamaktadır. Çok kültürlü ve çok dinli bir yapısı olan İstanbul’un mimari özellikleri de bu şekildedir.
            Şehirde birçok cami ve kilise yan yanadır. Birçok ırktan ve dinden insanın bulunduğu şehirde tarihi mekanlar ve kültürel alanlar bütün şehri kaplamıştır.
            İstanbul’da turistik bölgeler de bulunmaktadır. Bu anlamda bir turizm şehri olan İstanbul her yıl yabancı ve yerli turistlerin akınına uğramaktadır.
            İstanbul, Türkiye’nin en kalabalık ve en yoğun nüfusuna sahip bir şehirdir.
            Başkent Ankara olmasına rağmen Türkiye denince akla ilk gelen şehir ismi İstanbul’dur.
            Şehrin tarihi ve kültürel dokusu buna çok uygundur. Şairin de dediği gibi İstanbul’da güleni şöyle dursun, ağlayan bile bahtiyardır."""}]



#eğitilmiş modeli yükle
tokenizer =BertTokenizer.from_pretrained("lserinol/bert-turkish-question-answering")
model = BertForQuestionAnswering.from_pretrained("lserinol/bert-turkish-question-answering")



#ana ekran oluştur
pencere_1 = tk.Tk()
pencere_1.geometry('1500x750+10+0')
pencere_1.configure(bg="red")
pencere_1.title("Chat")

# Mesaj gönderme fonksiyonu
def send_message(message):
    message = sor.get()
    
    #
    in0 = tokenizer(message, qa_input[0]['cevap'],  return_tensors="pt")
    out0 = model(**in0)


    cevap_basla_idx=torch.argmax(out0.start_logits)
    cevap_bit_idx = torch.argmax(out0.end_logits)

    cevap_token=in0.input_ids[0, cevap_basla_idx: cevap_bit_idx+1]
    cevap = tokenizer.decode(cevap_token)
    
    cvp = cevap
    yazı = tk.Label(text=cvp, bg="black", fg="green", font="verdana 10 bold", justify="right", )#font="verdana 15 bold
    yazı.place(x=80, y=10, width=1350, height=100)

    if message.strip():  # Girilen mesaj boş değilse
         # Sohbet penceresini düzenlenebilir hale getir
        chat_log.config(state=tk.NORMAL) 

        #soru ve metinden dönen cevabı yaz
        chat_log.insert(tk.END, "Siz: " + message + "\n")
        chat_log.insert(tk.END, "Bot: " + cevap + "\n")
        chat_log.see(tk.END)
       
        # Sohbet penceresini tekrar disabl yap
        chat_log.config(state=tk.DISABLED)  

        #aşağı kaydırma
        chat_log.yview(tk.END) 

        # Mesaj giriş alanını temizle
        sor.delete(0, tk.END)  

yazı = tk.Label(text="", bg="black", fg="green", font="verdana 10 bold", justify="right", )
yazı.place(x=80, y=10, width=1350, height=100)

x = tk.Text(pencere_1, width=130, height=1, bg="red",font="bold 11", state= "disabled")
x.pack(side="bottom")

# Kullanıcı giriş kutusu
sor = tk.Entry(pencere_1, width=100, bg="green", fg="black", font="bold 15")
sor.pack(side="bottom" )
sor.bind("<Return>", send_message)  # Enter tuşuna basın  "<Return>"


# Sohbet logları için metin alanı
chat_log = tk.Text(pencere_1, width=130, height=35, bg="red",font="bold 11", state= "disabled")
chat_log.pack(side="bottom")

pencere_1.mainloop()