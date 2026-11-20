# ebSkola

Bezmaksas atvērtā koda mācību materiāli datorikai, programmēšanai un robotikai latviešu valodā (7.–12. klasei). Projekts ir veidots kā statiska tīmekļvietne skolēniem un pedagogiem ar uzsvaru uz praktisku darbu, reāliem koda piemēriem, atvērtā pirmkoda rīkiem (`VS Code`, `Git`, `Godot 4 .NET`, `Python`, `PostgreSQL`, `Arduino`) un sasniedzamo rezultātu sasaisti ar Latvijas izglītības standartiem (MK noteikumi Nr. 416 un Nr. 747).

Publiskā vietne: <https://ebskola.lv/>

## Kursu un satura pārskats

Vietnē ir **4 kursi**, **25 tēmas** un **148 nodarbības** (vēl 4 Programmēšanas I un 4 Programmēšanas II tēmas tiek izstrādātas), kā arī vienots programmēšanas špikeris un sasniedzamo rezultātu katalogs:

| Sadaļa | Mape / fails | Klase | Apjoms | Saturs |
|---|---|---|---|---|
| **Datorika 9. klasei** | `datorika9/` | 9. klase | 5 tēmas · 30 nodarbības | Tīmekļa tehnoloģijas (`HTML`, `CSS`, `JavaScript`), dizaina domāšana, multivide, `Git`/`GitHub` darba plūsma `VS Code` vidē un pārlūkspēles izstrāde ar publicēšanu `GitHub Pages`. Katrai nodarbībai ir pilns sākuma kods `datorika9/sakuma-kodi/`. |
| **Programmēšana I** | `programmesana1/` | 10.–12. klase | 16 tēmas (7., 9., 12. un 15. tiek izstrādāta) · 72 nodarbības | `Python` pamati, vadības struktūras, funkcijas, datu kolekcijas, datu pastāvība (`JSON`, `CSV`), algoritmi, programmatūras projektēšana, tīmekļa integrācija (`Flask`), datubāzes (`PostgreSQL` / `SQL`), OOP un izvietošana. |
| **Programmēšana II** | `programmesana2/` | 11.–12. klase | 10 tēmas (6., 7., 9. un 10. tiek izstrādāta) · 36 nodarbības | Padziļināts 2D spēļu un lietotņu izstrādes kurss ar `Godot 4 .NET` un `C#`: *Pong*, *Platformer*, *RPG* (klases turnīra simulators), *Top-down Shooter*, *Roguelike* un publicēta *Puzzle* spēle. Ietver pilnus projektus un automatizētus testus (`prog2_1/`, `prog2_2/`). |
| **Robotika** | `robotika/` | 7.–9. klase | 2 tēmas · 10 nodarbības | Praktiska robotika un elektronika: `LEGO SPIKE Prime` kustību, sensoru un manipulatoru programmēšana un ievads `Arduino` (`C++`) shēmās un mikrokontrolieros. |
| **Palīgmateriāli** | `paligm.html` | 7.–12. klase | 15 sadaļas | Programmēšanas špikeris vienuviet: `HTML`, `CSS`, `JavaScript`, `Python`, `PostgreSQL`/`SQL`, `Git`, `VS Code` īsceļi, regulārās izteiksmes, `HTTP`/`API`, drošība, izvietošana, atkļūdošana, plānošana un EN→LV terminu vārdnīca. |
| **Sasniedzamie rezultāti** | `sasnRez.html` | 7.–12. klase | Standarta pārskats | MK noteikumu Nr. 416 un Nr. 747 sasniedzamie rezultāti datorikā un programmēšanā. |

## Tehniskā uzbūve un lokāla palaišana

Šis repozitorijs ir statiska `HTML`/`CSS`/`JavaScript` vietne bez būvēšanas (*build*) soļa vai obligāta pakotņu pārvaldnieka. Produkcijā vietne izmanto kanoniskās bezpaplašinājuma (*extensionless*) saites (piemēram, `/datorika9/dat9_1/nodarbibas/dat9_11`, `/paligm`, `/sasnRez`), kuras nodrošina `_redirects` konfigurācija (Cloudflare Pages).

### Lokāla priekšskatīšana

Lai lokāli darbotos bezpaplašinājuma saites (piemēram, `/datorika9/dat9_1/nodarbibas/dat9_11`), visērtāk izmantot statisko serveri, kas automātiski piesaista `.html` failus:

```bash
npx serve .
```

Ja izmanto standarta Python HTTP serveri, lapas var atvērt ar pilno `.html` ceļu (piemēram, `http://localhost:8000/datorika9/dat9_1/nodarbibas/dat9_11.html`):

