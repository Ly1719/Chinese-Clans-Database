# Chinese Clans Database

**A city–year panel dataset of Chinese clan genealogies (族谱), built from approximately 100,000+ genealogies scraped from Shanghai Library’s collection, covering both provincial and over 300+ city-level panels for quantitative research.**

---

## 1. Overview  
The **Chinese Clans Database** aggregates and harmonizes genealogical archives into structured **cross-sectional** and **panel datasets** at both the **province–year** and **city–year** levels, spanning up to **2023**. Through intensive web scraping and robust data processing, the repository delivers clean, reproducible datasets and pipelines to support research in economics, sociology, political science, and history.

---

## 2. Data Volume & Your Contributions  
- Shanghai Library holds one of the world’s top collections of Chinese genealogies—over **300,000 volumes** representing nearly **40,000 unique genealogies**, across hundreds of surnames.  
- From these, I scraped metadata from approximately **100,000 genealogy records**, extracting titles, compilers, surnames, compilation years, and geographic information.  
- I processed and standardized the data to create:  
  - A **cross-sectional dataset** of city-level genealogical counts as of 2023.  
  - A **panel dataset** capturing annual changes at both the **province and city levels**, covering over **300+ cities**.  
- The entire pipeline—from web scraping to data cleaning, panel construction, and merging with socioeconomic indicators—was implemented by me using **Python**, ensuring reproducibility, transparency, and academic rigor.

---

## 3. Data Description

| Dataset Type         | File Name                         | Description                                                    |
|----------------------|-----------------------------------|----------------------------------------------------------------|
| Cross-sectional       | `genealogy_cross-section_2023.csv` | Total genealogies per city as of 2023.                         |
| Province-level Panel  | `genealogy_panel.csv`             | Annual genealogy counts per province.                          |
| City-level Panel      | `genealogy_panel.csv`             | Time-series counts per city for over 300+ cities.              |

---

## 4. Repository Structure
Chinese-Clans-Database/
├── README.md
├── src/
├── data/
├── notebooks/
├── figure/
├── reports/
├── genealogy_cross-section_2023.csv
├── genealogy_panel.csv
├── docs/
└── .idea/

## 5. Possible Use Cases
Economics: Investigate informal institutions, clan networks, and rural cooperation.

Sociology: Explore cultural persistence and kinship across generations.

Political Science: Analyze local governance and informal community structures.

History & Demography: Reconstruct social and demographic evolution using genealogical records.

## 7. Dependencies
Python 3.13  

## 8. Citation
If you use this dataset, please cite:

Yan Liao. (2025). Chinese Clans Database. GitHub Repository.
https://github.com/Ly1719/Chinese-Clans-Database