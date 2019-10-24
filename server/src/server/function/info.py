import os, psutil, time


class Information():

    def get_cpu_tempfunc(self):
        """ Return CPU temperature """
        result = 0
        mypath = "/sys/class/thermal/thermal_zone0/temp"
        with open(mypath, 'r') as mytmpfile:
            for line in mytmpfile:
                result = line

        result = float(result)/1000
        result = round(result, 1)
        return str(result)


    def get_gpu_tempfunc(self):
        """ Return GPU temperature as a character string"""
        res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
        return res.replace("temp=", "")


    def get_cpu_use(self):
        """ Return CPU usage using psutil"""
        cpu_cent = psutil.cpu_percent()
        return str(cpu_cent)


    def get_ram_info(self):
        """ Return RAM usage using psutil """
        ram_cent = psutil.virtual_memory()[2]
        return str(ram_cent)


    def get_swap_info(self):
        """ Return swap memory  usage using psutil """
        swap_cent = psutil.swap_memory()[3]
        return str(swap_cent)


    def info_get(self):
        global cpu_t,cpu_u,gpu_t,ram_info
        while 1:
            cpu_t = self.get_cpu_tempfunc()
            cpu_u = self.get_cpu_use()
            ram_info = self.get_ram_info()
            time.sleep(3)


        






