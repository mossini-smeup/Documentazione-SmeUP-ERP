# C5M - Riclassifiche
 :  : DEC T(ST) K(C5M)
## OBIETTIVO
Definire le impostazioni delle varie riclassifiche, ovvero delle diverse visualizzazioni del bilancio.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Descrive la riclassifica
 :  : FLD T$C5MC Tipo oggetto riclassifica
Indica oggetto e parametro in cui sono definite le linee della riclassifica in esame. In genere le linee della riclassifica sono definite in un sottosettore della C5N :  in questo caso il campo dovrà essere compilato con TAC5NXXX dove XXX è il sottosettore della C5N che definisce la riclassifica.
Di base per le riclassifiche obbligatorie BAS e CEE, le linee sono contenute nella tabella C5N sottosettore BA e CE rispettivamente.
 :  : FLD T$C5MD Configurazione
Indica per ogni livello di riclassifica quanti e quali caratteri delle sue linee devono essere considerati ed il loro significato.

_9_Esempio :  la configurazione della riclassifica CEE è la seguente :  '12333344444444'. Questo significa che il primo carattere della linea indicherà il primo livello di riclassifica, il secondo indicherà il secondo livello, i caratteri dal terzo al sesto indicheranno il terzo livello di riclassifica. I caratteri finali non vengono considerati poiché rappresentano le linee di dettaglio. Se entro nella C5N CE vedo che le prime linee di riclassifica sono le seguenti : 

![C5BASE_021](http://localhost:3000/immagini/MBDOC_OGG-TA_C5M/C5BASE_021.png)
La prima macro linea di riclassifica è quella dell'attivo; questa a sua volta è composta da :  crediti verso soci per versamenti dovuti + immobilizzazioni + attivo circolante + ratei e risconti. Le immobilizzazioni, a loro volta, sono composte da :  immobilizzazioni immateriali + immobilizzazioni materiali + immobilizzazioni finanziarie. A loro volta, le immobilizzazioni immateriali sono formate da costi di impianto e di ampliamento + costi di ricerca, sviluppo e pubblicità + diritti di brevetto industriale + concessioni, licenze e marchi + avviamento + immobilizzazioni in corso + altre immobilizzazioni immateriali. E così via.

 :  : FLD T$C5MA Riclassifica parziale
Se la riclassifica è parziale, allora, in fase di costruzione del file C5FOTO0F ovvero in fase di costruzione del riclassificato, non verranno scritti i record relativi a conti che non sono associati ad alcuna linea della riclassifica.
 :  : FLD T$C5MB Linee senza divisione
Se la riclassifica richiede linee senza divisione, allora, in fase di costruzione del file C5FOTO0F, non verrà scritta la divisione per i record relativi alle totalizzazioni per linea di riclassifica.
 :  : FLD T$C5MF Codice di riclassifica per calcolo %
Se viene riportato un codice di riclassifica valido, nei report di analisi di bilancio, nel calcolo della percentuale (se impostata la modalità di rappresentazione di colonna = OPIIxx) viene utilizzato il valore del saldo del codice di riclassifica riportato.
 :  : FLD T$C5MG Tipo Gestionali
Indica la tipologia di registrazioni gestionali prese in considerazione per la riclassifica. Di defautl viene assunto il valore " 9"
 :  : FLD T$C5MH Tipo Simulate
Indica la tipologia di registrazioni simulate prese in considerazione per la riclassifica. Di defautl viene assunto il valore "03".
 :  : FLD T$C5ML Inversione Valori
Questo campo permette l'inversione di segno dei valori di bilancio :  il dare come negativo e l'avere come positivo. Questa impostazione è prevista per essere funzionale soprattutto invertendo solo i valori del conto economico, per i quali si intende attribuire i costi come voci negative ed i ricavi come voci positive. E' comunque possibile invertire tutti i valori di bilancio per riclassifiche puramente economiche o non invertire nessun valore per riclassifiche di sintesi puramente contabile.

Valori possibili : 
- ' ' = inverte solo i valori del conto economico;
- '1'= inverte sia i valori del conto economico che dello stato patrimoniale;
- '2'= non inverte nessun valore.

 :  : FLD T$C5MM Livello Massimo a 0
Se valorizzato indica il livello massimo di riclassifica per cui una linea viene presentata anche se a 0.
Questo parametro è valido solo per le interrogazioni della riclassifica in loocup.
