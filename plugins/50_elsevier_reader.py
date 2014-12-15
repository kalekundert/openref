import re
    
@metadata_reader('elsevier')
def elsevier_reader(pdf, citation):
    citation.author = pdf_info.get('Author', '')
    citation.title = pdf_info.get('Title', '')

    pdf_match = re.match(
            '(?P<journal>\w+),\s+'
            '(?P<volume>\w+)\s+'
            '\((?P<year>\d{4})\)\s+'
            '(?P<pages>\d+-\d+)\.'
            , pdf_info.get('Subject', ''))

    if pdf_match:
        citation.journal = pdf_match.group('journal')
        citation.volume = pdf_match.group('volume')
        citation.year = pdf_match.group('year')
        citation.pages = pdf_match.group('pages')