```bash
python3 -m http.server 8000
```

### Godot C# projektu tehniskā pārbaude (`Programmēšana II`)

1. un 2. tēmai (`prog2_1` un `prog2_2`) ir automatizēti kompilācijas un spēles loģikas testi (`SmokeTest.cs`), ko var palaist ar lokāli uzstādītu `Godot 4 .NET` un `.NET SDK`:

```bash
python3 programmesana2/prog2_1/parbaudes/check.py --godot /cels/uz/Godot.NET --dotnet /cels/uz/dotnet
python3 programmesana2/prog2_2/parbaudes/check.py --godot /cels/uz/Godot.NET --dotnet /cels/uz/dotnet
```

## Repozitorija struktūra

```text
.
├── index.html                  # Galvenā sākumlapa un kursu/tēmu indekss
├── style.css                   # Globālais dizains, krāsu sistēma un sākumlapas/pārskatu stili
├── lesson.css                  # Kopīgais nodarbību izkārtojums (.course-lesson), SLA tabulas un drukas stili
├── lesson.js                   # Sākuma koda kopēšana ([data-copy]) un soļu progress (localStorage)
├── test.css                    # Atkārtojuma testu lapu (*_test.html) stili
├── test.js                     # Atkārtojuma testu vērtēšana un rezultāta nosūtīšana uz /api/tests
├── functions/api/tests.js      # Cloudflare Pages funkcija: ieraksta testa rezultātu Google Sheets tabulā
├── paligm.html                 # Programmēšanas špikeris un EN→LV terminu vārdnīca
├── sasnRez.html                # Izglītības standarta sasniedzamo rezultātu saraksts
├── _redirects                  # Kanonisko bezpaplašinājuma URL un pāradresāciju noteikumi
├── _headers                    # X-Robots-Tag galvenes palīgfailu izslēgšanai no meklētāju indeksa
├── sitemap.xml                 # Publisko lapu karte meklētājiem
├── robots.txt                  # Meklētāju indeksēšanas norādes
├── manifest.json               # Web lietotnes manifests un ikonu metadati
├── datorika9/                  # Datorika 9. klasei
│   ├── datorika9.html          # Kursa pārskats
│   ├── dat9_1/..dat9_5/        # 5 tēmu mapes (katrā dat9_Nmain.html — tēmas pārskats)
│   │   ├── nodarbibas/         # 6 tēmas nodarbību lapas (dat9_N1.html..dat9_N6.html)
│   │   └── testi/              # Atkārtojuma testi dat9_NS_test.html (mape ir arī tēmām bez testiem)
│   ├── git.html                # Git un GitHub palīdzības lapa
│   ├── priekskatijumi.css      # Kopīgie priekšskatījumu stili kursa un tēmu pārskatiem
│   ├── img/                    # Kopīgie attēli (piem., git.html ekrānšāviņš)
│   └── sakuma-kodi/            # Lejupielādējamie sākuma kodi (11.html..56.html, 25.zip, 26.zip, resursi)
├── programmesana1/             # Programmēšana I (Python)
│   ├── programmesana1.html     # Kursa pārskats
│   └── prog1_1/..prog1_16/     # 16 tēmu mapes (katrā prog1_Nmain.html un 6 nodarbības; 7., 9., 12. un 15. tēmā pagaidām tikai plāns prog1_Nplan.md)
│       └── testi/              # Atkārtojuma testi prog1_NS_test.html (visās izveidotajās tēmās)
├── programmesana2/             # Programmēšana II (Godot 4 .NET un C#)
│   ├── programmesana2.html     # Kursa pārskats
│   └── prog2_1/..prog2_10/     # 10 tēmu mapes (katrā prog2_Nmain.html un 6 nodarbības; 6., 7., 9. un 10. tēmā pagaidām tikai plāns prog2_Nplan.md)
│       └── testi/              # Atkārtojuma testi prog2_NS_test.html (visās izveidotajās tēmās)
│       ├── kods/               # Starpposmu C# skripti (1. un 2. tēmā)
│       ├── parbaudes/          # Automatizētie Godot/C# pārbaudes skripti (1. un 2. tēmā)
│       └── pong/, platformer/  # Pilni izpildāmi paraugprojekti un to .zip arhīvi
└── robotika/                   # Robotika (7.–9. klase)
    ├── robotika.html           # Kursa pārskats
    ├── rbtk7_1main.html..2main # 2 tēmu pārskata lapas (LEGO SPIKE un Arduino)
    └── rbtk7_11.html..rbtk7_25 # 10 nodarbību lapas
```

## Nodarbību uzbūve un konvencijas

