# Stundu pārstrāde: uzdevumi, laika plāns un koda piemēri

Datums: 2026-08-26

Šis dokuments apraksta izmaiņas, kas veiktas, pārskatot katru mācību stundas lapu pēc trim kritērijiem:

1. **Vai uzdevumi ir skaidri, vērsti uz skolēnu un saprotami skolēnam ar UDS vai vāju lasītprasmi?**
2. **Vai uzdevumi atbilst tēmai, mērķiem un ietilpst 70 minūtēs?**
3. **Vai koda piemērs lapas apakšā ir noderīgs un par stundas grūtāko daļu?**

---

## Kas tika mainīts visās stundās

| Kritērijs | Kā bija | Kā ir tagad |
|---|---|---|
| Uzdevuma virsraksts | `1. uzdevums - Iesildies ar gatavu piemēru` (viens un tas pats 120 lapās) | Nosaukts konkrēts rezultāts, piem. `1. uzdevums - Uzstādi Python un VS Code` |
| Uzdevuma apraksts | "Pievieno šīs stundas paņēmienu kā nelielu projekta daļu" | Viens teikums par to, kas būs gatavs beigās |
| Soļi | Vispārīgi, derīgi jebkurai stundai: "Atrodi vienu drošu vietu, ko drīkst mainīt" | 4-7 soļi, katrs viena darbība ar treknu pavēles darbības vārdu un konkrētu failu, komandu vai vērtību |
| Izvēlnes uzdevumi | "Izvēlies vienu projekta vietu: spēlētāju, pretinieku, kameru, UI..." | Izvēle izdarīta skolēna vietā - nosaukts konkrēts fails un funkcija |
| Gala kritērijs | Nebija | Katram uzdevumam `Gatavs, kad:` ar vienu novērojamu pazīmi |
| Laika plāns | Vispārīgs teksts, vienāds visās lapās; 47 lapās vispār nebija | Konkrēts šīs stundas plāns ar summu 70 min |
| Uzruna | Robotikā "jūs" forma, citur "tu" | Visur "tu" |
| Koda piemērs | Vairākās stundās rādīja vieglāko daļu vai nebija vispār | Rāda stundas grūtāko vietu, ar `result` bloku, kas apraksta gaidāmo rezultātu |

Jauna CSS klase `.done-when` failā `style.css` noformē `Gatavs, kad:` bloku.

---

## Programmēšana I (72 stundas)

Visās 72 stundās pārrakstīti visi četri uzdevumu bloki, pievienots `Gatavs, kad:` kritērijs un konkrēts 70 min plāns. Zemāk katras stundas jaunie uzdevumu nosaukumi un stundai specifiskās izmaiņas.


### 1. tēma - Darba vide un kodu pārvaldība

**[1.1 Datora sagatavošana un IDE](programmesana1/prog1_1/prog1_11.html)**

- 1. uzdevums - Uzstādi Python un VS Code
- 2. uzdevums - Uzraksti un palaid hello.py
- 3. uzdevums - Salauz kodu un iemācies lasīt kļūdu
- Papildu uzdevums - Iekārto ergonomisku darba vietu

> Apakšējais koda piemērs rādīja divus `print` izsaukumus - stundas vieglāko daļu. Aizstāts ar paraugu par to, ko darīt, kad terminālis neatrod Python (`Add Python to PATH`). Pievienots `prism-bash` izcēlējs.

**[1.2 GitHub un Mākoņkrātuve](programmesana1/prog1_1/prog1_12.html)**

- 1. uzdevums - Izveido GitHub kontu
- 2. uzdevums - Izveido pirmo krātuvi un uzstādi GitHub Desktop
- 3. uzdevums - Uzraksti programmu, kas saliek tavu krātuves saiti
- Papildu uzdevums - Papildini savu profilu

**[1.3 Koda sinhronizācija (Desktop)](programmesana1/prog1_1/prog1_13.html)**

- 1. uzdevums - Klonē krātuvi uz datoru
- 2. uzdevums - Izdari izmaiņu, commit un push
- 3. uzdevums - Izlasi Diff un salabo neskaidru commit ziņu
- Papildu uzdevums - Izmēģini Pull

> Salabots neaizvērts `<section>` tags. Pievienots `prism-bash` izcēlējs.

**[1.4 Failu sistēma un organizācija](programmesana1/prog1_1/prog1_14.html)**

- 1. uzdevums - Izveido projekta mapju struktūru
- 2. uzdevums - Uzraksti .gitignore un pārbaudi, ka faili pazūd
- 3. uzdevums - Pārbaudi relatīvos ceļus no apakšmapes
- Papildu uzdevums - Sakārto README pēc struktūras

> Salabots neaizvērts `<section>` tags. Pievienots `prism-bash` izcēlējs.

**[1.5 Dokumentēšana, README un Licences](programmesana1/prog1_1/prog1_15.html)**

- 1. uzdevums - Pievieno MIT licenci
- 2. uzdevums - Uzraksti README ar Markdown
- 3. uzdevums - Pārbaudi, kā README izskatās GitHub, un salabo formatējumu
- Papildu uzdevums - Salīdzini MIT un GPL

**[1.6 Noslēguma pārbaudes darbs - Darba vide un kodu pārvaldība](programmesana1/prog1_1/prog1_16.html)**

- 1. uzdevums - Izveido projekta struktūru un .gitignore
- 2. uzdevums - Uzraksti programmu un README
- 3. uzdevums - Publicē GitHub un pārbaudi pēc kritērijiem
- Papildu uzdevums - Sakārto commit vēsturi

> Teorijas sadaļā bija otrs, pretrunīgs 70 min plāns - noņemts.


### 2. tēma - Python pamati un ievade/izvade

**[2.1 Ievade un datu tipi](programmesana1/prog1_2/prog1_21.html)**

- 1. uzdevums - Izpēti trīs datu tipus ar type()
- 2. uzdevums - Uzraksti varoņa punktu rēķinātāju
- 3. uzdevums - Salauz to ar nepareizu ievadi un izlasi ValueError
- Papildu uzdevums - Pievieno otru varoni

> Uzdevumi atdalīti no 2.2 stundas: šeit tikai datu tipi un `type()`. Salabots neaizvērts `<section>` tags.

**[2.2 Interaktivitāte un konvertācija](programmesana1/prog1_2/prog1_22.html)**

- 1. uzdevums - Parādi, ko dara int() ap input()
- 2. uzdevums - Uzraksti varoņa lapu ar trim ievadēm
- 3. uzdevums - Pārbaudi robežgadījumus un salabo tos
- Papildu uzdevums - Pievieno mērvienības izvadei

> Iepriekš mācīja to pašu, ko 2.1. Tagad fokuss uz vairāku ievažu programmu un robežgadījumiem. Salabots neaizvērts `<section>` tags.

**[2.3 Matemātika un f-strings](programmesana1/prog1_2/prog1_23.html)**

- 1. uzdevums - Izmēģini //, % un **
- 2. uzdevums - Uzraksti inventāra kalkulatoru
- 3. uzdevums - Pārraksti izvadi ar f-string un noapaļo
- Papildu uzdevums - Pievieno kāpināšanu spēles formulā

> Salabots neaizvērts `<section>` tags.

**[2.4 Koda stils un komentāri](programmesana1/prog1_2/prog1_24.html)**

- 1. uzdevums - Pārsauc mainīgos snake_case
- 2. uzdevums - Sakārto kodu pēc PEP 8 un uzraksti jēdzīgus komentārus
- 3. uzdevums - Pārbaudi lasāmību ar klasesbiedru
- Papildu uzdevums - Pārbaudi kodu ar rīku

> Salabots neaizvērts `<section>` tags.

**[2.5 Spēles plānošana](programmesana1/prog1_2/prog1_25.html)**

- 1. uzdevums - Uzraksti spēles pseidokodu
- 2. uzdevums - Definē mainīgos un formulu
- 3. uzdevums - Pārbaudi formulu uz papīra un tad kodā
- Papildu uzdevums - Uzzīmē blokshēmu

> Salabots neaizvērts `<section>` tags.

**[2.6 Noslēguma projekts: "Lielais skaitļu duelītis"](programmesana1/prog1_2/prog1_26.html)**

- 1. uzdevums - Savāc ievadi un konvertē tipus
- 2. uzdevums - Uzraksti formulu un f-string izvadi
- 3. uzdevums - Sakārto stilu un iesniedz GitHub
- Papildu uzdevums - Pievieno otro raundu

> Teorijas sadaļā bija otrs, pretrunīgs 70 min plāns - noņemts.


### 3. tēma - Vadības struktūras un validācija

**[3.1 Zarošanās un operatori](programmesana1/prog1_3/prog1_31.html)**

