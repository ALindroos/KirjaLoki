# Asennusohjeet

## Vaatimukset:
+ python 3.5 & pip
+ venv-kirjasto virtaaliympäristöä varten

Jos halutaan siirtää ohjelma vielä Heroku-palveluun, tarvitaan vielä:
+ git
+ heroku-cli

## Käyttöönotto lokaalisti:
+ Lataa projektin Github repositorio (clone tai zip) ja pura haluamaasi kansioon
+ Luo kansioon venv-virtaaliympäristö terminaalista komennolla:
``` python -m venv venv ```
+ Käynnistä virtaaliympäristö komenolla:
``` source venv/bin/activate ```
+ Lataa ja asenna tarvittavat riippuvuudut komennolla: ``` pip install -r requirements.txt ```
+ Käynnistä sovellus kommennolla: ``` python3 run.py ``` ja sovellukseen päsee selaimella osoitteessa http://127.0.0.1:5000/

## Heroku:
+ Tässä vaiheessa käyttäjällä pitäisi olla GitHub- ja Heroku-tunnukset käytössä ja sovellukselle oma repositorio

+ Luodaan heroku-sovellus: ``` heroku create <nimi sovellukselle> ```
+ Lisätään linkitys repoon: ``` git remote add heroku https://git.heroku.com/<sovelluksen nimi>.git ```
+ Asetaan sovellukseen Heroku-ympäristömuuttuja: ```heroku config:set HEROKU=1 ```
+ Luodaan sovelluksen tarvitsema PostgreSQL tietokanta: ``` heroku addons: add heroku-postgresql:hobby-dev ```
+ Ja siirretään sovellus Herokuun: ``` push heroku master ```


