<h1 align="center">
  <br>
  ![alt text](http://chefsapprentice.space/static/browse/images/logo.png "ChefsApprentice logo")
</h1>

# Spis opp maten din!

ChefsApprentice er fremtidens sosiale medium for en mer bærekraftig verden. Ved å søke i vår database etter matoppskrifter kan du bruke opp restene fra gårsdagen ved å lage en matrett som bruker dem opp. Slik kaster vi mindre mat, og tar bedre vare på planeten vår!

## Hvordan sette opp prosjektet
1. Klon git repositoryen til din ønskede mappe (Krever gitlab-login)
```sh
$ git clone https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-10.git
```
2. Åpne mappen "chefsApprentice" i PyCharm. Denne er i "gruppe-10" mappen.
3. PyCharm skal automatisk detektere hvilke pakker som skal innstalleres, alt du trenger å gjøre er å trykke "Install Packages" på beskjeden som kommer opp. Om denne ikke kommer opp må du installere Django, Pillow og Django Crispy Forms som vist under
```
pip install Django==2.1.7
```
```
pip install pillow
```
```
pip install django-crispy-forms
```
4. Første gangen du åpner prosjektet må du legge til django server som en konfigurasjon.
5. Nederst vil det stå "Error: please enable django support for the project" trykk på "fix" og enable django support.
som rotmappe velger du 'bane-til-gruppe_10'/gruppe_10/chefsApprentice/chefsApprentice, settings fil velger du
settings.py som ligger i rotmappen og manage script velger du manage.py som ligger et nivå over.
6. Nå må du kjøre kommandoene:
```
cd chefsApprentice/
python manage.py makemigrations
python manage.py migrate
```
slik at databasen blir satt opp med riktige modeller
7. Nå skal alt være klart til å kjøre serveren. Gå inn i terminalen (Alt+F12) og utfør
```
python manage.py runserver
```
**Obs!** Det kan hende at du må kjøre kommandoene ovenfor med python3 istedenfor python

8. Nå skal du få opp en beskjed som den under, og du kan åpne nettsiden i nettleseren på http://127.0.0.1:8000/
```
System check identified no issues (0 silenced).
April 06, 2019 - 17:20:31
Django version 2.1.7, using settings 'chefsApprentice.settings'
Starting development server at http://127.0.0.1:8000/
```
Om Databasen viser seg for å være tom(siden den ikke ligger i repositorien, men på serveren våres) må du følge neste steg 9

9.1 Alt som gjenstår er å sette opp nødvendig data i databasen. 
Vi må først legge til en bruker med brukernavn "Unknown":
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
user=User.objects.create_user('Unkown', password='userpassword')
user.save()
exit()
```
9.2 Lag en admin bruker:
```bash
python manage.py createsuperuser
```
fyll ut først brukernavn, så optional email og til slutt passord når disse meldingen dukker opp:
```bash
Username (leave blank to use 'bruker'): 
Email address: 
Password: 
Password (again): 
```

9.3 Gå tilbake til python shell og lag gruppene user og chef

```bash
python manage.py shell
```
```python
from django.contrib.auth.models import Group
user=Group.objects.create(name='user')
chef=Group.objects.create(name='chef')
user.save()
chef.save()
exit()
```

Da er alt klart for å sette prosjektet i drift.


## Hvordan kjøre tester
Alt du trenger å gjøre for å kjøre testene er å åpne terminalen (Alt+F12) og kjøre kommandoen
```
python manage.py tests
```
Testene blir også kjørt om man pusher en ny versjon til master.


## Server

Du kan finne seneste versjon av chefsApprentice på nettsiden: http://chefsapprentice.space/





## Pakker
- [Django](https://www.djangoproject.com/start/overview/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)

