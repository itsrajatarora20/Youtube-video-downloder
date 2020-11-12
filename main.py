from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size=0

def completed(stream=None,chunk=None,file_handle=None,remaining=None):
    #finding the percentage of completed file
    file_downloaded=(file_size-remaining)
    per= (file_downloaded/file_size)*100
    dbtn.config(text="{:.2f} % downloaded".format(per))


def startDownload():
    global file_size
    try:
        url= urlField.get()
        #changing button text
        dbtn.config(text="Please wait . . .")
        dbtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        # creating  youtube Object with url
        ob = YouTube(url , on_progress_callback=completed)
        #for high resolution video using first
        strm = ob.streams.first()
        file_size=strm.filesize
        print("Total size",file_size)
        strm.download(path_to_save_video)
        dbtn.config(text="Start Download")
        dbtn.config(state=NORMAL)
        showinfo("Downloaded Finished","Downloaded Successfully")
        urlField.delete(0,END)
    except Exception as e:
        print(e)
        print("Some Error")

def startThreading():
    thread=Thread(target=startDownload)
    thread.start()

#Starting GUI building
main=Tk()
main.geometry("600x500")
#Giving the title
main.title("Youtube Downloader")
main.iconbitmap('youtube.ico')

file=PhotoImage(file='headingimage.png')
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP,pady=5)

#url text entry field
urlField=Entry(main,font=("verdana",20),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10,pady=5)

dbtn=Button(main,text="Start Download",font=("verdana",18),relief="ridge",command=startThreading)
dbtn.pack(side=TOP,pady=8)


main.mainloop()