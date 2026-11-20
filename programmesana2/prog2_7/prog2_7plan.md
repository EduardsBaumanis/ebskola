# 7. tēma — Mašīnmācīšanās spēlēs: pretinieks, kas mācās (plāns)

> **Status:** plan only. No lesson pages exist yet. Write the lessons in the
> Programmēšana II format: Teorija, three tasks, "Ko sagatavo" (what goes in
> the GitHub repository and `README.md`, and how to hand in), "Ja kaut kas
> nestrādā".

## Why this topic exists

Topic 4 calls its state machine and A* pathfinding "AI", but neither one
learns from data. MK Nr. 416 requires the higher-level 2.4.18:

- compare machine-learning algorithms, including image recognition;
- use an ML library in the student's own program.

No Programmēšana II lesson does this. The topic also asks students to learn
an unfamiliar library from its documentation (2.4.10), which the course has
not required so far.

**Place in the course:** after topic 6 (databases) and before topic 8 (UI
and publishing). Topic 4's game AI is the starting point, and topics 5 and
6 give the skills to collect and store training data. The
learning opponent can then be part of the game published in topic 8.

**Prerequisites:** topics 1–5. Topic 6 is helpful for storing the data.
Programmēšana I topic 12 (scikit-learn) covers the same ideas in Python,
so this topic can go faster for students who did it.

## Results covered (MK Nr. 416, 7. pielikums, augstākais līmenis)

| Kods | Sasniedzamais rezultāts | Stundas |
|---|---|---|
| 2.4.18. | Salīdzina mašīnmācīšanās algoritmus (t. sk. attēlu atpazīšanai) un raksturo to izmantošanas iespējas jaunas programmatūras izstrādē. Izmanto bibliotēku, kurā realizēti mašīnmācīšanās algoritmi, izstrādājot programmatūru mācību uzdevuma realizācijai. | 7.1, 7.3–7.6 |
| 2.4.10. | Izmanto programmēšanas valodas un tās bibliotēku dokumentāciju un palīdzības sistēmu, lai patstāvīgi apgūtu citas to piedāvātās iespējas, kas nepieciešamas konkrētās programmatūras izstrādei. | 7.3, 7.5 |
| 2.4.11. | Meklē un pievieno atvērtā koda bibliotēkas un lieto API (programmsaskarni) specializētu funkciju veikšanai sava programmēšanas projekta īstenošanai. | 7.3, 7.5 |
| 2.4.14. | Izmanto dažādas datu struktūras (t. sk. masīvi, kopas, ieraksti, steks, rinda, saraksts, koks, grafs, datne) un ar tiem saistītos pamatalgoritmus. | 7.2 |

2.4.18 and 2.4.10 are the gaps. The other two are already covered elsewhere,
and this topic gives more practice. Cite them in `.lesson-meta` in the
current format, linking to `/sasnRez#prog2-a-…`.

## Tools

- ML.NET (`Microsoft.ML`, MIT licence) in a separate .NET console project
  for training (`dotnet new console`), so the large training packages stay
  out of the Godot project.
- Prediction inside Godot: either `Microsoft.ML` with the saved `model.zip`,
  or a model exported to ONNX and run with `Microsoft.ML.OnnxRuntime`. See
  the open questions.
- For image recognition (7.5): a small pre-trained ONNX image classifier,
  or ML.NET image classification (transfer learning) on a given image set.

## Lessons

Two projects in one repository: `Trenins/` (console, training) and
`Arena/` (Godot .NET game). Training data goes in `Trenins/data/`, and saved
models in `Arena/Models/`.

### 7.1 Noteikumi vai mācīšanās? ML spēlēs

- **File:** `prog2_71.html`
- **Goal:** Salīdzini topic 4 stāvokļu mašīnu ar pretinieku, kas izvēlas
  gājienu pēc spēlētāja iepriekšējiem gājieniem, un nosauc, kur spēļu
  industrijā lieto mašīnmācīšanos.
- **SR:** 2.4.18.
- **Theory:** hand-written rules vs learned models. Supervised learning
  (classification, regression), unsupervised learning and reinforcement
  learning. Uses in games: opponents and difficulty adjustment, cheat
  detection, recommendation, upscaling, image and voice recognition. The
  costs: data, training time, errors you cannot read.
- **Task 1:** play rock-paper-scissors in a given Godot scene against a
  random opponent, then against a frequency-counting opponent
  (`Dictionary<Move,int>`). Record 30 rounds each.
- **Task 2:** write `PatternOpponent.cs`, which predicts the next move from
  the last two moves (a lookup table). Compare its win rate with the other
  two.
- **Task 3:** play as unpredictably as you can, and show where the pattern
  opponent fails. In the README, explain why a model trained on many
  players could do better, and what it would need.

### 7.2 Treniņa dati no spēles

- **File:** `prog2_72.html`
- **Goal:** Pievieno spēlei telemetriju, kas katru spēlētāja lēmumu ieraksta
  CSV failā ar pazīmēm un iznākumu, un sagatavo datu kopu apmācībai.
- **SR:** 2.4.14.
- **Theory:** features and labels. Choosing features the game actually
  knows at the moment of the decision. Train and test split. Class balance.
  Players' consent and anonymous data.
