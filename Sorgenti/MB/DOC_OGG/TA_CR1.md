# CR1 - Personal.controllo qualità 2
## OBIETTIVO
__Personalizzazioni aggiuntive Q9000.__
Come la tab. CQ1, contiene alcune scelte di personalizzazione dell'applicazione. Con tali scelte si può condizionare il modo di esecuzione dei programmi.
## CONTENUTO DEI CAMPI
 :  : FLD T$LMCC **Controllo livello di modifica Cicli Collaudo**
Campo controllato dai valori standard di Sme.up SI/NO.
Se attivato comporta il controllo del livello di modifica del collaudo.
 :  : FLD T$CR1A **Congruenza esito collaudo Non Conformità**
Campo controllato dai valori standard di Sme.up SI/NO.
Se specificato SI, attiva il controllo di congruenza tra esito di collaudo e il difetto sulla Non Comformità (vedi tabella CQD)
Se il difetto non ammette esito conforme, la dichiarazione di collaudo non accetta esito con tipo Accettazione Conforme.
 :  : FLD T$CR1B **Verifica obbligatorietà rilievi**
**NB** Valido solo se attiva la gestione cicli di collaudo per oggetto.
Campo controllato dai valori standard di Sme.up SI/NO.
Se specificato SI, attiva il controllo della presenza rilievi obbligatori.
 :  : FLD T$CR1C **Numer.documenti**
Se impostato forza l'utilizzo di un unico numeratore (in TACRNDO) per tutti i tipi documento DQ; in caso contrario ogni documento utilizza un numeratore il cui codice è il suo tipo documento, sempre in TACRNDO.
Avere un unico numeratore serve a garantire l'univocità del G§NUDO per tutti i documenti, visto che questo campo ora riveste la funzione di IDOJ degli oggetti DQ (e quindi il codice dell'istanza).
 :  : FLD T$CR1D **Calcolo EM da IDQ**
Se impostato, nell'interfaccia del lotto, l'esponente di modifica, se assente nell'archivio, verrà acquisito tramite la routite £IDQ (interfaccia documenti qualità).
