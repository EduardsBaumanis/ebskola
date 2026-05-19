# ebSkola

Bezmaksas atvērtā koda mācību materiāli datorikai, programmēšanai un robotikai latviešu valodā. Projekts ir veidots kā statiska tīmekļvietne skolēniem un pedagogiem, ar uzsvaru uz praktisku darbu, atvērtā pirmkoda rīkiem un sasniedzamo rezultātu sasaisti ar Latvijas izglītības standartiem.

Publiskā vietne: <https://ebskola.lv/>

## Kas atrodas šajā repo

Šis repo ir GitHub Pages draudzīga statiska HTML/CSS vietne. Tajā nav build soļa, pakotņu pārvaldnieka vai servera puses koda - lapas var atvērt tieši pārlūkā vai palaist ar vienkāršu lokālo HTTP serveri.

Galvenās satura daļas:

| Sadaļa | Mape | Saturs |
|---|---|---|
| Datorika 9. klasei | `datorika9/` | Tīmekļa tehnoloģijas, HTML/CSS, JavaScript pamati un spēles projekta izstrāde. |
| Robotika | `robotika/` | LEGO SPIKE, Arduino, sensori, mikrokontrolieri un praktiski robotikas uzdevumi. |
| Programmēšana I | `programmesana1/` | Python pamati, algoritmi, datu struktūras, tīmekļa integrācija, datubāzes un izvietošana. |
| Programmēšana II | `programmesana2/` | Godot 4 un C++/GDExtension spēļu izstrādei. |
| Sagataves | `sagataves/` | HTML sagataves jaunu stundu un noslēguma darbu veidošanai. |

## Lokāla palaišana

Ātrākais variants ir atvērt `index.html` pārlūkā.

Ja gribi pārbaudīt saites un resursus tā, kā tie strādā tīmekļa serverī:

```bash
python3 -m http.server 8000
```

Pēc tam atver:

```text
http://localhost:8000
```

## Repo struktūra

```text
.
|-- index.html          # Galvenā kursu izvēlne
|-- style.css           # Kopīgais vizuālais stils un komponentes
|-- sasnRez.html        # Sasniedzamo rezultātu saraksts
|-- paligm.html         # Palīgmateriāli
|-- manifest.json       # PWA/metadatu manifests
|-- sitemap.xml         # Vietnes karte meklētājiem
|-- AUDIT.md            # Stundu kvalitātes audits un satura standarti
|-- SR-MAPPING.md       # Sasniedzamo rezultātu sasaistes pārskats
|-- datorika9/          # Datorika 9. klasei
|-- robotika/           # Robotikas kurss
|-- programmesana1/     # Programmēšana I
|-- programmesana2/     # Programmēšana II
`-- sagataves/          # Jaunu lapu sagataves
```

## Satura konvencijas

Satura uzturēšanai galvenais avots ir `AUDIT.md`. Īsā versija:

- Stundas faila nosaukums seko kursa/tēmas numerācijai, piemēram, `prog1_4/prog1_45.html`.
- Tēmas galvenā lapa beidzas ar `main.html`, piemēram, `prog1_4main.html`.
- Stundas virsraksts parasti ir formātā `{Tēmas_nr}.{Stundas_nr} {Nosaukums}`.
- Stundā jābūt skaidram izaicinājumam, kompaktai teorijai, 3 galvenajiem uzdevumiem, papildu uzdevumam, biežākajām kļūdām un navigācijai uz iepriekšējo/nākamo lapu.
- Sasniedzamie rezultāti tiek norādīti ar `.lesson-meta` blokiem un saitēm uz `sasnRez.html`.
- Kopīgo vizuālo stilu uztur `style.css`; atsevišķu lapu inline stili jālieto piesardzīgi.

## Jaunas stundas pievienošana

1. Izvēlies atbilstošo kursa un tēmas mapi.
2. Sāc no `sagataves/stundas_sagatave.html` vai līdzīgas esošas stundas tajā pašā kursā.
3. Atjauno `<title>`, `<h1>`, stundas izaicinājumu, SR saites, teoriju, uzdevumus un navigāciju.
4. Pievieno saiti tēmas `*main.html` lapā.
5. Ja stunda maina SR pārklājumu, atjauno `SR-MAPPING.md`.
6. Pārbaudi vietni lokāli ar `python3 -m http.server 8000`.

## Noderīgi uzturēšanas faili

- `AUDIT.md` - stundu standarti, kvalitātes vērtējumi un revīzijas piezīmes.
- `SR-MAPPING.md` - sasniedzamo rezultātu un stundu sasaistes pārskats.
- `sitemap.xml` - publicētās vietnes indeksējamās lapas.
- `robots.txt` - meklētāju indeksēšanas norādes.
- `manifest.json` - vietnes nosaukums, krāsas un ikona.

## Licence

Materiāli un kods publicēti ar MIT licenci. Skati `LICENSE`.
