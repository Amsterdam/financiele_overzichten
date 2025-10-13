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
# in de oorspronkelijke bestanden was de headerregel 10, als dat later veranderd is, kun je hier een nieuwe waarde instellen
header = 10
# scheidingsteken voor kolommen in csv kun je instellen met separator. We adviseren puntkomma te gebruiken.
separator = ";"
# om decimale komma's te gebruiken voor weggeschreven bestanden zet decimal_comma op True. We adviseren hier False te gebruiken.
decimal_comma = False
