## Contenuto
Il file V5STAT0F è un file estratto dagli archivi transazionali per analisi di tipo statistico sul ciclo attivo/passivo
I valori sono sommabili algebricamente, per cui una nota di accredito o uno sconto sono espressi con un valore negativo.
## Codice Oggetto (in TA/*CNTT)
 'V2'                               £FUNT1
 'V5STA'                               £FUNP1
## Chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida
N.A.

## Autorizzazioni
Classe LO.FLD per gestione autorizzazioni sui campi. Questa classe viene utilizzata in funzione dell'attributo "condizioni" specificato per ogni campo.

## Note strutturate (Tabella NSC)
N.A.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.


## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
V5STA05_U è il pgm EXIT utente per gestione personalizzata valori estrazione

## /COPY
N.A.

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
N.A.

## CONTENUTO DEI CAMPI
 :  : FLD D6TIPC **Livello**
Rappresenta la tipologia di statistica
I valori sono definiti da oggetto V2-V5STA
 :  : FLD D6TPRO **Livello**
Contiene il tipo protocollo contabile, composto da ttXXX+.+YY+'.'+ZZ     (Esempio FTVE1.09.01)
tt=FT, XXX=Registro IVA, YY=Anno, ZZ=Azienda
Solo per la ripresa Back-Log contiene il periodo di riferimento TAPER
 :  : FLD D6NPRO **Livello**
Contiene il Numero di Protocollo Contabile
Nel ciclo attivo corrisponde al Nr di Fattura.
 :  : FLD D6DPRO **Livello**
Il campo rappresenta valori diversi in relazione al tipo di statistica del record (D6TIPC)
Se AF/PF, contiene "Data protocollo Contabile"
Se AU/PE, contiene "Data fattura opp. Data bolla opp. Data documento V5"
Se AO/PO/AOT/AOC/POC, contiene "Data documento V5"
Se AB, contiene "Data periodo MPPIAN"
 :  : FLD D6ESPR **Livello**
Contiene l'esercizio relativo al campo Data Protocollo D6DPRO
 :  : FLD D6PEPR **Livello**
Contiene il periodo relativo al campo Data Protocollo D6DPRO
 :  : FLD D6ESCO **Livello**
Contiene l'esercizio di competenza contabile
 :  : FLD D6PECO **Livello**
Contiene il periodo di competenza contabile
 :  : FLD D6ARTI **Livello**
E' il codice articolo oggetto della riga (D6TPOG sarà di tipo 'AR')
 :  : FLD D6TPOG **Livello**
E' il tipo oggetto intestatario della riga
Può essere di tipo
- AR / TAV5S / ....... derivato dalle righe dei documenti V5
- E4, se la riga costituisce un'integrazione contabile da C5
- '**', se la riga rappresenta una quadratura contabile
 :  : FLD D6CDOG **Livello**
E' il codice oggetto intestatario della riga
 :  : FLD D6TPSP **Livello**
Nel caso di una riga di sconto/spesa/.., ne rappresenta il tipo (V2-TPSMS)
 :  : FLD D6CD01 **Livello**
I 10 campi liberi possono essere definiti in modo personalizzato con pgm B£EQRY_AOX
La loro valorizzazione può essere gestita attraverso il pgm di EXIT utente V5STA05_U
 :  : FLD D6NUM1 **Livello**
I 10 campi liberi possono essere definiti in modo personalizzato con pgm B£EQRY_AOX
La loro valorizzazione può essere gestita attraverso il pgm di EXIT utente V5STA05_U
 :  : FLD D6NUM9 **Livello**
Utilizzato come appoggio da pgm V5STA20, per ripartizione competenze
 :  : FLD D6NUM0 **Livello**
Salvato valore escluso da statistica per flag statistici V5 - vedi D6FL02
 :  : FLD D6DT01 **Livello**
Rappresenta la data di consegna del documento V5
Se R§DTCC>0 allora R§DTCC, altrimenti R§DTCR
 :  : FLD D6FL01 **Livello**
Assume valore '1' se il documento è una Nota di accredito
 :  : FLD D6FL02 **Livello**
D6FL02='1' , deriva da flag V5TDOC - T§FL02='9'  - da non integrare in statistica
i campi su V5STAT relativi a QTA' e VALORE sono uguali a ZERO
D6FL02='2' , deriva da flag V5RDOC - R§FL19='4'  - statistica solo valore
i campi su V5STAT relativi a QTA' sono uguali a ZERO
D6FL02='3' , deriva da flag V5RDOC - R§FL19='5'  - non genera statistiche
i campi su V5STAT relativi a QTA' e VALORE sono uguali a ZERO
D6FL02='4' , deriva da flag V5RDOC - R§FL19='6'  - statistica solo qtà
i campi su V5STAT relativi a VALORE sono uguali a ZERO
D6FL02='5' , deriva da flag V5RDOC - R§FL22='1'  - escludo da statistica
i campi su V5STAT relativi a QTA' e VALORE sono uguali a ZERO
I VALORE esclusi da statistica vengono salvati sul campo D6NUM0 del V5STAT per eventuali controlli.
 :  : FLD D6FL03 **Livello**
Se assume valore '1', significa che pgm V5STA20 ha effettuato ripartizione competenze
 :  : FLD D6FL04 **Livello**
Se assume valore '1', identifica record di fatturato contabilizzato per i quali non esiste registrazione E4
Valorizzato nel caso di tipo di ripresa GEC "Contabilizzato, No Registrazione"
