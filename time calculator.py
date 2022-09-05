
def add_time(start,duration,day=None):
    days={"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
    #--------particion de la informacion 
    x=start.split()
    hora1=x[0].split(":")
    horario=x[1]
    hora2=duration.split(":")
    # --------transformar a formato 24 Hrs---------------------
    hora_actual=int(hora1[0])
    if horario=="PM":
        hora_actual+=12
    #---------Sumar horas y minutos
    minutos=int(hora1[1])+int(hora2[1])
    horas_acumuladas=0
    if minutos>59:
        horas_acumuladas=minutos//60
        minutos-=(60*horas_acumuladas)
    hora_actual+=horas_acumuladas
    # print("HORA ACTUAL 1: ",hora_actual,"MINUTOS: ",minutos)
    dias=0
    #------normalizar HRs y DIAS-----
    dias=int(hora2[0])//24
    horas_restantes=int(hora2[0])-(dias*24)
    hora_actual+=horas_restantes
    # print(hora_actual,"-****-")
    #----CASO PASADO MEDIA NOCHE
    if hora_actual==24:
        hora_actual=hora_actual-12
        dias+=1
        horario="AM"
    #-----CASO DONDE ESTA ESTRE 12 y 24------
    elif hora_actual>12 and hora_actual<24:
        hora_actual-=12
        horario="PM"
    #---CASO DONDE ES 12------
    elif hora_actual==12:
        horario="PM"
    #----caso donde es mayor de 24-----
    elif hora_actual>24:
        hora_actual-=24
        dias+=1
        horario="AM"
    if minutos<10:
        minutos="0"+str(minutos)
    else:
        minutos=str(minutos)
    #--------Obtener el dia que finaliza----------
    d=0
    dn=0
    df=""
    HORA=""
    if day!=None:
        d=days[day.lower()]
        if dias>1:
            dn=d+dias
            print(dn,"D____N")
            if dn>7:
                dn=dn%7
                for k,v in days.items():
                    if v==dn:
                        df=k.capitalize()
            else:    
                for k,v in days.items():
                    if v==dn:
                        df=k.capitalize()     
            HORA=str(hora_actual)+":"+minutos+" "+horario+", "+df+" ("+str(dias)+" days later)"
        elif dias==1:
            dn=d+dias
            for k,v in days.items():
                    if v==dn:
                        df=k.capitalize()
            HORA=str(hora_actual)+":"+minutos+" "+horario+", "+df+" (next day)"
        elif dias<1:
            HORA=str(hora_actual)+":"+minutos+" "+horario+", "+day.capitalize()
    else:
        if dias>1: 
            HORA=str(hora_actual)+":"+minutos+" "+horario+" ("+str(dias)+" days later)"
        elif dias==1:
            HORA=str(hora_actual)+":"+minutos+" "+horario+" (next day)"
        elif dias<1:
            HORA=str(hora_actual)+":"+minutos+" "+horario
    # print("RESTANTE: ",dn)
    # print("------------------------------------")
    # print("DIA INICIO: ",day,"-",d," DIA FINALIZACION",df)
    # print("------------------------------------")
    # print("HORA ACTUAL 2: ",hora_actual,"HORAS RESTANTES :",horas_restantes,)     
    # print("HORA: ",hora_actual," MINUTOS: ",minutos,"HORARIO: ",horario,"DIAS:",dias,)
    return HORA
print(add_time("11:59 PM", "24:05", "Wednesday"))