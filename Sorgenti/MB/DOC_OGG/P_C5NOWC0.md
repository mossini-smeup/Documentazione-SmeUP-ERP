# Impostazione analitica
Gestisce l'impostazione dei dettagli di analitica per ciascun conto contabile.

_9_La gestione dell'analitica è definita dalle seguenti tabelle : 
* "C52" Attivazione analitica
* "C5B" Attivazione analitica sul conto contabile
* "C6B" Struttura analitica del conto contabile
* Il modello è gestito nello stesso archivio dell'analitica con azienda "**"

_9_Opzioni
* "02" Gestione tabella "C5B" Piano dei conti
* "11"/"12"/"!4"/"15"  Gestione tabella "C6B" Struttuta conto contabile
* "21"/"22"/"24"/"25"  Gestione modelli di analitica

_9_Legenda
Colonna A :  indica se il conto è definito di analitica sulla tabella "C5B"
Colonna S :  indica se è presente la struttutra, tabella "C6B"
Colonna M :  indica se è presente il modello, può assumere dev valori : 
* M se il modello è definito sul conto contabile in essere;
* D se il modello è definito di risalita come modello del conto contabile presente nella   sua struttura :  Campo "Modello da conto" in tabella "C6B"
