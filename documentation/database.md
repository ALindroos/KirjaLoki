### Tietokanna luonti
```
CREATE TABLE account (
	id INTEGER NOT NULL,    
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE book (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	title VARCHAR(144) NOT NULL, 
	author VARCHAR(144) NOT NULL, 
	description VARCHAR(526), 
	isbn VARCHAR(13) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE note (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	note VARCHAR(512) NOT NULL, 
	account_id INTEGER NOT NULL, 
	book_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(book_id) REFERENCES book (id)
)

CREATE TABLE read_books (
	book_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (book_id, account_id), 
	FOREIGN KEY(book_id) REFERENCES book (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
```

### Kuvaus

#### Account/User 
on käyttäjään liittyvät tiedot. Kirjautumistietojen lisäksi tätä käytetään oman kirjalista haltijana ja käyttäjä profiilina. Name viittaa käyttäjän nimimerkkiin joka näkyy myös muille käyttäjille, ja username yksilölliseen kirjautumistunnukseen. Role on joka ["USER"] tai ["USER", "ADMIN"] jotka määrittävät sallitut toiminnot

### Book
Kuvaa kirjan tietoja. Kirjan nimi, kirjailija, kuvaus (eli juonitiivistelmä, takakansiteksti yms.), ISBN.


### Note
eli käyttäjien kommentit.
Yhdestä moneen riippuvuus niin käyttäjään kuin kirjaan, näiden id:n perusteella. Sisältää käyttäjän antaman kommentin jostain kirjasta.

### read_books
on monesta-moneen yhdystaulu kirjojen ja käyttäjän välillä jonka avulla pidetään yllä käyttäjän lukemia kirjoja.
 