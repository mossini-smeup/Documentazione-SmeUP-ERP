 :  : HEA RESP(GIAGIU) STAT(10)
# OBIETTIVO
Analizza i log della conversione

# FUNZIONI E METODI
## COM Componenti
Costruisce una matrice in cui sono evidenziati per macro aree (OS,IL,DB) errori e warning in formato torta
## APP Applicazione
Costruisce una matrice in cui sono evidenziati per database e per linguaggio errori e warning in formato torta suddivise per applicazione
## OGG Dettaglio per oggetto
Costruisce una matrice in cui sono presenti gli oggetti convertiti (una sola volta in distinct) ed è evidenaziata tramite flag la presenza di errori e warning
## PIP Torta messaggi applicazioni modulo
Costruisce un grafico in cui vengono evidenziati i messaggi con gravità > 0
## DET Dettaglio
Costruisce una matrice di dettaglio massimo per gli oggetti convertiti
## TRE Albero oggetti sistema
Costruisce un albero per gli oggetti di sistema e lo posiziona nel mnu del moduo MUBASE (riservato)
## CNT Conteggio
Costruisce un grafico in cui è evidenziata la distribuzione delgi oggetti convertiti

# OGGETTI COLLEGATI
 :  : PRO.SER Cod="COM.1" Tit="Analisi componente " Fun="F(EXB;MUSER_01;COM)           P(LIBR(-(F;;OJ*LIB;Libreria)))"

 :  : PRO.SER Cod="PIP.2" Tit="Analisi OS" Fun="F(EXB;MUSER_01;PIP) 1(OG;OJ;-(O;;OGOJ;Oggetto))        3(;;-(F;;;OS/DB/IL))        P(LIBR(-(F;;OJ*LIB;Libreria)))"

 :  : PRO.SER Cod="PIP.3" Tit="Analisi DB" Fun="F(EXB;MUSER_01;PIP) 1(OG;OJ;-(O;;OGOJ;Oggetto))        3(;;-(F;;;OS/DB/IL))        P(LIBR(-(F;;OJ*LIB;Libreria)))"

 :  : PRO.SER Cod="PIP.4" Tit="Analisi IL" Fun="F(EXB;MUSER_01;PIP) 1(OG;OJ;-(O;;OGOJ;Oggetto))        3(;;-(F;;;OS/DB/IL))        P(LIBR(-(F;;OJ*LIB;Libreria)))"

 :  : PRO.SER Cod="DET.5" Tit="Dettaglio oggetto" Fun="F(EXB;MUSER_01;DET)                   1(OG;OJ;-(O;;OGOJ;Oggetto))                2(TA;B£A;-(O;;TAB£A;Applicaziione))        3(;;-(F;;;OS/DB/IL))                       P(                                         LIBR(-(F;;OJ*LIB;Libreria))                OGGE(-(F;;OJ*PGM;Oggetto))                 MESS(-(F;;OJ*MSGD;Messaggio))              )"

 :  : PRO.SER Cod="APP.6" Tit="Analisi per applicazione"                             Fun="F(EXB;MUSER_01;APP)                   1(OJ;*FILE;-(O;;OJ*FILE;File))             3(;;-(F;;;OS/DB/IL))                       P(                                         LIBR(-(F;;OJ*LIB;Libreria))                )"

 :  : PRO.SER Cod="OGG.7" Tit="Oggetti dell'applicazione"                Fun="F(EXB;MUSER_01;OGG)                   1(OG;OJ;-(O;;OJ*FILE;Oggetto))             2(TA;B£A;-(O;;TAB£A;Applicaziione))        3(;;-(F;;;OS/DB/IL))                       P(                                         LIBR(-(F;;OJ*LIB;Libreria))                )"
