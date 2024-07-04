from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#functionality part


# Function to clear the entry fields
def clear():
    bathshoEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairsparyEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    sugarEntry.delete(0,END)
    taeEntry.delete(0,END)
    mojoEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    dewEntry.delete(0,END)
    footoEntry.delete(0,END)
    powerEntry.delete(0,END)

        

    bathshoEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsparyEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    sugarEntry.insert(0,0)
    taeEntry.insert(0,0)
    mojoEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    dewEntry.insert(0,0)
    footoEntry.insert(0,0)
    powerEntry.insert(0,0)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinktaxEntry.delete(0,END)
    cosmeticspriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkpriceEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)








# def send_email():
#     def send_gmail():
#         try:
#             ob=smtplib.SMTP('smtp.gmail.com',587)
#             ob.starttls()
#             ob.login(senderEntry.get(),passwordEntry.get())
#             message=email_textarea.get(1.0,END)
#             ob.sendmail(senderEntry.get(),reciverEntry.get(),message)
#             ob.quit()
#             messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
#         except:
#             messagebox.showerror('Error','Something went wron,Please try again',parent=root1)



#     if textarea.get(1.0,END)=='\n':
#         messagebox.showerror('Error ','Bill is Empty')
#     else:
#         root1=Toplevel()
#         root1.title('Send Gmail')
#         root1.config(bg='gray20')
#         root1.resizable(0,0)

#         senderframe=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bg='gray20',fg='white')
#         senderframe.grid(row=0,column=0,padx=40,pady=20)


#         senderLabel=Label(senderframe,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
#         senderLabel.grid(row=0,column=0,padx=10,pady=8)

#         senderEntry=Entry(senderframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
#         senderEntry.grid(row=0,column=1,padx=10,pady=8)


#         passwordLabel=Label(senderframe,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
#         passwordLabel.grid(row=1,column=0,padx=10,pady=8)

#         passwordEntry=Entry(senderframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
#         passwordEntry.grid(row=1,column=1,padx=10,pady=8)
        
#         recipientframe=LabelFrame(root1,text='Reciver  Address',font=('arial',16,'bold'),bg='gray')
#         recipientframe.grid(row=1,column=0,padx=40,pady=20)

#         reciverLabel=Label(recipientframe,text="Password",font=('arial',14,'bold'))
#         reciverLabel.grid(row=1,column=0,padx=10,pady=8)
#         reciverEntry=Entry(recipientframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
#         reciverEntry.grid(row=0,column=1,padx=10,pady=8)

#         messageLabel=Label(recipientframe,text="Message",font=('arial',14,'bold'))
#         messageLabel.grid(row=1,column=0,padx=10,pady=8)

#         email_textarea=Text(recipientframe,font=('arial',14,'bold'),bd=2,relief=SUNKEN,
#                             width=42,height=11)
#         email_textarea.grid(row=2,column=0,columnspan=2)
#         email_textarea.delete(1.0,END)

#         email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-',',').replace('\t\t\t','\t\t'))

#         sendButtom=Button(root1,text='SEND',font=('arial',14,'bold'),width=15,command=send_gmail)
#         sendButtom.grid(row=2,column=0,pady=20)


#         root1.mainloop()






def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error ','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')



def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break

    else:
        messagebox.showerror('Error','Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number{billnumber} is saved Successfully')
        billnumber=random.randint(500,1000)





billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get() ==''or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Are Required')
    elif cosmeticspriceEntry.get()==''and grocerypriceEntry.get()==''and drinkpriceEntry.get()=='':
        messagebox.showerror('Error','NO Product are Selected')
    
    elif cosmeticspriceEntry.get()=='0 TK' and grocerypriceEntry.get()=='0 TK' and drinkpriceEntry.get()=='0 TK':
       messagebox.showerror('Error','NO Product are Selected') 
    else:

        textarea.delete(1.0,END)


        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number:{billnumber}\n')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer Phone Number:{phoneEntry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n=======================================================')
        if bathshoEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap \t\t\t{ bathshoEntry.get()}\t\t\t{soapprice} TK')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream \t\t\t{ facecreamEntry.get()}\t\t\t{facecreamprice} TK')

        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash \t\t\t{ facewashEntry.get()}\t\t\t{facewashprice} TK')

        if hairsparyEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray \t\t\t{ hairsparyEntry.get()}\t\t\t{hairsparyprice} TK')

        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel \t\t\t{ hairgelEntry.get()}\t\t\t{hairgelprice} TK')

        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion \t\t\t{ bodylotionEntry.get()}\t\t\t{bodylotionprice} TK')
        
        
        
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice \t\t\t{ riceEntry.get()}\t\t\t{riceEntry} TK')
        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal \t\t\t{ daalEntry.get()}\t\t\t{daalprice} TK')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil \t\t\t{ oilEntry.get()}\t\t\t{oilprice} TK')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar \t\t\t{ sugarEntry.get()}\t\t\t{sugarprice} TK')
        if taeEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{ taeEntry.get()}\t\t\t{teaptice} TK')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat \t\t\t{ wheatEntry.get()}\t\t\t{wheatprice} TK')
        

        if mojoEntry.get()!='0':
            textarea.insert(END,f'\nMojo \t\t\t{ mojoEntry.get()}\t\t\t{mojoprice} TK')

        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi \t\t\t{ pepsiEntry.get()}\t\t\t{pepsiprice} TK')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite \t\t\t{ spriteEntry.get()}\t\t\t{spriteprice} TK')
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew \t\t\t{ dewEntry.get()}\t\t\t{dewprice} TK')
        if footoEntry.get()!='0':
            textarea.insert(END,f'\nFooto \t\t\t{ footoEntry.get()}\t\t\t{footoprice} TK')
        if powerEntry.get()!='0':
            textarea.insert(END,f'\nFrutika \t\t\t{ powerEntry.get()}\t\t\t{powerprice} TK')
        textarea.insert(END,'\n-------------------------------------------------------')
        if cosmetictaxEntry.get()!='0.0TK':
            textarea.insert(END,f'\n Cosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0TK':
            textarea.insert(END,f'\n Grocery Tax\t\t\t\t{grocerytaxEntry.get()}')
        if drinktaxEntry.get()!='0.0TK':
            textarea.insert(END,f'\n Drinks Tax\t\t\t\t{drinktaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t{totalbill}')
        textarea.insert(END,'\n-------------------------------------------------------')
        save_bill()
        

def total():
    global soapprice,facecreamprice,facewashprice,hairsparyprice,hairgelprice,bodylotionprice
    global riceprice,daalprice,oilprice,sugarprice,teaptice,wheatprice
    global mojoprice,pepsiprice,spriteprice,dewprice,footoprice,powerprice
    global totalbill

    #cosmetic Price
    soapprice=int(bathshoEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsparyprice=int(hairgelEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*88
    bodylotionprice=int(bodylotionEntry.get())*60



    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsparyprice+hairgelprice+bodylotionprice
    cosmeticspriceEntry.delete(0,END)
    cosmeticspriceEntry.insert(0,f'{totalcosmeticprice}Tk')
    cosmetictax=totalcosmeticprice*0.7
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax)+'TK')


    #groserey price
    riceprice=int(riceEntry.get())*200 
    daalprice=int(daalEntry.get())*100
    oilprice=int(oilEntry.get())*120
    sugarprice=int(sugarEntry.get())*50
    teaptice=int(taeEntry.get())*140
    wheatprice=int(wheatEntry.get())*80


    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaptice+wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+'Tk')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+'TK')


    #drinks price
    mojoprice=int(mojoEntry.get())*50
    pepsiprice=int(pepsiEntry.get())*20
    spriteprice=int(spriteEntry.get())*30
    dewprice=int(dewEntry.get())*20
    footoprice=int(footoEntry.get())*45
    powerprice=int(powerEntry.get())*90


    totaldrinksprice=mojoprice+pepsiprice+spriteprice+dewprice+footoprice+powerprice
    drinkpriceEntry.delete(0,END)
    drinkpriceEntry.insert(0,str(totaldrinksprice)+'TK')
    drinkstax=totaldrinksprice*0.08
    drinktaxEntry.delete(0,END)
    drinktaxEntry.insert(0,str(drinkstax)+'TK')


    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax







    


