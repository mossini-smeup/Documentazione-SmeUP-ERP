# GESTIONE UNITA' DI MISURA ALTERNATIVE
Questa funzione si propone di unificare il modo di presentare, controllare e convertire le quantità in presenza di
unità di misura alternativa.
# FUNZIONI
-    01 - Det. quantità gestite
Riceve il metodo, l'oggetto (tipo griglia e oggetto), il contatto (tipo e codice), l'unità di misura interna e
esterna.
Ritorna i 3 valori di ammessa immissione (O=Obbligatoria, F=Facoltativa, P=Protetta) rispettivamente per la quantità
in unità di misura interna, esterna e per il fattore di conversione.
-    02 - Calcolo quantità
Riceve il metodo, l'oggetto (tipo griglia e oggetto), il contatto (tipo e codice), l'unità di misura interna e
esterna, i 3 valori di ammessa immissione, le 3 quantità.
Se non ha ricevuto tutte le quantità, ritorna le quantità non ricevute, in caso contrario controlla la loro
congruenza, e segnala l'eventuale squadratura con un opportuno codice di ritorno.
# METODO DI COSTRUZIONE
Tramite questo parametro si rende noto alla funzione il punto in cui essa è chiamata (inserimento documento,
entrata/uscita, movimentazione di magazzino, ...)
# TIPO GRIGLIA / CODICE OGGETTO
Individua l'oggetto (tipo e codice) di cui si sta trattando la quantità.
# TIPO CONTATTO / CODICE CONTATTO
Individua l'ente esterno (tipo e codice) con cui si sta trattando.
# QUANTITÀ 1
E' la quantità espressa nell'unità di misura interna.
# UM INTERNA
E' l'unità di misura in cui l'azienda tratta le quantità relative all'oggetto in esame nella sua attività interna.
# QUANTITÀ 2
E' la quantità espressa nell'unità di misura esterna.
# UM ESTERNA
E' l'unità di misura in cui l'azienda tratta le quantità relative all'oggetto in esame nei rapporti con enti esterni.
# FATTORE DI CONVERSIONE 3
E' il fattore di conversione tra le quantità 1 e 2.
Attenzione :  non è stabilito a priori se è dato dalla divisione della quantità interna per quella esterna o viceversa,
ma dipende dalle unità di misura in gioco.
# AMMESSA IMMISSIONE 1/2/3
Stabilisce il modo di gestire le quantità :  per maggiori particolari vedi la descrizione delle funzioni.
