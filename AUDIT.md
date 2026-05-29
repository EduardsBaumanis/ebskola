# ebSkola repo audits

Atjaunots: **2026-05-19**
Pārbaudītā versija: `main` pie `44a401e Fix canonical urls and redirects`

Šis audits aizstāj iepriekšējo 2026-05-17 mācību satura auditu. Jaunais audits skatās visu repozitoriju kā publicētu statisku mācību vietni: SEO, sitemap/robots, Cloudflare pāradresācijas, iekšējās saites, HTML metadatus, pieejamību, satura struktūru un uzturēšanas riskus.

## 1. Kopsavilkums

Kopējais stāvoklis: **labs, bet ar vienu svarīgu SEO risku**.

Pēc pēdējām izmaiņām vietnes kanoniskā adrese ir konsekventi pārcelta uz `https://ebskola.lv`, `.html` URL vairs netiek lietoti kā kanoniskie URL, sitemap ir derīgs, un vecie `.html` URL tiek pāradresēti uz extensionless adresēm.

Svarīgākais atlikušais risks: **neeksistējoši URL vēl arvien dzīvajā vietnē atgriež `200 OK` un rāda sākumlapu**. Tas var radīt Google Search Console kļūdas par dublikātiem, soft 404 vai lapām ar citu kanonisko adresi.

## 2. Repo apjoms

| Daļa | Skaits |
|---|---:|
| Kopā izsekoti faili | 258 |
| HTML faili | 181 |
| Publicētās HTML lapas | 176 |
| `sagataves/` HTML faili | 5 |
| CSS faili | 1 |
| XML faili | 1 |
| Sitemap URL | 176 |
| `_redirects` noteikumi | 231 |

HTML sadalījums:

| Mape/fails | HTML lapas |
|---|---:|
| `datorika9/` | 35 |
| `programmesana1/` | 84 |
| `programmesana2/` | 42 |
| `robotika/` | 12 |
| Saknes lapas (`index`, `paligm`, `sasnRez`) | 3 |
| `sagataves/` | 5 |

## 3. SEO un indeksācija

| Pārbaude | Rezultāts | Statuss |
|---|---:|---|
| `sitemap.xml` parsējas kā XML | jā | OK |
| Sitemap URL skaits | 176 | OK |
| Sitemap URL ar `.html` beigās | 0 | OK |
| Sitemap URL ārpus `https://ebskola.lv` | 0 | OK |
| Dublikāti sitemap `<loc>` laukos | 0 | OK |
| `robots.txt` norāda uz `https://ebskola.lv/sitemap.xml` | jā | OK |
| Publicētās lapas ar vienu `canonical` | 176/176 | OK |
| Publicētās lapas ar vienu `og:url` | 176/176 | OK |
| `canonical` sakrīt ar extensionless faila ceļu | 176/176 | OK |
| `og:url` sakrīt ar extensionless faila ceļu | 176/176 | OK |
| JSON-LD bloki parsējas | 176/176 | OK |
| Vecais GitHub Pages domēns repo saturā | 0 atradumi | OK |
| Nevēlami `https://ebskola.lv/...html` metadatos | 0 atradumi | OK |

Secinājums: **lokālais SEO stāvoklis ir sakārtots**. Sitemap, canonical, Open Graph un JSON-LD tagi tagad rāda vienu un to pašu extensionless URL sistēmu.

## 4. Cloudflare un redirects

`_redirects` sintakse pārbaudīta:

- 231 aktīvi noteikumi;
- 0 dublēti redirect avoti;
- 0 nepareizas formas noteikumi.

Dzīvajā vietnē pārbaudītie piemēri:

