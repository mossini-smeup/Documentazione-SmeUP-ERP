Questo documento contiene le informazioni necessarie per creare un nuovo ambiente sui server del laboratorio di sviluppo.

- Decidere la sigla dell'ambiente (di 3 lettere, ad esempio XYZ)
- Creare la libreria UP_XYZ come copia della libreria SMEUP_FIL
- Creare la libreria PER_XYZ (o XPER_XYZ in base al fatto che la si voglia salvare o meno) come copia della libreria SME_XXX
- Rivolgersi al responsabile sistemistico per la creazione (ove necessaria) degli utenti "utilizzatori". Tali utenti andranno creati con la codifica XYZ_nn (con nn progressivo) come copia dall'utente XXX_01
-- Questi utenti sono indispensabili in caso ci siano persone esterne (ad esempio clienti) con la necessità di collegarsi a tale ambiente
- Mediante il comando UP UT5 è poi necessario : 
-- Definire la lista librerie dell'ambiente appena creato (opzione 2)
-- Associare il nuovo ambiente agli utenti interessati (opzione 1)
- Tutti gli eventuali oggetti sistemistici che verranno creati (code lavori, stampanti ecc.) dovranno comunque avere la codifica XYZ_xxx

Alcuni documenti utili : 
- [Lab. Sviluppo - Nomenclatura librer](Sorgenti/MB/DOC/A£BASE_01E)
- [Gestione applicazioni utente](Sorgenti/MB/DOC_OGG/P_B£UT55)



