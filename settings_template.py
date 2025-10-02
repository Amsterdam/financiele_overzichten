# dit bestand bevat instellingen voor de tool
# onderstaande waarden zijn nu ingesteld voor gebruik door J.T.
# pas de waarden als dat nodig is aan voor je eigen systeem
# sla het bestand op als settings.py en voeg settings.py niet toe aan de repository
import getpass
username = getpass.getuser()

# basismap
base_folder = f"C:/Users/{username}/OneDrive - Gemeente Amsterdam"
# testmap voor inlezen
folder_in_test = f"{base_folder}/Data/AFIS/FIP"
# map voor inlezen van alle excel bestanden (indien toegevoegd aan persoonlijk OneDrive map, zie README.md)
folder_in = f"{base_folder}/Team Data, Rapportages en Innovatie (DR&I) - Boekingsregels"
# map voor schrijven
folder_uit = f"{base_folder}/Data/AFIS/FIP/CSV_data"
# voor testdraaien zet test op True, anders op False
test = True
# voor het doorlopen van alle bestanden bij het inlezen, zet check_al_gedaan op False
check_al_gedaan = True
decimal = "."
sep = ";"
