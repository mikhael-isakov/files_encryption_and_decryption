import datetime as dt 



class date_time(dt.datetime): 
    # 
    # Класс является расширением класса datetime библиотеки datetime 
    #
    @property 
    def nice_view(self):
        return self.strftime('%Y.%m.%d %H:%M:%S')