def find_anagrams(word, candidates):
    list_found = []
    for candidate in candidates:
        if ''.join(sorted(candidate.lower())) == ''.join(sorted(word.lower())) and not word.isupper():
             list_found.append(candidate)
    return list_found




