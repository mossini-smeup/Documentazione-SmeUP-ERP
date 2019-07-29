# OBIETTIVO
Gestione le informazioni relative agli avvisi di pagamento ricevute tramite home-banking, scartandole o associandovi la relativa scadenza presente in contabilità, creando contiguamente la pratica bancaria di ritiro riba passive.

# ATTRIBUZIONE AUTOMATICA (CORRISPONDENTE ALLA VOCE DI MENU SPUNTA AUTOMATICA)
Lanciando questa funzione per ogni avviso ancora in stato "attivo" viene lanciata una ricerca sulle scadenze passive aperte, ed in caso di corrispondenza perfetta (corrispondenza data dal soggetto reperito tramite il riferimento fiscale dell'avviso, dalla scadenza, dal tipo di pagamento e dall'importo), vengono automaticamente eseguite le seguenti azioni : 
 * cambio stato dell'avviso "da presentare" a "presentato"
 * indicazione sull'avviso dell'IDOJ della rata corrispondente
 * riporto dei dati dell'avviso sulla rata corrispondente
 * creazione automatica delle relativa pratica di ritiro riba, sul rapporto di c/c della banca riportata sull'avviso e con data pratica, la scadenza dell'avviso (Se un pratica con queste caratteristiche esiste già la rata viene aggiunta a tale pratica).

La relazione che si instaura fra l'avviso e la rata viene mantenuta anche successivamente, perciò una deselezione della rata associata dalla pratica di presentazione comporta automaticamente l'invesione dello stato dell'avvisO che torna allo stato da "presentare".

 :  : INI _2_>>**Pgm di lancio dell'attribuzione automatica degli avvisi**
 :  : CMD CALL C5N000G PARM('OF' 'R A ' 'V2C5TSC')
 :  : FIN

# GESTIONE  (CORRISPONDENTE ALLA VOCE DI MENU SPUNTA MANUALE)

Scrivendo '?' nel campo bianco a fianco della registrazione interessata si visualizzano una serie di opzioni illustrate in seguito : 

![C5D010_045](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR07L/C5D010_045.png)
-Attribuisci rata mi può portare a 3 diverse opzioni :  la prima mi trova subito la corrispondenza corretta ,la seconda trova una serie di anagrafiche verosimili (esempio due con la stessa ragione sociale), la terza non trova nulla e occorre fare una ricerca ex novo;
-Attribuisci rata manuale, coincide alla terza opzione qui sopra e si utilizza se l'attribuzione in automatico è sbagliata;
-Annulla avviso se voglio escludere questo avviso;
-Gestione rif. Fiscale permette di attribuire il Codice fiscale/Partiva iva dell'avviso nel caso non fosse indicato nel flusso;
-Dettaglio avviso mi da il dettaglio completo;
-Partitario soggetto rimandanda al partitario completo del fornitore.


 :  : INI _2_>>**Pgm di gestione degli avvisi**
 :  : CMD CALL C5N000G PARM('OF' 'R G ' 'V2C5TSC')
 :  : FIN


