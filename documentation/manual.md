# Käyttöohje

## Käyttäjistä:
Suurin osa toiminnoista on käytettävissä ainoastaan kirjautuneillä käyttäjillä. Kirjautumaton käyttäjä voi ainostaan hakea ja listata kirjoja, katsoa kirjojen tietoja tai käyttäjien sivuja, sekä kirjautua sisään tai luoda käyttäjän sovellukseen.

Loput ohjeen toiminnoista on kuvattu kirjautuneen käyttäjän kannalta. Poikkeuksena se, että vain ADMIN-tason käyttäjä voi poistaa kirjoja sovelluksesta.

# Keskeiset toiminnot:

## Yläpalkki:

#### Listaa Kirjoja:
Palauttaa kolme listaa sovelluksen kirjoista:
+ "Uusimmat kirjat", jossa 5 uusinta lisättyä kirjaa
+ "Luetuimmat kirjat", eli 10 käyttäjien kesken luetuinta kirjaa
+ Sekä "Puhutuimmat kirjat", eli 10 kirjaa joilla eniten kommentteja

#### Hae Kirjoja:
Yksinkertainen hakutoiminto. Hakee niin kirjan nimen kuin kirjalijan mukaan.

#### Lisää Kirja:
Avaa lomakkeen jonka avulla voi lisätä uuden kirjan sovellukseen. Vaadittavia tietoja on kirjan nimi, kirjailijan nimi ja ISBN. Kuvaus, joka voi olla tiivistelmä, juonikuvaus tai takakansi teksti ei ole pakollinen.

#### Oma KirjaLoki:
Näyttää käyttäjän oman sivun josta näkee kaikki käyttäjän luetuksi merkityt kirjat, niihin liittyvät mahdolliset käyttäjän kirjoittamat kommentit, sekä luettujen kirjojen määrä.

#### Lukijoiden merkintöjä:
Näyttää uusimpia kommenttejä mitä muut käyttäjät ovat jättäneet kaikille sellaisille kirjoille jotka itse on lukenut. 

#### Kirjaudu/Kirjaudu ulos
Jos käyttäjä on kirjautunut kirjaa käyttäjän ulos. Muussa tapauksessa avaa kirjautumis-sivun, josta myös linkki uuden käyttäjän luomista varten

## Kirjoihin liittyviä toimintoja:
Kirjan perustietoihin pääsee aina painamalla kirjan nimen kohdalla olevaa linkkiä.
Kirjan sivulta löytyy seuraavanlaisia komentoja:

#### Merkitse luotuksi/Poista luotuista kirjoista:
Merkitsee kirjan luotuksi jolloin se näkyy käyttäjän omalla sivulla luotuissa kirjoissa, tai poistaa sen listalta. Kirjan merkityksi lukeminen on myös vaatimus toisille toiminnoille.

#### Kirjoita kommentti/Muokka kommenttia:
Kommentin kirjoittaminen vaati että kirja on merkitty luetuksi. Avaa lomakkeen jonka avulla kirjalle voi lisätä lyhyen kirjaan liittyvän kommentin, mielipiteen, tai mietylauseen.
Kun kirjalle on lisätty kommentti, vaihtuu nappi niin että nyt kommenttia voi muokata tai halutessaan poistaa.
Yhteen kirjaan voi lisätä vain yhden kommentin per käyttäjä.

#### Muokkaa kirjan tietoja:
Avaa lomakkeen jonka avulla voi muokata kirjan tietoja. Sisältää myös mahdollisuuden poistaa kirja sovelluksesta, mutta vain ADMIN-käyttäjille.

#### Hae Helmetistä:
Etsii Helmetistä (Pääkaupunkisueden yleisten kirjastojen kirjastoverkko) ISBN perusteella kyseistä kirjaa. Jos vaikka heti haluaa varata kiinnostava näköisen kirjan.

## Käyttäjiin liittyviä toimintoja:

#### Rekisteröityminen:
Löytyy kirjaudu lomakkeella olevan "Luo uusi käyttäjätunnus?" linkin takaa.
Lomakkeella nimimerrkki viittaa nimeen joka näkyy myös muille käyttäjille ja käyttäjätunnus on kirjautumista varten.

#### ADMIN käyttäjän lisääminen
Sovellukseen voi lisätä ADMIN-käyttäjiä vain suoraan tietokannan kautta.
#### Jos sovellus on paikkallinen:
+ Avaa sovelluksen kansiosta sen tietokanta komennolla: ```sqlite3 application/books.db ```
+ Lisää käyttäjä komennolla: ``` INSERT INTO account (name, username, password, role) VALUES ('<Nimimerkki>', '<Käyttäjätunnus>', '<Salasana>','ADMIN'); ```
#### Jos sovellus on Herokussa:
+ avaa tietokanta komenolla ``` heroku pg:psql ```
+ Ja lisää AMIN-käyttäjä: ``` INSERT INTO account (name, username, password, role) VALUES ('<Nimimerkki>', '<Käyttäjätunnus>', '<Salasana>','ADMIN'); ```
 