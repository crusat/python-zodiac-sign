import locale

ru_dict = {
    "Capricorn": "Козерог",
    "Aquarius": "Водолей",
    "Pisces": "Рыбы",
    "Aries": "Овен",
    "Taurus": "Телец",
    "Gemini": "Близнецы",
    "Cancer": "Рак",
    "Leo": "Лев",
    "Virgo": "Дева",
    "Libra": "Весы",
    "Scorpio": "Скорпион",
    "Sagittarius": "Стрелец",
}


# @todo use gettext and etc
def _(word):
    l = locale.getlocale()
    if l[0] == 'ru_RU':
        return ru_dict[word]
    else:
        return word


def get_zodiac_sign(d, month=None):
    # params
    if month is None:
        month = int(d.month)
        day = int(d.day)
    else:
        day = int(d)
        month = int(month)
    # calculate
    zodiac_sign = ''
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = _("Capricorn")
    elif (month == 1 and day >= 20) or (month == 2 and day <= 17):
        zodiac_sign = _("Aquarius")
    elif (month == 2 and day >= 18) or (month == 3 and day <= 19):
        zodiac_sign = _("Pisces")
    elif (month == 3 and day >= 20) or (month == 4 and day <= 19):
        zodiac_sign = _("Aries")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = _("Taurus")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = _("Gemini")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = _("Cancer")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = _("Leo")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = _("Virgo")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = _("Libra")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = _("Scorpio")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = _("Sagittarius")
    return zodiac_sign
