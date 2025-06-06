# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, StandardItem


class GildedRoseTest(unittest.TestCase):

    def test_normal_item_before_sell_date(self):
        item = Item("Elixir of the Valley", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 9)

    def test_normal_item_on_sell_date(self):
        item = Item("Wine", 0, 5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 3)

    def test_normal_item_after_sell_date(self):
        item = Item("Dust", -3, 6)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -4)
        self.assertEqual(item.quality, 4)

    def test_quality_never_negative(self):
        item = Item("Rusty Sword", 3, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 0)

    def test_aged_brie_before_sell_date(self):
        item = Item("Aged Brie", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 11)

    def test_aged_brie_at_max_quality(self):
        item = Item("Aged Brie", 10, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 50)

    def test_sulfuras_item_does_not_change(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

    def test_backstage_pass_long_before_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 14)
        self.assertEqual(item.quality, 21)

    def test_backstage_pass_ten_days_left(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 22)

    def test_backstage_pass_five_days_left(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 23)

    def test_backstage_pass_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_backstage_pass_at_max_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)

    def test_standard_item_can_be_used_directly(self):
        item = Item("Common Item", 5, 10)
        updater = StandardItem()
        updater.update(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 9)

    def test_item_repr(self):
        item = Item("Elixir", -5, 0)
        self.assertEqual(repr(item), "Elixir, -5, 0")

    def test_aged_brie_reaches_max_quality(self):
        item = Item("Aged Brie", 1, 49)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)

    def test_aged_brie_after_sell_date_and_at_max_quality(self):
        item = Item("Aged Brie", 0, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)

    def test_aged_brie_increases_quality_twice_correctly(self):
        item = Item("Aged Brie", 3, 48)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()  # 49
        self.assertEqual(item.quality, 49)

        gilded_rose.update_quality()  # 50
        self.assertEqual(item.quality, 50)

    def test_aged_brie_increases_quality_after_sell_date_until_max(self):
        item = Item("Aged Brie", -2, 49)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        self.assertEqual(item.sell_in, -3)  # sell_in diminue
        self.assertEqual(item.quality, 50)  # qualité atteint 50

    def test_aged_brie_after_sell_date_continues_to_increase_quality_until_max(self):
        item = Item("Aged Brie", -1, 49)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 50)  # doit passer de 49 à 50 ici

    def test_aged_brie_after_sell_date_increases_quality_below_max(self):
        item = Item("Aged Brie", -3, 48)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        self.assertEqual(item.sell_in, -4)
        self.assertEqual(item.quality, 50)  # Passe de 48 → 50 en un jour

    def test_aged_brie_after_sell_date_increases_quality_twice(self):
        item = Item("Aged Brie", -1, 48)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()  # 49
        gilded_rose.update_quality()  # 50

        self.assertEqual(item.sell_in, -3)
        self.assertEqual(item.quality, 50)

    def test_aged_brie_after_sell_date_starts_at_zero(self):
        item = Item("Aged Brie", -5, 0)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()
        self.assertEqual(item.quality, 2)  # 0 → 2 (car sell_in < 0)

        gilded_rose.update_quality()
        self.assertEqual(item.quality, 4)  # 2 → 4 # Passe directement de 0 à 2 !


if __name__ == "__main__":
    unittest.main()