- 1. uzdevums - Izmēģini salīdzināšanas operatorus
- 2. uzdevums - Uzraksti vecuma pārbaudītāju
- 3. uzdevums - Iztestē visus trīs zarus
- Papildu uzdevums - Pievieno ceturto grupu

> Salabots neaizvērts `<section>` tags.

**[3.2 Loģiskie operatori](programmesana1/prog1_3/prog1_32.html)**

- 1. uzdevums - Izmēģini and, or un not
- 2. uzdevums - Uzraksti lietussarga padomdevēju
- 3. uzdevums - Saīsini ligzdotus if ar loģiskajiem operatoriem
- Papildu uzdevums - Uzraksti paroles pārbaudi

> Salabots neaizvērts `<section>` tags.

**[3.3 While cikli un kontrole](programmesana1/prog1_3/prog1_33.html)**

- 1. uzdevums - Uzraksti skaitītāja ciklu ar while
- 2. uzdevums - Uzbūvē bezgalīgu spēles ciklu ar break
- 3. uzdevums - Pievieno continue un iztestē cikla izeju
- Papildu uzdevums - Pievieno gājienu skaitītāju

> Salabots neaizvērts `<section>` tags.

**[3.4 Kļūdu apstrāde un validācija](programmesana1/prog1_3/prog1_34.html)**

- 1. uzdevums - Noķer ValueError ar try/except
- 2. uzdevums - Uzbūvē drošu ievadi ciklā
- 3. uzdevums - Pievieno vērtību validāciju un iztestē
- Papildu uzdevums - Ierobežo mēģinājumu skaitu

> Uzdevumos mainīgais bija gan `vecums`, gan `likme`; saskaņots ar stundas koda piemēru uz `likme`. Salabots neaizvērts `<section>` tags.

**[3.5 Saraksti un For cikli](programmesana1/prog1_3/prog1_35.html)**

- 1. uzdevums - Izveido sarakstu un izdrukā to ar for
- 2. uzdevums - Uzbūvē klases materiālu inventāru
- 3. uzdevums - Pārbaudi elementus ar in un iztestē tukšu sarakstu
- Papildu uzdevums - Pievieno numerāciju izvadē

> Salabots neaizvērts `<section>` tags.

**[3.6 Noslēguma projekts: "Gudrais Akmens-Šķēres-Papīrīts"](programmesana1/prog1_3/prog1_36.html)**

- 1. uzdevums - Uzbūvē spēles kodolu ar random
- 2. uzdevums - Pievieno tiesnesi ar if/elif/else
- 3. uzdevums - Pievieno ciklu, validāciju un iesniedz GitHub
- Papildu uzdevums - Pievieno rezultātu tabulu

> Teorijas sadaļā bija otrs, pretrunīgs 70 min plāns - noņemts.


### 4. tēma - Funkcijas un modularitāte

**[4.1 Funkciju definēšana un parametri](programmesana1/prog1_4/prog1_41.html)**

- 1. uzdevums - Uzraksti pirmo funkciju bez parametriem
- 2. uzdevums - Pievieno parametrus punktu rēķinātājam
- 3. uzdevums - Izsauc funkciju vairākas reizes ar dažādiem datiem
- Papildu uzdevums - Pievieno noklusējuma vērtību

> Salabots neaizvērts `<section>` tags.

**[4.2 Vērtību atgriešana (return)](programmesana1/prog1_4/prog1_42.html)**

- 1. uzdevums - Salīdzini print un return
- 2. uzdevums - Uzraksti bonusa funkciju ar return
- 3. uzdevums - Saliec divas funkcijas kopā vienā aprēķinā
- Papildu uzdevums - Atgriez divas vērtības

> Salabots neaizvērts `<section>` tags.

**[4.3 Modularitāte un koda sadalīšana](programmesana1/prog1_4/prog1_43.html)**

- 1. uzdevums - Sadali kodu divos failos
- 2. uzdevums - Importē moduli un izsauc tā funkcijas
- 3. uzdevums - Salīdzini import un from import
- Papildu uzdevums - Pievieno trešo moduli

> Salabots neaizvērts `<section>` tags.

**[4.4 Lokālie/globālie mainīgie un vārdnīcas](programmesana1/prog1_4/prog1_44.html)**

- 1. uzdevums - Pārbaudi, kur mainīgais ir redzams
- 2. uzdevums - Izveido spēlētāja vārdnīcu
- 3. uzdevums - Maini vārdnīcu no funkcijas iekšpuses
- Papildu uzdevums - Ieliec sarakstu vārdnīcā

> Salabots neaizvērts `<section>` tags.

**[4.5 Spēles plānošana ar shēmām](programmesana1/prog1_4/prog1_45.html)**

- 1. uzdevums - Uzzīmē skaitļu minētāja shēmu
- 2. uzdevums - Pārvērs shēmu funkcijās
- 3. uzdevums - Salīdzini shēmu ar kodu un salabo neatbilstības
- Papildu uzdevums - Pievieno mēģinājumu ierobežojumu

**[4.6 Noslēguma projekts: Skaitļu minētājs](programmesana1/prog1_4/prog1_46.html)**

- 1. uzdevums - Uzraksti salidzina() funkciju
- 2. uzdevums - Saliec spēles ciklu ar mājieniem
- 3. uzdevums - Pievieno mēģinājumu skaitu un iesniedz GitHub
- Papildu uzdevums - Pasargā spēli no burtiem

> Teorijas sadaļā bija otrs, pretrunīgs 70 min plāns - noņemts.


### 5. tēma - Datu struktūras

**[5.1 Saraksti](programmesana1/prog1_5/prog1_51.html)**

- 1. uzdevums - Izmēģini len, append un insert
- 2. uzdevums - Uzbūvē materiālu kasti ar pop
- 3. uzdevums - Iztestē indeksu robežas
- Papildu uzdevums - Sakārto sarakstu

**[5.2 Vārdnīcas](programmesana1/prog1_5/prog1_52.html)**

- 1. uzdevums - Izveido un maini vārdnīcu
- 2. uzdevums - Uzbūvē spēlētāja profilu ar sarakstu iekšā
- 3. uzdevums - Pasargā kodu no KeyError
- Papildu uzdevums - Izveido vārdnīcu vārdnīcā

**[5.3 For cikli](programmesana1/prog1_5/prog1_53.html)**

- 1. uzdevums - Izej cauri sarakstam ar for
- 2. uzdevums - Izdrukā vārdnīcu ar .items()
- 3. uzdevums - Saskaiti un filtrē ciklā
- Papildu uzdevums - Pievieno enumerate

**[5.4 Aptaujas izveide](programmesana1/prog1_5/prog1_54.html)**

- 1. uzdevums - Uzraksti aptaujas jautājumus
- 2. uzdevums - Izveido aptauju digitālā rīkā
- 3. uzdevums - Savāc atbildes un ievieto tās Python struktūrās
- Papildu uzdevums - Izrēķini procentus

**[5.5 Analīze un integrācija](programmesana1/prog1_5/prog1_55.html)**

- 1. uzdevums - Atlasi derīgās atbildes
- 2. uzdevums - Uzraksti veikala izvadi ar enumerate
- 3. uzdevums - Savieno aptaujas datus ar spēli
- Papildu uzdevums - Atrodi populārāko vārdu

**[5.6 Noslēguma projekts: Atmiņu kāršu spēle](programmesana1/prog1_5/prog1_56.html)**

- 1. uzdevums - Izveido klāju un spēles stāvokli
- 2. uzdevums - Uzraksti divu kāršu atvēršanu
- 3. uzdevums - Pievieno pāru pārbaudi un iesniedz GitHub
- Papildu uzdevums - Palielini klāju līdz 4x4

> Teorijas sadaļā bija otrs, pretrunīgs 70 min plāns - noņemts. Pamatdarbs sākas ar 2x2 klāju, 4x4 pārcelts uz papildu uzdevumu, lai ietilptu 70 minūtēs.


### 6. tēma - Faili un dati

**[6.1 Failu I/O](programmesana1/prog1_6/prog1_61.html)**

- 1. uzdevums - Ieraksti un nolasi teksta failu
- 2. uzdevums - Salīdzini režīmus w un a
- 3. uzdevums - Saglabā spēles datus JSON formātā
- Papildu uzdevums - Nolasi failu pa rindām

**[6.2 Digitālais rīks](programmesana1/prog1_6/prog1_62.html)**

- 1. uzdevums - Izveido stāsta tabulu izklājlapā
- 2. uzdevums - Eksportē to par CSV un nolasi ar DictReader
- 3. uzdevums - Pārbaudi, vai visas saites ved uz esošām lokācijām
- Papildu uzdevums - Pievieno otro izvēli

**[6.3 Datu transformācija](programmesana1/prog1_6/prog1_63.html)**

