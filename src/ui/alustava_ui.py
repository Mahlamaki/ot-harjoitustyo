""" Projekti vielä todella pahasti kesken, aika ei riittänyt ennen viikon palautusta.En ole saanut vielä 
kursittua mitään kunnolla yhtenäiseksi tai toimivaksi"

class AlustavaUI:

    def __init__(self):
        self._io =KonsoliIO()
    
    def _action(self):
        
        while True: 
            toiminto = self._io.tulosta("Luo uusi käyttäjä painamalla x-näppäintä")
            if toiminto != "x":
                self._io.tulosta("Luo uusi käyttäjä painamalla x-näppäintä")
                continue
            if toiminto == "x":
                break
        username = self._io.lue("Käyttjätunnus: ")
        name = self._io.lue("Nimi: ")

        user_respositories.create(username,name)
