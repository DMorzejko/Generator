def genSQl(set, data):
    ins = 'INSERT INTO '
    val = 'VALUES '
    tables = ['Klient', 'Obiekt'] #kasować """, 'Brama', 'Centrala', 'Akumulator', 'Typ'"""
    table = tables[set]
    sqlSet = []

    #   Klient
    if set == 0:
        fields = '(Id_kli, Nazwa, Nip, Ulica, Nr_budynku, miasto, nr_telefonu, email) '
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + data[i][0] + "', '" + data[i][1] + "', '" + \
                         data[i][2] + "', '" + data[i][3] + "', '" + data[i][4] + "', '" + \
                         data[i][5] + "', '" + data[i][6] + "', '" + data[i][7] +"')"
            sqlSet.append(sqlCommand)
        return sqlSet

    #   Obiekt
    elif set == 1:
        fields = '(Id_obj, nazwa, ulica, numer_budynku, miasto, telefon, mail, os_odp, klient_id_kli) '
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + data[i][0] + "', '" + data[i][1] + "', '" + \
                         data[i][2] + "', '" + data[i][3] + "', '" + data[i][4] + "', '" + \
                         data[i][5] + "', '" + data[i][6] + "', '" + data[i][7] + "', '" + data[i][8] + "')"
            sqlSet.append(sqlCommand)
        return sqlSet
    """
    #   Brama
    elif set == 2:
        fields = '(miasto, kod_pocztowy) '
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + data[i][1] + "', '" + data[i][0] + "')"
            sqlSet.append(sqlCommand)
        return sqlSet

    #   Centrala
    elif set == 3:
        fields = '(adres, miasto_id) '
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + str(data[i][0]) + "', '" + str(data[i][1]) + "')"
            sqlSet.append(sqlCommand)
        return sqlSet

    #   Akumulator
    elif set == 4:
        fields = '(imie, nazwisko, oddzial_rckik_id) '
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + str(data[i][0]) + "', '" + \
                         str(data[i][1]) + "', '" + str(data[i][2]) + "')"
            sqlSet.append(sqlCommand)
        return sqlSet

    #   Typ
    elif set == 5:
        fields = '(oddzial_rckik_id) '
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + str(data[i]) + "')"
            sqlSet.append(sqlCommand)
        return sqlSet

"""