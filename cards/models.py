from django.db import models


PHASES = (
    ('Enfrentamiento', 'Enfrentamiento'),
    ('Influencia', 'Influencia'),
)

CARD_TYPES = (
    ('Acción', 'Acción'),
    ('Equipo', 'Equipo'),
    ('Evento', 'Evento'),
    ('Invocación', 'Invocación'),
    ('Panteón', 'Panteón'),
    ('Personaje', 'Personaje'),
    ('Recurso', 'Recurso'),
)



class Era(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Mythology(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length=200)
    phase = models.CharField(max_length=20, choices=PHASES)

    def __str__(self):
        return f'{self.phase}: {self.name}'


class Card(models.Model):
    abilities = models.ManyToManyField(Ability)
    card_type = models.CharField(max_length=20, choices=CARD_TYPES)
    cost = models.IntegerField(blank=True, null=True)
    eras = models.ManyToManyField(Era)
    init_pow = models.IntegerField(blank=True, null=True)
    max_pow = models.IntegerField(blank=True, null=True)
    mythology = models.ForeignKey(Mythology, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    passive_effect = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=300, blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    image = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

    def _tags(self):
        return ', '.join([tag.name for tag in self.tags.all()])
    _tags.short_description = 'Tags'

    def _abilities(self):
        return '\n'.join([str(a) for a in self.abilities.all()])
    _abilities.short_description = 'Abilities'

    def _eras(self):
        return '/'.join([str(era) for era in self.eras.all()])
    _eras.short_description = 'Eras'