#GUI part
root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
#creating the header label
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                   ,bg='black',fg='white',bd=12,relief=GROOVE)#this for title colour 
headingLabel.pack(fill=X)
#customer details start
cutomer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                 ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
cutomer_details_frame.pack(fill=X)

nameLabel=Label(cutomer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(cutomer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(cutomer_details_frame,text='Mobile Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(cutomer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(cutomer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(cutomer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(cutomer_details_frame,text='Search',
                    font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)#customer details  end
#product section
productsFrame=Frame(root)
productsFrame.pack()
#cosmetic section
cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold')
                                 ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)



bathshopLabel=Label(cosmeticsFrame,text='Shoap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathshopLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathshoEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathshoEntry.grid(row=0,column=1,pady=9,padx=10) 
bathshoEntry.insert(0,0)


facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)


facewashLabel=Label(cosmeticsFrame,text='Face wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsparyLabel=Label(cosmeticsFrame,text='Hair Spary',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairsparyLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsparyEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsparyEntry.grid(row=3,column=1,pady=9,padx=10)
hairsparyEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)



bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)


#grocery section
groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold')
                                 ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1,pady=9)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)


oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)


daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)

wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)


sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)



taeLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
taeLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
taeEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
taeEntry.grid(row=5,column=1,pady=9,padx=10)
taeEntry.insert(0,0)



#drinks section
drinksFrame=LabelFrame(productsFrame,text='Drinks',font=('times new roman',15,'bold')
                                 ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2,pady=9)

mojoLabel=Label(drinksFrame,text='Mojo',font=('times new roman',15,'bold'),bg='gray20',fg='white')
mojoLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
mojoEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
mojoEntry.grid(row=0,column=1,pady=9,padx=10)
mojoEntry.insert(0,0)



pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)


spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)



dewLabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)



footoLabel=Label(drinksFrame,text='Footo',font=('times new roman',15,'bold'),bg='gray20',fg='white')
footoLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
footoEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
footoEntry.grid(row=4,column=1,pady=9,padx=10)
footoEntry.insert(0,0)



powerLabel=Label(drinksFrame,text='Frutika',font=('times new roman',15,'bold'),bg='gray20',fg='white')
powerLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
powerEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
powerEntry.grid(row=5,column=1,pady=9,padx=10)
powerEntry.insert(0,0)

#bill area section
billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new Roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)



#bill area section
billmanuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold')
                                 ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmanuFrame.pack()

cosmeticspriceLabel=Label(billmanuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmeticspriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticspriceEntry=Entry(billmanuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticspriceEntry.grid(row=0,column=1,pady=6,padx=10)


grocerypriceLabel=Label(billmanuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry=Entry(billmanuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)


drinkpriceLabel=Label(billmanuFrame,text='Drink Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkpriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
drinkpriceEntry=Entry(billmanuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkpriceEntry.grid(row=2,column=1,pady=6,padx=10)




cosmetictaxLabel=Label(billmanuFrame,text='Cosmetic tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmanuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)


grocerytaxLabel=Label(billmanuFrame,text='Grocery tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry=Entry(billmanuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)


drinktaxLabel=Label(billmanuFrame,text='Drinks Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinktaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
drinktaxEntry=Entry(billmanuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinktaxEntry.grid(row=2,column=3,pady=6,padx=10)

#button frame section
buttonframe=Frame(billmanuFrame,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonframe,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10
                   ,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)


billButton=Button(buttonframe,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)



#emailButton=Button(buttonframe,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
#emailButton.grid(row=0,column=2,pady=20,padx=5)


printButton=Button(buttonframe,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=2,pady=20,padx=5)

clearButton=Button(buttonframe,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=3,pady=20,padx=5)




root.mainloop()






