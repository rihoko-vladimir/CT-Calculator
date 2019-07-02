from datetime import datetime
from dateutil.relativedelta import relativedelta as RD


f = "%Y/%m/%d/%H/%M/%S"
rus_ct = datetime.strptime("2020/6/13/11/0/0", f) #CT Date is variative, please re-check at rikc.by
phys_ct = datetime.strptime("2020/6/25/11/0/0",f)
math_ct = datetime.strptime("2020/6/17/11/0/0",f)
cur_time = datetime.now()
def calculate(message):
    if message == '/start' or message =='/help':
        return "/rus_ct - отображение оставшегося времени до начала ЦТ по предмету 'Русский язык'.\n/math_ct - отображение оставшегося времени до начала ЦТ по предмету 'Математика'.\n/phys_ct - отображение оставшегося времени до начала ЦТ по предмету 'Физика'.\n/help - отображение списка доступных команд.\n"
    elif message == '/phys_ct':
        yleft = RD(phys_ct, cur_time).years
        Mleft = RD(phys_ct, cur_time).months
        dleft = RD(phys_ct, cur_time).days
        hleft = RD(phys_ct, cur_time).hours
        mleft = RD(phys_ct, cur_time).minutes
        sleft = RD(phys_ct, cur_time).seconds
        send = 'До ЦТ по физике осталось '
        if yleft != 0:
            send += str(yleft) + " год "
        else:
            pass
        if Mleft != 0:
            if Mleft == 1:
                send += str(Mleft) + " месяц "
            elif Mleft == 2 or Mleft == 3 or Mleft == 4:
                send += str(Mleft) + " месяца "
            elif Mleft >4 and Mleft <= 12:
                send += str(Mleft) + " месяцев "
            else:
                pass
        else:
            pass
        if dleft != 0:
            if dleft == 1 or dleft == 21 or dleft == 31:
                send += str(dleft) + " день "
            elif dleft == 2 or dleft == 3 or dleft == 4 or dleft == 22 or dleft == 23 or dleft == 24:
                send += str(dleft) + " дня "
            elif (dleft >4 and dleft <= 20) or (dleft > 24 and dleft < 31):
                send += str(dleft) + " дней "
            else:
                pass
        else:
            pass
        if hleft != 0:
            if hleft == 1 or hleft == 21:
                send += str(hleft) + " час "
            elif hleft == 2 or hleft == 3 or hleft == 4 or hleft == 22 or hleft == 23 or hleft == 24:
                send += str(hleft) + " часа "
            elif (hleft >4 and hleft <= 20):
                send += str(hleft) + " часов "
            else:
                pass
        else:
            pass
        if mleft != 0:
            send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/math_ct':
        yleft = RD(math_ct, cur_time).years
        Mleft = RD(math_ct, cur_time).months
        dleft = RD(math_ct, cur_time).days
        hleft = RD(math_ct, cur_time).hours
        mleft = RD(math_ct, cur_time).minutes
        sleft = RD(math_ct, cur_time).seconds
        send = 'До ЦТ по математике осталось '
        if yleft != 0:
            send += str(yleft) + " год "
        else:
            pass
        if Mleft != 0:
            if Mleft == 1:
                send += str(Mleft) + " месяц "
            elif Mleft == 2 or Mleft == 3 or Mleft == 4:
                send += str(Mleft) + " месяца "
            elif Mleft >4 and Mleft <= 12:
                send += str(Mleft) + " месяцев "
            else:
                pass
        else:
            pass
        if dleft != 0:
            if dleft == 1 or dleft == 21 or dleft == 31:
                send += str(dleft) + " день "
            elif dleft == 2 or dleft == 3 or dleft == 4 or dleft == 22 or dleft == 23 or dleft == 24:
                send += str(dleft) + " дня "
            elif (dleft >4 and dleft <= 20) or (dleft > 24 and dleft < 31):
                send += str(dleft) + " дней "
            else:
                pass
        else:
            pass
        if hleft != 0:
            if hleft == 1 or hleft == 21:
                send += str(hleft) + " час "
            elif hleft == 2 or hleft == 3 or hleft == 4 or hleft == 22 or hleft == 23 or hleft == 24:
                send += str(hleft) + " часа "
            elif (hleft >4 and hleft <= 20):
                send += str(hleft) + " часов "
            else:
                pass
        else:
            pass
        if mleft != 0:
            send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/rus_ct':
        yleft = RD(rus_ct, cur_time).years
        Mleft = RD(rus_ct, cur_time).months
        dleft = RD(rus_ct, cur_time).days
        hleft = RD(rus_ct, cur_time).hours
        mleft = RD(rus_ct, cur_time).minutes
        sleft = RD(rus_ct, cur_time).seconds
        send = 'До ЦТ по русскому языку осталось '
        if yleft != 0:
            send += str(yleft) + " год "
        else:
            pass
        if Mleft != 0:
            if Mleft == 1:
                send += str(Mleft) + " месяц "
            elif Mleft == 2 or Mleft == 3 or Mleft == 4:
                send += str(Mleft) + " месяца "
            elif Mleft >4 and Mleft <= 12:
                send += str(Mleft) + " месяцев "
            else:
                pass
        else:
            pass
        if dleft != 0:
            if dleft == 1 or dleft == 21 or dleft == 31:
                send += str(dleft) + " день "
            elif dleft == 2 or dleft == 3 or dleft == 4 or dleft == 22 or dleft == 23 or dleft == 24:
                send += str(dleft) + " дня "
            elif (dleft >4 and dleft <= 20) or (dleft > 24 and dleft < 31):
                send += str(dleft) + " дней "
            else:
                pass
        else:
            pass
        if hleft != 0:
            if hleft == 1 or hleft == 21:
                send += str(hleft) + " час "
            elif hleft == 2 or hleft == 3 or hleft == 4 or hleft == 22 or hleft == 23 or hleft == 24:
                send += str(hleft) + " часа "
            elif (hleft >4 and hleft <= 20):
                send += str(hleft) + " часов "
            else:
                pass
        else:
            pass
        if mleft != 0:
            send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            send += str(sleft) + " секунд "
        else:
            pass
    else:
        send = "Неизвестная команда. Напишие /help для вывода списка доступных команд.\n"
    return send
print(calculate('/phys_ct'))