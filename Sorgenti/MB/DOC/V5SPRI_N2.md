# Struttura accantonamento V5
Tutte le funzioni (gestione / visualizzazione / ritorno quantità) sono gestite dalla £GMR, a cui si passano le seguenti chiavi : 

 * **£FUNK1**, tipo origine (DO/OR)
 * **£FUNK2**, tipo documento
 * **£FUNK3**, numero documento
 * **£FUNK4**, riga / sequenza 1
 * **£FUNK5**, riga / sequenza 2
 * **£FUNK6**, fase
(Vedi impostazioni chiavi GMRRIM, in Doc. Applicativo GMRRIM).

In particolare per il DO (gestione accantonamento su righe documenti) l'accantonamento è guidato dalla tabella V55 / elemento = tipo documento.

Verrà creata una riga di richiesta di movimentazione per ogni gruppo di chiavi (es. lotto, lotto/ubicazione, lotto/cliente, ....) con la qtà richiesta e la sospesa (nella U.M. esterna)
Ricordare di impostare in tab. GM1 il numeratore di idnetificativo riga che è la key unique del GMRRIM.
