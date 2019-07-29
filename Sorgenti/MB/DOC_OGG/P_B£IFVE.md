# GESTIONE DEFINIZIONI INTERFACCE
## OBIETTIVO
Permettere la visualizzazione e la definizione delle interfacce definite a livello di sistema.
Consentire le verifiche di due tipi : 
-    esistenza e disponibilità degli oggetti di sistema (programmi e dati) necessari per una interfaccia.
-    simulazione dell'accesso ai dati di cui si richiede l'interfaccia.
## NOTE OPERATIVE
Le righe che si presentano sono tutte e sole quelle definite nella tabella B£1. Il programma è solo una forma di immissione più quidata e controllata ma non permette di aggiungere nuove interfacce.
Opzione
Questo campo si presenta quando è attiva la possibilità di richiamare il programma di verifica cioè quando l'interfaccia descrive un oggetto applicativo (Es. articolo, cliente, ubicazione ecc.)
Interfaccia
Descrizione dell'interfaccia definita per la tabella B£1
Applicazione
Codice dell'applicazione.
Tale codice può essere associato mediante la B£1 a  due diverse tabelle : 
1.   Tabella *CNAA
Solo descrittivo
Il campo tipo oggetto si presenta con inversione di fondo.
Sono possibili le normali interrogazioni ma non i controlli.
2.   Tabella B£Vxx (xx=tipo oggetto)
Oltre alle normali interrogazioni è possibile inserire il carattere "/". In tal caso si presenta un formato di  9
dettaglio che visualizza tutte le interfacce descritte per l'oggetto permettendo la selezione delle sole interfacce
che non presentano errori, cioè per le quali è soddisfatta la disponibilità di file e programmi descritti nella specifica tabella.
## TASTI FUNZIONALI
F6   Controllo interfacce
Esegue per tutte le interfacce descritte in tabella B£V la verifica sopra descritta e presenta il campo lampeggiante  se l'esito ha dato risultato negativo.
## TABELLE COLLEGATE
B£1   - Personalizzazione
*CNAA - Codici ambiente applicativo *CNTT - Codici oggetti applicativi
B£Vxx - Dettaglio interfacce applicative
