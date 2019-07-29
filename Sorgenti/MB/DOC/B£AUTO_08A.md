# Obiettivo
Normalmente le autorizzazioni sono pensate per proteggere l'esecuzione di una funzione o la visualizzazione dei dati. In alcuni casi si vuole proteggere la visualizzazione o la gestione di un oggetto.
Ad esempio potrei volere che una persona possa vedere solo i clienti di cui è responsabile oppure inibire la modifica delle note per gli articoli che appartengono a certe classi.

# Soluzione in SME.up

In SME.up abbiamo predisposto un archivio che consente nel modo più flessibile possibile di assegnare ad un oggetto prima un codice di appartenenza e poi ottenere le autorizzazioni dell'utente rispetto a quel codice.
Il risultato sono tre proprietà (OAV) generali di ogni oggetto.
- Visibilità
- Gestione
- Accesso agli allegati quali note, parametri, rubriche ecc.

# Dove posso comprendere l'effetto
Dalla scheda del modulo B£AUTO è possibile accedere alla gestione delle "autorizzazioni per oggetto".
In questa scheda posso : 
- Vedere le impostazioni presenti
- Modificare le impostazioni
- Simulare l'effetto su un insieme scelto di oggetti.

# Esempi
Supponiamo di voler proteggere la modifica o la visibilità di un cliente in base alla filiale di riferimento. Procederemo nel modo seguente : 

- Creiamo un OAV U/xxx del cliente che restituisca 'ENABLED' se l'utente di esecuzione del lavoro £PDSNU è abilitato a vedere il cliente e 'DISABLED' se non è abilitato
- Aggiungiamo una riga nel AUTOOG0F con  AO£CLA  (Classe) 'OGG.MAS' , AO£TIP  (Tipo oggetto) 'CN',   AO£PAR (Parametro oggetto) 'CLI', AO£COD (Codice oggetto)  '' ,   AO£ATT (Attributo) 'U/xxx' ,  AO£VAL (Valore attributo) '', AO£GRA     (Funzione autorizzaz.) '**'
- Nell'UP AUT aggiungiamo un record con classe 'OGG.MAS' e funzione 'ENABLED' con valori massimi (99, 89, 79 ...)
- Nell'UP AUT aggiungiamo un record con classe 'OGG.MAS' e funzione 'DISABLED' con valori minimi (91, 81, 71 ...)
- Attiviamo "nuova gestione azioni" in B£2 con valore '1'
- A questo punto ogni utente potrà accedere alle schede, alla gestione e alle risorse (immagine, cartella)  solo dei clienti per i quali l'OAV restituisce ENABLED.
- Se vogliamo che i clienti a cui un utente non è abilitato siano esclusi anche dai surf possiamo agire sulla exit B£IVD0_U aggiungendo una WHERE per l'oggetto CNCLI che filtri i clienti.

