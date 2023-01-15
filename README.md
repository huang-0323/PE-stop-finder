# **PE-stop-finder**

* * *

PE-stop-finder is an easy-to-use, fast program that can be used for genome analysis of the PE gene-stop experiment and subsequent sgRNA design. It has low configuration requirements and can be run on a personal laptop.

## **Feature**

* * *

PE-stop-finder have following features can be apply on PE-stop editing process and experiment design.

- All editability at different level(ORF/Exon/Transcript/Gene) info from genome are summarized into a simple result.
- Different motif editability result are summarized into an CSV file.
- Detail sgRNA design from specific input sequence are output into a GFF-format file.
- Analysis results can be visualized in a variety of graphs(Stack bar-chart/pie-chart).

## **Requirements**

* * *

- Software 
  1. Python3\
     Dependent Python modules:
  - [pysam](https://pysam.readthedocs.io/en/latest/index.html)
  - [pandas](https://pandas.pydata.org/)
  - [regex](https://pypi.org/project/regex/)
  - [biopython](https://pypi.org/project/biopython/)
  2. R(>4.0)\
     Dependent R packages:
  - [ggplot2](https://github.com/tidyverse/ggplot2)
  - [stringr](https://mirrors.tuna.tsinghua.edu.cn/CRAN/web/packages/stringr/index.html)
  3. [ORFinder](https://www.ncbi.nlm.nih.gov/orffinder/)


- Data

  - Genome file(.fa/.fna/.fasta)
  - Annotation file(.gff)\
    _note: chromosome name from genome file should be same as in annotation file. We recommend download those file from NCBI genome browser._

- manual file
  - motif annotation file(.motif)\
      content should be (edit motif)-(window length)-(PAM)\
    _example: CAAN(3,12)NGG_

## **Usage**

* * *

PE-stop-finder program are divide into three function, each function can be run independently, but the result files between functions can be called to each other.

### **Function 1: Genome-wide editability analysis**

```shell
python PPSID summary --help
Usage: PPSID summary [OPTIONS]

Options:
  -f, --genome PATH  Select the genome file.   [required]
  -g, --gff PATH     Select the gff file.   [required]
  -r, --region TEXT  Set the design area.  [default: default]
  -m, --motif PATH   Set the motif sequence.
  -o, --output TEXT
  --help             Show this message and exit
```

#### **Parameters**

| Parmeters | Description                                          | Input           |
| --------- | ---------------------------------------------------- | --------------- |
| -f        | genome file or sequences file.                       | .fa/.fna/.fasta |
| -g        | genome annotation file.                              | .gff            |
| -r        | region that use for analysis(default: whole genome). | chromosome name |
| -m        | motif that use for search.                           | .motif          |
| -o        | output file prefix.                                  | text            |

#### **result file**

Genome-wide editability analysis function will output 2 .csv file, including prefix.coverage.summary.csv and prefix.stop.summary.csv.

| Field | Description (prefix.coverage.summary.csv)             |
| ----- | ----------------------------------------------------- |
| exon  | motif editability of each exon (percentage).          |
| id    | motif editability of each transcription (percentage). |
| gene  | motif editability of each transcription (percentage). |

| Field             | Description (prefix.stop.summary.csv)    |
| ----------------- | ---------------------------------------- |
| chr               | sequence chromosome position.            |
| start             | sequence start position.                 |
| end               | sequence end position.                   |
| id                | sequence id(provide by annotation file). |
| exon              | exon number(provide by annotation file). |
| gene_name         | gene symbol(provide by annotation file). |
| seq               | sequence.                                |
| motif_editability | sequence editability of each motif .     |

### **Function 2: sgRNA design**

```shell
python PPSID design --help
Usage: PPSID design [OPTIONS]

Options:
  -in, --seq PATH         Select the genome file.   [required]
  -if, --isfasta BOOLEAN  runing in the orf mode
  -m, --motif PATH        Select the gff file.   [required]
  -o, --output TEXT
  --help                  Show this message and exit.
```

#### **Parameters**

| Parmeters | Description                                         | Input           |
| --------- | --------------------------------------------------- | --------------- |
| -in       | genome file or sequences file.                      | .fa/.fna/.fasta |
| -if       | running orf analysis for input seq(default: False). | True/False      |
| -m        | motif that use for search.                          | .motif          |
| -o        | output file prefix.                                 | text            |

#### **result file**

sgRNA design function will output .out file, this file has seven columns separated by commas

| Field     | Description                                                 |
| --------- | ----------------------------------------------------------- |
| chr       | sequence chromosome position.                               |
| start     | sequence start position.                                    |
| end       | sequence end position.                                      |
| id        | sequence id(provide by annotation file).                    |
| exon      | exon number(provide by annotation file).                    |
| gene_name | gene symbol(provide by annotation file).                    |
| sgRNA     | all available sgRNA for this sequence, separated by commas. |

### **Function 3: Analysis result visualization**

    Lorem.ipsum(epicurei[, saepe[, explicari]])

#### **Parameters**

| Senserit  | Repudiandae                         | Vis |
| --------- | ----------------------------------- | --- |
| epicurei  | Usu no tale prima, vis fugit  id.   | Cu  |
| saepe     | Ea vis graecis concludaturque.      | Cum |
| explicari | Clita quando `this` in mea `saepe`. | Cum |

#### **result file**

Ea alii putent integre sed.

## Citation

* * *
