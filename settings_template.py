# dit bestand bevat instellingen voor de tool
# pas de waarden als dat nodig is aan voor je eigen systeem
# sla het bestand op als settings.py en voeg settings.py niet toe aan de repository
import getpass
username = getpass.getuser()

folder_in = f"C:/Users/{username}/OneDrive - Gemeente Amsterdam/Team Data, Rapportages en Innovatie (DR&I) - Boekingsregels"
# voor J.T.
folder_uit = f"C:/Users/{username}/OneDrive - Gemeente Amsterdam/Data/AFIS/FIP/CSV_data"
# voor T. en M. (en anderen met toegang tot "FIP/CSV_data" van J.T.) ...
# ... comment regel 9 en uncomment regel 12
# basis_folder_uit = f"C:/Users/{username}/OneDrive - Gemeente Amsterdam/Bestanden van Tse, Jeffrey - FIP/CSV_data"
check_al_gedaan = True
decimal = "."
sep = ";"
