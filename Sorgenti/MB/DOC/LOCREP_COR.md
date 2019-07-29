# Programma del corso

 T(**Introduzione**)
- A cosa serve questo corso : 
-- Capire le basi relative al componente e dei servizi che lo riforniscono
--- Cosa fa
---- Report tabellari basandosi su dati nel formato matriciale di Loocup
---- A uno o due livelli
---- In file PDF
---- Su vari formati
--- Cosa non fa
---- Report compositi
---- Di formato composito
---- Riportando dati che non siano nel formato matriciale di Loocup
--- Capire il funzionamento del motore su cui si basa
---- Le funzioni EXB e EXD e la loro conversione in REP
---- I folder gestiti i default e la loro impostazione (REP.SRC, REP.TMP, REP.OUT)
---- Jasper Report
----- Cos'è
----- Come funziona
------ Le zone del documento
------ Le variabili
------ I Field
----- Cosa sono i template
--- Cosa devono fornire i servizi che producono i dati per il report


 T(**Il documento prodotto**)
- Esempio di un report ed analisi dei suoi costituenti
-- ESEMPIO :  LOA15-->A3.F1.S2
-- File
-- Documento
--- Copertina
--- Corpo
-- Pagina
--- Header
--- Footer
--- Dettaglio
-- Contenuto
--- Filtri
--- Gruppi
--- Rotture
--- Stili e layout


 T(**Il setup**)
- Il setup del report
-- Da dove può arrivare il setup
--- Dallo script della scheda (Scheda CMP_REP come esempio)
--- Dal servizio
--- Dalla funzione se il servizio lo supporta
-- Analisi della finestra di setup
--- File (accenti) : 
---- Password
--- Documento (accenti) : 
---- Template
---- Gestione automatica del dettaglio
--- Pagina
---- Numero campi per colonna di stampa
--- Contenuto
---- Riga lettura facilitata
---- Esplosione gruppi
--- Tecnica
-- Cosa viene emesso nella finestra di setup
--- Cosa viene passato nel XML in /Setup/Program/REP
--- Il servizio LOSER_07
--- Gli oggetti J3 e il setup A01
- La scheda degli oggetti J3
- Modificabilità dei J3 ed effetti
- Esempio di implementazione del supporto degli override da funzione
-- Il LOA15_SE


 T(**Personalizzabilità**)
- Esempio di creazione di un template personalizzato
-- iReport (l'editor dei template --- il link)
--- I template esistenti
--- L'editing di un template "from scratch"
---- La tabella dati
---- Le immagini
---- Il background
---- Gli StaticFields
---- I TextField
----- Le incompatibilità ($, etc.)

