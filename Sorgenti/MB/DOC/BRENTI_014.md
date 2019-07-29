# Definizione
La storicizzazione dei dati permette di poter gestire per date di validità il valore di alcuni dati di base e di alcune estensioni dell'anagrafica contatti.

Tale scelta è applicabile sia a qualsiasi campo anagrafico che a qualsiasi estensione, ma tale applicazione dovrebbe essere fatta in modo oculato, in quanto tale definizione comporta l'obbligo da parte degli utenti di indicare sempre le date di validità, nonchè il fatto che (soprattutto per quel che riguarda l'anagrafico) ogni combinazione di date presenti comporta la scrittura di un apposito record anagrafico.

Es. se si gestisce la ragione sociale ed il telefono per data e si ha : 
>- ragione sociale        dal          0 a 31/12/2007 = aaa
-                        dal 01/01/2008 a 31/12/9999 = BBB
- telefono               dal          0 a 30/06/2008 = 111 1111
-                        dal 01/07/2008 a 31/12/9999 = 999 9999

Fisicamente sul database si ha : 
>- record 1        dal          0 a 31/12/2007 = ragione sociale = aaa telefono 111 1111
- record 2        dal 01/01/2008 a 30/06/2008 = ragione sociale = BBB telefono 111 1111
- record 3        dal 01/07/2008 a 31/12/9999 = ragione sociale = BBB telefono 999 9999


L'interfaccia funzionerà di conseguenza sempre in riferimento alla date di validità, ritornando i dati validi alla data passata. Se non viene passata alcuna data viene assunta come data di riferimento la data odierna.

Per ogni soggetto deve sempre esistere almeno un record che abbia data iniziale 0 e uno (che può anche essere lo stesso) che abbia data finale 31/12/9999

# Attivazione
 * Definizione dei dati che si vogliono storicizzare per ogni tipo contatto.
    I dati più idonei ad essere storicizzati sono : 
 ** Dati descrittivi
 ** Dati geografici
 ** Dati fiscali
 ** Categoria contabile
 * Tali dati vanno impostati indicando il campo o l'estensione nello script relativo ad ogni tipo contatto (radice "CN_F" + Tipo contatto). Per la compilazione si faccia riferimento alla documentazione di "Configurazione dello script".
 * Con questa funzionalità verrà automaticamente attivato anche il data entry a formato esteso, per tale motivo è necessario controllare che la sua parametrizzazione sia corretta (Cfr. "Configurazione Data Entry V2").
 * Una volta eseguita la suddetta configurazione, perchè il controllo della data venga attivato dall'interfaccia è necessario attivare il relativo flag nella tabella BR2.

 :  : DEC T(ST) K(BR2)

- E' infine consigliato, anche se può avvenire in un momento successivo, eseguire il travaso dei dati storici per la partita IVA (qualora tale dato sia stato previsto come da storicizzare) in precedenza riportati tramite l'utilizzo dell'estensione £09 del BRESCO.

 :  : INI Lancio Travaso Estesione £09 Partita IVA nell'anagrafica
 :  : CMD CALL BRUT07A
 :  : FIN
