# POSSIBLE_CHANGES.md — Implementējami uzlabojumi pēc pedagoģijas eseju analīzes

**Sagatavots:** 2026-05-17
**Avoti:** `CRITICAL_PEDAGOGY_ESSAYS.md` (4 kritiskās esejas) un `PEDAGOGY_PHILOSOPHY_ESSAYS.md` (4 filozofiskās esejas).
**Mērķis:** Pārvērst eseju abstraktās tēzes konkrētos, izpildāmos labojumos `ebskola` materiāliem, vispirms pārbaudot, vai katrs uzslavas vai kritikas punkts ir patiess attiecībā uz pašreizējo kodu bāzi.

---

## 0. Metodoloģija — kā tika pārbaudīta leģitimitāte

Katrs eseju apgalvojums tika pārbaudīts ar `grep`/failu auditu pret reālo repozitoriju (148 nodarbību HTML faili). Apgalvojumi tiek marķēti:

- **LEĢITĪMS** — pierādījumi apstiprina problēmu.
- **DAĻĒJI ATRISINĀTS** — problēma bija reāla, bet pa daļai jau novērsta (galvenokārt 2026-05-17 `main` atjauninājumā).
- **PĀRSPĪLĒTS** — apgalvojums daļēji vai pilnīgi neatbilst pašreizējam stāvoklim.

Pārbaudes rezultātu kopsavilkums:

| Pārbaude | Rezultāts | Spriedums |
|---|---|---|
| Glosārijs/terminu vārdnīca eksistē? | 0 reālu glosāriju | Kritika LEĢITĪMA |
| `prog1_7`/`prog1_8` lieto "līmenis", ne "1./2./3. uzdevums" | 9 faili ar "līmenis" | Kritika LEĢITĪMA |
| "Priekšzināšanu robeža" marķieris | 148/148 faili | Kritika DAĻĒJI ATRISINĀTA |
| "70 min" darba ritms | 148/148 faili | Kritika DAĻĒJI ATRISINĀTA |
| Privātuma / privāta repo opcijas | 2 faili | Kritika LEĢITĪMA |
| Zema-infrastruktūras alternatīvas (SQLite, ZIP) | 1 fails | Kritika LEĢITĪMA |
| Tvēruma robežas izteikumi ("ārpus kursa") | 1 fails | Kritika LEĢITĪMA |
| "Mācīšanās pierādījuma" mikropārbaudes | 0 failu | Kritika LEĢITĪMA |
| Spēļu dominance (main faili ar "spēle") | 22 main faili | Kritika LEĢITĪMA |

---

## 1. Kritiskā eseja 1 — "Project-Based Overreach"

### Apgalvojumi un spriedumi

| # | Apgalvojums | Spriedums | Pierādījums |
|---|---|---|---|
| 1.1 | Katra tēma beidzas ar projektu → "production mentality", pulēšana var maskēt seklu izpratni | **LEĢITĪMS** | 22 main faili centrēti ap spēļu projektiem; vērtēšanas tabulās ir "polish"/"pulēts" kritēriji |
| 1.2 | Programmēšana I ir pārblīvēta (no IDE līdz PostgreSQL+OOP+Flask 12 tēmās) | **LEĢITĪMS** | 12 tēmas × 6 stundas; satura blīvums apstiprināms |
| 1.3 | Trūkst skaidra dalījuma "core / optional / enrichment" | **DAĻĒJI ATRISINĀTS** | "Papildus uzdevums" jau atdala 4. uzdevumu; bet nav core-vs-enrichment marķējuma teorijā |
| 1.4 | Spēles dominē → šaurs priekšstats par to, kam programmēšana der | **LEĢITĪMS** | Gandrīz visi projekti ir spēles |

### Implementējamie labojumi

**L1.1 — "Konceptuālais kodols" baneris katras tēmas main lapā** (mazs darbs)
Katras `*main.html` augšā pievieno `<div class="info-box">` ar 3-5 punktu sarakstu "Ko KATRAM skolēnam jāsaprot pēc šīs tēmas" (non-negotiable spine), atsevišķi no projektu ambīcijām. Tas tieši atbild uz 1.3.