- 1. uzdevums - Notīri datus ar strip un int
- 2. uzdevums - Pārvērs CSV rindas par vārdnīcu pēc id
- 3. uzdevums - Salīdzini meklēšanu sarakstā un vārdnīcā
- Papildu uzdevums - Pasargā no bojātas rindas

**[6.4 Rezultātu tabulas](programmesana1/prog1_6/prog1_64.html)**

- 1. uzdevums - Nolasi JSON un apstrādā trūkstošu failu
- 2. uzdevums - Pievieno jaunu rezultātu un saglabā
- 3. uzdevums - Sakārto un parādi TOP 5
- Papildu uzdevums - Neļauj dublētiem vārdiem

**[6.5 Analīze un Vizualizācija](programmesana1/prog1_6/prog1_65.html)**

- 1. uzdevums - Izrēķini summu, vidējo un biežumu
- 2. uzdevums - Uzzīmē stabiņu diagrammu ar simboliem
- 3. uzdevums - Izdari secinājumu par datiem
- Papildu uzdevums - Sakārto diagrammu pēc lieluma

**[6.6 Noslēguma projekts: Quiz spēle ar Highscore](programmesana1/prog1_6/prog1_66.html)**

- 1. uzdevums - Ielādē jautājumus no JSON
- 2. uzdevums - Uzraksti spēles ciklu ar punktiem
- 3. uzdevums - Saglabā rezultātu CSV un parādi TOP 5
- Papildu uzdevums - Pievieno kategorijas

> Teorijas sadaļā bija otrs, pretrunīgs 70 min plāns - noņemts.


### 7. tēma - Algoritmi un to efektivitāte

**[7.1 Meklēšanas pamati](programmesana1/prog1_7/prog1_71.html)**

- 1. uzdevums - Uzraksti lineāro meklēšanu
- 2. uzdevums - Uzraksti bināro meklēšanu sakārtotā sarakstā
- 3. uzdevums - Saskaiti soļus abiem un salīdzini
- Papildu uzdevums - Izmēģini iebūvēto index()

> Trīs koda piemēri, izkaisīti starp uzdevumiem, aizstāti ar vienu apakšējo piemēru par binārās meklēšanas robežām (`+1`/`-1`, `<=`) - tieši tur skolēni iestrēgst bezgalīgā ciklā.

**[7.2 Kārtošanas loģika](programmesana1/prog1_7/prog1_72.html)**

- 1. uzdevums - Samaini divus elementus vietām
- 2. uzdevums - Uzraksti burbuļa pirmo gājienu
- 3. uzdevums - Pabeidz pilnu Bubble Sort
- Papildu uzdevums - Apturi kārtošanu agrāk

> Koda piemēri konsolidēti vienā apakšējā piemērā par ligzdotiem cikliem un apmaiņu bez pagaidu mainīgā.

**[7.3 Big O un Sarežģītība](programmesana1/prog1_7/prog1_73.html)**

- 1. uzdevums - Izmēri O(1) darbību
- 2. uzdevums - Salīdzini O(n) ar O(n kvadrātā)
- 3. uzdevums - Nosaki sarežģītību svešam kodam
- Papildu uzdevums - Atrodi O(log n)

> Koda piemēri konsolidēti vienā apakšējā piemērā, kas mēra O(n) pret O(n²) un uzsver, ka svarīgs ir laika pieauguma koeficients, nevis sekundes.

**[7.4 Iebūvēto funkciju ātrums](programmesana1/prog1_7/prog1_74.html)**

- 1. uzdevums - Atrodi min un max ar iebūvētajām funkcijām
- 2. uzdevums - Salīdzini iebūvēto sum() ar savu ciklu
- 3. uzdevums - Izmēri abus ar time un izdari secinājumu
- Papildu uzdevums - Pārbaudi arī len() un sorted()

> **Stunda pārstrādāta, jo tā dublēja 7.5.** Tagad fokuss tikai uz pašrakstītu ciklu pret iebūvēto funkciju (`min`/`max`/`sum`), abi O(n).

**[7.5 Iebūvēto funkciju efektivitāte](programmesana1/prog1_7/prog1_75.html)**

- 1. uzdevums - Salīdzini sorted() ar savu bubble_sort
- 2. uzdevums - Izmēri 'in' sarakstā pret kopu
- 3. uzdevums - Izvēlies pareizo struktūru un pamato izvēli
- Papildu uzdevums - Pārbaudi arī vārdnīcu

> **Stunda bija gandrīz identiska 7.4** - vienāds teorijas virsraksts un vienādi uzdevumu nosaukumi. Teorija pārsaukta uz "Pareizā funkcija un pareizā datu struktūra" un papildināta; uzdevumi tagad par datu struktūras izvēli: `in` sarakstā (O(n)) pret kopu (O(1)). Iepriekš bija hibrīds - trīs konkrēti uzdevumi un viens vispārīgs papildu uzdevums ar sagataves soļiem.

**[7.6 Noslēguma projekts: "Koda lauzējs: AI Efektivitāte"](programmesana1/prog1_7/prog1_76.html)**

- 1. uzdevums - Uzraksti datora minēšanas robežas
- 2. uzdevums - Pabeidz binārās meklēšanas AI
- 3. uzdevums - Saskaiti minējumus un salīdzini ar lineāro
- Papildu uzdevums - Pamani krāpšanos


### 8. tēma - Projektēšana un plānošana

**[8.1 Problēmas formulēšana un automatizācija](programmesana1/prog1_8/prog1_81.html)**

- 1. uzdevums - Atrodi trīs rutīnas darbības
- 2. uzdevums - Uzraksti 'pirms un pēc' salīdzinājumu
- 3. uzdevums - Noformē problēmas ziņojumu
- Papildu uzdevums - Novērtē automatizācijas ieguvumu

> Nebija neviena koda piemēra - pievienots Markdown paraugs, kas pretstata vāju un spēcīgu problēmas formulējumu. Pievienoti `prism-python` un `prism-markdown` izcēlēji.

**[8.2 Prasību specifikācija - Lietotāju stāsti](programmesana1/prog1_8/prog1_82.html)**

- 1. uzdevums - Uzraksti trīs lietotāju stāstus
- 2. uzdevums - Pievieno akceptēšanas kritērijus
- 3. uzdevums - Sakārto backlog pēc prioritātes
- Papildu uzdevums - Uzraksti pretstāstu

> Nebija neviena koda piemēra - pievienots paraugs, kas pretstata pārbaudāmus un nepārbaudāmus akceptēšanas kritērijus. Pievienoti `prism-python` un `prism-markdown` izcēlēji.

**[8.3 Datu modelis un UI plūsma](programmesana1/prog1_8/prog1_83.html)**

- 1. uzdevums - Uzzīmē ER diagrammu ar divām būtībām
- 2. uzdevums - Uzzīmē UI plūsmu
- 3. uzdevums - Pārbaudi, vai plūsma sasaucas ar datiem
- Papildu uzdevums - Pievieno trešo būtību

> Uzdevumi bija pilnīgi vispārīgi ("Izpēti pamatus", "Izveido risinājumu", "Pārbaudi un uzlabo") - pārrakstīti par ER diagrammas un UI plūsmas zīmēšanu.

**[8.4 Prezentācijas māksla - Pitch sagatavošana](programmesana1/prog1_8/prog1_84.html)**

- 1. uzdevums - Uzraksti lifta runu
- 2. uzdevums - Saplāno piecus slaidus
- 3. uzdevums - Iztestē prezentāciju uz laiku
- Papildu uzdevums - Sagatavo atbildes uz jautājumiem

> Pievienots `prism-markdown` izcēlējs.

**[8.5 Sasniedzamie rezultāti un resursu plānošana](programmesana1/prog1_8/prog1_85.html)**

- 1. uzdevums - Nospraud trīs starprezultātus
- 2. uzdevums - Veic resursu auditu
- 3. uzdevums - Uzraksti laika grafiku un riskus
- Papildu uzdevums - Uzraksti Definition of Done

> Pievienots `prism-python` izcēlējs.

**[8.6 Noslēguma projekts: Projektējuma aizstāvēšana](programmesana1/prog1_8/prog1_86.html)**

- 1. uzdevums - Savāc projektējuma mapi kopā
- 2. uzdevums - Sasaisti prasību ar tehnisku izvēli
- 3. uzdevums - Aizstāvi projektējumu un pieraksti piezīmes
- Papildu uzdevums - Novērtē klasesbiedra projektējumu

> Uzdevumi bija pilnīgi vispārīgi - pārrakstīti par projektējuma mapes savākšanu un aizstāvēšanu. Teorijas sadaļā bija otrs 70 min plāns - noņemts. Pievienots `prism-markdown` izcēlējs.


### 9. tēma - Web integrācija un bibliotēkas

**[9.1 Ārējās bibliotēkas un instalēšana](programmesana1/prog1_9/prog1_91.html)**

