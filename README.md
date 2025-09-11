# Alberto Fardin | Senior Software Engineer & Creative Director

Sito personale statico con background di particelle e layout minimale. Contiene i link principali e il CV in PDF.

> URL: https://www.albertofardin.it

## Stack tecnico

- HTML5 semantico
- CSS3 (Inter come font da Google Fonts)
- JavaScript vanilla
- [particles.js](https://vincentgarreau.com/particles.js/) come sfondo animato
- Nessun build step. Nessun framework richiesto.

> Nota: `particles.min.js` è servito in locale e inizializzato da `assets/app.js`.
> Non sono richieste chiavi o variabili d'ambiente.

## Personalizzazione

- Colori: modifica le variabili CSS in `:root` dentro `assets/style.css`.
- Particelle: regola le opzioni in `assets/app.js` (numero, dimensione, velocità, interattività).
- Link e testi: modifica le sezioni corrispondenti in `index.html`.
- Font: cambia il link a Google Fonts nel `<head>` se serve un carattere diverso.
