# OBIETTIVO
 Superare il limite strutturale della MDV estendendo il buffer di scrittura a 30 Kb.

## Struttura
 Tutte le informazioni saranno identificate tramite due caratteristiche principali : 
 1) La struttura, questa definisce la modalità di presentazione delle informazioni
 2) Il contesto, il contesto è paragonabile al sottosettore di una tabella, lega le informazioni d i una stessa struttura a eventi diversi.
 Se non ricevuta la struttura ed il contesto, si assume sia una MDV viene quindi assunto : 
 - Struttura :  STR.MDV
 - Contesto  :  <nome del programma>
 Se non ricevuto l'utente si assume l'utente di sistema.

# FUNZIONI / METODI
-**"GES"** Gestione memorizzazione Video
  Gestisce le memorizzazioni video dell'utente richiesto, di qualsiasi struttura.
  -**"WRI"** in Scrittura
  -**"LET"** in Lettura
  -**"DEL"** in Cancellazione (Esclusa struttura RE)
  -**"RIC"** in Ricerca
  -**"   "** in Gestione (Ricerca o lettura)

  INPUT :  £MDEST -> Struttura delle informazioni.
         £MDECO -> Contesto di memorizzazione
         £MDENM -> Nome della memorizzazione
         £MDEUS -> Utente della memorizzazione, "**" per renderlo pubblico,
                                                "**+Gruppo" per condividerlo al proprio gruppo
         £MDEIM -> Buffer di scrittura o lettura
         £MDE35 -> *ON se errore in lettura o scriuttura

-**"MDV"** Gestione memorizzazione Video di stato.
  Questa funzione nasce per sostituire in maniera veloce la vecchia £MDV. Se chiamata senza metodo
  assume lettura e alla successiva chiamata scrittura.
  NOTA BENE : 
  Il Nome della memorizzazione assunto è *LAST e non è modificabile
  -**"WRI"** Scrivi *LAST
  -**"LET"** Leggi  *LAST dell'utente del job del suo gruppo utente o dell'utente **
  -**"LEU"** Leggi  *LAST di un qualsiasi utente
  INPUT :  £MDEST -> Struttura delle informazioni, lasciare vuoto oppure sovrascrivere il default.
         £MDECO -> Contesto di memorizzazione,   lasciare vuoto oppure sovrascrivere il default.
         £MDENM -> Nome della memorizzazione,    viene sempre assunto *LAST.
         £MDEUS -> Utente della memorizzazione   lasciare vuoto oppure sovrascrivere il default.
                   (solo se il metodo non è LET)
         £MDEIM -> Buffer di scrittura o lettura
         £MDE35 -> *ON se errore in lettura o scriuttura
