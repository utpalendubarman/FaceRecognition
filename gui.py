import tkMessageBox
import face_detection as fd
import cv2
from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()
root.title("Attendence Management System")
root.geometry("700x600")
root.config(background="#ffffff")
logo = ImageTk.PhotoImage(Image.open("Resources/logo_icon.png"))
logo_img = Label(root, image = logo,background="#ffffff")
#recognizer=cv2.face_BPHFaceRecognizer.create()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#Function goes here
def new_register(name,id):
   print("Hello")
   print(name.get())

def take_face(img):
    face=face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5)
    if face is ():
        return None
    else:
        return face

def take_attendence():
    tkMessageBox.showinfo("Take Attendence", "This function is not available now")
def check_attendence():
    tkMessageBox.showinfo("Take Attendence", "This function is not available now")


def register_face():
    cap=cv2.VideoCapture(0)
    counter=0
    while(True):
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=take_face(gray)
        if face is not None:
            for (x,y,w,h) in face:
                color = (255, 0, 0)
                stroke = 2
                x2 = x + w
                y2 = y + h
                cv2.rectangle(frame, (x, y), (x2, y2), color, stroke)
                rest=50-counter;
                if rest==1:
                    cv2.putText(frame, "Finished", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, 255)
                else:
                    cv2.putText(frame,str(rest),(100,100),cv2.FONT_HERSHEY_COMPLEX,2,255)
                cv2.imshow("frame",frame)
                crop=gray[y:y+h,x:x+w]
                cv2.imwrite("face-data/"+str(counter)+".jpg",crop)
                counter+=1
            if cv2.waitKey(20) & 0xFFF ==ord('q'):
                break
            if counter==50:
                break


def register_user():
    ##NEW SEPERATE WINDOW FOR NEW USER REGISTRATION
    register=Tk()
    register.title("Register New User")
    register.geometry("500x400")
    register.config(background="#ffffff")
    id_label=Label(register,text="User ID", font=("Arial sans MS",14,"bold"),background="#ffffff")
    id_input=Entry(register,bd=2,width="30",font=("Arial sans MS",14))
    name_label=Label(register,text="User Name",font=("Arial sans MS",14,"bold"),background="#ffffff")
    name_input=Entry(register,bd=2,width="30",font=("Arial sans MS",14))
    take_face = Button(register,
                             text="Take Face",
                             width="30",
                             height="2",
                             background="#000000",
                             foreground="#ffffff",
                             activeforeground="#ff0000",
                            command=register_face
                              )
    complete_registration = Button(register,
                       text="Register",
                       width="30",
                       height="2",
                       background="#000000",
                       foreground="#ffffff",
                       activeforeground="#ff0000",
                       command=new_register(name_input, id_input)
                       )
    id_label.pack(pady=(30,0))
    id_input.pack()
    name_label.pack(pady=(30,0))
    name_input.pack()
    take_face.pack(pady="30")
    complete_registration.pack()
    register.mainloop()
def exit_app():
    root.destroy()

##COMPONENTS HERE

heading=Label(
    root,
    text="Attendence Management System",
    font=("Comic sans MS",24,"bold"),
    background="#ffffff"
)
take_attendence=Button(root,
                       text="Take Attendence",
                       width="30",
                       height="2",
                       background="#000000",
                       foreground="#ffffff",
                       activeforeground="#ff0000",
                       command=take_attendence)
check_attendence=Button(root,
                        text="Check Attendence",
                        width="30",
                        height="2",
                        background="#000000",
                        foreground="#ffffff",
                        activeforeground="#ff0000",
                        command=check_attendence
                        )
register_user=Button(root,
                     text="Register New User",
                     width="30",
                     height="2",
                     background="#000000",
                     foreground="#ffffff",
                     activeforeground="#ff0000",
                     command=register_user
                     )
exit_btn=Button(root,
                text="Exit",
                width="30",
                height="2",
                background="#000000",
                foreground="#ffffff",
                activeforeground="#ff0000",
                command=exit_app
                )
logo_img.pack(pady="30")
heading.pack(pady=(0,30))
take_attendence.pack(pady=(0,30))
check_attendence.pack(pady=(0,30))
register_user.pack(pady=(0,30))
exit_btn.pack(pady=(0,30))
root.mainloop()