# Jak uruchomić

`python3 stegano.py [=e/d]`

jeżeli `-e`
to trzeba wybrać dodatkowo opcje `-m [1/2/3/4]

```py
python3 stegano.py -e -m 1 # endline spaces
python3 stegano.py -e -m 2 # single/double spaces
python3 stegano.py -e -m 3 # literówki w atrybutach
python3 stegano.py -e -m 4 # znaczniki font
```

jeżeli `-d`
to wystaczy tylko ten jeden argument

```py
python3 stegano.py -d
```

> Wiadomość musi być poniżej lub równa 120 bitów

`cover.html` zawiera oryginalny plik html.
`watermark.html` to plik, który jest edytowany by ukryć wiadomość
