import re

def embed_font_tags(cover, bits):
    # Usuwamy podwójne fonty
    cover = re.sub(r"<FONT></FONT>", "", cover, flags=re.IGNORECASE)
    font_tags = list(re.finditer(r"<FONT[^>]*>", cover, flags=re.IGNORECASE))
    if len(bits) > len(font_tags):
        return None
    result = cover
    offset = 0
    for i, bit in enumerate(bits):
        m = font_tags[i]
        if bit == "1":
            # otwarcie-zamknięcie-otwarcie
            insert = m.group() + "</FONT>" + m.group()
            pos = m.start() + offset
            result = result[:pos] + insert + result[m.end()+offset:]
            offset += len(insert) - (m.end() - m.start())
        else:
            # po zamknięciu doklej pustą parę
            close_tag = "</FONT>"
            pos = result.find(close_tag, m.end()+offset)
            if pos != -1:
                result = result[:pos+len(close_tag)] + "<FONT></FONT>" + result[pos+len(close_tag):]
                offset += len("<FONT></FONT>")
    return result

def extract_font_tags(watermarked):
    bits = ""
    # Szukamy sekwencji otwarcie-zamknięcie-otwarcie lub pustych par po zamknięciu
    # uproszczona wersja
    i = 0
    while i < len(watermarked):
        if watermarked[i:i+6].upper() == "<FONT>":
            if watermarked[i+6:i+13].upper() == "</FONT>":
                if watermarked[i+13:i+19].upper() == "<FONT>":
                    bits += "1"
                    i += 19
                else:
                    bits += "0"
                    i += 6
            else:
                i += 6
        else:
            i += 1
    return bits.rstrip("0")