- 1. uzdevums - Izveido virtuālo vidi un instalē bibliotēku
- 2. uzdevums - Izsauc reālu API ar requests
- 3. uzdevums - Saglabā atkarības requirements.txt
- Papildu uzdevums - Pievieno otru bibliotēku

**[9.2 Atvērtā koda licences un dokumentācija](programmesana1/prog1_9/prog1_92.html)**

- 1. uzdevums - Noskaidro savu bibliotēku licences
- 2. uzdevums - Atrodi atbildi oficiālajā dokumentācijā
- 3. uzdevums - Noformē README ar licenci un atkarībām
- Papildu uzdevums - Salīdzini divas licences

**[9.3 Python pārvēršana tīmekļa saskarnē](programmesana1/prog1_9/prog1_93.html)**

- 1. uzdevums - Palaid pirmo Streamlit lapu
- 2. uzdevums - Pievieno ievades elementus un pogu
- 3. uzdevums - Pārcel savu Python spēli uz saskarni
- Papildu uzdevums - Pievieno sānjoslu

**[9.4 HTML un Python sasaiste](programmesana1/prog1_9/prog1_94.html)**

- 1. uzdevums - Ieliec savu HTML Streamlit lapā
- 2. uzdevums - Uzraksti CSS kartiņu stilu
- 3. uzdevums - Saliec divu kolonnu izkārtojumu
- Papildu uzdevums - Pievieno lapas ikonu un nosaukumu

**[9.5 Interaktivitāte pārlūkprogrammā](programmesana1/prog1_9/prog1_95.html)**

- 1. uzdevums - Saglabā skaitītāju ar session_state
- 2. uzdevums - Uzbūvē To-Do sarakstu ar formu
- 3. uzdevums - Pievieno dzēšanu un notīrīšanu
- Papildu uzdevums - Pievieno atzīmi par izpildi

**[9.6 Noslēguma projekts: "Krustiņi un nullītes" pārlūkā](programmesana1/prog1_9/prog1_96.html)**

- 1. uzdevums - Uzzīmē 3x3 laukumu ar pogām
- 2. uzdevums - Pievieno gājienus un uzvaras pārbaudi
- 3. uzdevums - Pievieno statistiku un restartu
- Papildu uzdevums - Pievieno vienkāršu AI


### 10. tēma - Datubāzes

**[10.1 Ievads datubāzēs un PostgreSQL](programmesana1/prog1_10/prog1_101.html)**

- 1. uzdevums - Izveido datubāzi un pieslēdzies
- 2. uzdevums - Uzraksti pirmo CREATE TABLE
- 3. uzdevums - Pārbaudi datu tipu ierobežojumus
- Papildu uzdevums - Pievieno CHECK ierobežojumu

> Pievienots `prism-bash` izcēlējs.

**[10.2 SQL CRUD: SELECT, INSERT, UPDATE, DELETE](programmesana1/prog1_10/prog1_102.html)**

- 1. uzdevums - Ievadi datus ar INSERT
- 2. uzdevums - Filtrē un kārto ar SELECT
- 3. uzdevums - Droši lieto UPDATE un DELETE
- Papildu uzdevums - Izmēģini transakciju

**[10.3 Tabulu projektēšana un saites](programmesana1/prog1_10/prog1_103.html)**

- 1. uzdevums - Izveido otro tabulu ar ārējo atslēgu
- 2. uzdevums - Pārbaudi, ko dara ārējā atslēga
- 3. uzdevums - Novērs datu dublēšanos
- Papildu uzdevums - Pievieno trešo tabulu

**[10.4 JOIN un sarežģīti vaicājumi](programmesana1/prog1_10/prog1_104.html)**

- 1. uzdevums - Savieno tabulas ar INNER JOIN
- 2. uzdevums - Salīdzini INNER un LEFT JOIN
- 3. uzdevums - Izveido TOP sarakstu ar GROUP BY
- Papildu uzdevums - Filtrē grupas ar HAVING

**[10.5 Python ↔ PostgreSQL (psycopg2)](programmesana1/prog1_10/prog1_105.html)**

- 1. uzdevums - Pieslēdzies datubāzei no Python
- 2. uzdevums - Ievadi un nolasi datus ar parametriem
- 3. uzdevums - Pārbaudi, kāpēc %s ir obligāts
- Papildu uzdevums - Lieto with un RealDictCursor

> Pievienots `prism-bash` izcēlējs.

**[10.6 Noslēguma projekts: Highscore datubāze](programmesana1/prog1_10/prog1_106.html)**

- 1. uzdevums - Izveido trīs tabulu shēmu
- 2. uzdevums - Uzraksti Python funkcijas rezultātu pievienošanai
- 3. uzdevums - Izveido TOP sarakstu un statistiku
- Papildu uzdevums - Filtrē pēc datumu intervāla


### 11. tēma - Objektorientētā programmēšana

**[11.1 Klases un objekti](programmesana1/prog1_11/prog1_111.html)**

- 1. uzdevums - Izveido pirmo klasi un divus objektus
- 2. uzdevums - Pievieno atribūtus katram objektam
- 3. uzdevums - Salīdzini klases un objekta atribūtus
- Papildu uzdevums - Saskaiti izveidotos objektus

**[11.2 Konstruktori un atribūti](programmesana1/prog1_11/prog1_112.html)**

- 1. uzdevums - Pārraksti klasi ar __init__
- 2. uzdevums - Pievieno noklusējuma vērtības
- 3. uzdevums - Pārbaudi datus konstruktorā
- Papildu uzdevums - Pievieno izveides laiku

**[11.3 Metodes un self](programmesana1/prog1_11/prog1_113.html)**

- 1. uzdevums - Uzraksti pirmo metodi ar self
- 2. uzdevums - Liec metodei mainīt objekta stāvokli
- 3. uzdevums - Pievieno metodi, kas atgriež atbildi
- Papildu uzdevums - Pievieno atjaunošanās metodi

**[11.4 Mantošana un super()](programmesana1/prog1_11/prog1_114.html)**

- 1. uzdevums - Izveido bērna klasi
- 2. uzdevums - Izsauc vecāku konstruktoru ar super()
- 3. uzdevums - Pievieno bērnam savu metodi
- Papildu uzdevums - Pievieno trešo lomu

**[11.5 Polimorfisms un dunder metodes](programmesana1/prog1_11/prog1_115.html)**

- 1. uzdevums - Pārraksti vienu metodi vairākās klasēs
- 2. uzdevums - Izsauc tās vienā ciklā
- 3. uzdevums - Pievieno __str__ un __repr__
- Papildu uzdevums - Pievieno salīdzināšanu

**[11.6 Noslēguma projekts: Klases turnīra simulators](programmesana1/prog1_11/prog1_116.html)**

- 1. uzdevums - Uzbūvē bāzes klasi un divas lomas
- 2. uzdevums - Pievieno šķēršļus un polimorfismu
- 3. uzdevums - Palaid turnīra ciklu un statistiku
- Papildu uzdevums - Pievieno turnīra žurnālu


### 12. tēma - Web izstrāde

**[12.1 Front-end un back-end arhitektūra](programmesana1/prog1_12/prog1_121.html)**

- 1. uzdevums - Izseko īstam HTTP pieprasījumam
- 2. uzdevums - Uzzīmē savas lietotnes arhitektūru
- 3. uzdevums - Sadali funkcijas starp priekšgalu un aizmuguri
- Papildu uzdevums - Salīdzini statusa kodus

**[12.2 Flask: Python kā web serveris](programmesana1/prog1_12/prog1_122.html)**

- 1. uzdevums - Palaid pirmo Flask serveri
- 2. uzdevums - Atgriez JSON no maršruta
- 3. uzdevums - Pieņem datus ar POST
- Papildu uzdevums - Pievieno maršrutu ar parametru

**[12.3 REST API izstrāde](programmesana1/prog1_12/prog1_123.html)**

- 1. uzdevums - Uzbūvē GET un POST pēc REST
- 2. uzdevums - Pievieno validāciju un pareizus statusa kodus
- 3. uzdevums - Pievieno filtrēšanu un kārtošanu
- Papildu uzdevums - Pievieno DELETE

**[12.4 Front-end + API integrācija](programmesana1/prog1_12/prog1_124.html)**

- 1. uzdevums - Izsauc savu API ar fetch
- 2. uzdevums - Parādi datus tabulā
- 3. uzdevums - Nosūti formu ar POST
- Papildu uzdevums - Atrisini CORS kļūdu

**[12.5 Izvietošana mākonī un drošība](programmesana1/prog1_12/prog1_125.html)**

- 1. uzdevums - Izņem noslēpumus no koda
- 2. uzdevums - Sagatavo projektu izvietošanai
- 3. uzdevums - Izvieto mākonī un pārbaudi
- Papildu uzdevums - Pievieno pieprasījumu ierobežojumu

