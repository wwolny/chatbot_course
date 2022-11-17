## intent:greet
- heja
- helo
- witam
- dzień dobry
- cześć
- hej
- witam, nazywam się Jan Kowalski
- dzień dobry nazywam się Andrzej
- witam jestem Krzysztof
- dzień dobry nazywam się Andrzej i pracuję w firmie informatycznej
- witam nazwyam się Krzyszof 

## intent:bye
- dzięki, dowidzenia
- spadam, cześć
- super, zadzwonię zapisac się na kurs
- Dzięki
- dziękuję za informajce na temat kursów
- bardzo odpowiada mi oferta kursów, dziękuję
- jestem zadowolny, dziękuję za pomoc
- nic się już więcej nie dowim, do widzenia
- to już wszystko co chciałem się dowiedzieć
- bardzo mi pomogłeś, dzięki
- nic się nie dowiedziałem, muszę kończyć

## intent:affirm
- tak, zgadza się
- zgadza się
- owszem
- tak
- właśnie czegos takiego szukałem
- tak jesst
- dokładnie tak
- dobrze

## intent:deny
- wolałbym nie
- raczej nie
- szukam czegoś innego
- nie odpowiada mi to
- zupełnie nie
- coś jest nie tak
- przeczę

## intent:compare_entities
- W jakiej one są [cenie](attribute:price)?
- Jaki jest ich [koszt](attribute:price)?
- proszę o porównanie tych kursów ze względu na [cenę](attribute:price)?
- czy mógłbym zobaczyć jaki jest [czas trwania](attribute:durationInDays) tych kursów?
- chciałbym zobaczyć porównanie [cen](attribute:price) tych kursów
- takich kursów szukałem, czy mógłbym zobaczyć porównanie [cen](attribute:price) tych kursów
- proszę pokazać mi [ceny](attribute:price) tych szkoleń
- a jak wygląda sytuacja z [cenami](attribute:price) za te szkolenia?
- czy mógłbym zobaczyć porównanie [cen](attribute:price) tych kursów?
- ciekaw jestem jak wygląda porównanie [cen](attribute:price) przedstawionych szkoleń 

## intent:help
- Pomocy
- nie rozumiem, potrzebuję pomocy
- o co tutaj chodzi?
- help
- proszę o informację co tu mogę znaleźć
- co tu mogę znaleźć
- jaką pomoc mogę od ciebie otrzymać

## intent:query_search
- Chciałbym zapisać się na kurs [Javy](technology:Java).
- Witam, jestem początkującym programistą i chciałbym nauczyć się programować w [Pythonie](technology:Python). Czy dostanę u Państwa taki kurs?
- Poszukuję kursów internetowych dotyczących programowania [aplikacji mobilnych](technology).
- Dzień dobry, szukam kursów dotyczących programowania w [JS](technology). Szczególnie interesuję mnie pisanie stron 
- Proszę mi podać Państwa ofertę dotyczącą [Dockera](technology)
- Szukam kursów na temat [zarządzania](technology) i programów jak [Confluence](technology), czy [Jira](technology)
- Chciałbym zapisac się na kurs z [zarządzania projektami](technology). Czy mają Państwo u siebie takie kursy? W jakiej [cenie](attribute:price) mogę je znaleźc?
- Potrzebuję jak najszybciej znaleźć kurs dla mojej firmy z [Kubernetes](technology) i [Dockera](technology)
- Witam, szukam szkolenia z pakietu [Microsoft Office](technology)
- chciałbym zpaisać się na kurs z tworzwenia oprogramowania [Agile](technology)
- czy są dostępne kursy o tematyce programowania w [C](technology)?
- szukam szkoleń dla mojej firmy z technologii [PHP](technology)
- chciałbym się doszkolić z [Power BI](technology), gdyż potrzebuję na zajęcia na uczelni
- czy są tutaj dostępne kursy z [Swifta](technology)???
- Chciałbym nauczyć się [Javascriput](technology), czy macie coś dostępnego na ten temat?
- Jakie kursy są dostępne z [ElasticSearcha](technology) tutaj?
- chciałbym nauczyć się obsługiwać [Linuxa](technology), czy są dostępne jakieś kursy z tego?
- potrzebuję nauczyć się do pracy technologii [Cloudowych](technology), czy macie coś z [AWS](technology) lub [GCP](technology)??
- poszukuję kursów o tematyce [Deep Learningowej](technology)
- chciałbym nauczyć się [NLP](technology), czy macie dostępne jakieś kursy z [Spacy](technology) lub [NLTK](technology)

