# 🐹 IH RF – Analiza danych federacji sportowej chomików

Projekt obejmuje zaprojektowanie relacyjnej bazy danych, jej wypełnienie realistycznymi danymi,
przeprowadzenie analizy statystycznej oraz automatyczne wygenerowanie raportu końcowego
w formacie HTML/PDF.

---

## 📦 Spis treści
1. Opis projektu  
2. Użyte technologie  
3. Struktura plików  
4. Instrukcja uruchomienia projektu  
5. Schemat bazy danych  
6. Normalizacja (EKNF / 3NF)  
7. Najtrudniejsze elementy projektu  

---

## 1️⃣ Opis projektu

Celem projektu jest analiza działalności federacji sportowej **IH RF**, organizującej zawody
sportowe dla chomików. Projekt obejmuje zarówno aspekt sportowy (wyniki, kariery zawodników,
konkurencyjność dyscyplin), jak i organizacyjno-finansowy
(popularność sportu, rentowność federacji, atrakcyjność dla sponsorów).

Całość została zaprojektowana w sposób umożliwiający pełną automatyzację:
od utworzenia bazy danych, przez jej wypełnienie, aż po wygenerowanie raportu końcowego.

---

## 2️⃣ Użyte technologie

- MySQL – relacyjna baza danych  
- Python 3 – główny język programowania  
- mysql-connector-python – komunikacja Python ↔ MySQL  
- pandas – przetwarzanie i analiza danych  
- matplotlib – wizualizacja danych  
- SciPy – testy statystyczne  
- Jupyter Notebook – środowisko analityczne i raportowe  
- nbconvert – automatyczne generowanie raportów HTML/PDF  

---

## 3️⃣ Struktura plików

```
.
├── create_database.py
├── fill_database.py
├── analiza_ihrf_z_raportem_ladny.ipynb
├── raport_IHRF.html
└── README.md
```

---

## 4️⃣ Instrukcja uruchomienia projektu

```bash
python create_database.py
python fill_database.py
jupyter nbconvert --to html --execute --no-input analiza_ihrf_z_raportem_ladny.ipynb
```

---

## 5️⃣ Schemat bazy danych

Baza danych składa się z tabel:
employees, sponsors, sponsorships, funding_sources, hamsters, disciplines,
competitions, prohibited_substances, doping_controls.

Relacje:
- competitions.discipline_id → disciplines.discipline_id  
- competitions.hamster_id → hamsters.hamster_id  
- sponsorships.sponsor_id → sponsors.sponsor_id  
- doping_controls.hamster_id → hamsters.hamster_id  
- doping_controls.substance_id → prohibited_substances.substance_id  

---

## 6️⃣ Normalizacja – EKNF (3NF)

Baza danych spełnia warunki trzeciej postaci normalnej (3NF):
- atrybuty są atomowe,
- brak zależności częściowych,
- brak zależności przechodnich.

---

## 7️⃣ Najtrudniejsze elementy projektu

Największym wyzwaniem było:
- zachowanie spójności czasowej danych,
- analiza bez tabeli uczestników zawodów,
- poprawne rozliczenie kosztów wynagrodzeń,
- pełna automatyzacja raportowania.

---

## ✅ Podsumowanie

Projekt obejmuje pełny cykl pracy z danymi:
projekt bazy → generowanie danych → analiza → raport końcowy.
