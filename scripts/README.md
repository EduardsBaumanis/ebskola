# Datorika 9 materiālu pārbaudes

`python3 scripts/check_datorika9.py` pārbauda lokālās saites un enkurus, 30 nodarbību struktūru, lapā ievietotā un lejupielādējamā sākuma koda vienādību un abu multivides ZIP komplektu saturu. Vajadzīga tikai Python standarta bibliotēka.

`python3 scripts/check_datorika9_browser.py` papildus atver piemērus pārlūkā, izpilda skolēna izmaiņu scenārijus un pārbauda spēļu darbību, kā arī kopēšanu, soļu atzīmes un lapu platumu. Pārbaude pati palaiž īslaicīgu lokālu HTTP serveri. Tā neveido GitHub kontus un neko nepublicē.

Pārlūka pārbaudei vajadzīga Python pakotne `playwright` un Chrome/Chromium. Ceļu var norādīt ar vides mainīgo `DATORIKA_CHROME`; pēc noklusējuma izmanto `/usr/bin/google-chrome`, ja tas ir pieejams, citādi Playwright Chromium. Pakotnes un pārlūks nepieciešami tikai pārbaudēm; pati vietne paliek statiska un bez būvēšanas soļa.

Pārlūka pārbaudes neaizstāj izmēģinājumu skolas Windows kontā: programmu uzstādīšana, Paint/Sound Recorder iespējas, Git autorizācija un GitHub Pages publicēšana jāpārbauda skolas vidē.
