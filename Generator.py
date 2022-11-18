
import dbConnection
import string
import random
from faker import Faker


def randomize(l):
    pnone = 0.8
    if random.random() < pnone:
        selection = ''
    else:
        selection = random.choice(l)
    return selection
class generator:

    def __init__(self):
        print('Generator')

    def get(self, set, num):
        if set == 0:
            return self.gen0(num)
        elif set == 1:
            return self.gen1(num)
        elif set == 2:
            return self.gen2(num)




    # Klient
    def gen0(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT MAX(id_kli) FROM Klient')
        maxId = conn.getData()[0]
        conn.execute('SELECT Nazwa FROM Klient')
        KlNazwa = conn.getData()
        conn.execute('SELECT Nip FROM Klient')
        KlNip = conn.getData()

        del conn

        result = []
        nipy = []
        nazwy = []
        for i in range(num):
            while True:
                kNip = random.randint(1000000000,9999999999)
                if kNip not in KlNip or nipy:
                    nipy.append(kNip)
                    break
            while True:
                with open(r'data/K_nazwa.txt', 'r', encoding='utf-8') as fp:
                    kNaz = random.choice(fp.readlines())
                    if kNaz not in KlNazwa or nazwy:
                        nazwy.append(kNaz)
                        break
            with open(r'data/ulica.txt', 'r', encoding='utf-8') as fp:
               kUlica = random.choice(fp.readlines())
            kNr = str(random.randrange(100))
            with open(r'data/miasto.txt', 'r', encoding='utf-8') as fp:
                kMia = random.choice(fp.readlines())
            kTel = random.randint(500000000, 999999999)
            kMail = 'biuro@'+ str((kNaz)) + '.com.pl'

            maxId += 1
            result.append([str(maxId),str((kNaz)), str(kNip),
                           str((kUlica)), str(kNr),
                           str((kMia)), str(kTel), str(kMail)])
        return result

    def toList(self, data):
        result = []
        for i in range(len(data)):
            result.append(str(data[i]).split())

        return result


    # Obiekt
    def gen1(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT MAX(id_obj) FROM Obiekt')
        maxOId = conn.getData()[0]
        conn.execute('SELECT Id_kli FROM Klient')
        KlId = conn.getData()
        conn.execute('SELECT Nazwa FROM Obiekt')
        ObNazwa = conn.getData()
        del conn

        result = []
        ObNazwy = []
        for i in range(num):
            maxOId += 1
            while True:
                with open(r'data/O_nazwa.txt', 'r', encoding='utf-8') as fp:
                    ONaz = random.choice(fp.readlines())
                    if ONaz not in ObNazwy or ObNazwa:
                        ObNazwy.append(ONaz)
                        break
            with open(r'data/ulica.txt', 'r', encoding='utf-8') as fp:
               oUlica = random.choice(fp.readlines())
            oNr = str(random.randrange(100))
            with open(r'data/miasto.txt', 'r', encoding='utf-8') as fp:
                oMia = random.choice(fp.readlines())
            oTel = random.randint(500000000, 999999999)
            oMail = 'biuro@'+ str((ONaz)) + '.com.pl'
            with open(r'data/osodp.txt', 'r', encoding='utf-8') as fp:
               oOsOd = random.choice(fp.readlines())
            klId = random.choice(KlId)


            result.append([str(maxOId),str((ONaz)), str(oUlica),
                           str((oNr)), str(oMia),
                           str((oTel)), str(oMail), str(oOsOd), str(klId), str(maxOId)])
        return result

    # Akumulator, Centrala, Typ, Brama
    def gen2(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT numer FROM Brama')
        BCheck = conn.getData()
        conn.execute('SELECT id_obj FROM Obiekt')
        BObId = conn.getData()
        conn.execute('SELECT MAX(id_typ) FROM typ')
        maxTypId = conn.getData()[0]
        del conn

        bramy = []
        result = []
        for i in range(num):

            #akumulator
            maxTypId += 1
            Akumulator = ['MAŁY', 'DUŻY']
            Aku = random.choice(Akumulator)
            #centrala
            if Aku == 'DUŻY':
                Centrala = 'FS'
            else:
                Centrala = 'SL'

            # typ
            typy = ['S', 'G', 'R', 'O']
            podtypyS = ['2T', '3T']
            podtypyOR = ['H']
            BTyp = random.choice(typy)
            if BTyp == 'S':
                BPodTyp = randomize(podtypyS)
            elif BTyp == 'R' or 'O':
                BPodTyp = randomize(podtypyOR)
            else:
                BPodTyp = None

            #brama
            while True:
                numer = random.randint(130000,229999)
                if numer not in BCheck or bramy:
                    bramy.append(numer)
                    break
            RysChoice = ['TAK','NIE']
            rysunek = random.choice(RysChoice)
            if numer > 199999:
                czasookres = '6M'
            else:
                czasookres = '12M'
            obj_id = random.choice(BObId)




            result.append([str(maxTypId), str(Aku), str(maxTypId),
                           str(Centrala), str(maxTypId), str(maxTypId), str(BTyp),
                           str(BPodTyp), str(numer), str(rysunek), str(czasookres),
                           str(obj_id), str(obj_id), str(maxTypId), str(maxTypId)])
        return result



    """
    # Oddzial_RCKiK
    def gen3(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT id FROM miasta')
        idCities = conn.getData()
        del conn

        result = []
        fake = Faker('pl_PL')

        for i in range(num):
            adress = fake.street_address()
            result.append([adress, str(random.choice(idCities))])

        return result


    # Pracownicy
    def gen4(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT id FROM oddzial_rckik')
        idOddzial = conn.getData()
        del conn

        result = []

        for i in range(num):
            plec = random.choice([0, 1])
            if plec == 0:
                with open(r'data/imionaM.txt', 'r', encoding='utf-8') as fp:
                    fName = random.choice(fp.readlines())
                with open(r'data/nazwiskaM.txt', 'r', encoding='utf-8') as fp:
                    lName = random.choice(fp.readlines())
            else:
                with open(r'data/imionaK.txt', 'r', encoding='utf-8') as fp:
                    fName = random.choice(fp.readlines())
                with open(r'data/nazwiskaK.txt', 'r', encoding='utf-8') as fp:
                    lName = random.choice(fp.readlines())
            result.append([str(fName).strip(), str(lName).strip(), str(random.choice(idOddzial))])

        return result


    # Oddzial_terenowy
    def gen5(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT id FROM oddzial_rckik')
        idOddzial = conn.getData()
        del conn

        result = []

        for i in range(num):
            result.append(str(random.choice(idOddzial)))
        return result


    # Pobrania + Krew
    def gen6(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT id FROM oddzial_rckik')
        idOddzial = conn.getData()
        conn.execute('SELECT id FROM krwiodawcy')
        idKrwiodacy = conn.getData()
        conn.execute('SELECT id FROM pracownicy')
        idPracownicy = conn.getData()
        conn.execute('SELECT MAX(id) FROM pobrania')
        lastID = conn.getData()[0]
        del conn

        result = []

        for i in range(num):
            date = self.genDate('-20y', 'today')
            result.append([str(random.choice(idOddzial)), str(random.choice(idKrwiodacy)),
                           str(random.choice(idPracownicy)), (str(date[2]) + '/' + str(date[1]) + '/' + str(date[0]))])

            lastID += 1
            ml = random.randrange(150, 1000)
            if ml > 450:
                ml = 450
            status = random.choice(['D', 'U', 'B'])
            expYear = str(int(date[0]) + 1)
            result.append([str(lastID), str(ml), status, (str(date[2]) + '/' + str(date[1]) + '/' + expYear)])

        return result


    # Wyniki_badan
    def gen7(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT id FROM krew')
        idKrew = conn.getData()
        del conn

        result = []

        for i in range(num):
            desc = 'Opis badania w kartotece nr. ' + str(random.randrange(1000000))
            result.append([str(random.choice(idKrew)), str(random.choice(['0', '1'])), desc])

        return result


    # Wydania_krwi
    def gen8(self, num):
        conn = dbConnection.DbConnection()
        conn.execute('SELECT id FROM krew WHERE wydania_krwi_id IS NULL')
        idKrew = conn.getData()
        conn.execute('SELECT id FROM jednostki_docelowe')
        idJednostki = conn.getData()
        conn.execute('SELECT MAX(id) FROM wydania_krwi')
        lastID = conn.getData()[0]
        del conn

        result = []

        for i in range(num):
            lastID += 1
            date = self.genDate('-10y', 'today')
            result.append([str(random.randrange(999999)), (str(date[2]) + '/' + str(date[1]) + '/' + str(date[0])),
                           str(random.choice(idJednostki)).strip(), str(random.choice(idKrew)).strip(),
                           str(lastID)])

        return result


    # Jednostki_docelowe
    def gen9(self, num):
        result = []
        fake = Faker('pl_PL')
        for i in range(num):
            name = 'Szpital ' + fake.city()
            result.append([name])

        return result"""


"""   def genDate(self, start, end):
        fake = Faker()
        result = str(fake.date_between(start_date=start, end_date=end))
        return result.split('-')    #['YYYY', 'MM', 'DD']"""

