 :  : HEA RESP(LS) STAT(80)
## OBIETTIVO
Riunire le funzioni di ricerca informazioni nella documentazione. Pur essendo nato per ricercare nella documentazione, il servizio consente di trovare in modo analogo all'interno di qualsiasi file. In funzione delle impostazioni fornisce tutti i membri che contengono una stringa.
 T(Possiamo ad esempio trovare risposte alle seguenti domande : )
- Membri del file BRSRC nella libreria SMEDEV che contengono "£IFCON"
- SCRIPT di scheda il cui nome inizia con LO e contengono la parola "ESEMPIO" oppura "PROVA"
- Tutti i documenti in cui si parla di "AUTORIZZAZIONI"

Almeno in parte questo servizio risolve in modo interattivo le funzioni di ricerca per le quali utilizziamo "UP SCA"
In particolare potremo avere come risposta la lista dei membri oppure l'insieme di tutte le righe che soddisfano la condizione sul contenuto

## FUNZIONI/METODI
### Impostazioni
Dopo aver definito libreria e file all'interno di questa, posso indicare vincoli sul contenuto del nome, del tipo e della descrizione del membro. Tali limiti sono consigliati (se conosciuti) per velocizzare la ricerca in quanto se non sono soddisfatte tali condizioni il membro non viene aperto.
Sul contenuto (e solo su questo) sono attive anche le condizioni di "OR" oppre "AND". Tali condizioni si possono indicare in alternativa e non sono gestite le parentesi. Se si vuole ricercare una stringa composta da più parole, questa va posta fra apici.

### Ricerca documenti
Quando un documento soddisfa le condizioni, la scansione si ferma e si aggiunge una riga nella lista dei membri.

### Matrice delle righe
Il contenuto di ogni riga che soddisfa le condizioni viene posta in matrice.

## Metodi di richiamo
Abitualmente le variabili sono gestite da una sezione di impostazioni. E' possibile anche passare le variabili all'interno del parametro di funzione come descritto di seguito. Avremo pertanto che F(EXB;LOSER_o4;RIC.RIG) 1(OJ;*FILE;DOC) 2(PJ;*LIB;SMEDEV) P(FUL(Esempio)) ricerca tutte le righe di documentazione dove si trova la parola "esempio"

## Sviluppi previsti
 :  : PAR L(LET)
- Estendere le funzioni di ricerca gestendo parentesi, liste, range ecc
- Portare su tutti i campi (per esempio descrizione) le ricerche estese di cui sopra
- Gestire ricerca in liste di files oppure un file in tutte le librerie ecc( simil UP SCA)


 :  : PRO.SER Cod="IMP.ORI.1" Tit="Impostazioni. Matrice origine" Fun="F(EXB;LOSER_04;IMP.ORI)"

 :  : PRO.SER Cod="IMP.UPD.2" Tit="Impostazioni. Aggiornamento" Fun="F(EXB;LOSER_04;IMP.UPD)"

 :  : PRO.SER Cod="RIC.MBR.3" Tit="Ricerca. Membri" Fun="F(EXB;LOSER_04;RIC.MBR) 1(OJ;*FILE;-(F;;OJ*FILE;FILE)) 2(OJ;*LIB;-(F;;OJ*LIB;LIBRERIA)) P( NAM(-(F;;**;Nel nome)) TIP(-(F;;**;Nel tipo)) DES(-(F;;**;Nel testo)) FUL(-(F;;**;Nel contenuto)))"

 :  : PRO.SER Cod="RIC.RIG.4" Tit="Ricerca. Righe nei membri" Fun="F(EXB;LOSER_04;RIC.RIG)" Ref="RIC.MBR.3"

 :  : PRO.SER Cod="PRE.VAR.5" Tit="Presentazione. Stato variabili" Fun="F(TRE;LOSER_04;PRE.VAR)"