**[12.6 Noslēguma projekts: Daudzspēlētāju Krustiņi un nullītes](programmesana1/prog1_12/prog1_126.html)**

- 1. uzdevums - Uzraksti spēles klasi ar uzvaras pārbaudi
- 2. uzdevums - Pievieno API gājieniem un stāvoklim
- 3. uzdevums - Savieno pārlūku un izvieto mākonī
- Papildu uzdevums - Saglabā partijas datubāzē

---

## Robotika 7. klase (10 stundas)

Šis kurss atšķīrās ar to, ka uzdevumi jau bija konkrēti, bet visa uzruna bija "jūs" formā, un astoņās stundās bija 4 numurēti uzdevumi pret 3 uzdevumu laika budžetu. Ceturtais uzdevums pārsaukts par "Papildu uzdevums".

**[1.1 Ievads LEGO SPIKE un robota pamatkustības](robotika/rbtk7_11.html)**

- 1. uzdevums - Uzbūvē braukšanas bāzi un palaid pirmos 20 cm
- 2. uzdevums - Nobrauc precīzus 50 cm turp un atpakaļ
- 3. uzdevums - Izbrauc kvadrātu ar repeat ciklu
- Papildu uzdevums - Izbrauc astoņnieka trajektoriju

> Uzdevumi pārrakstīti jau iepriekš (Vienkāršošana); šoreiz saskaņota uzruna un formatējums.

**[1.2 Distances sensors un izvairīšanās no šķēršļiem](robotika/rbtk7_12.html)**

- 1. uzdevums - Pieliec distances sensoru un nolasi attālumu ekrānā
- 2. uzdevums - Liec robotam apstāties 10 cm pirms sienas
- 3. uzdevums - Liec robotam bezgalīgi apbraukt šķēršļus
- Papildu uzdevums - Notur 15 cm distanci no rokas

> Sadaļā "Biežākās kļūdas" bija palikusi "jūs" forma - pārrakstīta. Salabota drukas kļūda "borts" -> "ports".

**[1.3 Krāsu sensors un līniju sekotājs](robotika/rbtk7_13.html)**

- 1. uzdevums - Apstādini robotu uz sarkanas krāsas
- 2. uzdevums - Uzraksti divu stāvokļu līniju sekotāju
- 3. uzdevums - Noregulē slieksni un ātrumu uz reālās trases
- Papildu uzdevums - Saskaiti zaļos krustojumus

> **1. uzdevums bija palicis bez virsraksta** - tā vietā bija `<h3>Izpildes soļi:</h3>`. Koda piemērs pārtaisīts par sliekšņa izrēķināšanu (vidējais starp melnās un baltās virsmas rādījumu) - tieši tur skolēni iestrēgst. Pievienots `prism-python` izcēlējs.

**[1.4 Manipulatori (Satvērējs)](robotika/rbtk7_14.html)**

- 1. uzdevums - Uzbūvē satvērēju uz trešā motora
- 2. uzdevums - Atver un aizver spīles ar Hub pogām
- 3. uzdevums - Izpildi autonomo piegādes misiju
- Papildu uzdevums - "Sargātāja" režīms ar diviem sensoriem

> Koda piemērs pārorientēts uz satveršanu ar laiku, nevis grādiem - ar grādiem motors iesprūst un programma apstājas uz visiem laikiem. Pievienots `prism-python` izcēlējs.

**[1.5 Noslēguma projekts: Pārbaudes misija](robotika/rbtk7_15.html)**

- 1. uzdevums - Pārbaudi, vai bāze brauc atkārtojami
- 2. uzdevums - Liec robotam apstāties pēc sensora
- 3. uzdevums - Salien visu vienā misijā un nodemonstrē
- Papildu uzdevums - Adaptīva misija

> **Sensori bija piešķirti portiem A un B, kas jau ir dzenošie motori** - nomainīts uz E un F. Nebija apakšējā koda piemēra - pievienots par sākuma stāvokļa atgriešanu (bez tās misija strādā tikai vienu reizi).

**[2.1 Ievads Arduino un Tinkercad](robotika/rbtk7_21.html)**

- 1. uzdevums - Saliec Tinkercad shēmu ar strāvas padevi
- 2. uzdevums - Pieslēdz LED un iededz to nepārtraukti
- 3. uzdevums - Liec diodei mirgot ar delay
- Papildu uzdevums - Policijas bākugunis ar mainīgo

> **Ielādēja tikai `prism-powershell`, lai gan viss kods ir C++** - nomainīts uz `prism-cpp`. Koda piemērs pārtaisīts par saikni starp pina numuru kodā un vadu shēmā.

**[2.2 Pogas un If-Else loģika](robotika/rbtk7_22.html)**

- 1. uzdevums - Saliec shēmu ar pogu un LED
- 2. uzdevums - Izdrukā pogas stāvokli Serial Monitor
- 3. uzdevums - Liec pogai ieslēgt diodi ar if-else
- Papildu uzdevums - "Reversais" luksofors

> **Aiz `</html>` bija lieks `<!DOCTYPE html>`** - noņemts. Izcēlējs nomainīts uz `prism-cpp`. Koda piemērs papildināts ar abām biežākajām kļūmēm: `INPUT_PULLUP` trūkums un `=` pret `==`.

**[2.3 Analogie signāli (Potenciometrs)](robotika/rbtk7_23.html)**

- 1. uzdevums - Pieslēdz potenciometra trīs kājas
- 2. uzdevums - Izdrukā vērtības 0-1023 Serial Monitor
- 3. uzdevums - Regulē LED spilgtumu ar kloķi
- Papildu uzdevums - Instrumentu panelis ar sliekšņiem

> Izcēlējs nomainīts uz `prism-cpp`. Koda piemērs pārorientēts uz 0-1023 pārvēršanu par 0-255 un tildes (~) portu prasību.

**[2.4 Servo motors](robotika/rbtk7_24.html)**

- 1. uzdevums - Pieslēdz servo motora trīs vadus
- 2. uzdevums - Liec motoram griezties pa trim leņķiem
- 3. uzdevums - Vadi motora leņķi ar potenciometru
- Papildu uzdevums - Motora vadība ar divām pogām

> **C++ mainīgais saucās `kloķis` - ar diakritiku, ko kompilators nepieņem** - nomainīts uz `klokis`, un par to pievienota jauna rindiņa sadaļā "Biežākās kļūdas". Izcēlējs nomainīts uz `prism-cpp`.

**[2.5 Noslēguma projekts: Reakcijas spēle](robotika/rbtk7_25.html)**

- 1. uzdevums - Saslēdz shēmu un nodefinē mainīgos
- 2. uzdevums - Uzraksti spēles loģiku ar millis()
- 3. uzdevums - Pievieno 3 raundus, vidējo un false start
- Papildu uzdevums - Skaņas signāls

> **`const int` mainīgie bija liekami `setup()` iekšpusē, kur `loop()` tos neredz** - pārcelti virs `setup()`. Stundā nebija neviena numurēta uzdevuma (bija "1. solis", "2. solis") un nebija apakšējā koda piemēra - pievienots par sākuma stāvokļa atgriešanu un false start noteikšanu. Izcēlējs nomainīts uz `prism-cpp`.


---

## Vietnes mēroga labojumi

**Neaizvērts `<section>` tags 17 Programmēšanas I stundās.** Teorijas sadaļa netika aizvērta pirms sadaļas "Praktiskie uzdevumi", tāpēc sekcijas ligzdojās viena otrā. Kļūda bija abos zaros (gan 1.1, gan Vienkāršošana), tātad nav radusies apvienošanas laikā. Skartās stundas: 1.3-1.5, 2.1-2.5, 3.1-3.5, 4.1-4.4.

**Neizcelti koda bloki 18 lapās.** Lapas lietoja `language-` klases, kurām nebija ielādēts attiecīgais Prism komponents (`bash`, `markdown`, `python`, `json`, `powershell`, `cpp`), tāpēc tie koda bloki tika rādīti kā pelēks teksts. Tagad katrai lietotajai valodai ir ielādēts izcēlējs; pārbaude aptver visas 185 vietnes HTML lapas.

**Dublēti 70 min plāni.** Sešās stundās teorijas sadaļā bija iestrādāts otrs laika plāns, kas neatbilda lapas augšā norādītajam. Saglabāts tikai augšējais.

**Jauna CSS klase.** `style.css` pievienota `.done-when` klase (mala kreisajā pusē, izcelts fons), kas noformē katra uzdevuma gala kritēriju.


---

## Zaru apvienošana (1.1 un Vienkāršošana)

Pirms satura darba tika atrisināta zaru novirze: vietējais `main` (commit "Vienkāršošana") un `origin/main` ("1.1") bija atšķīrušies un konfliktēja 33 failos.

