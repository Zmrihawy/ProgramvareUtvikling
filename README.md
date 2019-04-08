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
4. Nå skal alt være klart til å kjøre serveren. Gå inn i terminalen (Alt+F12) og utfør
```
python manage.py runserver
```
5. Nå skal du få opp en beskjed som den under, og du kan åpne nettsiden i nettleseren på http://127.0.0.1:8000/
```
System check identified no issues (0 silenced).
April 06, 2019 - 17:20:31
Django version 2.1.7, using settings 'chefsApprentice.settings'
Starting development server at http://127.0.0.1:8000/
```



## Hvordan kjøre tester
Alt du trenger å gjøre for å kjøre testene er å åpne terminalen (Alt+F12) og kjøre kommandoen
```
python manage.py tests
```




## Pakker
- [Django](https://www.djangoproject.com/start/overview/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)

