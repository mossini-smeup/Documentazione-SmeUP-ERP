# GESTIONE PARAMETRI B£J IN MDV
## OBIETTIVI
Leggere e scrivere i parametri di una azione B£J nell'MDV.
## FUNZIONI/METODI (£G70FU/£G70ME)
- READ o blanks -
  Lettura parametri
- WRITE -
  Scrittura parametri
- DELETE -
  Cancellazione parametri

## GRUPPO AZIONI (£G70GA)
Specifica il gruppo azione (B£H) al quale l'azione appartiene.
Serve solo se non viene utilizzato il campo £G70SS.
Se non specificato viene derivato dalla LDA nella posizione 201-210.

## AZIONE (£G70AZ)
Specifica l'azione (B£J) della quale si vogliono gestire i parametri.
Se non specificata viene derivata dalla LDA nella posizione 988-992.

## SS AZIONE (£G70SS)
Specifica il sottosettore della B£J al quale l'azione appartiene.
Se non specificato viene derivato dal gruppo azioni (£G70GA)

## PARAMETRI (£G70PA)
DS lunga 300 contenente l'MDV dei parametri.
Nei programmi basta scrivere sotto la /COPY £G70DS le definizioni
dei campi dei parametri per averli riempiti automaticamente.
Esempio
D/COPY QILEGEN,£G70DS
D  U$TIPA                 1     12
D  U$TROT                13     15
D  U$CODI                16     30
D  U$PERI                31     40
