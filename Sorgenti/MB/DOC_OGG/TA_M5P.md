# M5P - Guida rilascio m5 - p5
## OBIETTIVI
Descrivere le modalità con le quali viene eseguito il rilascio del consiglio di pianificazione, verso l'ambiente del ciclo interno. L'elemento di questa tabella va inserito, insieme con il programma di rilascio (M5PNP5_SM) nel parametro suggerimento della fonte pianificata, assegnata al consiglio tramite la politica di pianificazione.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$M5PA __Tipo ordine assunto__
È un elemento della tabella P5T :  se impostato definisce il tipo ordine che verrà assegnato all'ordine di produzione.
Questo valore , se presente, ha la precedenza su quello derivato dai parametri logistici.
 :  : FLD T$M5PB __Richiesta tipo ordine__
Se impostato, e se il rilascio è interattivo, verrà chiesto il tipo da assegnare all'ordine che verrà rilasclato.
 :  : FLD T$M5PC __Gestione commessa__
Se impostato, nell'applicazione suggerimento con variazioni, viene presentata la commessa con possibilità di modificarla.
 :  : FLD T$M5PD __N.Ordine produzione manuale__
Se impostato, nell'applicazione suggerimento con variazioni, è possibile impostare il numero dell'ordine di produzione che verrà scritto.
 :  : FLD T$M5PE __Passa a ordine__
Se impostato, nell'applicazione suggerimento, dopo che è stato scritto un ordine di produzione, si passa in modo automatico alla sua variazione
 :  : FLD T$M5PJ __Stato annullamento__
Se impostato definisce lo stato in cui viene posto l'ordine di produzione in caso di applicazione di un suggerimento di annullamento.
Se questo campo non è impostato, l'applicazione di un suggerimento di annullamento cancellerà fisicamente il record dell'ordine di produzione.
