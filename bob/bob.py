def hey(phrase):
    phrase = phrase.strip()

    if not phrase:
        return "Fine. Be that way!"
    elif phrase.endswith("?"):
        if phrase.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif phrase.isupper():
        return "Whoa, chill out!"
    return "Whatever."
