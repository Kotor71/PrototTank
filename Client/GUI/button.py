import threading,time
import tkinter as tk

from command.control import control_process
start = 0
class gui_button():

        def __init__(self, client, interface):
                self.client = client
                self.control = control_process(self.client)
                var_R = tk.StringVar()
                var_R.set(0)

                Scale_R = tk.Scale(interface.root,label=None,
                from_=0,to=255,orient=tk.HORIZONTAL,length=505,
                showvalue=1,tickinterval=None,resolution=1,variable=var_R,troughcolor='#F44336',command=control_process.set_R,fg=interface.color_text,bg=interface.color_bg,highlightthickness=0)
                Scale_R.place(x=30,y=330)                            #Define a Scale and put it in position

                var_G = tk.StringVar()
                var_G.set(0)

                Scale_G = tk.Scale(interface.root,label=None,
                from_=0,to=255,orient=tk.HORIZONTAL,length=505,
                showvalue=1,tickinterval=None,resolution=1,variable=var_G,troughcolor='#00E676',command=control_process.set_G,fg=interface.color_text,bg=interface.color_bg,highlightthickness=0)
                Scale_G.place(x=30,y=360)                            #Define a Scale and put it in position

                var_B = tk.StringVar()
                var_B.set(0)

                Scale_B = tk.Scale(interface.root,label=None,
                from_=0,to=255,orient=tk.HORIZONTAL,length=505,
                showvalue=1,tickinterval=None,resolution=1,variable=var_B,troughcolor='#448AFF',command=control_process.set_B,fg=interface.color_text,bg=interface.color_bg,highlightthickness=0)
                Scale_B.place(x=30,y=390)                            #Define a Scale and put it in position

                Btn_Steady = tk.Button(interface.root, width=10, text='Ultrasonic',fg=interface.color_text,bg=interface.color_btn,relief='ridge')
                Btn_Steady.place(x=30,y=445)
                interface.root.bind('<KeyPress-z>', control_process.call_steady)
                Btn_Steady.bind('<ButtonPress-1>', control_process.call_steady)
                
                Btn_FindColor = tk.Button(interface.root, width=10, text='FindColor',fg=interface.color_text,bg=interface.color_btn,relief='ridge')
                Btn_FindColor.place(x=115,y=445)
                interface.root.bind('<KeyPress-z>', control_process.call_FindColor)
                Btn_FindColor.bind('<ButtonPress-1>', control_process.call_FindColor)
                
                Btn_WatchDog = tk.Button(interface.root, width=10, text='WatchDog',fg=interface.color_text,bg=interface.color_btn,relief='ridge')
                Btn_WatchDog.place(x=200,y=445)
                interface.root.bind('<KeyPress-z>', control_process.call_WatchDog)
                Btn_WatchDog.bind('<ButtonPress-1>', control_process.call_WatchDog)

                Btn_Fun4 = tk.Button(interface.root, width=10, text='FindLine',fg=interface.color_text,bg=interface.color_btn,relief='ridge')
                Btn_Fun4.place(x=285,y=445)
                interface.root.bind('<KeyPress-z>', control_process.call_FindLine)
                Btn_Fun4.bind('<ButtonPress-1>', control_process.call_FindLine)
                Btn_Fun5 = tk.Button(interface.root, width=10, text='Function 5',fg=interface.color_text,bg=interface.color_btn,relief='ridge')
                Btn_Fun5.place(x=370,y=445)
                interface.root.bind('<KeyPress-z>', control_process.call_WatchDog)
                Btn_Fun5.bind('<ButtonPress-1>', control_process.call_WatchDog)
                Btn_Fun6 = tk.Button(interface.root, width=10, text='Function 6',fg=interface.color_text,bg=interface.color_btn,relief='ridge')
                Btn_Fun6.place(x=455,y=445)
                interface.root.bind('<KeyPress-z>', control_process.call_WatchDog)
                Btn_Fun6.bind('<ButtonPress-1>', control_process.call_WatchDog)


                Btn_Steady.config(bg='#FF6D00', fg='#000000')
                Btn_FindColor.config(bg='#FF6D00', fg='#000000')
                Btn_WatchDog.config(bg='#FF6D00', fg='#000000')
                Btn_Fun4.config(bg='#FF6D00', fg='#000000')
                Btn_Fun5.config(bg='#FF6D00', fg='#000000')
                Btn_Fun6.config(bg='#FF6D00', fg='#000000')


                Btn_Steady.config(bg=interface.color_btn, fg=interface.color_text)
                Btn_FindColor.config(bg=interface.color_btn, fg=interface.color_text)
                Btn_WatchDog.config(bg=interface.color_btn, fg=interface.color_text)
                Btn_Fun4.config(bg=interface.color_btn, fg=interface.color_text)
                Btn_Fun5.config(bg=interface.color_btn, fg=interface.color_text)
                Btn_Fun6.config(bg=interface.color_btn, fg=interface.color_text)
                interface.Btn_LeftSide.bind('<ButtonPress-1>', control_process.call_LeftSide)
                interface.Btn_LeftSide.bind('<ButtonRelease-1>',control_process.call_Turn_stop)
                interface.Btn_RightSide.bind('<ButtonPress-1>', control_process.call_RightSide)
                interface.Btn_RightSide.bind('<ButtonRelease-1>', control_process.call_Turn_stop)
                interface.Btn0.bind('<ButtonPress-1>', control_process.call_forward)
                interface.Btn1.bind('<ButtonPress-1>', control_process.call_back)
                interface.Btn2.bind('<ButtonPress-1>', control_process.call_Left)
                interface.Btn3.bind('<ButtonPress-1>', control_process.call_Right)

                interface.Btn0.bind('<ButtonRelease-1>', control_process.call_FB_stop)
                interface.Btn1.bind('<ButtonRelease-1>', control_process.call_FB_stop)
                interface.Btn2.bind('<ButtonRelease-1>', control_process.call_Turn_stop)
                interface.Btn3.bind('<ButtonRelease-1>', control_process.call_Turn_stop)

                interface.root.bind('<KeyPress-z>', control_process.call_forward) 
                interface.root.bind('<KeyPress-a>', control_process.call_Left)
                interface.root.bind('<KeyPress-d>', control_process.call_Right)
                interface.root.bind('<KeyPress-s>', control_process.call_back)

                interface.root.bind('<KeyPress-q>', control_process.call_LeftSide)
                interface.root.bind('<KeyPress-e>', control_process.call_RightSide)
                interface.root.bind('<KeyRelease-q>', control_process.call_Turn_stop)
                interface.root.bind('<KeyRelease-e>', control_process.call_Turn_stop)

                interface.root.bind('<KeyRelease-z>', control_process.call_FB_stop)
                interface.root.bind('<KeyRelease-a>', control_process.call_Turn_stop)
                interface.root.bind('<KeyRelease-d>', control_process.call_Turn_stop)
                interface.root.bind('<KeyRelease-s>', control_process.call_FB_stop)

                interface.root.bind('<KeyPress-u>', control_process.call_CLeft) 
                interface.root.bind('<KeyPress-o>', control_process.call_CRight)
                interface.root.bind('<KeyPress-i>', control_process.call_headup) 
                interface.root.bind('<KeyPress-k>', control_process.call_headdown)
                interface.root.bind('<KeyPress-j>', control_process.call_headleft)
                interface.root.bind('<KeyPress-l>', control_process.call_headright)
                interface.root.bind('<KeyPress-f>', control_process.call_headhome)
                interface.Btn_Cleft.bind('<ButtonPress-1>', control_process.call_CLeft)
                interface.Btn_Cright.bind('<ButtonPress-1>', control_process.call_CRight)
                interface.Btn_up.bind('<ButtonPress-1>', control_process.call_headup)
                interface.Btn_down.bind('<ButtonPress-1>', control_process.call_headdown)
                interface.Btn_left.bind('<ButtonPress-1>', control_process.call_headleft)
                interface.Btn_right.bind('<ButtonPress-1>', control_process.call_headright)
                interface.Btn_home.bind('<ButtonPress-1>', control_process.call_headhome)