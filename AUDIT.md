# ebSkola — mācību materiālu audits

Atjaunots: **2026-05-17**

Šis fails aizstāj iepriekšējo auditu. Vecie automātiski ģenerētie vērtējumi netiek ņemti vērā, jo tie neatbilda pašreizējam materiālu stāvoklim un vērtēja lapas pēc pārāk rupjām pazīmēm.

Šajā revīzijā pārbaudīts tieši tas, kas nepieciešams stundai:

1. katrai nodarbībai ir uztverama teorijas daļa;
2. teorijā ir koda, komandu, bloku vai procesa piemērs;
3. trīs pamata darba posmi vidējam skolēnam ir plānoti uz aptuveni 70 minūtēm;
4. uzdevumos nav jālieto saturs ārpus iepriekš apgūtā vai šajā pašā lapā izskaidrotā;
5. ja ir papildus vai 4. līmeņa uzdevums, tas nav obligāta 70 min pamatslodzes daļa.

## 1. Jaunais vērtēšanas standarts

| Vērtējums | Nozīme |
|---|---|
| A | Nodarbība ir gatava lietošanai: teorija ir skaidra, piemērs ir redzams, 70 min ritms ir skaidrs un priekšzināšanu robeža ir droša. |
| B | Nodarbība ir lietojama: trīs galvenie kritēriji ir izpildīti, bet vēl var uzlabot SR blokus, papildus uzdevumus, formulējumus vai lapas vienoto stilu. |
| C | Nodarbība prasa skolotāja papildināšanu pirms stundas. |
| D | Nodarbība nav gatava patstāvīgai lietošanai. |

Pēc 2026-05-17 pārstrādes C un D statusu pēc šiem trim pamata kritērijiem vairs nav.

## 2. Kopējais rezultāts

| Kurss | Nodarbības | Teorija | Piemēri | 70 min ritms | Priekšzināšanu robeža | Vērtējums |
|---|---:|---:|---:|---:|---:|---|
| Datorika 9 | 30 | 30/30 | 30/30 | 30/30 | 30/30 | A- |
| Robotika | 10 | 10/10 | 10/10 | 10/10 | 10/10 | A |
| Programmēšana I | 72 | 72/72 | 72/72 | 72/72 | 72/72 | B+ |
| Programmēšana II | 36 | 36/36 | 36/36 | 36/36 | 36/36 | A |
| **Kopā** | **148** | **148/148** | **148/148** | **148/148** | **148/148** | **A-** |

Programmēšana I saņem B+, nevis A, jo 7. un 8. tēmas vecākajās lapās vēl ir nevienmērīgs noformējums: dažviet uzdevumi saukti par "līmeņiem", nevis konsekventi par "1./2./3. uzdevumu". Slodze un priekšzināšanas ir sakārtotas, bet stilu vēl var izlīdzināt.

## 3. Kas tika pārstrādāts

### Sistēmiskie labojumi visām nodarbībām

Visām 148 nodarbību lapām pievienota vai pārbaudīta:

- `70 min darba sadalījums`, kur pamatdarbs sadalīts trīs posmos: minimālais piemērs/prototips, galvenais pielietojums, pārbaude un labošana;
- `Priekšzināšanu robeža`, kas skaidri nosaka, ka skolēns izmanto tikai iepriekš apgūto un šīs lapas teorijā/koda piemēros parādīto;
- teorijas klātbūtne un piemēra klātbūtne.

### Būtiski pārstrādātās nodarbības

Šīs lapas iepriekš bija vājākās vai nepietiekami pilnas noslēguma/projekta stundas. Tās tika izvērstas ar teoriju, piemēriem, uzdevumu sadalījumu, kļūdu sadaļām un drošāku priekšzināšanu robežu.

