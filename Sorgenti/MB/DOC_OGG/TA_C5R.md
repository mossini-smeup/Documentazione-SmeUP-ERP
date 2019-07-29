# C5R - Registri IVA
 :  : DEC T(ST) K(C5R)
## OBIETTIVO
Definire le caratteristiche dei registri IVA
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Contiene la descrizione del registro IVA
 :  : FLD T$C5RT **Tipo registro IVA**
È un elemento V2/C5TRG :  definisce se il regsitro è di vendite, acquisti, ecc.. È riportato nella testata della registrazione, leggendo l'elemento 'Codice registro IVA' contenuto nel tipo registrazione.
 :  : FLD T$C5RA **Registro origine**
È un elemento di questa stessa tabella :  se impostato, il registro di questo elemento di tabella non ha righe proprie, ma condivide quelle del registro qui digitato, invertendone il segno. In questo modo si gestisce l'IVA intracomunitaria senza duplicazione di registrazioni, semplicemente indicando nel registro IVA vendite intacomunitarie come registro origine il registro acquisti intracomunitari.
 :  : FLD T$C5RB **Protocollo manuale**
È un elemento V2/SI/NO :  se impostato, il numero di protocollo non viene assegnato automaticamente all'atto della chiusura della registrazione, ma deve essere inserito manualmente dall'utente.
 :  : FLD T$C5RC **Corrispettivi**
È un elemento V2/SI/NO :  indica se il registro è un rgistro corrispettivi o meno.
 :  : FLD T$C5RD **Ultima pagina stampata**
Indica l'ultima pagina stampata per il registro.
 :  : FLD T$C5RE **Stampa su Registro**
Permette di indicare se un registro vada o meno considerato per gli obblighi IVA. Questo parametro può tornare utile per esempio nella gestione dell'IVA straniera relativa ad posizioni fiscali estere(Es. Ho un deposito in una nazione estera dal quale fatture e nella quale prendo anche partita IVA estera).
 :  : FLD T$C5RF **Stampa su Riepilogo**
Permette di indicare se il registro vada stampato o meno all'interno del riepilogo.
 :  : FLD T$C5RG **Settore attività**

 :  : FLD T$C5RH **Dati integrativi**
Permette di impostare la presenza o meno dei dati integrativi sulla stampa del registro.

 :  : FLD T$C5RJ **Codice Interfaccia**
Tramite questo campo viene condizionata l'interfaccia dell'oggetto FT (Fattura). Viene assunto che l'interfaccia sia SM (cioè Sme.Up).**NOTA BENE** :  per ragioni storiche vale ancora la risalita che prevedeva di controllare l'interfaccia a partire dalla deviazione della tabella C5R. Se la tabella C5R è deviata viene presa in considerazione l'interfaccia corrispondente a tale deviazione.

 :  : FLD T$C5RK **Fonte Interfaccia SM**
Se l'interfaccia dell'oggetto FT è SM, è possibile condizionare la fonte dati dell'oggetto fattura : 
* " " Assunto :  di default le fatture del ciclo attivo vengono ricercate nei documenti, mentre quelle del ciclo passivo e dei corrispettivi nella contabilità.
* "1" Contabilità :  forza che le fatture del registro vengano ricercate nella contabilità
* "2" Documenti :  forza che le fatture del registro vengano ricercate nei documenti

 :  : FLD T$C5RL **Split Payment**
Questo campo ha rilevanza solo sui registri d'acquisto. Indica che le fatture in essa registrate rientrano nel regime dello split payment e che per tale motivo su di essere verrà rilevata anche l'iva vendite. In questo caso sarà infatti inoltre necessario creare un registro vendite che abbia come origine il registro acquisti di partenza.

 :  : FLD T$C5RM **Imposta non liquidabile**
Questo campo identifica, un registro in cui vanno registrate le fatture per cui l'imposta risulta non liquidabile per termine detrazione, secondo la normativa italiana.
Vanno qui registrate le fatture ricevute l'anno precedente ma registrate nell'anno successivo.

Per effetto di questo si scateneranno tutte le considerazioni descritte nel documento specifico del modulo Iva.

