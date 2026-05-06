# ebSkola — Mācību materiālu audits un standarti

Šis dokuments fiksē mācību materiālu standartus, izmaiņu kopsavilkumu pēc 2026. maija revīzijas un katras stundas vērtējumu.

## 1. Vienoti nosaukumu standarti

| Elements | Standarts | Piemērs |
|---|---|---|
| Lapas <title> | `{Tēmas_nr}.{Stundas_nr} {Nosaukums}` | `4.5 Spēles plānošana ar shēmām` |
| Stundas h1 | `{Tēmas_nr}.{Stundas_nr} {Nosaukums}` | `4.5 Spēles plānošana ar shēmām` |
| Tēmas apkopojuma h1 | `{Tēmas_nr}. Tēma — {Nosaukums}` | `4. Tēma — Funkcijas un Modularitāte` |
| Sānu navigācijas saite | `{Tēmas_nr}.{Stundas_nr} {Īss nosaukums}` | `4.5 Spēles plānošana ar shēmām` |
| Sānu navigācijas pirmā saite | `{Tēmas_nr}. Tēmas apkopojums + Špikeris` | `4. Tēmas apkopojums + Špikeris` |
| Uzdevumu nosaukumi | `{Nr}. uzdevums: {Nosaukums}` (4. = `Papildus uzdevums:`) | `2. uzdevums: Personalizēts ziņojums` |
| Sasniedzamo rezultātu saite | `<div class="lesson-meta"><a href="../../sasnRez.html">SR {kods}. {Nosaukums}</a></div>` | `SR 2.4.15. Modulāras programmas un funkcijas` |

### Stundas struktūras paraugs

1. `<h1>` — stundas virsraksts standarta formātā
2. `<p><b>Tavs šīs stundas izaicinājums:</b> ...` — viens teikums Blūma taksonomijas darbības vārdā
3. `<div class="lesson-meta">` — sasniedzamo rezultātu kodi un īsi nosaukumi (saskaņoti ar `sasnRez.html`)
4. `<h2>Teorija: {Virsraksts}</h2>` — kompakta teorija ar koda piemēriem
5. `<h2>1. uzdevums: ...` līdz `<h2>3. uzdevums: ...` — trīs galvenie uzdevumi (kopā ~80 min)
6. `<h2>Papildus uzdevums: ...` — 4. uzdevums izvēles ātrākajiem (laiks netiek skaitīts)
7. `<h2>Biežākās kļūdas (un kā tās labot)</h2>` — preventīvi padomi
8. `<h2>Koda piemērs</h2>` (ja attiecināms)
9. `<div class="stundas-navigacija">` — pogas iepriekšējā / nākamā stundā

### Tēmas noslēguma projekts

Katra tēma noslēdzas ar **vienkāršu spēli**, kas izmanto visu, kas tēmā apgūts:

| Tēma | Beigu projekts |
|---|---|
| Programmēšana I — 1. tēma (Vide) | Personīgais GitHub repo ar dokumentāciju |
| Programmēšana I — 2. tēma (Python pamati) | "Lielais skaitļu duelītis" |
| Programmēšana I — 3. tēma (Vadības struktūras) | "Gudrais Akmens-Šķēres-Papīrīts" |
| Programmēšana I — 4. tēma (Funkcijas) | **"Skaitļu minētājs"** ★ (jauns) |
| Programmēšana I — 5. tēma (Kolekcijas) | **"Atmiņu kāršu spēle"** ★ (jauns) |
| Programmēšana I — 6. tēma (Datu pastāvība) | **"Quiz spēle ar Highscore"** ★ (jauns) |
| Programmēšana I — 7. tēma (Algoritmi) | "Slepenā koda lauzējs" |
| Programmēšana I — 8. tēma (Projektēšana) | **"Krustiņi un nullītes" arhitektūra** ★ (jauns) |
| Programmēšana I — 9. tēma (Web) | **"Krustiņi un nullītes" pārlūkā** ★ (jauns) |
| Datorika 9 — 1. tēma | Spēles projekta pieteikums |
| Datorika 9 — 2. tēma | Stilizēta spēles lapa |
| Datorika 9 — 3. tēma | Vienkārša teksta spēle JS |
| Datorika 9 — 4. tēma | Spēles dzinēja prototips |
| Datorika 9 — 5. tēma | Pilnvērtīga spēle internetā |
| Robotika — 1. tēma | LEGO SPIKE Pārbaudes misija |
| Robotika — 2. tēma | **Reakcijas spēle (Arduino)** ★ (jauns) |

