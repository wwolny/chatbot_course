## intent:greet
- hej
- siemka
- witam
- dzień dobry
- dobry wieczór
- cześć
- Cześć

## intent:bye
- pa
- papa
- dowidzenia
- Dziękuje, dowidzenia!
- Dziękuję
- dzięki

## intent:affirm
- tak
- owszem
- jasne

## intent:deny
- nie
- raczej nie

## intent:compare_entities
- Który [kosztuje](attribute:price) więcej?
- Za który więcej [zapłacę](attribute:price)?
- Ile [kasy](attribute:price) kosztują te kursy?
- Który kurs [kosztuje](attribute:price) ile?
- a jakie są ich [ceny](attribute:price)?

## intent:help
- Pomóż mi
- czy mógłbyś mi pomóc
- Pomoc
- help

## intent:query_search
- wypisz kursy w [Python](technology) za co najwyżej [3000](max_price) zł
- wypisz kursy w [Python](technology) za max [4000](max_price)
- wypisz kursy [Python](technology) po co najwyżej [3000](max_price) zł
- wypisz kursy w [Python](technology) za co najmniej [3000](min_price) zł
- wypisz kursy w [Python](technology) za min [4000](min_price)
- wypisz kursy [Python](technology) po co najmniej [3000](min_price) zł
- wypisz kursy od [2000](min_price) zł do [8000](max_price) zł
- wypisz kursy między [2000](min_price) zł, a [8000](max_price) zł
- wypisz kursy między [2000](min_price), a [8000](max_price)
- wypisz kursy [Python](technology)
- wypisz kursy [Python](technology:python)
- wypisz kursy [Java](technology)
- wypisz kursy [c++](technology)
- wypisz kursy [python](technology)
- wypisz kursy [PostGIS](technology)
- wypisz kursy [Przetwarzanie Tekstu](technology)
- wypisz kursy [Jira](technology)
- wypisz kursy [Git](technology)
- wypisz kursy [Confluence](technology)
- szukam kursów w [Java](technology:java)
- pokaż kursy w [python](technology)
- [Java](technology)
- w [Javie](technology:Java)
- podaj kursy z [JEE](technology)
- jakie masz kursy z [C](technology)
- Wypisz kursy, które dotyczą języka [C++](technology:c++)
- Szukam kursów z [Pythona](technology:python)
- dzień dobry, szukam kursów internetowych dla osób zaczynającyhc naukę z [Pythonem](technology:python). Czy mógłby mi Pan polecić jakiś kurs?
- Szukam kursów w [Python](technology) dla początkujących. Czy macie coś takiego dostępnego?
- wypisz kusry z sztuki [prezentacji](technology)
- wypisz kursy z sztuki [prezentacji](technology)
- Szukam kursów dotyczacych sztuki [prezentacji](technology)
- wypisz kursy dotyczące [python](technology)

## intent:out_of_scope
- Czy możesz kupić mi kurs?
- Czy mogę założyć własny kurs?
- Chcę przetestować kurs

## intent:query_attribute
- Jaka jest [cena](attribute:price) za ten kurs?
- Ile [kosztuje](attribute:price) [pierwszy](mention) kurs?
- Jaka jest [cena](attribute:price) na [drugim](mention) kursie?
- A ile to [kosztuje](attribute:price)?
- A dla [kogo](attribute:addressedTo) jest [pierwszy](mention) kurs?
- Ile [trwa](attribute:durationInDays) [drugi](mention) kurs?
- Jakie są [wymagania](attribute:prerequisites) do [trzeciego](mention) kursu?
- ile [kosztuje](attribute:price) [pierwszy](mention)?
- Ile [trwa](attribute:durationInDays) [trzeci](mention)?
- Czy potrzebuję coś [wiedzieć](attribute:prerequisites), żeby wziąć udział w [czwartym](mention:czwarty)?
- podaj mi [wszystkie informacje](attribute:all) o [pierwszy](mention)
- ile [trwa](attribute:durationInDays) [piąty](mention:5) kurs?
- ile [kosztuje](attribute:price) ten kurs?
- Ile [trwa](attribute:durationInDays) ten kurs?
- Intersuje mnie kurs [czwarty](mention). Ile [kosztuje](attribute:price) ten kurs?
- A jakie są do niego [wymagania](attribute:prerequisites)?
- Ile dni [trwa](attribute:durationInDays) ten kurs?

## intent:query_entities
- wypisz kursy
- Czy możesz znaleźć dla mnie kurs?
- Pokaż mi dostępne kursy?
- Znajdź mi ciekawe kursy informatyczne!
- cześć, pokaż mi kursy
- Chciałbym zapisać się na kurs. Jakie kursy masz dostępne?

## intent:resolve_entity
- [1](mention)
- [3](mention)
- [2](mention)
- [4](mention)
- [5](mention)
- [Pierwszy](mention)
- [Drugi](mention)
- [Trzeci](mention)
- [Czwarty](mention)
- [Piąty](mention)
- Pokaż [pierwszy](mention)
- Pokaż [drugi](mention)
- Pokaż [trzeci](mention)
- Pokaż [czwarty](mention)
- Pokaż [piąty](mention)
- [Pierwszy](mention:1)
- [pierwszy](mention:1)
- [pierwszy](mention:1)

## intent:bot_challenge
- Czy jesteś robotem?
- Z kim rozmawiam?
- Czy jesteś człowiekiem?

## synonym:1
- Pierwszy
- pierwszy

## synonym:5
- piąty

## synonym:Java
- Javie

## synonym:addressedTo
- kogo

## synonym:all
- wszystkie informacje

## synonym:c++
- C++

## synonym:course
- kursy
- kurs
- kursów

## synonym:czwarty
- czwartym

## synonym:durationInDays
- trwa

## synonym:java
- Java

## synonym:prerequisites
- wymagania
- wiedzieć

## synonym:price
- kosztuje
- zapłacę
- kasy
- cena

## synonym:python
- Python
- Pythona
- Pythonem

## lookup:course
  data/lookup_tables/course.txt

## lookup:technology
  data/lookup_tables/keywords.txt
