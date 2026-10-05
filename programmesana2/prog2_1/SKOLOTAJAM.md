# prog2_1 izvērtējums un darba secība

Sākotnējā tēma labi sadalīja vides apgūšanu, taču uzdevumi paši par sevi nenodrošināja pilnu Pong game loop (spēles ciklu). Trūka savienojoša code (koda) un precīzu scene (scēnu) settings (iestatījumu); gandrīz visa kustība, atlēkšana un punktu logic (loģika) bija atlikta uz pēdējo nodarbību. Pārstrādātā secība saglabā sešas 80 minūšu nodarbības, trīs pamatuzdevumus katrā, izvēles uzdevumu, pārbaudes un GitHub iesniegšanu.

## Konstatētais un labojumi

| Šķērslis sākotnējā saturā | Ieviestais risinājums |
|---|---|
| Object (objektiem) trūka precīzu izmēru, redzamā element (elementa) novietojuma un main scene (galvenās scēnas) izvēles. | Skaidri Scenes/Main.tscn, Paddle.tscn, Ball.tscn, position (pozīcijas), Polygon2D (2D daudzstūris) virsotnes, formas un F5. Pirmo scene (scēnu) palaida jau 1.1. |
| Git push (nosūtīšana uz attālo krātuvi) bija dots bez remote repository (attālās krātuves) un pirmās publishing (publicēšanas) secības. | VS Code Initialize, Stage, Commit (izmaiņu fiksējums), Publish to GitHub (publicēt GitHub)/Push (nosūtīšana uz attālo krātuvi) un rezultāta pārbaude browser (pārlūkā). |
| Build (būvēt projektu) button (poga) prasīta pirms pirmā C# script (skripta) izveides. | 1.3 pārbauda SDK (programmatūras izstrādes komplekts), izveido BuildCheck.cs, tad kompilē un palaiž; diagnostika balstās reālā rezultātā. |
| Atkārtoti Hello piemēri maz palīdzēja noslēguma spēlei. | 1.4 veido tieši Paddle class (klasi), tās type (tipus), Export (eksportēt) field (laukus) un atšķirīgus instance (instanču) settings (iestatījumus). |
| Nosaukumi un koka ceļi mainījās: Punkti, UI (lietotāja saskarne)/Punkti, Main, Game un citi nesaskaņoti varianti. | Viens koks un viena class (klašu) secība; HUD (spēles informācijas panelis)/Score, HUD (spēles informācijas panelis)/Message, HUD (spēles informācijas panelis)/Instructions. Main node (mezglam) piesaista Game.cs. |
| Formas un renderētie object (objekti) atšķīrās; Collision Layers (sadursmju slānis)/Masks nebija konkretizētas. | Vienādi fiziskie/vizuālie izmēri un kopīga slāņu tabula; object (objektu) root (saknes) un child node (bērnu) koordinātes skaidri nodalītas. |
| Visa spēles kustība palika 1.6, neatstājot laiku patstāvīgai pārbaudei. | 1.5 ir gatavs laukums, divu spēlētāju vadība, bumbas atlēkšana un iziešanas noteikšana. |
| Ball piemērs nesavienoja bumbas iziešanu ar Game punktu uzskaiti, bet apgalvoja pilnu spēli. | Ball.ExitSide nolasa Game. Pēc punkta ResetBall nodzēš marķieri; viens event (notikums) dod vienu punktu. |
| Bumba sāka lidot uzreiz, paātrinājās neierobežoti, uzvara un restart (restartēšana) bija nepilnīgas. | Pamatā konstants ātrums, gaidīšana pirms Space serves, virziena maiņa pēc punkta, abu spēlētāju uzvara pie 5 un R visam spēles stāvoklim. |
| Attēli un dekoratīvas class (klases) solīja function (funkcijas), kas uzdevumos nebija realizētas. | Aizstātas ar pilniem saderīgiem file (failiem), īstām structure (struktūrām), pārbaudēm un lejupielādējamu project (projektu). |
| Trūka skaidras vietas skolēna radošajai iecerei. | 1.6 atsevišķs dizaina/stāsta uzdevums, apkopojums un iesniegšanas kritēriji; spēlē redzamie teksti maināmi Inspector (īpašību panelis). |

## Nodarbību rezultāti

1. Godot .NET project (projekts) atveras, Main scene (scēna) palaižas un sākumpunkts publicēts GitHub.
2. Divas raketes un bumba ir redzamas, ar atbilstošām collision (sadursmes) formām un kopīgām scene (scēnām).
3. BuildCheck.cs kompilējas un izpildās; skolēns prot nolasīt un novērst vienu compiler error (kompilācijas kļūdu).
4. Paddle.cs izdrukā instance (instanču) data (datus); skolēns saprot type (tipus) un Inspector (īpašību panelis) pārrakstījumus.
5. Raketes vada ar saviem key (taustiņiem) un aptur pie sienām. Bumba atlec, iziešanas brīdī apstājas. Šis posms vēl neskaita punktus.
6. Game.cs apvieno pilnu partiju, HUD (spēles informācijas panelis) un jaunu spēli. Skolēns veido savu dizainu/stāstu un testē ar citiem spēlētājiem.

