# 9. tēma — Izstrādes modeļi, dizains un IT profesijas (plāns)

> **Status:** plan only. No lesson pages exist yet. Write the lessons with
> `plan.md` section 4 (the task standard) and decisions D1–D8, F1–F4.

## Why this topic exists

Programmēšana I must cover all general-level results of the technology
domain, and many of them are about the design process. The course so far
builds software but never:

- names the software life cycle or development models;
- looks at the people and professions in the industry (course goal 1);
- compares existing solutions;
- teaches information design or editing images, audio and video;
- builds a prototype in variants and improves it over several rounds of
  testing.

This topic covers the optimal-level 2.4.2 and eight general-level results.

**Place in the course:** right before topic 10. Topic 10 plans a
project (problem, requirements, design, tests). With 9.1 first, the student
already knows which development model that plan follows, and topic 10's
roadmap (10.5) can name it.

**Prerequisites:** topics 1–8. 9.4 works on a given HTML page, because the
student has not built a web page in this course yet (that starts in topic 11).

## Results covered (MK Nr. 416, 7. pielikums)

| Kods | Līmenis | Sasniedzamais rezultāts | Stundas |
|---|---|---|---|
| 2.4.2. | optimālais | Nosauc un raksturo ar piemēriem dažus programmatūras izstrādes modeļus, t. sk. ūdenskrituma, V-modeli, pakāpeniskās un interaktīvās. | 9.1, 9.6 |
| 2.4.2. | vispārīgais | Nosauc un raksturo ar piemēriem programmatūras dzīves cikla galvenos posmus – specificēšana, projektēšana, izstrāde, testēšana, uzturēšana. | 9.1 |
| 1.1.1. | vispārīgais | Salīdzina līdzīgus risinājumus un raksturo tajos izmantotos materiālus, tehnoloģiskos procesus, to priekšrocības un trūkumus, nosaka, kādi dizaina procesa soļi un darbības veiktas, lai tos radītu. | 9.3 |
| 1.1.2. | vispārīgais | Pēta un izvērtē dizaina izstrādes procesā iesaistīto darbinieku (dizainera, ražošanas vadītāja, programmētāja, projektu vadītāja, materiālzinātnieka u. c.) lomu risinājumu izstrādes procesā. Reflektē par savām prasmēm un profesionālajām interesēm attiecīgajā nozarē. | 9.2 |
| 1.3.1. | vispārīgais | Plānojot risinājumu, veido tā modeļus un variantus, lai veiktu nepieciešamās izmaiņas un uzlabojumus gala risinājuma idejā. | 9.6 |
| 1.3.2. | vispārīgais | Testē un lieto iterācijās radītos risinājumus, analizē iegūtos datus un formulē pamatotus ierosinājumus, lai pilnveidotu risinājuma izstrādes darba plānu. | 9.6 |
| 2.2.1. | vispārīgais | Atpazīst un analizē informācijas dizaina pamatprincipu izmantošanu daudzveidīgos piemēros. | 9.4 |
| 2.2.2. | vispārīgais | Salīdzina dažādos medijos izmantotos informācijas dizaina risinājumus, analizē konkrēto piemēru priekšrocības un trūkumus. | 9.4 |
| 2.2.3. | vispārīgais | Veido un apstrādā digitālus attēlus, audio un videodatnes, lietojot dažādas lietotnes atbilstoši dotajam uzdevumam. | 9.5, 9.6 |

When the lessons are written, cite these in `.lesson-meta` in the current
format: short label, the law's text in `title`, and a link to
`/sasnRez#prog1-o-…` or `/sasnRez#prog1-v-…`.

## Tools (Windows)

- Python with `Pillow` (pip) for 9.5.
- Windows built-ins: Photos, Clipchamp (video), Sound Recorder.
  Audacity (free) for audio editing.
- Paper prototypes photographed with a phone, or a free online wireframe
  tool (see open questions).

## Lessons

All student files go in `tema09/` in the `programmesana-pamatkurss`
repository. Notes go in `README.md` under `### 16.x …` (D3). Imported files
have the lesson number last (D2). Large media files stay small: images under
1 MB, and video is linked, not committed (see 9.5).

### 9.1 Programmatūras dzīves cikls un izstrādes modeļi

- **File:** `prog1_91.html`
- **Goal:** Šajā stundā tu sakārtosi izstrādes darbus pa dzīves cikla
  posmiem un uzrakstīsi programmu, kas projektam iesaka piemērotāko izstrādes
  modeli.
- **SR:** 2.4.2. (vispārīgais), 2.4.2. (optimālais)
- **Theory:** the five stages (specification, design, development, testing,
  maintenance), with an example of each from the student's own earlier
  projects. Waterfall, V-model (each stage paired with its test level),
  incremental and iterative development. When each fits: fixed vs changing
  requirements, risk, and how early the user sees something.
- **Task 1 (try):** sort 12 given activities ("uzraksti lietotāja stāstu",
  "izlabo kļūdu pēc laidiena", …) into the five stages in the README.
- **Task 2 (build):** `modeli_91.py` has a dictionary of four models with
  their traits. A function `ieteikt(prasibas_mainas, risks, termins)`
  returns the best match and the reason.
- **Task 3 (test):** run it for three given project descriptions and for
  your own topic 10 project. Find one input where the answer is
  questionable, and explain it in the README.
- **Notebook:** which model the course's own topic projects have followed
  so far, and how you can tell.

### 9.2 Lomas izstrādes komandā un IT profesijas

- **File:** `prog1_92.html`
- **Goal:** Šajā stundā tu izpētīsi, kas strādā pie programmatūras
  izveides, savāksi īstus darba sludinājumus un ar programmu atradīsi,
  kuras prasmes prasa visbiežāk.
