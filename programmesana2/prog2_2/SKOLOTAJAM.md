# prog2_2 izvērtējums un darba secība

Sākotnējie uzdevumi trenēja atsevišķas prasmes, bet bez skolotāja papildu code (koda) un skaidrojumiem negarantēja funkcionālu platformer (platformas spēli). Pārstrādātā tēma veido vienu project (projektu) sešās nodarbībās; katrā saglabāti trīs pamatuzdevumi, izvēles extension (paplašinājums), pārbaudes un iesniegšanas kritēriji. Saglabāts esošais 80 minūšu nodarbības plānojums.

## Uzsvars uz darbu Godot window (logā)

Stundu valoda un virsraksti vienkāršoti. Norādījumi vispirms nosauc Scene (scēna) panel (panelī) atlasāmo object (objektu), tad Inspector (īpašību panelis) field (lauku) vai button (pogu) un sagaidāmo rezultātu. Godot angļu nosaukumi saglabāti, lai skolēns tos varētu atrast savā screen (ekrānā). 2.1 stundā ir panel (paneļu) atgādne, bet tēmas pārskatā — biežāko klikšķu tabula.

- 2.1 skolēns maina Speed (ātrums) un Physics Ticks per Second (fizikas soļi sekundē), aplūko Output (izvade) un pieraksta novērojumus; četru aprēķinu vietā pietiek ar īsu kustības salīdzinājumu.
- 2.2 skolēns pievieno key (taustiņus) Input Map (ievades darbību karte), maina Speed (ātrums) un salīdzina kustību pa diagonāli. Kvadrātsaknes aprēķins nav iesniegšanas prasība.
- 2.3 saglabāti if (nosacījuma pārbaude), switch (izvēle pēc vērtības) un foreach (katra elementa cikls) piemēri ar Output (izvade) pārbaudēm. Python pārrakstīšana un apzināta break (izpildes pārtraukšana) izņemšana vairs nav pamatuzdevumi.
- 2.4 Layer (slānis) un Mask (maska) skaidro ar Inspector (īpašību panelis) numurētajiem kvadrātiņiem; file (faila) bitmask (bitu masku) value (vērtības) skolēnam nav jāiegaumē.
- 2.5 lēcienu salīdzina, mainot Jump Velocity (lēciena ātrums) Inspector (īpašību panelis) panel (panelī). Lēciena augstuma formulas vietā pārbauda, vai platformas un atslēgu var sasniegt.
- 2.6 tekstu ievietošana un izskata maiņa aprakstīta ar konkrētiem field (laukiem). Papildu uzdevums ir Label (teksta etiķete) teksta krāsa un izmērs.

Pilnie C# piemēri, spēles file (faili) un ZIP (saspiests arhīvs) nav mainīti. Vērtē skolēna veikto izmaiņu rezultātu un īsu skaidrojumu; jaunās iesniegšanas prasības skati katras stundas sadaļā “Ko sagatavo”.

## Konstatētie šķēršļi un ieviestās izmaiņas

