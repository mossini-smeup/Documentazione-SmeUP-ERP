# TARSS     -  RISALITA AL SOTTOSETTORE
Definisce la modalità con cui risalire al sottosettore delle tabelle al fine di ottenere un uso dinamico dei sottosettori stessi.
Questo attributo assume validità solo se la caratteristica del sottosettore è diversa da "N" (Obbligatoriamente bianco).

## VALORI POSSIBILI

### ' ' NON RISALE (ASSUME OGGETTO)
Se riceve un sottosettore diverso da bianco viene mantenuto.
Se riceve un sottosettore bianco ed è attiva la gestione dell'oggetto, viene assunto il
l'oggetto nel sottosettore indipendentemente dal fatto che sia un sottosettore valido.

### '1' ASSUME IL BIANCO
Viene sempre impostato il sottosettore bianco, anche se ricevuto.

### '2' AL BIANCO SE MANCA O DEVIAZIONE
Se ricevuto un sottosettore diverso da bianco e non ha deviazione viene mantenuto, se
sottosettore valido, altrimenti assume bianco.
Se ricevuto un sottosettore diverso da bianco e ha deviazione valida, viene assunta,
altrimenti diventa bianco (NB :  non viene mantenuto il sottisettore ricevuto).

### '3' RISALE OGGETTO SE PASSO BIANCO
Se ricevuto un sottosettore diverso da bianco viene mantenuto
Se ricevuto un sottosettore bianco cerca di derivarlo.
Se non impostato l'oggetto del sottosettore rimane bianco.
Altrimenti assume l'oggetto se è un sottosettore valido.
Si differenzia dal caso ' ' per il fatto che il sottosettore dell'oggetto deve esistere.

### '4' ASSUME OGGETTO SE MANCA BIANCO
Se ricevuto un sottosettore bianco se esiste il sottosettore dell'oggetto risale a quello.
Se ricevuto un sottosettore diverso da bianco viene mantenuto se il sottosettore esiste.
Si differenzia dal caso '3' perchè la risalilta al bianco viene fatta anche quando viene
passato il sottosettore blank.

## ESEMPIO
Oggetto nel sottosettore A (Azienda) con risalita al sottosettore ' ' (Non risale)
### Ricerca tabella
Il sottosettore è sempre l'azienda.
### Gestione tabella
Il sottosettore è libero.

Oggetto nel sottosettore A (Azienda) con risalita al sottosettore '1' (Assume il bianco)
### Ricerca tabella
Il sottosettore è sempre bianco anche se passato un sottosettore esplicito.
### Gestione tabella
Il sottosettore è sempre bianco, viene impedito l'uso del sottosettore.

Oggetto nel sottosettore A (Azienda) con risalita al sottosettore '2' (Al bianco se manca o deviazione) con deviazione bianca
### Ricerca tabella
Il sottosettore è sempre quello ricevuto, se inesistente assume bianco.
### Gestione tabella
Il sottosettore è libero.

Oggetto nel sottosettore A (Azienda) con risalita al sottosettore '2' (Al bianco se manca o deviazione) con deviazione XX
### Ricerca tabella
Il sottosettore è XX, se inesistente assume bianco.
### Gestione tabella
Il sottosettore è libero.

Oggetto nel sottosettore A (Azienda) con risalita al sottosettore '3' (Assume oggetto, se manca bianco)
### Ricerca tabella
Il sottosettore è sempre quello ricevuto, se bianco viene assunto l'oggetto, se inesistente assume bianco.
### Gestione tabella
Il sottosettore è libero.
