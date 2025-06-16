# Podstawy Kryptografii Podsumowanie laboratorium

[English version 🇬🇧](#cryptography-classes-lab-overview)

## Lab 01 – Szyfry klasyczne: Cezar i Afiniczny

**Cel:**  

Poznanie klasycznych szyfrów podstawieniowych: Cezara i afinicznego.  

**Co zrobiłem:**  
- Zaimplementowałem szyfrowanie i deszyfrowanie szyfrem Cezara i afinicznym ([lab01/cipher.py](lab01/cipher.py)).
- Dodałem obsługę plików wejściowych/wyjściowych ([lab01/files.py](lab01/files.py)).
- Napisałem narzędzia do kryptoanalizy z tekstem jawnym i bez ([lab01/crypto_analysis.py](lab01/crypto_analysis.py)).
- Przygotowałem pliki z danymi testowymi ([lab01/data/](lab01/data/)).

**Czego się nauczyłem:**  
- Zasad działania szyfrów podstawieniowych.
- Znaczenia klucza i jego łamania przez analizę tekstu jawnego i kryptoanalizę.

## Lab 02 – XOR i kryptoanaliza

**Cel:** 

Zrozumienie działania szyfru XOR oraz podstaw kryptoanalizy przy wielokrotnym użyciu tego samego klucza.  

**Co zrobiłem:**  

- Zaimplementowałem narzędzie do przygotowania, szyfrowania, kryptoanalizy i czyszczenia plików ([lab02/xor.py](lab02/xor.py)).
- Przeprowadziłem atak na szyfr XOR przy wielokrotnym użyciu tego samego klucza.

**Czego się nauczyłem:**  
- Jak działa szyfr XOR i dlaczego nie należy używać tego samego klucza wielokrotnie.
- Podstawy ataków na szyfry strumieniowe.

## Lab 03 – Szyfrowanie blokowe obrazów (ECB, CBC)

**Cel:**  

Zastosowanie trybów szyfrowania blokowego (ECB, CBC) na obrazach.  

**Co zrobiłem:**  
- Zaimplementowałem ładowanie, dzielenie na bloki i składanie obrazów ([lab03/img_process.py](lab03/img_process.py)).
- Zaimplementowałem szyfrowanie blokowe z użyciem funkcji skrótu ([lab03/cipher.py](lab03/cipher.py)).
- Przygotowałem program główny do obsługi trybów ECB i CBC ([lab03/main.py](lab03/main.py)).

**Czego się nauczyłem:**  

- Różnic między trybami ECB i CBC.
- Wpływu trybu szyfrowania na bezpieczeństwo i wygląd zaszyfrowanego obrazu.

## Lab 04 – Właściwości funkcji skrótu

**Cel:**  
Analiza funkcji skrótu pod kątem lawinowości i odporności na kolizje.  

**Co zrobiłem:**  

- Porównałem wyniki różnych funkcji skrótu dla podobnych danych ([lab04/diff.py](lab04/diff.py), [lab04/diff.txt](lab04/diff.txt), [lab04/hash.txt](lab04/hash.txt)).
- Przeanalizowałem liczbę różniących się bitów w skrótach.

**Czego się nauczyłem:**  
- Działania efektów lawinowych w funkcjach skrótu.
- Jak oceniać odporność funkcji skrótu na kolizje.

## Lab 05 – Szyfrowanie i podpis cyfrowy ElGamal

**Cel:**  

Poznanie algorytmu ElGamal do szyfrowania i podpisu cyfrowego.

**Co zrobiłem:**  
- Zaimplementowałem generowanie kluczy, szyfrowanie, deszyfrowanie, podpisywanie i weryfikację ([lab05/elegamal.py](lab05/elegamal.py), [lab05/logic/](lab05/logic/)).
- Przetestowałem poprawność działania na przykładowych danych.

**Czego się nauczyłem:**  
- Jak działa szyfrowanie i podpis cyfrowy ElGamal.
- Znaczenie losowości i bezpieczeństwa kluczy.

## Lab 06 – Steganografia w HTML

**Cel:**  

Ukrywanie informacji w plikach HTML różnymi metodami steganograficznymi.

**Co zrobiłem:**  

- Zaimplementowałem 4 metody ukrywania bitów w HTML ([lab06/stegano.py](lab06/stegano.py), [lab06/algorithms/](lab06/algorithms/)):
  - Spacje na końcu linii
  - Pojedyncza/podwójna spacja
  - Literówki w atrybutach
  - Specjalne znaczniki FONT
- Przygotowałem pliki testowe ([lab06/cover.html](lab06/cover.html), [lab06/watermark.html](lab06/watermark.html)).

**Czego się nauczyłem:**  

- Różne techniki steganografii tekstowej.
- Ograniczenia i wykrywalność ukrywania informacji w HTML.



## Lab 07 – PGP: Klucze, podpisy, szyfrowanie

**Cel:**  

Praktyczne użycie narzędzi PGP do generowania kluczy, podpisywania, szyfrowania i weryfikacji.  

**Co zrobiłem:**  

- Wygenerowałem własną parę kluczy PGP ([lab07/task01/0xA02CECDA.asc](lab07/task01/0xA02CECDA.asc)).
- Podpisałem i zaszyfrowałem pliki, przeprowadziłem import i analizę kluczy ([lab07/task02/](lab07/task02/), [lab07/task03/](lab07/task03/), [lab07/task04/](lab07/task04/)).
- Przećwiczyłem eksport, import, podpisywanie, szyfrowanie i weryfikację podpisów.

**Czego się nauczyłem:**  

- Praktycznych aspektów zarządzania kluczami PGP.
- Działania podpisów cyfrowych i szyfrowania plików w PGP.
- Znaczenia bezpieczeństwa kluczy i poprawnej weryfikacji tożsamości.

---

# Cryptography classes Lab overview

## Lab 01 – Classical ciphers: Caesar and Affine

**Goal:**  

To learn about classical substitution ciphers: Caesar and affine.  

**What I did:**  
- Implemented encryption and decryption using Caesar and affine ciphers ([lab01/cipher.py](lab01/cipher.py)).
- Added input/output file handling ([lab01/files.py](lab01/files.py)).
- Wrote tools for cryptanalysis with and without known plaintext ([lab01/crypto_analysis.py](lab01/crypto_analysis.py)).
- Prepared test data files ([lab01/data/](lab01/data/)).

**What I learned:**  
- The principles of substitution ciphers.
- The importance of the key and how to break it using plaintext analysis and cryptanalysis.

## Lab 02 – XOR and cryptanalysis

**Goal:** 

Understanding the XOR cipher and basics of cryptanalysis when the same key is reused.  

**What I did:**  

- Implemented a tool for preparing, encrypting, cryptanalyzing, and cleaning files ([lab02/xor.py](lab02/xor.py)).
- Performed an attack on the XOR cipher with key reuse.

**What I learned:**  
- How the XOR cipher works and why key reuse is insecure.
- Basics of attacks on stream ciphers.

## Lab 03 – Block cipher image encryption (ECB, CBC)

**Goal:**  

Applying block cipher modes (ECB, CBC) to images.  

**What I did:**  
- Implemented image loading, splitting into blocks, and merging ([lab03/img_process.py](lab03/img_process.py)).
- Implemented block encryption using hash functions ([lab03/cipher.py](lab03/cipher.py)).
- Prepared a main program for ECB and CBC modes ([lab03/main.py](lab03/main.py)).

**What I learned:**  

- Differences between ECB and CBC modes.
- The impact of cipher mode on security and the appearance of the encrypted image.

## Lab 04 – Hash function properties

**Goal:**  
Analysis of hash functions in terms of avalanche effect and collision resistance.  

**What I did:**  

- Compared results of different hash functions for similar data ([lab04/diff.py](lab04/diff.py), [lab04/diff.txt](lab04/diff.txt), [lab04/hash.txt](lab04/hash.txt)).
- Analyzed the number of differing bits in hashes.

**What I learned:**  
- How the avalanche effect works in hash functions.
- How to assess the collision resistance of hash functions.

## Lab 05 – ElGamal encryption and digital signature

**Goal:**  

Learning the ElGamal algorithm for encryption and digital signatures.

**What I did:**  
- Implemented key generation, encryption, decryption, signing, and verification ([lab05/elegamal.py](lab05/elegamal.py), [lab05/logic/](lab05/logic/)).
- Tested correctness on sample data.

**What I learned:**  
- How ElGamal encryption and digital signatures work.
- The importance of randomness and key security.

## Lab 06 – Steganography in HTML

**Goal:**  

Hiding information in HTML files using various steganographic methods.

**What I did:**  

- Implemented 4 methods for hiding bits in HTML ([lab06/stegano.py](lab06/stegano.py), [lab06/algorithms/](lab06/algorithms/)):
  - Spaces at the end of lines
  - Single/double spaces
  - Typos in attributes
  - Special FONT tags
- Prepared test files ([lab06/cover.html](lab06/cover.html), [lab06/watermark.html](lab06/watermark.html)).

**What I learned:**  

- Various text steganography techniques.
- Limitations and detectability of hiding information in HTML.

## Lab 07 – PGP: Keys, signatures, encryption

**Goal:**  

Practical use of PGP tools for key generation, signing, encryption, and verification.  

**What I did:**  

- Generated my own PGP key pair ([lab07/task01/0xA02CECDA.asc](lab07/task01/0xA02CECDA.asc)).
- Signed and encrypted files, performed key import and analysis ([lab07/task02/](lab07/task02/), [lab07/task03/](lab07/task03/), [lab07/task04/](lab07/task04/)).
- Practiced export, import, signing, encryption, and signature verification.

**What I learned:**  

- Practical aspects of PGP key management.
- How digital signatures and file encryption work in PGP.
- The importance of key security and proper identity verification.

---
---
---