## Minimums un radošās izvēles

Pamatdarbs ir divu spēlētāju spēle līdz 5 punktiem ar skaidru sākumu, punktu iegūšanu, uzvaru un atkārtošanu. Artificial intelligence (mākslīgais intelekts), menu (izvēlnes), audio (skaņas) un bumbas paātrināšanās nav obligāti. Fiksētā laukuma izmērs ir 1280 × 720; window (loga) attēlošanas mērogošanai izmantots canvas_items ar keep proporcijām.

Skolēns izvēlas nosaukumu, komandu identitāti, bumbas nozīmi un stāstu; maina vismaz trīs vizuālus element (elementus) un pamato izvēles. Stāstam jābūt redzamam spēles sākumā un uzvaras tekstā. Vienkāršas paša veidotas figūras ir pietiekamas; nav obligāti jāmeklē gatavs attēlu komplekts. Fizikas izmēru save (saglabāšana) ļauj mainīt dizainu, nezaudējot pārbaudītu spēli.

Vērtējot atsevišķi pārbauda funkcionālo loop (ciklu), skolēna code (koda) skaidrojumu, radošās izvēles un testing (testēšanu). Ja 1.5 fizika vēl nedarbojas, vispirms novērš šo kļūdu un atliek izvēles papildinājumus. Class (klases) darba temps un nepieciešamais individuālais atbalsts jāpārbauda mācību darbā; automatizēti test (testi) to neaizstāj.

## Atbalsta file (faili)

- `kods/1_3/BuildCheck.cs`, `kods/1_4/Paddle.cs`: pilni starpposmu file (faili).
- `pong/Scripts/Paddle.cs`, `Ball.cs`: 1.5 gala file (faili), kuri nemainīti turpinās 1.6.
- `pong/Scripts/Game.cs`: 1.6 game loop (spēles cikls).
- `pong/`: pilns izpildāms piemērs; `pong.zip`: identiska kopija bez būvēšanas cache (kešatmiņas).
- Visu skolēnam vajadzīgo script (skriptu) saturs un download (lejupielādes) link (saites) ir stundu lapās.

## Tehniskās pārbaudes

Godot 4.7.2 .NET, .NET SDK (programmatūras izstrādes komplekts) 8.0.425. 1.3, 1.4, 1.5 script (skripti) un gala project (projekts) kompilējas bez kļūdām un brīdinājumiem. Godot izpildīti 100 apgalvojumu test (testi): 25 — 1.5 posmam bez Game piesaistes, 75 — gatavai spēlei.

Pārbaudīta faktiskā input (ievade) un collision (sadursmes): raketes kustība, key (taustiņu) atlaišana un pretēju virzienu atcelšana, vienlaicīga divu spēlētāju vadība, abu sienu robežas, bumbas atlēkšana no abām sienām/raketēm, sānu iziešana, punktu pareizība un vienreizēja piešķiršana, gaidīšana pirms serves, abu spēlētāju uzvara precīzi pie 5 un R spēles laikā/pēc iznākuma. Punktu pārbaudēs bumba novietota pie konkrētās malas un to šķērso ar fizikas kustību.

No repozitorija root (saknes):

```bash
python3 programmesana2/prog2_1/parbaudes/check.py --godot /cels/uz/Godot.NET --dotnet /cels/uz/dotnet
```

Norādi savas system (sistēmas) izpildfailus. Test (testi) darbojas pagaidu project (projekta) kopijās un nemaina lejupielādējamo piemēru.

ZIP (saspiests arhīvs) atjaunošana pēc piemēra izmaiņām (no šīs tēmas folder (mapes)):

```bash
python3 - <<'PY'
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
with ZipFile('pong.zip', 'w', ZIP_DEFLATED) as archive:
    for path in sorted(Path('pong').rglob('*')):
        if path.is_file() and not {'.godot', 'bin', 'obj'}.intersection(path.parts):
            archive.write(path, path)
PY
```

## Avoti precizējumiem

- [Godot C# pamati un SDK (programmatūras izstrādes komplekts)](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/c_sharp_basics.html).
- [Godot CharacterBody2D (vadāma 2D tēla mezgls) kustība un atlēkšana](https://docs.godotengine.org/en/stable/tutorials/physics/using_character_body_2d.html).
- [Godot C# Export (eksportēt) property (īpašības)](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/c_sharp_exports.html).
- [VS Code Git darba secība un publishing (publicēšana)](https://code.visualstudio.com/docs/sourcecontrol/quickstart).
