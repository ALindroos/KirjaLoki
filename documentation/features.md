
# User Stories

## Backlog




## Done

### Kommenteissa näkyy käyttäjän nimi ja on linkki käyttäjän sivulle
Kirjoihin jätetyissä kommenteissa näkyy sen kirjoittaneen käyttäjän nimi, ja nimestä linkki käyttäjän sivulle. Näin voi katselle mitä kirjoja kiinnostavan kommentin jättänyt käyttäjä on lukenut ja mitä niistä ajatellut.

### Käyttäjä voi katsoa mitä muut käyttäjä ovat kommentoineet hänen lukemiinsa kirjoihin
Ylävalikon linkista "Lukijoiden merkintöjä" näkyy mitä kommentteja muut käyttäjät ovat jättäneet luetuille kirjoille. Näkymästä näkee kommentteja vain sellaisille kirjoille mitä on itse lukenut ja tietenkään omia kommentteja ei näy.
```
SELECT book.id AS book_id, book.date_created AS book_date_created, book.date_modified AS book_date_modified, book.title AS book_title, book.author AS book_author, book.description AS book_description, book.isbn AS book_isbn, anon_1.account_id AS anon_1_account_id 
FROM (SELECT account.id AS account_id 
FROM account 
WHERE account.id = ?) AS anon_1 JOIN read_books AS read_books_1 ON anon_1.account_id = read_books_1.account_id JOIN book ON book.id = read_books_1.book_id ORDER BY anon_1.account_id

SELECT Book.id, Book.title, Book.author, Account.id, Account.name, Note.note, Note.date_created FROM Book, Account, Note LEFT JOIN read_books ON read_books.account_id = ? WHERE Note.book_id = Book.id AND Book.id = read_books.book_id AND Account.id != ? AND Note.account_id = Account.id ORDER BY 7 DESC
```

### Käyttäjä voi poistaa/muokata kommentteja
käyttäjä voi nyt muokata kirjoittamaansa kommenttia. Muokkaus-näkymästä löytyy myös nappi jolla voi käyttäjä voi poistaa kommentinsa.

### Käyttäjä voi kirjoittaa komentteja kirjoille
Käyttäjä voi lisätä kirjalla kommentin joka näkyy kirjan perustiedoissa kaikille käyttäjille. Kommentin voi lisätä vain luetulle kirjalle ja vain yhden per kirja.
```
INSERT INTO note (date_created, date_modified, note, account_id, book_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

### Siirtyminen pilvessä olevaan tietokantaan
Sovellus käyttää nyt Herokun Postgresql-tietokantaa, tarkoittaen että käyttäjä voi käyttää sovellusta miltä tahansan koneelta netin välityksellä

### Käyttäjä voi luoda käyttäjätunnuksen sovellukseen
Käyttäjä voi luoda sovelluksen kautta uuden käyttäjätunnuksen, olettaen että saman nimistä tunnusta ei ole jo luotu

### Käyttäjä voi poistaa kirjoja luettujen kirjojen listalta
Kirjan sivuilla on nyt nappi jonka avulla lisätyn kirjan voi poistaa omalta listaltaan

### Käyttöliittymä
Sovelluksella on nyt pohja mielyttävämmälle käyttöliittymälle

### Admin-käyttäjä voi poistaa kirjoja
Kirjoja on mahdollista poistaa sovelluksesta, mutta oikeus on tähän vain pääkäyttäjällä

### Käyttäjä voi katsella omia lisättyjä kirjojaan
Käyttäjä näkee omalta sivultaan luetuiksi lisäämänsä kirjat ja mahdollisesti näihin lisättyjä kommentteja. Omaan sivuun löytyy linkki ylävalikosta nimelle "Oma KirjaLoki".
```
SELECT book.id AS book_id, book.date_created AS book_date_created, book.date_modified AS book_date_modified, book.title AS book_title, book.author AS book_author, book.description AS book_description, book.isbn AS book_isbn, anon_1.account_id AS anon_1_account_id 
FROM (SELECT account.id AS account_id 
FROM account 
WHERE account.id = ?) AS anon_1 JOIN read_books AS read_books_1 ON anon_1.account_id = read_books_1.account_id JOIN book ON book.id = read_books_1.book_id ORDER BY anon_1.account_id

SELECT note.id AS note_id, note.date_created AS note_date_created, note.date_modified AS note_date_modified, note.note AS note_note, note.account_id AS note_account_id, note.book_id AS note_book_id 
FROM note 
WHERE ? = note.account_id
```

### Käyttäjä voi lisätä kirjoja omalle luettujen kirjojen listalle
Käyttäjä voi kirjantiedoista nappia painamalla lisätä kirjan omalle luettujen kirjojen listalle
```
INSERT INTO read_books (book_id, account_id) VALUES (?, ?)
```

### Käyttäjä voi kirjautua sovellukseen ja kirjautua ulos
Käyttäjä voi kirjautua olemassa olevilla tunnuksilla järjestelmäään ja poistua

### Käyttäjä voi lisätä kirjan
Käyttöliittymän kautta voi lisätä kirjan. Aluksi tiedoilla: kirjan nimi, kirjailija, kuvaus.
```
INSERT INTO book (date_created, date_modified, title, author, description, isbn) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

### Käyttäjä voi muokata kirjojen tietoja
Käyttäjä voi muokata kaikkia kirjan tietoja: nimi, kirjailija, kuvaus.

### Käyttäjä voi listata kirjoja
Komennolla "Listaa kirjat" käyttäjä näkee kirjoista listauksia seuraavasti. Uusimmat lisätyt kirjat, luetuimmat kirjat (montako eri käyttäjää merkinnyt luetuksi), puhutuimmat kirjat (kommenttien määrä kirjassa). Jokaisesta listojen kirjasta on linkki kirjan omalle sivulle jolta voi katsoa tarkempia tietoja.
```
SELECT Book.id, Book.title, Book.author, Book.date_created FROM Book GROUP By Book.id ORDER BY 4 DESC  LIMIT 5

SELECT Book.id, Book.title, Book.author, COUNT(read_books.book_id) FROM Book LEFT JOIN read_books ON Book.id = read_books.book_id GROUP BY Book.id HAVING COUNT(read_books.book_id) > 0 ORDER BY 4 DESC LIMIT 10

SELECT Book.id, Book.title, Book.author, COUNT(Note.book_id) FROM Book LEFT JOIN Note ON Note.book_id = Book.id GROUP BY Book.id HAVING COUNT(Note.book_id) > 0 ORDER BY 4 DESC LIMIT 10
```

### Käyttäjä voi katsoa yksittäisen kirjan tiedot
Näyttää kaikki kirjan tiedot (nimi,kirjailija,kuvaus) ja käyttäjien kommentit, sekä sisältää mahdollisuuden muokata kirjan tietoja. 
```
SELECT book.id AS book_id, book.date_created AS book_date_created, book.date_modified AS book_date_modified, book.title AS book_title, book.author AS book_author, book.description AS book_description, book.isbn AS book_isbn 
FROM book 
WHERE book.id = ?

SELECT Note.note, Note.account_id, Account.name FROM Note LEFT JOIN Account ON Note.account_id = Account.id WHERE Note.book_id = ?
```

### Käyttäjä voi hakea kirjoja
Haku-toiminolla käyttäjä voi hakea kirjoja, tällä hetkellä otsikon ja kirjailijan nimen perusteella.
```
SELECT Book.id, Book.title, Book.author FROM Book WHERE lower(Book.title) LIKE lower(?) OR lower(Book.author) LIKE lower(?)
```

