## Obiettivi
 - Ottenere un insieme di manuali omogenei dal punto di vista formale, di struttura e di contenuto che possono essere generati tutti i giorni e resi disponibili in formato PDF per consultazione e/o stampa.
 - I manuali saranno disponibili sul sito, forniti assieme al software, stampati ogni sei mesi e visibili in laboratorio.
 - In futuro potremo pensare a sistemi di ricerca direttamente sui manuali prodotti
 - Il PDF conterrà le immagini quindi per consultarli non avremo bisogno dell'accesso alle immagini sul server

Decisioni (già esecutive)

- Apriremo due nuovi files DOC_VIS per tutti i documenti di visione e DOC_OPE per tutti i documenti operativi.
- Definiamo il nuovo oggetto V2 TIMAN con i valori :  OPE / VIS / TEC / SVI
- Quando ci si vuole riferire all'applicazione SMEup in generale si userà la sigla SM (codificata in tabella B£A)

Decisioni (da eseguire)

- Scriveremo un programma (servizio / scheda) di utilità per : 
-- Vedere come diventano i manuali attuali
--- Moduli senza alcun documento
--- Documenti mai richiamati
--- Documenti richiamati e vuoti o non esistenti
-- Generare i documenti in DOC_BOK (in futuro potrebbero essere virtuali)
- Scriveremo i seguenti programmi : 
-- Gestione di un paragrafo
--- La £G90 fornisce TAG e testo. Dato un contesto (HTML, Stampa ecc) dobbiamo ottenere il testo che restituiamo al chiamante, trasformato e pulito
- Assegnazione responsabilità per oggetto
-- Avremo un programma che, dati un oggetto e una funzione (DOC, SVI ecc) restituisce : 
--- Responsabile
--- Stato di avanzamento (esempio numero da 01 a 99 - (gabellare?)
--- Importanza (A, B, C)
-- I dati potranno essere progressivamente : 
--- Cablati nel programma
--- In un documento (esempio membro di SCP_SET)
--- In un database
- Dovremo rivedere un documento "FONDAMENTALE" riguardante l'organizzazione della documentazione di SME.up (Attuale B£DOCU_10) che conterrà la parte da rilasciare di questo documento


Ipotesi di lavoro
- I documenti contengono LINK a documenti oppure solo testo. In un documento di testo il richiamo ad altro documento è solo un riferimento.
- Mi piacerebbe definire un responsabile per ogni applicazione (chiaro, noto e cablato..). Dovrebbe essere un OAV della tabella B£A. Potrebbero esserci un responsabile e due aiutanti. Oppure potremmo portarci
- Aggiungiamo (provvisoriamente) una LABAL alla scheda dell'applicazione chiamata "manuali"
- Per ora i manuali delle applicazioni sono virtuali
- Dovremmo studiare il manuale/i del modulo

## Manuali per applicazione
 - Visione  (xx_VIS in DOC_BOK)
 -- xx_Vnnn (con nnn da 001 a 010)

- Applicativo (xx_APP in DOC_BOK)
-- Scansione dei moduli
--- In DOC
--- In DOC_OPE
-- Glossario
-- FAQ
--- xx in DOC_QEA
--- Scansione dei moduli
- In DOC_QEA
- Operativo (xx_OPE in DOC_BOK)
-- xx_OPE in DOC_OPE
-- Scansione dei moduli
--- In DOC_OPE
- Tecnico (xx_TEC  in DOC_BOK)
-- Files
-- Tabelle
-- Copy/Api
-- Calassi di autorizzazione
-- Servizi
-- Schede
-- Conversioni
- Sviluppo (xx_SVI  in DOC_BOK)
-- Scansione dei moduli

*********** DA QUI NOTE DI GALDINI *****************************************************************

Il vocabolario di Sme.UP

Formano il vocabolario di Sme.Up : 
- Documentazione degli oggetti applicativi (membri OG_XX di DOC_OGG)
- Glossari delle singole applicazioni xx (voci del membro GLO_xx di DOC_VOC)
- Glossario degli acronimi Sme.Up (voci del membro GLO_ACR_01 di DOC_VOC)
- Glossario degli acronimi applicativi (voci del membro GLO_ACR_02 di DOC_VOC)
- Glossario degli acronimi informatici (voci del membro GLO_ACR_03 di DOC_VOC)

NOTE DI COMPLIAZIONE
I termini generali vanno descritti in GLO_B£.
Se un concetto è definito come oggetto NON va nel glossario dell'applicazione. (Esempio il cespite).
Se un concetto è definito come acronimo NON va nel glossario dell'applicazione. (Esempio MRP).

C'è quindi il problema di come costruire il glossario dell'applicazione. Per gli oggetti si riesce,
in quanto c'è l'elenco degli oggetti di un'applicazione e quindi si riescono a comprendere.
Per gli acronimi questo non succede. Si potrebbe mettere nel glossario dell'applicazione il Link
al termine come acronimo, però bisogerebbe capire quando risolverlo e quando tarscurarlo.


****************************************************************************************************





