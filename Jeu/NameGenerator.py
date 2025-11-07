import random

first_names = ["Alycia", "Désir", "Fleury", "Lilly", "Terry", "Elias", "Noah", "Lina", "Adam", "Sofia", "Yanis", "Maya", "Rayan", "Inès", "Isaac", "Manon", "Paul", "Charles", "Peter", "Ray", "Quentin", "Elie", "Sélène", "Estelle"]
last_names = ["Bennani", "Labussiere", "Rufier", "Galli", "Whycherley", "Abouda", "Raulin", "Reignoux", "Tord", "Paword", "Lepetit", "Reynolds", "Lacroix", "Belkacem", "Dupont", "Morel", "Gomez", "Fischer", "Durand", "Martin", "Leclerc"]

# Function to generate a random full name
def generate_random_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"