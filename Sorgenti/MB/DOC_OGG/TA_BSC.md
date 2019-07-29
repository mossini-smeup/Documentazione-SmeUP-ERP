# BSA - Modo reperimento calendario
 :  : DEC T(ST) K(BSC)
## OBIETTIVI
-    Specifica il modo di reperimento del calendario di un oggetto, come disponibilità nel tempo
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$BSCA **Origine**
Definisce il luogo in cui vengono reperite le informazioni.
 :  : FLD T$BSCB **Tipo risorsa**
È un elemento della tabella TRG. Va impostato se il calendario è reperito dal calendario della risorsa o dal calendario della squadra.
 :  : FLD T$BSCC **Gruppo fonti**
Va impostato se il calendario è reperito dalla disponibilità.
 :  : FLD T$BSCD **Suff.pgm.**
Va impostato se il calendario è reperito da un programma specifico.
Il programma utilizzato è BRFUCAL_x (dove x è questo suffisso).
 :  : FLD T$BSCE **Par.pgm.**
E' un parametro di caratterizzazione del programma precedente.
 :  : FLD T$BSCF **Ora disponibilità**
Va impostato se il calendario è reperito dalla disponibilità.
Dato che gli eventi della disponibilità sono caratterizzati solo dalla data, mentre nella schedulazione essi vengono confrontati con eventi in cui è specificata anche l'ora, con questo campo si imposta l'ora "assunta" per questi eventi.
 ' '  - vengono datati al mattimo (ora 0) gil impegni, ed alla sera (ora 24) le coperture
 'A'  - vengono datati al mattimo (ora 0) sia gli impegni sia le coperture
 'B'  - vengono datati alla sera (ora 24) sia gli impegni sia le coperture
 'C'  - vengono datati alla sera (ora 24) gil impegni, ed al mattino (ora 0) le coperture
