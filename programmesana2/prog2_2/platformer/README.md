# Bākas gaisma — platformer (platformas spēles) piemērs

Šis ir `prog2_2` tēmas pamatspēles piemērs salīdzināšanai un kļūdu meklēšanai. Savu project (projektu) veido, secīgi izpildot 2.1–2.6 stundas. Piemērs ietver vienu līmeni, trīs platformas, piecus punktu priekšmetus, atslēgu, bīstamu zonu, finišu, HUD (spēles informācijas panelis) un atkārtotu spēli.

## Palaišana

1. Izpako ZIP (saspiests arhīvs) atsevišķā folder (mapē).
2. Atver **Godot 4.7.2 .NET**, Project Manager (projektu pārvaldnieks) izvēlies **Import (importēt)** un norādi `project.godot`. Vajadzīgs **.NET 8 SDK (programmatūras izstrādes komplekts)** (ne tikai Runtime (izpildlaiks)).
3. Nospied **Build (būvēt projektu)**, pēc tam **F5**. Main scene (galvenā scēna) jau ir `res://Scenes/Level1.tscn`.
4. Ja lieto citu Godot 4 .NET version (versiju), izveido tajā tukšu C# project (projektu) un pārnes `Scenes`, `Scripts` un Input Map (ievades darbību karte) settings (iestatījumus). Saglabā savas Godot version (versijas) ģenerēto `.csproj`; iestati 1280 × 720 un Level1 kā main scene (galveno scēnu).

Pirmajai compilation (kompilācijai) var būt nepieciešams internet (internets) NuGet (NET pakotņu pārvaldnieks) package (pakotņu) atjaunošanai. Šis ir Godot darbvirsmas project (projekts); mācību website (vietnes) HTML (hiperteksta iezīmēšanas valoda) lapas pašas spēli nepalaiž.

## Vadība un mērķis

- A/D vai ←/→: pārvietoties.
- Space: lēkt no zemes.
- R: sākt visu līmeni no jauna arī pēc uzvaras vai zaudējuma.

Atrodi atslēgu augšējā platformā un sasniedz zaļo bāku. Coin dod 1 punktu, Gem — 5; visi pieci punktu priekšmeti kopā dod 9. Atslēga punktus nedod, bet atver finišu. Saskare ar sarkano zonu vai izkrišana aiz grīdas malas izraisa zaudējumu. Punkti uzvarai nav obligāti.

Pirmajai platformai lec pretī no attāluma, piemēram, no sākuma position (pozīcijas), vienlaikus turot D un nospiežot Space. No nākamajām platformām lec uz labo pusi. Sākot lēcienu tieši zem platformas, var atsisties pret tās apakšu.

## Project (projekta) uzbūve

- `Scripts/Player.cs`: horizontālā kustība, gravitācija, lēciens un priekšmetu state (stāvoklis).
- `Scripts/Pickup.cs`: Area2D (2D saskares zona) signal (signāls), Player type (tipa) pārbaude, vienreizēja savākšana.
- `Scripts/Level.cs`: HUD (spēles informācijas panelis), stāsta teksti, uzvara, zaudējums un R.
- `Scenes/Player.tscn`, `Scenes/Pickup.tscn`: atkārtoti izmantojamas scene (scēnas).
- `Scenes/Level1.tscn`: izspēlējams piemēra līmenis.

Collision (sadursme) Inspector (īpašību panelis) checkbox (ķeksīši): platformas/grīda — Layer (slānis) 1, Mask (maska) nav; Player — Layer (slānis) 2, Mask (maska) 1; Area2D (2D saskares zona) zonas — Layer (slānis) 3, Mask (maska) 2. `.tscn` file (failos) 3. slānim atbilst bitmask (bitu maskas) value (vērtība) 4.

## Individualizēšana

Pēc Build (būvēt projektu) atlasi Level1 root (sakni) un nomaini `Game Title`, `Mission`, `Win Text`, `Lose Text`, `Locked Text`. Izvēlies savu varoni, pasauli un mērķi. Maini Polygon2D (2D daudzstūris) figūras vai aizstāj tās ar saviem Sprite2D (2D attēla mezgls) attēliem. Pielāgo collision shape (sadursmes formas), saglabājot fizikas sakņu Scale (mērogs) (1,1). Izmaini maršrutu un izspēlē to pēc katras izmaiņas.

Ja atslēgu attēlo kā citu priekšmetu, pielāgo arī HUD (spēles informācijas panelis) vārdu `Atslēga` method (metodē) `UpdateHud`. Iesniegšanai README papildini ar savu stāstu, trīs dizaina izvēļu pamatojumu, resource (resursu) avotiem un testing (testēšanas) rezultātiem.

## Pārbaudes pirms iesniegšanas

1. Sākumā ir 0 punktu, nav atslēgas, redzama vadība un mērķis.
2. Varonis apstājas pie šķēršļiem, lec no zemes, gaisā nevar lēkt atkārtoti.
3. Katrs priekšmets dod atlīdzību tikai vienreiz, HUD (spēles informācijas panelis) mainās.
4. Finišs bez atslēgas dod norādi, ar atslēgu — uzvaras tekstu.
5. Bīstamā zona un kritiens ārpus laukuma atsevišķi izraisa zaudējumu.
6. Pēc iznākuma kustība un savākšana apstājas; R atjauno visu game state (spēles stāvokli). Atkārto divreiz.
7. Pārbaudi no jaunas project (projekta) kopijas bez `.godot` folder (mapes).

Visi vizuālie element (elementi) ir vienkāršas project (projektā) definētas figūras, ārēji attēli nav nepieciešami. Code (kods) un figūras pieejami ar pievienoto MIT licenci.
