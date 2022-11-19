```mermaid
classDiagram
	Pelilauta --|> Ruudut
	Ruudut "1" --> "*" Pelaajat
	Pelaajat "1" --> "1" Pelinappulat
	Pelilauta : +pelivuoro
	Pelilauta : +nopanheitto()
	class Ruudut {
	}
	class Pelaajat {
		+pelaaja_id
		+nappula_id
		+ruutu_id
	}
	class Pelinappulat {
		+pelaaja_id
	}
``
