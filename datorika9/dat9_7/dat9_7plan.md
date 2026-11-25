# 7. tēma — Tīkli, internets un drošība (plāns)

> **Status:** plan only. No lesson pages, tests or starter files exist yet.
> Write the lessons in the format of the existing Datorika 9 lessons: theory
> with examples, "Sākuma kods un darba vieta", three tasks with "Vide:",
> "Izmanto teoriju:" and "Gatavs, kad:", and "Iesniedz 3. uzdevuma rezultātu".

## Why this topic exists

After the 2026-11-23 law check (`datorika9/law-analysis-plan.md`), seven
results that this course counts as datorika have no lesson. They cover
networks, internet services, and health, safety and ethics:

- **2.3.2:** how a simple network is built, client-server architecture,
  network devices, modelling common networks.
- **2.5.1, 2.5.4:** email and other communication tools, choosing an
  internet provider and connection, internet services, and the benefits and
  risks of online collaboration.
- **3.3.1, 3.3.3, 3.3.4, 3.3.5:** ergonomics and overuse of games and
  devices, safety and ethics online, identity theft, and device, software
  and data security.

**The thread:** the game the students published in 5.6 is the example
throughout. They watch it travel from the GitHub Pages server to a browser,
measure what a connection does to it, and build small security tools in
HTML and JavaScript: a phishing quiz and a password checker. At the end they
add a "Droša spēlēšana" page to their own game. The topic keeps the course's
browser-game thread, and each lesson has an HTML starter, as in topics 1–5.

**Place in the course:** after topic 6. The author decided on 2026-11-25
(D5) to keep the order: topics 1–5 stay as they are, then 6, then 7. It
needs a published game (5.6), and it reuses JavaScript from topics 3–4:
variables, `if`, arrays, functions, `setInterval`.

**Prerequisites:** topics 1–5, especially events and functions (4.1–4.2),
the timer (4.4) and the published game (5.6).

## Results covered (MK Nr. 747, 7. pielikums, beidzot 9. klasi)

| Kods | Sasniedzamais rezultāts | Nodarbības |
|---|---|---|
| 2.3.2. | Skaidro vienkārša datortīkla uzbūves pamatprincipus (to skaitā klientservera arhitektūru). Klasificē ar datortīkliem biežāk saistītas ierīces un apraksta to izmantošanas iespējas, modelējot biežāk lietoto datortīklu piemērus. | 7.1, 7.2, 7.6 |
| 2.5.1. | Apmainās ar informāciju virtuālajā vidē, izmantojot dažādas formas un risinājumus, tai skaitā skaidro e-pasta adreses struktūru un lieto dažādas e-pasta sistēmas un citus saziņas rīkus. | 7.3 |
| 2.5.4. | Nosauc piemērotākā interneta pakalpojumu sniedzēja un interneta pieslēguma abonēšanas veida izvēles svarīgākos kritērijus, kā arī biežāk lietoto interneta pakalpojumu veidus. Raksturo tiešsaistes sadarbības pakalpojumu un rīku izmantošanas priekšrocības un iespējamos riskus. | 7.2, 7.5 |
| 3.3.1. | Raksturo ergonomiskās prasības darba vides iekārtošanai. Patstāvīgi veic un ievēro pasākumus veselības traucējumu mazināšanai darbā. Apzinās faktorus, kas var ietekmēt un apdraudēt veselību, un veic pasākumus, lai izvairītos no iespējamajiem apdraudējumiem un atkarībām, tai skaitā datorspēļu, viedierīču un sociālo tīklu pārmērīgas lietošanas. | 7.6 |
| 3.3.3. | Rīkojas saskaņā ar drošības un ētikas normām darbā ar programmvadāmajām ierīcēm un tiešsaistē un skaidro to nozīmi. | 7.3, 7.4, 7.6 |
| 3.3.4. | Mazina identitātes zādzības iespējas, raksturojot identitātes zādzības metodes un piemērus. | 7.4 |
| 3.3.5. | Apzinās faktorus, kas var ietekmēt un apdraudēt ierīces, programmatūras un datu drošību, un veic pasākumus, lai izvairītos no iespējamajiem apdraudējumiem. | 7.5, 7.6 |

