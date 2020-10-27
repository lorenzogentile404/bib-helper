bib_file = open('crypto.bib', "r") # Insert here .bib file
bib_content = bib_file.read()

bib_list = bib_content.split('}\n\n@')

while True:
    search_terms = input('Insert search terms: ')

    # Quit
    if search_terms == ':q':
        break

    # Split search terms
    search_terms_list = [search_term.lower() for search_term in search_terms.split()]

    # Count the number of search terms included in each bib_el (not case sensitive)
    result_list = [(bib_el, sum([search_term in bib_el.lower() for search_term in search_terms_list])) for bib_el in bib_list]
    # Filter bib_el containing at least one search term
    result_list = list(filter(lambda e: e[1] >= 1, result_list))
    # Order results by increasing number of search terms contained (relevance)
    result_list = sorted(result_list, key = lambda e: e[1])

    # Print result list
    for e in result_list:
        print('\n@' + e[0] + '}\n')
        print('Relevance: ' + str(e[1]))
