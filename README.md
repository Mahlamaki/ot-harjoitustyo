# Ohjelmistotekniikka, harjoitustyö

## Kirjakerholog

Sovellus tulee toimimaan kirjakerhomme kirjarekisterinä. Lisäämme sinne aina luetun kirjan. Kirjasta tallennetaan ainakin seuraavat tiedot: Kirjoittaja, Kirjan nimi, Kirjakerhon antama Arvostelu. Kirjakerhon rekisteristä voi sitten katsoa, mitä kaikkia kirjoja on luettu ja mitä arvosanoja niille on annettu. Lisäksi kirjoja voidaan etsiä eri hakutoiminnoin, esimerkiksi kirjailijan tai arvioinnin mukaan.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changeloog](./dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
  
## Projektin asennusohjeet

Kloonaa projekti koneellesi ja siirry projektin kansioon:
```
git clone git@github.com:Mahlamaki/ot-harjoitustyo.git
```
```
cd ot-harjoitustyo
```

Asenna riippuvuudet:
```
poetry install
```

Alusta tietokanta:
```
poetry run invoke build
```

Käynnistä
```
poetry run invoke start
```

## Komentorivitoimitoja

### ohjelman käynnistys
```
poetry run invoke start
```

### testaus
```
poetry run invoke test
```

### testikattavuus
```
poetry run invoke coverage-report
```
raportti löytyy htmlcov-hakemistosta

### pylint
```
poetry run invoke lint
```
tämä suorittaa .pylitrc tiedostosta löytyvät tarkistukset
