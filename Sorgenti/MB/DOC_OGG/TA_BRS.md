# BRS - Criteri di selezione
 :  : DEC T(ST) K(BRS)
## OBIETTIVI
 *     Descrivere un metodo da utilizzare nella scansione di distinta e ciclo per : 
 **    decidere se un componente/operazione è valido;
 **    modificare il contenuto di alcuni campi della riga in elaborazione per distinta/ciclo.
## SOTTOSETTORI
Non gestiti
## ESEMPI
1.   Utilizzare un tipo di scatola in funzione del primo carattere della configurazione;
2.   Modificare il tempo di lavorazione di un cilindro in funzione della sua lunghezza.
## NOTE TECNICHE
Si vuole permettere all'utente di scrivere, mediante un programma, nuovi criteri in aggiunta a quelli offerti da SMEUP.
Il programma deve avere una struttura di chiamata come quella di BRSCO_001.
_7_NB :  Per la simulazione utilizzare, se disponibile, la funzione TSTBRS.
## CONTENUTO DEI CAMPI
 :  : FLD T$BRSA **Programma specifico**
In questo campo si inserisce il nome del programma che implementa il criterio di selezione desiderato
 :  : FLD T$BRSB **Parametro del programma**
Campo libero che viene passato al programma per condizionarne l'esecuzione