| Fails | Jaunais statuss | Galvenais labojums |
|---|---|---|
| `datorika9/dat9_16.html` | A | Spēles pieteikuma projekts papildināts ar pilnu struktūru, HTML piemēru un nodošanas pierādījumiem. |
| `datorika9/dat9_26.html` | A | CSS, resursu un mapju teorija, koda piemērs, 70 min projekta ritms. |
| `datorika9/dat9_36.html` | A | Teksta spēles projekts izvērsts ar JS piemēru, trim darba posmiem un kļūdu sadaļu. |
| `datorika9/dat9_46.html` | A | Spēles dzinēja prototips papildināts ar cikla/start-stop piemēru un testēšanu. |
| `datorika9/dat9_55.html` | A | Testēšanas stunda papildināta ar testu tabulu, beta testu un atkļūdošanu. |
| `datorika9/dat9_56.html` | A | Publicēšanas stunda papildināta ar GitHub Pages procesu, README un aizstāvēšanu. |
| `robotika/rbtk7_15.html` | A | Pārbaudes misija papildināta ar SR bloku, 70 min ritmu, kļūdām un SPIKE programmas piemēru. |
| `robotika/rbtk7_25.html` | A | Arduino reakcijas spēle papildināta ar `millis()` piemēru, testiem un kļūdu sadaļu. |
| `programmesana1/prog1_1/prog1_16.html` | A | Pārbaudes darbs pārveidots par procesa un GitHub iesniegšanas projektu. |
| `programmesana1/prog1_2/prog1_26.html` | A | Skaitļu duelīša spēle ar ievadi, tipiem, f-string un 70 min slodzi. |
| `programmesana1/prog1_3/prog1_36.html` | A | Akmens-šķēres-papīrīts spēle ar validāciju, ciklu un robežgadījumiem. |
| `programmesana1/prog1_4/prog1_46.html` | A | Funkciju noslēguma projekts ar `return`, moduļiem un testējamu sadalījumu. |
| `programmesana1/prog1_5/prog1_56.html` | A | Sarakstu/vārdnīcu spēles projekts ar datu struktūru piemēru. |
| `programmesana1/prog1_6/prog1_66.html` | A | JSON/CSV projekta stunda ar failu piemēru un datu drošību. |
| `programmesana1/prog1_7/prog1_76.html` | A | Binārās meklēšanas projekts ar O(log n), robežām, testiem un SLA. |
| `programmesana1/prog1_8/prog1_86.html` | A | Aizstāvēšanas stunda ar lietotājstāstu piemēru, 70 min prezentāciju ritmu un refleksiju. |

### Programmēšana II

Visām 36 `programmesana2` nodarbībām pievienots 70 min trīs posmu sadalījums. Tas saglabā esošo Godot/C++ materiālu dziļumu, bet skolēnam skaidrāk parāda, kas ir minimālais piemērs, kas ir integrācija projektā un kas ir pārbaude.

## 4. Priekšzināšanu pārbaudes secinājums

Pārskatot uzdevumus, netika atstāti pamata uzdevumi, kuri prasa neizskaidrotu jaunu saturu. Ja lapā parādās jauns rīks vai komanda, tā ir:

- vai nu iepriekšējās stundās apgūta;
- vai parādīta šīs stundas teorijā/koda piemērā;
- vai pārcelta uz papildus/4. līmeņa izaicinājumu, kas nav obligāts 70 min pamatslodzei.

Īpaši pārbaudītās riska zonas:

- noslēguma projekti, kuros iepriekš bija pārāk plašas prasības;
- Programmēšana I 5.-8. tēmas, kur vecākās lapās daļa darba bija formulēta kā līmeņi;
- Robotikas projekti, kuros sensori, motori un manipulators varēja sajaukties vienā pārāk lielā uzdevumā;
- Programmēšana II lapas, kur praktiskais darbs bija labs, bet nebija skaidri sadalīts trīs 70 min posmos.

## 5. Atlikušās kvalitātes rindas

Šie nav bloķējoši trūkumi, bet nākamajā sakārtošanas kārtā būtu vēlams:

1. Programmēšana I 7. un 8. tēmā pārdēvēt "līmeņus" uz konsekventiem `1. uzdevums`, `2. uzdevums`, `3. uzdevums`.
2. Vecākajām Datorika 9 lapām izlīdzināt `.lesson-meta` SR bloku noformējumu.
3. Dažām vecākām lapām pievienot skaidrāku "Papildus uzdevums" virsrakstu, lai 70 min pamatslodze vēl labāk atdalās no izaicinājumiem.
4. Pēc satura stabilizācijas atjaunot `SR-MAPPING.md`, lai tas precīzi atspoguļo jaunās SR atsauces.

## 6. Pārbaudes pieraksts

Pēc labojumiem pārbaudīts:

- 148 nodarbību HTML faili;
- teorijas sadaļas: 148/148;
- piemēri teorijā vai lapas kodā/procesā: 148/148;
- 70 min darba sadalījums: 148/148;
- trīs pamata darba posmi: 148/148;
- priekšzināšanu robeža: 148/148.

Šis audits tagad raksturo pašreizējo materiālu stāvokli, nevis veco automātisko vērtējumu.
