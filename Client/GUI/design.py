
from socket import *
import sys
import time
import threading
import tkinter as tk
from network.connect_mqtt import connexion_mqtt

from GUI.button import gui_button
stat=0
class gui():

    def __init__(self):      # jusqua = donnée supplémentaire
      # (appel au constructeur de la classe mère)
        self.ip_stu=0        #Shows connection status
        self.color_bg='#000000'        #Set background color
        self.color_text='#E1F5FE'      #Set text color
        self.color_btn='#0277BD'       #Set button color
        self.color_line='#01579B'      #Set line color
        self.color_can='#212121'       #Set canvas color
        self.color_oval='#2196F3'      #Set oval color
        self.target_color='#FF6D00'

        self.root = tk.Tk()            #Define a window named root
        self.root.title('Adeept RaspTank')      #Main window title
        self.root.geometry('800x600')  #Main window size, middle of the English letter x.
        self.root.config(bg=self.color_bg)  #Set the background color of root window

#BOUTON

        self.Btn0 = tk.Button(self.root, width=8, text='Forward',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn1 = tk.Button(self.root, width=8, text='Backward',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn2 = tk.Button(self.root, width=8, text='Left',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn3 = tk.Button(self.root, width=8, text='Right',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_RightSide = tk.Button(self.root, width=8, text='-->',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_LeftSide = tk.Button(self.root, width=8, text='<--',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_up = tk.Button(self.root, width=8, text='Up',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_down = tk.Button(self.root, width=8, text='Down',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_left = tk.Button(self.root, width=8, text='Grab',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_right = tk.Button(self.root, width=8, text='Loose',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_home = tk.Button(self.root, width=8, text='Home',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_Cleft = tk.Button(self.root, width=8, text='\\',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.Btn_Cright = tk.Button(self.root, width=8, text='/',fg=self.color_text,bg=self.color_btn,relief='ridge')
        self.canvas_cover=tk.Canvas(self.root,bg=self.color_bg,height=30,width=510,highlightthickness=0)
        try:
            self.logo =self.tk.PhotoImage(file = 'logo.png')         #Define the picture of logo,but only supports '.png' and '.gif'
            self.l_logo=self.tk.Label(root,image = self.logo,bg=self.color_bg) #Set a label to show the logo picture
            self.l_logo.place(x=30,y=13)                        #Place the Label in a right position
        except:
            pass


        self.E1 = tk.Entry(self.root,show=None,width=16,bg="#37474F",fg='#eceff1')

        self.canvas_ultra=tk.Canvas(self.root,bg=self.color_btn,height=23,width=352,highlightthickness=0)
        self.CPU_TEP_lab=tk.Label(self.root,width=18,text='CPU Temp:',textvariable=connexion_mqtt.on_message,fg=self.color_text,bg='#212121')
        self.CPU_USE_lab=tk.Label(self.root,width=18,text='CPU Usage:',fg=self.color_text,bg='#212121')
        self.RAM_lab=tk.Label(self.root,width=18,text='RAM Usage:',fg=self.color_text,bg='#212121')
        self.l_ip=tk.Label(self.root,width=18,text='Status',fg=self.color_text,bg=self.color_btn)
        self.l_ip_3=tk.Label(self.root,width=10,text='IP Address:',fg=self.color_text,bg='#000000')
        self.l_ip_4=tk.Label(self.root,width=18,text='Disconnected',fg=self.color_text,bg='#F44336')
        self.l_ip_5=tk.Label(self.root,width=18,text='Use default IP',fg=self.color_text,bg=self.color_btn)
        self.label_ins=tk.Label(self.root,width=71,text='Instruction',fg=self.color_text,bg=self.color_btn)
        self.label_openCV=tk.Label(self.root,width=28,text='OpenCV Status',fg=self.color_text,bg=self.color_btn)


        self.place()



        self.instruction()


    def place(self):
            self.Btn0.place(x=100,y=195)
            self.Btn1.place(x=100,y=230)
            self.Btn2.place(x=30,y=230)
            self.Btn3.place(x=170,y=230)
            self.Btn_LeftSide.place(x=30,y=195)
            self.Btn_RightSide.place(x=170,y=195)
            self.Btn_up.place(x=400,y=195)
            self.Btn_down.place(x=400,y=230)
            self.Btn_left.place(x=330,y=230)
            self.Btn_right.place(x=470,y=230)
            self.Btn_home.place(x=250,y=230)
            self.Btn_Cleft.place(x=330, y=195)
            self.Btn_Cright.place(x=470, y=195)
            self.CPU_TEP_lab.place(x=400,y=15)                         #Define a Label and put it in position
            self.CPU_USE_lab.place(x=400,y=45)                         #Define a Label and put it in position
            self.RAM_lab.place(x=400,y=75)                         #Define a Label and put it in position
            self.l_ip.place(x=30,y=110)                           #Define a Label and put it in position
            self.E1.place(x=180,y=40)                             #Define a Entry and put it in position
            self.l_ip_4.place(x=400,y=110)                         #Define a Label and put it in position
            self.canvas_ultra.place(x=30,y=145)
            self.l_ip_5.place(x=400,y=145)                         #Define a Label and put it in position
            self.label_ins.place(x=30,y=300)                         #Define a Label and put it in position
            self.l_ip_3.place(x=175,y=15)                         #Define a Label and put it in position
            self.label_openCV.place(x=180,y=110)                         #Define a Label and put it in position


            self.canvas_cover.place(x=30,y=420)

    def instruction(self):
        self.instructions = []
        self.instruction_1 = 'You can use shortcuts to control the robot'
        self.instructions.append(self.instruction_1)
        self.instruction_2 = 'W: Forward   S: Backward   A: Turn left   D: Turn right'
        self.instructions.append(self.instruction_2)
        self.instruction_3 = 'I: Look up   K: Look down   J: Grab   L: Loose'
        self.instructions.append(self.instruction_3)
        self.instruction_4 = 'Q: Hand reaches out   E: Hand takes back   U & O: Hand rotation'
        self.instructions.append(self.instruction_4)
        self.instruction_5 = 'F(the Home button on GUI): Arm and head return to original positionl position'
        self.instructions.append(self.instruction_5)
        self.instruction_6 = 'then the PWM of servos will be set to 0'
        self.instructions.append(self.instruction_6)
        self.instruction_7 = 'for better battery and servo maintenance'
        self.instructions.append(self.instruction_7)
        self.instruction_8 = 'Test Version, no openCV functions'
        self.instructions.append(self.instruction_8)

        for ins_show in self.instructions:
            self.label_ins.config(text=ins_show)





                      #GUI

            ################################
            #canvas_rec=canvas_ultra.create_rectangle(0,0,340,30,fill = '#FFFFFF',width=0)
            #canvas_text=canvas_ultra.create_text((90,11),text='Ultrasonic Output: 0.75m',fill=color_text)
            ################################
