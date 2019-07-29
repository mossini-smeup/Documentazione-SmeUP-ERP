# Dati di Input

* Tipi Oggetto 1 Previsti : 
** Q3
** OG
** LI
** VD
** OJ*FILE

* Parametri
** NoFlt :  Disattiva il controllo del filtro di JOB
** NoCnt :  Disattiva il calcolo del n° di righe (viene eseguita solo la Distinct)
** NRW :  N° Righe per Pagina (Assume 5000)

* Parametri INPUT
** WHR :  Stringa WHERE SQL libera che va ad aggiungersi alla WHERE dell'oggettp
** LI :  Definizione di una LISTA, la cui WHERE corrispondente va ad aggiungersi alla WHERE dell'oggetto, la struttura per questo campo è la seguente :  LI(TipoOggetto;NomeLista;NomeCampoFile)
** DDWN :  Parametro di Drill Down con la struttura prevista dal B£SER_83 - FLDn(Nome Campo) VALn(Valore) OPEn(Operazione)
** Context :  Stringa che va ad aggiungersi al codice Context costruito dal pgm

# CONTEXT

* Composto da : 
** B£SER_84
** £UIBME
** Nome file
** Campo
** Nome Tracciato
** Eventuale stringa passata con il parametro Context

# Determinazione Elenco dei Campi Utilizzabili

* Viene assunto lo schema T/BAR (Barratore) dell'oggetto se esiste, in alternativa tutti i campi del file corrispondente all'oggetto