| Sākotnējā problēma | Ieviestais risinājums |
|---|---|
| Node2D (2D mezgls)/Mover un CharacterBody2D (vadāma 2D tēla mezgls)/Player mainījās bez skaidras pārejas; trūka redzamā object (objekta) un scene (scēnu) settings (iestatījumu). | MovementLab ir atsevišķs eksperiments. No 2.2 lieto vienu Player.tscn un Player.cs; norādītas formas, izmēri, position (pozīcijas), folder (mapes) un F5 main scene (galvenā scēna). |
| Delta (soļa ilgums) tika skaidrots kā obligāts jebkurai kustībai, monitor (monitora) Hz sajaukts ar physics tick rate (fizikas biežumu). | Nošķirta Position (pozīcija) pārbīde, Velocity (ātrums) un gravitācija; eksperiments maina Physics Ticks per Second (fizikas soļi sekundē) un beigās atjauno 60 Hz. |
| C# switch (izvēle pēc vērtības) kļūdaini aprakstīja automātisku pāreju uz nākamo netukšo case (izvēles gadījums). | Pilnajā code (kodā) katrs case (izvēles gadījums) beidzas ar break (izpildes pārtraukšana); skolēns pārbauda katra priekšmeta rezultātu Output (izvade) panel (panelī). |
| Atsevišķie Player piemēri pārrakstīja kustību vai priekšmetu logic (loģiku). | Pilni savstarpēji saderīgi file (faili) katram būtiskajam posmam; skaidri norādīts, kad aizstāt method (metodi) un kad papildināt class (klasi). |
| Monētas pazušana nebija sasaistīta ar punktiem; reference (atsauces) uz ScoreUp, grupām vai Game nebija izveidotas. | Pickup pārbauda Player type (tipu) un tieši izsauc publisku OnPickup. Vienreizējas savākšanas aizsardzība; punkti un atslēga saglabājas Player instance (eksemplārā). |
| Area2D (2D saskares zona) Mask (maska) nebija saskaņota ar Player Layer (slānis). | Vienota Inspector (īpašību panelis) kvadrātiņu tabula grīdai, spēlētājam un priekšmetiem; skolēns ieslēdz un izslēdz Mask (maska) un pārbauda rezultātu. |
| Lēciena norādījumos atšķīrās variable (mainīgie), trūka eksperimentu atcelšanas, papildu dubultlēciens nebija korekti definēts. | Vienots Velocity (ātrums), Gravity (gravitācija), JumpVelocity (lēciena ātrums); pārbaudāms pamatlēciens. Mainīgs augstums un coyote time (īss lēciena papildlaiks pēc platformas malas) ir izvēles uzlabojums, pēc lēciena patērējot toleranci. |
| 6. stundā prasīti gan 3 līmeņi, gan tikai 1; vienlaikus jauns ienaidnieks, HP (dzīvības punkti), timer (taimeris) un līmeņu pārvaldnieks. | Pamatprasība visur ir viens pabeigts līmenis. Sarežģītākas system (sistēmas) ir izvēles extension (paplašinājumi). |
| Nebija pilna uzvaras, zaudējuma un restartēšanas path (ceļa); piemērs uzvarot aizvēra spēli. | Level.cs ar redzamu uzvaru/zaudējumu, atslēgas pārbaudi, bīstamu zonu, kritiena pārbaudi un pilnu scene (scēnas) atjaunošanu ar R. |
| Dekoratīvs PhysicsCheckpoint code (kods) un attēli solīja vēl neieviestas function (funkcijas). | Tie aizstāti ar īstiem project (projekta) node (mezgliem), savienotu code (kodu) un konkrētiem pārbaudes rezultātiem. |
| Maz vietas skolēna individuālai iecerei. | 6. stundā atsevišķs dizaina un stāsta uzdevums, apkopojums un iesniegšanas kritēriji; sākuma un beigu teksti maināmi Inspector (īpašību panelis). |

## Sasniedzamais minimums

Viens no sākuma līdz finišam izspēlējams līmenis, trīs platformas, pieci punktu priekšmeti un atslēga, vadības norādes, HUD (spēles informācijas panelis), bīstamā zona, uzvara, zaudējums un pilns restart (restartējums). Punktus vākt ir izvēles izaicinājums; uzvarai vajadzīga atslēga. Pēc spēles iznākuma varonis nekustas un priekšmetus nesavāc.

Skolēns izvēlas nosaukumu, varoni, pasauli un stāsta mērķi; maina vismaz trīs vizuālus element (elementus) un vismaz vienu platformas/priekšmeta novietojumu, pārbaudot maršrutu. Māksliniecisko computational complexity (sarežģītību) neaizstāj ar prasību izmantot konkrētu attēlu komplektu. Pietiek ar paša izvēlētām, skaidri salasāmām figūrām un pamatotu dizainu.

## Atbalsts un vērtēšana

