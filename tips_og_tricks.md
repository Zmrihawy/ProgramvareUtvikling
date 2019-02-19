# Tips&Tricks

## Virtual Environments

### Pip vil ikke oppdatere/installere
'NoneType' object has no attribute 'bytes'

Fors�k � tving pip til � oppdatere gjennom
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
#### Gj�re et venv flyttbar:
virtualenv --relocatable ENV

# Django
## Opprette nye apps
S�rg for � v�re i rett path, og utf�r:
> python manage.py startapp *appnavnher*

## Kj�re server fra terminal
> python manage.py runserver
 
## Django won't refresh *staticfiles*
Dersom du har laget en ny css-fil, men sidene dine bruker fortsatt den gamle, fors�k:
> Ctrl + Shift + Delete
p� windows, eller
> Shift + Cmd + Backspace
p� mac, og slett *hurtiglager for nettsider* i nettleseren din

