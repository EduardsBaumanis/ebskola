# Mācību satura audits

Sākotnējais audits: 2026-06-02. Datorika 9 pārskatīta: 2026-09-14.

Šis audits salīdzina `sasnRez.html` ierakstītos sasniedzamos rezultātus ar faktiskajām mācību stundu lapām. SR kodi tiek vērtēti kursa/vecumposma kontekstā, jo, piemēram, `2.4.1.` 9. klases datorikā, Programmēšanā I un Programmēšanā II nav viens un tas pats rezultāts.

## Metodika

- Obligātie SR ir `sasnRez.html` tabulu ieraksti ar `class="sr-kods"`.
- 9. klases datorikas caurviju prasmes un mācību jomas mērķi ar `goal-num` ir pārbaudīti atsevišķi, jo tie tiek lietoti daļā stundu SR atsaucēs.
- Par mācību stundām skaitītas visas ne-`main.html` lapas mapēs `datorika9`, `robotika`, `programmesana1` un `programmesana2`. Kursu un tēmu ievadlapas auditā netiek skaitītas kā stundas.
- Datorika 9 SR piesaistes atrodas atveramajā skolotāja sadaļā ar `.lesson-meta`. Pārējos kursos izmantota sākotnējā metode: ievaddaļa no `h1` līdz pirmajam `h2`. Datorika 9 piesaistes pārbaudītas pret konkrēto uzdevumu saturu, nošķirot daļēju apguvi no visa SR izpildes.
- Pēc šīs kārtas ieteiktās piesaistes ir ierakstītas pašos stundu HTML failos; audits vairs neuzskata priekšlikumu par segumu, ja stunda to faktiski nenorāda.

## Kopsavilkums

| Kurss | Stundas | Obligātie SR | Nosegti | Nenosegti | Piezīmes |
|---|---:|---:|---:|---:|---|
| Datorika 9. klase | 30 | 37 | 22 rezultātu daļas | 15 bez tieša uzdevuma | Piesaiste neapliecina visa SR apguvi; skatīt piezīmes zemāk. |
| Robotika 7. klase | 10 | 7 | 7 | 0 | OK |
| Programmēšana I | 72 | 29 | 29 | 0 | OK |
| Programmēšana II | 36 | 23 | 23 | 0 | OK |

## Pārskatījuma secinājumi

Datorika 9 iepriekšējais vērtējums “37 no 37” tika balstīts uz SR saišu esamību. Tas neapliecināja visu rezultātu praktisku apguvi. Pārstrādātajā kursā noņemtas nepamatotas Office, datortīklu un robotu/sensoru prasību piesaistes. Pārējo kursu tabulas šajā pārskatījumā nav pārvērtētas.

Saglabātas piecas tēmas un 30 dubultstundas. Katrai tēmai noslēguma projekts aizņem pēdējās divas dubultstundas. Skolēns iesniedz trešā uzdevuma praktisko rezultātu; izvēles papildu uzdevums neietekmē ieskaiti.

## Datorika 9: rezultātu pārklājums

22 no 37 saraksta kodiem ir tieši vingrinātas daļas. Arī šiem kodiem nedrīkst automātiski piešķirt pilnu apguvi: piemēram, skaņas ievietošana neaizstāj video veidošanu, bet vienkāršs zīmējums Paint neaizstāj visu darbu ar rastra un vektoru grafiku.

Bez tieša uzdevuma šajā 30 nodarbību kursā paliek: `1.1.3`, `1.3.3`, `1.3.4`, `3.4.3`, `3.4.4`, `2.3.2`, `2.4.1`, `2.4.2`, `2.4.3`, `2.4.4`, `2.4.9`, `2.4.11`, `2.5.1`, `2.5.4`, `2.6.3`. To apguvi nepieciešams pārbaudīt citos skolēnu darbos; iepriekšējo klašu apguve netiek pieņemta par notikušu.

Caurviju prasmes attīsta praktiski: skolēns izvēlas sava darba saturu, ievēro soļus, labo kļūdas un pārbauda klasesbiedra darbu. Šis pārskats nepielīdzina šīs darbības pilnai visu caurviju un mācību jomas mērķu apguvei.

