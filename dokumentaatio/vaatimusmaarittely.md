# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen on tarkoitus mahdollistaa käyttäjälle paperiton tapa luoda oppimateriaalia kertaavia muistipeli"lappuja". 
Kysymyksien keksiminen, ja niihin vastaaminen edistäävät oppimista, ja näitä lappuja on sitten kätevää ja hyödyllistä käyttää materiaalin aktiivisessa mieleen palauttamisessa.

## Käyttäjät
Ainakin aluksi sovelluksessa on vain normaali käyttäjiä. Riippuen siitä, miten sovellusta lähtisi laajentamaan,
Voisi käyttäjätyyppejä olla enemmänkin.
## Käyttöliittymäluonnos
Ainakin näin varhaisessa muodossa, sovelluksessa olisi 8 näkymää.

__tähän tulee myöhemmin kuva__


## Perusversion tarjoama toiminnallisuus
### Käyttäjätunnuksen luominen ja kirjautuminen
- Tunnuksen tulee olla uniikki ja vähintään 4 merkkiä
- Sovellus aukeaa suoraan näkymään, jossa voi kirjautua sisään omalla käyttäjätunnuksella, tai luoda käyttäjätunnuksen

### Kirjautumisen jälkeen
-Avautuu etusivu, jossa on mahdollista valita **"Luo lappu"**, **"muokkaa lappuja"**, **"Harjoittele"**
- Luo lappu- kohdassa avautuu näkymä, jossa on kaksi tekstikenttää, toiseen käyttäjä kirjoittaa kysymyksen/käsitteen ja toiseen vastauksen. Lisäksi on napit poista (josta palataan takaisin edelliseen näkymään) ja tallenna (joka tallentaa lapun ja palaa sitten edelliseen näkymään)
- Muokkaa lappuja- napilla pääsee katselemaan lappulistausta-> tiettyä lappua painamalla pääsee samaan näkymään kuin lapun luonnissa, jossa lappua pääsee siis muokkaamaan tai poistamaan. Lopuksi palataan takaisin lappulistaukseen.
- Harjoittele- napilla päästään harjoittelemaan lappujen sisältöä. Sovellus generoi ainakin alustavassa versiossa vielä kysymyksiä täysin sattumanvaraisesti. Kuitenkin niin, että jokainen kysymys, ainakin tässä alustavassa versiossa, esitetään vain kerran. 
- Käyttäjälle siis näytetään ensin lapun kysymys osa, käyttäjä saa pohtia oman vastauksensa ja painaa "katso vastaus", ja vastauksen lukemisen jälkeen painaa jatka, jolloin tulee seuraava kysymys. Kun kysymykset loppuvat, tulee tästä ilmoitus ja palataan etusivulle.
## Jatkokehitysideoita
- Kirjautumiseen voi lisätä salasanan
- Sovellukseen voisi lisätä mahdollisuuden lisätä useita kursseja. Kirjautumisen jälkeen avautuisi listaus, josta voi joko valita uuden lappukokoelman luomisen, tai siirtyä jonkin jo luodun lappukokonaisuuden käsittelyyn.
- Usean käyttäjän yhteiset laput, johon kaikki voisivat lisätä omia kysymyksiä ja vastauksia.
- usean käyttäjän toteutuksessa sovelluksen toiminnan voisi pelillistää
- Oikeiden vastauksien prosenttiosuudet ja muut tilastot
- Sovellus voisi generoida kysymyksiä sitä mukaan, kuinka hyvin opiskelija on niihin vastannut (vaikeita enemmän ja heti ekalla oikein vastaamia vähemmän) 

