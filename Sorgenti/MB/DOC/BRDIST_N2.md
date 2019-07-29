# Eredità operazione di impiego in scansione DB
Viene eseguita solo nell'esplosione di produzione / produzione totale.

Se ad un livello l'operazione è blanks viene ereditata quella del livello immediatamente superiore, se fittizio.

Esempio : 
>.  Tipo Parte       Codice      Operazione scritta nel legame            Risultato operazione ritornata
.                      A                  blank
.    (0)               B                  0010                                0010
.    (2)               C                  blank                               0010 (ereditata)
.    (2)               D                  blank                               blank (non ereditata)

