## Contenuto
Dati informativi e classificazioni degli enti esterni con cui l'azienda viene in contatto.
Ogni contatto appartiene ad un tipo (tabella BRE) che lo caratterizza (ad esempio clienti, fornitori, concorrenti, probabili clienti, ecc..).

## Codice Oggetto (in TA/*CNTT)
 'CN'                               £FUNT1
 'Tipo ente' (TA/BRE)	  £FUNP1

## Chiave primaria
E§TRAG - E§AZIE - E§CRAG - E§SCEN - E§DINV - E§DFNV - E§IDOJ

## Ulteriore chiave primaria
E§IDOJ

## Altri condizionamenti facoltativi in ricerca

## Tabella guida

## Autorizzazioni
La classe di autorizzazione è BREN01.
La funzione di autorizzazione dipende dal programma in cui si esegue il controllo : 
 * Nel formato guida (BREN01G) è il tipo dell'ente.
 * Nelle liste è costruita in questo modo :  BREN01xxxY, dove xxx è il tipo ente, mentre Y è il suffisso del programma di lista, rispettivamente ' '/'A'/'L', per le tre modalità : 
 ** BREN01L   -    Lista richiamata dal formato guida.
 ** BRAEN1LA  -    Lista richiamata dalla ricerca. Se si vuol permettere la manutenzione dalla ricerca (inserimento, variazione) si autorizza questa funzione.
 ** BRAEN1LT  -    Lista richiamata dalla parzializzazione : abilitare solo la scelta, ed eventualmente il dettaglio.

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella BRE. Se non inserito si assume CON.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella BRZ.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-CNyyy, dove yyy è il tipo ente; se assente viene associato il flusso x-CN.

## Costruzione automatica campi (tabella B£C)
La struttura della matrice risultante quando è attivata la funzione di costruzione campo è la seguente : 
>Descrizione                    Riga £SC Da  A
Codice Ente                        1    01  15
Tipo Ente                          1    16  18
Descrizione Ente                   2    01  35
Categoria Ente                     2    36  39


## Presenza monitor - visualizzatore
....

## Programmi di controllo
....

## /COPY
Funzioni informazioni ENTI  £BRI : 
 :  : DEC T(MB) P(QILEGEN) K(£BRI)

## Gruppi flag
Da Categoria enti (TA/BRZ).

## Workflow e popup
Sensibile alla nuova gestione popup, se attivata in B£2.

## Note particolari

## CONTENUTO DEI CAMPI
 :  : FLD E§LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella BRZ.
Se non codificato, si assume il livello 2.

 :  : FLD E§STAT **Stato**
In inserimento si deriva il primo stato valido del livello determinato.
jkljkl