## intent:out_of_scope
- Chciałbym kupić mrożony jogurt
- lalala

## intent:query_attribute
- Oba kursy wyglądając bardzo ciekawie, proszę mi podać [cenę](attribute:price) za ten [pierwszy](mention) kurs?
- Rozumiem, a ile [kosztuje](attribute:price) ten [trzeci](mention) kurs?
- Ile [zapłacę](attribute:price) za [drugi](mention) kurs?
- A ile to [wyjdzie](attribute:price)?
- Chciałbym wiedzieć dla [kogo](attribute:addressedTo) jest [piąty](mention) kurs?
- Czy [drugi](mention) kurs długo [trwa](attribute:durationInDays)?
- Czy [czwarty](mention) kurs ma jakieś [wymagania](attribute:prerequisites)?
- ile [zapłacę](attribute:price) za [ostatni](mention)?
- Czy potrzebuję mieć jakąś [wiedzę](attribute:prerequisites), żeby wziąć udział w [piątym](mention)?
- interesują mnie [cena](attribute:price) za ten [piąty](mention)
- chciałbym poznać [wymagania](attribute:prerequisites) [czwartego](mention)
- proszę rozwinąć [cenę](attribute:price) [trzeci](mention)
- czy mógłbym zapoznać się z [czasem trwania](attribute:durationInDays) [pierwszego](mention)
- bardzo ciekawi mnie [koszt](attribute:price) [ostatniego](mention)
- potrzebuję informacji na temat [ceny](attribute:price) [ostatniego](mention)
- ten kurs [piąty](mention) jaką ma [cenę](attribute:price)
- bardzo chciałbym się zaznajomić z [wymaganiami](attribute:prerequisites) kursu [drugiego](mention)
- czy można coś więcej się dowiedzieć na temat [wymagań](attribute:prerequisites) kursu [trzeciego](mention)
- a jakie są [wymagania](attribute:prerequisites) do kursu [piątego](mention)

## intent:query_entities
- wypisz jakiś kurs
- Czy możesz znaleźć dla mnie jakiś dowolny kurs?
- Pokaż mi dostępne kursy?
- chciałbym zobaczyć przykładowe kursy
- poszukuję kursów
- jakie kursy możesz mi zaoferować

## intent:resolve_entity
- opowiedz mi więcej o [piątym](mention)
- podoba mi się [drugi](mention). czy mógłbyś rozwinąć?
- chciałbym zapoznać się ze wszystkimi informacjiami na temat [pierwszego](mention)
- podaj mi wszystkie informacje o [pierwszym](mention)
- interesuje mnie kurs [pierwszy](mention), czy mógłbyś przedstawić mi wszystkie informacje na jego temat?
- chciałbym poczytać więcej o szkoleniu [pierwszym](mention), czy mógłbyś rozwinąć?
- proszę powiedzieć mi więcej o szkoleniu [pierwszym](mention)
- bardzo ciekawi mnie szkolenie [pierwsze](mention)
- prosze rozwinąć szkolenie [pierwsze](mention)
- infromacje o [pierwszym](mention)
- [pierwszy](mention)
- przedstaw [pierwszy](mention)
- pokaż [pierwszy](mention)
- chciałbym przeanalizować [pierwsze](mention) szkolenie
- [pierwsze](mention) szkolenie wygląda dobrze. rozwiń je proszę
- czy posiadasz więcej informacji o [pierwszym](mention) szkoleniu???????
- interesujący kurs [pierwszy](mention) prosze mi rozwinąć
- interesujący kurs [pierwszy](mention) prosze mi przedstawić

## intent:bot_challenge
- Ja tutaj chyba rozmawiam z robotem!