**L1.2 — "Minimālā veiksme" katra noslēguma projekta lapā** (mazs darbs)
Katrā `*_?6.html` / `prog2_?6.html` projektu lapā pievieno sadaļu "Minimālā pieņemamā versija (MVP)" — vienkāršākā strādājošā versija, ko students var iesniegt. Tas mazina pulēšanas spiedienu (1.1) un nodrošina, ka vājākie skolēni redz sasniedzamu mērķi.

**L1.3 — Ne-spēļu projektu alternatīvas** (vidējs darbs)
Vismaz pa vienam projektam katrā kursā piedāvāt ne-spēles alternatīvu ar tādu pašu tehnisko saturu:
- Programmēšana I (6. tēma): blakus "Quiz spēlei" — "Personīgo izdevumu analizators" (tie paši JSON/CSV/failu prasmes).
- Programmēšana I (10. tēma): blakus "Highscore DB" — "Bibliotēkas grāmatu katalogs" (tās pašas SQL prasmes).
- Programmēšana II: vismaz vienai tēmai piedāvāt "rīks/simulācija" alternatīvu spēlei. Tas tieši atbild uz 1.4.

**L1.4 — `Priekšzināšanu robeža` jau eksistē** — nav jāveic; tikai jāuztur konsekvence jaunajās lapās.

---

## 2. Kritiskā eseja 2 — "Equity, Access, Toolchains"

### Apgalvojumi un spriedumi

| # | Apgalvojums | Spriedums | Pierādījums |
|---|---|---|---|
| 2.1 | Toolchain pieņem stabilu vidi (Godot, PostgreSQL, cloud) → nevienlīdzība | **LEĢITĪMS** | Topiki 9-12 + prog2 prasa SCons, psycopg2, Render utt. |
| 2.2 | Trūkst glosārija angļu terminiem → valodas barjera | **LEĢITĪMS** | 0 reālu glosāriju atrasti |
| 2.3 | Publiska GitHub publicēšana bez privātuma alternatīvām | **LEĢITĪMS** | Tikai 2 faili min privātumu |
| 2.4 | Trūkst zema-infrastruktūras ceļu (SQLite pirms PostgreSQL, ZIP pirms GitHub) | **LEĢITĪMS** | Tikai 1 fails min SQLite/ZIP |
| 2.5 | Vērtēšana pēc gala artefakta = infrastruktūra kļūst par atzīmi | **DAĻĒJI ATRISINĀTS** | Vērtēšanas tabulas jau vērtē procesu (commits, README), bet ne eksplicīti "neatkarīgi no hardware" |

### Implementējamie labojumi

**L2.1 — Glosārijs `paligm.html`** (vidējs darbs, augsta vērtība)
Pievieno jaunu `paligm.html` kategoriju "Terminu vārdnīca (EN → LV)" ar tabulu: angļu termins | latviešu skaidrojums | konteksts. Sākt ar ~60 biežākajiem: commit, push, pull, branch, repository, REST, JSON, endpoint, query, schema, Scene Tree, Node, signal, GDExtension, object pooling, pathfinding, profiling, deploy, etc. Tas tieši atbild uz 2.2 un ir vienas vietas risinājums visam kursam.

**L2.2 — "Bez interneta / vāja datora" piezīmes setup lapās** (mazs-vidējs darbs)
Lapās, kas prasa instalāciju vai cloud (prog1_1x, prog1_10x, prog1_12x, prog2_1x), pievieno `<div class="info-box">` "Ja nav piekļuves":
- GitHub vietā → ZIP arhīva iesniegšana e-klasē vai skolas koplietots repo.
- PostgreSQL vietā → vispirms SQLite vai ER-diagramma uz papīra.
- Render/cloud vietā → lokāla demonstrācija skolotājam (`localhost`).
- Godot C++ vietā → GDScript prototips kā atkāpšanās ceļš (C++ paliek mērķis).
Tas atbild uz 2.1 un 2.4.

