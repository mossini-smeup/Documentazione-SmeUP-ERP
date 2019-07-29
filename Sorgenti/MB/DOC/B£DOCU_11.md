# Definizioni
La collana è un elenco di book.
Il book è un elenco di documenti.
Collane e book possono essere reali (l'elenco è contenuto in un membro) oppure virtuali, se non esiste il membro (l'elenco è costruito dinamicamente in base a regole).

aa - applicazione (elemento di tabella B£A)
mmmm - modulo (elemento aammmm di tabella B£A MO)
ttt - tipo manuale (elemento V2 TMAN)

# Nomenclatura
Si definiscono i seguenti membri di DOCBOK (reali o virtuali).
- C_A_aa - Collana dell'applicazione :  contiene l'elenco dei book dell'applicazione
- C_M_aammmm - Collana del modulo :  contiene l'elenco dei book del modulo
- C_T_ttt - Collana del tipo manuale :  contiene l'elenco dei book di tutte le applicazioni di tipo ttt. NB :  attualmente NON torna i book dei moduli.
- aa_ttt - Book dell'applicazione :  contiene la lista dei documenti di tipo ttt dell'applicazione aa. NON contiene i documenti dei moduli ma solo quelli riferiti esplicitamente all'applicazione
- aammmmttt - Book del modulo :  contiene la lista dei documenti di tipo tt del modulo aammmm.

# Modo di reperimento
La documentazione dell'oggetto applicazione (istanza della tabella B£A) è deviata sull'oggetto MB/DOCNOK/C_A_aa.

La documentazione dell'oggetto modulo (istanza della tabella B£AMO) è deviata sull'oggetto MB/DOCNOK/C_M_aammmm.


