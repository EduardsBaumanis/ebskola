# prog2_2 izvērtējums un darba secība

Sākotnējie uzdevumi trenēja atsevišķas prasmes, bet bez skolotāja papildu koda un skaidrojumiem negarantēja funkcionālu platformas spēli. Pārstrādātā tēma veido vienu projektu sešās nodarbībās; katrā saglabāti trīs pamatuzdevumi, izvēles paplašinājums, pārbaudes un iesniegšanas kritēriji. Saglabāts esošais 80 minūšu nodarbības plānojums.

## Uzsvars uz darbu Godot logā

Stundu valoda un virsraksti vienkāršoti. Norādījumi vispirms nosauc Scene panelī atlasāmo objektu, tad Inspector lauku vai pogu un sagaidāmo rezultātu. Godot angļu nosaukumi saglabāti, lai skolēns tos varētu atrast savā ekrānā. 2.1 stundā ir paneļu atgādne, bet tēmas pārskatā — biežāko klikšķu tabula.

- 2.1 skolēns maina Speed un Physics Ticks per Second, aplūko Output un pieraksta novērojumus; četru aprēķinu vietā pietiek ar īsu kustības salīdzinājumu.
- 2.2 skolēns pievieno taustiņus Input Map, maina Speed un salīdzina kustību pa diagonāli. Kvadrātsaknes aprēķins nav iesniegšanas prasība.
- 2.3 saglabāti if, switch un foreach piemēri ar Output pārbaudēm. Python pārrakstīšana un apzināta break izņemšana vairs nav pamatuzdevumi.
- 2.4 Layer un Mask skaidro ar Inspector numurētajiem kvadrātiņiem; faila bitu masku vērtības skolēnam nav jāiegaumē.
- 2.5 lēcienu salīdzina, mainot Jump Velocity Inspector panelī. Lēciena augstuma formulas vietā pārbauda, vai platformas un atslēgu var sasniegt.
- 2.6 tekstu ievietošana un izskata maiņa aprakstīta ar konkrētiem laukiem. Papildu uzdevums ir Label teksta krāsa un izmērs.

Pilnie C# piemēri, spēles faili un ZIP nav mainīti. Vērtē skolēna veikto izmaiņu rezultātu un īsu skaidrojumu; jaunās iesniegšanas prasības skati katras stundas sadaļā “Ko sagatavo”.

## Konstatētie šķēršļi un ieviestās izmaiņas

| Sākotnējā problēma | Ieviestais risinājums |
|---|---|
| Node2D/Mover un CharacterBody2D/Player mainījās bez skaidras pārejas; trūka redzamā objekta un scēnu iestatījumu. | MovementLab ir atsevišķs eksperiments. No 2.2 lieto vienu Player.tscn un Player.cs; norādītas formas, izmēri, pozīcijas, mapes un F5 galvenā scēna. |
| Delta tika skaidrots kā obligāts jebkurai kustībai, monitora Hz sajaukts ar fizikas biežumu. | Nošķirta Position pārbīde, Velocity un gravitācija; eksperiments maina Physics Ticks per Second un beigās atjauno 60 Hz. |
| C# switch kļūdaini aprakstīja automātisku pāreju uz nākamo netukšo case. | Pilnajā kodā katrs case beidzas ar break; skolēns pārbauda katra priekšmeta rezultātu Output panelī. |
| Atsevišķie Player piemēri pārrakstīja kustību vai priekšmetu loģiku. | Pilni savstarpēji saderīgi faili katram būtiskajam posmam; skaidri norādīts, kad aizstāt metodi un kad papildināt klasi. |
| Monētas pazušana nebija sasaistīta ar punktiem; atsauces uz ScoreUp, grupām vai Game nebija izveidotas. | Pickup pārbauda Player tipu un tieši izsauc publisku OnPickup. Vienreizējas savākšanas aizsardzība; punkti un atslēga saglabājas Player instancē. |
| Area2D Mask nebija saskaņota ar Player Layer. | Vienota Inspector kvadrātiņu tabula grīdai, spēlētājam un priekšmetiem; skolēns ieslēdz un izslēdz Mask un pārbauda rezultātu. |
| Lēciena norādījumos atšķīrās mainīgie, trūka eksperimentu atcelšanas, papildu dubultlēciens nebija korekti definēts. | Vienots Velocity, Gravity, JumpVelocity; pārbaudāms pamatlēciens. Mainīgs augstums un coyote time ir izvēles uzlabojums, pēc lēciena patērējot toleranci. |
| 6. stundā prasīti gan 3 līmeņi, gan tikai 1; vienlaikus jauns ienaidnieks, HP, taimeris un līmeņu pārvaldnieks. | Pamatprasība visur ir viens pabeigts līmenis. Sarežģītākas sistēmas ir izvēles paplašinājumi. |
| Nebija pilna uzvaras, zaudējuma un restartēšanas ceļa; piemērs uzvarot aizvēra spēli. | Level.cs ar redzamu uzvaru/zaudējumu, atslēgas pārbaudi, bīstamu zonu, kritiena pārbaudi un pilnu scēnas atjaunošanu ar R. |
| Dekoratīvs PhysicsCheckpoint kods un attēli solīja vēl neieviestas funkcijas. | Tie aizstāti ar īstiem projekta mezgliem, savienotu kodu un konkrētiem pārbaudes rezultātiem. |
| Maz vietas skolēna individuālai iecerei. | 6. stundā atsevišķs dizaina un stāsta uzdevums, apkopojums un iesniegšanas kritēriji; sākuma un beigu teksti maināmi Inspector. |

