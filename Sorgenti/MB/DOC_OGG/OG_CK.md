 Ogni controllo eseguito nella £K89 deve essere oggettizzato (con un codice univoco).
 I codici controllo devono essere univoci per tipo oggetto.
 I codici dei controlli standard devono cominciare con S , mentre i controlli utente con X .
 (Ad esempio non posso definire un codice X00001 per CNCLI e un altro con
 lo stesso codice per CNFOR, mentre posso definire X00001 per CM e CN o per CM e CNCLI).
 Un codice controllo non è riutilizzabile, come un codice messaggio. E' legato al singolo
 controllo sul singolo campo.
 (ad esempio :  il controllo di obbligatorietà di E§TRAG è diverso sia dal controllo
 che il valore del campo E§TRAG sia valido sia dal controllo di obbligatorietà di A§ARTI.

## Interfaccia
 L'interfaccia dell'oggetto Controllo (CK) è la £ICK.

## Codifica controlli

 * Controlli dinamici. Generati a runtime a partire dagli OAV dell'oggetto (tipo + parametro).
 ** Codifica G00001 per oggettizzazione errata, G00002 per obbligatorietà, G00003     per valore non valido, G00004 per valore non congruente rispetto alle ricerche condizionate.
    Definiti nello script B£K89G in DOC_VOC.
 * Controlli standard. Definiti nello script B£K89_xx in DOC_VOC.
 ** Codifica **S**+progressivo
 * Controlli utente. Vanno codificati nello script B£K89_xxU in DOC_VOC.
 ** Codifica **X**+progressivo
