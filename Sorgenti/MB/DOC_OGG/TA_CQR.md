# CQR - Regole di commutazione P.d.C.
 :  : DEC T(ST) K(CQR)
## OBIETTIVO
Stabilire le regole di commutazione (ovvero le regole che consentono di passare da un piano di campionamento ad un altro) da applicare ai piani di campionamento o al livello di collaudo.
## CONTENUTO DEI CAMPI
 :  : FLD T$NCXP **Numero conformi**
Numero 'Nc' di lotti con esito di collaudo conforme, su un numero di lotti collaudati consecutivi specificati dal campo successivo. La conformità o meno del collaudo è determinata della tabella 'CQB' (Esito controllo collaudo).
 :  : FLD T$NLXP **Su numero lotti**
Numero 'N' di lotti consecutivi da considerare da utilizzare in combinazione al campo precedente. La regola deve intendersi come :  SE negli ultimi 'N' lotti consegnati trovo 'Nc' lotti conformi consecutivi, partendo dall'ultimo consegnato (data più recente), allora cambio il piano di campionamento assegnato all'ultimo lotto nel piano 'PdC più leggero'.
 :  : FLD T$TCXP **PdC più leggero**
Campo controllato dalla tabella 'CQP' (Piano controllo qualità). Piano di campionamento da utilizzare al posto dell'attuale, se si è verificata la condizione precedente (ovvero è stato riscontrato un numero di lotti conformi maggiore od uguale al valore specificato nel primo campo, su una sequenza di lotti consecutivi specificata nel secondo campo).
 :  : FLD T$REXP **Regola specifica**
Eventuale regola specifica di variazione, gestita da un programma ad hoc. Attualmente non utilizzato.
 :  : FLD T$NCXS **Numero non conf.**
Numero di lotti 'NNc' con esito di collaudo non conforme su un numero di lotti collaudati consecutivi specificati dal campo successivo. La conformità o meno del collaudo è determinata dalla tabella 'CQB' (Esito controllo collaudo).
 :  : FLD T$TCXS **Piano di campionamento più pesante**
Campo controllato dalla tabella 'CQP' (Piano controllo qualità). Piano di campionamento da utilizzare al posto dell'attuale, se si è verificata la condizione precedente (ovvero è stato riscontrato un numero 'NNc' di lotti non conformi, maggiore od uguale al valore specificato nel primo campo su una sequenza di lotti consecutivi specificata nel secondo campo).
