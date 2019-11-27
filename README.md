# protabletochki

### Project setup
Run
`pip install -r requirements.txt`.

### Modules
`parser.py` parses website [ПроТаблетки](https://protabletky.ru) and saves 
articles concerning some drug to file `drugs.json`.

`choose_drugs.py` parses the same website and chooses drugs with the most number
of comments.

`translator.py` gets text from json file, by default `drugs.json`, translates the fields that need to be translated
and writes the output to other file, by default `drugs_en.json`.

`tokenizator.py` gets text from json file, by default `drugs_en.json`, normalize the fields that need to be normalized
and writes the output to other file, by default `drugs_token.json`.

`json_utils.py` contains functions to read and write JSON to/from file.

[Cтатья](https://docs.google.com/document/d/1aj9DaP0IygpUmQsxu24yj5ePrehVejW8jn-K_B3qpd4/mobilebasic)
