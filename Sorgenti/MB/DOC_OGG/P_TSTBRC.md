# Generalità
La funzione £BRC esegue la ricerca ed il controllo delle configurazioni, con la possibilità, di richiamare, dall'interno di essa, ulteriori funzioni.
Si veda anche la documentazione delle tabelle BRC e C£B.
# Funzioni / Metodi
La funzione da eseguire nei programmi è sempre la CTR (Controllo) col metodo MAN (Manutenzione) o INT (Interrogazione), a seconda della modalità del richiamo.
Tutte le altre funzioni sono richiamate dall'interno, tramite caratteri speciali : 
-    se la configurazione inizia con '%' vengono presentate le funzioni interne possibili, in base al metodo di richiamo e al tipo di BRC.
-    se la configurazione inizia con '?' viene eseguita la ricerca alfabetica delle configurazioni.
# Articolo
# Modello
E' un parametro di input :  è l'elemento della tabella BRC che definisce il modello della configurazione.
# Configurazione
# Nota
E' un parametro di output :  nel caso si sia scelta una configurazione codificata contiene la sua descrizione.
# Esempi di utilizzo
Manutenzione articoli
La routine viene eseguita solo se la BRC del formato video è valida o blanks. Se è blanks la configurazione è un campo libero. Se è valida si prevedono i seguenti casi : 
 * Configurazione orizzontale, La sua costruzione può essere guidata da un flusso di costruzione campi (B£F) o da una tabella di gestione varianti (C£P). Può essere di due tipi : 
 ** Non codificata :  è sostanzialmente un'estensione del codice articolo, significativa in presenza di gruppo distinta o gruppo ciclo :  va memorizzata nel campo di configurazione dell'anagrafica.
 ** Codificata :  serve nel caso in cui l'articolo può essere prodotto in diverse versioni, definite a priori.
Va memorizzata nell'archivio configurazioni, nell'anagrafica articoli può essere inserita opzionalmente una configurazione tra quelle memorizzate, nel qual caso rappresenta la configurazione proposta.
 * Configurazione verticale; La sua costruzione può essere guidata da un archivio di domande/risposte o da una famiglia di parametri (entrambi intestati alla coppia articolo/configurazione).
 ** Può essere solo codificata :  valgono le stesse considerazioni di quella orizzontale, con la differenza che in questo caso il codice è sempre una sigla (ed al massimo può essere di 15 caratteri), mentre le informazioni sono contenute nello sviluppo (di domande/risposte o parametri).


## Configurazione implicita
Un articolo può essere intestatario di un gruppo di domande e di parametri (comandati dal contenuto della BRA). Essi possono assumere il significato di estensione del codice, quindi equipararsi ad una configurazione orizzontale non codificata.

## Interrogazione articoli
Riceve l'articolo, la BRC e la configurazione. Se la BRC è blanks la configurazione è totalmente libera. In caso contario, se la configurazione  è blanks viene proposta quella dell'articolo
 * Se la configurazione non è codificata : 
 ** se inizia con  % vengono presentate le funzioni di costruzione e di verifica.
 * Se la configurazione è codificata : 
 ** se inizia con ? vengono presentate le configurazioni codificate.
 ** (????) se inizia con % vengono presentate le funzioni di costruzione e di verifica.
 ** viene controllato che sia una configurazione valida tra quelle codificate.

## Manutenzione righe documenti
Stesso comportamento dell'interrogazione articoli, con in più la possibilità di configurazione implicita (alle righe documenti si possono collegare parametri o domande/risposte).

## Interrogazione righe documenti
Da vedere :  come permettere la decodifica della configurazione (Carattere di prosecuzione).

## Scansione distinta e ciclo
Le scansioni ricevono la configurazione e la usano per selezionare o ridefinire il record (legame o operazione), in funzione del criterio di selezione BRS codificato nel record stesso.
Tale criterio dovrà essere uno dei seguenti : 
 * Configurazione orizzontale
 * Configurazione verticale
 ** a domande/risposte
 ** a parametri

Ciascuna partendo da uno di questo oggetti : 
 * anagrafica articolo.
 * configurazione ricevuta.
 * oggetto esterno ricevuto (ad esempio una riga di V5).
