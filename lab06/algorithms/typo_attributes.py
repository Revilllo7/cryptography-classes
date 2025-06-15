import re

def embed_typo_attributes(cover, bits):
    # Usuwamy literówki
    cover = re.sub(r"margin-botom", "margin-bottom", cover)
    cover = re.sub(r"lineheight", "line-height", cover)
    p_tags = list(re.finditer(r"<p[^>]*>", cover))
    if len(bits) > len(p_tags):
        return None
    result = cover
    offset = 0
    for i, bit in enumerate(bits):
        m = p_tags[i]
        insert = ""
        if bit == "0":
            insert = ' style="margin-botom: 0cm;"'
        else:
            insert = ' style="lineheight: 100%"'
        # Dodaj atrybut do <p>
        pos = m.end() + offset - 1
        result = result[:pos] + insert + result[pos:]
        offset += len(insert)
    return result

def extract_typo_attributes(watermarked):
    bits = ""
    for m in re.finditer(r"<p[^>]*>", watermarked):
        tag = m.group()
        if "margin-botom" in tag:
            bits += "0"
        elif "lineheight" in tag:
            bits += "1"
    return bits