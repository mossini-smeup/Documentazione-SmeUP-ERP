# B£W - Stati
 :  : DEC T(ST) K(B£W)
## OBIETTIVO
Catalogare gli stati e guidare la progressione (o regressione) dello stato.
## UTILIZZO
Permette di gestire lo stato di un documento, definendo una struttura relazionale tra i diversi stati.
## SOTTOSETTORI
I sottosettori permettono di suddividere i gruppi di stati. La denominazione di alcuni di tali sottosettori è definita in modo fisso da parte di SMEUP. L'utente dovrà codificare i propri sottosettori con i prefissi X e $.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice stato**
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$B£W1 **Stato principale**
Se si imposta questo campo, lo stato di questa tabella è lo stato principale.
 :  : FLD T$B£W2 **Stato successivo assunto**
Indica lo stato successivo che può essere assunto, cioè quello di destinazione.
 :  : FLD T$B£W3 **Minimo stato provenienza**
Se valorizzato, viene controllato qual è il minimo stato di provenienza.
 :  : FLD T$B£W4 **Massimo stato provenienza**
Il massimo stato di provenienza non può essere maggiore dello stato in esame.
 :  : FLD T$B£W5 **Minimo stato di arretramento**
Il minimo stato deve essere, chiaramente, minore dello stato attuale che si sta esaminando.
 :  : FLD T$B£W6 **Livello**
Indica il livello valido per questo stato.
