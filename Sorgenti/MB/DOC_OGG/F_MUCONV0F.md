 :  : DEC T(OJ)  P(*FILE) K(MUCONV0F)
## Contenuto
File conversione oggetti AS.UP

## Codice Oggetto (in TA/*CNTT)
N.A.

## Chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
MULIBR - Libreria
MUTIPO - Tipo
MUOGGE - Oggetto
MUSTAT - Stato

## Tabella guida
La tabella di riferimento è la MU1(Personalizzazioni MULT).

## /COPY
Funzione di conversione (£MUC) : 
 :  : DEC T(MB) P(QILEGEN) K(£MUC)

## Comandi Correlati
MU - Conversione sorgente
 :  : DEC T(OJ)  P(*CMD) K(MUOS02C)

## Note particolari
Il MUCONV è un file di log in cui vengono scritte tutte le informazioni interessanti
riguardanti l'oggetto che si sta convertendo. Oltre la registrazione dell'avvenuta esportazione
vengono registrati anche messaggi di gravità 20 (warning) o 30 (error)
riguardanti funzioni non supportate o comunque cose che richiedono attenzione.

## CONTENUTO DEI CAMPI

 :  : FLD MUCONT
Contesto conversione.
Tale campo è concepito per avere a disposizioni più scenari di conversione

 :  : FLD MULIBR
Libreria dell'oggetto convertito

 :  : FLD MUTIPO
Tipo dell'oggetto convertito

 :  : FLD MUOGGE
Tipo dell'oggetto convertito

 :  : FLD MUATTR
Attributo dell'oggetto convertito (RPGLE,CLLE,PF,LE,etc.)

 :  : FLD MUAPPL
Applicazione Sme.Up alla quale fa riferimento l'oggetto converito

 :  : FLD MUMODU
Modulo Sme.Up al quale fa riferimento l'oggetto converito

 :  : FLD MULIVE
In esportazione il livello assunto è 2.

 :  : FLD MUSTAT
In esportazione lo stato assunto è 00.

 :  : FLD MUGRAV
Gravità del messaggio : 
- 00=Ok;
- 20=Warning;
- 30=Error;

 :  : FLD MUMESS
Codice riferimento messaggio dal file messaggi MSGMU

 :  : FLD MUINFO
Testo del messaggio MUMESS con la decodifica delle variabili

 :  : FLD MUFILE
File sorgente dell'oggetto convertito

 :  : FLD MUMEMB
Nome membro sorgente dell'oggetto convertito

 :  : FLD MUFL01
V2 SI/NO se il programma è considerato exit.
La ricerca delle caratteristiche di exit è descritta nel pgm MUUT01
 :  : DEC T(OJ)  P(*PGM) K(MUUT01)

 :  : FLD MUFL02
V2 SI/NO se il programma è una replica.
La ricerca delle caratteristiche di exit è descritta nel pgm MUUT03
 :  : DEC T(OJ)  P(*PGM) K(MUUT03)
