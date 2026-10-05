# Zvaigžņu duelis — Pong piemērs

`prog2_1` sešu stundu rezultāta piemērs salīdzināšanai un kļūdu meklēšanai. Divi spēlētāji vada raketes, bumba atlec no raketēm un sienām, punkti tiek piešķirti par iziešanu aiz pretējās malas. Pirmais līdz 5 punktiem uzvar.

## Palaišana

1. Izpako ZIP (saspiests arhīvs) atsevišķā folder (mapē).
2. Godot **4.7.2 .NET** Project Manager (projektu pārvaldnieks) izvēlies **Import (importēt)** un norādi `project.godot`. Nepieciešams **.NET 8 SDK (programmatūras izstrādes komplekts)**, ne tikai Runtime (izpildlaiks).
3. Nospied **Build (būvēt projektu)** un **F5**. Main scene (galvenā scēna) ir `res://Scenes/Main.tscn`.
4. Pirmajai compilation (kompilācijai) var būt vajadzīgs internet (internets) NuGet (NET pakotņu pārvaldnieks) package (pakotnēm).

Ja lieto citu Godot 4 .NET version (versiju), izveido tajā tukšu C# project (projektu), pārnes `Scenes`, `Scripts` un Input Map (ievades darbību karte) settings (iestatījumus), saglabā savas version (versijas) ģenerētos C# project (projekta) file (failus). Iestati 1280 × 720, Stretch Mode (izstiepšanas režīms) `canvas_items`, Stretch Aspect (izstiepšanas proporcijas) `keep` un Main.tscn kā main scene (galveno scēnu).

Tas ir darbvirsmas Godot project (projekts). Mācību website (vietnes) HTML (hiperteksta iezīmēšanas valoda) lapā spēle pati nepalaižas.

## Vadība

- W/S: kreisā rakete.
- ↑/↓: labā rakete.
- Space: sākt pirmo vai nākamo izspēli.
- R: sākt jaunu partiju ar 0 : 0 jebkurā brīdī, arī pēc uzvaras.

Bumba aiz labās malas dod punktu kreisajam; aiz kreisās — labajam. Pēc punkta raketes un bumba atgriežas sākuma pozīcijās; nākamā izspēle gaida Space. Serves virziens mainās pēc katra punkta. Pie 5 punktiem kustība apstājas un redzams uzvarētājs.

## Uzbūve

- `Scenes/Paddle.tscn`, `Scripts/Paddle.cs`: atkārtoti lietojama rakete ar saviem input (ievades) nosaukumiem.
- `Scenes/Ball.tscn`, `Scripts/Ball.cs`: lidojums, atlēkšana, serve, iziešanas puse.
- `Scenes/Main.tscn`, `Scripts/Game.cs`: punkti, spēles sākums/beigas, HUD (spēles informācijas panelis) un R.
- `Pong.csproj`, `Pong.sln`: compilation (kompilācijai) un redaktoram vajadzīgie project (projekta) file (faili).

Main bērni ir PaddleLeft, PaddleRight, Ball, WallTop, WallBottom, CenterLine un HUD (spēles informācijas panelis). HUD (spēles informācijas panelis) bērni ir Score, Message un Instructions. Code (kods) izmanto tieši šos nosaukumus.

Inspector (īpašību panelis) Collision (sadursme) checkbox (ķeksīši): sienas — Layer (slānis) 1, Mask (maska) nav; raketes — Layer (slānis) 2, Mask (maska) 1; bumba — Layer (slānis) 3, Mask (maska) 1 un 2. Fizikas sakņu Scale (mērogs) ir (1,1). Rakete ir 24 × 120, bumba 20 × 20, sienas 1280 × 20. Lai noteiktu sānu iziešanu, laukuma pamata izmērs ir 1280 × 720.

## Individualizēšana

Pēc Build (būvēt projektu) atlasi Main root (sakni) un maini Game Title (spēles nosaukums), Left Name (nosaukums), Right Name (nosaukums), Mission (mērķis) un Victory Text (teksts). Izvēlies savu pasauli un to, ko nozīmē raketes, bumba un sacensības iznākums.

Maini vismaz trīs vizuālus element (elementus). Polygon2D (2D daudzstūris) figūras vari aizvietot ar saviem attēliem, saglabājot sākotnējos fiziskos izmērus. Pielāgo font (fontus) un krāsas tā, lai abi spēlētāji redz bumbu un rezultātu. README papildini ar stāstu, trīs dizaina izvēļu pamatojumu, resource (resursu) avotiem un pārbaudes rezultātiem.

## Manuālās pārbaudes

1. Sākumā ir 0 : 0, bumba centrā un gaida Space; vadība un mērķis redzami.
2. Katras raketes key (taustiņi) darbojas atsevišķi un vienlaikus; sienas aptur abas raketes.
3. Bumba atlec no abām sienām un abām raketēm.
4. Katras malas šķērsošana dod tikai vienu punktu pareizajam spēlētājam.
5. Pēc punkta saglabājas rezultāts, bumba gaida Space un virziens mainās.
6. Gan kreisais, gan labais var uzvarēt pie 5; pēc uzvaras spēle nekustas un Space to neatsāk.
7. R partijas vidū un pēc uzvaras atjauno visus sākuma apstākļus. Atkārto vismaz divreiz.
8. Project (projektu) iespējams atvērt un kompilēt no kopijas bez `.godot` cache (kešatmiņas).

Visi piemēra vizuālie element (elementi) ir project (projektā) definētas figūras. Ārēji attēli nav nepieciešami. Code (kods) un figūras pieejami ar pievienoto MIT licenci.