- **Task 1:** in the topic 4 shooter (or a given arena), log `(distance,
  enemyHp, playerHp, ammo, action)` to `user://telemetry.csv` at each
  decision.
- **Task 2:** a `DataCleaner` console tool that drops broken rows, counts
  each class and writes `train.csv` and `test.csv` (80/20, fixed seed).
- **Task 3:** remove one class almost completely and see how the counts
  change. Write in the README what that would do to a model.

### 7.3 Pirmais modelis ar ML.NET

- **File:** `prog2_73.html`
- **Goal:** Apmāci klasifikatoru, kas pēc spēles stāvokļa prognozē
  spēlētāja nākamo darbību, un pārbaudi to ar testa datiem.
- **SR:** 2.4.18., 2.4.10., 2.4.11.
- **Theory:** `MLContext`, `IDataView`, the pipeline (`MapValueToKey`,
  `Concatenate`, trainer, `MapKeyToValue`), `Fit`, `Transform`,
  `Evaluate`, and saving with `mlContext.Model.Save`. How to find all of
  this in the ML.NET documentation and samples: the lesson gives only the
  first step and links to the docs page for the rest.
- **Task 1:** `dotnet new console` in `Trenins/`, add `Microsoft.ML`, and
  load `train.csv` into an `IDataView` with a `[LoadColumn]` class.
- **Task 2:** train `SdcaMaximumEntropy`, print `MacroAccuracy` and
  `LogLoss` on the test set, and save `model.zip`.
- **Task 3:** using only the documentation, add the confusion matrix
  printout (`ConfusionMatrix.GetFormattedConfusionTable()`). Say which
  action the model mixes up most.

### 7.4 Algoritmu salīdzināšana

- **File:** `prog2_74.html`
- **Goal:** Apmāci to pašu uzdevumu ar trim dažādiem algoritmiem un pamato,
  kuru izmantot spēlē, ņemot vērā precizitāti, ātrumu un modeļa izmēru.
- **SR:** 2.4.18.
- **Theory:** linear models, decision trees and boosted trees (FastTree,
  LightGBM), and neural networks (short). Overfitting: comparing train and
  test scores. Prediction speed matters at 60 frames per second.
- **Task 1:** train `SdcaMaximumEntropy`, `LightGbm` and
  `FastForest`/OVA on the same data.
- **Task 2:** a comparison table: accuracy, training time, time for 1000
  predictions (`Stopwatch`), and `model.zip` size.
- **Task 3:** shrink the training data to 10 % and repeat. Which algorithm
  suffers most? Choose one for the game, and give your reason in the README.

### 7.5 Attēlu atpazīšana

- **File:** `prog2_75.html`
- **Goal:** Izmanto gatavu attēlu klasifikācijas modeli, lai programma
  atpazītu zīmējumu vai ekrānuzņēmumu, un salīdzini to ar vienkāršu paša
  modeli.
- **SR:** 2.4.18., 2.4.10., 2.4.11.
- **Theory:** why images need different algorithms (convolutional networks,
  transfer learning). Pre-trained models and the ONNX format. Input size
  and normalisation, and reading class scores. Licence and training data of
  a downloaded model.
- **Task 1:** run a given small ONNX classifier on five images with
  `Microsoft.ML.OnnxRuntime`. Print the top three classes and their scores.
- **Task 2:** a drawing pad in Godot (`Image` from a `SubViewport`) that
  saves a 28×28 drawing. A digit or shape model classifies it.
- **Task 3:** compare it with a model you train with ML.NET image
  classification on a small given image set (or the 7.4 trainers on raw
  pixels). Record the accuracy and why they differ.

### 7.6 Noslēguma projekts: Pretinieks, kas mācās

- **File:** `prog2_76.html`
- **Goal:** Ieliec apmācītu modeli Godot spēlē: pretinieks prognozē
  spēlētāja nākamo darbību un pielāgo savu taktiku, un tu pierādi, ka tas
  spēlē labāk nekā noteikumu pretinieks.
- **SR:** 2.4.18.
- **Step 1:** load the chosen model in `Arena/` once (not every frame), and
  wrap it in `IOpponentBrain`, so the rule-based state machine and the ML
  brain can be swapped in the Inspector.
- **Step 2:** the enemy acts on the prediction (for example dodging where
  the player will shoot). Fall back to the state machine if the model file
  is missing.
- **Step 3:** run 20 matches against each brain. Record the results in a
  table, and write a README section with the data source, the chosen
  algorithm and why, the known weaknesses, and how player data is handled.
- **Assessment (SLA):** the model is trained on the student's own collected
  data; the algorithm choice is backed by the 7.4 comparison; prediction
  does not slow the frame rate (measured); and there is a working fallback.

## Open questions for the author

1. **ML.NET inside Godot.** `Microsoft.ML` should work in a Godot .NET
   desktop project, but it is large. ONNX Runtime is lighter for prediction
   only. Test both on a school computer and pick one before 7.3 is written.
2. **Image set for 7.5.** Use a given set (e.g. hand-drawn shapes made by
   the class) to avoid licence questions, or a public dataset with a clear
   licence?