| URL | Rezultāts |
|---|---|
| `https://ebskola.lv/robots.txt` | `200 OK` |
| `https://ebskola.lv/sitemap.xml` | `200 OK` |
| `https://ebskola.lv/index.html` | `301 -> / -> 200` |
| `https://ebskola.lv/datorika9/dat9_14.html` | `301 -> /datorika9/dat9_14 -> 200` |
| `https://ebskola.lv/programmesana1/prog1_3main.html` | `301 -> /programmesana1/prog1_3/prog1_3main -> 200` |
| `https://ebskola.lv/par.html` | `301 -> / -> 200` |
| GSC redzētais garais dublikāta URL ar `datorika9/dat9_3main.html` | `301 -> /datorika9/dat9_3main -> 200` |
| GSC redzētais garais dublikāta URL ar `prog1_6main.html` | `301 -> /programmesana1/prog1_6/prog1_6main -> 200` |

Atlikušais risks:

| URL | Rezultāts | Problēma |
|---|---|---|
| `https://ebskola.lv/this-definitely-does-not-exist` | `200 OK` | Neeksistējoša lapa tiek rādīta kā derīga lapa |

Šis ir svarīgākais nākamais labojums. Kamēr neeksistējošas adreses atgriež `200 OK`, Google var turpināt atrast nejaušas vai kļūdainas adreses un klasificēt tās kā dublikātus vai soft 404.

Ieteikums: izveidot pārbaudītu 404 risinājumu Cloudflare Pages vidē. To vajag testēt uzmanīgi, lai netiktu salauztas īstās extensionless lapas.

## 5. Iekšējās saites

| Pārbaude | Rezultāts |
|---|---:|
| Pārbaudīti `<a>` tagi | 2547 |
| Root-relative lokālās saites | 2526 |
| Lokālās saites uz neeksistējošiem mērķiem | 0 |
| Faktiskas iekšējās `<a href="...html">` saites | 0 |
| Relatīvās publicēto lapu navigācijas saites | 0 |

Secinājums: iekšējā navigācija tagad ir daudz drošāka nekā iepriekš. Saites ir root-relative (`/datorika9/dat9_14`), tāpēc nejauši dziļi URL vairs neveidos kļūdainus ceļus kā `programmesana1/programmesana1/...`.

## 6. Pieejamība un HTML higiēna

| Pārbaude | Rezultāts |
|---|---:|
| HTML faili ar `<h1>` | 181/181 |
| Attēlu tagi | 65 |
| Attēli bez `alt` | 0 |
| Publicētās lapas ar canonical | 176/176 |
| Publicētās lapas ar `lang="lv"` | 176/176 |
| Publicētās lapas ar viewport meta | 176/176 |

Nelielas problēmas:

1. `sagataves/par.html`, `sagataves/paligm.html`, `sagataves/devitaKlase1.html` trūkst `lang="lv"`.
2. Visiem 5 `sagataves/` HTML failiem trūkst `viewport` meta vai tas nav konsekvents.
3. `programmesana1/prog1_8/prog1_83.html` ir viena ārējā saite ar `target="_blank"`, bet bez `rel="noopener noreferrer"`.

Tā kā `sagataves/` ir bloķēta `robots.txt`, tas nav kritisks indeksācijas risks, bet repozitorija kvalitātei būtu labi arī sagataves uzturēt pēc tā paša HTML standarta.

## 7. Mācību satura struktūra

Mācību lapas:

| Kurss | Nodarbību lapas |
|---|---:|
| Datorika 9 | 30 |
| Robotika | 10 |
| Programmēšana I | 72 |
| Programmēšana II | 36 |
| **Kopā** | **148** |

Automātiski pārbaudāmie satura signāli:

| Signāls | Atradumi |
|---|---:|
| `Sasniedzamie rezultāti` | 159 |
| Teorijas virsrakstu signāli | 427 |
| Precīzs `70 min` marķieris | 112/148 nodarbībās |
| `darba sadalījums` marķieris | 101 atradums |
| Precīzs `Priekšzināšanu` marķieris | 10/148 nodarbībās |

Secinājums: satura struktūra kopumā ir plaša un lietojama, bet vecais audits apgalvoja pilnīgu `70 min` un `Priekšzināšanu robeža` konsekvenci. Pašreizējā repo stāvoklī šie marķieri nav vienādi nosaukti visās nodarbībās.

