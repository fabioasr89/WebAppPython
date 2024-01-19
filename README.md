Semplice web app MVT di esempio scritta in python usando il micro framework FLASK, con ambiente virtualizzato.

Nell'applicativo ho implementato una semplice autenticazione che, a partire da una semplice pagina di login,
immettendo username e password verifica su un db mysql la presenza dell'utente, lo mette in sessione e lo reindirizza su una pagina index.
Ho implementato anche la funzionalità di logout.
Le sessioni sono gestite  con FLASK.
Inoltre, ho configurato i logger per gestire sia lo stdout che il rolling su filesystem.
Il layout delle pagine web è gestito con una master ereditata da login ed index, inserite tutte sotto la cartella templates, utilizzata
di default da flask.
Il css è di bootstrap 5.

Per testare la web app, importare il progetto su un ide appropriato (esempio visual studio code), attivare l'ambiente
virtualizzato usando da cmd il comando:

	.venv/Scripts/activate

A quel punto basterà eseguire l'istruzione

	python server.py

per avviare tutto. Ovviamente, dovrete (PRIMA) creare il percorso  var/opt/log nel vostro filesystem per poter permettere al rolling di funzionare,
e definire la tabella users su un db mysql eseguendo GLI SCRIPT allegati nel progetto.
A quel punto dovrebbe funzionare senza problemi.