- `kods/2_1`, `kods/2_2`, `kods/2_3`: pilni attiecīgās stundas C# file (faili) salīdzināšanai. To link (saites) un saturs ir stundu lapās.
- `platformer/`: pilns gala piemērs; `platformer.zip`: tā pati version (versija) bez būvēšanas cache (kešatmiņas). Piemērs ir kļūdu meklēšanas atbalsts; skolēnam joprojām jāveic savas izmaiņas un jāizskaidro code (kods).
- Pēc 2.4 jāstrādā savākšanai; pēc 2.5 jābūt sasniedzamai atslēgai. Ja šīs pārbaudes neizdodas, vispirms novērš kļūdu un atliek izvēles uzlabojumus.
- 6. stundā funkcionālo rezultātu pārbauda pēc tabulas, radošo ieguldījumu — pēc spēlē redzamām izvēlēm un to pamatojuma. Skolēns pieraksta klasesbiedra atsauksmi un veikto labojumu.
- Pieejama mācību secība un izpildāms piemērs mazina tehniskos šķēršļus; faktiskais darba temps un nepieciešamais individuālais atbalsts jāpārbauda class (klasē).

## Tehniskā pārbaude

Pārbaudīts ar Godot .NET 4.7.2 un .NET SDK (programmatūras izstrādes komplekts) 8.0.425: compilation (kompilācija) bez kļūdām un brīdinājumiem, visas 53 spēles pārbaudes izpildītas. Automātiskā pārbaude kompilē 2.1–2.3 pilnos file (failus) un gala project (projektu) atsevišķās pagaidu folder (mapēs). Godot vidē tā pārbauda īstu kustību un platformu maršrutu ar input (ievades) darbībām, Area2D (2D saskares zona) savākšanu, finišu ar/bez atslēgas, abus zaudējuma veidus, HUD (spēles informācijas panelis) un R spēles laikā un pēc iznākuma.

Visām septiņām HTML (hiperteksta iezīmēšanas valoda) lapām pārbaudītas vietējās link (saites) un anchor (enkuri), stundu structure (struktūra), JSON-LD, pilno code block (koda bloku) atbilstība lejupielādēm un ZIP (saspiests arhīvs) atbilstība source file (avota failiem). Browser (pārlūkā) pārbaudīts 1366 px un 390 px platums, arī atvērti code block (koda bloki): nav lapas horizontālas pārplūdes vai JavaScript kļūdu.

No repozitorija root (saknes):

```bash
python3 programmesana2/prog2_2/parbaudes/check.py --godot /cels/uz/Godot.NET --dotnet /cels/uz/dotnet
```

Test (testa) izsaukumā norāda savas system (sistēmas) executable (izpildfailu) ceļus. Pārbaude neveic izmaiņas skolēna piemērā. Lapu norādījumu izpilde ar skolēnu klases apstākļos paliek atsevišķa pedagoģiskā pārbaude.

ZIP (saspiests arhīvs) atjaunošana pēc piemēra izmaiņām (no šīs tēmas folder (mapes)):

```bash
python3 - <<'PY'
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
with ZipFile('platformer.zip', 'w', ZIP_DEFLATED) as archive:
    for path in sorted(Path('platformer').rglob('*')):
        if path.is_file() and not {'.godot', 'bin', 'obj'}.intersection(path.parts):
            archive.write(path, path)
PY
```

## Tehnisko precizējumu avoti

- [Godot: CharacterBody2D (vadāma 2D tēla mezgls) un MoveAndSlide](https://docs.godotengine.org/en/stable/tutorials/physics/using_character_body_2d.html).
- [Godot: Area2D (2D saskares zona) noteikšana un maskas](https://docs.godotengine.org/en/stable/classes/class_area2d.html).
- [Godot: C# darba vides priekšnosacījumi](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/c_sharp_basics.html).
- [Microsoft: C# if (nosacījuma pārbaude) un switch (izvēle pēc vērtības)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/selection-statements).
