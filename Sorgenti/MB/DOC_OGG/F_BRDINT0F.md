## Contenuto
Record relativi alle dichiarazioni d'intento emesse (verso i fornitori) e ricevute (dai clienti). Con date e riferimenti caratteristici.

## Codice Oggetto (in TA/*CNTT)
Nessuno.

## Chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria

## Autorizzazioni
Classi autorizzazione BRIN01G.

## Note strutturate (Tabella NSC)
 Il contenitore si assume dal parametro AWA della categoria £CA dell'azienda.
 Chiave 1  - OJ*FILE (BRDINT0F)
 Chiave 2  - ** (D§IDOJ)
 Chiave 3 -  N.A.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
 Vengono richiamati i flussi di modifica enti ??????

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
N.A.

## /COPY
Funzioni Dichiarazioni d'Intento BRN : 
 :  : DEC T(MB) P(QILEGEN) K(£BRN).

## Gruppi flag

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI
NO!!  La documentazione dei flag va messa nel pgm del flaggatore.
 :  : FLD D§TDIC**Tipo dichiarazione**
 1 = Singola, 2 = Fino a concorrenza importo, 3 = Di un periodo.
 :  : FLD D§FL01**Registro**
 1 = Emesse (Fornitore), 2 = Ricevute (Cliente).