★ = aizstāj iepriekšējo "CYOA / Choose Your Own Adventure" projektu, kas tika noņemts saskaņā ar 2026. maija revīziju.

## 2. Stundas laika rāmis (80 min)

- **1. uzdevums** — pamatlīmenis (~20 min)
- **2. uzdevums** — vidējs līmenis (~25 min)
- **3. uzdevums** — padziļināts (~25 min) + teorijas un kļūdu pārskats (~10 min)
- **Papildus uzdevums** — neierobežots, NETIEK ieskaitīts 80 min budžetā

Laiks stundas materiālā netiek rādīts skolēnam — tas ir paredzēts pedagogam.

## 3. Sasniedzamie rezultāti (saskaņā ar MK noteikumiem Nr. 416)

Katra stunda obligāti satur saiti uz `sasnRez.html` ar konkrētiem kodiem. Galvenais sasniedzamo rezultātu saraksts:

### Datorika 9 (Pamatkurss)
- **2.3.x** — Datortehnika un datņu pārvaldība
- **2.4.x** — Lietojumprogrammatūras lietošana
- **2.5.x** — Tiešsaistes saziņa un sadarbība
- **2.6.x** — Algoritmi un programmēšana

### Programmēšana I (Optimālais līmenis)
- **2.3.x** — Datorikas nozare un tendences
- **2.4.1.–2.4.19.** — Programmēšanas un izstrādes prasmes
- **3.1.1.** — Ergonomika un drošība
- **3.1.3.** — Intelektuālais īpašums un licences

Katras stundas `<div class="lesson-meta">` blokā ir 1–4 SR kodi ar īsiem nosaukumiem.

## 4. Vērtējumu tabula

Skala: 1 (slikti) – 5 (izcili) trijās dimensijās:
- **K** = stundas kvalitāte tēmā (cik labi tā saskan ar tēmas mērķiem)
- **F** = stundas izklaidējamība jeb interesantums skolēnam
- **T** = teorijas kvalitāte (vai viss, kas vajadzīgs uzdevumiem, tiek izskaidrots)

### Programmēšana I