Abi zari darīja dažādas lietas:

- **1.1** - plaša formatējuma kārta pār 185 failiem: em-domuzīmes nomaiņa pret defisi, `Tavs šīs stundas izaicinājums:` -> `Stundas uzdevums:`, uzdevumu ietveršana vienā sadaļā.
- **Vienkāršošana** - dziļa satura pārstrāde 34 stundās (visa 9. klases datorika un robotikas 1.1-1.2) ar konkrētiem uzdevumiem un `Gatavs, kad:` kritērijiem.

Tiešs `-X theirs` (1.1 uzvar katrā konfliktā) būtu atgriezis ~25 stundas uz vispārīgo sagatavi, atstājot vispārīgus uzdevumu virsrakstus virs konkrētiem `Gatavs, kad:` kritērijiem - sliktāku rezultātu nekā jebkurš no zariem atsevišķi.

Tāpēc apvienošana veikta ar `-X ours` (saglabājot stundu saturu), un pēc tam 1.1 konvencijas uzliktas atsevišķi. Rezultāts sakrīt ar 1.1 konvencijām precīzi - **0 em-domuzīmju** un **149 faili ar `Stundas uzdevums:`**, tieši tāpat kā `origin/main` - vienlaikus saglabājot visu Vienkāršošanas saturu.

Drošības zars pirms apvienošanas: `backup/vienkarsosana-pirms-merge`.


---

## Programmēšana II (36 stundas)

Šim kursam bija atsevišķas prasības, tāpēc tas atšķiras no pārējiem:

| Prasība | Kā risināts |
|---|---|
| **80 min stundas**, nevis 70 | Katrā stundā plāns 10 + 20 + 25 + 20 + 5 min. Pēdējās 5 minūtes atvēlētas darba iesniegšanai. |
| Skolēni atceras **Programmēšanas I 1.-6. tēmu** | Uzdevumi tieši atsaucas uz Python sarakstiem, vārdnīcām, cikliem un failu darbu un rāda C++ variantu kā to pašu citā pierakstā. |
| **Nekādu Godot priekšzināšanu** | 1.1 sākas ar lejupielādi un editora piecu daļu apskatu. Soļos nosaukta katra izvēlne un poga. |
| Valoda **piemērota, bet pārvaldāma skolēnam ar UDS** | Viens solis - viena darbība. Katram uzdevumam viens nosaukts rezultāts un pārbaudāms `Gatavs, kad:`. Nav izvēlņu tipa uzdevumu. |
| **Skaidrs stundas gala mērķis, ko iesniedz skolotājam** | Katras stundas beigās jauna sadaļa **Ko iesniedz skolotājam**: stundas mērķis vienā teikumā, numurēts iesniedzamo darbu saraksts un iesniegšanas veids. |

> **Piezīme par priekšzināšanām.** Kursa 3. tēma māca objektorientēto programmēšanu. Programmēšanas I OOP ir 11. tēmā, tātad **ārpus** tā, ko šie skolēni atceras. Tāpēc 3.1 nesāk ar pieņēmumu, ka klases ir pazīstamas: pirmais solis ir uzrakstīt Python vārdnīcu un tai blakus to pašu kā C++ klasi.

> **Piezīme par kursa grūtumu.** Kurss lieto Godot 4 ar C++ GDExtension, kas prasa kompilatoru un SCons build vidi. Tas ir ievērojami stāvāks slīpums nekā Python. Uzdevumos tas ņemts vērā: 1.3 (build vides uzstādīšana) ir atzīmēta kā tēmas tehniski grūtākā stunda, tajā norādīts, ka ilga kompilēšana ir normāla, un **pats kļūdas teksts ir iesniedzams darbs**, lai stunda nebeigtos ar tukšu rezultātu, ja uzstādīšana neizdodas.


### 1. tēma - Ievads Godot un C++

**[1.1 Godot instalācija un projekta sagatavošana](programmesana2/prog2_1/prog2_11.html)**

- 1. uzdevums - Uzstādi Godot un izveido Pong projektu
- 2. uzdevums - Atrodi piecas editora daļas
- 3. uzdevums - Iestati logu un saglabā projektu Git
- Papildu uzdevums - Saglabā savu editora izkārtojumu

> **Iesniedz:** Tev ir uzstādīts Godot 4 un izveidots tukšs Pong projekts pareizā loga izmērā, kas saglabāts GitHub krātuvē, un tu proti nosaukt piecas editora galvenās daļas.

**[1.2 Scene Tree un Node sistēma](programmesana2/prog2_1/prog2_12.html)**

- 1. uzdevums - Izveido pirmo scēnu ar trim mezgliem
- 2. uzdevums - Saliec Pong laukuma koku
- 3. uzdevums - Saglabā paddle kā atsevišķu scēnu
- Papildu uzdevums - Sakārto koku pēc atbildības

> **Iesniedz:** Tev ir saglabāta Pong scēna main.tscn, kurā objekti sakārtoti saprotamā Node kokā, un viens paddle ir izveidots kā atkārtoti lietojama scēna paddle.tscn.

**[1.3 C++ un GDExtension sagatavošana](programmesana2/prog2_1/prog2_13.html)**

- 1. uzdevums - Uzstādi kompilatoru un SCons
- 2. uzdevums - Lejupielādē godot-cpp un nokompilē to
- 3. uzdevums - Pieslēdz bibliotēku Godot projektam
- Papildu uzdevums - Saprot, ko dara katrs solis

> **Iesniedz:** Tavā datorā ir uzstādīts C++ kompilators un SCons, nokompilēta godot-cpp bibliotēka, un Godot projekts atveras bez kļūdas par trūkstošu GDExtension bibliotēku.

**[1.4 Pirmais C++ skripts: mainīgie un izvade](programmesana2/prog2_1/prog2_14.html)**

- 1. uzdevums - Uzraksti .hpp un .cpp failu pāri
- 2. uzdevums - Reģistrē klasi un nokompilē
- 3. uzdevums - Pievieno mainīgo un izdrukā to Godot
- Papildu uzdevums - Salīdzini ar Python

> **Iesniedz:** Tev ir uzrakstīta pirmā C++ klase Hello, kas ir reģistrēta, nokompilēta, pievienota Godot scēnai un palaižot spēli izdrukā tekstu Output panelī.

**[1.5 Spēles laukuma izveide](programmesana2/prog2_1/prog2_15.html)**

- 1. uzdevums - Novieto objektus pēc koordinātēm
- 2. uzdevums - Pievieno sienas un vidus līniju
- 3. uzdevums - Pievieno punktu skaitītāju un kameru
- Papildu uzdevums - Izrēķini pozīcijas pats

> **Iesniedz:** Tavā main.tscn scēnā ir gatavs Pong laukums: abi paddle malās, bumba centrā, divas sienas ar sadursmes formām, vidus līnija, rezultāta uzraksts un kamera.

**[1.6 Noslēguma projekts: Pong](programmesana2/prog2_1/prog2_16.html)**

- 1. uzdevums - Liec paddle kustēties
- 2. uzdevums - Liec bumbai lidot un atlekt
- 3. uzdevums - Pievieno punktus un uzvaru
- Papildu uzdevums - Paātrini bumbu pēc katra sitiena

> **Iesniedz:** Tev ir strādājoša Pong spēle: abi spēlētāji vada savus paddle, bumba lido un atlec, spēle skaita punktus un paziņo uzvarētāju pie 5 punktiem. Visa spēles loģika ir C++ klasēs.


### 2. tēma - Spēles mehānika

**[2.1 Process un fizikas cikli](programmesana2/prog2_2/prog2_21.html)**

- 1. uzdevums - Liec objektam kustēties ar delta
- 2. uzdevums - Salīdzini _process un _physics_process
- 3. uzdevums - Pārbaudi, kas notiek bez delta
- Papildu uzdevums - Liec objektam kustēties pa apli

> **Iesniedz:** Tev ir C++ klase, kas pārvieto objektu, izmantojot delta, un tu ar mērījumu vari pierādīt, kāpēc bez delta spēles ātrums mainās atkarībā no datora.

**[2.2 Input apstrāde un Input Map](programmesana2/prog2_2/prog2_22.html)**

- 1. uzdevums - Izveido Input Map darbības
- 2. uzdevums - Vadi objektu ar taustiņiem
- 3. uzdevums - Normalizē diagonālo kustību
- Papildu uzdevums - Pievieno skriešanas taustiņu

> **Iesniedz:** Tev ir izveidotas četras Input Map darbības, un C++ klase pārvieto objektu pēc taustiņiem tā, ka diagonālā kustība nav ātrāka par taisno.

**[2.3 Vadības struktūras spēles loģikā](programmesana2/prog2_2/prog2_23.html)**

