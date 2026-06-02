# Mācību satura audits

Datums: 2026-06-02

Šis audits salīdzina `sasnRez.html` ierakstītos sasniedzamos rezultātus ar faktiskajām mācību stundu lapām. SR kodi tiek vērtēti kursa/vecumposma kontekstā, jo, piemēram, `2.4.1.` 9. klases datorikā, Programmēšanā I un Programmēšanā II nav viens un tas pats rezultāts.

## Metodika

- Obligātie SR ir `sasnRez.html` tabulu ieraksti ar `class="sr-kods"`.
- 9. klases datorikas caurviju prasmes un mācību jomas mērķi ar `goal-num` ir pārbaudīti atsevišķi, jo tie jau tiek lietoti daļā stundu SR atsaucēs.
- Par mācību stundām skaitītas visas ne-`main.html` lapas mapēs `datorika9`, `robotika`, `programmesana1` un `programmesana2`. Kursu un tēmu ievadlapas auditā netiek skaitītas kā stundas.
- Stundas SR piesaiste tiek ņemta no stundu ievaddaļas: no `h1` līdz pirmajam `h2`, kur lapās atrodas SR saites.
- “Ieteicamā piesaiste” ir auditora priekšlikums, nevis seguma fakts; SR kļūst “nosegts” tikai tad, kad konkrētā stunda to tiešām norāda vai saturā tiek pievienota atbilstoša aktivitāte.

## Kopsavilkums

| Kurss | Stundas | Obligātie SR | Nosegti | Nenosegti | Piezīmes |
|---|---:|---:|---:|---:|---|
| Datorika 9. klase | 30 | 37 | 25 | 12 | Jāpiesaista trūkstošie SR; caurviju/mērķu robi: 3 |
| Robotika 7. klase | 10 | 7 | 7 | 0 | OK |
| Programmēšana I | 72 | 29 | 25 | 4 | Jāpiesaista trūkstošie SR |
| Programmēšana II | 36 | 23 | 16 | 7 | Jāpiesaista trūkstošie SR |

## Galvenie secinājumi

- Kopā atrasti 23 obligātie `sasnRez.html` SR, kuri nav piesaistīti nevienai atbilstošā kursa stundai.
- Visām analizētajām stundu lapām ir vismaz viena SR atsauce.
- Pēc audita korekcijas vairs nav stundu ar sveša vecumposma SR kodiem: `robotika/rbtk7_15.html` tagad lieto `D.7.*` kodus, nevis 9. klases datorikas kodus.
- Pēc audita korekcijas `programmesana1/prog1_7/prog1_74.html` SR saite ir korekti aizvērta, tāpēc SR parsēšana un fokusa zona vairs neizplūst tālāk lapā.

## Nenosegtie obligātie SR

### Datorika 9. klase

