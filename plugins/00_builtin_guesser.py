@type_guesser
def builtin_guesser(pdf):
    try: return pdf_info['Creator'].lower()
    except: return None