**L2.3 — Privātuma opcija** (mazs darbs)
Visās lapās, kas prasa publisku publicēšanu (noslēguma projekti), pievieno teikumu: "Ja nevēlies publiskot — izmanto privātu GitHub repo (Settings → Private) vai iesniedz lokāli skolotājam." Atbild uz 2.3.

**L2.4 — Vērtēšanas atruna** (mazs darbs)
Vērtēšanas tabulās pievieno zemsvītras piezīmi: "Vērtē konceptuālo izpratni un procesu, NEVIS datora jaudu vai interneta pieejamību." Atbild uz 2.5.

---

## 3. Kritiskā eseja 3 — "Scaffolding, Consistency, Formula"

### Apgalvojumi un spriedumi

| # | Apgalvojums | Spriedums | Pierādījums |
|---|---|---|---|
| 3.1 | Viena veidne visiem konceptiem maskē atšķirīgu pedagoģiju | **DAĻĒJI PĀRSPĪLĒTS** | Veidne ir, bet tā ir adekvāta lielākajai daļai; pilnīga diferenciācija nav reāli uzturama |
| 3.2 | Terminoloģijas nekonsekvence ("līmenis" vs "uzdevums", dažādi virsraksti) | **LEĢITĪMS** | 9 faili prog1_7/8 lieto "līmenis", ne "1./2./3. uzdevums" |
| 3.3 | Koda piemēri kļūst par receptēm → vāja far-transfer | **LEĢITĪMS** | Lielākā daļa lapu: viens piemērs, "atkārto un pielāgo" |
| 3.4 | "Biežākās kļūdas" tikai uzskaita lokālas kļūdas, nemāca kļūdu kategorijas | **LEĢITĪMS** | Sekcijas ir konkrētas, bet bez kategorizācijas |
| 3.5 | Trūkst "evidence of learning" mikropārbaudes katrā lapā | **LEĢITĪMS** | 0 failu ar šādu sadaļu |
| 3.6 | Nekonsekventi prerekvizītu marķieri | **DAĻĒJI ATRISINĀTS** | "Priekšzināšanu robeža" tagad 148/148 |

### Implementējamie labojumi

**L3.1 — Pārdēvēt "līmenis" → "uzdevums" prog1_7/prog1_8** (mazs darbs, augsta vērtība)
Skripts, kas `prog1_8/*.html` (un prog1_7) pārdēvē "1. līmenis (Vienkāršs)" → "1. uzdevums", "2. līmenis" → "2. uzdevums", "3. līmenis" → "3. uzdevums", saskaņojot ar pārējo kursu. Tas tieši atbild uz 3.2 un ir minēts arī AUDIT.md "atlikušajās rindās".

**L3.2 — "Mācīšanās pierādījums" mikrobloks** (vidējs darbs)
Pievieno katrai nodarbībai īsu `<div class="info-box">` "Pārbaudi sevi (1 minūte)" ar 1-2 punktiem, ko students var pateikt/parādīt PIRMS gala projekta, piem.:
- "Es protu paskaidrot, kāpēc šeit lietoju vārdnīcu, ne sarakstu."
- "Es varu parādīt vienu testu, kas neizdevās, un kā to izlaboju."
Atbild uz 3.5.

**L3.3 — Kļūdu kategoriju leģenda `paligm.html`** (mazs darbs)
`paligm.html` "Atkļūdošana" kategorijā pievieno sekciju "Kļūdu tipi" ar tabulu: sintakses / izpildlaika / loģikas / stāvokļa / datu-formas / vides / dizaina kļūda — katrai īss piemērs. Tad nodarbību "Biežākās kļūdas" var atsaukties uz šīm kategorijām. Atbild uz 3.4.

