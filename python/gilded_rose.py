"""-*- coding: utf-8 -*-
Module pour gérer la mise à jour des items du jeu Gilded Rose."""

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods,too-many-instance-attributes
class Item:
    """Représente un item du jeu Gilded Rose."""

    def __init__(self, name: str, sell_in: int, quality: int):
        """Initialise un item avec son nom, sa date de péremption (sell_in) et sa qualité."""
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        """Représentation de l'item pour le débogage."""
        return f"{self.name}, {self.sell_in}, {self.quality}"


class Updateable(ABC):
    """Interface abstraite pour les mises à jour de qualité d'un item."""

    @abstractmethod
    def update(self, item: Item) -> None:
        # pylint: disable=unnecessary-pass
        """Met à jour l'item selon sa logique spécifique."""
        pass


class StandardItem(Updateable):
    """Met à jour les items standards : la qualité diminue avec le temps."""

    def update(self, item: Item) -> None:
        """Met à jour la qualité et la date de péremption d'un item standard."""
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        # pylint: disable=chained-comparison
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1
        # pylint: enable=chained-comparison


class AgedBrieItem(Updateable):
    """Aged Brie : plus il vieillit, meilleure est sa qualité (jusqu'à 50)."""

    def update(self, item: Item) -> None:
        """Met à jour la qualité et la date de péremption d'Aged Brie."""
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class SulfurasItem(Updateable):
    """Sulfuras est un objet légendaire qui ne change jamais."""

    def update(self, item: Item) -> None:
        # pylint: disable=unnecessary-pass
        """Ne fait rien car Sulfuras ne change jamais."""
        pass


class BackstagePassItem(Updateable):
    """Backstage Pass : qualité augmente selon les jours restants jusqu'au concert."""

    def update(self, item: Item) -> None:
        """Met à jour la qualité et la date de péremption des Backstage Pass."""
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = min(item.quality + 3, 50)
        elif item.sell_in <= 10:
            item.quality = min(item.quality + 2, 50)
        else:
            item.quality = min(item.quality + 1, 50)

        item.sell_in -= 1


class GildedRose:
    """Gère la mise à jour quotidienne des items du magasin."""

    def __init__(self, items: list[Item]):
        """Initialise le magasin avec une liste d'items."""
        self.items = items

    def update_quality(self):
        """Met à jour la qualité de tous les items."""
        for item in self.items:
            updater = self._get_updater(item)
            updater.update(item)

    def _get_updater(self, item: Item) -> Updateable:
        """Retourne la bonne stratégie de mise à jour en fonction du nom de l'item."""
        if item.name == "Aged Brie":
            return AgedBrieItem()
        elif item.name.startswith("Backstage passes"):
            return BackstagePassItem()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasItem()
        else:
            return StandardItem()
