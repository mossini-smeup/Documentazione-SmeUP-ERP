Riportiamo di seguito una serie di aspetti a cui prestare attenzione nell'utilizzare fonti utente per interfacciare altri gestionali.

# Quantità

Su fonti di copertura futura (ordini di produzione, acquisto, conto lavoro) impostare : 
 * Quantità residua in £M5DQT;
 * Quantità originale in £M5DQO, al fine di permettere all'MRP la corretta emissione di suggerimenti di riduzione.

# Date

Su fonti di copertura futura (ordini di produzione, acquisto, conto lavoro) se necessario tenere conto del tempo di rettifica nel determinare la data £M5DDT (avanzare la data fine ordine del tempo di rettifica).

# Campi per navigazione (implosione/esplosione)

Al fine di consentire una corretta navigazione tra i fabbisogni e le coperture è necessario : 
 * Impostare nel campo tipo documento (£M5DTD) i valori '*AS' per le coperture (ordini) e '*CO' per i fabbisogni (impegni).
 * Impostare in maniera congruente i campi numero documento e numero riga (£M5DND e £M5DRG).

# Campi per navigazione (implosione/esplosione)

Nel ca£o si utilizzi l'ATP è necessario impostare correttamente, nelle fonti di tipo "ordine di vendita" il campo "numero record" (£M5DRN).

