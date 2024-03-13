#  My News Application:-
#importing libraries/modules
import io
import requests
import webbrowser
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

class NewsApp:
    
    def __init__(self):
        #fetching data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=3a4d1740d8c04a148aa86cda5e1d00e3').json()
        #load GUI
        self.load_gui()
        self.load_news_item(0)

#gui main
    def load_gui(self):
        self.root = Tk()
        self.root.geometry('450x600')
        self.root.title('My News Application')
        self.root.resizable(0,0)
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
            
    def load_news_item(self,index):
        self.clear()


#image error handling
        try:
            img_url=self.data['articles'][index]['urlToImage']
            raw_data= urlopen(img_url).read()
            im = Image.open( io.BytesIO(raw_data)).resize((400,300))
            photo=ImageTk.PhotoImage(im)

        except:
            img_url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQYAAADACAMAAADRLT0TAAAATlBMVEX///+ysrLLy8uvr6/5+fm4uLj8/PzExMTn5+fBwcG7u7vX19f19fXj4+Pc3NyXl5fR0dGmpqbKysrr6+uSkpLv7++enp6Li4uioqKAgIAhIPmjAAAEJUlEQVR4nO3ci3KjIBQGYBBUEFE0Mem+/4vuORhNvOylM7sl1f+baVI1yXBOEBBshQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeGOmrMpL6kIk1ysllQqpi5FYpiRTLnVBkjJjFigPQ+qipJTLSZW6KAk1ak6D8qkLk0zxzAJJXZpkwmsaTttK1ovKIKVOXaA0ymUaVJa6QElcVpXhpJ2mles0lKmLlICfR05q/s2kLtSXKx4jJ2VN7adR1PnGUO5RBfKCNuqzjqH0FPh4bdlP50XiYn21x5XlNGiaN891xT2PnNa1QZ1qDGXnsPtxWy63z+Fl5GR5u6hOOYZ6Rj32FPq5rWzqwn2Zl2mGsTF4vcg6zRiqeM45UdQ8K+1fLy/OMoZyi2mGZnfP8dXyVewxs8XFZn6KTnMZc7ystNvMHN2wmmaoVo0F56FOXcj/z65nW6i/XO06wRjKbOacis2k5AnGUKv6H0PepObwnWaziVj5/Z1HVqzjjcMEt0mDzFOX9L8K24BlOWwmZw++eLNpC8eQ93YeefGm34tY7efmuGOozQJNjLd0m6FE3H/YMdReuPFb36slh1288btfOl9ob3vM6cgBVTuxjrMs+2k45jzUbssgpdWi3k3QQVuHnUFSDDbfT8JR51/2hk6/dcwhFNIQba8j/5SGY15ul5/Lw1FvAiqC+gR53NF03YTs74TmkL0lAAAAAAAAfIYp87+eRPzlC5vxMrsp/kGBkrCt86r7w4v6Mf6i/VWYYVysuWphv+Uav2n5kdeiCs+TaLXQvBKhRWFiyDU/6TyL0wlzGvTjoI8LuNoLN6ah1VoGfunAazeFLgwf/QZVRMbvmUJ316qTFEgp82stcttVd4pB3qqrE67tYphTGiraS4mTH/ZK331G7ywfaSjopVYUneIPcYo+y3T5/f2nZLppyS1QhN0gWkenQCmqnCpKR4FQ7FTTy8VJ4fkcumvNVagVA9endrwLrNWiopfaEN/d3ChH9BPefz1rToO4uNBeOBDhpeBWs+5EvJmHHuw49/5IA0cad3mX3YXjILPppIgHP0LT+B/CVdRo0lH//vfCjCcFNQlSBt8ZwYE+0jB0ouN2gn5fpiH2LKWrb6Uz97F1DIs03PoQgosJ4jQ0758Gf+NH29cf9HRb1AZKQ891va2faYhPgW98a4eMDtZ3rv1UYxZpiOu9w3dKg8hv/lJdKYLsYlvDXd6cBsrMPRhFQYQ2/rlAcXWkppbA5J0wV9/kdzqvcmPV3GGGmxHDvfEffTwp4onxDdIgfBVv3dClHTy17gX3g4I7T811v48NgXDjWkzo+57/wU2ouHqYKhP81pD7evyrCn6340pSVtSqDC8/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb+cnJPojNOxxqCEAAAAASUVORK5CYII="
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 270))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image=photo)
        label.pack(pady=(20,20))

#news heading
        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

#news content
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

#buttons
        if index != 0:
            prev = Button(frame,text='Prev.',width=16,height=3,command=lambda:self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame,text = 'Read More.', width = 16, height = 3,command= lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame,text = 'Next.', width = 16, height = 3,command=lambda:self.load_news_item(index + 1))
            next.pack(side=LEFT)

        self.root.mainloop()
        
    def open_link(self,url):
        webbrowser.open(url)
#global object        
obj = NewsApp()

                                  