```mermaid
classDiagram
Pelilauta -- Ruudut
Pelilauta -- Pelaajat
Pelinappulat -- Ruudut
Pelaajat --  Pelinappulat
Ruudut -- Kortit
class Ruudut {
-Aloitusruutu
-Vankila
-Sattuma
-Yhteismaa
-Asemat_ja_laitokset
-Kaikki_kadut
}
class Kortit {
-Sattumakortit
-Yhteismaakortit
}

```
