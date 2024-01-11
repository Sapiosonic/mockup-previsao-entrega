# Requisitos

# 1. pegar a data atual ok
# 2. separar em horas e minutos ok
# 3. verificar se o horario atual é hora cheia ok
    # se for, considerar esse horario ok
    # se não for desconsiderar minutos e segundos e adicionar 1 hora ok
# 4. retornar o horario inicial e começar a subtração das horas restantes
# 5. sempre que completar um dia verificar se o próximo dia é dia útil

from datetime import datetime

now = datetime.now()
current_time = now
hours = 0
sla = 18
working_hours = 8

def get_current_date():
    return print(now.strftime("%d-%m-%Y"))

def get_current_time(current_time):
    current_time = now.strftime("%H:%M:%S")

    if(int(current_time[4]) > 00):
        if(int(current_time[6]) > 00):
            current_time = now.strftime("%H")
            current_time_int = int(current_time)
            return current_time_int + 1
    else:
        current_time = now.strftime("%H")
        current_time_int = int(current_time)
        return current_time
    
hours = get_current_time(current_time)
print(hours)











# source https://www.programiz.com/python-programming/datetime/current-time