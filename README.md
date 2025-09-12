# financiele_overzichten
Tools om financiële overzichten te controleren en/of te transformeren

# Heb je geen ervaring met Python? Volg dan deze stappen
## Benodigde programma's
1. Download en installeer deze programma's met de standaardinstellingen:
* [Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
* [Git](https://git-scm.com/downloads/win)

## De applicatie opslaan (dit is allemaal eenmalig)
1. Maak een map waarin je de bestanden willen opslaan, noem deze bijvoorbeeld _scripts_
1. Klik in de map _scripts_ met de rechtermuisknop en kies voor _Git Bash here_ (windows 10) of _Open Git Bash_ (windows 11)
1. Kopieer en plak (met rechtse muisknop of shift + Insert):
* `git clone https://github.com/Amsterdam/financiele_overzichten.git`
1. Je kan het Git bash venster nu afsluiten met `exit`

1. Er is nu een map gemaakt met de naam _financiele\_overzichten_  

1. Ga naar de Windows startknop en type daar `cmd`
1. Kies _Anaconda Prompt (Miniconda3)_
1. Ga in de prompt naar de map _financiele\_overzichten_
1. kopieer en plak:
* `conda env create --file environment.yml`

## De applicatie gebruiken
1. Ga naar de Windows startknop en type daar `cmd`
1. Kies _Anaconda Prompt (Miniconda3)_
1. Ga in de prompt naar de map _financiele\_overzichten_
1. kopieer en plak:
* `python tool.py`

## De applicatie updaten
De applicatie is nog niet uitontwikkeld en er komen updates beschikbaar.
Heb je de applicatie eerder al opgeslagen met de stappen onder _De applicatie opslaan (dit is allemaal eenmalig)_?
Dan kun je zo de nieuwste versie krijgen:
1. Ga naar de map waarin de bestanden zijn opgeslagen, in het voorbeeld heet deze _scripts/financiele\_overzichten_
1. Klik in de map _scripts/financiele\_overzichten_ met de rechtermuisknop en kies voor _Git Bash here_ (windows 10) of _Open Git Bash_ (windows 11)
1. Kopieer en plak (met rechtse muisknop of shift + Insert):
* `git pull origin main`
1. Je kan het Git bash venster nu afsluiten met `exit`
1. Je hebt de nieuwste versie
