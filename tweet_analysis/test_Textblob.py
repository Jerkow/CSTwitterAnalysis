import tweet_analysis.Textblob as TB

data = {'tweet_textual_content': ['Je suis un Francais et je vais dans l\'espace alors c\'est super','Et oui c\'est cool ça']}

def test():
    assert TB.vocabulaire(data) == {'Et', 'oui', 'suis', 'cool', "l'espace", 'super', 'Francais', 'vais'}

