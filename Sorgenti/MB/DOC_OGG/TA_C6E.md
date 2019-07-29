# C6E - Fonti esistenti disp.finanz.
 :  : DEC T(ST) K(C6E)
## OBIETTIVO
Definisce le caratteristiche delle fonti esistenti nelle analisi di disponibilità finanziaria.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il codice della fonte.
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$C6EA **Origine Fonte**
È un elemento V2/C5OFP, che definisce la natura della fonte.
 :  : FLD T$C6EB **Parametro 1/2 Fonte**
Assumono un significato diverso in funzione dell'origine fonte : 
_Se l'origine è AP (altra applicazione)  : _
Il primo parametro è la sigla del'applicazione (elemento della tabella '*CNAA').
Il secondo parametro è controllato dal programma specifico B£TC6E_xx, dove xx è la sigla dell'applicazione.
_Se l'origine è UT (fonte utente)  : _
Sono un programma ed un parametro di condizionamento, per interfacciare fonti esterne a SMEUP.
 :  : FLD T$C6EE.T$C6EB **Parametro 1/2 Fonte**
 :  : FLD T$C6EC **Azione fonte (+/-/N)**
Definisce se il contributo della fonte è positivo, negativo oppure neutro per la disponibilità.
 :  : FLD T$C6ED **Ordinamento fonte**
È un carattere che stabilisce, nell'ambito delle fonti esistenti, la posizione in cui verrà esposta.
 :  : FLD T$C6EF **Presenta anche se 0**
Se impostato, mostra la riga della fonte anche se con valore zero.
 :  : FLD T$C6EG **Descrizione ridotta**
È la descrizione che può essere usata nei casi di rappresentazioni compatte.
 :  : FLD T$C6EI **Suffisso programma aggiustamento**
Se impostato, è il suffisso x del programma C5C6D0G_x, che viene lanciato all'atto della scrittura di questo tipo, per modificarne il comportamento.
 :  : FLD T$C6EL **Riclassifica**
È un elemento della tabella 'C5*RF' :  viene usato nell'analisi disponibilità riepilogata. Se impostato, verranno raggruppate per questo campo. Se non impostato verrà assunta come riclassifica l'azione fonte della stessa tabella.
 :  : FLD T$C6EM **Ordinamento riclassifica**
È usato nelle analisi disponibilità riepilogata :  all'interno della riclassifica impostata nel campo fonti, verranno presentate ordinate per questo campo. Se non impostato verrà assunto come ordinamento fonte.
