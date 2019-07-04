from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta as RD
f = "%Y/%m/%d/%H/%M/%S"
ct_date = {
            "rus_ct" : datetime.strptime("2020/6/13/11/0/0", f), #CT Date is variative, please re-check at rikc.by
            "phys_ct" : datetime.strptime("2020/6/25/11/0/0", f),
            "math_ct" : datetime.strptime("2020/6/17/11/0/0", f),
            "by_ct" : datetime.strptime("2020/6/11/11/0/0", f),
            "com_ct" : datetime.strptime("2020/6/15/11/0/0", f),
            "bio_ct" : datetime.strptime("2020/6/19/11/0/0", f),
            "forlang_ct" : datetime.strptime("2020/6/21/11/0/0", f),
            "chem_ct" : datetime.strptime("2020/6/23/11/0/0", f),
            "by_hist_ct" : datetime.strptime("2020/6/27/11/0/0", f),
            "geo_ct" : datetime.strptime("2020/6/29/11/0/0", f),
            "hist_ct" : datetime.strptime("2020/7/1/11/0/0", f)}
template = {"main" : "До ЦТ по предмету %s осталось ",
            "rus_ct" : "'Русский язык'",
            "phys_ct" : "'Физика'",
            "math_ct" : "'Математика'",
            "by_ct" : "'Белорусский язык'",
            "com_ct" : "'Обществоведение'",
            "bio_ct" : "'Биология'",
            "forlang_ct" : "'Иностранный язык'",
            "chem_ct" : "'Химия'",
            "by_hist_ct" : "'История Беларуси'",
            "geo_ct" : "'География'",
            "hist_ct" : "'История'",
            "min" : " минут%s ",
            "months" : " месяц%s ",
            "hour" : " час%s ",
            "sec" : " секунд%s "}
def calc(name):
    curtime = datetime.now()
    return {
        'rus_ct': RD(ct_date["rus_ct"], curtime),
        'phys_ct': RD(ct_date["phys_ct"], curtime),
        'math_ct': RD(ct_date["math_ct"], curtime),
        'by_ct': RD(ct_date["by_ct"], curtime),
        'com_ct': RD(ct_date["com_ct"], curtime),
        'bio_ct': RD(ct_date["bio_ct"], curtime),
        'forlang_ct': RD(ct_date["forlang_ct"], curtime),
        'chem_ct': RD(ct_date["chem_ct"], curtime),
        "by_hist_ct": RD(ct_date["by_hist_ct"], curtime),
        "geo_ct": RD(ct_date["geo_ct"], curtime),
        "hist_ct": RD(ct_date["hist_ct"], curtime)}[name]
def calculate(a):
    left=calc(a)
    send = template["main"]%(template[a])
    yleft = left.years
    Mleft = left.months
    dleft = left.days
    hleft = left.hours
    mleft = left.minutes
    sleft = left.seconds
    if yleft != 0:
            send += str(yleft) + " год "
    else:
        pass
    if Mleft != 0:
        if Mleft == 1:
            send += str(Mleft) + template["months"]%('')
        elif Mleft == 2 or Mleft == 3 or Mleft == 4:
            send += str(Mleft) + template["months"]%('а')
        elif Mleft >4 and Mleft <= 12:
            send += str(Mleft) + template["months"]%('ев')
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
            send += str(hleft) + template["hour"]%('')
        elif hleft == 2 or hleft == 3 or hleft == 4 or hleft == 22 or hleft == 23 or hleft == 24:
            send += str(hleft) + template["hour"]%('а')
        elif (hleft >4 and hleft <= 20):
            send += str(hleft) + template["hour"]%('ов')
        else:
            pass
    else:
        pass
    if mleft != 0:
        if mleft % 10 == 1 and mleft != 11:
            send += str(mleft) + template["min"]%('а')
        elif (mleft % 10 == 3 and mleft != 13) or (mleft % 10 == 4 and mleft != 14) or (mleft % 10 == 2 and mleft != 12) :
            send += str(mleft) + template["min"]%('ы')
        else:
            send += str(mleft) + template["min"]%('')
    else:
        pass
    if sleft != 0:
        if sleft % 10 == 1 and sleft != 11:
            send += str(sleft) + template["sec"]%('а')
        elif (sleft % 10 == 3 and sleft != 13) or (sleft % 10 == 4 and sleft != 14) or (sleft % 10 == 2 and sleft != 12) :
            send += str(sleft) + template["sec"]%('ы')
        else:
            send += str(sleft) + template["sec"]%('')
    else:
        pass
    return send
#Hi there!