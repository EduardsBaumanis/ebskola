# Zvaigžņu duelis — Pong piemērs

`prog2_1` sešu stundu rezultāta piemērs salīdzināšanai un kļūdu meklēšanai. Divi spēlētāji vada raketes, bumba atlec no raketēm un sienām, punkti tiek piešķirti par iziešanu aiz pretējās malas. Pirmais līdz 5 punktiem uzvar.

## Palaišana

1. Izpako ZIP atsevišķā mapē.
2. Godot **4.7.2 .NET** Project Manager izvēlies **Import** un norādi `project.godot`. Nepieciešams **.NET 8 SDK**, ne tikai Runtime.
3. Nospied **Build** un **F5**. Galvenā scēna ir `res://Scenes/Main.tscn`.
4. Pirmajai kompilācijai var būt vajadzīgs internets NuGet pakotnēm.

Ja lieto citu Godot 4 .NET versiju, izveido tajā tukšu C# projektu, pārnes `Scenes`, `Scripts` un Input Map iestatījumus, saglabā savas versijas ģenerētos C# projekta failus. Iestati 1280 × 720, Stretch Mode `canvas_items`, Stretch Aspect `keep` un Main.tscn kā galveno scēnu.

Tas ir darbvirsmas Godot projekts. Mācību vietnes HTML lapā spēle pati nepalaižas.

## Vadība

- W/S: kreisā rakete.
- ↑/↓: labā rakete.
- Space: sākt pirmo vai nākamo izspēli.
- R: sākt jaunu partiju ar 0 : 0 jebkurā brīdī, arī pēc uzvaras.

Bumba aiz labās malas dod punktu kreisajam; aiz kreisās — labajam. Pēc punkta raketes un bumba atgriežas sākuma pozīcijās; nākamā izspēle gaida Space. Serves virziens mainās pēc katra punkta. Pie 5 punktiem kustība apstājas un redzams uzvarētājs.

## Uzbūve

- `Scenes/Paddle.tscn`, `Scripts/Paddle.cs`: atkārtoti lietojama rakete ar saviem ievades nosaukumiem.
- `Scenes/Ball.tscn`, `Scripts/Ball.cs`: lidojums, atlēkšana, serve, iziešanas puse.
- `Scenes/Main.tscn`, `Scripts/Game.cs`: punkti, spēles sākums/beigas, HUD un R.
- `Pong.csproj`, `Pong.sln`: kompilācijai un redaktoram vajadzīgie projekta faili.

Main bērni ir PaddleLeft, PaddleRight, Ball, WallTop, WallBottom, CenterLine un HUD. HUD bērni ir Score, Message un Instructions. Kods izmanto tieši šos nosaukumus.

Inspector Collision ķeksīši: sienas — Layer 1, Mask nav; raketes — Layer 2, Mask 1; bumba — Layer 3, Mask 1 un 2. Fizikas sakņu Scale ir (1,1). Rakete ir 24 × 120, bumba 20 × 20, sienas 1280 × 20. Lai noteiktu sānu iziešanu, laukuma pamata izmērs ir 1280 × 720.

## Individualizēšana

Pēc Build atlasi Main sakni un maini Game Title, Left Name, Right Name, Mission un Victory Text. Izvēlies savu pasauli un to, ko nozīmē raketes, bumba un sacensības iznākums.

Maini vismaz trīs vizuālus elementus. Polygon2D figūras vari aizvietot ar saviem attēliem, saglabājot sākotnējos fiziskos izmērus. Pielāgo fontus un krāsas tā, lai abi spēlētāji redz bumbu un rezultātu. README papildini ar stāstu, trīs dizaina izvēļu pamatojumu, resursu avotiem un pārbaudes rezultātiem.

## Manuālās pārbaudes

1. Sākumā ir 0 : 0, bumba centrā un gaida Space; vadība un mērķis redzami.
2. Katras raketes taustiņi darbojas atsevišķi un vienlaikus; sienas aptur abas raketes.
3. Bumba atlec no abām sienām un abām raketēm.
4. Katras malas šķērsošana dod tikai vienu punktu pareizajam spēlētājam.
5. Pēc punkta saglabājas rezultāts, bumba gaida Space un virziens mainās.
6. Gan kreisais, gan labais var uzvarēt pie 5; pēc uzvaras spēle nekustas un Space to neatsāk.
7. R partijas vidū un pēc uzvaras atjauno visus sākuma apstākļus. Atkārto vismaz divreiz.
8. Projektu iespējams atvērt un kompilēt no kopijas bez `.godot` kešatmiņas.

Visi piemēra vizuālie elementi ir projektā definētas figūras. Ārēji attēli nav nepieciešami. Kods un figūras pieejami ar pievienoto MIT licenci.
