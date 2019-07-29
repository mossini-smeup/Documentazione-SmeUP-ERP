Il componente GEO (Geolocalizzazione) fornisce un'implementazione delle api di Google map.

E' in grado quindi, fornito un xml di tipo matrice, di rappresentare marcatori e aree su diversi tipi di mappa geografica, oltre che fornire possibilità di zoom e navigazione tipiche di google maps.

# Attributi di setup supportati.
Type (default = markers) può assumere i seguenti valori : 
- markers :  imposta i markers alle coordinate o agli indirizzi presenti nella tabella
- polyline :  crea una polilinea tra le coordinate presenti nella tabella
- polygon :  crea un poligono tra le coordinate presenti nella tabella
- circles :  crea dei cerchi alle coordinate presenti nella tabella con raggio uguale al
  valore presente nella tabella
- rectangles :  non implementato in quanto utilizza coordinate sia per l inizio che per   la fine

Latitude :  imposta la latitudine del centro della visualizzazione, se omesso in caso di  type = markers imposta la latitudine media dei markers presenti default = 0;

Longitude :  imposta la longitudine del centro della visualizzazione, se omesso in caso  di type = markers imposta la longitudine media dei markers presenti default = 0;

Zoom :  imposta il fattore di zoom default = 1;

MapType (default = hybrid) può assumere i seguenti valori : 
- hybrid
- satellite
- terrain

LatCol :  nome della colonna della tabella contenete le latitudini;

LngCol :  nome della colonna della tabella contenete le longitudini;

AddCol :  nome della colonna della tabella contenete gli indirizzi che verranno poi  trasformati in coordinate;

IcoCol :  nome della colonna della tabella contenete le immagini;

StyCol :  nome della colonna della tabella contenete lo stile;

TitCol :  nome della colonna della tabella contenete i titoli da visualizzare;

ValCol :  nome della colonna della tabella contenete i valori utilizzati per dimensionare  i raggi dei cerchi quando type=circles;