Visu kursu nodarbības izmanto vienotu lasīšanas izkārtojumu (`style.css` + `lesson.css` + `lesson.js`) un `<body class="page-reference course-lesson has-sidebar">`:

- **Failu numerācija:**
  - `datorika9/`: `dat9_{T}/nodarbibas/dat9_{T}{S}.html`, `dat9_{T}/testi/dat9_{T}{S}_test.html` un `dat9_{T}/dat9_{T}main.html` (`T` = 1..5, `S` = 1..6). Kopīgie faili (`datorika9.html`, `git.html`, `priekskatijumi.css`, `img/`, `sakuma-kodi/`) paliek kursa mapes saknē.
  - `programmesana1/`: `prog1_{T}/prog1_{T}{S}.html`, `prog1_{T}/testi/prog1_{T}{S}_test.html` un `prog1_{T}/prog1_{T}main.html` (`T` = 1..16, `S` = 1..6).
  - `programmesana2/`: `prog2_{T}/prog2_{T}{S}.html`, `prog2_{T}/testi/prog2_{T}{S}_test.html` un `prog2_{T}/prog2_{T}main.html` (`T` = 1..10, `S` = 1..6).
  - `robotika/`: `rbtk7_{T}{S}.html` un `rbtk7_{T}main.html` (`T` = 1..2, `S` = 1..5).
- **Standarta stundas struktūra:**
  1. Kursa augšējā josla (`.course-topbar`) un tēmas nodarbību sānjosla (`.sidebar-nav`).
  2. Stundas virsraksts `<h1>` formātā `{Tēma}.{Stunda} {Nosaukums}` un mērķis (`.lesson-goal`).
  3. Sasniedzamo rezultātu saites (`.lesson-meta`) uz `/sasnRez`.
  4. Teorijas sadaļa ar `.logic-box` skaidrojumiem, koda piemēriem un uzskatāmām tabulām. *(Datorika 9 un Programmēšana I no 1.2; Programmēšana II no 1.2)* Teorijas sadaļas (`<section id="teorija">`) pašā sākumā, tieši zem `<h2>`, ir poga `<p class="start-test" id="atkartojuma-tests"><a class="btn primary start-test-btn" href="…_test">Sākt testu →</a></p>` uz nodarbības atkārtojuma testu — tas ir skolēna pirmais darbs pirms jaunās teorijas.
  5. *(Datorika 9)* Sākuma koda bloks (`#sakuma-kods`) ar kopēšanas pogu (`data-copy="pilnais-kods"`) un lejupielādes saiti no `sakuma-kodi/`.
  6. Trīs secīgi pamatuzdevumi (`<section class="logic-box lesson-task" id="uzdevums-1">` līdz `id="uzdevums-3">`), katrā numurēti soļi `<ol class="step-list">` un pabeigtības kritērijs `<p class="done-when">`. Skripts `lesson.js` visiem `.lesson-task > .step-list > li` elementiem automātiski pievieno izvēles rūtiņas un saglabā progresu pārlūka `localStorage`.
  7. Izvēles papildu uzdevums (`<details class="course-help extra-task">`).
  8. Biežāko kļūdu / diagnostikas sadaļa, iesniegšanas kritēriji (`.submission` vai `.hand-in-box`) un tēmu noslēguma projektos — četru līmeņu snieguma līmeņu apraksta (SLA) tabula (`.assessment-rubric`).
  9. Navigācija uz iepriekšējo un nākamo nodarbību (`.stundas-navigacija`).
- **SEO un saites:** iekšējās saites starp lapām izmanto bezpaplašinājuma ceļus (piemēram, `/programmesana1/prog1_1/prog1_11`), un katras lapas `<head>` satur kanonisko URL, Open Graph metadatus un `Schema.org` (`LearningResource`, `BreadcrumbList`) strukturētos datus.

## Jaunas nodarbības pievienošana vai esošas atjaunošana

1. Izvēlies atbilstošo kursa un tēmas mapi un par pamatu paņem blakus esošu tā paša kursa nodarbību.
2. Atjauno `<head>` metadatus (`<title>`, `meta[name="description"]`, `link[rel="canonical"]`, `og:*` un JSON-LD `LearningResource`/`BreadcrumbList`).
3. Atjauno `<h1>`, `.lesson-goal`, `.lesson-meta` saites, teoriju, 3 pamatuzdevumus (`#uzdevums-1`..`#uzdevums-3`), papildu uzdevumu un `.stundas-navigacija`.
4. Ja mainās `Datorika 9` nodarbības sākuma kods, sinhroni atjauno gan nodarbības HTML failā iekodēto `#pilnais-kods` bloku, gan attiecīgo failu mapē `datorika9/sakuma-kodi/`.
5. Ja pievieno jaunu lapu:
   - pievieno saiti tēmas `*main.html` lapā un visās attiecīgās tēmas nodarbību `.sidebar-nav` izvēlnēs;
   - pievieno `.html` → bezpaplašinājuma pāradresācijas likumu failā `_redirects`;
   - pievieno jauno kanonisko URL failā `sitemap.xml`.

