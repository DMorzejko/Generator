def genSQl(set, data):
    ins = 'INSERT INTO '
    val = 'VALUES '
    tables = ['Klient', 'Obiekt', 'Akumulator']
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
            #print(sqlCommand)
        return sqlSet

    #   Obiekt
    elif set == 1:
        fields1 = '(Id_obj, nazwa, ulica, numer_budynku, miasto, telefon, mail, os_odp, klient_id_kli) '
        fields2 = '(ID_PRZ)'
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields1 + val + "('" + data[i][0] + "', '" + data[i][1] + "', '" + \
                         data[i][2] + "', '" + data[i][3] + "', '" + data[i][4] + "', '" + \
                         data[i][5] + "', '" + data[i][6] + "', '" + data[i][7] + "', '" + data[i][8] + "') "
            sqlSet.append(sqlCommand)
            sqlCommand = ins + "Przedmioty_Przegladu"+ fields2 + val + " ( " + data[i][9] + " )"
            sqlSet.append(sqlCommand)
        return sqlSet

    # Akumulator, Centrala, Typ, Brama
    elif set == 2:
        fields1 = '(typ_id, typ)'
        fields2 = '(id_centrala,typ,akumulator_typ_id)'
        fields3 = '(id_typ, typ, podtyp)'
        fields4 = '(numer, rysunek, czasookres, obiekt_id_obj, przedmioty_przegladu_id_prz, typ_id_typ, centrala_id_centrala)'
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields1 + val + " ('" + data[i][0] + "', '" + data[i][1] + "') "
            sqlSet.append(sqlCommand)
            sqlCommand = ins + "centrala" + " " + fields2 + val + " ('" + data[i][2] + "', '" + data[i][3] + "', '" \
                         + data[i][4] +  "') "
            sqlSet.append(sqlCommand)
            sqlCommand = ins + "typ" + " " + fields3 + val + " ('" + data[i][5] + "', '" + data[i][6] + "', '" \
                         + data[i][7] + "') "
            sqlSet.append(sqlCommand)
            sqlCommand = ins + "brama" + " " + fields4 + val + " ('" + data[i][8] + "', '" + data[i][9] + "', '" \
                         + data[i][10] + "', '" + data[i][11] + "', '" + data[i][12] + "', '" + data[i][13] + "', '" \
                         + data[i][14] + "') "
            sqlSet.append(sqlCommand)
        return sqlSet