| Stunda | Nosaukums | K | F | T | Piezīmes |
|---|---|---|---|---|---|
| 1.1 | Datora sagatavošana un IDE | 5 | 3 | 4 | Skaidri soļi, ergonomika minēta |
| 1.2 | GitHub un Mākoņkrātuve | 4 | 3 | 4 | Pirmais commit pieredze |
| 1.3 | Koda sinhronizācija (Desktop) | 4 | 3 | 4 | Versiju kontrole |
| 1.4 | Failu sistēma un organizācija | 3 | 2 | 4 | Sausa, bet nepieciešama |
| 1.5 | Dokumentēšana un README | 4 | 3 | 5 | Markdown labi pasniegts |
| 1.6 | Noslēguma projekts | 4 | 3 | 4 | Personīgs repo |
| 2.1 | Ievade un datu tipi | 5 | 4 | 5 | Stabils pamats |
| 2.2 | Interaktivitāte un konvertācija | 5 | 4 | 4 | Daudz piemēru |
| 2.3 | Matemātika un f-strings | 5 | 4 | 5 | f-string ir spēcīgs rīks |
| 2.4 | Koda stils un komentāri | 4 | 3 | 4 | PEP 8 ievads |
| 2.5 | Spēles plānošana | 4 | 4 | 4 | Algoritmu shēmas |
| 2.6 | "Lielais skaitļu duelītis" | 5 | 5 | 4 | Pirmā spēle |
| 3.1 | Zarošanās un operatori | 5 | 4 | 5 | Izcili ievads if/else |
| 3.2 | Loģiskie operatori | 5 | 4 | 4 | And/Or/Not skaidri |
| 3.3 | While cikli un kontrole | 5 | 4 | 5 | break/continue |
| 3.4 | Kļūdu apstrāde un validācija | 4 | 3 | 5 | try/except labi izklāstīts |
| 3.5 | Saraksti un For cikli | 5 | 4 | 4 | Saites uz nākamo tēmu |
| 3.6 | "Gudrais Akmens-Šķēres-Papīrīts" | 5 | 5 | 4 | Iemīļota spēle |
| 4.1 | Funkciju definēšana un parametri | 5 | 4 | 5 | Receptes analoģija |
| 4.2 | Vērtību atgriešana (return) | 5 | 4 | 5 | Skaidrs scope ievads |
| 4.3 | Modularitāte un koda sadalīšana | 4 | 3 | 4 | Imports tiek izskaidrots |
| 4.4 | Lokālie/globālie mainīgie un vārdnīcas | 4 | 4 | 4 | Vārdnīcas pirmais ievads |
| 4.5 | Spēles plānošana ar shēmām | 5 | 4 | 5 | Pārstrādāts uz "Skaitļu minētāju" |
| 4.6 | Noslēguma projekts: Skaitļu minētājs | 5 | 5 | 5 | ★ jauns saturs, vienkārša spēle |
| 5.1 | Saraksti (list) un to metodes | 5 | 4 | 5 | Append/pop demonstrēti |
| 5.2 | Vārdnīcas (dict) | 5 | 4 | 5 | Atslēga-vērtība |
| 5.3 | For cikli un iterācija | 5 | 4 | 5 | Iter caur kolekcijām |
| 5.4 | Google Forms aptauja | 3 | 4 | 3 | Kontekstuāli nepieciešama |
| 5.5 | Aptaujas datu analīze un integrācija | 4 | 3 | 4 | Izņemta CYOA atsauce |
| 5.6 | Noslēguma projekts: Atmiņu kāršu spēle | 5 | 5 | 5 | ★ jauns saturs |
| 6.1 | Failu lasīšana un rakstīšana | 5 | 3 | 5 | with open() pamati |
| 6.2 | Google Sheets un eksports | 4 | 3 | 4 | Praktisks rīks |
| 6.3 | Datu tīrīšana un transformācija | 4 | 3 | 4 | Strip/replace |
| 6.4 | Rezultātu tabulas (Highscores) | 5 | 5 | 5 | Pastāvīga spēles atmiņa |
| 6.5 | Datu vizualizācija un analīze | 4 | 4 | 4 | matplotlib ievads |
| 6.6 | Noslēguma projekts: Quiz spēle | 5 | 5 | 5 | ★ jauns saturs |
| 7.1 | Lineārā pret bināro meklēšanu | 5 | 4 | 5 | Klasisks algoritmu temats |
| 7.2 | Kārtošanas loģika | 4 | 4 | 4 | Bubble + sort |
| 7.3 | Big O notācija | 4 | 3 | 4 | Sausa, bet svarīga |
| 7.4 | Iebūvēto funkciju efektivitāte | 4 | 3 | 4 | timeit ievads |
| 7.5 | Algoritmu pielietojums spēlēs | 5 | 5 | 4 | AI mājieni |
| 7.6 | Noslēguma projekts: Slepenā koda lauzējs | 5 | 5 | 4 | Kriptogrāfijas spēle |
| 8.1 | Problēmas formulēšana un automatizācija | 4 | 3 | 4 | Pielāgots Krustiņiem |
| 8.2 | Lietotāju stāsti (User Stories) | 4 | 3 | 4 | Standarta formāts |
| 8.3 | Datu modelis un UI plūsma | 4 | 3 | 4 | ER diagrammas |
| 8.4 | Pitch sagatavošana | 4 | 4 | 4 | Mīkstās prasmes |
| 8.5 | Sasniedzamie rezultāti un resursi | 3 | 3 | 4 | Plānošana |
| 8.6 | Projektējuma aizstāvēšana | 4 | 4 | 3 | Prezentācija |
| 9.1–9.5 | Web (Flask/Streamlit) lessons | — | — | — | Stub failu — saturs vēl izstrādājams |
| 9.6 | Noslēguma projekts: Krustiņi pārlūkā | 5 | 5 | — | ★ definēts main lapā |

