from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Race, CharacterClass, Character


class RaceModelTest(TestCase):
    def setUp(self):
        self.race = Race.objects.create(name="Elf")

    def test_race_name(self):
        self.assertEqual(str(self.race), "Elf")

    def test_race_unicode(self):
        self.assertEqual(self.race.__str__(), "Elf")

    def test_race_model(self):
        self.assertIsInstance(self.race, Race)


class CharacterClassModelTest(TestCase):
    def setUp(self):
        self.character_class = CharacterClass.objects.create(name="Wizard")

    def test_character_class_name(self):
        self.assertEqual(str(self.character_class), "Wizard")

    def test_character_class_unicode(self):
        self.assertEqual(self.character_class.__str__(), "Wizard")

    def test_character_class_model(self):
        self.assertIsInstance(self.character_class, CharacterClass)


class CharacterModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com"
        )
        self.race = Race.objects.create(name="Elf")
        self.character_class = CharacterClass.objects.create(name="Wizard")
        self.character = Character.objects.create(
            name="Gandalf",
            race=self.race,
            character_class=self.character_class,
            player=self.user,
        )

    def test_character_name(self):
        self.assertEqual(str(self.character), "Gandalf")

    def test_character_unicode(self):
        self.assertEqual(self.character.__str__(), "Gandalf")

    def test_character_model(self):
        self.assertIsInstance(self.character, Character)

    def test_character_absolute_url(self):
        expected_url = f"/character/{self.character.pk}/"
        self.assertEqual(self.character.get_absolute_url(), expected_url)

    def test_character_default_values(self):
        self.assertEqual(self.character.strength, 10)
        self.assertEqual(self.character.dexterity, 10)
        self.assertEqual(self.character.constitution, 10)
        self.assertEqual(self.character.intelligence, 10)
        self.assertEqual(self.character.wisdom, 10)
        self.assertEqual(self.character.charisma, 10)
        self.assertEqual(self.character.max_hit_points, 10)
        self.assertEqual(self.character.current_hit_points, 10)

    def test_character_player(self):
        self.assertEqual(self.character.player, self.user)
