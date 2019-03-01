# Käyttöohje


### ADMIN käyttäjän lisääminen
Sovellukseen voi lisätä ADMIN-käyttäjiä vain suoraan tietokannan kautta.
Jos sovellus on paikkallinen:
+ Avaa sovelluksen kansiosta sen tietokanta komennolla: ```sqlite3 application/books.db ```
+ Lisää käyttäjä komennolla: ``` INSERT INTO account (name, username, password, role) VALUES ('<Nimimerkki>', '<Käyttäjätunnus>', '<Salasana>','ADMIN'); ```
Jos sovellus on Herokussa:
+ avaa tietokanta komenolla ``` heroku pg:psql ```
+ Ja lisää AMIN-käyttäjä: ``` INSERT INTO account (name, username, password, role) VALUES ('<Nimimerkki>', '<Käyttäjätunnus>', '<Salasana>','ADMIN'); ```
 