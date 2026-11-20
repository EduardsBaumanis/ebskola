# 15. tēma — Datortīkli, ierīces un droša darba vide (plāns)

> **Status:** plan only. No lesson pages exist yet. Write the lessons with
> `plan.md` section 4 (the task standard) and decisions D1–D8, F1–F4.

## Why this topic exists

The other topics never cover computer networks, operating systems, comparing
devices, or health and safety beyond a short ergonomics check in 1.1. MK
Nr. 416 requires all of these for Programmēšana I. This topic covers one
optimal-level result and nine general-level results that no lesson covers now.

**Place in the course:** right before topic 16. Topic 16 puts an app on the
internet, so a student who has done this topic will already know what
HTTP/HTTPS, a router, an IP address and a port are. 16.1 and 16.5 should
link back here.

**Prerequisites:** topics 1–14. 15.3 and 15.4 use `requests` and the virtual
environment from 11.1.

## Results covered (MK Nr. 416, 7. pielikums)

| Kods | Līmenis | Sasniedzamais rezultāts | Stundas |
|---|---|---|---|
| 2.3.1. | optimālais | Salīdzina dažāda veida datortīklus, to uzbūvi, drošības risinājumus un lietošanas iespējas atbilstoši mērķauditorijai. Veic maršrutētāja konfigurēšanu, izmantojot vedni datortīkla vajadzībām. | 15.1, 15.2, 15.6 |
| 2.3.1. | vispārīgais | Nosauc un raksturo ar piemēriem biežāk lietotos datortīkla veidus un risinājumus, t. sk. akcentējot tā drošību. Izvēlas piemērotāko pieejamo datortīklu, ņemot vērā drošības apsvērumus un izmaksas. | 15.1 |
| 3.1.3. | vispārīgais | Nosauc iespējamos drošības riskus, lietojot atvērtu datu apmaiņu, salīdzina atvērtas un šifrētas datu apmaiņas priekšrocības un trūkumus. | 15.3 |
| 2.3.9. | vispārīgais | Nosauc un ar piemēriem raksturo biežāk lietoto programmvadāmo ierīču operētājsistēmas. Sastāda nepieciešamo programmvadāmo ierīču, programmatūras un citu resursu sarakstu atbilstoši lietotāja vajadzībām konkrētā uzdevuma veikšanai. | 15.4, 15.6 |
| 2.3.11. | vispārīgais | Pielāgo operētājsistēmas un lietotnes iestatījumus lietotāju vajadzībām, veicinot ikdienas darba drošību un efektivitāti. Izvēlas konkrētā uzdevuma veikšanai piemērotāko(-ās) lietotni(-es) un pamato savu izvēli. | 15.4 |
| 2.1.2. | vispārīgais | Salīdzina dažādas programmvadāmas ierīces un to izmantojamību sadzīvē un ražošanā, tai skaitā datorvadāmās iekārtas datorizētu telpisku modeļu, digitālu rasējumu un attēlu izveidē. | 15.4 |
| 2.1.1. | vispārīgais | Tehnoloģiju izvēlē ņem vērā informāciju par darba apstākļu ietekmi uz lietotāju veselību un vidi, lai neradītu apdraudējumu sev un citiem. | 15.5 |
| 3.1.1. | vispārīgais | Apzinās un skaidro faktorus, kas var ietekmēt un apdraudēt cilvēka fizisko un garīgo veselību, izstrādājot vai lietojot risinājumus, un veic pasākumus, lai izvairītos no apdraudējumiem un atkarībām, t. sk. viedierīču pārmērīgas lietošanas. Analizē savas darba vietas iekārtojumu atbilstoši ergonomikas prasībām un iekārto to atbilstoši veicamajam uzdevumam. | 15.5 |
| 3.1.2. | vispārīgais | Risinājuma izstrādes procesā ievēro darba drošības prasības un lieto darba aizsardzības līdzekļus, paredz nepieciešamos darba aizsardzības līdzekļus apdraudējumu samazināšanai un pārbaudei. | 15.5 |
| 3.1.4. | vispārīgais | Skaidro sava risinājuma lietošanai nepieciešamo tehnoloģiju un veicamo darbību ietekmi uz lietotāju veselību un vidi, salīdzinot dažādus riska faktorus. | 15.5, 15.6 |

