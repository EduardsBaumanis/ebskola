# 12. tēma — Mākslīgais intelekts un atvērtie dati (plāns)

> **Status:** plan only. No lesson pages exist yet. Write the lessons with
> `plan.md` section 4 (the task standard) and decisions D1–D8, F1–F4.

## Why this topic exists

Three optimal-level results of Programmēšana I have no lesson at all:

- **2.4.18:** machine learning. The old sasnRez.html used this code for
  OOP by mistake.
- **2.3.3:** independently finding and using public learning materials,
  datasets and sources.
- **3.2.5:** how scientific research drives technology.

Machine learning ties all three together. A model needs a public dataset
(2.3.3), and today's ML tools come straight out of research papers (3.2.5).

**Place in the course:** right after topic 11. It needs pip and a virtual
environment (11.1), reading library documentation (11.2) and Streamlit
(11.3–11.5) for the project. Topic 8 (algorithms, comparing solutions by
measurement) also comes before it.

**Prerequisites:** topics 1–11, in particular lists and dictionaries
(topic 5), CSV files (topic 6), functions and modules (topic 4), and pip and
Streamlit (topic 11).

## Results covered (MK Nr. 416, 7. pielikums)

| Kods | Līmenis | Sasniedzamais rezultāts | Stundas |
|---|---|---|---|
| 2.4.18. | optimālais | Nosauc vismaz vienu lietotni, kurā tiek izmantota mašīnmācīšanās, raksturo ar piemēriem ieguvumus, kurus sniedz mašīnmācīšanās algoritmu izmantošana tajās. | 12.1, 12.3, 12.4, 12.6 |
| 2.3.3. | optimālais | Patstāvīgi meklē un izmanto publiski pieejamus digitālus mācību materiālus un krātuves, datus un informācijas avotus savu zināšanu papildināšanai un risinājumu izstrādei. | 12.2, 12.6 |
| 3.2.5. | optimālais | Ilustrē ar piemēriem un analizē, kā zinātniskie pētījumi ietekmē sasniegumus dažādās dzīves jomās un tehnoloģiju attīstību, lieto iegūto informāciju sava risinājuma koncepcijas izstrādē. | 12.5, 12.6 |

The lessons also revisit the general-level 3.1.5 (licences and personal
data), when choosing a dataset and in the project README.

When the lessons are written, cite these in `.lesson-meta` in the current
format: short label, the law's text in `title`, and a link to
`/sasnRez#prog1-o-…`.

## Tools (Windows)

- Python venv from 11.1 with `scikit-learn`, `pandas` and `joblib` (pip).
  Check that the install works on a school computer before the first lesson:
  the wheels are large.
- A browser tool for training without code, for 12.1 (see open questions).
- Public data sources: data.gov.lv (Latvian open data portal), the CSP
  (Central Statistical Bureau) database, the UCI Machine Learning Repository,
  and the datasets built into scikit-learn.

## Lessons

All student files go in `tema12/` in the `programmesana-pamatkurss`
repository. Notes go in `README.md` under `### 15.x …` (D3). Imported files
have the lesson number last (D2).

### 12.1 Kur slēpjas mašīnmācīšanās?

- **File:** `prog1_121.html`
- **Goal:** Šajā stundā tu atradīsi mašīnmācīšanos lietotnēs, ko lieto katru
  dienu, un salīdzināsi programmu ar paša rakstītiem noteikumiem ar
  programmu, kas noteikumus "iemācās" no piemēriem.
- **SR:** 2.4.18. (optimālais)
- **Theory:** rules written by a person vs rules learned from data.
  Examples: spam filter, photo search, face unlock, recommendations,
  translation, chat assistants. What each one gains from ML, and what it
  costs: data, errors, energy.
- **Task 1 (try):** train an image model in the browser with no code (three
  classes, for example rock, paper and scissors with your hand). Test it and
  write down where it fails.
- **Task 2 (build):** `spams_121.py` is a rule-based spam check: a list of
  keywords and a score. Run it on 10 given messages.
- **Task 3 (test):** find two messages the rules get wrong and add a rule
  for each. Then find one that breaks the new rule. Write in the README why
  learning from examples scales better than adding rules.
- **Notebook:** three apps you use, what in each is learned from data, and
  what the benefit is.

### 12.2 Atvērtie dati: atrodi, pārbaudi un ielādē

- **File:** `prog1_122.html`
- **Goal:** Šajā stundā tu pats atradīsi publisku datu kopu, pārbaudīsi tās
  avotu un licenci un ielādēsi to Python programmā.
- **SR:** 2.3.3. (optimālais)
- **Theory:** what open data is. Where to search (data.gov.lv, CSP, UCI,
  Kaggle). How to judge a source: who published it, when it was updated,
  the licence (CC BY, CC0), the columns and units, and whether it contains
  personal data.
- **Task 1 (try):** load a built-in scikit-learn dataset (for example
  `load_iris`) into a `pandas` table. Use `head()`, `describe()` and
  `value_counts()`.
- **Task 2 (build):** find a CSV on data.gov.lv or CSP that answers a
  question you choose. Save it as `dati_122.csv` and write `ielade_122.py`,
  which loads and cleans it (column names, missing values, numbers stored as
  text).
