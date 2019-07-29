# P53 - Parametri schedulazione
 :  : DEC T(ST) K(P53)
## OBIETTIVO
Definisce i parametri di schedulazione che interessano la gestione della produzione.
**!!! ATTENZIONE !!!!!**
È da compilare SOLTANTO se impostata la gestione degli impegni risorse di base (P5IRIS).
Se impostata la gestione avanzata (S5IRIS), le tipizzazioni delle risorse sono contenute negli scenari (tabella S5B), mentre l'attivazione scenari si imposta in tabella P51.
## CONTENUTO DEI CAMPI
 :  : FLD T$P53A __Attivazione scenari__
Campo non utilizzato nell'applicazione.
 :  : FLD T$P53B __Tipo risorsa generale__
Definisce l'oggetto che tipizza la risorsa generale (di tipo 'RI').
 :  : FLD T$P53C __Tipo risorsa specifica__
Se presente, significa che si desidera attivare la gestione delle risorse a due livelli (normalmente centri di lavoro/macchine).