When the lessons are written, cite these in `.lesson-meta` in the current
format: short label, the law's text in `title`, and a link to
`/sasnRez#prog1-o-…` or `/sasnRez#prog1-v-…`.

## Tools (Windows)

- Windows Terminal / PowerShell: `ipconfig`, `ping`, `tracert`, `nslookup`.
  These are already on every school computer.
- Python `socket`, `platform`, `shutil`, `urllib` (standard library) and
  `requests` (installed in 11.1).
- A router to configure. See the open questions: students must not change
  the school network.

## Lessons

All student files go in `tema15/` in the `programmesana-pamatkurss`
repository. Notes go in `README.md` under `### 13.x …` (D3). Imported files
have the lesson number last (D2).

### 15.1 Datortīkla uzbūve un veidi

- **File:** `prog1_151.html`
- **Goal:** Šajā stundā tu uzzīmēsi sava mājas vai skolas tīkla shēmu un ar
  komandām atradīsi sava datora IP adresi, maršrutētāju un ceļu līdz
  serverim.
- **SR:** 2.3.1. (vispārīgais), 2.3.1. (optimālais)
- **Theory:** LAN, WLAN, WAN and the internet. Router, switch, access point.
  IP address, DNS. Wired vs Wi-Fi: speed, cost, security. Open and protected
  Wi-Fi, WPA2/WPA3.
- **Task 1 (try):** run `ipconfig`, `ping ebskola.lv`, `tracert ebskola.lv`
  and `nslookup ebskola.lv`, and write down what each line means.
- **Task 2 (build):** write `tikls_151.py`, which 15.6 imports. It reads the
  computer name and local IP with `socket`, pings three addresses with
  `subprocess` in a function `parbaudi(adrese)`, and prints a small table.
- **Task 3 (test):** ping an address that does not exist and a name that
  does not resolve. Catch both errors and print a clear message.
- **Notebook:** a comparison table of three network types (home, school,
  café hotspot) by speed, cost and security, plus "Kuru izvēlētos …?"
- **Watch out:** `ping` output on Windows is in the system language. Parse
  only the return code, not the text.

### 15.2 Maršrutētāja konfigurēšana

- **File:** `prog1_152.html`
- **Goal:** Šajā stundā tu ar vedni iestatīsi maršrutētāju klases tīklam: tīkla
  nosaukumu, drošu paroli, viesu tīklu un administratora paroli.
- **SR:** 2.3.1. (optimālais)
- **Theory:** what a router setup wizard changes: SSID, WPA2/WPA3 key, admin
  password, guest network, DHCP range, firmware update. Why the default admin
  password is the first thing attackers try.
- **Task 1 (try):** go through the wizard on a router emulator or a spare
  router (see open questions) and screenshot every step.
- **Task 2 (build):** set up the "klases tīkls" to a given brief: a separate
  guest network, WPA2/WPA3, a changed admin password, and a DHCP range for 30
  devices.
- **Task 3 (test):** a classmate checks the settings against the brief with
  a checklist. The student fixes everything that does not match and writes
  why each setting matters.
- **Watch out:** this is the only lesson with no Python. It still ends with a
  commit: screenshots in `tema15/152/` and the checklist in the README.

### 15.3 Atvērta un šifrēta datu apmaiņa

- **File:** `prog1_153.html`
- **Goal:** Šajā stundā tu redzēsi, kā izskatās dati, kas ceļo bez
  šifrēšanas, un salīdzināsi tos ar HTTPS savienojumu.
- **SR:** 3.1.3. (vispārīgais)
- **Theory:** HTTP vs HTTPS. What a man-in-the-middle can read on open Wi-Fi.
  Certificates and the padlock in the browser. A hash is not encryption.
  Passwords are never sent or stored as plain text.
- **Task 1 (try):** `requests.get` against an `http://` and an `https://`
  test address. Compare the URL, `response.url`, the status and the
  certificate info.
- **Task 2 (build):** `atslega_153.py` with a toy Caesar cipher
  (encrypt/decrypt). Then show with a loop how fast it breaks, and compare it
  with `hashlib.sha256` for storing a password.
- **Task 3 (test):** try to "log in" with the wrong password against the
  stored hash, and show that the hash cannot be turned back into the
  password.