- 1. uzdevums - Pārraksti Python if C++ sintaksē
- 2. uzdevums - Izveido enum un switch priekšmetu veidiem
- 3. uzdevums - Pievieno ciklu, kas pārbauda visus priekšmetus
- Papildu uzdevums - Saskaiti katra veida priekšmetus

> **Iesniedz:** Tu proti C++ sintaksē uzrakstīt if/else if/else, izveidot enum class ar switch un apstrādāt priekšmetu sarakstu ar ciklu, un vari nosaukt galvenās atšķirības no Python.

**[2.4 Sadursmju noteikšana](programmesana2/prog2_2/prog2_24.html)**

- 1. uzdevums - Pievieno sienu un pārbaudi sadursmi
- 2. uzdevums - Izveido savācamu monētu ar Area2D
- 3. uzdevums - Iestati Collision Layers
- Papildu uzdevums - Saskaiti savāktās monētas

> **Iesniedz:** Tavā projektā spēlētājs apstājas pie StaticBody2D sienas, savāc Area2D monētu, kas pazūd, un tu proti ar Collision Layers un Masks noteikt, kurš objekts ar kuru sadursies.

**[2.5 Gravitācija un platformas mehānika](programmesana2/prog2_2/prog2_25.html)**

- 1. uzdevums - Pievieno gravitāciju
- 2. uzdevums - Pievieno lēcienu un zemes pārbaudi
- 3. uzdevums - Pievieno mainīgu lēciena augstumu un coyote time
- Papildu uzdevums - Pievieno dubulto lēcienu

> **Iesniedz:** Tavam varonim ir strādājoša platformas mehānika: gravitācija, lēciens tikai no zemes, mainīgs lēciena augstums atkarībā no taustiņa turēšanas ilguma un coyote time tolerance.

**[2.6 Noslēguma projekts: Platformas spēle](programmesana2/prog2_2/prog2_26.html)**

- 1. uzdevums - Uzbūvē pirmo līmeni
- 2. uzdevums - Pievieno ienaidnieku un savācamos
- 3. uzdevums - Pievieno finišu, HUD un līmeņu maiņu
- Papildu uzdevums - Pievieno otro līmeni

> **Iesniedz:** Tev ir izspēlējama platformas spēle: varonis ar gravitāciju un lēcienu, vismaz viens līmenis ar platformām, patrulējošs ienaidnieks, savācamas monētas, HUD ar HP un rezultātu, un finišs, kas noved pie uzvaras vai nākamā līmeņa.


### 3. tēma - Objektorientētā programmēšana C++

**[3.1 C++ klases pamati](programmesana2/prog2_3/prog2_31.html)**

- 1. uzdevums - Izveido pirmo klasi ar laukiem
- 2. uzdevums - Pievieno konstruktoru un metodes
- 3. uzdevums - Pārbaudi private un public atšķirību
- Papildu uzdevums - Izveido komandu no trim dalībniekiem

> **Iesniedz:** Tu proti C++ uzrakstīt klasi ar laukiem, konstruktoru un metodēm, izveidot no tās objektu un paskaidrot, kāpēc daļa lauku ir private.

**[3.2 Mantošana C++ un Godot](programmesana2/prog2_3/prog2_32.html)**

- 1. uzdevums - Izveido bērna klasi
- 2. uzdevums - Pārraksti metodi ar override
- 3. uzdevums - Izsauc visas lomas vienā ciklā
- Papildu uzdevums - Pievieno trešo lomu

> **Iesniedz:** Tu proti izveidot bērna klasi ar public mantošanu, izsaukt vecāka konstruktoru, pārrakstīt metodi ar virtual un override un apstrādāt visas lomas vienā ciklā.

**[3.3 Signāli un objektu komunikācija](programmesana2/prog2_3/prog2_33.html)**

- 1. uzdevums - Reģistrē un raidi signālu
- 2. uzdevums - Pieslēdzies signālam no cita objekta
- 3. uzdevums - Salīdzini signālu ar tiešu izsaukumu
- Papildu uzdevums - Pievieno signālam vairāk datu

> **Iesniedz:** Tu proti C++ klasē reģistrēt Godot signālu, to raidīt notikuma brīdī un pieslēgt tam citu objektu, un vari izskaidrot, kāpēc signāls ir ērtāks par tiešu izsaukumu.

**[3.4 Custom GDExtension klases editorā redzamas](programmesana2/prog2_3/prog2_34.html)**

- 1. uzdevums - Padari klasi redzamu editorā
- 2. uzdevums - Pievieno rediģējamas īpašības
- 3. uzdevums - Iestati vērtības Inspector un pārbaudi
- Papildu uzdevums - Pievieno izvēlni ar variantiem

> **Iesniedz:** Tava C++ klase parādās Godot editorā kā mezgla tips, tās lauki ir rediģējami Inspector panelī, un vairāki viena tipa mezgli var strādāt ar dažādām vērtībām bez koda maiņas.

**[3.5 Statistikas sistēma un struct](programmesana2/prog2_3/prog2_35.html)**

- 1. uzdevums - Izveido struct statistikai
- 2. uzdevums - Ieliec struct klasē un pievieno metodes
- 3. uzdevums - Pievieno pagaidu bonusus sarakstā
- Papildu uzdevums - Pievieno bonusiem ilgumu

> **Iesniedz:** Tu proti izveidot struct datu grupēšanai, ielikt to klasē kā lauku (kompozīcija) un rēķināt kopējo vērtību no saraksta, nevis glabāt to atsevišķi.

**[3.6 Noslēguma projekts: Klases turnīra simulators](programmesana2/prog2_3/prog2_36.html)**

- 1. uzdevums - Saliec komandu un šķēršļus
- 2. uzdevums - Uzraksti vienas kārtas loģiku
- 3. uzdevums - Pievieno turnīra ciklu un rezultātu
- Papildu uzdevums - Parādi turnīru uz ekrāna

> **Iesniedz:** Tev ir strādājošs klases turnīra simulators: trīs dalībnieku lomas ar atšķirīgu uzvedību, trīs šķēršļi, kārtu cikls ar signāliem par izstāšanos un izdrukāts uzvarētājs ar kārtu skaitu.


### 4. tēma - Datu struktūras un AI

**[4.1 Vector un Array](programmesana2/prog2_4/prog2_41.html)**

- 1. uzdevums - Izveido ienaidnieku sarakstu ar vector
- 2. uzdevums - Pievieno un izņem elementus droši
- 3. uzdevums - Salīdzini vector ar Godot Array
- Papildu uzdevums - Atrodi tuvāko ienaidnieku

> **Iesniedz:** Tu proti C++ izveidot std::vector sarakstu, droši pievienot un izņemt elementus un izskaidrot, ar ko tas atšķiras no Godot Array.

**[4.2 Map un Dictionary](programmesana2/prog2_4/prog2_42.html)**

- 1. uzdevums - Izveido inventāru ar std::map
- 2. uzdevums - Pievieno drošu meklēšanu
- 3. uzdevums - Salīdzini map ar Godot Dictionary
- Papildu uzdevums - Izmēģini unordered_map

> **Iesniedz:** Tu proti C++ izveidot std::map inventāru, droši meklēt tajā priekšmetus, nepievienojot tukšus ierakstus, un izskaidrot, kad jālieto Godot Dictionary.

**[4.3 State machines AI uzvedībai](programmesana2/prog2_4/prog2_43.html)**

- 1. uzdevums - Izveido stāvokļu enum un pārslēgšanu
- 2. uzdevums - Pievieno pārejas noteikumus
- 3. uzdevums - Iztestē visus stāvokļus
- Papildu uzdevums - Pievieno stāvokļa taimeri

> **Iesniedz:** Tavam ienaidniekam ir strādājoša stāvokļu mašīna ar pieciem stāvokļiem, pārejas notiek pēc attāluma līdz spēlētājam, un DEAD ir gala stāvoklis, no kura nevar izkļūt.

**[4.4 Pathfinding ar A*](programmesana2/prog2_4/prog2_44.html)**

- 1. uzdevums - Sagatavo navigācijas reģionu
- 2. uzdevums - Liec ienaidniekam sekot ceļam
- 3. uzdevums - Salīdzini taisno kustību ar pathfinding
- Papildu uzdevums - Zīmē ceļu uz ekrāna

> **Iesniedz:** Tavā līmenī ir izcepts navigācijas reģions, un ienaidnieks ar NavigationAgent2D apiet sienas, lai nonāktu pie spēlētāja, nevis iestrēgst pret tām.

**[4.5 Šaušanas mehānika un object pooling](programmesana2/prog2_4/prog2_45.html)**

- 1. uzdevums - Izšauj pirmo lādiņu
- 2. uzdevums - Izveido lādiņu krātuvi
- 3. uzdevums - Salīdzini abas pieejas ar mērījumu
- Papildu uzdevums - Pievieno šaušanas ātruma ierobežojumu

