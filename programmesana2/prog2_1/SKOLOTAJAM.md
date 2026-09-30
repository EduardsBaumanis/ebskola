# prog2_1 izvērtējums un darba secība

Sākotnējā tēma labi sadalīja vides apgūšanu, taču uzdevumi paši par sevi nenodrošināja pilnu Pong spēles ciklu. Trūka savienojoša koda un precīzu scēnu iestatījumu; gandrīz visa kustība, atlēkšana un punktu loģika bija atlikta uz pēdējo nodarbību. Pārstrādātā secība saglabā sešas 80 minūšu nodarbības, trīs pamatuzdevumus katrā, izvēles uzdevumu, pārbaudes un GitHub iesniegšanu.

## Konstatētais un labojumi

| Šķērslis sākotnējā saturā | Ieviestais risinājums |
|---|---|
| Objektiem trūka precīzu izmēru, redzamā elementa novietojuma un galvenās scēnas izvēles. | Skaidri Scenes/Main.tscn, Paddle.tscn, Ball.tscn, pozīcijas, Polygon2D virsotnes, formas un F5. Pirmo scēnu palaida jau 1.1. |
| Git push bija dots bez attālās krātuves un pirmās publicēšanas secības. | VS Code Initialize, Stage, Commit, Publish to GitHub/Push un rezultāta pārbaude pārlūkā. |
| Build poga prasīta pirms pirmā C# skripta izveides. | 1.3 pārbauda SDK, izveido BuildCheck.cs, tad kompilē un palaiž; diagnostika balstās reālā rezultātā. |
| Atkārtoti Hello piemēri maz palīdzēja noslēguma spēlei. | 1.4 veido tieši Paddle klasi, tās tipus, Export laukus un atšķirīgus instanču iestatījumus. |
| Nosaukumi un koka ceļi mainījās: Punkti, UI/Punkti, Main, Game un citi nesaskaņoti varianti. | Viens koks un viena klašu secība; HUD/Score, HUD/Message, HUD/Instructions. Main mezglam piesaista Game.cs. |
| Formas un renderētie objekti atšķīrās; Collision Layers/Masks nebija konkretizētas. | Vienādi fiziskie/vizuālie izmēri un kopīga slāņu tabula; objektu saknes un bērnu koordinātes skaidri nodalītas. |
| Visa spēles kustība palika 1.6, neatstājot laiku patstāvīgai pārbaudei. | 1.5 ir gatavs laukums, divu spēlētāju vadība, bumbas atlēkšana un iziešanas noteikšana. |
| Ball piemērs nesavienoja bumbas iziešanu ar Game punktu uzskaiti, bet apgalvoja pilnu spēli. | Ball.ExitSide nolasa Game. Pēc punkta ResetBall nodzēš marķieri; viens notikums dod vienu punktu. |
| Bumba sāka lidot uzreiz, paātrinājās neierobežoti, uzvara un restartēšana bija nepilnīgas. | Pamatā konstants ātrums, gaidīšana pirms Space serves, virziena maiņa pēc punkta, abu spēlētāju uzvara pie 5 un R visam spēles stāvoklim. |
| Attēli un dekoratīvas klases solīja funkcijas, kas uzdevumos nebija realizētas. | Aizstātas ar pilniem saderīgiem failiem, īstām struktūrām, pārbaudēm un lejupielādējamu projektu. |
| Trūka skaidras vietas skolēna radošajai iecerei. | 1.6 atsevišķs dizaina/stāsta uzdevums, apkopojums un iesniegšanas kritēriji; spēlē redzamie teksti maināmi Inspector. |

## Nodarbību rezultāti

1. Godot .NET projekts atveras, Main scēna palaižas un sākumpunkts publicēts GitHub.
2. Divas raketes un bumba ir redzamas, ar atbilstošām sadursmes formām un kopīgām scēnām.
3. BuildCheck.cs kompilējas un izpildās; skolēns prot nolasīt un novērst vienu kompilācijas kļūdu.
4. Paddle.cs izdrukā instanču datus; skolēns saprot tipus un Inspector pārrakstījumus.
5. Raketes vada ar saviem taustiņiem un aptur pie sienām. Bumba atlec, iziešanas brīdī apstājas. Šis posms vēl neskaita punktus.
6. Game.cs apvieno pilnu partiju, HUD un jaunu spēli. Skolēns veido savu dizainu/stāstu un testē ar citiem spēlētājiem.

