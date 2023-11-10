from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title('Weather App')
root.geometry('890x470+300+300')
root.configure(bg='#57adff')
#root.resizable(False,False)

#icon
def getWeather():
    city = textfield.get()
    # if city(city!="") -> can include a validation here
    geolocator = Nominatim(user_age="geoapiExercises")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)

    long_lat.config(text=f"{round(location.latitude,1)}N,{round(location.longitude,1)}E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # see lecture 8 to setup API
    # see lecture 11 -> to use one-call instead of standard API
    api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.latitude)+"&units=metric&exclude=hourly&appid={}"

    #lec-9 onwards
    json_data = requests.get(api).json()
    print(json_data)

    #current
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    # to test if API call is successful or not
    #print(temp)
    #print(humidity)
    #print(pressure)
    #print(speed)
    #print(description)

    t.config(text=(temp,"K"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(description))

    #days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

    # individual cells details

    # cell - 1
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    print(firstdayimage)
    photo1 = Image.Tk.PhotoImage(file=f"resources/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")

    # cell - 2
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    print(seconddayimage)
    img = (Image.open("f{secondaryimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo2 = Image.Tk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']

    day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")

    # cell - 3
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    print(thirddayimage)
    img = (Image.open("f{thirdimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo3 = Image.Tk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3= json_data['daily'][2]['temp']['night']

    day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")

    # cell - 4
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    print(fourthdayimage)
    img = (Image.open("f{fourthimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo4 = Image.Tk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4= json_data['daily'][3]['temp']['night']

    day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")

    # cell - 5
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    print(fifthdayimage)
    img = (Image.open("f{fifthimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo5 = Image.Tk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']

    day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")

    # cell - 6
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    print(sixthdayimage)
    img = (Image.open("f{sixthimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo6 = Image.Tk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6= json_data['daily'][5]['temp']['night']

    day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")

    # cell - 7
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
    print(seventhdayimage)
    img = (Image.open("f{seventhimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo7 = Image.Tk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7= json_data['daily'][6]['temp']['night']

    day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")

#icon
image_icon = PhotoImage(file="resources/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file="resources/rounded rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x=43,y=110)

#labels
t = Label(root,text="Teamperature",font=("Helvetica",11), fg="white",bg="#203243")
t.place(x=50,y=120)

h = Label(root,text="Humidity",font=("Helvetica",11), fg="white",bg="#203243")
h.place(x=50,y=140)

p = Label(root,text="Pressure",font=("Helvetica",11), fg="white",bg="#203243")
p.place(x=50,y=160)

w = Label(root,text="Wind Speed",font=("Helvetica",11), fg="white",bg="#203243")
w.place(x=50,y=180)

d = Label(root,text="Description",font=("Helvetica",11), fg="white",bg="#203243")
d.place(x=50,y=200)

#search_box

Search_image = PhotoImage(file="resources/rounded rectangle 3.png")
myimage = Label(image=Search_image,bg="#57adff")
myimage.place(x=290,y=109)

weath_image = PhotoImage(file="resources/layer 7.png")
weather_image = Label(root,image=weath_image,bg="#203242")
weather_image.place(x=308,y=114)

textfield = Entry(root,justify='center',width=15,font=("poppins",25,'bold'),bg="#203243",border=0,fg='white')

textfield.place(x=420,y=125)
textfield.focus()

Search_icon = PhotoImage(file="resources/layer 6.png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor='hand2',bg="#203243")
myimage_icon.place(x=650,y=111)

# bottom boxes
frame = Frame(root,width=900,height=100,bg='#212120')
frame.pack(side=BOTTOM)

firstbox = PhotoImage(file="resources/rounded rectangle 2.png")
secondbox = PhotoImage(file="resources/rounded rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=0)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=0)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=0)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=0)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=0)

#clock - to place time
clock = Label(root,text="2:30 PM",font=("Helvetica",30,'bold'),fg='white',bg="#57adff")
clock.place(x=43,y=30) # check if this is off screen or not

#timezone
timezone = Label(root,font=("Helvetica",30,'bold'),fg='white',bg="#57adff")
timezone.place(x=650,y=30)

#longitude and latitude

long_lat = Label(root,font=("Helvetica",30,'bold'),fg='white',bg="#57adff")
long_lat.place(x=680,y=30)

# cell window structure declared below

#first cell

firstframe = Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)
day1 = Label(firstframe,font="arial 15", bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage = Label(firstframe,bg="#282829")
firstimage.place(x=10,y=5)

day1temp = Label(firstframe,bg='#282829',fg="#57adff",font="arial 15 bold")
day1temp.place(x=100,y=50)

#second cell

secondframe = Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)
day2 = Label(secondframe, bg="#282829",fg="#fff")
day2.place(x=10,y=5)

secondimage = Label(secondframe,bg="#282829")
secondimage.place(x=10,y=5)

day2temp = Label(secondframe,bg='#282829',fg="#57adff")
day2temp.place(x=2,y=70)

#third cell

thirdframe = Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)
day3 = Label(thirdframe, bg="#282829",fg="#fff")
day3.place(x=10,y=5)

thirdimage = Label(thirdframe,bg="#282829")
thirdimage.place(x=10,y=5)

day3temp = Label(thirdframe,bg='#282829',fg="#57adff")
day3temp.place(x=2,y=70)


#fourth cell

fourthframe = Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505,y=325)
day4 = Label(fourthframe, bg="#282829",fg="#fff")
day4.place(x=10,y=5)

fourthimage = Label(fourthframe,bg="#282829")
fourthimage.place(x=10,y=5)

day4temp = Label(fourthframe,bg='#282829',fg="#57adff")
day4temp.place(x=2,y=70)

#fifth cell

fifthframe = Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)
day5 = Label(fifthframe, bg="#282829",fg="#fff")
day5.place(x=10,y=5)

fifthimage = Label(firstframe,bg="#282829")
fifthimage.place(x=10,y=5)

day5temp = Label(fifthframe,bg='#282829',fg="#57adff")
day5temp.place(x=2,y=70)

#sixth cell

sixthframe = Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)
day6 = Label(sixthframe, bg="#282829",fg="#fff")
day6.place(x=10,y=5)

sixthimage = Label(sixthframe,bg="#282829")
sixthimage.place(x=10,y=5)

day6temp = Label(sixthframe,bg='#282829',fg="#57adff")
day6temp.place(x=2,y=70)

#seventh cell

seventhframe = Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=805,y=325)
day7 = Label(seventhframe, bg="#282829",fg="#fff")
day7.place(x=10,y=5)

seventhimage = Label(firstframe,bg="#282829")
seventhimage.place(x=10,y=5)

day7temp = Label(seventhframe,bg='#282829',fg="#57adff")
day7temp.place(x=2,y=70)

mainloop()
