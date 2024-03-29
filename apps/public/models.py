from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

###
### The below @receiver is a Python decorator. Decorators can alter the way
### that methods work. This one in particular listens for anytime a User object is
### saved, and if it is just being created, it creates a new security token associated
### with that user. These tokens are used for the REST Framework, and allow us to 
### track who is logged in and allow different permissions per user
###
###

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


###
### Below is an example of a model. Uncomment to see it in action.
### When you create a new model, you must create a new schema migration
### [ python manage.py schemamigration __YOUR-APP-NAME__ --auto ]
### Once the migration is created, you then have to apply it with:
### [ python manage.py migrate ]
###

# class Address(models.Model):
#     ''' Model features for an address '''
#     street = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     state = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)

#     def __unicode__(self):
#         return u'%s, %s, %s' % (self.street, self.city, self.state)

#     class Meta:
#         verbose_name_plural = 'Addresses'

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    glycemic_index = models.IntegerField()


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    ingredients = models.ManyToManyField('Ingredient')
    cook_time = models.CharField(max_length=50)
    COOK_METHODS = (
        ('bake', 'Bake in the Oven'),
        ('microwave', 'Microwave'),
        ('fry', 'Fry'),
        ('dutch_oven', 'Dutch Oven'),
        ('outside_grill', 'Grill'),
        ('boil', 'Boil'),
        ('none', 'Nothing'),
    )
    cook_method = models.CharField(max_length=50, choices=COOK_METHODS)

    def __unicode__(self):
        return self.name

