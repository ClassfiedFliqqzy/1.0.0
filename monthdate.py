
def russiandate(r):
    import datetime
    mydate = datetime.now() ## Получение текущего месяца (через ПК)
    month = mydate.strftime("%B") ## Выдать название текущего месяца
    if month == "September": month = "Сентябрь" ## Сентябрь
    if month == "October": month = "Октябрь" ## Октябрь
    if month == "November": month = "Ноябрь" ## Ноябрь
    if month == "December": month = "Декабрь" ## Декабрь
    if month == "January": month = "Январь" ## Январь
    if month == "February": month = "Февраль" ## Февраль
    if month == "March": month = "Март" ## Март
    if month == "April": month = "Апрель" ## Апрель
    if month == "May": month = "Май" ## Май
    if month == "June": month = "Июнь" ## Июнь
    if month == "July": month = "Июль" ## Июль
    if month == "August": month = "Август" ## Август