> **Iesniedz:** Tavā spēlē ir strādājoša šaušana, kas izmanto lādiņu krātuvi (object pooling), un tu ar mērījumu vari pierādīt, ar ko tā ir labāka par lādiņu veidošanu un dzēšanu katru reizi.

**[4.6 Noslēguma projekts: Top-down šautene](programmesana2/prog2_4/prog2_46.html)**

- 1. uzdevums - Spēlētājs ar kustību un mērķēšanu
- 2. uzdevums - Divi ienaidnieku tipi ar AI
- 3. uzdevums - Viļņu sistēma un rezultāts
- Papildu uzdevums - Pievieno savācamos bonusus

> **Iesniedz:** Tev ir izspēlējama top-down šautene: spēlētājs ar 8 virzienu kustību un mērķēšanu pret peli, vismaz divi ienaidnieku tipi ar atšķirīgu AI, viļņu sistēma ar augošu grūtību un HUD ar punktiem un HP.


### 5. tēma - Dati un algoritmi

**[5.1 Failu I/O Godot vidē](programmesana2/prog2_5/prog2_51.html)**

- 1. uzdevums - Ieraksti un nolasi failu
- 2. uzdevums - Saglabā spēles rezultātu
- 3. uzdevums - Apstrādā trūkstošu failu
- Papildu uzdevums - Saglabā vairākas vērtības

> **Iesniedz:** Tava spēle saglabā rezultātu failā user:// mapē, ielādē to pēc restarta un neizmet kļūdu, ja saglabāšanas faila vēl nav.

**[5.2 JSON serializācija un Resource sistēma](programmesana2/prog2_5/prog2_52.html)**

- 1. uzdevums - Pārvērs Dictionary par JSON
- 2. uzdevums - Nolasi JSON atpakaļ
- 3. uzdevums - Apstrādā bojātu JSON
- Papildu uzdevums - Saglabā sarakstu JSON failā

> **Iesniedz:** Tava spēle saglabā stāvokli salasāmā JSON failā, ielādē to atpakaļ ar pareiziem datu tipiem un neapstājas, ja fails ir bojāts.

**[5.3 Save/Load arhitektūra](programmesana2/prog2_5/prog2_53.html)**

- 1. uzdevums - Izveido SaveManager ar slotiem
- 2. uzdevums - Liec objektiem saglabāt sevi pašiem
- 3. uzdevums - Pievieno autosave un versiju
- Papildu uzdevums - Parādi slotu izvēlni

> **Iesniedz:** Tavā spēlē ir SaveManager ar vairākiem slotiem, objekti paši saglabā savus datus caur Saveable interfeisu, darbojas autosave, un saglabātajam failam ir versijas pārbaude.

**[5.4 Procedural generation](programmesana2/prog2_5/prog2_54.html)**

- 1. uzdevums - Ģenerē labirintu ar Random Walk
- 2. uzdevums - Pārvērs režģi par spēles laukumu
- 3. uzdevums - Pārbaudi, vai labirints ir izejams
- Papildu uzdevums - Pievieno sēklu atkārtojamībai

> **Iesniedz:** Tava spēle pati uzģenerē labirintu ar Random Walk algoritmu, pārvērš to par spēlējamu laukumu un pirms sākuma pārbauda, ka izeja tiešām ir sasniedzama.

**[5.5 Algoritmu efektivitāte](programmesana2/prog2_5/prog2_55.html)**

- 1. uzdevums - Izmēri divu algoritmu laiku
- 2. uzdevums - Atrodi un salabo lēno vietu savā spēlē
- 3. uzdevums - Pierādi uzlabojumu ar mērījumu
- Papildu uzdevums - Salīdzini vector ar map meklēšanu

> **Iesniedz:** Tu proti izmērīt koda izpildes laiku, atrast lēnāko vietu ar Godot profileri, to izlabot un ar skaitļiem pierādīt, ka uzlabojums tiešām notika.

**[5.6 Noslēguma projekts: Procedurālais klases labirints](programmesana2/prog2_5/prog2_56.html)**

- 1. uzdevums - Savieno labirintu ar spēlētāju
- 2. uzdevums - Pievieno savācamos un šķēršļus
- 3. uzdevums - Pievieno meta-progresu un saglabāšanu
- Papildu uzdevums - Pievieno spēlētāja klases

> **Iesniedz:** Tev ir izspēlējams procedurālais labirints: katrs līmenis tiek uzģenerēts un pārbaudīts, ka ir izejams, labirintā ir savācamie un šķēršļi, un kopējais progress saglabājas JSON failā arī pēc neveiksmīga mēģinājuma.


### 6. tēma - Pilnvērtīga izstrāde un publicēšana

**[6.1 UI elementi un Control nodes](programmesana2/prog2_6/prog2_61.html)**

- 1. uzdevums - Uzbūvē sākuma izvēlni
- 2. uzdevums - Savieno pogas ar kodu
- 3. uzdevums - Pievieno enkurus un pārbaudi izmērus
- Papildu uzdevums - Pievieno iestatījumu logu

> **Iesniedz:** Tavai spēlei ir sākuma izvēlne ar trim pogām Control mezglos, pogas ir savienotas ar C++ kodu caur signāliem, un izvēlne paliek centrā, mainot loga izmēru.

**[6.2 Animācijas un Tween](programmesana2/prog2_6/prog2_62.html)**

- 1. uzdevums - Uztaisi pirmo Tween animāciju
- 2. uzdevums - Animē izvēlnes parādīšanos
- 3. uzdevums - Pievieno atsauksmes animāciju spēlē
- Papildu uzdevums - Izmēģini AnimationPlayer

> **Iesniedz:** Tavā spēlē darbojas Tween animācijas: izvēlne parādās mīksti, un vismaz viens spēles notikums dod spēlētājam vizuālu atsauksmi, kas nesajūk pie ātras atkārtošanas.

**[6.3 Audio sistēma](programmesana2/prog2_6/prog2_63.html)**

- 1. uzdevums - Atskaņo pirmo skaņu
- 2. uzdevums - Pievieno fona mūziku ar pāreju
- 3. uzdevums - Sakārto skaļumu ar audio bus
- Papildu uzdevums - Saglabā skaļuma iestatījumus

> **Iesniedz:** Tavā spēlē skan skaņas efekti un fona mūzika ar mīkstām pārejām, un mūziku ar efektiem var regulēt atsevišķi caur diviem audio bus.

**[6.4 Atkļūdošana un profilēšana](programmesana2/prog2_6/prog2_64.html)**

- 1. uzdevums - Atrodi kļūdu ar izdrukām
- 2. uzdevums - Lieto breakpoint un mainīgo skatu
- 3. uzdevums - Atrodi lēnāko vietu ar profileri
- Papildu uzdevums - Pievieno pašpārbaudes izdrukas

> **Iesniedz:** Tu proti atrast kļūdu trīs veidos: ar izdrukām, ar breakpoint un mainīgo skatu, un ar profileri atrast laikietilpīgāko funkciju.

**[6.5 Eksports un publicēšana](programmesana2/prog2_6/prog2_65.html)**

- 1. uzdevums - Eksportē spēli uz datoru
- 2. uzdevums - Eksportē uz tīmekli un palaid lokāli
- 3. uzdevums - Publicē spēli internetā
- Papildu uzdevums - Uzraksti spēles aprakstu

> **Iesniedz:** Tava spēle ir eksportēta gan kā datora programma, gan kā tīmekļa versija, un tā ir publicēta internetā ar publisku saiti, kas strādā arī citās ierīcēs.

**[6.6 Noslēguma projekts: Puzzle spēle](programmesana2/prog2_6/prog2_66.html)**

- 1. uzdevums - Izvēlies puzli un uztaisi laukumu
- 2. uzdevums - Uzraksti uzvaras noteikumu un līmeņus
- 3. uzdevums - Pievieno izvēlni, skaņu un eksportē
- Papildu uzdevums - Pievieno padoma pogu

> **Iesniedz:** Tev ir pabeigta un publicēta puzles spēle: strādājošs laukums, pareizi atpazīta uzvara, vismaz trīs atrisināmi līmeņi, sākuma izvēlne, skaņa, saglabāts labākais rezultāts un publiska tīmekļa saite.


---

## Kas vēl nav izdarīts

**Neapvienotais zars** `claude/audit-lesson-content-mLhPS` atstāts neaiztikts. Tas nav apvienots ar `origin/main`, satur 2 satura commitus, bet ir balstīts uz vecu koku - apvienojot to tagad, `style.css` tiktu atgriezts par ~2275 rindām.

Visas 148 mācību stundas (30 datorikā, 10 robotikā, 72 Programmēšanā I, 36 Programmēšanā II) tagad atbilst stundu standartam.
