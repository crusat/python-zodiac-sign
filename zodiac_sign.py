import locale

# (start(day, month), end(day, month))
sign_dates = (
    ((20, 3), (19, 4)),  # Aries
    ((20, 4), (20, 5)),
    ((21, 5), (20, 6)),
    ((21, 6), (22, 7)),
    ((23, 7), (22, 8)),
    ((23, 8), (22, 9)),
    ((23, 9), (22, 10)),
    ((23, 10), (21, 11)),
    ((22, 11), (21, 12)),
    ((22, 12), (19, 1)),
    ((20, 1), (17, 2)),
    ((18, 2), (19, 3)),  # Pisces
)

en_dict = (
    (0, "Aries"),
    (1, "Taurus"),
    (2, "Gemini"),
    (3, "Cancer"),
    (4, "Leo"),
    (5, "Virgo"),
    (6, "Libra"),
    (7, "Scorpio"),
    (8, "Sagittarius"),
    (9, "Capricorn"),
    (10, "Aquarius"),
    (11, "Pisces"),
)

ru_dict = (
    (0, "Овен"),
    (1, "Телец"),
    (2, "Близнецы"),
    (3, "Рак"),
    (4, "Лев"),
    (5, "Дева"),
    (6, "Весы"),
    (7, "Скорпион"),
    (8, "Стрелец"),
    (9, "Козерог"),
    (10, "Водолей"),
    (11, "Рыбы"),
)



# @todo use gettext and etc
def _(word_index):
    l = locale.getlocale()
    if l[0] == 'ru_RU':
        return ru_dict[word_index][1]
    else:
        return en_dict[word_index][1]


def get_zodiac_sign(d, month=None):
    # params
    if month is None:
        month = int(d.month)
        day = int(d.day)
    else:
        day = int(d)
        month = int(month)
    # calculate
    for index, sign in enumerate(sign_dates):
        if (month == sign[0][1] and day >= sign[0][0]) or (month == sign[1][1] and day <= sign[1][0]):
            return _(index)
    return ''
