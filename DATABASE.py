import pandas as pd

def create_data():
    features = ['ID','Информация', 'Координата Х', 'Координата У', 'Связи','Сам объект']
    data = pd.DataFrame(0,index=[0], columns=features)
    return data

DATA = []

def add_line(label, data):

    pass

def download_line():

    pass

#Попробовать добавить такую функцию, которая бы копировала имеющиеся данные в буфер обмена