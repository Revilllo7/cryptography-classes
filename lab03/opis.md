## Struktura projektu / Project Structure

`main.py` Main. Pobiera argumenty od użythownika
`img_process.py` Ładuje image, rozcina go na bloki i potem łączy
`cipher.py` Logika ECB i CBC
`utils.py` Ładuje klucz lub daje domyślną wartość pustego stringa
`plain.bmp` Obraz
`key.txt` (optional) Opcjonalny plik klucza

---

## Wynik / Output

Program daje dwa outputy w postaci zdjęć

- `ecb_crypto.bmp` – Zaszyfrowany ECB.
- `cbc_crypto.bmp` – Zaszyfrowany CBC.

---

## Jak uruchomić / How to Run

### Wymagania / Requirements

- Python 3.7+
- Pillow
- NumPy

Zainstalowanie wymaganych paczek:

```bash
pip install pillow numpy
```
