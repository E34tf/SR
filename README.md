## Opis
> Zbiór mikrousług podsystemu realizującego funkcję pamięci podręcznej systemu rekomendacyjnego.

> Kluczową funkcjonalnością jest zapewnienie „oportunistycznej” aktualizacji profili zapisanych w pamięci podręcznej w sposób nie blokujący dostępu do tychże profili.

> Realizacja zadania polega m.in. na zastosowaniu dwóch odmiennych serwerów bazodanowych typu NoSQL (Cassandra lub HBase oraz Redis) – naturalnie wraz z ich aplikacjami klienckimi.

> Ponadto należy zrealizować asynchroniczną komunikację między dwoma komponentami: Recommendation Engine (implementowanego w postaci zredukowanej do funkcji pozyskiwania profili użytkowników i filmów) oraz Profile Server. Tę asynchroniczną komunikację można zrealizować z użyciem technologii kolejkowych (np. implementując Queuing Server z użyciem serwera Redis).

> Autor tekstu: *Andrzej Szwabe*
> Andrzej.Szwabe@put.poznan.pl


## Wymagania
* Raport "How to".
* Działający program, realizujący zadanie.
* Zaślepki modułów systemu rekomendacyjnego, związanych z pamięcią podręczną.


## TODO:
- [ ] Obsługa:
    - [ ] Cassandra.
    - [ ] Redis.
- [ ] Dockers.
- [ ] Stworzenie reprezentacji profilu.
- [ ] Komunikacja pomiędzy docker'ami a programem.
- [ ] Komunikacja pomiędzy *Recommendation Engine* a *Profile Server*