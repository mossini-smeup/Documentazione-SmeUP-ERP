# Autorizzazioni sul modulo V5STAT

## Autorizzazioni
E' possibile in SME-UP gestire l'autorizzazione a livello di singolo campo di un file. Questa possibilità è particolarmente interessante nelle statistiche, qualora si voglia controllare l'accesso alle informazioni inerenti a valori di costo/prezzo/margine.
La reportistica non renderà visibile le colonne relative a campi non autorizzati per l'utente.

La gestione delle autorizzazioni a livello di campo è possibile grazie alla
**Classe di autorizzazione LO.FLD = "Protezione Campo" (Tabella B£P - Elemento LO.FLD).**
Nella tabella sono indicati i gruppi di autorizzazione a cui i campi di un file possono appartenere.

L'assegnazione del Gruppo di Autorizzazione ai campi dei file è definita nel programma B£EQRY_AO. Per interrogare il Gruppo di Autorizzazione a cui un campo appartiene, si può utilizzare la /COPY £IR1.
L'autorizzazione a livello di utente/gruppo utente sarà gestita con la funzione UP AUT.

Per esempio, il campo D6COST="Costo del Venduto" del V5STAT, ha il Gruppo di Autorizzazione 9 (B£S-AZ Elemento LOP9 = Valori Costo Margine).
Il valore assegnato al campo in B£EQRY_AO è 91. Se ad un utente viene impostato nel gruppo di autorizzazione 9 il valore 90, l'utente non sarà abilitato alla sua visualizzazione. E' possibile per esempio verificare con la funzione UP SQL che, interrogando il file V5STAT, la colonna relativa al campo non sarà visualizzata.

E' inoltre possibile autorizzare l'accesso alle consultazioni delle singole sezioni della scheda , es. :  vendite fatturato, Fatturato e spedito, etc, tramite la classe LO.EXD, funzione V5STAT.
Le sezioni controllate dal valore assegnato sono attualmente le seguenti : 
 * _2_Vendite Fatturato :  valore 09
 * _2_Vendite Fatturato e spedito :  valore 09
 * _2_Ordinato residuo :  Valore 19
 * _2_Ordinato totale :  valore 19
 * _2_Backlog ordinato :  valore 29
 * _2_Acquisti Fatturato :  valore 59
 * _2_Acquisti fatturato e ricevuto :  valore 59
 * _2_Acquisti ordinato residuo :  valore 69
 * _2_Acquisti ordinato totale :  valore 69
 * _2_Menù del modulo :  valore 99
