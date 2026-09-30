# Bākas gaisma — platformas spēles piemērs

Šis ir `prog2_2` tēmas pamatspēles piemērs salīdzināšanai un kļūdu meklēšanai. Savu projektu veido, secīgi izpildot 2.1–2.6 stundas. Piemērs ietver vienu līmeni, trīs platformas, piecus punktu priekšmetus, atslēgu, bīstamu zonu, finišu, HUD un atkārtotu spēli.

## Palaišana

1. Izpako ZIP atsevišķā mapē.
2. Atver **Godot 4.7.2 .NET**, Project Manager izvēlies **Import** un norādi `project.godot`. Vajadzīgs **.NET 8 SDK** (ne tikai Runtime).
3. Nospied **Build**, pēc tam **F5**. Galvenā scēna jau ir `res://Scenes/Level1.tscn`.
4. Ja lieto citu Godot 4 .NET versiju, izveido tajā tukšu C# projektu un pārnes `Scenes`, `Scripts` un Input Map iestatījumus. Saglabā savas Godot versijas ģenerēto `.csproj`; iestati 1280 × 720 un Level1 kā galveno scēnu.

Pirmajai kompilācijai var būt nepieciešams internets NuGet pakotņu atjaunošanai. Šis ir Godot darbvirsmas projekts; mācību vietnes HTML lapas pašas spēli nepalaiž.

## Vadība un mērķis

- A/D vai ←/→: pārvietoties.
- Space: lēkt no zemes.
- R: sākt visu līmeni no jauna arī pēc uzvaras vai zaudējuma.

Atrodi atslēgu augšējā platformā un sasniedz zaļo bāku. Coin dod 1 punktu, Gem — 5; visi pieci punktu priekšmeti kopā dod 9. Atslēga punktus nedod, bet atver finišu. Saskare ar sarkano zonu vai izkrišana aiz grīdas malas izraisa zaudējumu. Punkti uzvarai nav obligāti.

Pirmajai platformai lec pretī no attāluma, piemēram, no sākuma pozīcijas, vienlaikus turot D un nospiežot Space. No nākamajām platformām lec uz labo pusi. Sākot lēcienu tieši zem platformas, var atsisties pret tās apakšu.

## Projekta uzbūve

- `Scripts/Player.cs`: horizontālā kustība, gravitācija, lēciens un priekšmetu stāvoklis.
- `Scripts/Pickup.cs`: Area2D signāls, Player tipa pārbaude, vienreizēja savākšana.
- `Scripts/Level.cs`: HUD, stāsta teksti, uzvara, zaudējums un R.
- `Scenes/Player.tscn`, `Scenes/Pickup.tscn`: atkārtoti izmantojamas scēnas.
- `Scenes/Level1.tscn`: izspēlējams piemēra līmenis.

Collision Inspector ķeksīši: platformas/grīda — Layer 1, Mask nav; Player — Layer 2, Mask 1; Area2D zonas — Layer 3, Mask 2. `.tscn` failos 3. slānim atbilst bitu maskas vērtība 4.

## Individualizēšana

Pēc Build atlasi Level1 sakni un nomaini `Game Title`, `Mission`, `Win Text`, `Lose Text`, `Locked Text`. Izvēlies savu varoni, pasauli un mērķi. Maini Polygon2D figūras vai aizstāj tās ar saviem Sprite2D attēliem. Pielāgo sadursmes formas, saglabājot fizikas sakņu Scale (1,1). Izmaini maršrutu un izspēlē to pēc katras izmaiņas.

Ja atslēgu attēlo kā citu priekšmetu, pielāgo arī HUD vārdu `Atslēga` metodē `UpdateHud`. Iesniegšanai README papildini ar savu stāstu, trīs dizaina izvēļu pamatojumu, resursu avotiem un testēšanas rezultātiem.

## Pārbaudes pirms iesniegšanas

1. Sākumā ir 0 punktu, nav atslēgas, redzama vadība un mērķis.
2. Varonis apstājas pie šķēršļiem, lec no zemes, gaisā nevar lēkt atkārtoti.
3. Katrs priekšmets dod atlīdzību tikai vienreiz, HUD mainās.
4. Finišs bez atslēgas dod norādi, ar atslēgu — uzvaras tekstu.
5. Bīstamā zona un kritiens ārpus laukuma atsevišķi izraisa zaudējumu.
6. Pēc iznākuma kustība un savākšana apstājas; R atjauno visu spēles stāvokli. Atkārto divreiz.
7. Pārbaudi no jaunas projekta kopijas bez `.godot` mapes.

Visi vizuālie elementi ir vienkāršas projektā definētas figūras, ārēji attēli nav nepieciešami. Kods un figūras pieejami ar pievienoto MIT licenci.
