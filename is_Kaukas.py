def is_Kaukas(bank):
    true_region = ['Абсолют', "ВФБ", "ПСБ", "Металлинвестбанк"]
    if bank == '':
        return ''

    if bank in true_region:
        return 'Да, все верно'

