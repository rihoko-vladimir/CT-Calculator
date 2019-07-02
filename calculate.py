from datetime import datetime
from dateutil.relativedelta import relativedelta as RD


f = "%Y/%m/%d/%H/%M/%S"
rus_ct = datetime.strptime("2020/6/13/11/0/0", f) #CT Date is variative, please re-check at rikc.by
phys_ct = datetime.strptime("2020/6/25/11/0/0", f)
math_ct = datetime.strptime("2020/6/17/11/0/0", f)
by_ct = datetime.strptime("2020/6/11/11/0/0", f)
com_ct = datetime.strptime("2020/6/15/11/0/0", f)
bio_ct = datetime.strptime("2020/6/19/11/0/0", f)
forlang_ct = datetime.strptime("2020/6/21/11/0/0", f)
chem_ct = datetime.strptime("2020/6/23/11/0/0", f)
by_hist_ct = datetime.strptime("2020/6/27/11/0/0", f)
geo_ct = datetime.strptime("2020/6/29/11/0/0", f)
hist_ct = datetime.strptime("2020/7/1/11/0/0", f)
def calculate(message):
    cur_time = datetime.now()
    if message == '/phys_ct':
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/by_ct':
        yleft = RD(by_ct, cur_time).years
        Mleft = RD(by_ct, cur_time).months
        dleft = RD(by_ct, cur_time).days
        hleft = RD(by_ct, cur_time).hours
        mleft = RD(by_ct, cur_time).minutes
        sleft = RD(by_ct, cur_time).seconds
        send = 'До ЦТ по Белорусскому языку осталось '
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/com_ct':
        yleft = RD(com_ct, cur_time).years
        Mleft = RD(com_ct, cur_time).months
        dleft = RD(com_ct, cur_time).days
        hleft = RD(com_ct, cur_time).hours
        mleft = RD(com_ct, cur_time).minutes
        sleft = RD(com_ct, cur_time).seconds
        send = 'До ЦТ по Обществоведению осталось '
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/bio_ct':
        yleft = RD(bio_ct, cur_time).years
        Mleft = RD(bio_ct, cur_time).months
        dleft = RD(bio_ct, cur_time).days
        hleft = RD(bio_ct, cur_time).hours
        mleft = RD(bio_ct, cur_time).minutes
        sleft = RD(bio_ct, cur_time).seconds
        send = 'До ЦТ по Биологии осталось '
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/forlang_ct':
        yleft = RD(forlang_ct, cur_time).years
        Mleft = RD(forlang_ct, cur_time).months
        dleft = RD(forlang_ct, cur_time).days
        hleft = RD(forlang_ct, cur_time).hours
        mleft = RD(forlang_ct, cur_time).minutes
        sleft = RD(forlang_ct, cur_time).seconds
        send = 'До ЦТ по Иностранному языку осталось '
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/chem_ct':
        yleft = RD(chem_ct, cur_time).years
        Mleft = RD(chem_ct, cur_time).months
        dleft = RD(chem_ct, cur_time).days
        hleft = RD(chem_ct, cur_time).hours
        mleft = RD(chem_ct, cur_time).minutes
        sleft = RD(chem_ct, cur_time).seconds
        send = 'До ЦТ по Химии осталось '
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/by_hist_ct':
        yleft = RD(by_hist_ct, cur_time).years
        Mleft = RD(by_hist_ct, cur_time).months
        dleft = RD(by_hist_ct, cur_time).days
        hleft = RD(by_hist_ct, cur_time).hours
        mleft = RD(by_hist_ct, cur_time).minutes
        sleft = RD(by_hist_ct, cur_time).seconds
        send = 'До ЦТ по Истории Беларуси осталось '
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/geo_ct':
        yleft = RD(geo_ct, cur_time).years
        Mleft = RD(geo_ct, cur_time).months
        dleft = RD(geo_ct, cur_time).days
        hleft = RD(geo_ct, cur_time).hours
        mleft = RD(geo_ct, cur_time).minutes
        sleft = RD(geo_ct, cur_time).seconds
        send = 'До ЦТ по Географии осталось '
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    elif message == '/hist_ct':
        yleft = RD(hist_ct, cur_time).years
        Mleft = RD(hist_ct, cur_time).months
        dleft = RD(hist_ct, cur_time).days
        hleft = RD(hist_ct, cur_time).hours
        mleft = RD(hist_ct, cur_time).minutes
        sleft = RD(hist_ct, cur_time).seconds
        send = 'До ЦТ по Всемирной Истории осталось '
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
            if mleft % 10 == 1 and mleft != 11:
                send += str(mleft) + " минута "
            elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
                send += str(mleft) + " минуты "
            else:
                send += str(mleft) + " минут "
        else:
            pass
        if sleft != 0:
            if sleft % 10 == 1 and sleft != 11:
                send += str(sleft) + " секунда "
            elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
                send += str(sleft) + " секунды "
            else:
                send += str(sleft) + " секунд "
        else:
            pass
    return send