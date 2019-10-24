import threading


class information_process(threading.Thread):

    def Info_receive(self):
        global CPU_TEP,CPU_USE,RAM_USE
        HOST = ''
        INFO_PORT = 2256                            #Define port serial 
        ADDR = (HOST, INFO_PORT)
        InfoSock = socket(AF_INET, SOCK_STREAM)
        InfoSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        InfoSock.bind(ADDR)
        InfoSock.listen(5)                      #Start server,waiting for client
        InfoSock, addr = InfoSock.accept()
        print('Info connected')
        while 1:
            try:
                info_data = ''
                info_data = str(InfoSock.recv(BUFSIZ).decode())
                info_get = info_data.split()
                CPU_TEP,CPU_USE,RAM_USE= info_get
                print('cpu_tem:%s\ncpu_use:%s\nram_use:%s'%(CPU_TEP,CPU_USE,RAM_USE))
                CPU_TEP_lab.config(text='CPU Temp: %s℃'%CPU_TEP)
                CPU_USE_lab.config(text='CPU Usage: %s'%CPU_USE)
                RAM_lab.config(text='RAM Usage: %s'%RAM_USE)
            except:
                pass

