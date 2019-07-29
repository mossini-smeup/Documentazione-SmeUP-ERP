# BRD - Tipo operazione
 :  : DEC T(ST) K(BRD)
## OBIETTIVI
Definisce le caratteristiche di operazioni dello stesso tipo.
## CONTENUTO DEI CAMPI
 :  : FLD T$BRD1 **Tipo tempo**
Indica il significato che assumeranno i tempi nelle operazioni di questo tipo.
 :  : FLD T$BRDU **Unità di misura dei tempi**
È un elemento della tabella UMS. Definisce l'unità di misura in cui verranno espressi i tempi nelle operazioni di questo tipo.
 :  : FLD T$BRDA **Presentazione tempi**
È un campo di 10 caratteri i quali condizionano, in modo posizionale, la presentazione dei tempi nella gestione dell'operazione. Si possono selezionare fino ad un massimo di 6 tempi. Per ognuno di essi, il carattere 'O' imposta che è obbligatorio, il carattere 'F' imposta che è solo presentato, il carattere ' ' indica che il valore non è presentato nel formato di dettaglio.
Ad esempio, una codifica di questo tipo :  "O F F  OO "significa che vengono presentati i tempi 1,3,5,8,9, e che sono obbligatori i tempi 1,8,9.
 :  : FLD T$BRDB **Rilevanza operazione**
È un elemento V2/RIOPE (riferirsi all'aiuto specifico per una descizione dettagliata). Definisce il modo in cui la riga di ciclo viene trattata dalla gestione degli impegni risorse e dalla schedulazione. In questo campo si inserisce il valore proposto all'atto dell'inserimento della riga di ciclo, ed è ivi modificabile.
- [Rilevanza operazione](Sorgenti/MB/DOC_OGG/V2_RIOPE)
 :  : FLD T$BRDC **Tipo milestone**
È un elemento V2/BRMIL (riferirsi all'aiuto specifico per una descizione dettagliata). Definisce la modalità di dichiarazione di questa riga (se induce altre dichiarazioni o è indotta da altre dichiarazioni).
In questo campo si inserisce il valore proposto all'atto dell'inserimento della riga di ciclo, ed è ivi modificabile.
 :  : FLD T$BRDD **Natura tempi**
E' posibile caratrerizzare quali tempi (nelle posizioni da 1 a 10) sono il lavoro, la macchina e l'attrezzaggio, rispettivamente impostando la sigla L,M o A, nella posizione corrispondente.
Questa informazione è utlizzata nella determinazione degli OAV J/Hxx, di tempo previsto, effettivo e rendimento di lavoro, macchina e attrezzaggio.
Se si lascia il campo vuoto viene assunta la stringa "LMA".
Se NON si vuol caratterizzare, per questo tipo operazione, nessun tempo nè di lavoro, nè di macchina, nè di attrezzaggio, è sufficiente inserire in prima posizione il carattere N (in realtà basta un carattere qualsisi, diverso da L,M e A).
