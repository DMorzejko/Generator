import dbConnection
import random
import string

def randomize(l):
    pnone = 0.8
    if random.random() < pnone:
        selection = ''
    else:
        selection = random.choice(l)
    return selection
class generator:
    def __init__(self):
        print('Uruchomiono generator: ')
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
                    kNaz = kNaz.strip()
                    kNaz += ''.join(random.choices(string.ascii_letters,k=10))
                    if kNaz not in KlNazwa or nazwy:
                        nazwy.append(kNaz)
                        break
            with open(r'data/ulica.txt', 'r', encoding='utf-8') as fp:
                kUlica = random.choice(fp.readlines())
                kUlica = kUlica.strip()
            kNr = str(random.randrange(100))
            with open(r'data/miasto.txt', 'r', encoding='utf-8') as fp:
                kMia = random.choice(fp.readlines())
                kMia = kMia.strip()
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
                    ONaz = ONaz.strip()
                    ONaz += ''.join(random.choices(string.ascii_letters,k=10))
                    if ONaz not in ObNazwy or ObNazwa:
                        ObNazwy.append(ONaz)
                        break
            with open(r'data/ulica.txt', 'r', encoding='utf-8') as fp:
                oUlica = random.choice(fp.readlines())
                oUlica = oUlica.strip()
            oNr = str(random.randrange(100))
            with open(r'data/miasto.txt', 'r', encoding='utf-8') as fp:
                oMia = random.choice(fp.readlines())
                oMia = oMia.strip()
            oTel = random.randint(500000000, 999999999)
            oMail = 'biuro@'+ str((ONaz)) + '.com.pl'
            with open(r'data/osodp.txt', 'r', encoding='utf-8') as fp:
                oOsOd = random.choice(fp.readlines())
                oOsOd = oOsOd.strip()
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

        #res = [eval(i) for i in BCheck]
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
                numer = random.randint(1,1300000)
                if numer not in BCheck and numer not in bramy:
                    bramy.append(numer)
                    print(BCheck)
                    print(bramy)
                    break

            RysChoice = ['TAK','NIE']
            rysunek = random.choice(RysChoice)
            if numer > 599999:
                czasookres = '6M'
            else:
                czasookres = '12M'
            obj_id = random.choice(BObId)




            result.append([str(maxTypId), str(Aku), str(maxTypId),
                           str(Centrala), str(maxTypId), str(maxTypId), str(BTyp),
                           str(BPodTyp), str(numer), str(rysunek), str(czasookres),
                           str(obj_id), str(obj_id), str(maxTypId), str(maxTypId)])
        return result