## Atkārtojuma testi

Tests `datorika9/dat9_{T}/testi/dat9_{T}{S}_test.html`, `programmesana1/prog1_{T}/testi/prog1_{T}{S}_test.html` vai `programmesana2/prog2_{T}/testi/prog2_{T}{S}_test.html` ir domāts nodarbības `{T}.{S}` sākumam un atkārto **iepriekšējo** nodarbību (piemēram, `dat9_12_test.html` jautā par 1.1). Skolēns atsevišķos laukos ieraksta vārdu un uzvārdu (`name="vards"`, `name="uzvards"`), izvēlas klasi un atbild uz pieciem jautājumiem. Pēc iesniegšanas lapa parāda pareizās atbildes, bet `test.js` nosūta rezultātu uz `/api/tests`, kur `functions/api/tests.js` to pievieno kā jaunu rindu Google Sheets tabulā (laiks, tests, klase, vārds, uzvārds, punkti, jautājumu skaits, katra atbilde).

- **Kursi, klases un tabulas lapas:** kursu nosaka `data-test` sākums, un katram kursam ir sava tabulas lapa (cilne), ko atrod pēc tās kārtas, nevis nosaukuma (sarakstu `COURSES` skati failā `functions/api/tests.js`):
  - `dat9_…` — klases 9.a, 9.b, 9.c → **1.** lapa;
  - `prog1_…` — klases 11.a, 11.b, 11.c, 12.a, 12.b, 12.c → **2.** lapa;
  - `prog2_…` — klases 12.a, 12.b, 12.c → **3.** lapa. Tabulā jābūt vismaz trim lapām; virsraksta rindu tukšā lapā funkcija ieraksta pati.

  Klase, kas neatbilst kursam, tiek noraidīta, tāpēc jaunai klasei vai kursam papildini gan `<select name="klase">` testu lapās, gan `COURSES`.

- **Jauns tests:** nokopē esošu `*_test.html` tēmas mapē `testi/`, nomaini virsrakstu, saites un `data-test` vērtību. Katram jautājumam ir `<fieldset class="test-question" data-correct="b">` ar četrām atbildēm (`value="a"`..`"d"`) un skaidrojumu `.test-explain`. Pievieno pāradresāciju failā `_redirects` un nodarbības teorijas sākumā pogu `.start-test` ar saiti uz testu (nokopē no citas nodarbības un nomaini saiti). Testu lapas nav meklētāju indeksā (`noindex`) un nav jāpievieno `sitemap.xml`.
- **Google Sheets pieslēgums (vienreiz):** Google Cloud projektā ieslēdz *Google Sheets API*, servisa kontam izveido JSON atslēgu, tabulu kopīgo ar servisa konta e-pastu kā redaktoram un Cloudflare Pages iestatījumos pievieno noslēpumu `GOOGLE_SERVICE_ACCOUNT_JSON` ar visu JSON faila saturu. Atslēgas failu repozitorijā neglabā. Pārbaude: `https://ebskola.lv/api/tests` atbild `{"ok":true,"sheet":"connected","header":"current","tabs":{"dat9":"current","prog1":"current","prog2":"current"}}` (`"empty"` — lapā vēl nav neviena rezultāta, `"missing"` — tabulā nav tik daudz lapu).
- **Tabula bez kolonnas „Uzvārds”:** ja pārbaude atbild `"header":"old"`, tabula izveidota pirms vārda un uzvārda sadalīšanas, un rezultāti tiek rakstīti ar pilnu vārdu kolonnā „Vārds”. Ar peles labo pogu uzklikšķini uz kolonnas E („Punkti”) burta → *Insert 1 column left* un šūnā E1 ieraksti `Uzvārds`. Turpmākie rezultāti uzvārdu rakstīs atsevišķi; vecās rindas paliek ar pilnu vārdu kolonnā „Vārds”.
- Funkcija darbojas tikai publicētajā vietnē. Lokālā priekšskatījumā tests novērtē atbildes, bet rezultātu nenosūta.

## Licence

Materiāli un pirmkods ir publicēti ar MIT licenci. Skatīt [`LICENSE`](LICENSE).