| SR | Grupa | Īss saturs | Ieteicamā piesaiste |
|---|---|---|---|
| `1.1.3` | Dizaina process un tehnoloģijas | Prot veikt darbības ar rokas un elektriskajiem instrumentiem, ierīcēm, iekārtām un programmvadāmajām ierīcēm darbā ar dažādiem materiāliem.... | [dat9_15](datorika9/dat9_15.html), [dat9_16](datorika9/dat9_16.html), [dat9_55](datorika9/dat9_55.html) |
| `1.4.3` | Dizaina process un tehnoloģijas | Vērtē savu un citu skolēnu izstrādāto dizaina risinājumu atbilstoši pašu izstrādātajiem kritērijiem. Sniedz pamatotu atgriezenisko saiti par... | [dat9_55](datorika9/dat9_55.html), [dat9_56](datorika9/dat9_56.html) |
| `3.4.4` | Dizaina process un tehnoloģijas | Pēta, kā uzņēmumi un dizaina risinājumu izstrādātāji plāno un īsteno inovācijas procesus un attīsta produktus. | [dat9_13](datorika9/dat9_13.html), [dat9_54](datorika9/dat9_54.html) |
| `2.3.2` | Datorika, digitālā pratība un programmēšana | Skaidro vienkārša datortīkla uzbūves pamatprincipus (to skaitā klientservera arhitektūru). Klasificē ar datortīkliem biežāk saistītas ierīces un... | [dat9_11](datorika9/dat9_11.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.3` | Datorika, digitālā pratība un programmēšana | Pārzina dažādus datu attēlošanas veidus (to skaitā tiešsaistē) un tos lieto atbilstoši savu mērķu sasniegšanai. | [dat9_34](datorika9/dat9_34.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.4` | Datorika, digitālā pratība un programmēšana | Prezentācijas sagatavošanai un demonstrēšanai efektīvi izmanto prezentāciju lietotnes rīkus un tehniskas ierīces. Plāno, izveido un demonstrē... | [dat9_16](datorika9/dat9_16.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.8` | Datorika, digitālā pratība un programmēšana | Apvieno teksta, attēlu, audio un video saturu vienotā multimediju produktā, ievērojot izvirzīto mērķi un mērķauditoriju. | [dat9_26](datorika9/dat9_26.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.9` | Datorika, digitālā pratība un programmēšana | Risinājuma radīšanā dublē dažāda veida saturu starp dažādu tipu dokumentiem, nepieciešamības gadījumā nodrošinot vienvirziena informācijas... | [dat9_22](datorika9/dat9_22.html), [dat9_24](datorika9/dat9_24.html) |
| `2.5.1` | Datorika, digitālā pratība un programmēšana | Apmainās ar informāciju virtuālajā vidē, izmantojot dažādas formas un risinājumus, tai skaitā skaidro e-pasta adreses struktūru un lieto dažādas... | [dat9_56](datorika9/dat9_56.html) |
| `2.5.2` | Datorika, digitālā pratība un programmēšana | Lieto tīmekļvietnes ar autorizāciju un bez tās, tai skaitā veic lietotāja konta aktivizēšanu, deaktivizēšanu un dzēšanu. Izmanto mācību procesā... | [dat9_11](datorika9/dat9_11.html), [dat9_56](datorika9/dat9_56.html) |
| `2.5.4` | Datorika, digitālā pratība un programmēšana | Nosauc piemērotākā interneta pakalpojumu sniedzēja un interneta pieslēguma abonēšanas veida izvēles svarīgākos kritērijus, kā arī biežāk lietoto... | [dat9_13](datorika9/dat9_13.html), [dat9_56](datorika9/dat9_56.html) |
| `2.6.3` | Datorika, digitālā pratība un programmēšana | Pārvalda programmējamas ierīces (mikrokontrolierus, robotus), izveidojot un palaižot vienkāršus algoritmus to vadībai. Lieto sensoru ievades... | [rbtk7_21](robotika/rbtk7_21.html), [rbtk7_25](robotika/rbtk7_25.html), [dat9_46](datorika9/dat9_46.html) |

### Robotika 7. klase

Visi obligātie SR ir piesaistīti vismaz vienai stundai.

### Programmēšana I

| SR | Grupa | Īss saturs | Ieteicamā piesaiste |
|---|---|---|---|
| `2.3.1` | Sasniedzamie rezultāti (Optimālais līmenis) | Pēta un analizē datorikas nozares attīstību un tās ietekmi uz sabiedrību. | [prog1_11](programmesana1/prog1_1/prog1_11.html), [prog1_62](programmesana1/prog1_6/prog1_62.html) |
| `2.3.3` | Sasniedzamie rezultāti (Optimālais līmenis) | Izvērtē tehnoloģiju lomu un ietekmi dažādās dzīves jomās. | [prog1_92](programmesana1/prog1_9/prog1_92.html), [prog1_125](programmesana1/prog1_12/prog1_125.html) |
| `2.4.2` | Sasniedzamie rezultāti (Optimālais līmenis) | Argumentēti izvēlas programmēšanas rīkus un bibliotēkas. | [prog1_91](programmesana1/prog1_9/prog1_91.html), [prog1_122](programmesana1/prog1_12/prog1_122.html) |
| `2.4.3` | Sasniedzamie rezultāti (Optimālais līmenis) | Izstrādā programmatūras prototipus un tos testē. | [prog1_86](programmesana1/prog1_8/prog1_86.html), [prog1_126](programmesana1/prog1_12/prog1_126.html) |

### Programmēšana II

| SR | Grupa | Īss saturs | Ieteicamā piesaiste |
|---|---|---|---|
| `2.3.1` | Sasniedzamie rezultāti (Augstākais līmenis) | Pēta un analizē datorikas nozares attīstību un tās ietekmi uz sabiedrību padziļinātos projektos. | [prog2_11](programmesana2/prog2_1/prog2_11.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.3.2` | Sasniedzamie rezultāti (Augstākais līmenis) | Skaidro datorikas nozares galvenos virzienus un profesijas augstākajā līmenī. | [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.4.3` | Sasniedzamie rezultāti (Augstākais līmenis) | Izstrādā programmatūras prototipus un tos testē. | [prog2_16](programmesana2/prog2_1/prog2_16.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.5` | Sasniedzamie rezultāti (Augstākais līmenis) | Veic datu analīzi un vizualizāciju. | [prog2_55](programmesana2/prog2_5/prog2_55.html), [prog2_64](programmesana2/prog2_6/prog2_64.html) |
| `2.4.8` | Sasniedzamie rezultāti (Augstākais līmenis) | Dokumentē kodu un ievēro koda noformēšanas vadlīnijas. | [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.9` | Sasniedzamie rezultāti (Augstākais līmenis) | Lieto versiju pārvaldības sistēmas (Git). | [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.4.11` | Sasniedzamie rezultāti (Augstākais līmenis) | Lieto standartizētas bibliotēkas un API. | [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |

## Datorika 9. klases caurviju un mērķu pārklājums

| Kods | Statuss | Stundas / ieteikums |
|---|---|---|
| `5.2.1` | Nosegts | [3.1 Ievads JavaScript un mainīgie](datorika9/dat9_31.html), [3.2 Datu tipi un interaktivitāte (Input/Output)](datorika9/dat9_32.html), [3.3 Loģiskie operatori un sazarojumi (If/Else)](datorika9/dat9_33.html), [3.5 Cikli (Loops) un atkārtošanās loģika](datorika9/dat9_35.html), [3.6 Noslēguma projekts: Radošā teksta spēle JS](datorika9/dat9_36.html) |
| `5.2.2` | Nav piesaistīts | [dat9_14](datorika9/dat9_14.html), [dat9_54](datorika9/dat9_54.html) |
| `5.2.3` | Nosegts | [1.6 Noslēguma projekts: Spēles projekta pieteikums](datorika9/dat9_16.html), [3.6 Noslēguma projekts: Radošā teksta spēle JS](datorika9/dat9_36.html), [5.6 Noslēguma projekts: Pilnvērtīga spēle internetā](datorika9/dat9_56.html) |
| `5.2.4` | Nosegts | [4.6 Noslēguma projekts: Spēles dzinēja prototips](datorika9/dat9_46.html), [5.5 Spēles testēšana, atkļūdošana un publicēšana](datorika9/dat9_55.html) |
| `5.2.5` | Nav piesaistīts | [dat9_13](datorika9/dat9_13.html), [dat9_56](datorika9/dat9_56.html) |
| `5.2.6` | Nosegts | [1.1 Izstrādes vide un GitHub integrācija](datorika9/dat9_11.html), [2.5 Datņu sistēmas organizēšana un arhīvi](datorika9/dat9_25.html), [3.1 Ievads JavaScript un mainīgie](datorika9/dat9_31.html), [3.2 Datu tipi un interaktivitāte (Input/Output)](datorika9/dat9_32.html) |
| `7.6` | Nav piesaistīts | [dat9_16](datorika9/dat9_16.html), [dat9_56](datorika9/dat9_56.html) |

## Stunda pret SR

### Datorika 9. klase

| Stunda | SR kodi | Atbilstība |
|---|---|---|
| [1.1 Izstrādes vide un GitHub integrācija](datorika9/dat9_11.html) | `2.3.1`, `5.2.6` | Atbilst vecumposmam |
| [1.2 HTML skelets un satura strukturēšana](datorika9/dat9_12.html) | `2.6.1`, `2.3.3` | Atbilst vecumposmam |
| [1.3 Dizaina pētniecība un tirgus analīze](datorika9/dat9_13.html) | `1.1.1`, `1.2.3` | Atbilst vecumposmam |
| [1.4 Spēles koncepcija un mērķauditorija](datorika9/dat9_14.html) | `1.2.1`, `1.2.2` | Atbilst vecumposmam |
| [1.5 UX/UI pamati un spēles prototipēšana](datorika9/dat9_15.html) | `1.1.2`, `1.3.2` | Atbilst vecumposmam |
| [1.6 Noslēguma projekts: Spēles projekta pieteikums](datorika9/dat9_16.html) | `1.3.1`, `1.5.1`, `2.6.1`, `5.2.3` | Atbilst vecumposmam |
| [2.1 CSS pamati un vizuālā ergonomika](datorika9/dat9_21.html) | `1.1.1`, `2.5.3` | Atbilst vecumposmam |
| [2.2 Izkārtojuma kontrole un "Box Model"](datorika9/dat9_22.html) | `1.1.1`, `2.4.1` | Atbilst vecumposmam |
| [2.3 Grafisko resursu sagatavošana un optimizācija](datorika9/dat9_23.html) | `2.4.6`, `2.4.7` | Atbilst vecumposmam |
| [2.4 Audio materiālu apstrāde un integrācija](datorika9/dat9_24.html) | `2.4.6`, `2.4.10` | Atbilst vecumposmam |
| [2.5 Datņu sistēmas organizēšana un arhīvi](datorika9/dat9_25.html) | `2.3.3`, `5.2.6` | Atbilst vecumposmam |
| [2.6 Noslēguma projekts: Stilizēta spēles lapa](datorika9/dat9_26.html) | `1.4.1`, `2.4.5`, `2.4.6`, `2.4.10` | Atbilst vecumposmam |
| [3.1 Ievads JavaScript un mainīgie](datorika9/dat9_31.html) | `2.6.1`, `5.2.1`, `5.2.6` | Atbilst vecumposmam |
| [3.2 Datu tipi un interaktivitāte (Input/Output)](datorika9/dat9_32.html) | `2.6.1`, `5.2.1`, `5.2.6` | Atbilst vecumposmam |
| [3.3 Loģiskie operatori un sazarojumi (If/Else)](datorika9/dat9_33.html) | `2.6.1`, `5.2.1` | Atbilst vecumposmam |
| [3.4 Masīvi (Arrays) un datu strukturēšana](datorika9/dat9_34.html) | `2.6.1`, `2.4.2` | Atbilst vecumposmam |
| [3.5 Cikli (Loops) un atkārtošanās loģika](datorika9/dat9_35.html) | `2.6.1`, `5.2.1` | Atbilst vecumposmam |
| [3.6 Noslēguma projekts: Radošā teksta spēle JS](datorika9/dat9_36.html) | `2.6.1`, `2.6.2`, `5.2.1`, `5.2.3` | Atbilst vecumposmam |
| [4.1 Funkcijas un koda atkārtota izmantošana](datorika9/dat9_41.html) | `2.6.1`, `1.3.4` | Atbilst vecumposmam |
| [4.2 Notikumu klausītāji (Event Listeners) un interakcija](datorika9/dat9_42.html) | `2.6.1`, `1.3.3` | Atbilst vecumposmam |
| [4.3 DOM manipulācija – dinamiska elementu pārvaldība](datorika9/dat9_43.html) | `2.6.1`, `2.4.7` | Atbilst vecumposmam |
| [4.4 Laika kontrole (Timers) un spēles cikls](datorika9/dat9_44.html) | `2.6.1`, `3.4.3` | Atbilst vecumposmam |
| [4.5 Sadursmju noteikšanas (Collision detection) pamati](datorika9/dat9_45.html) | `2.6.1`, `5.2.1` | Atbilst vecumposmam |
| [4.6 Noslēguma projekts: Spēles dzinēja prototips](datorika9/dat9_46.html) | `2.6.1`, `1.3.4`, `1.4.2`, `5.2.4` | Atbilst vecumposmam |
| [5.1 Projekta specifikācija un laika plānošana](datorika9/dat9_51.html) | `1.3.1`, `1.5.1` | Atbilst vecumposmam |
| [5.2 Vizuālo resursu un saskarnes (UI) pabeigšana](datorika9/dat9_52.html) | `2.4.11`, `1.1.2` | Atbilst vecumposmam |
| [5.3 Spēles pamatloģikas programmēšana](datorika9/dat9_53.html) | `2.6.1`, `2.6.2` | Atbilst vecumposmam |
| [5.4 Papildfunkciju ieviešana (Power-ups, līmeņi, skaņa)](datorika9/dat9_54.html) | `5.2.1`, `2.3.1` | Atbilst vecumposmam |
| [5.5 Spēles testēšana, atkļūdošana un publicēšana](datorika9/dat9_55.html) | `1.3.3`, `1.4.2`, `2.6.1`, `5.2.4` | Atbilst vecumposmam |
| [5.6 Noslēguma projekts: Pilnvērtīga spēle internetā](datorika9/dat9_56.html) | `1.5.1`, `2.4.10`, `2.5.3`, `5.2.3` | Atbilst vecumposmam |

### Robotika 7. klase

| Stunda | SR kodi | Atbilstība |
|---|---|---|
| [1.1 Ievads LEGO SPIKE un robota pamatkustības](robotika/rbtk7_11.html) | `D.7.1.1`, `D.7.2.1` | Atbilst vecumposmam |
| [1.2 Distances sensors un izvairīšanās no šķēršļiem](robotika/rbtk7_12.html) | `D.7.2.1`, `D.7.4.1` | Atbilst vecumposmam |
| [1.3 Krāsu sensors un līniju sekotājs](robotika/rbtk7_13.html) | `D.7.2.1`, `D.7.3.1`, `D.7.4.2` | Atbilst vecumposmam |
| [1.4 Manipulatori (Satvērējs)](robotika/rbtk7_14.html) | `D.7.1.1`, `D.7.4.2`, `D.7.5.1` | Atbilst vecumposmam |
| [1.5 Noslēguma projekts: Pārbaudes misija](robotika/rbtk7_15.html) | `D.7.2.1`, `D.7.3.1`, `D.7.4.2`, `D.7.5.1`, `D.7.6.1` | Atbilst vecumposmam |
| [2.1 Ievads Arduino un Tinkercad](robotika/rbtk7_21.html) | `D.7.1.1`, `D.7.2.1`, `D.7.6.1` | Atbilst vecumposmam |
| [2.2 Pogas un If-Else loģika](robotika/rbtk7_22.html) | `D.7.2.1`, `D.7.3.1`, `D.7.6.1` | Atbilst vecumposmam |
| [2.3 Analogie signāli (Potenciometrs)](robotika/rbtk7_23.html) | `D.7.2.1`, `D.7.4.1`, `D.7.6.1` | Atbilst vecumposmam |
| [2.4 Servo motors](robotika/rbtk7_24.html) | `D.7.1.1`, `D.7.4.2`, `D.7.6.1` | Atbilst vecumposmam |
| [2.5 Noslēguma projekts: Reakcijas spēle](robotika/rbtk7_25.html) | `D.7.1.1`, `D.7.2.1`, `D.7.3.1`, `D.7.6.1` | Atbilst vecumposmam |

### Programmēšana I

| Stunda | SR kodi | Atbilstība |
|---|---|---|
| [1.1 Datora sagatavošana un IDE](programmesana1/prog1_1/prog1_11.html) | `2.4.12`, `3.1.1` | Atbilst vecumposmam |
| [1.2 GitHub un Mākoņkrātuve](programmesana1/prog1_1/prog1_12.html) | `2.4.9`, `2.4.12` | Atbilst vecumposmam |
| [1.3 Koda sinhronizācija (Desktop)](programmesana1/prog1_1/prog1_13.html) | `2.4.9` | Atbilst vecumposmam |
| [1.4 Failu sistēma un organizācija](programmesana1/prog1_1/prog1_14.html) | `2.4.12`, `2.4.9` | Atbilst vecumposmam |
| [1.5 Dokumentēšana, README un Licences](programmesana1/prog1_1/prog1_15.html) | `2.4.6`, `2.4.8` | Atbilst vecumposmam |
| [1.6 Noslēguma pārbaudes darbs — Darba vide un kodu pārvaldība](programmesana1/prog1_1/prog1_16.html) | `2.4.8`, `2.4.9`, `2.4.12`, `3.1.1` | Atbilst vecumposmam |
| [10.1 Ievads datubāzēs un PostgreSQL](programmesana1/prog1_10/prog1_101.html) | `2.4.17`, `2.4.4` | Atbilst vecumposmam |
| [10.2 SQL CRUD: SELECT, INSERT, UPDATE, DELETE](programmesana1/prog1_10/prog1_102.html) | `2.4.17`, `2.4.13` | Atbilst vecumposmam |
| [10.3 Tabulu projektēšana un saites](programmesana1/prog1_10/prog1_103.html) | `2.4.1`, `2.4.6` | Atbilst vecumposmam |
| [10.4 JOIN un sarežģīti vaicājumi](programmesana1/prog1_10/prog1_104.html) | `2.4.4`, `2.4.5` | Atbilst vecumposmam |
| [10.5 Python ↔ PostgreSQL (psycopg2)](programmesana1/prog1_10/prog1_105.html) | `2.4.11`, `3.2.5` | Atbilst vecumposmam |
| [10.6 Noslēguma projekts: Highscore datubāze](programmesana1/prog1_10/prog1_106.html) | `2.4.17`, `2.4.4`, `2.4.5`, `2.4.15` | Atbilst vecumposmam |
| [11.1 Klases un objekti](programmesana1/prog1_11/prog1_111.html) | `2.4.18`, `2.4.15` | Atbilst vecumposmam |
| [11.2 Konstruktori un atribūti](programmesana1/prog1_11/prog1_112.html) | `2.4.18`, `2.4.15` | Atbilst vecumposmam |
| [11.3 Metodes un self](programmesana1/prog1_11/prog1_113.html) | `2.4.18`, `2.4.15` | Atbilst vecumposmam |
| [11.4 Mantošana un super()](programmesana1/prog1_11/prog1_114.html) | `2.4.18`, `2.4.15` | Atbilst vecumposmam |
| [11.5 Polimorfisms un dunder metodes](programmesana1/prog1_11/prog1_115.html) | `2.4.18`, `2.4.11` | Atbilst vecumposmam |
| [11.6 Noslēguma projekts: Klases turnīra simulators](programmesana1/prog1_11/prog1_116.html) | `2.4.18`, `2.4.15`, `2.4.14` | Atbilst vecumposmam |
| [12.1 Front-end un back-end arhitektūra](programmesana1/prog1_12/prog1_121.html) | `2.4.1`, `2.4.7` | Atbilst vecumposmam |
| [12.2 Flask: Python kā web serveris](programmesana1/prog1_12/prog1_122.html) | `2.4.11`, `2.4.15` | Atbilst vecumposmam |
| [12.3 REST API izstrāde](programmesana1/prog1_12/prog1_123.html) | `2.4.11`, `2.4.7` | Atbilst vecumposmam |
| [12.4 Front-end + API integrācija](programmesana1/prog1_12/prog1_124.html) | `2.4.7`, `2.4.11` | Atbilst vecumposmam |
| [12.5 Izvietošana mākonī un drošība](programmesana1/prog1_12/prog1_125.html) | `2.4.6`, `3.1.1`, `3.2.5` | Atbilst vecumposmam |
| [12.6 Noslēguma projekts: Daudzspēlētāju Krustiņi un nullītes](programmesana1/prog1_12/prog1_126.html) | `2.4.1`, `2.4.7`, `2.4.11`, `2.4.18`, `2.4.17` | Atbilst vecumposmam |
| [2.1 Ievade un datu tipi](programmesana1/prog1_2/prog1_21.html) | `2.4.13` | Atbilst vecumposmam |
| [2.2 Interaktivitāte un konvertācija](programmesana1/prog1_2/prog1_22.html) | `2.4.13` | Atbilst vecumposmam |
| [2.3 Matemātika un f-strings](programmesana1/prog1_2/prog1_23.html) | `2.4.13` | Atbilst vecumposmam |
| [2.4 Koda stils un komentāri](programmesana1/prog1_2/prog1_24.html) | `2.4.8` | Atbilst vecumposmam |
| [2.5 Spēles plānošana](programmesana1/prog1_2/prog1_25.html) | `2.4.1`, `2.4.6` | Atbilst vecumposmam |
| [2.6 Noslēguma projekts: "Lielais skaitļu duelītis"](programmesana1/prog1_2/prog1_26.html) | `2.4.8`, `2.4.9`, `2.4.13`, `3.1.1` | Atbilst vecumposmam |
| [3.1 Zarošanās un operatori](programmesana1/prog1_3/prog1_31.html) | `2.4.14` | Atbilst vecumposmam |
| [3.2 Loģiskie operatori](programmesana1/prog1_3/prog1_32.html) | `2.4.13`, `2.4.14` | Atbilst vecumposmam |
| [3.3 While cikli un kontrole](programmesana1/prog1_3/prog1_33.html) | `2.4.14` | Atbilst vecumposmam |
| [3.4 Kļūdu apstrāde un validācija](programmesana1/prog1_3/prog1_34.html) | `2.4.10`, `2.4.13` | Atbilst vecumposmam |
| [3.5 Saraksti un For cikli](programmesana1/prog1_3/prog1_35.html) | `2.4.16`, `2.4.14` | Atbilst vecumposmam |
| [3.6 Noslēguma projekts: "Gudrais Akmens-Šķēres-Papīrīts"](programmesana1/prog1_3/prog1_36.html) | `2.4.10`, `2.4.13`, `2.4.14`, `2.4.16` | Atbilst vecumposmam |
| [4.1 Funkciju definēšana un parametri](programmesana1/prog1_4/prog1_41.html) | `2.4.15` | Atbilst vecumposmam |
| [4.2 Vērtību atgriešana (return)](programmesana1/prog1_4/prog1_42.html) | `2.4.15` | Atbilst vecumposmam |
| [4.3 Modularitāte un koda sadalīšana](programmesana1/prog1_4/prog1_43.html) | `2.4.15`, `2.4.6` | Atbilst vecumposmam |
| [4.4 Lokālie/globālie mainīgie un vārdnīcas](programmesana1/prog1_4/prog1_44.html) | `2.4.13`, `2.4.16` | Atbilst vecumposmam |
| [4.5 Spēles plānošana ar shēmām](programmesana1/prog1_4/prog1_45.html) | `2.4.1`, `2.4.6` | Atbilst vecumposmam |
| [4.6 Noslēguma projekts: Skaitļu minētājs](programmesana1/prog1_4/prog1_46.html) | `2.4.15`, `2.4.14`, `2.4.13`, `2.4.10` | Atbilst vecumposmam |
| [5.1 Saraksti](programmesana1/prog1_5/prog1_51.html) | `2.4.14` | Atbilst vecumposmam |
| [5.2 Vārdnīcas](programmesana1/prog1_5/prog1_52.html) | `2.4.14` | Atbilst vecumposmam |
| [5.3 For cikli](programmesana1/prog1_5/prog1_53.html) | `2.4.14` | Atbilst vecumposmam |
| [5.4 Aptaujas izveide](programmesana1/prog1_5/prog1_54.html) | `2.3.4`, `2.3.2` | Atbilst vecumposmam |
| [5.5 Analīze un integrācija](programmesana1/prog1_5/prog1_55.html) | `2.3.4`, `2.4.14` | Atbilst vecumposmam |
| [5.6 Noslēguma projekts: Atmiņu kāršu spēle](programmesana1/prog1_5/prog1_56.html) | `2.4.16`, `2.4.14`, `2.4.15` | Atbilst vecumposmam |
| [6.1 Failu I/O](programmesana1/prog1_6/prog1_61.html) | `2.4.14` | Atbilst vecumposmam |
| [6.2 Digitālais rīks](programmesana1/prog1_6/prog1_62.html) | `2.3.5`, `2.4.1` | Atbilst vecumposmam |
| [6.3 Datu transformācija](programmesana1/prog1_6/prog1_63.html) | `2.4.14` | Atbilst vecumposmam |
| [6.4 Rezultātu tabulas](programmesana1/prog1_6/prog1_64.html) | `2.4.14` | Atbilst vecumposmam |
| [6.5 Analīze un Vizualizācija](programmesana1/prog1_6/prog1_65.html) | `2.3.6` | Atbilst vecumposmam |
| [6.6 Noslēguma projekts: Quiz spēle ar Highscore](programmesana1/prog1_6/prog1_66.html) | `2.4.17`, `2.4.4`, `2.4.5` | Atbilst vecumposmam |
| [7.1 Meklēšanas pamati](programmesana1/prog1_7/prog1_71.html) | `2.4.19` | Atbilst vecumposmam |
| [7.2 Kārtošanas loģika](programmesana1/prog1_7/prog1_72.html) | `2.4.19` | Atbilst vecumposmam |
| [7.3 Big O un Sarežģītība](programmesana1/prog1_7/prog1_73.html) | `2.4.16` | Atbilst vecumposmam |
| [7.4 Iebūvēto funkciju ātrums](programmesana1/prog1_7/prog1_74.html) | `2.4.19`, `2.4.16` | Atbilst vecumposmam |
| [7.5 Iebūvēto funkciju efektivitāte](programmesana1/prog1_7/prog1_75.html) | `2.4.19`, `2.4.16` | Atbilst vecumposmam |
| [7.6 Noslēguma projekts: "Koda lauzējs: AI Efektivitāte"](programmesana1/prog1_7/prog1_76.html) | `2.4.10`, `2.4.13`, `2.4.16`, `2.4.19` | Atbilst vecumposmam |
| [8.1 Problēmas formulēšana un automatizācija](programmesana1/prog1_8/prog1_81.html) | `2.4.1` | Atbilst vecumposmam |
| [8.2 Prasību specifikācija — Lietotāju stāsti](programmesana1/prog1_8/prog1_82.html) | `2.4.4` | Atbilst vecumposmam |
| [8.3 Datu modelis un UI plūsma](programmesana1/prog1_8/prog1_83.html) | `2.4.5` | Atbilst vecumposmam |
| [8.4 Prezentācijas māksla — Pitch sagatavošana](programmesana1/prog1_8/prog1_84.html) | `2.3.10` | Atbilst vecumposmam |
| [8.5 Sasniedzamie rezultāti un resursu plānošana](programmesana1/prog1_8/prog1_85.html) | `2.4.5`, `2.4.1` | Atbilst vecumposmam |
| [8.6 Noslēguma projekts: Projektējuma aizstāvēšana](programmesana1/prog1_8/prog1_86.html) | `2.4.6`, `2.4.7`, `2.4.1` | Atbilst vecumposmam |
| [9.1 Ārējās bibliotēkas un instalēšana](programmesana1/prog1_9/prog1_91.html) | `2.4.11`, `2.4.12` | Atbilst vecumposmam |
| [9.2 Atvērtā koda licences un dokumentācija](programmesana1/prog1_9/prog1_92.html) | `3.1.3`, `2.4.11` | Atbilst vecumposmam |
| [9.3 Python pārvēršana tīmekļa saskarnē](programmesana1/prog1_9/prog1_93.html) | `2.4.7`, `2.4.11` | Atbilst vecumposmam |
| [9.4 HTML un Python sasaiste](programmesana1/prog1_9/prog1_94.html) | `2.4.7`, `2.4.11` | Atbilst vecumposmam |
| [9.5 Interaktivitāte pārlūkprogrammā](programmesana1/prog1_9/prog1_95.html) | `2.4.7`, `2.4.14` | Atbilst vecumposmam |
| [9.6 Noslēguma projekts: "Krustiņi un nullītes" pārlūkā](programmesana1/prog1_9/prog1_96.html) | `2.4.1`, `2.4.7`, `2.4.18`, `2.4.11` | Atbilst vecumposmam |

### Programmēšana II

| Stunda | SR kodi | Atbilstība |
|---|---|---|
| [1.1 Godot instalācija un projekta sagatavošana](programmesana2/prog2_1/prog2_11.html) | `2.4.12`, `3.1.2` | Atbilst vecumposmam |
| [1.2 Scene Tree un Node sistēma](programmesana2/prog2_1/prog2_12.html) | `2.4.13`, `2.4.15` | Atbilst vecumposmam |
| [1.3 C++ un GDExtension sagatavošana](programmesana2/prog2_1/prog2_13.html) | `2.4.12`, `2.4.2` | Atbilst vecumposmam |
| [1.4 Pirmais C++ skripts: mainīgie un izvade](programmesana2/prog2_1/prog2_14.html) | `2.4.13`, `2.4.15` | Atbilst vecumposmam |
| [1.5 Spēles laukuma izveide](programmesana2/prog2_1/prog2_15.html) | `2.4.7`, `2.4.13` | Atbilst vecumposmam |
| [1.6 Noslēguma projekts: Pong](programmesana2/prog2_1/prog2_16.html) | `2.4.1`, `2.4.7`, `2.4.15` | Atbilst vecumposmam |
| [2.1 Process un fizikas cikli](programmesana2/prog2_2/prog2_21.html) | `2.4.14`, `2.4.15` | Atbilst vecumposmam |
| [2.2 Input apstrāde un Input Map](programmesana2/prog2_2/prog2_22.html) | `2.4.14`, `2.4.7` | Atbilst vecumposmam |
| [2.3 Vadības struktūras spēles loģikā](programmesana2/prog2_2/prog2_23.html) | `2.4.14`, `2.4.13` | Atbilst vecumposmam |
| [2.4 Sadursmju noteikšana](programmesana2/prog2_2/prog2_24.html) | `2.4.14`, `2.4.7` | Atbilst vecumposmam |
| [2.5 Gravitācija un platformas mehānika](programmesana2/prog2_2/prog2_25.html) | `2.4.14`, `2.4.13` | Atbilst vecumposmam |
| [2.6 Noslēguma projekts: Platformas spēle](programmesana2/prog2_2/prog2_26.html) | `2.4.1`, `2.4.7`, `2.4.14`, `2.4.15` | Atbilst vecumposmam |
| [3.1 C++ klases pamati](programmesana2/prog2_3/prog2_31.html) | `2.4.18`, `2.4.15` | Atbilst vecumposmam |
| [3.2 Mantošana C++ un Godot](programmesana2/prog2_3/prog2_32.html) | `2.4.18`, `2.4.15` | Atbilst vecumposmam |
| [3.3 Signāli un objektu komunikācija](programmesana2/prog2_3/prog2_33.html) | `2.4.15`, `2.4.18` | Atbilst vecumposmam |
| [3.4 Custom GDExtension klases editor redzamas](programmesana2/prog2_3/prog2_34.html) | `2.4.7`, `2.4.18` | Atbilst vecumposmam |
| [3.5 Statistikas sistēma un struct](programmesana2/prog2_3/prog2_35.html) | `2.4.16`, `2.4.18` | Atbilst vecumposmam |
| [3.6 Noslēguma projekts: Klases turnīra simulators](programmesana2/prog2_3/prog2_36.html) | `2.4.1`, `2.4.7`, `2.4.15`, `2.4.18` | Atbilst vecumposmam |
| [4.1 Vector un Array](programmesana2/prog2_4/prog2_41.html) | `2.4.16`, `2.4.13` | Atbilst vecumposmam |
| [4.2 Map un Dictionary](programmesana2/prog2_4/prog2_42.html) | `2.4.16`, `2.4.4` | Atbilst vecumposmam |
| [4.3 State machines AI uzvedībai](programmesana2/prog2_4/prog2_43.html) | `2.4.18`, `2.4.19` | Atbilst vecumposmam |
| [4.4 Pathfinding ar A*](programmesana2/prog2_4/prog2_44.html) | `2.4.19`, `2.4.16` | Atbilst vecumposmam |
| [4.5 Šaušanas mehānika un object pooling](programmesana2/prog2_4/prog2_45.html) | `2.4.19`, `2.4.16` | Atbilst vecumposmam |
| [4.6 Noslēguma projekts: Top-down šautene](programmesana2/prog2_4/prog2_46.html) | `2.4.1`, `2.4.16`, `2.4.18`, `2.4.19` | Atbilst vecumposmam |
| [5.1 Failu I/O Godot vidē](programmesana2/prog2_5/prog2_51.html) | `2.4.17`, `2.4.4` | Atbilst vecumposmam |
| [5.2 JSON serializācija un Resource sistēma](programmesana2/prog2_5/prog2_52.html) | `2.4.17`, `2.4.16` | Atbilst vecumposmam |
| [5.3 Save/Load arhitektūra](programmesana2/prog2_5/prog2_53.html) | `2.4.17`, `2.4.6` | Atbilst vecumposmam |
| [5.4 Procedural generation](programmesana2/prog2_5/prog2_54.html) | `2.4.19`, `2.4.16` | Atbilst vecumposmam |
| [5.5 Algoritmu efektivitāte](programmesana2/prog2_5/prog2_55.html) | `2.4.19` | Atbilst vecumposmam |
| [5.6 Noslēguma projekts: Procedurālais klases labirints](programmesana2/prog2_5/prog2_56.html) | `2.4.1`, `2.4.16`, `2.4.17`, `2.4.19` | Atbilst vecumposmam |
| [6.1 UI elementi un Control nodes](programmesana2/prog2_6/prog2_61.html) | `2.4.7`, `2.4.15` | Atbilst vecumposmam |
| [6.2 Animācijas un Tween](programmesana2/prog2_6/prog2_62.html) | `2.4.7`, `2.4.15` | Atbilst vecumposmam |
| [6.3 Audio sistēma](programmesana2/prog2_6/prog2_63.html) | `2.4.7`, `2.4.15` | Atbilst vecumposmam |
| [6.4 Atkļūdošana un profilēšana](programmesana2/prog2_6/prog2_64.html) | `2.4.10`, `2.4.19` | Atbilst vecumposmam |
| [6.5 Eksports un publicēšana](programmesana2/prog2_6/prog2_65.html) | `2.4.6`, `3.1.4` | Atbilst vecumposmam |
| [6.6 Noslēguma projekts: Puzzle spēle](programmesana2/prog2_6/prog2_66.html) | `2.4.1`, `2.4.7`, `2.4.6`, `3.1.4` | Atbilst vecumposmam |

## Pilnā SR pārklājuma matrica

### Datorika 9. klase

| SR | Statuss | Piesaistītās stundas |
|---|---|---|
| `1.1.1` | Nosegts | [1.3 Dizaina pētniecība un tirgus analīze](datorika9/dat9_13.html), [2.1 CSS pamati un vizuālā ergonomika](datorika9/dat9_21.html), [2.2 Izkārtojuma kontrole un "Box Model"](datorika9/dat9_22.html) |
| `1.1.2` | Nosegts | [1.5 UX/UI pamati un spēles prototipēšana](datorika9/dat9_15.html), [5.2 Vizuālo resursu un saskarnes (UI) pabeigšana](datorika9/dat9_52.html) |
| `1.1.3` | Nav piesaistīts | Ieteikums: [dat9_15](datorika9/dat9_15.html), [dat9_16](datorika9/dat9_16.html), [dat9_55](datorika9/dat9_55.html) |
| `1.2.1` | Nosegts | [1.4 Spēles koncepcija un mērķauditorija](datorika9/dat9_14.html) |
| `1.2.2` | Nosegts | [1.4 Spēles koncepcija un mērķauditorija](datorika9/dat9_14.html) |
| `1.2.3` | Nosegts | [1.3 Dizaina pētniecība un tirgus analīze](datorika9/dat9_13.html) |
| `1.3.1` | Nosegts | [1.6 Noslēguma projekts: Spēles projekta pieteikums](datorika9/dat9_16.html), [5.1 Projekta specifikācija un laika plānošana](datorika9/dat9_51.html) |
| `1.3.2` | Nosegts | [1.5 UX/UI pamati un spēles prototipēšana](datorika9/dat9_15.html) |
| `1.3.3` | Nosegts | [4.2 Notikumu klausītāji (Event Listeners) un interakcija](datorika9/dat9_42.html), [5.5 Spēles testēšana, atkļūdošana un publicēšana](datorika9/dat9_55.html) |
| `1.3.4` | Nosegts | [4.1 Funkcijas un koda atkārtota izmantošana](datorika9/dat9_41.html), [4.6 Noslēguma projekts: Spēles dzinēja prototips](datorika9/dat9_46.html) |
| `1.4.1` | Nosegts | [2.6 Noslēguma projekts: Stilizēta spēles lapa](datorika9/dat9_26.html) |
| `1.4.2` | Nosegts | [4.6 Noslēguma projekts: Spēles dzinēja prototips](datorika9/dat9_46.html), [5.5 Spēles testēšana, atkļūdošana un publicēšana](datorika9/dat9_55.html) |
| `1.4.3` | Nav piesaistīts | Ieteikums: [dat9_55](datorika9/dat9_55.html), [dat9_56](datorika9/dat9_56.html) |
| `1.5.1` | Nosegts | [1.6 Noslēguma projekts: Spēles projekta pieteikums](datorika9/dat9_16.html), [5.1 Projekta specifikācija un laika plānošana](datorika9/dat9_51.html), [5.6 Noslēguma projekts: Pilnvērtīga spēle internetā](datorika9/dat9_56.html) |
| `3.4.3` | Nosegts | [4.4 Laika kontrole (Timers) un spēles cikls](datorika9/dat9_44.html) |
| `3.4.4` | Nav piesaistīts | Ieteikums: [dat9_13](datorika9/dat9_13.html), [dat9_54](datorika9/dat9_54.html) |
| `2.3.1` | Nosegts | [1.1 Izstrādes vide un GitHub integrācija](datorika9/dat9_11.html), [5.4 Papildfunkciju ieviešana (Power-ups, līmeņi, skaņa)](datorika9/dat9_54.html) |
| `2.3.2` | Nav piesaistīts | Ieteikums: [dat9_11](datorika9/dat9_11.html), [dat9_56](datorika9/dat9_56.html) |
| `2.3.3` | Nosegts | [1.2 HTML skelets un satura strukturēšana](datorika9/dat9_12.html), [2.5 Datņu sistēmas organizēšana un arhīvi](datorika9/dat9_25.html) |
| `2.4.1` | Nosegts | [2.2 Izkārtojuma kontrole un "Box Model"](datorika9/dat9_22.html) |
| `2.4.2` | Nosegts | [3.4 Masīvi (Arrays) un datu strukturēšana](datorika9/dat9_34.html) |
| `2.4.3` | Nav piesaistīts | Ieteikums: [dat9_34](datorika9/dat9_34.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.4` | Nav piesaistīts | Ieteikums: [dat9_16](datorika9/dat9_16.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.5` | Nosegts | [2.6 Noslēguma projekts: Stilizēta spēles lapa](datorika9/dat9_26.html) |
| `2.4.6` | Nosegts | [2.3 Grafisko resursu sagatavošana un optimizācija](datorika9/dat9_23.html), [2.4 Audio materiālu apstrāde un integrācija](datorika9/dat9_24.html), [2.6 Noslēguma projekts: Stilizēta spēles lapa](datorika9/dat9_26.html) |
| `2.4.7` | Nosegts | [2.3 Grafisko resursu sagatavošana un optimizācija](datorika9/dat9_23.html), [4.3 DOM manipulācija – dinamiska elementu pārvaldība](datorika9/dat9_43.html) |
| `2.4.8` | Nav piesaistīts | Ieteikums: [dat9_26](datorika9/dat9_26.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.9` | Nav piesaistīts | Ieteikums: [dat9_22](datorika9/dat9_22.html), [dat9_24](datorika9/dat9_24.html) |
| `2.4.10` | Nosegts | [2.4 Audio materiālu apstrāde un integrācija](datorika9/dat9_24.html), [2.6 Noslēguma projekts: Stilizēta spēles lapa](datorika9/dat9_26.html), [5.6 Noslēguma projekts: Pilnvērtīga spēle internetā](datorika9/dat9_56.html) |
| `2.4.11` | Nosegts | [5.2 Vizuālo resursu un saskarnes (UI) pabeigšana](datorika9/dat9_52.html) |
| `2.5.1` | Nav piesaistīts | Ieteikums: [dat9_56](datorika9/dat9_56.html) |
| `2.5.2` | Nav piesaistīts | Ieteikums: [dat9_11](datorika9/dat9_11.html), [dat9_56](datorika9/dat9_56.html) |
| `2.5.3` | Nosegts | [2.1 CSS pamati un vizuālā ergonomika](datorika9/dat9_21.html), [5.6 Noslēguma projekts: Pilnvērtīga spēle internetā](datorika9/dat9_56.html) |
| `2.5.4` | Nav piesaistīts | Ieteikums: [dat9_13](datorika9/dat9_13.html), [dat9_56](datorika9/dat9_56.html) |
| `2.6.1` | Nosegts | [1.2 HTML skelets un satura strukturēšana](datorika9/dat9_12.html), [1.6 Noslēguma projekts: Spēles projekta pieteikums](datorika9/dat9_16.html), [3.1 Ievads JavaScript un mainīgie](datorika9/dat9_31.html), [3.2 Datu tipi un interaktivitāte (Input/Output)](datorika9/dat9_32.html), [3.3 Loģiskie operatori un sazarojumi (If/Else)](datorika9/dat9_33.html), [3.4 Masīvi (Arrays) un datu strukturēšana](datorika9/dat9_34.html), [3.5 Cikli (Loops) un atkārtošanās loģika](datorika9/dat9_35.html), [3.6 Noslēguma projekts: Radošā teksta spēle JS](datorika9/dat9_36.html), [4.1 Funkcijas un koda atkārtota izmantošana](datorika9/dat9_41.html), [4.2 Notikumu klausītāji (Event Listeners) un interakcija](datorika9/dat9_42.html), [4.3 DOM manipulācija – dinamiska elementu pārvaldība](datorika9/dat9_43.html), [4.4 Laika kontrole (Timers) un spēles cikls](datorika9/dat9_44.html), [4.5 Sadursmju noteikšanas (Collision detection) pamati](datorika9/dat9_45.html), [4.6 Noslēguma projekts: Spēles dzinēja prototips](datorika9/dat9_46.html), [5.3 Spēles pamatloģikas programmēšana](datorika9/dat9_53.html), [5.5 Spēles testēšana, atkļūdošana un publicēšana](datorika9/dat9_55.html) |
| `2.6.2` | Nosegts | [3.6 Noslēguma projekts: Radošā teksta spēle JS](datorika9/dat9_36.html), [5.3 Spēles pamatloģikas programmēšana](datorika9/dat9_53.html) |
| `2.6.3` | Nav piesaistīts | Ieteikums: [rbtk7_21](robotika/rbtk7_21.html), [rbtk7_25](robotika/rbtk7_25.html), [dat9_46](datorika9/dat9_46.html) |

### Robotika 7. klase

| SR | Statuss | Piesaistītās stundas |
|---|---|---|
| `D.7.1.1` | Nosegts | [1.1 Ievads LEGO SPIKE un robota pamatkustības](robotika/rbtk7_11.html), [1.4 Manipulatori (Satvērējs)](robotika/rbtk7_14.html), [2.1 Ievads Arduino un Tinkercad](robotika/rbtk7_21.html), [2.4 Servo motors](robotika/rbtk7_24.html), [2.5 Noslēguma projekts: Reakcijas spēle](robotika/rbtk7_25.html) |
| `D.7.2.1` | Nosegts | [1.1 Ievads LEGO SPIKE un robota pamatkustības](robotika/rbtk7_11.html), [1.2 Distances sensors un izvairīšanās no šķēršļiem](robotika/rbtk7_12.html), [1.3 Krāsu sensors un līniju sekotājs](robotika/rbtk7_13.html), [1.5 Noslēguma projekts: Pārbaudes misija](robotika/rbtk7_15.html), [2.1 Ievads Arduino un Tinkercad](robotika/rbtk7_21.html), [2.2 Pogas un If-Else loģika](robotika/rbtk7_22.html), [2.3 Analogie signāli (Potenciometrs)](robotika/rbtk7_23.html), [2.5 Noslēguma projekts: Reakcijas spēle](robotika/rbtk7_25.html) |
| `D.7.3.1` | Nosegts | [1.3 Krāsu sensors un līniju sekotājs](robotika/rbtk7_13.html), [1.5 Noslēguma projekts: Pārbaudes misija](robotika/rbtk7_15.html), [2.2 Pogas un If-Else loģika](robotika/rbtk7_22.html), [2.5 Noslēguma projekts: Reakcijas spēle](robotika/rbtk7_25.html) |
| `D.7.4.1` | Nosegts | [1.2 Distances sensors un izvairīšanās no šķēršļiem](robotika/rbtk7_12.html), [2.3 Analogie signāli (Potenciometrs)](robotika/rbtk7_23.html) |
| `D.7.4.2` | Nosegts | [1.3 Krāsu sensors un līniju sekotājs](robotika/rbtk7_13.html), [1.4 Manipulatori (Satvērējs)](robotika/rbtk7_14.html), [1.5 Noslēguma projekts: Pārbaudes misija](robotika/rbtk7_15.html), [2.4 Servo motors](robotika/rbtk7_24.html) |
| `D.7.5.1` | Nosegts | [1.4 Manipulatori (Satvērējs)](robotika/rbtk7_14.html), [1.5 Noslēguma projekts: Pārbaudes misija](robotika/rbtk7_15.html) |
| `D.7.6.1` | Nosegts | [1.5 Noslēguma projekts: Pārbaudes misija](robotika/rbtk7_15.html), [2.1 Ievads Arduino un Tinkercad](robotika/rbtk7_21.html), [2.2 Pogas un If-Else loģika](robotika/rbtk7_22.html), [2.3 Analogie signāli (Potenciometrs)](robotika/rbtk7_23.html), [2.4 Servo motors](robotika/rbtk7_24.html), [2.5 Noslēguma projekts: Reakcijas spēle](robotika/rbtk7_25.html) |

### Programmēšana I

| SR | Statuss | Piesaistītās stundas |
|---|---|---|
| `2.3.1` | Nav piesaistīts | Ieteikums: [prog1_11](programmesana1/prog1_1/prog1_11.html), [prog1_62](programmesana1/prog1_6/prog1_62.html) |
| `2.3.2` | Nosegts | [5.4 Aptaujas izveide](programmesana1/prog1_5/prog1_54.html) |
| `2.3.3` | Nav piesaistīts | Ieteikums: [prog1_92](programmesana1/prog1_9/prog1_92.html), [prog1_125](programmesana1/prog1_12/prog1_125.html) |
| `2.3.4` | Nosegts | [5.4 Aptaujas izveide](programmesana1/prog1_5/prog1_54.html), [5.5 Analīze un integrācija](programmesana1/prog1_5/prog1_55.html) |
| `2.3.5` | Nosegts | [6.2 Digitālais rīks](programmesana1/prog1_6/prog1_62.html) |
| `2.3.6` | Nosegts | [6.5 Analīze un Vizualizācija](programmesana1/prog1_6/prog1_65.html) |
| `2.3.10` | Nosegts | [8.4 Prezentācijas māksla — Pitch sagatavošana](programmesana1/prog1_8/prog1_84.html) |
| `2.4.1` | Nosegts | [10.3 Tabulu projektēšana un saites](programmesana1/prog1_10/prog1_103.html), [12.1 Front-end un back-end arhitektūra](programmesana1/prog1_12/prog1_121.html), [12.6 Noslēguma projekts: Daudzspēlētāju Krustiņi un nullītes](programmesana1/prog1_12/prog1_126.html), [2.5 Spēles plānošana](programmesana1/prog1_2/prog1_25.html), [4.5 Spēles plānošana ar shēmām](programmesana1/prog1_4/prog1_45.html), [6.2 Digitālais rīks](programmesana1/prog1_6/prog1_62.html), [8.1 Problēmas formulēšana un automatizācija](programmesana1/prog1_8/prog1_81.html), [8.5 Sasniedzamie rezultāti un resursu plānošana](programmesana1/prog1_8/prog1_85.html), [8.6 Noslēguma projekts: Projektējuma aizstāvēšana](programmesana1/prog1_8/prog1_86.html), [9.6 Noslēguma projekts: "Krustiņi un nullītes" pārlūkā](programmesana1/prog1_9/prog1_96.html) |
| `2.4.2` | Nav piesaistīts | Ieteikums: [prog1_91](programmesana1/prog1_9/prog1_91.html), [prog1_122](programmesana1/prog1_12/prog1_122.html) |
| `2.4.3` | Nav piesaistīts | Ieteikums: [prog1_86](programmesana1/prog1_8/prog1_86.html), [prog1_126](programmesana1/prog1_12/prog1_126.html) |
| `2.4.4` | Nosegts | [10.1 Ievads datubāzēs un PostgreSQL](programmesana1/prog1_10/prog1_101.html), [10.4 JOIN un sarežģīti vaicājumi](programmesana1/prog1_10/prog1_104.html), [10.6 Noslēguma projekts: Highscore datubāze](programmesana1/prog1_10/prog1_106.html), [6.6 Noslēguma projekts: Quiz spēle ar Highscore](programmesana1/prog1_6/prog1_66.html), [8.2 Prasību specifikācija — Lietotāju stāsti](programmesana1/prog1_8/prog1_82.html) |
| `2.4.5` | Nosegts | [10.4 JOIN un sarežģīti vaicājumi](programmesana1/prog1_10/prog1_104.html), [10.6 Noslēguma projekts: Highscore datubāze](programmesana1/prog1_10/prog1_106.html), [6.6 Noslēguma projekts: Quiz spēle ar Highscore](programmesana1/prog1_6/prog1_66.html), [8.3 Datu modelis un UI plūsma](programmesana1/prog1_8/prog1_83.html), [8.5 Sasniedzamie rezultāti un resursu plānošana](programmesana1/prog1_8/prog1_85.html) |
| `2.4.6` | Nosegts | [1.5 Dokumentēšana, README un Licences](programmesana1/prog1_1/prog1_15.html), [10.3 Tabulu projektēšana un saites](programmesana1/prog1_10/prog1_103.html), [12.5 Izvietošana mākonī un drošība](programmesana1/prog1_12/prog1_125.html), [2.5 Spēles plānošana](programmesana1/prog1_2/prog1_25.html), [4.3 Modularitāte un koda sadalīšana](programmesana1/prog1_4/prog1_43.html), [4.5 Spēles plānošana ar shēmām](programmesana1/prog1_4/prog1_45.html), [8.6 Noslēguma projekts: Projektējuma aizstāvēšana](programmesana1/prog1_8/prog1_86.html) |
| `2.4.7` | Nosegts | [12.1 Front-end un back-end arhitektūra](programmesana1/prog1_12/prog1_121.html), [12.3 REST API izstrāde](programmesana1/prog1_12/prog1_123.html), [12.4 Front-end + API integrācija](programmesana1/prog1_12/prog1_124.html), [12.6 Noslēguma projekts: Daudzspēlētāju Krustiņi un nullītes](programmesana1/prog1_12/prog1_126.html), [8.6 Noslēguma projekts: Projektējuma aizstāvēšana](programmesana1/prog1_8/prog1_86.html), [9.3 Python pārvēršana tīmekļa saskarnē](programmesana1/prog1_9/prog1_93.html), [9.4 HTML un Python sasaiste](programmesana1/prog1_9/prog1_94.html), [9.5 Interaktivitāte pārlūkprogrammā](programmesana1/prog1_9/prog1_95.html), [9.6 Noslēguma projekts: "Krustiņi un nullītes" pārlūkā](programmesana1/prog1_9/prog1_96.html) |
| `2.4.8` | Nosegts | [1.5 Dokumentēšana, README un Licences](programmesana1/prog1_1/prog1_15.html), [1.6 Noslēguma pārbaudes darbs — Darba vide un kodu pārvaldība](programmesana1/prog1_1/prog1_16.html), [2.4 Koda stils un komentāri](programmesana1/prog1_2/prog1_24.html), [2.6 Noslēguma projekts: "Lielais skaitļu duelītis"](programmesana1/prog1_2/prog1_26.html) |
| `2.4.9` | Nosegts | [1.2 GitHub un Mākoņkrātuve](programmesana1/prog1_1/prog1_12.html), [1.3 Koda sinhronizācija (Desktop)](programmesana1/prog1_1/prog1_13.html), [1.4 Failu sistēma un organizācija](programmesana1/prog1_1/prog1_14.html), [1.6 Noslēguma pārbaudes darbs — Darba vide un kodu pārvaldība](programmesana1/prog1_1/prog1_16.html), [2.6 Noslēguma projekts: "Lielais skaitļu duelītis"](programmesana1/prog1_2/prog1_26.html) |
| `2.4.10` | Nosegts | [3.4 Kļūdu apstrāde un validācija](programmesana1/prog1_3/prog1_34.html), [3.6 Noslēguma projekts: "Gudrais Akmens-Šķēres-Papīrīts"](programmesana1/prog1_3/prog1_36.html), [4.6 Noslēguma projekts: Skaitļu minētājs](programmesana1/prog1_4/prog1_46.html), [7.6 Noslēguma projekts: "Koda lauzējs: AI Efektivitāte"](programmesana1/prog1_7/prog1_76.html) |
| `2.4.11` | Nosegts | [10.5 Python ↔ PostgreSQL (psycopg2)](programmesana1/prog1_10/prog1_105.html), [11.5 Polimorfisms un dunder metodes](programmesana1/prog1_11/prog1_115.html), [12.2 Flask: Python kā web serveris](programmesana1/prog1_12/prog1_122.html), [12.3 REST API izstrāde](programmesana1/prog1_12/prog1_123.html), [12.4 Front-end + API integrācija](programmesana1/prog1_12/prog1_124.html), [12.6 Noslēguma projekts: Daudzspēlētāju Krustiņi un nullītes](programmesana1/prog1_12/prog1_126.html), [9.1 Ārējās bibliotēkas un instalēšana](programmesana1/prog1_9/prog1_91.html), [9.2 Atvērtā koda licences un dokumentācija](programmesana1/prog1_9/prog1_92.html), [9.3 Python pārvēršana tīmekļa saskarnē](programmesana1/prog1_9/prog1_93.html), [9.4 HTML un Python sasaiste](programmesana1/prog1_9/prog1_94.html), [9.6 Noslēguma projekts: "Krustiņi un nullītes" pārlūkā](programmesana1/prog1_9/prog1_96.html) |
| `2.4.12` | Nosegts | [1.1 Datora sagatavošana un IDE](programmesana1/prog1_1/prog1_11.html), [1.2 GitHub un Mākoņkrātuve](programmesana1/prog1_1/prog1_12.html), [1.4 Failu sistēma un organizācija](programmesana1/prog1_1/prog1_14.html), [1.6 Noslēguma pārbaudes darbs — Darba vide un kodu pārvaldība](programmesana1/prog1_1/prog1_16.html), [9.1 Ārējās bibliotēkas un instalēšana](programmesana1/prog1_9/prog1_91.html) |
| `2.4.13` | Nosegts | [10.2 SQL CRUD: SELECT, INSERT, UPDATE, DELETE](programmesana1/prog1_10/prog1_102.html), [2.1 Ievade un datu tipi](programmesana1/prog1_2/prog1_21.html), [2.2 Interaktivitāte un konvertācija](programmesana1/prog1_2/prog1_22.html), [2.3 Matemātika un f-strings](programmesana1/prog1_2/prog1_23.html), [2.6 Noslēguma projekts: "Lielais skaitļu duelītis"](programmesana1/prog1_2/prog1_26.html), [3.2 Loģiskie operatori](programmesana1/prog1_3/prog1_32.html), [3.4 Kļūdu apstrāde un validācija](programmesana1/prog1_3/prog1_34.html), [3.6 Noslēguma projekts: "Gudrais Akmens-Šķēres-Papīrīts"](programmesana1/prog1_3/prog1_36.html), [4.4 Lokālie/globālie mainīgie un vārdnīcas](programmesana1/prog1_4/prog1_44.html), [4.6 Noslēguma projekts: Skaitļu minētājs](programmesana1/prog1_4/prog1_46.html), [7.6 Noslēguma projekts: "Koda lauzējs: AI Efektivitāte"](programmesana1/prog1_7/prog1_76.html) |
| `2.4.14` | Nosegts | [11.6 Noslēguma projekts: Klases turnīra simulators](programmesana1/prog1_11/prog1_116.html), [3.1 Zarošanās un operatori](programmesana1/prog1_3/prog1_31.html), [3.2 Loģiskie operatori](programmesana1/prog1_3/prog1_32.html), [3.3 While cikli un kontrole](programmesana1/prog1_3/prog1_33.html), [3.5 Saraksti un For cikli](programmesana1/prog1_3/prog1_35.html), [3.6 Noslēguma projekts: "Gudrais Akmens-Šķēres-Papīrīts"](programmesana1/prog1_3/prog1_36.html), [4.6 Noslēguma projekts: Skaitļu minētājs](programmesana1/prog1_4/prog1_46.html), [5.1 Saraksti](programmesana1/prog1_5/prog1_51.html), [5.2 Vārdnīcas](programmesana1/prog1_5/prog1_52.html), [5.3 For cikli](programmesana1/prog1_5/prog1_53.html), [5.5 Analīze un integrācija](programmesana1/prog1_5/prog1_55.html), [5.6 Noslēguma projekts: Atmiņu kāršu spēle](programmesana1/prog1_5/prog1_56.html), [6.1 Failu I/O](programmesana1/prog1_6/prog1_61.html), [6.3 Datu transformācija](programmesana1/prog1_6/prog1_63.html), [6.4 Rezultātu tabulas](programmesana1/prog1_6/prog1_64.html), [9.5 Interaktivitāte pārlūkprogrammā](programmesana1/prog1_9/prog1_95.html) |
| `2.4.15` | Nosegts | [10.6 Noslēguma projekts: Highscore datubāze](programmesana1/prog1_10/prog1_106.html), [11.1 Klases un objekti](programmesana1/prog1_11/prog1_111.html), [11.2 Konstruktori un atribūti](programmesana1/prog1_11/prog1_112.html), [11.3 Metodes un self](programmesana1/prog1_11/prog1_113.html), [11.4 Mantošana un super()](programmesana1/prog1_11/prog1_114.html), [11.6 Noslēguma projekts: Klases turnīra simulators](programmesana1/prog1_11/prog1_116.html), [12.2 Flask: Python kā web serveris](programmesana1/prog1_12/prog1_122.html), [4.1 Funkciju definēšana un parametri](programmesana1/prog1_4/prog1_41.html), [4.2 Vērtību atgriešana (return)](programmesana1/prog1_4/prog1_42.html), [4.3 Modularitāte un koda sadalīšana](programmesana1/prog1_4/prog1_43.html), [4.6 Noslēguma projekts: Skaitļu minētājs](programmesana1/prog1_4/prog1_46.html), [5.6 Noslēguma projekts: Atmiņu kāršu spēle](programmesana1/prog1_5/prog1_56.html) |
| `2.4.16` | Nosegts | [3.5 Saraksti un For cikli](programmesana1/prog1_3/prog1_35.html), [3.6 Noslēguma projekts: "Gudrais Akmens-Šķēres-Papīrīts"](programmesana1/prog1_3/prog1_36.html), [4.4 Lokālie/globālie mainīgie un vārdnīcas](programmesana1/prog1_4/prog1_44.html), [5.6 Noslēguma projekts: Atmiņu kāršu spēle](programmesana1/prog1_5/prog1_56.html), [7.3 Big O un Sarežģītība](programmesana1/prog1_7/prog1_73.html), [7.4 Iebūvēto funkciju ātrums](programmesana1/prog1_7/prog1_74.html), [7.5 Iebūvēto funkciju efektivitāte](programmesana1/prog1_7/prog1_75.html), [7.6 Noslēguma projekts: "Koda lauzējs: AI Efektivitāte"](programmesana1/prog1_7/prog1_76.html) |
| `2.4.17` | Nosegts | [10.1 Ievads datubāzēs un PostgreSQL](programmesana1/prog1_10/prog1_101.html), [10.2 SQL CRUD: SELECT, INSERT, UPDATE, DELETE](programmesana1/prog1_10/prog1_102.html), [10.6 Noslēguma projekts: Highscore datubāze](programmesana1/prog1_10/prog1_106.html), [12.6 Noslēguma projekts: Daudzspēlētāju Krustiņi un nullītes](programmesana1/prog1_12/prog1_126.html), [6.6 Noslēguma projekts: Quiz spēle ar Highscore](programmesana1/prog1_6/prog1_66.html) |
| `2.4.18` | Nosegts | [11.1 Klases un objekti](programmesana1/prog1_11/prog1_111.html), [11.2 Konstruktori un atribūti](programmesana1/prog1_11/prog1_112.html), [11.3 Metodes un self](programmesana1/prog1_11/prog1_113.html), [11.4 Mantošana un super()](programmesana1/prog1_11/prog1_114.html), [11.5 Polimorfisms un dunder metodes](programmesana1/prog1_11/prog1_115.html), [11.6 Noslēguma projekts: Klases turnīra simulators](programmesana1/prog1_11/prog1_116.html), [12.6 Noslēguma projekts: Daudzspēlētāju Krustiņi un nullītes](programmesana1/prog1_12/prog1_126.html), [9.6 Noslēguma projekts: "Krustiņi un nullītes" pārlūkā](programmesana1/prog1_9/prog1_96.html) |
| `2.4.19` | Nosegts | [7.1 Meklēšanas pamati](programmesana1/prog1_7/prog1_71.html), [7.2 Kārtošanas loģika](programmesana1/prog1_7/prog1_72.html), [7.4 Iebūvēto funkciju ātrums](programmesana1/prog1_7/prog1_74.html), [7.5 Iebūvēto funkciju efektivitāte](programmesana1/prog1_7/prog1_75.html), [7.6 Noslēguma projekts: "Koda lauzējs: AI Efektivitāte"](programmesana1/prog1_7/prog1_76.html) |
| `3.1.1` | Nosegts | [1.1 Datora sagatavošana un IDE](programmesana1/prog1_1/prog1_11.html), [1.6 Noslēguma pārbaudes darbs — Darba vide un kodu pārvaldība](programmesana1/prog1_1/prog1_16.html), [12.5 Izvietošana mākonī un drošība](programmesana1/prog1_12/prog1_125.html), [2.6 Noslēguma projekts: "Lielais skaitļu duelītis"](programmesana1/prog1_2/prog1_26.html) |
| `3.1.3` | Nosegts | [9.2 Atvērtā koda licences un dokumentācija](programmesana1/prog1_9/prog1_92.html) |
| `3.2.5` | Nosegts | [10.5 Python ↔ PostgreSQL (psycopg2)](programmesana1/prog1_10/prog1_105.html), [12.5 Izvietošana mākonī un drošība](programmesana1/prog1_12/prog1_125.html) |

### Programmēšana II

| SR | Statuss | Piesaistītās stundas |
|---|---|---|
| `2.3.1` | Nav piesaistīts | Ieteikums: [prog2_11](programmesana2/prog2_1/prog2_11.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.3.2` | Nav piesaistīts | Ieteikums: [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.4.1` | Nosegts | [1.6 Noslēguma projekts: Pong](programmesana2/prog2_1/prog2_16.html), [2.6 Noslēguma projekts: Platformas spēle](programmesana2/prog2_2/prog2_26.html), [3.6 Noslēguma projekts: Klases turnīra simulators](programmesana2/prog2_3/prog2_36.html), [4.6 Noslēguma projekts: Top-down šautene](programmesana2/prog2_4/prog2_46.html), [5.6 Noslēguma projekts: Procedurālais klases labirints](programmesana2/prog2_5/prog2_56.html), [6.6 Noslēguma projekts: Puzzle spēle](programmesana2/prog2_6/prog2_66.html) |
| `2.4.2` | Nosegts | [1.3 C++ un GDExtension sagatavošana](programmesana2/prog2_1/prog2_13.html) |
| `2.4.3` | Nav piesaistīts | Ieteikums: [prog2_16](programmesana2/prog2_1/prog2_16.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.4` | Nosegts | [4.2 Map un Dictionary](programmesana2/prog2_4/prog2_42.html), [5.1 Failu I/O Godot vidē](programmesana2/prog2_5/prog2_51.html) |
| `2.4.5` | Nav piesaistīts | Ieteikums: [prog2_55](programmesana2/prog2_5/prog2_55.html), [prog2_64](programmesana2/prog2_6/prog2_64.html) |
| `2.4.6` | Nosegts | [5.3 Save/Load arhitektūra](programmesana2/prog2_5/prog2_53.html), [6.5 Eksports un publicēšana](programmesana2/prog2_6/prog2_65.html), [6.6 Noslēguma projekts: Puzzle spēle](programmesana2/prog2_6/prog2_66.html) |
| `2.4.7` | Nosegts | [1.5 Spēles laukuma izveide](programmesana2/prog2_1/prog2_15.html), [1.6 Noslēguma projekts: Pong](programmesana2/prog2_1/prog2_16.html), [2.2 Input apstrāde un Input Map](programmesana2/prog2_2/prog2_22.html), [2.4 Sadursmju noteikšana](programmesana2/prog2_2/prog2_24.html), [2.6 Noslēguma projekts: Platformas spēle](programmesana2/prog2_2/prog2_26.html), [3.4 Custom GDExtension klases editor redzamas](programmesana2/prog2_3/prog2_34.html), [3.6 Noslēguma projekts: Klases turnīra simulators](programmesana2/prog2_3/prog2_36.html), [6.1 UI elementi un Control nodes](programmesana2/prog2_6/prog2_61.html), [6.2 Animācijas un Tween](programmesana2/prog2_6/prog2_62.html), [6.3 Audio sistēma](programmesana2/prog2_6/prog2_63.html), [6.6 Noslēguma projekts: Puzzle spēle](programmesana2/prog2_6/prog2_66.html) |
| `2.4.8` | Nav piesaistīts | Ieteikums: [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.9` | Nav piesaistīts | Ieteikums: [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.4.10` | Nosegts | [6.4 Atkļūdošana un profilēšana](programmesana2/prog2_6/prog2_64.html) |
| `2.4.11` | Nav piesaistīts | Ieteikums: [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.12` | Nosegts | [1.1 Godot instalācija un projekta sagatavošana](programmesana2/prog2_1/prog2_11.html), [1.3 C++ un GDExtension sagatavošana](programmesana2/prog2_1/prog2_13.html) |
| `2.4.13` | Nosegts | [1.2 Scene Tree un Node sistēma](programmesana2/prog2_1/prog2_12.html), [1.4 Pirmais C++ skripts: mainīgie un izvade](programmesana2/prog2_1/prog2_14.html), [1.5 Spēles laukuma izveide](programmesana2/prog2_1/prog2_15.html), [2.3 Vadības struktūras spēles loģikā](programmesana2/prog2_2/prog2_23.html), [2.5 Gravitācija un platformas mehānika](programmesana2/prog2_2/prog2_25.html), [4.1 Vector un Array](programmesana2/prog2_4/prog2_41.html) |
| `2.4.14` | Nosegts | [2.1 Process un fizikas cikli](programmesana2/prog2_2/prog2_21.html), [2.2 Input apstrāde un Input Map](programmesana2/prog2_2/prog2_22.html), [2.3 Vadības struktūras spēles loģikā](programmesana2/prog2_2/prog2_23.html), [2.4 Sadursmju noteikšana](programmesana2/prog2_2/prog2_24.html), [2.5 Gravitācija un platformas mehānika](programmesana2/prog2_2/prog2_25.html), [2.6 Noslēguma projekts: Platformas spēle](programmesana2/prog2_2/prog2_26.html) |
| `2.4.15` | Nosegts | [1.2 Scene Tree un Node sistēma](programmesana2/prog2_1/prog2_12.html), [1.4 Pirmais C++ skripts: mainīgie un izvade](programmesana2/prog2_1/prog2_14.html), [1.6 Noslēguma projekts: Pong](programmesana2/prog2_1/prog2_16.html), [2.1 Process un fizikas cikli](programmesana2/prog2_2/prog2_21.html), [2.6 Noslēguma projekts: Platformas spēle](programmesana2/prog2_2/prog2_26.html), [3.1 C++ klases pamati](programmesana2/prog2_3/prog2_31.html), [3.2 Mantošana C++ un Godot](programmesana2/prog2_3/prog2_32.html), [3.3 Signāli un objektu komunikācija](programmesana2/prog2_3/prog2_33.html), [3.6 Noslēguma projekts: Klases turnīra simulators](programmesana2/prog2_3/prog2_36.html), [6.1 UI elementi un Control nodes](programmesana2/prog2_6/prog2_61.html), [6.2 Animācijas un Tween](programmesana2/prog2_6/prog2_62.html), [6.3 Audio sistēma](programmesana2/prog2_6/prog2_63.html) |
| `2.4.16` | Nosegts | [3.5 Statistikas sistēma un struct](programmesana2/prog2_3/prog2_35.html), [4.1 Vector un Array](programmesana2/prog2_4/prog2_41.html), [4.2 Map un Dictionary](programmesana2/prog2_4/prog2_42.html), [4.4 Pathfinding ar A*](programmesana2/prog2_4/prog2_44.html), [4.5 Šaušanas mehānika un object pooling](programmesana2/prog2_4/prog2_45.html), [4.6 Noslēguma projekts: Top-down šautene](programmesana2/prog2_4/prog2_46.html), [5.2 JSON serializācija un Resource sistēma](programmesana2/prog2_5/prog2_52.html), [5.4 Procedural generation](programmesana2/prog2_5/prog2_54.html), [5.6 Noslēguma projekts: Procedurālais klases labirints](programmesana2/prog2_5/prog2_56.html) |
| `2.4.17` | Nosegts | [5.1 Failu I/O Godot vidē](programmesana2/prog2_5/prog2_51.html), [5.2 JSON serializācija un Resource sistēma](programmesana2/prog2_5/prog2_52.html), [5.3 Save/Load arhitektūra](programmesana2/prog2_5/prog2_53.html), [5.6 Noslēguma projekts: Procedurālais klases labirints](programmesana2/prog2_5/prog2_56.html) |
| `2.4.18` | Nosegts | [3.1 C++ klases pamati](programmesana2/prog2_3/prog2_31.html), [3.2 Mantošana C++ un Godot](programmesana2/prog2_3/prog2_32.html), [3.3 Signāli un objektu komunikācija](programmesana2/prog2_3/prog2_33.html), [3.4 Custom GDExtension klases editor redzamas](programmesana2/prog2_3/prog2_34.html), [3.5 Statistikas sistēma un struct](programmesana2/prog2_3/prog2_35.html), [3.6 Noslēguma projekts: Klases turnīra simulators](programmesana2/prog2_3/prog2_36.html), [4.3 State machines AI uzvedībai](programmesana2/prog2_4/prog2_43.html), [4.6 Noslēguma projekts: Top-down šautene](programmesana2/prog2_4/prog2_46.html) |
| `2.4.19` | Nosegts | [4.3 State machines AI uzvedībai](programmesana2/prog2_4/prog2_43.html), [4.4 Pathfinding ar A*](programmesana2/prog2_4/prog2_44.html), [4.5 Šaušanas mehānika un object pooling](programmesana2/prog2_4/prog2_45.html), [4.6 Noslēguma projekts: Top-down šautene](programmesana2/prog2_4/prog2_46.html), [5.4 Procedural generation](programmesana2/prog2_5/prog2_54.html), [5.5 Algoritmu efektivitāte](programmesana2/prog2_5/prog2_55.html), [5.6 Noslēguma projekts: Procedurālais klases labirints](programmesana2/prog2_5/prog2_56.html), [6.4 Atkļūdošana un profilēšana](programmesana2/prog2_6/prog2_64.html) |
| `3.1.2` | Nosegts | [1.1 Godot instalācija un projekta sagatavošana](programmesana2/prog2_1/prog2_11.html) |
| `3.1.4` | Nosegts | [6.5 Eksports un publicēšana](programmesana2/prog2_6/prog2_65.html), [6.6 Noslēguma projekts: Puzzle spēle](programmesana2/prog2_6/prog2_66.html) |

## Nākamās darbības

1. Pievienot vai precizēt mācību aktivitātes un SR saites sadaļā “Nenosegtie obligātie SR”.
2. Pēc katras piesaistes atkārtot auditu un pārliecināties, ka segums tiek vērtēts kursa kontekstā, nevis tikai pēc koda teksta.
3. Ja SR tiek piesaistīts tikai formāli, papildināt stundas uzdevumu vai vērtēšanas kritērijus, lai skolēnam SR tiešām būtu jādemonstrē.