### Datorika 9. klasei

| Stunda | Nosaukums | K | F | T | Piezīmes |
|---|---|---|---|---|---|
| 1.1 | Izstrādes vide un GitHub | 4 | 3 | 4 | Live Server + Git |
| 1.2 | HTML skelets un satura strukturēšana | 5 | 4 | 5 | Semantika |
| 1.3 | Dizaina pētniecība un tirgus analīze | 4 | 4 | 3 | Konkurence |
| 1.4 | Spēles koncepcija un mērķauditorija | 5 | 5 | 4 | Persona izveide |
| 1.5 | UX/UI pamati un spēles prototipēšana | 5 | 5 | 4 | Wireframe |
| 1.6 | Noslēguma projekts: Spēles pieteikums | 4 | 4 | 4 | Pitch dokuments |
| 2.1 | CSS pamati un vizuālā ergonomika | 5 | 4 | 5 | Selektori |
| 2.2 | Izkārtojuma kontrole un Box Model | 5 | 4 | 5 | Flex/Grid ievads |
| 2.3 | Grafisko resursu sagatavošana | 4 | 4 | 4 | Optimizācija |
| 2.4 | Audio materiālu apstrāde | 4 | 4 | 4 | Audio tags |
| 2.5 | Datņu sistēmas organizēšana | 3 | 3 | 4 | ZIP arhīvi |
| 2.6 | Noslēguma projekts: Stilizēta spēles lapa | 5 | 5 | 4 | Vizuālā prezentācija |
| 3.1 | Ievads JavaScript un mainīgie | 5 | 4 | 5 | let/const |
| 3.2 | Datu tipi un interaktivitāte | 5 | 4 | 5 | I/O |
| 3.3 | Loģiskie operatori un sazarojumi | 5 | 4 | 5 | If/Else |
| 3.4 | Masīvi un datu strukturēšana | 5 | 4 | 5 | Array metodes |
| 3.5 | Cikli un atkārtošanās loģika | 5 | 4 | 5 | for/while |
| 3.6 | Noslēguma projekts: Teksta spēle JS | 5 | 5 | 4 | Pārbaudes darbs |
| 4.1 | Funkcijas un koda atkārtota izmantošana | 5 | 4 | 5 | Modularitāte |
| 4.2 | Notikumu klausītāji (Event Listeners) | 5 | 5 | 5 | Interaktivitāte |
| 4.3 | DOM manipulācija | 5 | 5 | 5 | Dinamiska maiņa |
| 4.4 | Laika kontrole (Timers) un spēles cikls | 5 | 5 | 4 | setInterval |
| 4.5 | Sadursmju noteikšana | 5 | 5 | 4 | Bounding box |
| 4.6 | Noslēguma projekts: Spēles prototips | 5 | 5 | 4 | Spēlējams MVP |
| 5.1 | Projekta specifikācija un laika plānošana | 4 | 3 | 4 | Roadmap |
| 5.2 | Vizuālo resursu un saskarnes pabeigšana | 5 | 4 | 4 | Polish |
| 5.3 | Spēles pamatloģikas programmēšana | 5 | 5 | 4 | Mehānika |
| 5.4 | Papildfunkciju ieviešana | 5 | 5 | 4 | Power-ups, līmeņi, skaņa |
| 5.5 | Spēles testēšana, atkļūdošana, publicēšana | 5 | 4 | 4 | GitHub Pages |
| 5.6 | Noslēguma projekts: Spēle internetā | 5 | 5 | 4 | Publicēta spēle |

### Robotika

