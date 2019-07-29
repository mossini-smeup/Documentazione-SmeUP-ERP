# IGG - Metodi di aggregazione
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È il codice dell'elemento.
 :  : FLD T$DESC Descrizione
È la descrizione dell'indice.
 :  : FLD T$IGGA __SS Aggregazioni__
Identifica il subsettore della tabella IGR in cui sono catalogati i codici di aggregazione.
 :  : FLD T$G,1  __Codici Aggregazioni 1..9__
Sono elementi della tabella IGR con subsettore sopra referenziato. Indicano 9 possibili modi di totalizzazione/ordinamento dei report. I modi di aggregazione possono essere reperiti direttamente dal file statistico o come derivazione tramite OAV .
_9_Esempi di aggregazione : 
Cliente
Articolo
Agente
Classe materiale
Nazione
Commessa
Configurazione
Colore dei capelli del cliente
Etc.
I nove metodi di aggregazione possono essere incrociati a piacere anche tutti contemporaneamente.
 :  : FLD T$G,2.T$G,1 2° aggregazione
 :  : FLD T$G,3.T$G,1 2° aggregazione
 :  : FLD T$G,4.T$G,1 2° aggregazione
 :  : FLD T$G,5.T$G,1 2° aggregazione
 :  : FLD T$G,6.T$G,1 2° aggregazione
 :  : FLD T$G,7.T$G,1 2° aggregazione
 :  : FLD T$G,8.T$G,1 2° aggregazione
 :  : FLD T$G,9.T$G,1 2° aggregazione
 :  : FLD T$G,10.T$G,1 10° aggregazione
 :  : FLD T$G,11.T$G,1 11° aggregazione
 :  : FLD T$G,12.T$G,1 12° aggregazione
 :  : FLD T$G,13.T$G,1 13° aggregazione
 :  : FLD T$G,14.T$G,1 14° aggregazione
 :  : FLD T$G,15.T$G,1 15° aggregazione
 :  : FLD T$G,16.T$G,1 16° aggregazione
 :  : FLD T$G,17.T$G,1 17° aggregazione
 :  : FLD T$G,18.T$G,1 18° aggregazione