The lessons also revisit 2.6.1 and 2.6.2, because every starter is a small
JavaScript program that students extend and test, and 2.5.3 (sharing
files and links).

When the lessons are written, cite these in `.lesson-meta` in the current
format: `<a href="/sasnRez#dat9-2-3-2" title="{law text}">SR 2.3.2. {label}</a>`,
with 1–4 citations per lesson.

## Tools (Windows 11)

- VS Code, Edge or Chrome, and the student's GitHub Pages game, as in
  topics 1–5.
- **Browser DevTools:** the Network tab, throttling, and Offline mode.
- **Command Prompt:** `ipconfig`, `ping`, `tracert`. All three are allowed
  on the school network (author, 2026-11-25).
- **diagrams.net** (draw.io) in the browser, for network diagrams. It needs
  no account.
- **The student's personal email**, the one the GitHub account uses. The
  school email is blocked for registration on most websites, so students
  use their personal address for accounts and for 7.3 (author,
  2026-11-25).

## Starter files

Each lesson has `sakuma-kodi/7S.html`, a short page with a ready-made
script, in the style of `41.html`–`46.html`: comments mark what to change.
Media that the starters need go in `sakuma-kodi/atteli/` as before.

## Lessons

All student files go in `Desktop/datorika9-tema7` and in the topic repository
on GitHub, as in topics 1–5.

### 7.1 Kā spēle nonāk pie spēlētāja: klients, serveris un tīkls

- **File:** `dat9_71.html`
- **Starter:** `sakuma-kodi/71.html` is a "Tīkla pētnieks" page. It loads
  three files with `fetch` (its own `.html`, an image and a missing file)
  and shows the HTTP status, the size and the time in milliseconds for
  each.
- **Goal:** Šajā nodarbībā tu izsekosi, kā tava spēle no GitHub servera
  nonāk līdz pārlūkam, un uzzīmēsi šī ceļa tīkla shēmu.
- **SR:** 2.3.2.
- **Theory:**
  - Client and server, request and response, and status codes (200, 404).
  - IP address and domain name, and DNS as the "phone book".
  - Devices on the path: computer, Wi-Fi access point, switch, router,
    modem, the provider's network, the server.
  - LAN vs internet.
  - `ipconfig`: your address and the default gateway.
- **Task 1 (try):** open your published game, DevTools → Network, and
  reload. List every file the game loads, with its status and size. Which
  one is the biggest?
- **Task 2 (build):**
  - Draw the path from your computer to the GitHub Pages server in
    diagrams.net, labelling each device and what it does.
  - Add your real IP address and gateway from `ipconfig`.
  - Export the diagram as PNG and put it in `71.html`.
- **Task 3 (break and test):**
  - In the starter, change one file name to a missing one, then predict and
    check the status code.
  - Turn on DevTools → Offline and reload: what does `fetch` report?
  - Run `ping` and `tracert` to `github.io`: note the time in ms and count
    the hops.
  - Hand in `71.html` with the diagram.

### 7.2 Mājas un skolas tīkls, pieslēgums un ātrums

- **File:** `dat9_72.html`
- **Starter:** `sakuma-kodi/72.html` is a "Lejupielādes kalkulators". You
  enter the file size in MB and the speed in Mbit/s, and it shows the time.
  It has a deliberate bits/bytes bug (it does not multiply by 8).
- **Goal:** Šajā nodarbībā tu salīdzināsi mājas un skolas tīklu,
  izvēlēsies piemērotāko interneta pieslēgumu pēc kritērijiem un
  izlabosi kalkulatoru, kas jauc bitus ar baitiem.
- **SR:** 2.3.2., 2.5.4.
- **Theory:**
  - Home network vs school network: Wi-Fi, cable, guest network, a server
    in the school, who manages it.
  - Connection types: optical fibre, cable, DSL, 4G/5G mobile, satellite.
  - Choosing a provider:
    - download and upload speed;
    - price per month and contract length;
    - coverage at your address;
    - data limits;
    - support.
  - Common internet services: the web, email, cloud storage, streaming,
    video calls, online games.
  - Mbit/s vs MB, and why advertised speeds are "up to".
- **Task 1 (try):** run the calculator for your game (size from 7.1) and
  for a 4 GB game download. Compare with a stopwatch on a real download,
  find the 8× error and fix it.
