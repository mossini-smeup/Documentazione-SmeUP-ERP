# Dichiarazione :  aspetti particolari

La dichiarazione di un'assegnazione deve scrivere il codice dell'esecutore assegnato nel campo F4AA01 - questo per permettere alla ricostruzione dello stato del WF di ricostruire l'utente esecutore corrente delle transizioini con assegnazione.
A standard : 
 * Scheda assegnazioni (WFLSTWRK, impegni assegnabili) : 
 ** WFSER_07 carica gli impegni assegnabili.
 ** WFSUP_02 esegue l'assegnazione : 
 *** chiede a WFUTE_01 quali utenti possono essere assegnati.
 *** chiama la WFA in ATT/ASS, passando il codice dell'utente che dovrà essere assegnato.
 *** la WFA in ATT/ASS passa per WFWFA0_DA -> WFWFA0_LA -> WFATT_01, che scrive il F4AA01

Per un esempio delle varie modalità di assegnazione fare riferimento al WF ESE_004.
