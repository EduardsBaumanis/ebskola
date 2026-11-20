# 9. tēma — Tīkls, serveris un kriptogrāfija: daudzspēlētāju spēle (plāns)

> **Status:** plan only. No lesson pages exist yet. Write the lessons in the
> Programmēšana II format: Teorija, three tasks, "Ko sagatavo" (what goes in
> the GitHub repository and `README.md`, and how to hand in), "Ja kaut kas
> nestrādā".

## Why this topic exists

Every Programmēšana II game runs on one computer. Two higher-level results
are not covered at all:

- **2.3.1:** build and configure a multi-user local network with a protected
  access point, and run a simple server that can be reached from the
  internet.
- **3.1.2:** use cryptography in a concrete task.

Multiplayer is the natural place for both. The topic also makes students
learn Godot's networking API from the documentation (2.4.10), because that
API is too large to teach step by step.

**Place in the course:** after topic 8 (publishing). The student
has a finished, exported game and now makes it multiplayer. It comes before
topic 10, so the team project can choose to be networked.

**Prerequisites:** topics 1–8. 9.5 stores the online leaderboard in the
topic 6 database.

## Results covered (MK Nr. 416, 7. pielikums, augstākais līmenis)

| Kods | Sasniedzamais rezultāts | Stundas |
|---|---|---|
| 2.3.1. | Izveido un konfigurē atvērtu vai aizsargātu daudzlietotāju lokālu tīklu, t. sk. veidojot atvērtus vai aizsargātus bezvadu piekļuves punktus. Izveido vienkāršu serveri un konfigurē piekļuvi tam no interneta. | 9.1, 9.5, 9.6 |
| 3.1.2. | Izmanto kriptogrāfijas metodes konkrētā uzdevuma risinājumā. | 9.4, 9.6 |
| 2.4.10. | Izmanto programmēšanas valodas un tās bibliotēku dokumentāciju un palīdzības sistēmu, lai patstāvīgi apgūtu citas to piedāvātās iespējas, kas nepieciešamas konkrētās programmatūras izstrādei. | 9.2, 9.3 |

Cite them in `.lesson-meta` in the current format, linking to
`/sasnRez#prog2-a-…`.

## Tools

- Godot high-level multiplayer: `ENetMultiplayerPeer`, `[Rpc]` in C#,
  `MultiplayerSpawner` and `MultiplayerSynchronizer`.
- A protected Wi-Fi access point: Windows "Mobile hotspot" (WPA2) on one
  computer, or a spare router (see the open questions). Not the school
  network.
- `System.Security.Cryptography` (SHA-256, HMAC, PBKDF2, AES), which is
  part of .NET with nothing to install.
- An ASP.NET Core minimal API (`dotnet new web`) for the score server, and a
  tunnel or free host to reach it from the internet (see the open
  questions).

## Lessons

The game is a small 2D arena for 2–4 players, based on the topic 4 shooter
or a given starter. Repository: `Arena-Online` with `Game/` (Godot) and
`Server/` (ASP.NET Core).

### 9.1 Lokālais tīkls un aizsargāts piekļuves punkts

- **File:** `prog2_91.html`
- **Goal:** Izveido aizsargātu bezvadu tīklu klases grupai, pieslēdz tam
  divus datorus un pārbaudi, ka tie redz viens otru noteiktā portā.
- **SR:** 2.3.1.
- **Theory:** LAN, IP addresses, subnet and gateway. TCP vs UDP, and ports.
  Why games use UDP (ENet). Open vs WPA2/WPA3 networks: who can join and
  who can read the traffic. The Windows firewall and inbound rules.
- **Task 1:** turn on Windows Mobile hotspot with WPA2 and a strong
  password. Connect a second computer and record both IP addresses
  (`ipconfig`).
- **Task 2:** a two-line Godot test: one computer listens on UDP port
  `7777` (`PacketPeerUdp`) and the other sends "sveiki". Add a firewall
  rule when the packet is blocked.
- **Task 3:** compare the same test on an open hotspot. In the README, list
  who could join each network, and what someone on an open network could
  see.

### 9.2 Pirmais savienojums: serveris un klienti

- **File:** `prog2_92.html`
- **Goal:** Uzbūvē izvēlni "Izveidot spēli / Pievienoties", kurā viens
  dators kļūst par serveri un līdz trim citiem pievienojas pēc IP adreses.
- **SR:** 2.4.10.
- **Theory:** client–server vs peer-to-peer, and the authoritative server.
  `ENetMultiplayerPeer.CreateServer` / `CreateClient`, peer IDs, the
  `PeerConnected` / `PeerDisconnected` signals. The lesson explains these
  and links the Godot "High-level multiplayer" docs page for everything
  else.
- **Task 1:** host and join buttons. Print the peer IDs on both sides.
- **Task 2:** using the documentation, add a `MultiplayerSpawner` so each
  joining player gets their own character.
- **Task 3:** disconnect a client, then stop the server. Handle both
  signals so the game returns to the menu with a message instead of
  freezing.

