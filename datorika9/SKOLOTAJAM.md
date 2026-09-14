# Datorika 9. klasei: darba organizācija

Pārstrādāts pēc skolotāja sniegtajiem nosacījumiem 2026. gada 14. septembrī. Saglabātas piecas tēmas un 30 nodarbību adreses. Kurss paredzēts skolēniem ar minimālām datora lietošanas un programmēšanas priekšzināšanām.

## Laiks un vērtēšana

- 30 dubultstundas: katra ir divas 40 minūšu mācību stundas.
- Teorija un skolotāja demonstrējums — 10 minūtes; uzdevumi — 15, 20 un 25 minūtes. Trešā uzdevuma laikā ietilpst pārbaude un iesniegšana.
- Atlikušās 10 minūtes ir palīdzībai un atgriezeniskajai saitei. Visi obligātie darbi paredzēti stundās.
- Katrā tēmā 1.–4. nodarbība māca prasmes, 5.–6. nodarbība ir noslēguma projekta pirmā un otrā daļa. Projektam kopā paredzētas četras mācību stundas, ieskaitot nepieciešamo teoriju un demonstrējumu.
- Vērtē tikai trešā uzdevuma iesniegto rezultātu: ir vai nav pilnībā izpildīti tā pārbaudes punkti. Pirmie divi uzdevumi veido šo rezultātu; papildu uzdevums nav ieskaites nosacījums.
- Ikdienā skolēns iesniedz izpildāmu HTML failu. Ja darbam vajadzīgi attēli, skaņas vai README, iesniedz arī tos. 2.5. nodarbībā iesniedz ZIP, kura izvilktajā kopijā darbojas HTML lapa un resursi.
- Tēmas beigās iesniedz GitHub projekta saiti, kursa beigās arī GitHub Pages spēles saiti. Konkrēto iesniegšanas vietu nosaka skolotājs.

## Norādes un atbalsts

Visām lapām ir vienāda secība: mērķis, īsā teorija, pilns sākuma kods, trīs uzdevumi, iesniegšanas pārbaudes un izvēles papildu uzdevums. Laika sadalījums paliek skolotāja plānošanai; skolēnu lapās laika norādes un `small-note` bloki nav redzami. Pārejas starp programmām izceltas ar norādi “Vide”. Soļus var atzīmēt; atzīmes saglabājas konkrētajā pārlūkā, bet tās nav vērtējums.

Katrs no trim galvenajiem uzdevumiem atrodas atsevišķā `logic-box` blokā. Nodarbības daļu ātro saišu josla nav izmantota. 1.2. nodarbības teorijā ir galveno HTML tagu atgādne sešās atveramās grupās.

Nodarbību un tēmu lapu sānjoslā ir attiecīgās tēmas sešu nodarbību saraksts un saite uz tēmas sākumu. Pašreizējā lapa ir izcelta. Šaurā ekrānā saraksts atrodas virs satura un ir ritināms horizontāli.

Skolēnam nav jāmeklē iepriekšējās nodarbības kods. Projekta otrajā daļā paredzēta sava darba turpināšana, bet dots arī pilns rezerves paraugs. Vēlākās nodarbībās skolēns pārnes izvēlētās savas izmaiņas uz jauno pilno paraugu. Gatavās palīgfunkcijas nav jāpārraksta vai jāapgūst visas vienlaikus: uzdevums nosauc konkrēti maināmo vietu un tās rezultātu.

Skolotājs sākumā parāda vienu jaunās teorijas izmantošanas piemēru. Individuālās palīdzības laikā skolēns rāda pirmo nepabeigto soli un savu failu. Īsie soļi, redzams mērķis un izvēles veidā atveramais pilnais kods paredzēti, lai būtu vieglāk sekot darbam, arī skolēniem ar UDHS. Piemērotība un laika aplēses vēl jāpārbauda reālā klasē; šī pārstrāde nav skolēnu izmēģinājuma rezultāts.

Obligāto uzdevumu izpildei pietiek ar materiāliem šajā vietnē. MI rīki nav uzdevumu sastāvdaļa. Ārējie resursi vajadzīgi kontam, darba glabāšanai un publicēšanai; mācību teorija un kods ir šajā repo.

## Windows un Git sagatavošana

Pirms kursa pārbauda Windows 11 datorus skolēnu individuālajos kontos. Darba mapes ir `Desktop/datorika9-tema1` līdz `Desktop/datorika9-tema5`; lejupielādes — `Downloads`. Katras tēmas mape ir atsevišķs Git projekts. Ikdienas faili saucas `11.html`, `12.html` u. tml.; tēmas noslēguma fails — `index.html`.

VS Code var uzstādīt no Microsoft Store. Git uzstādīšanai skolotājs vajadzības gadījumā izmanto administratora tiesības. Pārbauda arī Paint un Sound Recorder; skaņas ierakstīšanai vajadzīgs mikrofons. Ja ierakstīšana nav iespējama, 2.4. nodarbībā ir lokāls gatavs WAV fails. Tas ļauj izpildīt lapas skaņas integrāciju, taču paša ieraksta veidošanu šajā gadījumā skolēns neapgūst.

Skolēni Git lieto VS Code sadaļā Source Control: Initialize Repository → Stage Changes (+) → Commit → Publish to GitHub, vēlāk Commit → Sync Changes. GitHub konta pieslēgšana vai Settings Sync nesaglabā projekta failus un neaizstāj Git autora iestatījumus.

