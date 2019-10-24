import threading, socket


class ultra_process(threading.Thread):

    def __init__(self,interface_gui):      # jusqua = donnée supplémentaire
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        self.color_text = interface_gui.color_text
        self.canvas_ultra = interface_gui.canvas_ultra

    def run(self):
        global ultra_data, canvas_text, canvas_rec
        self.ultra_HOST = ''
        self.ultra_PORT = 2257                            #Define port serial 
        self.ultra_ADDR = (self.ultra_HOST, self.ultra_PORT)
        self.ultra_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ultra_Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.ultra_Sock.bind(self.ultra_ADDR)
        self.ultra_Sock.listen(5)                      #Start server,waiting for client
        self.ultra_Sock, addr = self.ultra_Sock.accept()
        self.canvas_text=self.canvas_ultra.create_text((90,11),text='Ultrasonic OFF',fill=self.color_text)
        while 1:
            try:
                ultra_data = str(ultra_Sock.recv(BUFSIZ).decode())
                try: 
                    ultra_data = float(ultra_data)
                    if float(ultra_data) < 3:
                        #print(ultra_data)
                        try:
                            self.canvas_ultra.delete(canvas_text)
                            self.canvas_ultra.delete(canvas_rec)
                        except:
                            pass
                        #canvas_rec=canvas_ultra.create_rectangle(0,0,int(float(ultra_data)/145*3),30,fill = '#FFFFFF')
                        self.canvas_rec=canvas_ultra.create_rectangle(0,0,(352-int(float(ultra_data)*352/3)),30,fill = '#448AFF',width=0)
                        self.canvas_text=canvas_ultra.create_text((90,11),text='Ultrasonic Output: %sm'%ultra_data,fill=self.color_text)
                        #print('xxx')
                except:
                    pass
            except:
                pass

