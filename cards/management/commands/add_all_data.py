import pathlib

from django.core.management.base import BaseCommand
import yaml

from cards.models import Card, Ability, Tag, Era, Mythology


class Command(BaseCommand):
    help = 'Add all cards to the database'

    def handle(self, *args, **options):

        self._delete_all_data()

        eras = self._load_eras()
        mythologies = self._load_mythologies()
        tags = self._load_tags()

        self._load_cards(eras, mythologies, tags)

        print('Done!!!')

    def _delete_all_data(self):

        Card.objects.all().delete()
        Ability.objects.all().delete()
        Tag.objects.all().delete()
        Era.objects.all().delete()
        Mythology.objects.all().delete()

    def _load_eras(self):

        with open('cards/all_data/eras.yaml') as f:
            eras = yaml.safe_load(f)['eras']

        result = {}
        for name in eras:
            result[name] = Era.objects.create(name=name)

        return result

    def _load_mythologies(self):

        with open('cards/all_data/mythologies.yaml') as f:
            mythologies = yaml.safe_load(f)['mythologies']

        result = {}
        for name in mythologies:
            result[name] = Mythology.objects.create(name=name)

        return result

    def _load_tags(self):

        with open('cards/all_data/tags.yaml') as f:
            tags = yaml.safe_load(f)['tags']

        result = {}
        for name in tags:
            result[name] = Tag.objects.create(name=name)

        return result

    def _load_cards(self, eras, mythologies, tags):

        path = pathlib.Path('cards/all_data/cards/').glob('*.yaml')

        for file in path:
            with open(file) as f:
                card = yaml.safe_load(f)
                c = Card(
                    name=card['name'],
                    card_type=card['card_type'],
                    cost=card['cost'],
                    strength=card['strength'],
                    max_pow=card['max_pow'],
                    init_pow=card['init_pow'],
                    mythology=mythologies[card['mythology']] if card['mythology'] else None,
                    passive_effect=card['passive_effect'],
                    quote=card['quote'],
                    image=card['image']
                )

                c.save()

                for era in card['eras']:
                    c.eras.add(eras[era])

                if card['tags']:
                    for tag in card['tags']:
                        c.tags.add(tags[tag])

                if card['abilities']:
                    for ab in card['abilities']:
                        for p, a in ab.items():
                            ability = Ability.objects.create(name=a, phase=p)
                            c.abilities.add(ability)
