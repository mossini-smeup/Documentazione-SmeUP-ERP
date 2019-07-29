# STAMPA INFORMAZIONI ARCHIVI
# FORMATI VIDEO
# Obiettivo
Fornire tutte le informazioni collegate ad un archivio quali contenuto, metodi di elaborazione utilizzo in programmi ecc.
# FORMATO GUIDA
## Libreria
Serve ad indicare il SISTEMA INFORMATIVO qualora esistano archivi con nomi uguali e struttura diversa.
## File
Può essere indicato un file oppure tutti i file che iniziano con un prefisso mediante l'inserimento di un asterisco
## Documentazione generale
Permette di stampare il documento OFFICE/400 collegato al file. Si devono indicare la cartella che contiene la documentazione degli archivi e l'eventuale suffisso utilizzato per distinguere la documentazione dei file
## Metodi di accesso al file
Si stampano le viste logiche costruite sul file e se richiesto : 
-    l'elenco dei campi chiave
-    i programmi in cui tali vie di accesso sono utilizzate
## Elenco campi
Si stampano tutti i campi contenuti nell'archivio
Se richiesto per ogni campo si stampano : 
- gli archivi in cui lo stesso campo è utilizzato
- la documentazione del campo presente in OFFICE/400
## Relazioni
Si stampano tutti i collegamenti con gli altri archivi. Si potranno presentare le seguenti condizioni : 
-    Definizione
Il campo risulta essere la chiave univoca del file indicato quindi tale file rappresenta la definizione del campo.
In particolare il campo potrà essere descritto come definito in una TABELLA.
-    Collegamento
Tutte le chiavi del file indicato sono presenti nell'archivio in esame.
-    Sviluppo
Le prime chiavi del file logico risultano presenti nel nostro archivio quindi il file logico può essere visto come uno sviluppo di righe.

# Esempio
Si hanno i seguenti archivi : 
Archivio          Chiavi              Contiene
- Articolo          CODART
- Clienti           CODCLI
- Ordini            ORDINE              CODCLI/AGENTE
- Righe ordine      ORDINE/NUMERO       CODART/CODMAG/UNIMIS
- Commenti ordine   ORDINE/NUMERO/PROGRE
- Magazzino         CODMAG
- Giacenze          CODMAG/CODART
Tabelle                               Nome
- UNITA DI MISURA   UNIMIS             UMS
- AGENTI            AGENTE             AGE se sviluppiamo le RIGHE D'ORDINE avremo : 
Relazioni : CODART    Definito :       Articoli
Collegato :      Giacenze (Ho anche CODMAG)
UNIMIS    Def.Tabelle    UMS Unità di misura
ORDINE    Definito :       Ordini
Sviluppo :       Commenti riga ordine
CODMAG    Definito :       Magazzini
Collegato :      Giacenze (Ho anche CODART)
