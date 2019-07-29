# Obiettivi
A ciascun ente si possono associare tante altre informazioni oltre a quelle previste nei campi dell'anagrafico.

Questo programma permette la gestione di un gruppo di queste informazioni, di cui elenchiamo la lista : 
 * £01 Indirizzi di spedizione
 * £02 Indirizzi di contabilizzazione
 * £03 Indirizzi di conferma
 * £04 Indirizzi di tratt. prezzo
 * £05 Indirizzi di corrispondenza
 * £06 Indirizzi di vettore
 * £07 Modelli ammessi
 * £08 Param. fatturazione
 * £09 Partite IVA
 * £10 HOME PAGE INTERNET
 * £11 Documenti/Allegati specifici
 * £12 Percorsi validi
 * £13 Lettere di esenzione
 * £14 Dati specifici per modello
 * £15 Vettori e Agenti Aggiuntivi
 * £16 Indirizzi E-MAIL
 * £17 Contropartite contabili
 * £18 Numero R.I.D.
 * £19 Indirizzi alternativi Riba
 * £20 Calendario alternativo
 * £21 Coordinate bancarie
 * £22 Piano campionamento forzato
 * £23 Livello camp. forzato
 * £24 C.F.It.per non resid. mod. 770
 * £25 MSN messenger
 * £26 S.I.P.
 * £27 Indirizzo IP
 * £28 Skype
 * £29 Matricola Enasarco
 * £31 Tipo Ente Cessione

Queste tipolige di informazioni sono contenute nella tabella BRI (Tipi estensioni contatti) in cui sono anche richiamati i programmi specifici di utilizzo.
 :  : DEC T(ST) K(BRI)

# Gestione
Il programma per il lancio della manutenzione di queste informazioni può essere richiamato dalla gestione enti ( "8 Informazioni ente"  oppure "F7 Inserimento estensioni"), a seconda del tipo di data entry utilizzato) oppure lanciato dal suo formato guida.
Le modalità di gestione sono comuni a tutte queste tipologie di informazione, per comodità descriveremo l'utilizzo del tipo informazione £16 = Indirizzi E-Mail.

## Formato guida
![BRENTI_019](http://localhost:3000/immagini/MBDOC_OGG-P_BRES01/BRENTI_019.png)
La gestione si attiva aprendo la opportuna chiave di menù e inserendo : 
 * un tipo ente / codice ente a cui associare informazioni aggiuntive
 * il tipo informazione aggiuntiva (in questo caso £16)
 * un identificativo (può essere un valore di default "**" oppure un propgressivo qualsiasi :  il suo utilizzo è quello di differenziare più contati all'interno della stessa funzione aziendale)

Con l'opzione 01 e premendo INVIO si presenta il seguente formato di passaggio dove è possibile inserire la funzione aziendale di riferimento ed uno stato del contatto : 
![BRENTI_020](http://localhost:3000/immagini/MBDOC_OGG-P_BRES01/BRENTI_020.png)
Le funzioni aziendali sono codificate nella tabella V£F
 :  : DEC T(ST) K(V£F)

Dopo aver inserito lo stato e dato un successivo INVIO si presenta il formato di input vero e proprio : 
![BRENTI_021](http://localhost:3000/immagini/MBDOC_OGG-P_BRES01/BRENTI_021.png)