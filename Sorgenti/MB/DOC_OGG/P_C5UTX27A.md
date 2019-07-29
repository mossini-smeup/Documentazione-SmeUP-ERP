# Adeguamento V§N

Vengono aggiornati gli elementi della V§N corrispondenti ai paesi della black list in due parametri : 
* Appartenenza black list
* Codice nazione csv, cioè la codifica utilizzata per la trasmissione dei dati della black list

Vengono aggiornati tutti i paesi determinati dai decreti del Ministro delle finanze 4/05/1999 e del  Ministro delleconomia e delle finanze 21/11/2001, ad esclusione di quelli con limiti soggettivi ed oggettivi previsti dall'art. 3 del secondo decreto. Questi qual'ora si rientri nella casistica dovranno essere rettificati manualmente.

# Adeguamento Numeratore C5MBLA0F

Nel sottosettore della CRNC5 viene generato l'elemento OG.C5MBLA che servirà per numerare i movimenti delle  operazioni di black list.

# Definizione Classe d'Autorizzazione C5MB01G

Viene automaticamente generata l'elemento della B£P C5MB01G, per la gestione dei movimenti delle operazioni di black list.

# Valori Classe d'Autorizzazione C5MB01G

Vengono automaticamente generate le autorizzazioni della classe C5MB01G a partire da quelle della classe C5E401G (gestione registrazioni).

# Ricostruzione OAV CN

Viene lanciata la ricostruzione degli attributi di base ed intrinseci dell'oggetto CN, al fine creare l'OAV J/G05, che permette di individuare i soggetti appartenenti ad una nazione black list.
Questa azione è propedeuita al punto successivo.

# Costruzione liste BLACKL

Crea in automatico per i tipi contatto CLI e FOR un lista basata sull'oav del punto precedente, avente per per codice BLACKL.