**L3.4 — "Salīdzini divus risinājumus" variācija dažās stundās** (vidējs darbs, izvēles)
Stundās ar spēcīgu recepšu risku (cikli, funkcijas, SQL) pievieno vienu papildjautājumu: "Pirms palaid kodu — uzmini izvadi" vai "Šeit ir 2 risinājumi; kurš ir labāks un kāpēc?". Atbild uz 3.3. Nav jādara visās 148 lapās — pietiek ar atslēgas stundām.

**L3.5 — NEDARĪT pilnīgu lapu-tipu diferenciāciju** (3.1 pārspīlēts)
Pilnīga 8 lapu-tipu sistēma (concept/lab/debugging clinic/design critique...) būtu skaisti, bet nereāli uzturama vienam autoram un sabojātu pašreizējo navigācijas konsekvenci, kas ir reāls spēks (apstiprina abas eseju kopas). Ieteikums: saglabāt vienu veidni, bet atļaut sekciju mainīgumu (piem., dizaina stundām pievienot "Diskusija", algoritmu stundām "Prognozē rezultātu").

---

## 4. Kritiskā eseja 4 — "Professional Authenticity / Simulated Industry"

### Apgalvojumi un spriedumi

| # | Apgalvojums | Spriedums | Pierādījums |
|---|---|---|---|
| 4.1 | GitHub/deploy var kļūt ceremoniāli (nospied pogas, iegūsti saiti) | **LEĢITĪMS** | Lapas māca soļus, bet ne vienmēr "kāpēc" |
| 4.2 | Profesionālā vārdnīca rada uzpūstu pārliecību (DB/API bez normalizācijas, injekcijas, migrācijas) | **LEĢITĪMS** | Tikai 1 fails ar tvēruma robežu |
| 4.3 | OOP kļūst par ideoloģiju (klases, jo "profesionāli", ne jo vajag) | **LEĢITĪMS** | OOP tēmas nemāca, kad NElietot mantošanu |
| 4.4 | "Testēšana" paliek neformāla (palaid, paklikšķini) | **LEĢITĪMS** | Reti ir eksplicīti testu artefakti |
| 4.5 | Dokumentācija kļūst dekoratīva | **DAĻĒJI ATRISINĀTS** | README tiek prasīts, bet ne vienmēr ar konkrētām sekcijām |

### Implementējamie labojumi

**L4.1 — "Tvēruma robeža" atruna profesionālo rīku tēmās** (mazs darbs, augsta vērtība)
Pievieno `<div class="info-box">` "Ko šodien NEMĀCĀMIES" PostgreSQL (prog1_10x), API/Flask (prog1_12x), OOP (prog1_11x, prog2_3x), Godot (prog2) tēmu main lapās. Piem.: "Šodien mācāmies CRUD un tabulu saites. Vēl NErisinām autentifikāciju, migrācijas un mērogošanu — tās ir padziļināta kursa/prakses tēmas." Atbild uz 4.1 un 4.2. Šī ir vissvarīgākā un lētākā 4. esejas korekcija.

**L4.2 — "Kad NElietot klasi" punkts OOP teorijā** (mazs darbs)
prog1_11 un prog2_3 OOP teorijā pievieno īsu piezīmi: "Klase nav vienmēr labākā izvēle — vienkāršiem datiem pietiek ar vārdnīcu/struct; kompozīcija bieži ir skaidrāka par mantošanu." Atbild uz 4.3.

**L4.3 — Standartizēts README šablons `paligm.html`** (mazs darbs)
"Projekta plānošana" kategorijā pievieno README šablonu ar obligātām sekcijām: Kas tas ir / Kam domāts / Kā palaist / Atkarības / Kas nav pabeigts / Kādi dati tiek glabāti / Licence / Zināmās kļūdas. Noslēguma projektu lapas atsaucas uz to. Atbild uz 4.5.