## Sasniedzamais minimums

Viens no sākuma līdz finišam izspēlējams līmenis, trīs platformas, pieci punktu priekšmeti un atslēga, vadības norādes, HUD, bīstamā zona, uzvara, zaudējums un pilns restartējums. Punktus vākt ir izvēles izaicinājums; uzvarai vajadzīga atslēga. Pēc spēles iznākuma varonis nekustas un priekšmetus nesavāc.

Skolēns izvēlas nosaukumu, varoni, pasauli un stāsta mērķi; maina vismaz trīs vizuālus elementus un vismaz vienu platformas/priekšmeta novietojumu, pārbaudot maršrutu. Māksliniecisko sarežģītību neaizstāj ar prasību izmantot konkrētu attēlu komplektu. Pietiek ar paša izvēlētām, skaidri salasāmām figūrām un pamatotu dizainu.

## Atbalsts un vērtēšana

- `kods/2_1`, `kods/2_2`, `kods/2_3`: pilni attiecīgās stundas C# faili salīdzināšanai. To saites un saturs ir stundu lapās.
- `platformer/`: pilns gala piemērs; `platformer.zip`: tā pati versija bez būvēšanas kešatmiņas. Piemērs ir kļūdu meklēšanas atbalsts; skolēnam joprojām jāveic savas izmaiņas un jāizskaidro kods.
- Pēc 2.4 jāstrādā savākšanai; pēc 2.5 jābūt sasniedzamai atslēgai. Ja šīs pārbaudes neizdodas, vispirms novērš kļūdu un atliek izvēles uzlabojumus.
- 6. stundā funkcionālo rezultātu pārbauda pēc tabulas, radošo ieguldījumu — pēc spēlē redzamām izvēlēm un to pamatojuma. Skolēns pieraksta klasesbiedra atsauksmi un veikto labojumu.
- Pieejama mācību secība un izpildāms piemērs mazina tehniskos šķēršļus; faktiskais darba temps un nepieciešamais individuālais atbalsts jāpārbauda klasē.

## Tehniskā pārbaude

Pārbaudīts ar Godot .NET 4.7.2 un .NET SDK 8.0.425: kompilācija bez kļūdām un brīdinājumiem, visas 53 spēles pārbaudes izpildītas. Automātiskā pārbaude kompilē 2.1–2.3 pilnos failus un gala projektu atsevišķās pagaidu mapēs. Godot vidē tā pārbauda īstu kustību un platformu maršrutu ar ievades darbībām, Area2D savākšanu, finišu ar/bez atslēgas, abus zaudējuma veidus, HUD un R spēles laikā un pēc iznākuma.

Visām septiņām HTML lapām pārbaudītas vietējās saites un enkuri, stundu struktūra, JSON-LD, pilno koda bloku atbilstība lejupielādēm un ZIP atbilstība avota failiem. Pārlūkā pārbaudīts 1366 px un 390 px platums, arī atvērti koda bloki: nav lapas horizontālas pārplūdes vai JavaScript kļūdu.

No repozitorija saknes:

```bash
python3 programmesana2/prog2_2/parbaudes/check.py --godot /cels/uz/Godot.NET --dotnet /cels/uz/dotnet
```

Testa izsaukumā norāda savas sistēmas izpildfailu ceļus. Pārbaude neveic izmaiņas skolēna piemērā. Lapu norādījumu izpilde ar skolēnu klases apstākļos paliek atsevišķa pedagoģiskā pārbaude.

ZIP atjaunošana pēc piemēra izmaiņām (no šīs tēmas mapes):

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

- [Godot: CharacterBody2D un MoveAndSlide](https://docs.godotengine.org/en/stable/tutorials/physics/using_character_body_2d.html).
- [Godot: Area2D noteikšana un maskas](https://docs.godotengine.org/en/stable/classes/class_area2d.html).
- [Godot: C# darba vides priekšnosacījumi](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/c_sharp_basics.html).
- [Microsoft: C# if un switch](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/selection-statements).
