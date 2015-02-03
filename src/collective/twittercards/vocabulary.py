from zope.schema.vocabulary import SimpleVocabulary

twittercards_vocabulary = SimpleVocabulary.fromItems((
    ('Normal Summary', 'summary'),
    ('Large Summary', 'summary_large_image'),
    ('Photo', 'photo'),
    ('Gallery', 'gallery'),
    ('App', 'app'),
    ('Player', 'player'),
    ('Product', 'product')
))