**L4.4 — Minimāls testu artefakts noslēguma projektos** (vidējs darbs)
Noslēguma projektu pašpārbaudes sarakstos pievieno: "Pievieno `testi.md` ar tabulu: ievade → gaidītais rezultāts → faktiskais rezultāts (vismaz 3 rindas, t.sk. 1 robežgadījums)." Atbild uz 4.4 ar konkrētu, vērtējamu artefaktu, kas nav atkarīgs no infrastruktūras.

---

## 5. Filozofiskās esejas — apstiprinātās uzslavas (saglabāt, nemainīt)

Filozofiskās esejas pamatā ir uzslavējošas. Pārbaude apstiprina, ka šie spēki ir REĀLI un tos NEDRĪKST sabojāt ar augšminētajiem labojumiem:

| Uzslava | Apstiprinājums | Sekas |
|---|---|---|
| Konsekventa lapu struktūra mazina kognitīvo slodzi | Veidne tiešām vienota visos 148 failos | Visi labojumi izmanto esošās CSS klases (`info-box`, `logic-box`), nemaina veidni |
| Spirāļveida progresija (GitHub→README, validācija→try/except...) | Apstiprināms tēmu arkos | Saglabāt tēmu secību |
| "Biežākās kļūdas" kā anticipējoša rūpe | Sekcijas ir 148/148 | Tikai PAPILDINĀT ar kategorijām (L3.3), ne aizstāt |
| Publiska autorība dod aģentūru | GitHub Pages publicēšana māca reālu prasmi | Privātuma opcija (L2.3) ir PAPILDINĀJUMS, ne aizvietojums |
| Refleksija ("uzraksti secinājumus") pārvērš pieredzi mācīšanā | Klātesošs noslēguma stundās | Paplašināt ar mikro-refleksiju (L3.2) |

---

## 6. Prioritārā izpildes secība

**A. Ātrie uzvarējumi (1 sesija, augsta vērtība, zems risks):**
1. **L3.1** — pārdēvēt "līmenis" → "uzdevums" prog1_7/8 (skripts) — novērš AUDIT.md atzīmēto nekonsekvenci.
2. **L2.1** — glosārijs `paligm.html` (viena vieta, atrisina valodas barjeru visam kursam).
3. **L4.1** — "Ko šodien NEMĀCĀMIES" atrunas profesionālo rīku tēmu main lapās.
4. **L2.4** + **L2.3** — vērtēšanas atruna + privātuma opcija (īsi teikumi).

**B. Vidēja apjoma (1-2 sesijas):**
5. **L2.2** — zema-infrastruktūras alternatīvas setup lapās.
6. **L3.3** + **L4.3** — kļūdu kategoriju leģenda + README šablons `paligm.html`.
7. **L1.1** + **L1.2** — konceptuālais kodols + MVP main/projektu lapās.
8. **L3.2** — "Mācīšanās pierādījuma" mikrobloks.

**C. Lielāks darbs (plānot atsevišķi):**
9. **L1.3** — ne-spēļu projektu alternatīvas (jauns saturs).
10. **L4.4** — testu artefakti + **L4.2** OOP piezīmes.

**Apzināti NEDARĪT:**
- **L3.5** — pilnīga lapu-tipu diferenciācija (pārspīlēta kritika; sabojātu reālo navigācijas konsekvenci).

---

## 7. Kopsavilkums

No 18 izvērtētajiem eseju apgalvojumiem: **13 LEĢITĪMI**, **4 DAĻĒJI ATRISINĀTI** (galvenokārt pateicoties 2026-05-17 `main` atjauninājumam ar "Priekšzināšanu robeža" un "70 min"), **1 PĀRSPĪLĒTS** (pilnīga veidņu diferenciācija). Filozofisko eseju uzslavas par struktūru, spirāļveida progresiju un anticipējošu rūpi ir apstiprinātas un jāsaglabā.

Lielākā daļa korekciju ir **papildinājumi `paligm.html` un main lapu `info-box` blokiem**, kas izmanto jau esošās CSS klases un nemaina nodarbību veidni — tādējādi novēršot kritiku, vienlaikus saglabājot filozofisko eseju identificētos spēkus.