## Minimums un radošās izvēles

Pamatdarbs ir divu spēlētāju spēle līdz 5 punktiem ar skaidru sākumu, punktu iegūšanu, uzvaru un atkārtošanu. Mākslīgais intelekts, izvēlnes, skaņas un bumbas paātrināšanās nav obligāti. Fiksētā laukuma izmērs ir 1280 × 720; loga attēlošanas mērogošanai izmantots canvas_items ar keep proporcijām.

Skolēns izvēlas nosaukumu, komandu identitāti, bumbas nozīmi un stāstu; maina vismaz trīs vizuālus elementus un pamato izvēles. Stāstam jābūt redzamam spēles sākumā un uzvaras tekstā. Vienkāršas paša veidotas figūras ir pietiekamas; nav obligāti jāmeklē gatavs attēlu komplekts. Fizikas izmēru saglabāšana ļauj mainīt dizainu, nezaudējot pārbaudītu spēli.

Vērtējot atsevišķi pārbauda funkcionālo ciklu, skolēna koda skaidrojumu, radošās izvēles un testēšanu. Ja 1.5 fizika vēl nedarbojas, vispirms novērš šo kļūdu un atliek izvēles papildinājumus. Klases darba temps un nepieciešamais individuālais atbalsts jāpārbauda mācību darbā; automatizēti testi to neaizstāj.

## Atbalsta faili

- `kods/1_3/BuildCheck.cs`, `kods/1_4/Paddle.cs`: pilni starpposmu faili.
- `pong/Scripts/Paddle.cs`, `Ball.cs`: 1.5 gala faili, kuri nemainīti turpinās 1.6.
- `pong/Scripts/Game.cs`: 1.6 spēles cikls.
- `pong/`: pilns izpildāms piemērs; `pong.zip`: identiska kopija bez būvēšanas kešatmiņas.
- Visu skolēnam vajadzīgo skriptu saturs un lejupielādes saites ir stundu lapās.

## Tehniskās pārbaudes

Godot 4.7.2 .NET, .NET SDK 8.0.425. 1.3, 1.4, 1.5 skripti un gala projekts kompilējas bez kļūdām un brīdinājumiem. Godot izpildīti 100 apgalvojumu testi: 25 — 1.5 posmam bez Game piesaistes, 75 — gatavai spēlei.

Pārbaudīta faktiskā ievade un sadursmes: raketes kustība, taustiņu atlaišana un pretēju virzienu atcelšana, vienlaicīga divu spēlētāju vadība, abu sienu robežas, bumbas atlēkšana no abām sienām/raketēm, sānu iziešana, punktu pareizība un vienreizēja piešķiršana, gaidīšana pirms serves, abu spēlētāju uzvara precīzi pie 5 un R spēles laikā/pēc iznākuma. Punktu pārbaudēs bumba novietota pie konkrētās malas un to šķērso ar fizikas kustību.

No repozitorija saknes:

```bash
python3 programmesana2/prog2_1/parbaudes/check.py --godot /cels/uz/Godot.NET --dotnet /cels/uz/dotnet
```

Norādi savas sistēmas izpildfailus. Testi darbojas pagaidu projekta kopijās un nemaina lejupielādējamo piemēru.

ZIP atjaunošana pēc piemēra izmaiņām (no šīs tēmas mapes):

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

- [Godot C# pamati un SDK](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/c_sharp_basics.html).
- [Godot CharacterBody2D kustība un atlēkšana](https://docs.godotengine.org/en/stable/tutorials/physics/using_character_body_2d.html).
- [Godot C# Export īpašības](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/c_sharp_exports.html).
- [VS Code Git darba secība un publicēšana](https://code.visualstudio.com/docs/sourcecontrol/quickstart).
