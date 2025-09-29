import numpy as np
import os
import pandas as pd
from settings import basis_folder_in, basis_folder_uit, check_al_gedaan, decimal, sep


folder_in = f"{basis_folder_in}/Team Data, Rapportages en Innovatie (DR&I) - Boekingsregels"
folder_uit = f"{basis_folder_uit}/Bestanden van Tse, Jeffrey - FIP/CSV_data"

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
    data = pd.read_excel(f"{folder_in}/{f}", header=9)

    # data opschonen
    # volledige lege kolommen verwijderen
    data = data[[col for col in data.columns if "Unnamed" not in col]]

    # data wegschrijven
    data.to_csv(f"{folder_uit}/{f.replace('xlsx', 'csv')}", decimal=decimal, sep=sep)

# check de kolomnamen

# maak een dataframe om op te slaan
kolommen_dict = {}

# check of er al een kolommentabel is
if os.path.isfile(f"{folder_uit}/kolomnamen.xlsx"):
    # die inlezen
    kolommen_tabel = pd.read_excel(f"{folder_uit}/kolomnamen.xlsx")

# maak een lijst met uitvoerbestanden
files = [f for f in os.listdir(folder_uit) if f.lower().endswith("csv")]

# lees de kolomnamen in uit de omgezette CSVs
for f in files:
    print(f)
    data = pd.read_csv(f"{folder_uit}/{f}", decimal=decimal, sep=sep, nrows=1)
    kolommen = data.columns
    kolommen_dict[f] = kolommen.to_numpy()

# de nieuwe bestanden toevoegen aan de kolommentabel
# check of er al een kolommentabel was
if os.path.isfile(f"{folder_uit}/kolomnamen.xlsx"):
    # dan de nieuwe eraan plakken
    kolommen_tabel = pd.concat([kolommen_tabel, pd.DataFrame().from_dict(kolommen_dict).transpose()])    
else:
    # anders een tabel maken
    kolommen_tabel = pd.DataFrame().from_dict(kolommen_dict).transpose()

kolommen_tabel = kolommen_tabel.drop_duplicates()

kolommen_tabel.to_excel(f"{folder_uit}/kolomnamen.xlsx")