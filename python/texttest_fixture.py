"""
Fixture de test fonctionnel pour GildedRose.
Affiche l'état quotidien des items après mise à jour.
"""
import sys
from gilded_rose import Item, GildedRose


def main():
    """
    Fonction principale qui simule la mise à jour quotidienne des items.
    Utilisée par texttest pour vérifier le comportement du système.
    """
    print("OMGHAI!")

    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]

    days = 2


    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print(f"-------- day {day} --------")
        # En-tête avec mise en forme de tableau
        print("name, sell_in, quality")
        # Lignes des items
        for item in items:
            name = item.name.ljust(35)  # Nom aligné à gauche sur 35 caractères
            sell_in = str(item.sell_in).rjust(7)   # sell_in aligné à droite
            quality = str(item.quality).rjust(7)   # quality aligné à droite
            print(f"{name},{sell_in},{quality}")

        print("")  # saut de ligne entre chaque jour


if __name__ == "__main__":
    main()