Detalizētie nosacījumi: [Datorika 9 skolotāja piezīmes](datorika9/SKOLOTAJAM.md). SR avots: [sasnRez.html 9. klases sadaļa](sasnRez.html#datorika9); tā teksts šajā pārstrādē nav mainīts.

## Stunda pret SR

### Datorika 9. klase

| Stunda | SR kodi | Pierādījuma robeža |
|---|---|---|
| [1.1 Sagatavo VS Code un GitHub](datorika9/dat9_11.html) | `2.3.1`, `2.3.3`, `2.5.2` | Praktiski vingrināta rezultāta daļa. |
| [1.2 HTML lapas uzbūve un pirmā saglabātā versija](datorika9/dat9_12.html) | `2.3.3`, `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [1.3 Salīdzini spēles lapas un nosūti darbu uz GitHub](datorika9/dat9_13.html) | `1.1.1`, `1.2.3`, `2.5.3` | Praktiski vingrināta rezultāta daļa. |
| [1.4 Izvēlies spēles ideju un spēlētāju](datorika9/dat9_14.html) | `1.2.1`, `1.2.2`, `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [1.5 Izveido spēles ekrānus — projekta 1. daļa](datorika9/dat9_15.html) | `1.1.2`, `1.3.2`, `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [1.6 Pabeidz spēles pieteikumu — projekta 2. daļa](datorika9/dat9_16.html) | `1.2.2`, `1.3.1`, `1.5.1`, `2.5.3` | Praktiski vingrināta rezultāta daļa. |
| [2.1 Maini lapas krāsas un tekstu](datorika9/dat9_21.html) | `1.1.1`, `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [2.2 Sakārto atstarpes un spēles laukumu](datorika9/dat9_22.html) | `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [2.3 Sagatavo un pievieno spēles attēlu](datorika9/dat9_23.html) | `2.4.5`, `2.4.7`, `2.4.10` | Praktiski vingrināta rezultāta daļa. |
| [2.4 Pievieno un pielāgo spēles skaņu](datorika9/dat9_24.html) | `2.4.6`, `2.4.8`, `2.4.10` | Praktiski vingrināta rezultāta daļa. |
| [2.5 Sakārto failus un arhīvu — projekta 1. daļa](datorika9/dat9_25.html) | `2.3.3`, `2.4.8`, `2.4.10` | Praktiski vingrināta rezultāta daļa. |
| [2.6 Pabeidz noformēto spēles lapu — projekta 2. daļa](datorika9/dat9_26.html) | `1.4.1`, `2.4.8`, `2.4.10`, `2.5.3` | Praktiski vingrināta rezultāta daļa. |
| [3.1 JavaScript: spēles nosaukums, punkti un dzīvības](datorika9/dat9_31.html) | `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [3.2 Ievadi tekstu un aprēķini punktus](datorika9/dat9_32.html) | `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [3.3 Nosacījumi: kad spēlētājs uzvar?](datorika9/dat9_33.html) | `2.6.1`, `2.6.2` | Praktiski vingrināta rezultāta daļa. |
| [3.4 Masīvs: spēlētāja priekšmetu saraksts](datorika9/dat9_34.html) | `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [3.5 Cikls izveido izvēles — projekta 1. daļa](datorika9/dat9_35.html) | `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [3.6 Pabeidz teksta spēli — projekta 2. daļa](datorika9/dat9_36.html) | `2.6.1`, `2.6.2`, `1.4.2` | Praktiski vingrināta rezultāta daļa. |
| [4.1 Funkcijas: viena darbība vairākām pogām](datorika9/dat9_41.html) | `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [4.2 Vadi spēlētāju ar pogām un taustiņiem](datorika9/dat9_42.html) | `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [4.3 Pārvieto un maini lapas elementus](datorika9/dat9_43.html) | `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [4.4 Laiks un automātiska kustība](datorika9/dat9_44.html) | `2.6.1`, `2.6.2` | Praktiski vingrināta rezultāta daļa. |
| [4.5 Sadursme aptur spēli — projekta 1. daļa](datorika9/dat9_45.html) | `2.6.1`, `2.6.2` | Praktiski vingrināta rezultāta daļa. |
| [4.6 Pabeidz kustīgo spēli — projekta 2. daļa](datorika9/dat9_46.html) | `2.6.1`, `2.6.2`, `1.4.2` | Praktiski vingrināta rezultāta daļa. |
| [5.1 Izvēlies spēles uzlabojumus un saplāno darbu](datorika9/dat9_51.html) | `1.3.1`, `1.2.2`, `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [5.2 Pabeidz sākuma, spēles un beigu ekrānu](datorika9/dat9_52.html) | `1.1.2`, `2.6.1` | Praktiski vingrināta rezultāta daļa. |
| [5.3 Savieno punktus, dzīvības un spēles beigas](datorika9/dat9_53.html) | `2.6.1`, `2.6.2` | Praktiski vingrināta rezultāta daļa. |
| [5.4 Pievieno savācamu bonusu un skaņu](datorika9/dat9_54.html) | `2.6.1`, `2.6.2` | Praktiski vingrināta rezultāta daļa. |
| [5.5 Pārbaudi savu spēli — projekta 1. daļa](datorika9/dat9_55.html) | `2.6.2`, `1.4.2`, `1.4.3` | Praktiski vingrināta rezultāta daļa. |
| [5.6 Publicē savu spēli — projekta 2. daļa](datorika9/dat9_56.html) | `1.5.1`, `2.4.10`, `2.5.3`, `2.6.2` | Praktiski vingrināta rezultāta daļa. |

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
| [1.1 Datora sagatavošana un IDE](programmesana1/prog1_1/prog1_11.html) | `2.4.12`, `3.1.1`, `2.3.1` | Atbilst vecumposmam |
| [1.2 GitHub un Mākoņkrātuve](programmesana1/prog1_1/prog1_12.html) | `2.4.9`, `2.4.12` | Atbilst vecumposmam |
| [1.3 Koda sinhronizācija (Desktop)](programmesana1/prog1_1/prog1_13.html) | `2.4.9` | Atbilst vecumposmam |
| [1.4 Failu sistēma un organizācija](programmesana1/prog1_1/prog1_14.html) | `2.4.12`, `2.4.9` | Atbilst vecumposmam |
| [1.5 Dokumentēšana, README un Licences](programmesana1/prog1_1/prog1_15.html) | `2.4.6`, `2.4.8` | Atbilst vecumposmam |
| [1.6 Noslēguma pārbaudes darbs - Darba vide un kodu pārvaldība](programmesana1/prog1_1/prog1_16.html) | `2.4.8`, `2.4.9`, `2.4.12`, `3.1.1` | Atbilst vecumposmam |
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
| [6.2 Digitālais rīks](programmesana1/prog1_6/prog1_62.html) | `2.3.5`, `2.4.1`, `2.3.1` | Atbilst vecumposmam |
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
| [8.2 Prasību specifikācija - Lietotāju stāsti](programmesana1/prog1_8/prog1_82.html) | `2.4.4` | Atbilst vecumposmam |
| [8.3 Datu modelis un UI plūsma](programmesana1/prog1_8/prog1_83.html) | `2.4.5` | Atbilst vecumposmam |
| [8.4 Prezentācijas māksla - Pitch sagatavošana](programmesana1/prog1_8/prog1_84.html) | `2.3.10` | Atbilst vecumposmam |
| [8.5 Sasniedzamie rezultāti un resursu plānošana](programmesana1/prog1_8/prog1_85.html) | `2.4.5`, `2.4.1` | Atbilst vecumposmam |
| [8.6 Noslēguma projekts: Projektējuma aizstāvēšana](programmesana1/prog1_8/prog1_86.html) | `2.4.6`, `2.4.7`, `2.4.1`, `2.4.3` | Atbilst vecumposmam |
| [9.1 Ārējās bibliotēkas un instalēšana](programmesana1/prog1_9/prog1_91.html) | `2.4.11`, `2.4.12`, `2.4.2` | Atbilst vecumposmam |
| [9.2 Atvērtā koda licences un dokumentācija](programmesana1/prog1_9/prog1_92.html) | `3.1.3`, `2.4.11`, `2.3.3` | Atbilst vecumposmam |
| [9.3 Python pārvēršana tīmekļa saskarnē](programmesana1/prog1_9/prog1_93.html) | `2.4.7`, `2.4.11` | Atbilst vecumposmam |
| [9.4 HTML un Python sasaiste](programmesana1/prog1_9/prog1_94.html) | `2.4.7`, `2.4.11` | Atbilst vecumposmam |
| [9.5 Interaktivitāte pārlūkprogrammā](programmesana1/prog1_9/prog1_95.html) | `2.4.7`, `2.4.14` | Atbilst vecumposmam |
| [9.6 Noslēguma projekts: "Krustiņi un nullītes" pārlūkā](programmesana1/prog1_9/prog1_96.html) | `2.4.1`, `2.4.7`, `2.4.18`, `2.4.11` | Atbilst vecumposmam |
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
| [12.2 Flask: Python kā web serveris](programmesana1/prog1_12/prog1_122.html) | `2.4.11`, `2.4.15`, `2.4.2` | Atbilst vecumposmam |
| [12.3 REST API izstrāde](programmesana1/prog1_12/prog1_123.html) | `2.4.11`, `2.4.7` | Atbilst vecumposmam |
| [12.4 Front-end + API integrācija](programmesana1/prog1_12/prog1_124.html) | `2.4.7`, `2.4.11` | Atbilst vecumposmam |
| [12.5 Izvietošana mākonī un drošība](programmesana1/prog1_12/prog1_125.html) | `2.4.6`, `3.1.1`, `3.2.5`, `2.3.3` | Atbilst vecumposmam |
| [12.6 Noslēguma projekts: Daudzspēlētāju Krustiņi un nullītes](programmesana1/prog1_12/prog1_126.html) | `2.4.1`, `2.4.7`, `2.4.11`, `2.4.18`, `2.4.17`, `2.4.3` | Atbilst vecumposmam |

### Programmēšana II

| Stunda | SR kodi | Atbilstība |
|---|---|---|
| [1.1 Godot instalācija un projekta sagatavošana](programmesana2/prog2_1/prog2_11.html) | `2.4.12`, `3.1.2`, `2.3.1` | Atbilst vecumposmam |
| [1.2 Scene Tree un Node sistēma](programmesana2/prog2_1/prog2_12.html) | `2.4.13`, `2.4.15` | Atbilst vecumposmam |
| [1.3 C# un .NET sagatavošana](programmesana2/prog2_1/prog2_13.html) | `2.4.12`, `2.4.2`, `2.3.2`, `2.4.8`, `2.4.9`, `2.4.11` | Atbilst vecumposmam |
| [1.4 Pirmais C# skripts: mainīgie un izvade](programmesana2/prog2_1/prog2_14.html) | `2.4.13`, `2.4.15` | Atbilst vecumposmam |
| [1.5 Spēles laukuma izveide](programmesana2/prog2_1/prog2_15.html) | `2.4.7`, `2.4.13` | Atbilst vecumposmam |
| [1.6 Noslēguma projekts: Pong](programmesana2/prog2_1/prog2_16.html) | `2.4.1`, `2.4.7`, `2.4.15`, `2.4.3` | Atbilst vecumposmam |
| [2.1 Process un fizikas cikli](programmesana2/prog2_2/prog2_21.html) | `2.4.14`, `2.4.15` | Atbilst vecumposmam |
| [2.2 Input apstrāde un Input Map](programmesana2/prog2_2/prog2_22.html) | `2.4.14`, `2.4.7` | Atbilst vecumposmam |
| [2.3 Vadības struktūras spēles loģikā](programmesana2/prog2_2/prog2_23.html) | `2.4.14`, `2.4.13` | Atbilst vecumposmam |
| [2.4 Sadursmju noteikšana](programmesana2/prog2_2/prog2_24.html) | `2.4.14`, `2.4.7` | Atbilst vecumposmam |
| [2.5 Gravitācija un platformas mehānika](programmesana2/prog2_2/prog2_25.html) | `2.4.14`, `2.4.13` | Atbilst vecumposmam |
| [2.6 Noslēguma projekts: Platformas spēle](programmesana2/prog2_2/prog2_26.html) | `2.4.1`, `2.4.7`, `2.4.14`, `2.4.15` | Atbilst vecumposmam |
| [3.1 C++ klases pamati](programmesana2/prog2_3/prog2_31.html) | `2.4.18`, `2.4.15` | Atbilst vecumposmam |
| [3.2 Mantošana C++ un Godot](programmesana2/prog2_3/prog2_32.html) | `2.4.18`, `2.4.15` | Atbilst vecumposmam |
| [3.3 Signāli un objektu komunikācija](programmesana2/prog2_3/prog2_33.html) | `2.4.15`, `2.4.18` | Atbilst vecumposmam |
| [3.4 Custom GDExtension klases editorā redzamas](programmesana2/prog2_3/prog2_34.html) | `2.4.7`, `2.4.18` | Atbilst vecumposmam |
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
| [5.5 Algoritmu efektivitāte](programmesana2/prog2_5/prog2_55.html) | `2.4.19`, `2.4.5` | Atbilst vecumposmam |
| [5.6 Noslēguma projekts: Procedurālais klases labirints](programmesana2/prog2_5/prog2_56.html) | `2.4.1`, `2.4.16`, `2.4.17`, `2.4.19` | Atbilst vecumposmam |
| [6.1 UI elementi un Control nodes](programmesana2/prog2_6/prog2_61.html) | `2.4.7`, `2.4.15` | Atbilst vecumposmam |
| [6.2 Animācijas un Tween](programmesana2/prog2_6/prog2_62.html) | `2.4.7`, `2.4.15` | Atbilst vecumposmam |
| [6.3 Audio sistēma](programmesana2/prog2_6/prog2_63.html) | `2.4.7`, `2.4.15` | Atbilst vecumposmam |
| [6.4 Atkļūdošana un profilēšana](programmesana2/prog2_6/prog2_64.html) | `2.4.10`, `2.4.19`, `2.4.5` | Atbilst vecumposmam |
| [6.5 Eksports un publicēšana](programmesana2/prog2_6/prog2_65.html) | `2.4.6`, `3.1.4`, `2.3.1`, `2.3.2`, `2.4.9` | Atbilst vecumposmam |
| [6.6 Noslēguma projekts: Puzzle spēle](programmesana2/prog2_6/prog2_66.html) | `2.4.1`, `2.4.7`, `2.4.6`, `3.1.4`, `2.4.3`, `2.4.8`, `2.4.11` | Atbilst vecumposmam |

## SR pret stundām

### Datorika 9. klase

| SR | Grupa | Stundas |
|---|---|---|
| `1.1.1` | Dizaina process un tehnoloģijas | [dat9_13](datorika9/dat9_13.html), [dat9_21](datorika9/dat9_21.html), [dat9_22](datorika9/dat9_22.html) |
| `1.1.2` | Dizaina process un tehnoloģijas | [dat9_15](datorika9/dat9_15.html), [dat9_52](datorika9/dat9_52.html) |
| `1.1.3` | Dizaina process un tehnoloģijas | [dat9_15](datorika9/dat9_15.html), [dat9_16](datorika9/dat9_16.html), [dat9_55](datorika9/dat9_55.html) |
| `1.2.1` | Dizaina process un tehnoloģijas | [dat9_14](datorika9/dat9_14.html) |
| `1.2.2` | Dizaina process un tehnoloģijas | [dat9_14](datorika9/dat9_14.html) |
| `1.2.3` | Dizaina process un tehnoloģijas | [dat9_13](datorika9/dat9_13.html) |
| `1.3.1` | Dizaina process un tehnoloģijas | [dat9_16](datorika9/dat9_16.html), [dat9_51](datorika9/dat9_51.html) |
| `1.3.2` | Dizaina process un tehnoloģijas | [dat9_15](datorika9/dat9_15.html) |
| `1.3.3` | Dizaina process un tehnoloģijas | [dat9_42](datorika9/dat9_42.html), [dat9_55](datorika9/dat9_55.html) |
| `1.3.4` | Dizaina process un tehnoloģijas | [dat9_41](datorika9/dat9_41.html), [dat9_46](datorika9/dat9_46.html) |
| `1.4.1` | Dizaina process un tehnoloģijas | [dat9_26](datorika9/dat9_26.html) |
| `1.4.2` | Dizaina process un tehnoloģijas | [dat9_46](datorika9/dat9_46.html), [dat9_55](datorika9/dat9_55.html) |
| `1.4.3` | Dizaina process un tehnoloģijas | [dat9_55](datorika9/dat9_55.html), [dat9_56](datorika9/dat9_56.html) |
| `1.5.1` | Dizaina process un tehnoloģijas | [dat9_16](datorika9/dat9_16.html), [dat9_51](datorika9/dat9_51.html), [dat9_56](datorika9/dat9_56.html) |
| `3.4.3` | Dizaina process un tehnoloģijas | [dat9_44](datorika9/dat9_44.html) |
| `3.4.4` | Dizaina process un tehnoloģijas | [dat9_13](datorika9/dat9_13.html), [dat9_54](datorika9/dat9_54.html) |
| `2.3.1` | Datorika, digitālā pratība un programmēšana | [dat9_11](datorika9/dat9_11.html), [dat9_54](datorika9/dat9_54.html) |
| `2.3.2` | Datorika, digitālā pratība un programmēšana | [dat9_11](datorika9/dat9_11.html), [dat9_56](datorika9/dat9_56.html) |
| `2.3.3` | Datorika, digitālā pratība un programmēšana | [dat9_12](datorika9/dat9_12.html), [dat9_25](datorika9/dat9_25.html) |
| `2.4.1` | Datorika, digitālā pratība un programmēšana | [dat9_22](datorika9/dat9_22.html) |
| `2.4.2` | Datorika, digitālā pratība un programmēšana | [dat9_34](datorika9/dat9_34.html) |
| `2.4.3` | Datorika, digitālā pratība un programmēšana | [dat9_34](datorika9/dat9_34.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.4` | Datorika, digitālā pratība un programmēšana | [dat9_16](datorika9/dat9_16.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.5` | Datorika, digitālā pratība un programmēšana | [dat9_26](datorika9/dat9_26.html) |
| `2.4.6` | Datorika, digitālā pratība un programmēšana | [dat9_23](datorika9/dat9_23.html), [dat9_24](datorika9/dat9_24.html), [dat9_26](datorika9/dat9_26.html) |
| `2.4.7` | Datorika, digitālā pratība un programmēšana | [dat9_23](datorika9/dat9_23.html), [dat9_43](datorika9/dat9_43.html) |
| `2.4.8` | Datorika, digitālā pratība un programmēšana | [dat9_26](datorika9/dat9_26.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.9` | Datorika, digitālā pratība un programmēšana | [dat9_22](datorika9/dat9_22.html), [dat9_24](datorika9/dat9_24.html) |
| `2.4.10` | Datorika, digitālā pratība un programmēšana | [dat9_24](datorika9/dat9_24.html), [dat9_26](datorika9/dat9_26.html), [dat9_56](datorika9/dat9_56.html) |
| `2.4.11` | Datorika, digitālā pratība un programmēšana | [dat9_52](datorika9/dat9_52.html) |
| `2.5.1` | Datorika, digitālā pratība un programmēšana | [dat9_56](datorika9/dat9_56.html) |
| `2.5.2` | Datorika, digitālā pratība un programmēšana | [dat9_11](datorika9/dat9_11.html), [dat9_56](datorika9/dat9_56.html) |
| `2.5.3` | Datorika, digitālā pratība un programmēšana | [dat9_21](datorika9/dat9_21.html), [dat9_56](datorika9/dat9_56.html) |
| `2.5.4` | Datorika, digitālā pratība un programmēšana | [dat9_13](datorika9/dat9_13.html), [dat9_56](datorika9/dat9_56.html) |
| `2.6.1` | Datorika, digitālā pratība un programmēšana | [dat9_12](datorika9/dat9_12.html), [dat9_16](datorika9/dat9_16.html), [dat9_31](datorika9/dat9_31.html), [dat9_32](datorika9/dat9_32.html), [dat9_33](datorika9/dat9_33.html), [dat9_34](datorika9/dat9_34.html), [dat9_35](datorika9/dat9_35.html), [dat9_36](datorika9/dat9_36.html), [dat9_41](datorika9/dat9_41.html), [dat9_42](datorika9/dat9_42.html), [dat9_43](datorika9/dat9_43.html), [dat9_44](datorika9/dat9_44.html), [dat9_45](datorika9/dat9_45.html), [dat9_46](datorika9/dat9_46.html), [dat9_53](datorika9/dat9_53.html), [dat9_55](datorika9/dat9_55.html) |
| `2.6.2` | Datorika, digitālā pratība un programmēšana | [dat9_36](datorika9/dat9_36.html), [dat9_53](datorika9/dat9_53.html) |
| `2.6.3` | Datorika, digitālā pratība un programmēšana | [dat9_46](datorika9/dat9_46.html) |

### Robotika 7. klase

| SR | Grupa | Stundas |
|---|---|---|
| `D.7.1.1` | Datorika 7. klasei - robotikas konteksts (MK 747) | [rbtk7_11](robotika/rbtk7_11.html), [rbtk7_14](robotika/rbtk7_14.html), [rbtk7_21](robotika/rbtk7_21.html), [rbtk7_24](robotika/rbtk7_24.html), [rbtk7_25](robotika/rbtk7_25.html) |
| `D.7.2.1` | Datorika 7. klasei - robotikas konteksts (MK 747) | [rbtk7_11](robotika/rbtk7_11.html), [rbtk7_12](robotika/rbtk7_12.html), [rbtk7_13](robotika/rbtk7_13.html), [rbtk7_15](robotika/rbtk7_15.html), [rbtk7_21](robotika/rbtk7_21.html), [rbtk7_22](robotika/rbtk7_22.html), [rbtk7_23](robotika/rbtk7_23.html), [rbtk7_25](robotika/rbtk7_25.html) |
| `D.7.3.1` | Datorika 7. klasei - robotikas konteksts (MK 747) | [rbtk7_13](robotika/rbtk7_13.html), [rbtk7_15](robotika/rbtk7_15.html), [rbtk7_22](robotika/rbtk7_22.html), [rbtk7_25](robotika/rbtk7_25.html) |
| `D.7.4.1` | Datorika 7. klasei - robotikas konteksts (MK 747) | [rbtk7_12](robotika/rbtk7_12.html), [rbtk7_23](robotika/rbtk7_23.html) |
| `D.7.4.2` | Datorika 7. klasei - robotikas konteksts (MK 747) | [rbtk7_13](robotika/rbtk7_13.html), [rbtk7_14](robotika/rbtk7_14.html), [rbtk7_15](robotika/rbtk7_15.html), [rbtk7_24](robotika/rbtk7_24.html) |
| `D.7.5.1` | Datorika 7. klasei - robotikas konteksts (MK 747) | [rbtk7_14](robotika/rbtk7_14.html), [rbtk7_15](robotika/rbtk7_15.html) |
| `D.7.6.1` | Datorika 7. klasei - robotikas konteksts (MK 747) | [rbtk7_15](robotika/rbtk7_15.html), [rbtk7_21](robotika/rbtk7_21.html), [rbtk7_22](robotika/rbtk7_22.html), [rbtk7_23](robotika/rbtk7_23.html), [rbtk7_24](robotika/rbtk7_24.html), [rbtk7_25](robotika/rbtk7_25.html) |

### Programmēšana I

| SR | Grupa | Stundas |
|---|---|---|
| `2.3.1` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_11](programmesana1/prog1_1/prog1_11.html), [prog1_62](programmesana1/prog1_6/prog1_62.html) |
| `2.3.2` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_54](programmesana1/prog1_5/prog1_54.html) |
| `2.3.3` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_92](programmesana1/prog1_9/prog1_92.html), [prog1_125](programmesana1/prog1_12/prog1_125.html) |
| `2.3.4` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_54](programmesana1/prog1_5/prog1_54.html), [prog1_55](programmesana1/prog1_5/prog1_55.html) |
| `2.3.5` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_62](programmesana1/prog1_6/prog1_62.html) |
| `2.3.6` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_65](programmesana1/prog1_6/prog1_65.html) |
| `2.3.10` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_84](programmesana1/prog1_8/prog1_84.html) |
| `2.4.1` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_25](programmesana1/prog1_2/prog1_25.html), [prog1_45](programmesana1/prog1_4/prog1_45.html), [prog1_62](programmesana1/prog1_6/prog1_62.html), [prog1_81](programmesana1/prog1_8/prog1_81.html), [prog1_85](programmesana1/prog1_8/prog1_85.html), [prog1_86](programmesana1/prog1_8/prog1_86.html), [prog1_96](programmesana1/prog1_9/prog1_96.html), [prog1_103](programmesana1/prog1_10/prog1_103.html), [prog1_121](programmesana1/prog1_12/prog1_121.html), [prog1_126](programmesana1/prog1_12/prog1_126.html) |
| `2.4.2` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_91](programmesana1/prog1_9/prog1_91.html), [prog1_122](programmesana1/prog1_12/prog1_122.html) |
| `2.4.3` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_86](programmesana1/prog1_8/prog1_86.html), [prog1_126](programmesana1/prog1_12/prog1_126.html) |
| `2.4.4` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_66](programmesana1/prog1_6/prog1_66.html), [prog1_82](programmesana1/prog1_8/prog1_82.html), [prog1_101](programmesana1/prog1_10/prog1_101.html), [prog1_104](programmesana1/prog1_10/prog1_104.html), [prog1_106](programmesana1/prog1_10/prog1_106.html) |
| `2.4.5` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_66](programmesana1/prog1_6/prog1_66.html), [prog1_83](programmesana1/prog1_8/prog1_83.html), [prog1_85](programmesana1/prog1_8/prog1_85.html), [prog1_104](programmesana1/prog1_10/prog1_104.html), [prog1_106](programmesana1/prog1_10/prog1_106.html) |
| `2.4.6` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_15](programmesana1/prog1_1/prog1_15.html), [prog1_25](programmesana1/prog1_2/prog1_25.html), [prog1_43](programmesana1/prog1_4/prog1_43.html), [prog1_45](programmesana1/prog1_4/prog1_45.html), [prog1_86](programmesana1/prog1_8/prog1_86.html), [prog1_103](programmesana1/prog1_10/prog1_103.html), [prog1_125](programmesana1/prog1_12/prog1_125.html) |
| `2.4.7` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_86](programmesana1/prog1_8/prog1_86.html), [prog1_93](programmesana1/prog1_9/prog1_93.html), [prog1_94](programmesana1/prog1_9/prog1_94.html), [prog1_95](programmesana1/prog1_9/prog1_95.html), [prog1_96](programmesana1/prog1_9/prog1_96.html), [prog1_121](programmesana1/prog1_12/prog1_121.html), [prog1_123](programmesana1/prog1_12/prog1_123.html), [prog1_124](programmesana1/prog1_12/prog1_124.html), [prog1_126](programmesana1/prog1_12/prog1_126.html) |
| `2.4.8` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_15](programmesana1/prog1_1/prog1_15.html), [prog1_16](programmesana1/prog1_1/prog1_16.html), [prog1_24](programmesana1/prog1_2/prog1_24.html), [prog1_26](programmesana1/prog1_2/prog1_26.html) |
| `2.4.9` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_12](programmesana1/prog1_1/prog1_12.html), [prog1_13](programmesana1/prog1_1/prog1_13.html), [prog1_14](programmesana1/prog1_1/prog1_14.html), [prog1_16](programmesana1/prog1_1/prog1_16.html), [prog1_26](programmesana1/prog1_2/prog1_26.html) |
| `2.4.10` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_34](programmesana1/prog1_3/prog1_34.html), [prog1_36](programmesana1/prog1_3/prog1_36.html), [prog1_46](programmesana1/prog1_4/prog1_46.html), [prog1_76](programmesana1/prog1_7/prog1_76.html) |
| `2.4.11` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_91](programmesana1/prog1_9/prog1_91.html), [prog1_92](programmesana1/prog1_9/prog1_92.html), [prog1_93](programmesana1/prog1_9/prog1_93.html), [prog1_94](programmesana1/prog1_9/prog1_94.html), [prog1_96](programmesana1/prog1_9/prog1_96.html), [prog1_105](programmesana1/prog1_10/prog1_105.html), [prog1_115](programmesana1/prog1_11/prog1_115.html), [prog1_122](programmesana1/prog1_12/prog1_122.html), [prog1_123](programmesana1/prog1_12/prog1_123.html), [prog1_124](programmesana1/prog1_12/prog1_124.html), [prog1_126](programmesana1/prog1_12/prog1_126.html) |
| `2.4.12` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_11](programmesana1/prog1_1/prog1_11.html), [prog1_12](programmesana1/prog1_1/prog1_12.html), [prog1_14](programmesana1/prog1_1/prog1_14.html), [prog1_16](programmesana1/prog1_1/prog1_16.html), [prog1_91](programmesana1/prog1_9/prog1_91.html) |
| `2.4.13` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_21](programmesana1/prog1_2/prog1_21.html), [prog1_22](programmesana1/prog1_2/prog1_22.html), [prog1_23](programmesana1/prog1_2/prog1_23.html), [prog1_26](programmesana1/prog1_2/prog1_26.html), [prog1_32](programmesana1/prog1_3/prog1_32.html), [prog1_34](programmesana1/prog1_3/prog1_34.html), [prog1_36](programmesana1/prog1_3/prog1_36.html), [prog1_44](programmesana1/prog1_4/prog1_44.html), [prog1_46](programmesana1/prog1_4/prog1_46.html), [prog1_76](programmesana1/prog1_7/prog1_76.html), [prog1_102](programmesana1/prog1_10/prog1_102.html) |
| `2.4.14` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_31](programmesana1/prog1_3/prog1_31.html), [prog1_32](programmesana1/prog1_3/prog1_32.html), [prog1_33](programmesana1/prog1_3/prog1_33.html), [prog1_35](programmesana1/prog1_3/prog1_35.html), [prog1_36](programmesana1/prog1_3/prog1_36.html), [prog1_46](programmesana1/prog1_4/prog1_46.html), [prog1_51](programmesana1/prog1_5/prog1_51.html), [prog1_52](programmesana1/prog1_5/prog1_52.html), [prog1_53](programmesana1/prog1_5/prog1_53.html), [prog1_55](programmesana1/prog1_5/prog1_55.html), [prog1_56](programmesana1/prog1_5/prog1_56.html), [prog1_61](programmesana1/prog1_6/prog1_61.html), [prog1_63](programmesana1/prog1_6/prog1_63.html), [prog1_64](programmesana1/prog1_6/prog1_64.html), [prog1_95](programmesana1/prog1_9/prog1_95.html), [prog1_116](programmesana1/prog1_11/prog1_116.html) |
| `2.4.15` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_41](programmesana1/prog1_4/prog1_41.html), [prog1_42](programmesana1/prog1_4/prog1_42.html), [prog1_43](programmesana1/prog1_4/prog1_43.html), [prog1_46](programmesana1/prog1_4/prog1_46.html), [prog1_56](programmesana1/prog1_5/prog1_56.html), [prog1_106](programmesana1/prog1_10/prog1_106.html), [prog1_111](programmesana1/prog1_11/prog1_111.html), [prog1_112](programmesana1/prog1_11/prog1_112.html), [prog1_113](programmesana1/prog1_11/prog1_113.html), [prog1_114](programmesana1/prog1_11/prog1_114.html), [prog1_116](programmesana1/prog1_11/prog1_116.html), [prog1_122](programmesana1/prog1_12/prog1_122.html) |
| `2.4.16` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_35](programmesana1/prog1_3/prog1_35.html), [prog1_36](programmesana1/prog1_3/prog1_36.html), [prog1_44](programmesana1/prog1_4/prog1_44.html), [prog1_56](programmesana1/prog1_5/prog1_56.html), [prog1_73](programmesana1/prog1_7/prog1_73.html), [prog1_74](programmesana1/prog1_7/prog1_74.html), [prog1_75](programmesana1/prog1_7/prog1_75.html), [prog1_76](programmesana1/prog1_7/prog1_76.html) |
| `2.4.17` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_66](programmesana1/prog1_6/prog1_66.html), [prog1_101](programmesana1/prog1_10/prog1_101.html), [prog1_102](programmesana1/prog1_10/prog1_102.html), [prog1_106](programmesana1/prog1_10/prog1_106.html), [prog1_126](programmesana1/prog1_12/prog1_126.html) |
| `2.4.18` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_96](programmesana1/prog1_9/prog1_96.html), [prog1_111](programmesana1/prog1_11/prog1_111.html), [prog1_112](programmesana1/prog1_11/prog1_112.html), [prog1_113](programmesana1/prog1_11/prog1_113.html), [prog1_114](programmesana1/prog1_11/prog1_114.html), [prog1_115](programmesana1/prog1_11/prog1_115.html), [prog1_116](programmesana1/prog1_11/prog1_116.html), [prog1_126](programmesana1/prog1_12/prog1_126.html) |
| `2.4.19` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_71](programmesana1/prog1_7/prog1_71.html), [prog1_72](programmesana1/prog1_7/prog1_72.html), [prog1_74](programmesana1/prog1_7/prog1_74.html), [prog1_75](programmesana1/prog1_7/prog1_75.html), [prog1_76](programmesana1/prog1_7/prog1_76.html) |
| `3.1.1` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_11](programmesana1/prog1_1/prog1_11.html), [prog1_16](programmesana1/prog1_1/prog1_16.html), [prog1_26](programmesana1/prog1_2/prog1_26.html), [prog1_125](programmesana1/prog1_12/prog1_125.html) |
| `3.1.3` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_92](programmesana1/prog1_9/prog1_92.html) |
| `3.2.5` | Sasniedzamie rezultāti (Optimālais līmenis) | [prog1_105](programmesana1/prog1_10/prog1_105.html), [prog1_125](programmesana1/prog1_12/prog1_125.html) |