- **Task 2 (build):**
  - Model a home network and the school network in diagrams.net, with the
    devices from 7.1.
  - Add upload time and a "price per Mbit/s" field to the calculator, so
    that three provider offers can be compared.
  - The data comes from the teacher's handout of current Latvian offers.
- **Task 3 (break and test):**
  - Test the calculator with 0, negative and empty input and make it show a
    clear message (2.6.2).
  - In one paragraph in `72.html`, choose the best offer for a family of
    four that streams and plays online, and justify it with three criteria.
  - Hand in `72.html`.

### 7.3 E-pasts un saziņas rīki

- **File:** `dat9_73.html`
- **Starter:** `sakuma-kodi/73.html` is an "E-pasta adreses pārbaudītājs".
  It splits an address at `@` and shows the user name and the domain. It
  accepts addresses with two `@` signs, which is a bug the students find.
- **Goal:** Šajā nodarbībā tu izskaidrosi e-pasta adreses uzbūvi, nosūtīsi
  lietišķu e-pastu ar saiti uz savu spēli un izvēlēsies piemērotāko saziņas
  rīku dažādām situācijām.
- **SR:** 2.5.1., 3.3.3.
- **Theory:**
  - The structure of an address: user name, `@`, domain, top-level
    domain.
  - Webmail vs an email app.
  - The school email vs a personal one. The school address is blocked for
    registration on most websites, so accounts such as GitHub use the
    personal address. Which one to use for what, and keeping both secure.
  - Subject, greeting, To / CC / BCC, attachment vs link, and file size
    limits.
  - Other tools: chat, video calls, forums, and when each fits.
  - Netiquette, and what not to send.
  - Reply All mistakes, and BCC to protect addresses.
- **Task 1 (try):** test the checker with ten given addresses, find the
  ones it gets wrong, and fix the two-`@` bug and "no dot in the domain".
- **Task 2 (build):**
  - Send the teacher an email from your personal address with a clear subject,
    a greeting, two sentences about your game, and the GitHub Pages link
    (not an attachment).
  - Put a screenshot of the sent message in `73.html`.
- **Task 3 (break and test):**
  - Work through three scenario cards in `73.html`: an invitation to 30
    parents, a file of 40 MB, and an angry reply to a classmate.
  - For each, write which tool and field you use (BCC, a cloud link, a
    pause before answering) and why.
  - Hand in `73.html`.

### 7.4 Pikšķerēšana un identitātes zādzība

- **File:** `dat9_74.html`
- **Starter:** `sakuma-kodi/74.html` is a "Pikšķerēšanas detektīvs" quiz
  game. An array of messages, each with sender, text, link and `isDrosa`. It
  has a "Drošs / Aizdomīgs" button pair and score and lives, as in topic 4.
- **Goal:** Šajā nodarbībā tu atpazīsi identitātes zādzības metodes,
  izveidosi savu pikšķerēšanas atpazīšanas spēli un saplānosi, kā
  pasargāt savus kontus.
- **SR:** 3.3.4., 3.3.3.
- **Theory:**
  - Methods and examples:
    - phishing email and SMS (smishing);
    - fake login pages with look-alike domains (`github.com` vs
      `glthub.com`);
    - fake profiles;
    - data leaks and password reuse;
    - shoulder surfing;
    - "you have won" messages.
  - Signs to check: sender, link target (hover), urgency, a request for a
    password or code.
  - What to do: don't click, report, change the password, tell an adult or
    the teacher. Check haveibeenpwned.com.
- **Task 1 (try):** play the quiz. For every wrong answer, write which sign
  you missed.
- **Task 2 (build):** add three messages of your own to the array: one
  look-alike domain, one SMS and one safe message. Add an explanation that
  shows after each answer.
- **Task 3 (break and test):**
  - Make the game show the real link target when the mouse is over the
    link, and check that every message has a correct `isDrosa`.
  - Add the list "Mani 3 soļi kontu aizsardzībai" under the game.
  - Hand in `74.html`.
- **Watch out:** examples must use invented brands and domains, never a
  real bank or the school's real login page.

### 7.5 Ierīču, programmatūras un datu drošība

- **File:** `dat9_75.html`
- **Starter:** `sakuma-kodi/75.html` is a "Paroles stipruma mērītājs". It
  scores length and character types, so it rates `Parole123!` as "strong".
