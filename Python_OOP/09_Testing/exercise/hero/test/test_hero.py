from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Adam", 10, 100.0, 10.0)
        self.enemy = Hero("Eve", 10, 100.0, 10.0)

    def test_init_works_correct(self):
        self.assertEqual("Adam", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)

    def test_battle_fight_yourself_exception(self):
        with self.assertRaises(Exception) as ve:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ve.exception))

    def test_battle_health_less_than_zero_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_needs_to_rest_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight Eve. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_battle_you_win(self):
        self.hero.health += 100
        result = self.hero.battle(self.enemy)
        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(105, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_you_lose(self):
        self.enemy.health += 100
        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(105, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test_str_method(self):
        expected = f"Hero Adam: 10 lvl\nHealth: 100.0\nDamage: 10.0\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    main()
