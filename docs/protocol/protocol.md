# PROTOCOL

Version 0.0.1
Author: Carl Ollvik Aasa

Supervisors: Sonja Aits, sonja.aits@med.lu.se; Johanna Berg, johanna@tech.se
Collaborator: Anton Werin

## Task

The task we want to solve is, given a sample medical chart from the emegancy room admission, written in Swedish, annotate each occurrence  of a symptom (SYM), finding (FND) and negation (NEG) with a tag according to the labels in respective parenthesises. The specifics for this annotation are concurrently to be developed and enforced as a whole before evaluation. Put simply it's a sequence-labeling task to classify each token according, as belonging to one or none annotation class.

This will be done both by a trained medical professional and by a suppervised learning algorithm. Comparing these two on a rather small set of example text we will develop and iteratively test a prototype annotation assitor for Swedish medical charts.


## Background

BERT AND/OR Dictionary (we don't know which is best for medical journals, union or intersection

## Frågeställningar

Vilka existerande datakällor kan användas för att träna NLP modeller för svenska medicinska texter? Kan NLP verktyg som är utvecklad för engelska texter anpassas till svensk medicinsk text? Hur bra fungerar dessa NLP verktyg i upptag av COVID19 symptomdata från fritext i jämförelse med manuell läsning (gold standard)? Vilka typer av symptom nämns i journaltexter av COVID19 patienter?
## Methods

### Data Collection

#### Corpus

https://www.socialstyrelsen.se/utveckla-verksamhet/e-halsa/klassificering-och-koder/kodtextfiler/



Insamling av stora mänger medicinska texter på svenska behövs för att träna en grundläggande språkmodell. Själva innehållet är mindre relevant så länge det kommer från medicinska områden eller närliggande teman. Inklusionskriterier är därför bara om texterna är på svenska, är tillgängliga och om dem kan utan större problem omvandlas till en maskinläsbart format. Olika källor kommer att utvärderas och om de uppfyller kriterierna kommer texterna att samlas in och formaterats till en standardiserad format: SVT hemsida, existerande samlingar i språkbanken(3), wikipedia samt journaltexter från akutvårdspatienter vid Skånes Universitetssjukhus under 2020, med mera.

#### Sources

#### Data Structuring - Annotation

Nyckelord och -fraser som beskriver symptom kommer att annoteras i en del av texterna i samlingen, med fokus på texter relaterade till COVID19, t.ex. nyhets- och journaltexter, vilket har tidigare gjorts på engelska.(4) Detta behövs för att träna ett NER modell samt för att utvärdera NER verktyg.



### SpaCy

> SpaCy is a NLP library which has gained a lot of attention and praise. F
>
> | LIBRARY | PIPELINE                                                     | WPS CPU | WPS GPU |
> | ------- | ------------------------------------------------------------ | ------- | ------- |
> | spaCy   | [`en_core_web_lg`](https://spacy.io/models/en#en_core_web_lg) | 10,014  | 14,954  |
> | spaCy   | [`en_core_web_trf`](https://spacy.io/models/en#en_core_web_trf) | 684     | 3,768   |
> | Stanza  | `en_ewt`                                                     | 878     | 2,180   |
> | Flair   | `pos`(`-fast`) & `ner`(`-fast`)                              | 323     | 1,184   |
> | UDPipe  | `english-ewt-ud-2.5`                                         | 1,101   | *n/a*   |
>
> source https://spacy.io/usage/facts-figures#benchmarks
>
> It’s syntactic parser is the fastest available, and **its accuracy is within 1% of the best available**.
>
> These are not just idle claims—there are facts and figures to back up them. Head over to the spaCy [benchmarks](https://spacy.io/usage/facts-figures#benchmarks) for more information.

- **It’s minimalistic and opinionated.** spaCy doesn’t bombard you with many options to choose from. It just provides one algorithm for each task. And that algorithm is often the best (and it constantly gets perfected and improved). So instead of choosing what algorithm to use, you can be productive and just get your work done.
- **It’s highly extensible.** With the bloom of machine learning (ML) and deep learning (DL), text data comes into play for many of its applications. spaCy can be used alongside other popular ML and DL libraries such as scikit-learn, TensorFlow, and more.
- **It supports several languages.** Currently spaCy supports: German, Spanish, Greek, French, Italian, Dutch, and Portuguese, apart from English. For a complete list, follow this [link](https://spacy.io/usage/models#languages).
- **It’s customizable**. You can add custom components or add your own implementation where needed with spaCy.

#### 3. Anpassa ett existerande engelsk NER verktyg för svenska texter

Värdgruppen har verktyg som kan matcha texter mot listor (s.k. dictionaries) av medicinska termer på engelska (https://github.com/Aitslab/BioNLP) . För att göra om verktyget till svenska texter behövs motsvarande dictionaries på svenska. Det kommer att undersökas om ett dictionary med symptomfraser och -ord kan byggas genom att extraherar fraser från ICD-10 eller Snomed-CT. Dessutom kommer gruppens existerande dictonaries(5) att utvärderas och utökas manuellt. 4. Träna ett svensk medicinsk NER modell för symptom: Som komplement till NER med dictionaries, ska ett symptom NER modell tränas med annoterade textsamlingar som skapas tidigare i projektet (2.). 5. Utvärdering av verktyg i jämförelse med manuell läsning: Det slutliga målet för projektet är att använda de utvecklade verktyg för att analysera COVID19 patientjournaler för att extrahera vilka symptom nämns och hur ofta. För detta ska journaler från patienter som kom till akuten på SUS Malmö och testades positv för COVID19 analyseras. Alla verktyg som utvecklas i projektet (3. och 4.) ska därför blir jämförda mot annoteringarna av patientjournaler som gjordes genom manuell läsning (2.).

### Data

### Data

As a base for the SpaCy model a transformer based model from *The National Library of Sweden / KB Lab* will be used. This model is a complete pipeline with UPOS tagger, parser, sentencer,  ner and lemmatizer.

Observere that it is not yet possible to train the lemmatizer in spaCy, meaning that the performance is only as good as the quality of the rules/lookup tables available for Swedish which are limited. KB lab recommends using [Stanza](https://stanfordnlp.github.io/stanza/), [efselab](https://github.com/robertostling/efselab/blob/master/README.md) or [lemmy](https://github.com/sorenlind/lemmy).

Performance Scores

XPOS tagger (accuracy): **97.96**
UPOS tagger (accuracy): **98.40**
Parser (UAS/LAS): **93.51**/**90.74**
Sentencer (F score): **94.73**
NER (F score): **90.06**



#### Model specifications from KB

The models where initialized with [FastText](https://fasttext.cc/docs/en/crawl-vectors.html) word embeddings.

We trained two separate tagger models for UPOS and XPOS, but the parser and NER are the same for both models.

##### UPOS tagger

The UPOS tagger was trained using two Swedish treebanks from Universal Dependencies, [UD_Swedish-Talbanken](https://universaldependencies.org/treebanks/sv_talbanken/index.html) and [UD_Swedish-LinES](https://universaldependencies.org/treebanks/sv_lines/index.html). The treebanks contain mainly news and non-fiction.

Evaluation result on the joint Talbanken and LinES test sets: **96.37**

##### XPOS tagger

Since the Talbanken and LinES treebanks are annotated with different  XPOS tagsets we could not use them to train the XPOS model. Instead we  used Talbanken and the Stockholm-Umeå Corpus v3.0 ([SUC 3.0](https://spraakbanken.gu.se/en/resources/suc3)), which is a balanced corpus containing different types of news text, as well as fictional and non-fictional prose.

Evaluation result on the Talbanken test set plus a held-out portion of SUC 3.0: **96.84**

##### Dependency parser

The parser is trained on the Talbanken and LinES treebanks, and is equivalent in both models.

Evaluation results on the joint Talbanken and LinES test sets:

- Unlabelled Attachment Score (UAS) **87.03**
- Labelled Attachment Score (LAS) **82.20**

##### NER

Named Entity Recognition was trained on the Stockholm Umeå Corpus  v3.0 (SUC 3.0). Unlike pos tags, entities in SUC 3.0 were not annotated  by human annotators, but automatically generated using [Sparv](https://spraakbanken.gu.se/en/tools/sparv/annotations). This means that they cannot be considered a gold standard.

Evaluation results on a held-out portion of SUC 3.0:

- Precision **86.27**
- Recall **84.48**
- F score **85.37**

kommer sedan att testas på den annoterade delen av corpusen. Sedan kommer ett svenskt dictionary med symtom för covid-19 från ICD-10 koder och Snomed-CT att sammanställas. Detta kommer sedan att användas för att träna en svensk BERT (Kungliga Biblioteket) för symtom NER. Detta avslutar T5 arbetet, men projektet ämnar om det funkar sedan att gå vidare med att läsa och strukturera data från 100 000 akutmottagningsbesök under coronapandemin. Denna data i strukturerat format ämnas användas för att koppla ihop symptombild med positivt eller negativt test för covid-19 och ge en prediktiv sannolikhetsuppskattning för att en viss symptombild är kopplad till covid-19 positivitet.

## Ethical considerations

Alla texter som används i projektet ska behandlas enligt etiska och legala riktlinjer (patientsäkerhetslagen, GDPR). Etiskt tillstånd för användning av journaltexter från region Skåne finns.

## References

1. Semantic Scholar. COVID19 open dataset [Internet] [cited 202 Oct 4]. Available from: https://pages.semanticscholar.org/coronavirus-research
2. Bioinformatics, Volume 36, Issue 4, 15 February 2020, Pages 1234–1240, https://doi.org/10.1093/bioinformatics/btz682
3. (https://spraakbanken.gu.se/)
4. Cornell University Arxiv. English dictionaries, gold and silver standard corpora for biomedical natural language processing related to SARS-CoV-2 and COVID-19, arXiv:2003.09865 [q-bio.OT], https://arxiv.org/abs/2003.09865
5. https://github.com/Aitslab/corona/blob/master/dictionaries/corona_symptoms_SE.txt