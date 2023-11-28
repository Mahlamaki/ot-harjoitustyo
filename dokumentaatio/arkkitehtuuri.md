## Sovelluslogiikka

Login kirjat kuvataan Book- luokassa:

```mermaid
 classDiagram
      class Book{
          title
          author
          rating
      }

```

BookServicessä on yksi luokka. Alla listattuna sen tähänastiset metodit.

- `add_new_book(title, author, rating)`
- `browse_all_books()`

_BookService_ on yhteydessä [BookReporitory](https://github.com/Mahlamaki/ot-harjoitustyo/blob/main/src/repositories/book_repository.py)yn, jonka kautta saadaan hoidettua tietokantaannan kanssa kommunikointi.


