# IT4 Projekt

## Popis projektu
Sportovni stranka je bezplatná webová aplikace pro zobrazení sportovních výsledků
jako je kriket, fotbal a basketbal. Tato webová aplikace byla vytvořena pomocí Pythonu, konkrétněji webového rámce Django pro backend a pro frontend bylo použito Html, CSS a Javascript. 
Data použitá v aplikaci jsou přijímána pomocí open source rozhraní API pro sportovní výsledky nazývaného jako Sports.py 
Data z rozhraní API pro skóre jsou přijímána jako slovník týmů a skóre, který je poté iterován a uložen v databázi sqlite. 
Data v databázi se používají k zobrazení skóre. Uživatelé se musí před zobrazením skóre přihlásit, je to proto, aby bylo možné sledovat počet uživatelů používajících webovou aplikaci. 
Registrační formulář a přihlášení byly vytvořeny pomocí výchozích registračních stránek poskytovaných webovým rámcem Django








# Jak spustit projekt
1. Napiš
``` python
pip install -r requirements.txt
```
Nebo
``` python
pip3 install -r requirements.txt
```

2. Po instalaci požadovaných závislostí můžete spustit lokální server pomocí
``` python
python manage.py runserver
```
a přejděte na uvedenou adresu.