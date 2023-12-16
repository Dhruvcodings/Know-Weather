from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c964b35e913021701d140445c0294e9c").json()
    w_climate1.config(text=data["weather"][0]["main"])
    w_desc1.config(text=data["weather"][0]["description"])
    w_temp1.config(text=str(data["main"]["temp"]-273.15))
    w_pressure1.config(text=data["main"]["pressure"])




#create window
win=Tk()
win.title("Predict_Weather")
win.config(bg='blue')
win.geometry("500x570")


#create main heading and place it
name_label=Label(win,text="Predict Weather App",
                 font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)



#create combox and place it with set value and brown text
city_name=StringVar()
list_city=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Delhi","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,values=list_city,
                 font=("Times New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,width=450,height=50)
com.set("\tSelect a City")
com.config(foreground="brown")



#create a weather details
# create label in w_climate and then its result in w_climate1


#weather climate
w_climate=Label(win,text="Weather Climate",
                 font=("Times New Roman",15))
w_climate.place(x=25,y=260,height=50,width=210)

w_climate1=Label(win,
                 font=("Times New Roman",15))
w_climate1.place(x=250,y=260,height=50,width=210)


#weather description
w_desc=Label(win,text="Weather Description",
                 font=("Times New Roman",15))
w_desc.place(x=25,y=330,height=50,width=210)

w_desc1=Label(win,
              font=("Times New Roman",15))
w_desc1.place(x=250,y=330,height=50,width=210)


#weather temperature
w_temp=Label(win,text="Weather Temperature",
                 font=("Times New Roman",15))
w_temp.place(x=25,y=400,height=50,width=210)

w_temp1=Label(win,
              font=("Times New Roman",15))
w_temp1.place(x=250,y=400,height=50,width=210)


#weather pressure
w_pressure=Label(win,text="Weather pressure",
                 font=("Times New Roman",15))
w_pressure.place(x=25,y=470,height=50,width=210)

w_pressure1=Label(win,
                  font=("Times New Roman",15))
w_pressure1.place(x=250,y=470,height=50,width=210)



#create done button
done_button=Button(win,text="Done",
                 font=("Times New Roman",20,"bold"),command=data_get)
done_button.place(x=150,y=190,width=100,height=50)



win.mainloop()
