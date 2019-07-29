# BRF - Classe fiscale
 :  : DEC T(ST) K(BRF)
## OBIETTIVO
Identifica l'articolo ai fini delle valorizzazioni di magazzino.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica la classe fiscale.
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$BRFA **Escluso Valorizzazione**
Se si imposta '1' gli articoli appartenenti a questa classe sono memorizzati nell'archivio fiscale ma possono essere esclusi dalla valorizzazione in fase di stampa.
Se si imposta '2' gli articoli appartenenti a questa classe non sono memorizzati nell'archivio fiscale.
È necessario ricordare che questa impostazione può essere sostituita da un comportamento personale, definito a livello di scenario.
