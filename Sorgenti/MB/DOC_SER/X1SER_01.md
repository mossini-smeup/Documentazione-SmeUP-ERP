 :  : HEA RESP(FD) STAT(10)
# OBIETTIVO
Gestire la visibilità (e in un secondo tempo la modifica) dei dati dell'agenda in LoocUp.

# FUNZIONI/METODI

## Funzione OPN
Fornisce una matrice contenente le date valide per la persona o per la commessa scelte.
Nell'Oggetto 1 questa funzione può ricevere un contatto (CN) o una commessa (CM);
nell'Oggetto 2 questa funzione può ricevere un periodo (elemento della TA PER);
Se l'Oggetto 2 non viene passato, come periodo di riferimento in entrambi i casi viene utilizzato
l'anno corrente.

## Funzione RCO
Fornisce una matrice contenente le ore per commessa per data.
Nell'Oggetto 1 questa funzione può ricevere un contatto (CN) o una commessa (CM) : 
passando il contatto si ottiene ogni commessa del contatto per il periodo passato (se passato)
spaccato per giorno;
passando la commessa si ottiene invece lo spaccato giornaliero suddiviso per collaboratore per il pe
riodo passato (se passato).
Nell'Oggetto 2 questa funzione può ricevere un periodo (elemento della TA PER).
Se l'Oggetto 2 non viene passato, come periodo di riferimento in entrambi i casi viene utilizzato
l'anno corrente.

## Funzione TCO
Fornisce una matrice contenente le totalizzazioni delle commesse raggruppate in base al tipo
commessa.
Nell'Oggetto 1 questa funzione può ricevere un contatto (CN) o una commessa (CM) : 
se utilizzo il contatto, ottengo le sue commesse totalizzate, mentre se utilizzo la commessa ottengo
il totale di ore per quella commessa, perdendo informazioni sul contatto.
Nell'Oggetto 2 questa funzione può ricevere un periodo (elemento della TA PER).
Se l'Oggetto 2 non viene passato, come periodo di riferimento in entrambi i casi viene utilizzato
l'anno corrente.


## Funzione RPE
Fornisce una matrice contenente le totalizzazioni per commessa per il periodo passato(se passato).
Nell'Oggetto 1 questa funzione può ricevere un contatto (CN) o una commessa (CM) : 
se utilizzo il contatto, ottengo le sue commesse totalizzate, mentre se utilizzo la commessa ottengo
il totale di ore per quella commessa, perdendo informazioni sul contatto.
Nell'Oggetto 2 questa funzione può ricevere un periodo (elemento della TA PER).
Se l'Oggetto 2 non viene passato, come periodo di riferimento in entrambi i casi viene utilizzato
l'anno corrente.

## Funzione AVA
Fornisce l'albero degli esercizi validi per commessa o contatto.
Nell'Oggetto 1 questa funzione può ricevere un contatto (CN) o una commessa (CM).

## Funzione MVA
Fornisce l'albero dei mesi validi per commessa o contatto.
Nell'Oggetto 1 questa funzione può ricevere un contatto (CN) o una commessa (CM).
Nell'Oggetto 2 questa funzione riceve un periodo (elemento della TA PER).
Se il periodo non viene passato viene impostato l'anno 2000, ma se nella lettura del file
la prima data è maggiore, il servizio non ritorna nulla.

## Funzione RPE_C
Non mi sembra possa funzionare...

## Funzione TCC
Come la funzione RPE a meno del fatto che la matrice costruita fornisce informazioni in più : 
tipo commessa e relativa descrizione, azienda commessa, codice ente, azienda collaboratore, codice
zona e realtiva descrizione, codice collaboratore e relativa descrizione.

## Funzione DTA
Fornisce una matrice contenente le diverse tipologie di ore per il periodo scelto, spaccato per gior
no. Per tipologia di Ore s'intende quelle presenti nella TA IGI£2 relative alle presenze.
Nell'Oggetto 1 questa funzione ricev un contatto (CN).
Nell'Oggetto 2 questa funzione riceve un periodo (elemento della TA PER).
Se l'Oggetto 2 non viene passato, come periodo di riferimento in entrambi i casi viene utilizzato
l'anno corrente.

## Funzione PER
Come la funzione DAT a meno del fatto che la matrice costruita fornisce il totale delle Ore presenze
## Funzione COM
Come la funzione DAT a meno del fatto che la matrice costruita fornisce il totale delle ore per
commessa inserite nella classificazione delle ore presenza.
## Funzione GAD
Gestione agenda del giorno.
### Metodo DAY
Ritorna una matrice contenente i dati relativi all'agenda per la data passata in Oggetto 1.
I valori riportati sono ovviamente solo quelli scritti sul file VERAPG0F, pertanto di chi non ha compilato l'agenda non comparirà neppure il record vuoto.

 :  : PRO.SER Cod="OPN.1" Tit="Periodi validi per Comm./Col.. " Fun="F(EXB;X1SER_01;OPN) 1(CN;COL;-(O;;CNCOL;Contatto\Commessa)) 2(TA;PER;-(F;;TAPER;Periodo))"

 :  : PRO.SER Cod="RCO.2" Tit="Commessa valide per Periodo. " Fun="F(EXB;X1SER_01;RCO)" Ref="OPN.1"

 :  : PRO.SER Cod="TCO.3" Tit="Totalizz.commesse per CN o CM\PER. " Fun="F(EXB;X1SER_01;TCO)" Ref="OPN.1"

 :  : PRO.SER Cod="RPE.4" Tit="Totalizz.commesse per CN o CM\PER. " Fun="F(EXB;X1SER_01;RPE)" Ref="OPN.1"

 :  : PRO.SER Cod="AVA.5" Tit="Reperimento anni validi. " Fun="F(TRE;X1SER_01;AVA) 1(CN;COL;-(O;;CNCOL;Contatto\Commessa))"

 :  : PRO.SER Cod="MVA.6" Tit="Reperimento mesi validi. " Fun="F(TRE;X1SER_01;MVA)" Ref="OPN.1"

 :  : PRO.SER Cod="TCC.7" Tit="Totali per commessa/collaboratore. " Fun="F(EXB;X1SER_01;TCC)" Ref="OPN.1"

 :  : PRO.SER Cod="DTA.8" Tit="Ore presenze per CN o CM \periodo. " Fun="F(EXB;X1SER_01;DTA)" Ref="OPN.1"

 :  : PRO.SER Cod="PER.9" Tit="Totali Ore presenze per CN o CM \periodo. " Fun="F(EXB;X1SER_01;PER)" Ref="OPN.1"

 :  : PRO.SER Cod="COM.10" Tit="Totali commesse per CN\Periodo. " Fun="F(EXB;X1SER_01;COM)" Ref="OPN.1"

 :  : PRO.SER Cod="GAD.DAY.11" Tit=". Agenda del giorno" Fun="F(EXB;X1SER_01;GAD.DAY) 1(D8;*YYMD;-(O;;D8*YYMD;Data))"