### Programmēšana II

| SR | Grupa | Stundas |
|---|---|---|
| `2.3.1` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_11](programmesana2/prog2_1/prog2_11.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.3.2` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.4.1` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_16](programmesana2/prog2_1/prog2_16.html), [prog2_26](programmesana2/prog2_2/prog2_26.html), [prog2_36](programmesana2/prog2_3/prog2_36.html), [prog2_46](programmesana2/prog2_4/prog2_46.html), [prog2_56](programmesana2/prog2_5/prog2_56.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.2` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_13](programmesana2/prog2_1/prog2_13.html) |
| `2.4.3` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_16](programmesana2/prog2_1/prog2_16.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.4` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_42](programmesana2/prog2_4/prog2_42.html), [prog2_51](programmesana2/prog2_5/prog2_51.html) |
| `2.4.5` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_55](programmesana2/prog2_5/prog2_55.html), [prog2_64](programmesana2/prog2_6/prog2_64.html) |
| `2.4.6` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_53](programmesana2/prog2_5/prog2_53.html), [prog2_65](programmesana2/prog2_6/prog2_65.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.7` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_15](programmesana2/prog2_1/prog2_15.html), [prog2_16](programmesana2/prog2_1/prog2_16.html), [prog2_22](programmesana2/prog2_2/prog2_22.html), [prog2_24](programmesana2/prog2_2/prog2_24.html), [prog2_26](programmesana2/prog2_2/prog2_26.html), [prog2_34](programmesana2/prog2_3/prog2_34.html), [prog2_36](programmesana2/prog2_3/prog2_36.html), [prog2_61](programmesana2/prog2_6/prog2_61.html), [prog2_62](programmesana2/prog2_6/prog2_62.html), [prog2_63](programmesana2/prog2_6/prog2_63.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.8` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.9` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_65](programmesana2/prog2_6/prog2_65.html) |
| `2.4.10` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_64](programmesana2/prog2_6/prog2_64.html) |
| `2.4.11` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_13](programmesana2/prog2_1/prog2_13.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
| `2.4.12` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_11](programmesana2/prog2_1/prog2_11.html), [prog2_13](programmesana2/prog2_1/prog2_13.html) |
| `2.4.13` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_12](programmesana2/prog2_1/prog2_12.html), [prog2_14](programmesana2/prog2_1/prog2_14.html), [prog2_15](programmesana2/prog2_1/prog2_15.html), [prog2_23](programmesana2/prog2_2/prog2_23.html), [prog2_25](programmesana2/prog2_2/prog2_25.html), [prog2_41](programmesana2/prog2_4/prog2_41.html) |
| `2.4.14` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_21](programmesana2/prog2_2/prog2_21.html), [prog2_22](programmesana2/prog2_2/prog2_22.html), [prog2_23](programmesana2/prog2_2/prog2_23.html), [prog2_24](programmesana2/prog2_2/prog2_24.html), [prog2_25](programmesana2/prog2_2/prog2_25.html), [prog2_26](programmesana2/prog2_2/prog2_26.html) |
| `2.4.15` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_12](programmesana2/prog2_1/prog2_12.html), [prog2_14](programmesana2/prog2_1/prog2_14.html), [prog2_16](programmesana2/prog2_1/prog2_16.html), [prog2_21](programmesana2/prog2_2/prog2_21.html), [prog2_26](programmesana2/prog2_2/prog2_26.html), [prog2_31](programmesana2/prog2_3/prog2_31.html), [prog2_32](programmesana2/prog2_3/prog2_32.html), [prog2_33](programmesana2/prog2_3/prog2_33.html), [prog2_36](programmesana2/prog2_3/prog2_36.html), [prog2_61](programmesana2/prog2_6/prog2_61.html), [prog2_62](programmesana2/prog2_6/prog2_62.html), [prog2_63](programmesana2/prog2_6/prog2_63.html) |
| `2.4.16` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_35](programmesana2/prog2_3/prog2_35.html), [prog2_41](programmesana2/prog2_4/prog2_41.html), [prog2_42](programmesana2/prog2_4/prog2_42.html), [prog2_44](programmesana2/prog2_4/prog2_44.html), [prog2_45](programmesana2/prog2_4/prog2_45.html), [prog2_46](programmesana2/prog2_4/prog2_46.html), [prog2_52](programmesana2/prog2_5/prog2_52.html), [prog2_54](programmesana2/prog2_5/prog2_54.html), [prog2_56](programmesana2/prog2_5/prog2_56.html) |
| `2.4.17` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_51](programmesana2/prog2_5/prog2_51.html), [prog2_52](programmesana2/prog2_5/prog2_52.html), [prog2_53](programmesana2/prog2_5/prog2_53.html), [prog2_56](programmesana2/prog2_5/prog2_56.html) |
| `2.4.18` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_31](programmesana2/prog2_3/prog2_31.html), [prog2_32](programmesana2/prog2_3/prog2_32.html), [prog2_33](programmesana2/prog2_3/prog2_33.html), [prog2_34](programmesana2/prog2_3/prog2_34.html), [prog2_35](programmesana2/prog2_3/prog2_35.html), [prog2_36](programmesana2/prog2_3/prog2_36.html), [prog2_43](programmesana2/prog2_4/prog2_43.html), [prog2_46](programmesana2/prog2_4/prog2_46.html) |
| `2.4.19` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_43](programmesana2/prog2_4/prog2_43.html), [prog2_44](programmesana2/prog2_4/prog2_44.html), [prog2_45](programmesana2/prog2_4/prog2_45.html), [prog2_46](programmesana2/prog2_4/prog2_46.html), [prog2_54](programmesana2/prog2_5/prog2_54.html), [prog2_55](programmesana2/prog2_5/prog2_55.html), [prog2_56](programmesana2/prog2_5/prog2_56.html), [prog2_64](programmesana2/prog2_6/prog2_64.html) |
| `3.1.2` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_11](programmesana2/prog2_1/prog2_11.html) |
| `3.1.4` | Sasniedzamie rezultāti (Augstākais līmenis) | [prog2_65](programmesana2/prog2_6/prog2_65.html), [prog2_66](programmesana2/prog2_6/prog2_66.html) |