| Stunda | Nosaukums | K | F | T | Piezīmes |
|---|---|---|---|---|---|
| 1.1 | Ievads LEGO SPIKE un pamatkustības | 5 | 5 | 4 | Vizuāla programmēšana |
| 1.2 | Distances sensors | 5 | 5 | 4 | Šķēršļu izvairīšanās |
| 1.3 | Krāsu sensors un līniju sekotājs | 5 | 5 | 4 | Klasisks uzdevums |
| 1.4 | Manipulatori (Satvērējs) | 5 | 5 | 4 | Trešā ass |
| 1.5 | Noslēguma projekts: Pārbaudes misija | 5 | 5 | 4 | Sintēzes uzdevums |
| 2.1 | Ievads Arduino un Tinkercad | 5 | 5 | 5 | Pirmais Arduino |
| 2.2 | Pogas un If-Else | 5 | 5 | 5 | INPUT_PULLUP |
| 2.3 | Analogie signāli (Potenciometrs) | 5 | 5 | 4 | analogRead |
| 2.4 | Servo motors | 5 | 5 | 4 | Aktuatori |
| 2.5 | Noslēguma projekts: Reakcijas spēle | 5 | 5 | 5 | ★ pārstrādāts no Morzes koda |

## 5. CSS optimizācijas (style.css)

Galvenās izmaiņas studenta lasīšanas ērtībai:
- Pievienots **Inter** fonts prozas tekstam, **JetBrains Mono** atstāts tikai kodam
- Palielināts `line-height: 1.65` un `font-size: 17px`
- `h2` saglabā nepārtrauktu lasīšanas ritmu (noņemts `min-height: 60px`)
- Pievienots `:focus-visible` ar dzeltenu kontūru pieejamībai (a11y)
- `code` izceltam zelta krāsa (`#FFD580`) virs paneļa fona
- `.code-example .result` blokam pievienots "▶ Izvade" virsraksts
- `.lesson-meta` jauns CSS bloks SR kodu kompaktai izvietošanai
- `.info-box` (ar oranžu apmali) atšķirams no `.logic-box`
- Atjaunoti responsīvie pārtraukumi 1100/1000/850/700px

## 6. Veiktās izmaiņas (2026. maijs)

1. **Vienota nosaukumu konvencija** — visi tēmu/stundu nosaukumi sānjoslās, virsrakstos un saites tagos saskan ar `{Tēmas_nr}.{Stundas_nr}` formātu.
2. **CYOA atsauces izņemtas** — visi `Choose Your Own Adventure` un `CYOA` saturoši elementi aizstāti ar konkrētām vienkāršām spēlēm (Skaitļu minētājs, Atmiņu kāršu spēle, Quiz, Krustiņi un nullītes, Reakcijas spēle).
3. **3+1 uzdevumu modelis** — galvenās stundas nodod 3 uzdevumus (~80 min) un 4. "Papildus uzdevums" (laiks netiek skaitīts).
4. **Tēmas noslēguma projekti** — katrai tēmai noslēgumā ir vienkārša spēle, kas integrē visu tēmā apgūto.
5. **Sasniedzamo rezultātu sasaiste** — katra stunda satur `lesson-meta` saiti uz konkrētiem MK 416 noteikumu kodiem.
6. **CSS uzlabojumi** — lasīšanas ērtība, fokusa kontūras, koda izcēlumi.
7. **Tēmas apkopojuma saites** — visās stundās sānjoslā parādās `Tēmas apkopojums + Špikeris`.
8. **Robotika integrēta sānjoslā** — tagad ar `has-sidebar` un Arduino tēmas pārstrādes uz Reakcijas spēli.

## 7. Atvērtie uzdevumi (nav atrisināti šajā revīzijā)

- `programmesana1/prog1_9/prog1_9{1..6}.html` ir tukši (saturs vēl izstrādājams).
- `programmesana1/prog1_10main.html`, `prog1_11main.html`, `prog1_12main.html` ir tukši stubi.
- `paligm.html` (palīgmateriāli) ir tukšs.
- Programmēšana II (padziļinātais kurss) vēl nav strukturēts.