- **Notebook:** three risks of open data exchange and how HTTPS reduces each.
- **Watch out:** do not ask students to sniff other people's traffic. Use
  only their own requests.

### 15.4 Operētājsistēmas un programmvadāmas ierīces

- **File:** `prog1_154.html`
- **Goal:** Šajā stundā tu uzrakstīsi programmu, kas apraksta tavu datoru, un
  sastādīsi ierīču un programmatūras sarakstu konkrētam uzdevumam.
- **SR:** 2.3.9., 2.3.11., 2.1.2. (all vispārīgais)
- **Theory:** Windows, macOS, Linux, Android, iOS, and firmware in
  microcontrollers. What an OS does. Devices: PC, phone, microcontroller, 3D
  printer, CNC and laser cutter (CAD/CAM). Accessibility and power settings
  in Windows.
- **Task 1 (try):** `platform`, `os.cpu_count()` and `shutil.disk_usage` in
  `154.py`.
- **Task 2 (build):** `ierices_154.py` with a function that returns a
  dictionary of facts about the computer. Write it to `dators_154.json`.
- **Task 3 (test):** given a brief (for example a video-editing club or a
  robotics club), write a device and software list in the README with
  reasons. Compare it with the JSON from task 2: is this computer enough?
- **Also in the lesson:** change three Windows settings for safety and
  comfort (night light, notifications or focus, a screen lock time) and
  explain each choice. This is the 2.3.11 part.

### 15.5 Veselīga un droša darba vide

- **File:** `prog1_155.html`
- **Goal:** Šajā stundā tu novērtēsi savu darba vietu un uzrakstīsi
  programmu, kas atgādina par pārtraukumiem.
- **SR:** 2.1.1., 3.1.1., 3.1.2., 3.1.4. (all vispārīgais)
- **Theory:** posture, screen distance, the 20-20-20 rule, and hearing with
  headphones. Electrical safety: cables, chargers, no liquids. Screen time
  and notifications that are designed to keep you hooked. The energy use and
  e-waste of devices and data centres.
- **Task 1 (try):** an ergonomics checklist of your own workplace, scored
  in the README.
- **Task 2 (build):** `atgadinajums_155.py` asks for the work and break
  length in minutes and counts down with `time.sleep`. It prints a
  reminder, and can play a sound with `winsound`, which is Windows only.
- **Task 3 (test):** wrong input (0, negative numbers, text). Add a "test
  mode" where minutes are seconds so the whole cycle can be checked in class.
- **Notebook:** compare two risk factors from your own project (for example
  late-night gaming and a bright screen) and suggest one change for each.
- **Link:** this replaces the thin ergonomics coverage in 1.1, 1.6 and 2.6.
  Those lessons can link here.

### 15.6 Noslēguma projekts: Datorklases tehniskais pārskats

- **File:** `prog1_156.html`
- **Goal:** Šajā projektā tu sagatavosi pārskatu par vienu datorklasi vai
  savu mājas darba vietu: tīkla shēmu, ierīču sarakstu, drošības un veselības
  ieteikumus, un Python programmu, kas savāc datora datus.
- **SR:** 2.3.1. (optimālais), 2.3.9., 3.1.4. (vispārīgais)
- **Step 1:** a network diagram (paper and photo, or draw.io) with the
  router, access points and devices, plus three security recommendations.
- **Step 2:** `parskats_156.py` imports `ierices_154.py` and `tikls_151.py`,
  runs the ping checks, and writes `parskats_156.md`, a Markdown report with tables.
- **Step 3:** health and environment section. Ergonomics findings, the
  energy use estimate for the room for one school day, and two improvements.
- **Assessment (SLA):** the diagram is correct and readable; the program
  runs and handles an offline computer; the recommendations give reasons
  that name the risk; and there is a commit history with clear messages.

## Open questions for the author

1. **Router for 15.2.** Options: (a) the vendor's online emulator of a home
   router's web interface, if one is available in the classroom, (b) one or two
   spare home routers not connected to the school network, (c) Cisco Packet
   Tracer, which is free but needs a Netacad account. (a) is quickest. Check
   that the school's filters allow it.
2. **Sound in 15.5.** `winsound` is in the standard library and Windows
   only, which fits D8. Is sound wanted in class at all?