- **Goal:** Šajā nodarbībā tu noteiksi, kas apdraud ierīces, programmatūru
  un datus, uzlabosi paroles pārbaudītāju un izveidosi sava datora drošības
  plānu.
- **SR:** 3.3.5., 2.5.4.
- **Theory:**
  - Threats:
    - malware (virus, ransomware, spyware);
    - outdated software;
    - fake downloads;
    - public Wi-Fi;
    - lost devices;
    - human error.
  - Protection:
    - updates;
    - Windows Security;
    - downloads only from trusted sources;
    - backups (the 3-2-1 rule; Git and GitHub as a backup of code);
    - long passphrases and a password manager;
    - two-factor authentication;
    - HTTPS.
  - Risks of online collaboration tools: shared links open to "anyone",
    access rights, and secrets committed to a public repository.
- **Task 1 (try):** test the meter with ten passwords from the theory and
  find the ones it rates wrongly.
- **Task 2 (build):** add an array of the 20 most common passwords and a
  check against it. Score passphrases of four words higher than short
  complex passwords. Show the reason for each score.
- **Task 3 (break and test):**
  - Check the security settings of your GitHub account and of the personal
    email it uses: recovery options, active sessions, two-factor
    authentication. Turn on two-factor authentication on GitHub.
  - Check your game repository for any personal data or passwords.
  - Fill in a five-point "Mana datora drošības plāns" in `75.html`: updates,
    antivirus, backup, passwords, shared links.
  - Hand in `75.html`.
- **Watch out:** students must never type their real passwords into any
  exercise page. Say this in the theory and in task 1.

### 7.6 Noslēguma darbs: "Droša spēlēšana" lapa tavai spēlei

- **File:** `dat9_76.html`
- **Starter:** `sakuma-kodi/76.html` is a page template with sections
  "Kā spēle nonāk pie tevis", "Veselīga spēlēšana", "Drošība un privātums"
  and "Pārtraukuma atgādinājums". It includes a `setInterval` timer that
  shows a reminder after N minutes, with N set to 1 for testing.
- **Goal:** Šajā noslēguma darbā tu pievienosi savai publicētajai spēlei
  lapu par drošu un veselīgu spēlēšanu ar pārtraukuma atgādinājumu un to
  publicēsi.
- **SR:** 3.3.1., 3.3.3., 3.3.5., 2.3.2.
- **Theory:**
  - Ergonomics: screen distance and height, light, posture, the 20-20-20
    rule.
  - Signs of overuse of games, phones and social networks, and how to set
    limits (Windows and phone screen time).
  - Where to get help.
- **Step 1:** add `drosiba.html` to your game repository with the four
  sections: your 7.1 network diagram, ergonomics tips for your players, the
  safety and privacy rules of your game, and the break reminder.
- **Step 2:** connect the reminder to your game. After N minutes of play
  the game pauses and shows the reminder. Reuse `setInterval` and the pause
  from 4.4. Test it with N = 1, then set it to 30.
- **Step 3:** link the page from your game's start screen, publish with
  GitHub Pages and check the live version. Hand in the game link and the
  `drosiba.html` link.
- **Assessment (SLA):**
  - The network diagram is correct and labelled.
  - The ergonomics and overuse advice is specific and fits the audience.
  - The safety section names at least three real threats and what the
    player should do.
  - The reminder works in the live game, pauses play and does not start
    twice.
  - The page has no personal data.

## Open questions for the author

**Decided (2026-11-25):**

- Students use their personal email for accounts and 7.3, because the
  school email is blocked for registration on most websites.
- `ping` and `tracert` are allowed.
- The topic order stays 1–7.

Still open:

1. **Two-factor authentication on GitHub (7.5).** It needs a phone or an
   authenticator app. Check that students may use their phones in class,
   and plan a backup for students without one: recovery codes stored
   safely.
2. **Provider offers (7.2).** Real prices change quickly. Use a teacher
   handout dated each school year, or the providers' public pages with a
   date noted.
3. **Overlap with Sociālās zinības or Sports un veselība.** 3.3.1 (overuse,
   ergonomics) may also be taught there. Agree with those teachers, or keep
   7.6 short on theory and long on the reminder feature.
