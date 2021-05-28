def tokenizerDebug(self, text):
    """sumary_line

    """
    doc = self(text)
    tok_exp = self.tokenizer.explain(text)
    assert [t.text for t in doc if not t.is_space] == [t[1] for t in tok_exp]
    for t in tok_exp:
        print(t[1], "\t", t[0])