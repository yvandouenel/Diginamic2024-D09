simple_quote = 'En simple "quote", on doit échapper l\'apostrophe'

simple_quote = (
    "Avec une simple quote, je ne peux pas passer à la ligne \n sauf à échapper n..."
)
print(simple_quote)

double_quote = """Je suis une chaine  
mais je peux m'étendre sur plusieurs lignes"""
print(double_quote)

simple_quote_triple = """Même chose, et le truc cool
c'est que je n'ai plus besoin
d'échapper les apostrophes!"""
print(simple_quote_triple)

raw_string = r"Je suis une raw string,\nsans passage à la ligne!"

print(raw_string)

path = "C:\\test\\moto"
print(path)
