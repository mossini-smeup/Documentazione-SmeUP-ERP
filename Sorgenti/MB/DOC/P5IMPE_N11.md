# Costruzione impegni materiali su documento
La routine che gestisce questa scansione è la £DIB con modalità "DD" che lancia il programma B£IDIBD.

Il caso di scansione logistica (materiali alla fase) serve per il C/Lavoro di fase, la routine da lanciare è la £CIRDB in modalità "MF"/"DF".
A questa routine bisogna passare il tipo ordine, da cui si derivano tipo distinta e tipo ciclo origine. In assenza di esso (è il caso del C/Lavoro di fase in cui manca il tipo ordine), bisogna passare __esplicitamente__ il tipo distinta e il tipo ciclo (che sono presenti nel tipo impegno). Se non si vuole passare il tipo ciclo, perchè non si vuole avere l'assieme alla fase precedente, il sistema implicitamente scandirà il tipo ciclo "ART" per posizionare correttamente le fasi.
