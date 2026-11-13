# ebSkola

Bezmaksas atvērtā koda mācību materiāli datorikai, programmēšanai un robotikai latviešu valodā (7.–12. klasei). Projekts ir veidots kā statiska tīmekļvietne skolēniem un pedagogiem ar uzsvaru uz praktisku darbu, reāliem koda piemēriem, atvērtā pirmkoda rīkiem (`VS Code`, `Git`, `Godot 4 .NET`, `Python`, `PostgreSQL`, `Arduino`) un sasniedzamo rezultātu sasaisti ar Latvijas izglītības standartiem (MK noteikumi Nr. 416 un Nr. 747).

Publiskā vietne: <https://ebskola.lv/>

## Kursu un satura pārskats

Vietnē ir **4 kursi**, **25 tēmas** un **148 nodarbības**, kā arī vienots programmēšanas špikeris un sasniedzamo rezultātu katalogs:

| Sadaļa | Mape / fails | Klase | Apjoms | Saturs |
|---|---|---|---|---|
| **Datorika 9. klasei** | `datorika9/` | 9. klase | 5 tēmas · 30 nodarbības | Tīmekļa tehnoloģijas (`HTML`, `CSS`, `JavaScript`), dizaina domāšana, multivide, `Git`/`GitHub` darba plūsma `VS Code` vidē un pārlūkspēles izstrāde ar publicēšanu `GitHub Pages`. Katrai nodarbībai ir pilns sākuma kods `datorika9/sakuma-kodi/`. |
| **Programmēšana I** | `programmesana1/` | 10.–12. klase | 12 tēmas · 72 nodarbības | `Python` pamati, vadības struktūras, funkcijas, datu kolekcijas, datu pastāvība (`JSON`, `CSV`), algoritmi, programmatūras projektēšana, tīmekļa integrācija (`Flask`), datubāzes (`PostgreSQL` / `SQL`), OOP un izvietošana. |
| **Programmēšana II** | `programmesana2/` | 11.–12. klase | 6 tēmas · 36 nodarbības | Padziļināts 2D spēļu un lietotņu izstrādes kurss ar `Godot 4 .NET` un `C#`: *Pong*, *Platformer*, *RPG* (klases turnīra simulators), *Top-down Shooter*, *Roguelike* un publicēta *Puzzle* spēle. Ietver pilnus projektus un automatizētus testus (`prog2_1/`, `prog2_2/`). |
| **Robotika** | `robotika/` | 7.–9. klase | 2 tēmas · 10 nodarbības | Praktiska robotika un elektronika: `LEGO SPIKE Prime` kustību, sensoru un manipulatoru programmēšana un ievads `Arduino` (`C++`) shēmās un mikrokontrolieros. |
| **Palīgmateriāli** | `paligm.html` | 7.–12. klase | 15 sadaļas | Programmēšanas špikeris vienuviet: `HTML`, `CSS`, `JavaScript`, `Python`, `PostgreSQL`/`SQL`, `Git`, `VS Code` īsceļi, regulārās izteiksmes, `HTTP`/`API`, drošība, izvietošana, atkļūdošana, plānošana un EN→LV terminu vārdnīca. |
| **Sasniedzamie rezultāti** | `sasnRez.html` | 7.–12. klase | Standarta pārskats | MK noteikumu Nr. 416 un Nr. 747 sasniedzamie rezultāti datorikā un programmēšanā. |

## Tehniskā uzbūve un lokāla palaišana

Šis repozitorijs ir statiska `HTML`/`CSS`/`JavaScript` vietne bez būvēšanas (*build*) soļa vai obligāta pakotņu pārvaldnieka. Produkcijā vietne izmanto kanoniskās bezpaplašinājuma (*extensionless*) saites (piemēram, `/datorika9/dat9_11`, `/paligm`, `/sasnRez`), kuras nodrošina `_redirects` konfigurācija (Cloudflare Pages).

### Lokāla priekšskatīšana

Lai lokāli darbotos bezpaplašinājuma saites (piemēram, `/datorika9/dat9_11`), visērtāk izmantot statisko serveri, kas automātiski piesaista `.html` failus:

```bash
npx serve .
```

Ja izmanto standarta Python HTTP serveri, lapas var atvērt ar pilno `.html` ceļu (piemēram, `http://localhost:8000/datorika9/dat9_11.html`):

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
├── paligm.html                 # Programmēšanas špikeris un EN→LV terminu vārdnīca
├── sasnRez.html                # Izglītības standarta sasniedzamo rezultātu saraksts
├── _redirects                  # Kanonisko bezpaplašinājuma URL un pāradresāciju noteikumi
├── _headers                    # X-Robots-Tag galvenes palīgfailu izslēgšanai no meklētāju indeksa
├── sitemap.xml                 # Publisko lapu karte meklētājiem
├── robots.txt                  # Meklētāju indeksēšanas norādes
├── manifest.json               # Web lietotnes manifests un ikonu metadati
├── datorika9/                  # Datorika 9. klasei
│   ├── datorika9.html          # Kursa pārskats
│   ├── dat9_1main.html..5main  # 5 tēmu pārskata lapas
│   ├── dat9_11.html..dat9_56   # 30 nodarbību lapas
│   ├── git.html                # Git un GitHub palīdzības lapa
│   └── sakuma-kodi/            # Lejupielādējamie sākuma kodi (11.html..56.html, 25.zip, 26.zip, resursi)
├── programmesana1/             # Programmēšana I (Python)
│   ├── programmesana1.html     # Kursa pārskats
│   └── prog1_1/..prog1_12/     # 12 tēmu mapes (katrā prog1_Nmain.html un 6 nodarbības)
├── programmesana2/             # Programmēšana II (Godot 4 .NET un C#)
│   ├── programmesana2.html     # Kursa pārskats
│   └── prog2_1/..prog2_6/      # 6 tēmu mapes (katrā prog2_Nmain.html un 6 nodarbības)
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
  - `datorika9/`: `dat9_{T}{S}.html` un `dat9_{T}main.html` (`T` = 1..5, `S` = 1..6).
  - `programmesana1/`: `prog1_{T}/prog1_{T}{S}.html` un `prog1_{T}/prog1_{T}main.html` (`T` = 1..12, `S` = 1..6).
  - `programmesana2/`: `prog2_{T}/prog2_{T}{S}.html` un `prog2_{T}/prog2_{T}main.html` (`T` = 1..6, `S` = 1..6).
  - `robotika/`: `rbtk7_{T}{S}.html` un `rbtk7_{T}main.html` (`T` = 1..2, `S` = 1..5).
- **Standarta stundas struktūra:**
  1. Kursa augšējā josla (`.course-topbar`) un tēmas nodarbību sānjosla (`.sidebar-nav`).
  2. Stundas virsraksts `<h1>` formātā `{Tēma}.{Stunda} {Nosaukums}` un mērķis (`.lesson-goal`).
  3. Sasniedzamo rezultātu saites (`.lesson-meta`) uz `/sasnRez`.
  4. Teorijas sadaļa ar `.logic-box` skaidrojumiem, koda piemēriem un uzskatāmām tabulām.
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

## Licence

Materiāli un pirmkods ir publicēti ar MIT licenci. Skatīt [`LICENSE`](LICENSE).

