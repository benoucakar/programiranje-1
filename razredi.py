class Pes():
    # Argumenti

    def __init__ (self, ime, starost):
        self.ime = ime
        self.starost = starost
        self.sreca = 5
        self.lakota = 5

    # Metode

    def podatki(self):
        print("Ime: " + self.ime)
        print("Starost: " + str(self.starost) + " let")
        print("Sreča: " + str(self.sreca))
        print("Lakota: " + str(self.lakota))

    def igra(self):
        self.lakota += 1
        self.sreca += 1
        self.podatki()

    def nahrani(self):
        self.lakota -= 2
        self.podatki()
    
    def kreganje(self):
        self.sreca -= 2
        self.podatki()
    
    def __add__(self, kuza):
        self.sreca += 2
        kuza.sreca += 2

kuza1 = Pes("Piko", 3)
kuza2 = Pes("Erik", 100)
kuza3 = Pes("Rex", 5)


def tekstura():
    print("                     &&&")
    print("               &&&&&&&&&                          &&")
    print("               &&     &&                      &&&")
    print("                       &&&&&&&&&&&&&&&&&&&&&&")
    print("                       & &&      &&&&&&& &&&")
    print("                      &&  &             &&  &")
    print("                      &   &            &&    &&")
