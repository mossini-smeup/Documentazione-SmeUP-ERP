## Contenuto
Impegni materiali residui di un oggetto (al netto dei prelievi eseguiti).

## Codice Oggetto (in TA/*CNTT)
 'IT'                               £FUNT1

## Chiave primaria
 N.Relativo di record               £FUNK1
E' un oggetto "temporaneo" in quanto il sou identificativo non è permanente. Ad ogni rigenerazione degli impegni può variare.
Questa chave quindi può essere utilizzata per accedere all'oggetto (ed ai suoi attributi) ma non per collegarvi informazioni (note, parametri, ecc.. ).

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
La chiave primaria "Permanente" è : 
Q§TORI / Q§TDOC / Q§NDOC / Q§USR1 /Q§ARTI / Q§USR2 / Q§OPER

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle P5I (Impegni materiali) : 
 :  : DEC T(ST) K(P5I)

## Autorizzazioni
N.A.

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
E' possibile impostare in tabella P5I il suffisso x di un programma di aggiustamento P5FUIMT_x, che può modificare il contenuto del record prima della scrittura.
E' possibile impostare, sempre in tabella P5I, il suffisso x di un programma di aggiustamento P5FASIM_x, che permette di ripristinare campi del record tra una rifasatura e l'altra.

## /COPY
Interfaccia impegni materiali (£IIM) : 
 :  : DEC T(MB) P(QILEGEN) K(£IIM)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI
 :  : FLD Q§TORI Tipo origine
Viene ripreso il valore contenuto nell'elemento di tabella del tipo impegno materiali.