Pirms pirmā Commit katram skolēnam jāsagatavo Git autora vārds un e-pasts. Vari to izdarīt bez termināļa projekta lokālajā konfigurācijā: pēc Initialize Repository ar VS Code File → Open File atver `Desktop/datorika9-tema1/.git/config` (paslēpto mapes daļu var ierakstīt faila ceļā). Saglabājot jau esošās sadaļas, pievieno:

```ini
[user]
    name = SkolenaGitHubLietotajvards
    email = skolena-GitHub-noreply-adrese
```

Abus parauga tekstus aizstāj ar konkrētā konta vērtībām; precīzo noreply adresi ņem GitHub Settings → Emails. Lokālā konfigurācija attiecas uz šo projektu, tāpēc jaunas tēmas mapē to atkārto. Skolotājs var izvēlēties arī iepriekš sagatavotu lietotāja konfigurāciju. `.git` saturu nekopē starp skolēniem un nepievieno iesniedzamajiem arhīviem.

Pirmajā nosūtīšanā izmanto publisku mācību projektu, kurā ir tikai darbam paredzētie materiāli. Tas nodrošina skolotājam atveramu saiti un ļauj izmantot GitHub Pages. Kursa lapas publicēšanas iestatījumus skolēns maina 5.6. nodarbībā; pašas ebSkola vietnes publicēšana šajā pārstrādē netiek veikta.

Pogu nosaukumu avoti: [VS Code Source Control](https://code.visualstudio.com/docs/sourcecontrol/quickstart), [Git konfigurācijas dokumentācija](https://git-scm.com/docs/git-config), [GitHub Pages publicēšanas avots](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site). Nosaukumi pārbaudīti 2026. gada 14. septembrī; skolas uzstādītajā versijā tie var nedaudz atšķirties.

Windows lietotņu atgādnes: [Microsoft Paint](https://www.microsoft.com/en-us/windows/paint) un [Sound Recorder](https://support.microsoft.com/en-us/windows/apps/sound-recorder-app-for-windows-faq). Ierakstu atrašanās vietu un eksporta iespējas pārbauda skolas uzstādītajā Sound Recorder versijā.

## Satura un sasniedzamo rezultātu robežas

Par pamatu izmantota [sasnRez.html 9. klases sadaļa](../sasnRez.html#datorika9), kā norādījis skolotājs. Tās teksts nav mainīts. Stundu SR piesaistes norāda praktiski vingrinātu rezultāta daļu, nevis automātiski apliecina visa plašā SR izpildi. Jaunais pārklājuma saraksts ir [mācību satura auditā](../macibu-satura-audits.md).

Agrākā piesaiste “HTML/CSS lapa = strukturēts Office dokuments” vai “JavaScript masīvs = izklājlapa” nav pietiekama. Tāpat pārlūkspēle neaizstāj mikrokontroliera un sensoru programmēšanu. Šīs nepamatotās piesaistes ir noņemtas, saglabājot lietotāja prasītās piecas tēmas.

Šajā kursā tieši vingrina vienkāršu lapu veidošanu, programmēšanas pamatus, failu pārvaldību, darba nosūtīšanu GitHub, attēlu un skaņas iekļaušanu, spēles plānošanu un pārbaudi. Ar kursu vien nepietiek, lai apliecinātu visus 37 plašos rezultātus vietnes sarakstā. Īpaši vajadzīgi atsevišķi praktiski darbi izklājlapām, lielu teksta dokumentu noformēšanai, prezentāciju lietotnei, video apstrādei, datortīkliem un programmējamām ierīcēm ar sensoriem. Plašo rezultātu atlikušās daļas jāvērtē pēc skolēnu agrāko klašu darbiem vai citiem kursiem; to apguve netiek pieņemta par notikušu.

SR 1.4.2 paredz testēšanas rezultātu dokumentēšanu. Tāpēc projektos saglabāti īsi faktiski README pārbaudes ieraksti; vispārīgu secinājumu pārrakstīšana ir izņemta. SR 2.4.6 šeit vingrina skaņas ieraksta un formāta daļu, nevis pilnu video izveides un pēcapstrādes rezultātu. SR 2.4.8 gadījumā apvieno tekstu, attēlu un audio; video komponente šajās nodarbībās nav iekļauta.

## Materiālu uzturēšana

Vietne paliek statiska; būvēšanas solis nav vajadzīgs. Nodarbību HTML failus var rediģēt tieši. Papildu stils un soļu/kopēšanas atbalsts ir tikai `kursa-stils.css` un `kursam.js`, tāpēc citu kursu izskats nav mainīts.

Pilns sākuma kods ir gan nodarbības HTML, gan failā `sakuma-kodi/NN.html`. Mainot piemēru, atjauno abas kopijas. 2.5. un 2.6. nodarbības ZIP komplektā jābūt atbilstošajam kodam un lokālajiem resursiem. Mājaslapas kodā ievietotais paraugs jāiekodē kā HTML teksts (`&lt;`, `&gt;`, `&amp;`); lejupielādējamais fails ir īsts HTML.

Pārbaudei izmanto `python3 scripts/check_datorika9.py`. Pārlūka pārbaudes skaidrojums ir `scripts/README.md`.
