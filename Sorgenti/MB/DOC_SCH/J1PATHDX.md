# Help  J1PATDIR_X

Obiettivo :  presentare una sottoscheda di gestione di una cartella, il cui percorso è definibile mediante variabili statiche e di SCP_CLO.
In questa sottoscheda vengono presentati : 
 * Il percorso calcolato.
 * Una sezione di gestione risorse sul percorso.
 * Un bottone per creare la cartella, se non è presente.
 * Un bottone per tornare alla cartella qualora si navighi in sue sottocartelle.
Questa scheda può gestire correttamente i dinamismi anche in presenza di più istanze di essa aperte contemporaneamente, provvisto che i richiami siano differenziati mediante chiamate con NUM diverso.

## Parametri in input

 * PA.VAR - variabile OPZIONALE contenente percorso base (di solito in in SCP_CLO/DEFAULT).
 * PA.NUM - numero per rendere univoche le sezioni in schede con più sottoschede di allegati; serve per la correttezza dei dinamismi dopo la creazione delle directory.
 * OG.K1  - parte finale del percorso se c'è &PA.VAR, altrimenti è il percorso completo.

## Attenzione!!!

Se OG.K1 è più lungo di 15 non funziona - non risolve la variabile!!!

## Esempi di richiamo

 * F(EXD;*SCO;) 1(AR;;&OG.K1) 2(MB;SCP_SCH;J1PATHDIRX) P(VAR(*DIRART))
  * chiamato ad esempio come sottoscheda della scheda articolo, dove : 
  * *DIRART è una variabile definita in SCP_CLO, ad esempio \\server\articoli
  * dato l'articolo A01 il percorso gestito è \\server\articoli\A01
 * F(EXD;*SCO;) 1(J1;PATHFILE;C : \prova) 2(MB;SCP_SCH;J1PATHDIRX)
  * in questo caso viene gestito direttamente il percorso C : \prova
 * F(EXD;*SCO;) 1(J1;PATHFILE;C : \prova) 2(MB;SCP_SCH;J1PATHDIRX) P(NUM(1)) e F(EXD;*SCO;) 1(J1;PATHFILE;C : \prova) 2(MB;SCP_SCH;J1PATHDIRX) P(NUM(2)) se possono essere chiamate insieme, altrimenti i dinamismi di una scheda si incrociano con quelli dell'altra.