### 9.3 Sinhronizācija un RPC

- **File:** `prog2_93.html`
- **Goal:** Panāc, ka visi spēlētāji redz vienu un to pašu spēli: kustību,
  šāvienus un punktus, un ka klients nevar sev pats piešķirt punktus.
- **SR:** 2.4.10.
- **Theory:** multiplayer authority. `MultiplayerSynchronizer` for
  position. `[Rpc]` modes (`AnyPeer`, `Authority`, `CallLocal`, reliable or
  unreliable). Why score changes only happen on the server.
- **Task 1:** synchronise the position of each player's character.
- **Task 2:** shooting as an RPC to the server, which spawns the bullet and
  decides hits. Score updates go from the server to everyone.
- **Task 3:** try to cheat: call the score RPC from a client. Show that the
  server ignores it (check `GetRemoteSenderId()`).

### 9.4 Kriptogrāfija spēlē: paroles, paraksti un šifrēšana

- **File:** `prog2_94.html`
- **Goal:** Izmanto kriptogrāfiju trīs uzdevumos: drošai paroles glabāšanai,
  rezultāta parakstīšanai pret viltošanu un saglabājuma faila šifrēšanai.
- **SR:** 3.1.2.
- **Theory:** hashing vs encryption vs signing. Salt and slow hashing
  (PBKDF2), and why plain SHA-256 is not enough for passwords. HMAC and a
  shared secret. AES with a key and an IV. Where keys must never be (in the
  repository, in the client). Godot ENet with DTLS, mentioned as encryption
  of the connection itself.
- **Task 1:** `PasswordHasher.cs` with `Rfc2898DeriveBytes.Pbkdf2` and a
  random salt. Verify a right and a wrong password.
- **Task 2:** `ScoreSigner.cs` builds an HMAC-SHA256 of
  `player|score|time`. The server checks it. Change one digit and show that
  the check fails.
- **Task 3:** encrypt the topic 5 save file with AES and decrypt it. Then
  open the file in a text editor and change one byte. What happens, and why
  should the save also be signed?
- **Ja kaut kas nestrādā:** `CryptographicException` from a wrong key or IV
  length, and Base64 strings copied with spaces.

### 9.5 Vienkāršs serveris, pieejams no interneta

- **File:** `prog2_95.html`
- **Goal:** Izveido rekordu serveri ar ASP.NET Core, padari to sasniedzamu no
  interneta un nosūti tam parakstītu rezultātu no Godot spēles.
- **SR:** 2.3.1.
- **Theory:** what a server is (a program listening on a port). HTTP
  methods and JSON. `localhost` vs LAN address vs public address. NAT and
  why a home or school computer cannot be reached from outside. Port
  forwarding vs tunnel vs hosting, and the risks of opening a port.
- **Task 1:** `dotnet new web` with `POST /scores` and `GET /scores/top`.
  Store the scores in the topic 6 database, or in JSON. Test them with the
  `.http` file in VS Code.
- **Task 2:** make it reachable: first from the LAN (bind to `0.0.0.0` and
  a firewall rule), then from the internet with the chosen method. Check
  from a phone on mobile data.
- **Task 3:** the server accepts only scores with a valid HMAC (9.4).
  `HttpRequest` from Godot sends a signed score. Send a forged one and
  show `401`.

### 9.6 Noslēguma projekts: Tiešsaistes arēna

- **File:** `prog2_96.html`
- **Goal:** Pabeidz daudzspēlētāju arēnu LAN tīklā ar rekordiem
  tiešsaistes serverī un dokumentē tīkla uzbūvi un drošības risinājumus.
- **SR:** 2.3.1., 3.1.2.
- **Step 1:** a full match for 2–4 players on the protected hotspot: lobby,
  round timer, scores, and a winner screen.
- **Step 2:** at the end of the match, the host signs and sends every score
  to the online server, and the game shows the online top 10.
- **Step 3:** README: a network diagram (devices, addresses, ports,
  hotspot security), what is hashed, signed and encrypted and why, where the
  secret key is kept, and two remaining risks.
- **Assessment (SLA):** the LAN game runs on separate computers; the server
  is authoritative for scores; cryptography is used correctly (salt,
  HMAC check, no keys in Git); and the server is reachable from outside
  the school network during the demo.

## Open questions for the author

1. **Access point.** Windows Mobile hotspot needs a Wi-Fi adapter and may be
   disabled by the school's policy. The alternative is one spare router per
   room, kept off the school network.
2. **Reaching the server from the internet.** Options: (a) a quick tunnel
   (for example `cloudflared tunnel --url http://localhost:5000`, no
   account needed), (b) a free hosting tier, (c) port forwarding on a spare
   router. (a) is simplest. Check the school's filters, and agree a rule
   that the tunnel is closed after the lesson.
3. **ENet over a tunnel.** HTTP tunnels do not carry ENet's UDP traffic, so
   the game itself stays LAN-only, and only the score server goes online.
   Is that enough for the demo?
