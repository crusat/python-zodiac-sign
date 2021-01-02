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

# English
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

# German
de_dict = (
    (0, "Widder"),
    (1, "Stier"),
    (2, "Zwillinge"),
    (3, "Krebs"),
    (4, "Löwe"),
    (5, "Jungfrau"),
    (6, "Waage"),
    (7, "Skorpion"),
    (8, "Schütze"),
    (9, "Steinbock"),
    (10, "Wassermann"),
    (11, "Fische"),
)

# Spanish
es_dict = (
    (0, "Aries"),
    (1, "Tauro"),
    (2, "Géminis"),
    (3, "Cáncer"),
    (4, "Leo"),
    (5, "Virgo"),
    (6, "Libra"),
    (7, "Escorpio"),
    (8, "Sagitario"),
    (9, "Capricornio"),
    (10, "Acuario"),
    (11, "Piscis"),
)

# Russian
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

# Portuguese
pt_dict = (
    (0, "Áries"),
    (1, "Touro"),
    (2, "Gêmeos"),
    (3, "Cancer"),
    (4, "Leão"),
    (5, "Virgem"),
    (6, "Libra"),
    (7, "Escorpião"),
    (8, "Sargitário"),
    (9, "Capricórnio"),
    (10, "Aquário"),
    (11, "Peixes"),
)

# Greek
el_dict = (
    (0, "Κριός"),
    (1, "Ταύρος"),
    (2, "Δίδυμοι"),
    (3, "Καρκίνος"),
    (4, "Λέων"),
    (5, "Παρθένος"),
    (6, "Ζυγός"),
    (7, "Σκορπιός"),
    (8, "Τοξότης"),
    (9, "Αιγόκερως"),
    (10, "Υδροχόος"),
    (11, "Ιχθείς"),
)

language_dict = {
    'en_US': en_dict,
    'de_DE': de_dict,
    'ru_RU': ru_dict,
    'pt_BR': pt_dict,
    'pt_PT': pt_dict,
    'el': el_dict,
    'el_CY': el_dict,
    'el_GR': el_dict,
    'es_ES': es_dict,
    None: en_dict
}


# @todo use gettext and etc
def _(word_index, language=None):
    if language is not None:
        return language_dict.get(language)[word_index][1]
    language = locale.getlocale()
    return language_dict.get(language[0], language_dict.get('en_US'))[word_index][1]


def get_zodiac_sign(d, month=None, language=None):
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
            return _(index, language)
    return ''