- **SR:** 1.1.2. (vispārīgais)
- **Theory:** roles in a team: product owner or project manager, designer
  (UX/UI), developer (front-end, back-end), tester, DevOps, data analyst,
  and security specialist. Who does what in each life-cycle stage, linked
  to 9.1. Trends in the industry (course goal 1).
- **Task 1 (try):** match roles to the stages of a given project in a table.
- **Task 2 (build):** collect five Latvian job adverts by hand into
  `sludinajumi_92.csv` (role, skills separated by `;`). `prasmes_92.py`
  counts the skills and prints the top 10.
- **Task 3 (test):** the same skill spelled differently ("Python", "python",
  "Python 3"). Normalise the names and check that the counts change as
  expected.
- **Notebook:** which role interests you, which of its top skills you
  already have from this course, and which you would learn next.

### 9.3 Līdzīgu risinājumu salīdzināšana

- **File:** `prog1_93.html`
- **Goal:** Šajā stundā tu salīdzināsi trīs līdzīgas lietotnes pēc saviem
  kritērijiem un uzrakstīsi programmu, kas aprēķina, kura ir labākā tavam
  lietotājam.
- **SR:** 1.1.1. (vispārīgais)
- **Theory:** comparing solutions by function, technology (web or native,
  offline, platform), cost and business model, accessibility and privacy.
  Working backwards: which design steps (research, prototype, testing) the
  makers probably took.
- **Task 1 (try):** pick three similar apps (for example three to-do apps or
  three typing trainers). Fill in a comparison table in the README.
- **Task 2 (build):** `salidzinat_93.py` holds the criteria with weights and
  scores 1–5 for each app, and prints a weighted ranking.
- **Task 3 (test):** change one weight and see if the winner changes. Add a
  check that the weights add up to 1 and every score is 1–5.
- **Notebook:** advantages and disadvantages of each app, and two design
  steps its makers must have done, with the evidence.

### 9.4 Informācijas dizains: hierarhija, kontrasts un medijs

- **File:** `prog1_94.html`
- **Goal:** Šajā stundā tu atpazīsi informācijas dizaina principus dažādos
  piemēros, salīdzināsi vienu ziņu plakātā, tīmekļa lapā un lietotnē un
  ar programmu pārbaudīsi krāsu kontrastu.
- **SR:** 2.2.1., 2.2.2. (vispārīgais)
- **Theory:** hierarchy, contrast, alignment, proximity and repetition.
  Colour and readability, typography, icons. How the same information
  changes between a poster, a web page, a phone app and an infographic.
- **Task 1 (try):** annotate three given examples (a timetable, a weather
  app and a game HUD). Name the principle used or broken in each.
- **Task 2 (build):** `kontrasts_94.py` computes the WCAG contrast ratio of
  two hex colours (relative luminance formula) and says whether the text
  passes AA.
- **Task 3 (test):** check the colours of the given page. Fix the pairs that fail, and test the function with
  black/white (21:1) and the same colour twice (1:1).
- **Notebook:** one message shown in two media, with the advantages and
  disadvantages of each.

### 9.5 Attēli, skaņa un video lietotnei

- **File:** `prog1_95.html`
- **Goal:** Šajā stundā tu sagatavosi attēlus ar Python programmu, apstrādāsi
  skaņu un samontēsi īsu video, kas parāda tavu lietotni.
- **SR:** 2.2.3. (vispārīgais)
- **Theory:** raster vs vector, resolution and file size, PNG/JPG/WebP,
  sample rate and normalising audio, video resolution and length for the
  web. Licences of media you did not make (link to 11.2).
- **Task 1 (try):** open an image with Pillow and print its size and mode.
  Make a thumbnail.
- **Task 2 (build):** `atteli_95.py` resizes every image in a folder to a
  maximum width, adds a small text watermark and saves WebP copies. It
  prints the size before and after.
- **Task 3 (test):** a folder with a non-image file and a very small image.
  The program skips and reports them. Then record and trim a 10-second
  voice-over in Audacity, and make a 30–60 s screen video in Clipchamp. Put
  a link to the video in the README; don't commit it.
- **Watch out:** video files must not go into Git. Add `*.mp4` to
  `.gitignore` (1.4) as a step.

### 9.6 Noslēguma projekts: Prototips iterācijās

- **File:** `prog1_96.html`
- **Goal:** Šajā projektā tu izveidosi divus savas lietotnes ideju prototipu
  variantus, pārbaudīsi tos ar lietotājiem divās iterācijās un pamatosi,
  kāpēc tavs darba plāns mainījās.
- **SR:** 1.3.1., 1.3.2., 2.2.3. (vispārīgais), 2.4.2. (optimālais)
- **Step 1:** choose a development model (9.1) and give a reason. Make two
  variants of the main screen (paper or wireframe tool), photographed or
  exported, with the images prepared by `atteli_95.py`.
- **Step 2:** iteration 1. Three users each do the same two tasks on both
  variants. Record the time and the problems in `tests_96.csv`.
  `analize_96.py` prints the averages and the most common problems.
- **Step 3:** improve the chosen variant, run iteration 2 the same way and
  compare the numbers. Update the work plan in the README and make a 60 s
  video presenting the result.
- **Assessment (SLA):** there are two real variants, not one; the test data
  is collected and analysed by the program; the changes come from the data;
  the plan update gives reasons; and the chosen model fits how the work
  actually went.

## Open questions for the author

1. **Wireframe tool.** Paper plus a phone photo works everywhere. A free
   online tool (for example Figma's education plan or Penpot) is nicer but
   needs accounts. Which one?
2. **Job adverts in 9.2.** Collecting them by hand avoids scraping
   questions. Is a fixed set of 20 adverts in a given CSV better for weaker
   groups?
