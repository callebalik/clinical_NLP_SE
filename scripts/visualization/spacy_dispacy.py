from spacy import displacy


def spacy_displacy(doc, style, jupyter=False):
    # styling output from displacy
    colors = {
        "SYM": "linear-gradient(90deg, #99154e, #99154e)",
        "NEG": "linear-gradient(90deg, #ffc93c, #ffc93c)",
    }

    options = {
        "compact": False,
        "bg": "#09a3d5",
        "color": "white",
        "font": "Source Sans Pro",
        "ents": ["SYM", "NEG"],
        "colors": colors,
    }

    # display input with displacy
    displacy.render(doc, style=style, jupyter=jupyter, options=options)
