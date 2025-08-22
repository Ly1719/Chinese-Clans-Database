# Chinese Clans Database

**A city–year panel dataset of Chinese clan genealogies (族谱), built by scraping all genealogical records preserved in the Shanghai Library (about 100,000+ entries), covering the entire collection from the earliest available records up to 2024, and organized into over 300 city-level panels for quantitative research.**

---

## 1. Overview  
The Chinese Clans Database is built upon intensive web scraping of genealogical records from the Shanghai Library, covering the entire collection. These archives are then aggregated and harmonized into structured **cross-sectional** and **panel datasets** at both the **province–year** and **city–year** levels. The repository delivers clean, reproducible datasets to support research in economics, sociology, political science, and history.


- Shanghai Library holds the world’s most comprehensive collection of Chinese genealogies — covering more than 100,000 genealogical records across hundreds of surnames. 
- From these, I scraped metadata from approximately 100,000 genealogy records, extracting titles, compilers, surnames, compilation years, and geographic information.  
- I processed and standardized the data to create:  
  - A **cross-sectional dataset** of city-level genealogical counts as of 2023.  
  - A **panel dataset** capturing annual changes at both the province and city levels, covering over 300+ cities.  
- The entire pipeline—from web scraping to data cleaning, panel construction, and merging with socioeconomic indicators—was implemented by me using **Python**, ensuring reproducibility, transparency, and academic rigor.

---

## 2. Data Description

| Dataset Type         | File Name                         | Description                                                    |
|----------------------|-----------------------------------|----------------------------------------------------------------|
| Cross-sectional       | `genealogy_cross-section_2023.csv` | Total genealogies per city as of 2023.                         |
| Province-level Panel  | `genealogy_panel.csv`             | Annual genealogy counts per province.                          |
| City-level Panel      | `genealogy_panel.csv`             | Time-series counts per city for over 300+ cities.              |

---

## 3. Possible Use Cases
Economics: Investigate informal institutions, clan networks, and rural cooperation.

Sociology: Explore cultural persistence and kinship across generations.

Political Science: Analyze local governance and informal community structures.

History & Demography: Reconstruct social and demographic evolution using genealogical records.

---

## 4. Dependencies
Python 3.13  

---

## 5. Citation
If you use this dataset, please cite:

Yan Liao. (2025). Chinese Clans Database. GitHub Repository.
https://github.com/Ly1719/Chinese-Clans-Database