import os
import polars as pl
from settings import folder_in_test, folder_in, folder_uit, test, check_al_gedaan, separator, decimal_comma

# check of test al is gedaan:
if test:
    folder_in = folder_in_test

# maak een lijst met de bestanden in de invoermap
files = [f for f in os.listdir(folder_in) if f.lower().endswith("xlsx")]

# bestanden die al zijn gedaan niet op nieuw doen
# dit is een optie die aan en uit kan
if check_al_gedaan:
    files = [f for f in files if not os.path.isfile(f"{folder_uit}/{f.replace('xlsx', 'csv')}")]

# doorloop de bestanden
for f in files:
    print(f)
    # data inlezen
    data = pl.read_excel(f"{folder_in}/{f}", read_options={'header_row': 9})

    # data opschonen
    # volledige lege kolommen verwijderen
    data = data[[col for col in data.columns if "Unnamed" not in col]]

    # data wegschrijven
    data.write_csv(f"{folder_uit}/{f.replace('xlsx', 'csv')}", separator=separator, decimal_comma=decimal_comma)

# check de kolomnamen

# maak een dataframe om op te slaan
kolommen_dict = {}

# check of er al een kolommentabel is
if os.path.isfile(f"{folder_uit}/kolomnamen.xlsx"):
    # die inlezen
    kolommen_tabel = pl.read_excel(f"{folder_uit}/kolomnamen.xlsx")

# maak een lijst met uitvoerbestanden
files = [f for f in os.listdir(folder_uit) if f.lower().endswith("csv")]

# lees de kolomnamen in uit de omgezette CSVs
for f in files:
    print(f)
    data = pl.read_csv(f"{folder_uit}/{f}", separator=separator, decimal_comma=decimal_comma, n_rows=1, ignore_errors=True)
    file_name = pl.Series(f, [None])
    data = data.insert_column(0, file_name)
    kolommen = data.columns
    kolommen_dict[f] = kolommen

# de nieuwe bestanden toevoegen aan de kolommentabel
# check of er al een kolommentabel was
if os.path.isfile(f"{folder_uit}/kolomnamen.xlsx"):
    # dan de nieuwe eraan plakken
    kolommen_tabel = pl.concat([kolommen_tabel, pl.from_dict(kolommen_dict).transpose()])    
else:
    # anders een tabel maken
    kolommen_tabel = pl.from_dict(kolommen_dict).transpose()

# kolommen_tabel = kolommen_tabel.loc[~kolommen_tabel.index.duplicated(keep='first')]

kolommen_tabel.write_excel(f"{folder_uit}/kolomnamen.xlsx")