- **Task 3 (test):** break the file on purpose (a missing column, a comma as
  the decimal separator, a different encoding) and make the loader report
  each problem clearly.
- **Notebook:** a "data card": source, link, date, licence, columns, and
  what it can and cannot answer.
- **Watch out:** many Latvian CSV files use `;` as the separator and `,` as
  the decimal mark. Show `sep=";"` and `decimal=","` in the worked example.

### 12.3 Pirmais modelis: klasifikācija ar scikit-learn

- **File:** `prog1_123.html`
- **Goal:** Šajā stundā tu apmācīsi lēmumu koku, kas pēc mērījumiem atpazīst
  klasi, un pārbaudīsi to ar datiem, ko modelis nav redzējis.
- **SR:** 2.4.18. (optimālais)
- **Theory:** features and labels, training and test data, `fit` and
  `predict`. A decision tree as a set of `if` rules the computer found
  itself, linked to topic 3. Reading the scikit-learn documentation (11.2).
- **Task 1 (try):** split the iris data with `train_test_split`, train a
  `DecisionTreeClassifier`, and predict for three rows.
- **Task 2 (build):** `modelis_123.py` with functions `apmacit(dati)` and
  `prognozet(modelis, vertibas)`. Save the model with `joblib.dump`.
- **Task 3 (test):** print the tree with `export_text` and check one
  prediction by hand against the printed rules. Enter impossible values
  (negative lengths) and add validation before `predict`.

### 12.4 Cik labs ir modelis? Precizitāte, kļūdas un godīgums

- **File:** `prog1_124.html`
- **Goal:** Šajā stundā tu izmērīsi, cik bieži modelis kļūdās, atradīsi, kur
  tieši, un izvērtēsi, kam šīs kļūdas var kaitēt.
- **SR:** 2.4.18. (optimālais)
- **Theory:** accuracy and the confusion matrix. Overfitting: a deep tree
  that is perfect on training data and worse on test data. Bias from
  unbalanced data. Personal data and consent.
- **Task 1 (try):** `accuracy_score` and `confusion_matrix` for the 12.3
  model.
- **Task 2 (build):** `salidzinat_124.py` trains trees with `max_depth` 1–10
  and prints the train and test accuracy in a table. Choose a depth and
  explain why.
- **Task 3 (test):** remove most examples of one class from the training
  data, retrain, and show how the errors for that class grow.
- **Notebook:** one real case where a biased model harmed people (from a
  source you found and cite), and what would have prevented it.

### 12.5 Pētījumi, kas mainīja tehnoloģijas

- **File:** `prog1_125.html`
- **Goal:** Šajā stundā tu izsekosi, kā vairāki zinātniski pētījumi noveda
  līdz lietotnēm, ko lieto šodien, un izmantosi vienu pētījumu sava projekta
  idejā.
- **SR:** 3.2.5. (optimālais)
- **Theory:** from research to product. Examples: the perceptron (1958),
  backpropagation (1986), ImageNet and deep networks (2012), the transformer
  (2017), and today's chat assistants. Also non-ML research: public-key
  cryptography, which makes HTTPS possible. How to read a paper's abstract
  and how to tell research from marketing.
- **Task 1 (try):** `laika_skala_125.json` with given milestones (year,
  research, result in technology). `125.py` prints them sorted by year.
- **Task 2 (build):** add three milestones you researched yourself, each
  with a source link. Add a function that prints only the milestones for one
  area of life (medicine, transport, communication).
- **Task 3 (test):** a milestone with a missing year or source. The program
  reports it instead of crashing. Check each of your sources: is it the
  research itself, or a news article about it?
- **Notebook:** one research result and how it will shape the 12.6 project
  idea.

### 12.6 Noslēguma projekts: MI palīgs pārlūkā

- **File:** `prog1_126.html`
- **Goal:** Šajā projektā tu apmācīsi modeli ar paša atrastiem atvērtajiem
  datiem un izveidosi Streamlit lietotni, kurā cits cilvēks var ievadīt
  vērtības un saņemt modeļa prognozi.
- **SR:** 2.4.18., 2.3.3., 3.2.5. (all optimālais)
- **Step 1:** choose a question and a public dataset with a data card
  (12.2). Train and evaluate the model, and save it with `joblib`.
- **Step 2:** `lietotne_126.py` (Streamlit) loads the saved model, takes
  input with validation, and shows the prediction and how sure the model is
  (`predict_proba`).
- **Step 3:** a README with the data source and licence, the test accuracy,
  known weaknesses, and the research the idea builds on (12.5). Then a
  two-minute demo.
- **Assessment (SLA):** the data source is found independently, cited and
  licensed for use; the model is evaluated on test data; the app handles bad
  input; and the README is honest about where the model fails.

## Open questions for the author

1. **No-code tool for 12.1.** Google Teachable Machine runs in the browser
   and needs a webcam. If webcams are not allowed, use the sound or pose
   models, or replace task 1 with a given set of images.
2. **Package size.** `scikit-learn` plus `pandas` is a big install. Check
   that pip works through the school proxy, or pre-install them.
3. **Chat assistants.** Should 12.1 or 12.4 also cover using AI coding
   assistants responsibly in this course? That would touch course goal 7
   (intellectual property, safe use).
