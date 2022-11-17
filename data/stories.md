## Hello
* greet
  - utter_greet

## query entities
  * query_entities
    - action_query_entities

## query attribute
* query_attribute
  - action_query_attribute
  - slot{"mention": 1}
  - slot{"price": "1950"}

## query search
* query_search
  - action_query_search
  - slot{"technology": "Python"}
  - slot{"min_price": "1000"}
  - slot{"max_price": "3000"}

## resolve entity
* resolve_entity
  - slot{"mention": 1}
  - action_resolve_entity
  - slot{"title": "Administracja Apache Hadoop"}
  - slot{"durationInDays": "3"}

## Bye
* bye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## help
* help
  - utter_help

## out of scope
* out_of_scope
  - utter_out_of_scope

## interactive_story_1
* query_entities
    - action_query_entities
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_attribute{"attribute": "price", "mention": "pierwszy"}
    - slot{"attribute": "price"}
    - slot{"mention": "pierwszy"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Administracja Apache Hadoop"}
* query_attribute{"attribute": "durationInDays", "mention": "trzeci"}
    - slot{"attribute": "durationInDays"}
    - slot{"mention": "trzeci"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Mikroserwisy z wykorzystaniem NodeJS i Docker"}
* query_attribute{"attribute": "prerequisites"}
    - slot{"attribute": "prerequisites"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Mikroserwisy z wykorzystaniem NodeJS i Docker"}
* query_attribute{"attribute": "all", "mention": "pierwszy"}
    - slot{"attribute": "all"}
    - slot{"mention": "pierwszy"}
    - action_query_attribute
    - slot{"mention": null}
* bye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL", "Testowanie 360 - wszystko o testowaniu", "Warstwa prezentacji z użyciem JavaServer Faces", "Zarządzanie ryzykiem", "Protokół SSL i TLS", "ASP.NET MVC i WEBAPI", "JIRA - Prowadzenie i praca w projekcie agile", "Full-stack monorepo", "Przygotowanie do uzyskania certyfikatu OCP", "Zaawansowane tworzenie aplikacji z użyciem Angular", "Zaawansowane modele raportowe w Power BI", "Efektywność osobista w branży IT", "Search Driven Analytics - zastosowanie Kibany i Elasticsearcha", "Hadoop dla programistów", "Agile Testing", "Zarządzanie wymaganiami", "Reguły tworzenia aplikacji dla systemów wbudowanych i branży automotive", "Tworzenie darmowych gier", "ArcGIS Szkolenie Podstawowe", "Programowanie reaktywne w języku Java i Spring WebFlux", "Projektowanie zorientowane na użytkownika", "Programowanie w języku Swift na platformie iOS", "Implementacja Dapps w Ethereum z wykorzystaniem kontraktów w Solidity", "Planowanie i budżetowanie projektów", "Projektowanie złożonych modeli domen z wykorzystaniem Domain Driven Design", "Prezentacja i udostępnianie danych przestrzennych za pomocą GeoServera", "ISTQB Agile Tester", "Design gier komputerowych", "IBUQ Poziom Podstawowy - szkolenie z egzaminem", "Testy bezpieczeństwa nowoczesnych aplikacji internetowych", "Architektura systemów", "Wszystkie aspekty pracy nad trafnością wyników wyszukiwania w Apache Solr i Elasticsearch", "Linux w systemach wbudowanych", "SCRUM dla Software Engineers", "Tworzenie gier na platformie iOS i tvOS", "Pipeline as code - automatyzacja tworzenia pipelinów przy użyciu Jenkins Job DSL", "Tworzenie interfejsu użytkownika w grach komputerowych", "Programowanie sieciowe w języku Python", "Zaawansowany HTML", "Programowanie w języku Kotlin", "Podstawy uczenia maszynowego w języku Python", "Programowanie w języku C++", "Wprowadzenie do technologii Big Data", "Zaawansowane utrwalanie danych z użyciem JPA i Hibernate", "Analiza biznesowa - przygotowanie do certyfikacji CCBA", "Analiza danych z użyciem Apache Spark", "Nowoczesna Java", "Praktyczne wykorzystanie blockchain na przykładzie Ethereum", "Kryptografia na platformie Java w praktyce", "Szkolenie dla trenerów", "Przygotowanie do PSM", "Wzorce i dobre praktyki na platformie JEE", "Programowanie w języku Scala", "Programowanie .NET - kurs podstawowy", "Tworzenie gier z gatunku side scroller w silniku Unity", "Warsztat analityka danych w języku Python", "Nowoczesne przetwarzanie danych w R", "Leaflet - Tworzenie interaktywnych map na stronach internetowych", "Puppet Advanced - zaawansowane techniki użycia Puppet", "Test-Driven Development w języki c#", "Przygotowanie do egzaminu Unity Certified Developer", "Utrwalanie danych z użyciem JPA i Hibernate", "IQBBA Poziom Podstawowy - szkolenie z egzaminem certyfikacyjnym", "PHP 7 od podstaw", "Logika biznesowa z użyciem EJB", "Narzędzia programisty Java", "Interpretowalne uczenie maszynowe", "Responsive Web Design - projektowanie i wdrażanie", "Podstawy HTML", "Programowanie funkcyjne w języku Java", "Praca z kontenerami w chmurze Azure", "Bezpieczeństwo aplikacji w oparciu o Spring Security", "Integracja Aplikacji Korporacyjnych na przykładzie Apache Camel lub Spring Integration", "Projektowanie rozwiązań Big Data z wykorzystaniem Apache Hadoop", "Analiza oraz zabezpieczanie przed szkodliwym kodem w praktyce", "Tworzenie gier w wirtualnej rzeczywistości w silniku Unity", "Microsoft Project w zarządzaniu projektami", "Testowanie na platformie Java", "Spring framework", "DevOps Foundations", "DevOps - zwinne dostarczanie aplikacji", "Entity Framework Core 2.0", "Skuteczne zarządzanie komunikacją i przywództwo w projektach i programach IT", "Deep Learning", "Lepszy kod dzięki technikom refaktoryzacji i wzorcom projektowym", "Programowanie kart Java Card", "Działanie i wykorzystanie blockchain", "Efektywne tworzenie hybrydowych aplikacji mobilnych z Ionic Framework", "Strumieniowe przetwarzanie Big Data", "Analizy przestrzenne w QGIS", "Podstawy języka UML2 w realnych projektach", "Tworzenie aplikacji na platformie Android", "Zarządzanie konfliktem", "Podstawy CSS", "Projektowanie systemów Big Data dla architektów", "Kubernetes w praktyce", "User Experience - projektowanie satysfakcji odbiorcy", "Tworzenie gier FPS w silniku Unity", "Automatyzacja wdrożeń z użyciem Azure Resource Manager", "Automatyzacja testów funkcjonalnych na platformie Android z wykorzystaniem narzędzia Espresso", "Tworzenie gier na platformę Android w silniku Unity", "Wprowadzenie do platformy JEE", "Podniesienie efektywności w chmurze z Ansible", "Programowanie .NET - kurs zaawansowany", "Budowanie rozwiązań serverless/FaaS w chmurze Azure ", "Analiza biznesowa w praktyce", "Tworzenie aplikacji Android w języku Kotlin", "Tworzenie aplikacji z użyciem Angular", "Zaawansowane programowanie w języku Java", "QGIS - zaawansowane metody wizualizacji danych przestrzennych", "Programowanie w języku python", "Podstawy analizy danych numerycznych w języku Python", "Własna wyszukiwarka w oparciu o Apache Solr i Elasticsearch", "Zaawansowane programowanie w języku Swift", "NativeScript w praktyce", "Efektywne programowanie w języku Java", "Zautomatyzowane testy usług sieciowych z użyciem SoapUI", "Zaawansowane programowanie w języku Python", "Tworzenie gier z gatunku Hyper Casual w silniku Unity", "Korporacyjna Magistrala Usług na przykładzie Apache ServiceMix", "Zabezpieczenie transmisji danych w sieci", "Testowanie bezpieczeństwa rozwiązań IoT", "Tworzenie gier wykorzystujących rozszerzoną rzeczywistość w silniku Unity", "Modelowanie procesów biznesowych z użyciem notacji BPMN2", "Budowanie aplikacji React przy wykorzystaniu języka TypeScript", "Prototypowanie gier", "Wzorce projektowe i refaktoryzacja w języku Java", "Podstawy analizy danych w R", "Wzorce projektowe w języku Python", "Metody optymalizacji gier w silniku Unity", "Tworzenie aplikacji z wykorzystaniem NestJS", "Zaawansowane tworzenie aplikacji na platformie Android", "Chmura dla biznesu", "Narzędzia OWAS dla testerów", "Tworzenie i ocena specyfikacji wymagań", "Tworzenie Web Services przy użyciu Windows Communication Foundation Framework", "Projektowanie hurtowni danych z wykorzystaniem pakietu Pentaho Business Intelligence", "Programowanie współbieżne w języku C++", "Tworzenie aplikacji z użyciem ReactJS", "Podejście produktowe w wytwarzaniu oprogramowania", "Tworzenie aplikacji webowych z użyciem Vaadin", "Modelowanie procesów biznesowych w UML i BPMN przy użyciu narzędzia Enterprise Architect", "Techniczne aspekty budowania wydajnych procesów ładowania hurtowni danych z wykorzystaniem Pentaho Data Integration", "Tworzenie aplikacji w chmurze z wykorzystaniem Windows Azure", "Testy automatyczne i Test Driven Design w JavaScript", "Zarządzanie projektami wg metody Łańcucha Krytycznego - CCPM", "Przypadki użycia w zarządzaniu wymaganiami", "Automatyzacja w procesie testowania oprogramowania", "UML2 dla analityków", "Zaawansowany Spring framework", "Wydajność w języku Java", "Infrastruktura Klucza Publicznego", "Docker w praktyce", "Wielowątkowość w języku Java", "Dobre praktyki programowania obiektowego w języku C++", "Programowanie w języku Groovy", "Bazy danych NoSQL - MongoDB", "Migracja AngularJS do Angular", "Techniczne aspekty eksploracji danych zgromadzonych w hurtowni danych  z wykorzystaniem Pentaho Data Mining", "Korporacyjna Magistrala Usług na przykładzie Mule ESB", "Tworzenie gier Top-Down w silniku Unity", "Enterprise Architect - narzędzie do modelowania", "Web Components", "Programowanie w języku Java", "Wprowadzenie do GIS na przykładzie platformy QGIS", "Wzorce projektowe w języku C++", "Full-stack Firebase", "Utrzymanie jakości w grach komputerowych", "Automatyzacja i zarządzenie procesami z użyciem Spring Batch", "Zaawansowane style CSS i preprocesory w praktyce", "Rozszerzanie edytora Unity", "Praktyczne zastosowanie bibliotek Boost oraz nowych standardów C++", "Warsztat analityka danych w R", "Jak rekrutować specjalistów w branży it", "Wstęp do NoSQL", "Elasticsearch - od podstaw do zagadnień zaawansowanych", "JIRA - Administracja systemem wspomagającym śledzenie błędów i zarządzanie projektem", "Project Portfolio Management - budowa i zarządzanie portfelem projektów", "Wprowadzenie do SOA", "Analiza danych tekstowych i języka naturalnego", "Tworzenie aplikacji WebGIS na bazie PostGIS, Geoserver, OpenLayers i QGIS", "Certyfikowany Administrator Kubernetes'a", "Certyfikowany Programista Aplikacji Kubernetes", "Podstawy programowania w R", "Wprowadzenie do bezpieczeństwa informacji", "Wprowadzenie do chmury AWS", "Podstawy systemu Linux", "Confluence jako narzędzie wspierające zarządzanie treścią", "Continuous Integration", "Administracja serwerem Tomcat", "Modelowanie z użyciem notacji UML2", "Apache Solr - od podstaw do zagadnień zaawansowanych", "Tworzenie aplikacji internetowych z użyciem frameworka Laravel", "Motywacja 4.0", "Bazy danych NoSQL - Cassandra", "Wytwarzanie i dostarczanie oprogramowania w kulturze devops z użyciem Azure Devops", "Programowanie w języku JavaScript", "Analiza kodu za pomocą SonarQube", "Zalecenia CERT dla języka C++ w praktyce", "Podstawy uczenia maszynowego z R", "Administracja serwerem JBoss", "Zalecenia CERT dla języka C w praktyce", "Przetwarzanie Big Data z użyciem Apache Spark", "Programowanie w Qt - poziom podstawowy", "Wizualizacja danych w R", "Tworzenie gier z wykorzystaniem Unity ", "RxJS - Reaktywne programowanie w JavaScript", "Domain Driven Design w procesie tworzenia aplikacji na przykładzie rozwiązań JEE", "Techniki myślenia analitycznego i podejmowanie decyzji biznesowych w obszarze IT", "Architektura mikroserwisów z wykorzystaniem Spring Cloud", "Tworzenie aplikacji webowych z wykorzystaniem ExpressJS", "Konfiguracja protokołu SSL i TLS", "Przygotowanie do zdobycia certyfikatu IQBBA Poziom Podstawowy", "Rozwój oprogramowania z wykorzystaniem Refaktoryzacji", "Testowanie użyteczności i UX", "Puppet Essentials - podstawy języka i technologii Puppet", "Bazy danych NoSQL - Redis", "Projektowanie i programowanie obiektowe w języku PHP", "Kontrola wersji z Git", "Testy automatyczne na platformie .NET", "Przygotowanie do uzyskania certyfikatu OCA", "PWA - Progresywne aplikacje webowe", "Modelowanie aplikacji z użyciem notacji UML dla wytwórców aplikacji wbudowanych", "Android - programowanie reaktywno-funkcyjne", "Testy wydajnościowe aplikacji internetowych z wykorzystaniem Apache JMeter ", "Inżynieria odwrotna kodu w systemach Windows i Linux oraz metody zabezpieczania programów", "Budowanie efektywnych zespołów", "Gatsby - statyczne strony i dynamiczne aplikacje", "OpenLayers 3 - Tworzenie interaktywnych map na stronach internetowych", "Zarządzanie danymi przestrzennymi w Oracle Spatial", "iOS - programowanie reaktywno-funkcyjne", "Tworzenie aplikacji z użyciem VueJS", "MapInfo - szkolenie podstawowe", "Programowanie w języku C"]}

## interactive_story_1
* greet
    - utter_greet
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_entities
    - action_query_entities
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_entities
    - action_query_entities
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Administracja Apache Hadoop", "Programowanie w Qt - poziom zaawansowany", "Mikroserwisy z wykorzystaniem NodeJS i Docker", "Zarządzanie Projektami IT", "Wprowadzenie do języka SQL i bazy PostgreSQL"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Programowanie sieciowe w języku Python", "Podstawy uczenia maszynowego w języku Python", "Warsztat analityka danych w języku Python", "Programowanie w języku python", "Podstawy analizy danych numerycznych w języku Python"]}
* query_search{"technology": "Java"}
    - slot{"technology": "Java"}
    - action_query_search
    - slot{"listed_items": ["Warstwa prezentacji z użyciem JavaServer Faces", "Programowanie reaktywne w języku Java i Spring WebFlux", "Nowoczesna Java", "Kryptografia na platformie Java w praktyce", "Testowanie na platformie Java"]}
* query_search{"technology": "c++"}
    - slot{"technology": "c++"}
    - action_query_search
    - slot{"listed_items": ["Wzorce projektowe w języku C++", "Praktyczne zastosowanie bibliotek Boost oraz nowych standardów C++", "Dobre praktyki programowania obiektowego w języku C++", "Zalecenia CERT dla języka C++ w praktyce", "Programowanie w języku C++"]}
* stop
    - utter_help

## interactive_story_1
* greet
    - utter_greet
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Programowanie w języku python", "Programowanie sieciowe w języku Python", "Podstawy analizy danych numerycznych w języku Python", "Zaawansowane programowanie w języku Python", "Wzorce projektowe w języku Python"]}
* query_attribute{"attribute": "durationInDays", "mention": "5"}
    - slot{"attribute": "durationInDays"}
    - slot{"mention": "5"}
    - action_query_attribute
* query_attribute{"attribute": "price"}
    - slot{"attribute": "price"}
    - action_query_attribute
* query_search{"technology": "java"}
    - slot{"technology": "java"}
    - action_query_search
    - slot{"listed_items": ["RxJS - Reaktywne programowanie w JavaScript", "Programowanie w języku Java", "Warstwa prezentacji z użyciem JavaServer Faces", "Programowanie reaktywne w języku Java i Spring WebFlux", "Narzędzia programisty Java"]}
* stop
    - utter_help

## interactive_story_1
* greet
    - utter_greet
* query_search{"technology": "c++"}
    - slot{"technology": "c++"}
    - action_query_search
    - slot{"listed_items": ["Programowanie współbieżne w języku C++", "Programowanie w języku C++", "Zalecenia CERT dla języka C++ w praktyce", "Wzorce projektowe w języku C++", "Dobre praktyki programowania obiektowego w języku C++"]}
* compare_entities{"attribute": "price"}
    - slot{"attribute": "price"}
    - action_compare_entities
* query_attribute{"attribute": "prerequisites", "mention": "trzeciego"}
    - slot{"attribute": "prerequisites"}
    - slot{"mention": "trzeciego"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Zalecenia CERT dla języka C++ w praktyce"}
* query_attribute{"attribute": "durationInDays"}
    - slot{"attribute": "durationInDays"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Zalecenia CERT dla języka C++ w praktyce"}
* bye
    - utter_goodbye

## interactive_story_1
* query_entities
    - action_query_entities
    - slot{"listed_items": ["Programowanie .NET - kurs podstawowy", "Analiza danych tekstowych i języka naturalnego", "Korporacyjna Magistrala Usług na przykładzie Apache ServiceMix", "OpenLayers 3 - Tworzenie interaktywnych map na stronach internetowych", "ISTQB Agile Tester"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"listed_items": ["Programowanie sieciowe w języku Python", "Wzorce projektowe w języku Python", "Podstawy analizy danych numerycznych w języku Python", "Warsztat analityka danych w języku Python", "Podstawy uczenia maszynowego w języku Python"]}
* query_attribute{"mention": "czwarty", "attribute": "price"}
    - slot{"attribute": "price"}
    - slot{"mention": "czwarty"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Warsztat analityka danych w języku Python"}
* query_attribute{"attribute": "prerequisites"}
    - slot{"attribute": "prerequisites"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Warsztat analityka danych w języku Python"}
* query_attribute{"attribute": "durationInDays"}
    - slot{"attribute": "durationInDays"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Warsztat analityka danych w języku Python"}
* bye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* query_search{"technology": " Pytho"}
    - slot{"technology": [" Pytho"]}
    - action_query_search
    - slot{"listed_items": ["Podstawy analizy danych numerycznych w języku Python", "Programowanie sieciowe w języku Python", "Strumieniowe przetwarzanie Big Data", "Zaawansowane programowanie w języku Python", "Warsztat analityka danych w języku Python"]}
* resolve_entity{"mention": "1"}
    - slot{"mention": "1"}
    - action_resolve_entity

## interactive_story_1
* greet
    - utter_greet
* query_search{"technology": "prezentacji"}
    - slot{"technology": ["prezentacji"]}
    - action_query_search
* query_search{"technology": "prezentacji"}
    - slot{"technology": ["prezentacji"]}
    - action_query_search
* query_search{"technology": "prezentacji"}
    - slot{"technology": ["prezentacji"]}
    - action_query_search
    - slot{"listed_items": ["Wizualizacja danych w R", "Tworzenie aplikacji webowych z użyciem Vaadin", "MapInfo - szkolenie podstawowe", "Warstwa prezentacji z użyciem JavaServer Faces"]}
* resolve_entity{"mention": "1"}
    - slot{"mention": "1"}
    - action_resolve_entity
* bye
    - utter_goodbye
* stop
    - utter_help

## interactive_story_1
* greet
    - utter_greet
* query_search{"technology": "python"}
    - slot{"technology": ["python"]}
    - action_query_search
    - slot{"listed_items": ["Deep Learning", "Programowanie w języku python", "Zaawansowane programowanie w języku Python", "Praca z kontenerami w chmurze Azure", "Podstawy uczenia maszynowego w języku Python"]}
* resolve_entity{"mention": "1"}
    - slot{"mention": "1"}
    - action_resolve_entity
* compare_entities{"attribute": "price"}
    - slot{"attribute": "price"}
    - action_compare_entities
* bye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* query_search{"technology": "OWAS"}
    - slot{"technology": ["OWAS"]}
    - action_query_search
    - slot{"listed_items": ["Narzędzia OWAS dla testerów"]}
    - slot{"mention": "1"}
* resolve_entity
    - action_resolve_entity
* query_attribute{"attribute": "price"}
    - slot{"attribute": "price"}
    - action_query_attribute
* query_attribute{"attribute": "prerequisites"}
    - slot{"attribute": "prerequisites"}
    - action_query_attribute
* bye
    - utter_goodbye
