## Documentare un costruttore LOAXX
Un costruttore è, salvo eccezioni, un insieme di funzionalità ad alto livello offerte da una scheda di Looc.up (con i suoi servizi collegati).

Per migliorare l'accessibilità alla documentazione e agli esempi sono state definite le seguenti convenzioni, dato un costruttore LOAxx : 

- Va creato in B£G15G un oggetto V2LOCOS LOAxx, se il costruttore è rilasciato;
- La scheda applicativa è SCP_SCH(LOAxx); tale scheda fornisce il servizio quando richiamata con opportuni parametri;
- Eventuale documentazione operativa, linkabile dalla scheda LOxxx, va messa in DOC_OPE(V2LOCOSAxx);
- La documentazione tecnica è in DOC_OGG(V2LOCOSAxx) (link automatico, vedi dopo);
- La scheda contenente esempi (non prove!) è in SCP_SCHESE(COS_Axx) (link automatico, vedi dopo);


Documentazione tecnica ed esempi non vanno linkati in quanto sono automaticamente reperibili dal punto di accesso standard riservato all'help dei costruttori : 
_2_Barra dei menù di Looc.Up Smeup -> Per lo sviluppatore -> Costruttori
oppure
_2_Applicazione LO -> modulo Costruttori
