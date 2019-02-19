# Tips&Tricks

## Virtual Environments

### Pip vil ikke oppdatere/installere
'NoneType' object has no attribute 'bytes'

Forsøk å tving pip til å oppdatere gjennom
```
python -m pip install -U --force-reinstall pip
```

### Aktivere/deaktivere venvs
#### Aktivering:
> \path\to\env\Scripts\activate
#### Deaktivering:
>deactivate
#### Slette et venv:
>deactivate
>rm -r /path/to/ENV
#### Gjøre et venv flyttbar:
virtualenv --relocatable ENV

# Django
## Opprette nye apps
Sørg for å være i rett path, og utfør:
> python manage.py startapp *appnavnher*

## Kjøre server fra terminal
> python manage.py runserver
 
## Django won't refresh *staticfiles*
Dersom du har laget en ny css-fil, men sidene dine bruker fortsatt den gamle, forsøk:
> Ctrl + Shift + Delete
på windows, eller
> Shift + Cmd + Backspace
på mac, og slett *hurtiglager for nettsider* i nettleseren din