Svarīgākais satura uzlabojums: ja šie kritēriji joprojām ir standarts, katrai nodarbībai vajag vienotu sadaļu nosaukumu, piemēram:

- `70 min darba sadalījums`;
- `Priekšzināšanu robeža`;
- `1. uzdevums`, `2. uzdevums`, `3. uzdevums`;
- `Papildus uzdevums`.

## 8. Uzturēšana un automatizācija

Pašlaik repo nav atrasts:

- `package.json`;
- testu vai lint skripti;
- GitHub Actions / CI konfigurācija;
- automātisks sitemap/canonical ģenerators.

Tas nav bloķējoši statiskai vietnei, bet tas nozīmē, ka liela daļa kvalitātes tagad balstās manuālās pārbaudēs. Tā kā repo satur 176 publicētas lapas un 231 redirect noteikumu, ieteicams pievienot vismaz vienkāršu statisko pārbaudes skriptu.

Minimālais automatizācijas komplekts:

1. pārbaudīt, ka katrai publicētai HTML lapai ir tieši viens canonical un og:url;
2. pārbaudīt, ka canonical sakrīt ar extensionless ceļu;
3. pārbaudīt, ka sitemap satur visas publicētās lapas un nesatur `sagataves/`;
4. pārbaudīt, ka iekšējie `<a href>` mērķi eksistē;
5. pārbaudīt, ka `_redirects` nav dublētu avotu;
6. pārbaudīt, ka nav vecā `eduardsbaumanis.github.io/ebskola` domēna.

## 9. Prioritātes

### P0 — jāizdara nākamais

1. Sakārtot neeksistējošu URL apstrādi, lai tie neatgriež `200 OK`.
   - Piemērs, kas pašlaik ir risks: `https://ebskola.lv/this-definitely-does-not-exist`.
   - Mērķis: `404` vai pārdomāta `301` pāradresācija, nevis sākumlapa ar `200`.

### P1 — ieteicams drīz

1. Standartizēt `70 min darba sadalījums` un `Priekšzināšanu robeža` sadaļas visās 148 nodarbībās.
2. Sakārtot `sagataves/` HTML higiēnu: `lang`, `viewport`, iespējams arī `noindex`.
3. Salabot vienīgo `target="_blank"` bez `rel="noopener noreferrer"`.
4. Pievienot statisku auditēšanas skriptu, lai šo failu var pārģenerēt vai vismaz pārbaudīt automātiski.

### P2 — vēlāk

1. Ģenerēt `sitemap.xml` un `_redirects` no failu koka, lai tie neatšķiras no reālās struktūras.
2. Turpināt vienādot vecāko Programmēšana I tēmu uzdevumu nosaukumus un 70 min ritmu.
3. Pārskatīt `SR-MAPPING.md`, lai tas pilnībā atbilst pašreizējām nodarbībām.

## 10. Pārbaudes pieraksts

Veiktās pārbaudes:

- `git status --short --branch`;
- HTML failu un mapju skaita pārbaude;
- `sitemap.xml` XML parse un `<loc>` analīze;
- `robots.txt` sitemap rindas pārbaude;
- canonical un `og:url` pārbaude visām 176 publicētajām lapām;
- JSON-LD parse pārbaude visām 176 publicētajām lapām;
- iekšējo `<a href>` mērķu pārbaude;
- `.html` metadatu un iekšējo saišu meklēšana;
- vecā GitHub Pages domēna meklēšana;
- `_redirects` sintakses un dublēto avotu pārbaude;
- attēlu `alt` pārbaude;
- `git diff --check`;
- dzīvie `curl -I -L` testi pret `https://ebskola.lv`.

Šī audita galvenais secinājums: **repo iekšējā SEO struktūra ir sakārtota; nākamais lielais solis ir pareiza 404/unknown URL apstrāde Cloudflare pusē un satura marķieru konsekvence visās nodarbībās.**
