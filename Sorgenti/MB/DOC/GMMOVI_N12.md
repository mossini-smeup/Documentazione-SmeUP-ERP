# Modalità trattamento recuperi di produzione
Devono avere __sempre__ come tipo impegno "PP".
Per quanto riguarda il segno : 
 * se è impostata espressamente nel campo causale di recupero (prima nel tipo impegno, poi nei parametri logistici - campo causale di recupero), deve essere "+"
 * se invece è la causale normale di prelievo, i segno deve essere "-". In questo secondo caso la quantità del movimento è negativa (e l'effetto sulla giacenza positivo).

Nel programma di prelievo manuale (P5FUIML), si digita __sempre__ una quantità positiva. è il programma che eventualmente cambia il segno alla qtà del movimento se è un recupero eseguito con una casuale di prelievo.
