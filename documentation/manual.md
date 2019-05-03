# Asennusohje

### Paikallinen asennus

- Kloonaa sovelluksen repositorio
- Luo sovelluksen hakemistoon virtuaaliympäristö komennolla python3 -m venv venv
- Aktivoi virtuaaliympäristö komennolla source venv/bin/activate
- Asenna sovelluksen riippuvuudet komennolla pip install -r requirements.txt
- Käynnistä sovellus komennolla python3 run.py

### Heroku

- Saadaksesi sovelluksen toiminaan herokussa aja seuraavat komennot:
 - heroku create sovelluksen-nimi
 - git remote add heroku https://git.heroku.com/sovelluksen-nimi.git
 - git push heroku master


# Käyttöohje

- Tiedon lisääminen, muokkaaminen tai poistaminen sovelluksessa vaatii kirjautumisen. Kirjautuminen tapahtuu sovelluksen yläpalkista löytyvästä linkistä "Kirjaudu".

### Kiireellisyysluokat

- Kiireellisyysluokan lisääminen tapahtuu valitsemalla sovelluksen yläpalkista "Kiireellisyysluokat" > "Lisää kiireellisyysluokka".
- Kiireellisyysluokkien listaaminen tapahtuu valitsemalla sovelluksen yläpalkista "Kiireellisyysluokat" > "Lista kiireellisyysluokista".

### Aukiolotunnit

- Aukiolotuntien lisääminen tapahtuu valitsemalla sovelluksen yläpalkista "Aukiolotunnit" > "Lisää aukiolotunteja". Tarvittava kiireellisyysluokka on lisättävä ennen aukiolotunnin lisäämistä.
- Aukiolotuntien listaaminen tapahtuu valitsemalla sovelluksen yläpalkista "Aukiolotunnit" > "Lisää aukiolotunteja".

### Työntekijät

- Työntekijöiden lisääminen tapahtuu valitsemalla sovelluksen yläpalkista "Työntekijät" > "Lisää työntekijä".
- Työntekijöiden listaaminen tapahtuu valitsemalla sovelluksen yläpallkista "Työntekijät" > "Lista työntekijöistä".
- Työntekijöitä voi muokata ja poistaa työntekijälistan painikkeista.
- Työntekijäkohtaisten työtuntien listaaminen tapahtuu valitsemalla sovelluksen yläpalkista "Työntekijät" > "Työntekijäkohtaiset työtunnit".

### Työvuorot

- Työvuorojen lisääminen tapahtuu valitsemalla sovelluksen yläpalkista "Työvuorot" > "Lisää työvuoroja". Tarvittavat aukiolotunnit ja työntekijät on lisättävä ennen työvuorojen lisäämistä.
- Työvuorojen listaaminen tapahtuu valitsemalla sovelluksen yläpalkista "Työvuorot" > "Lista työvuoroista".
- Niiden työvuorojen, joihin ei ole lisätty tarpeeksi työntekijöitä, listaaminen tapahtuu valitsemalla sovelluksen yläpalkista "Työvuorot" > "Työntekijöitä tarvitsevat työvuorot".
