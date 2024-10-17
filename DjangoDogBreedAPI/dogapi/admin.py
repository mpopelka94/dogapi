from django.contrib import admin
from .models import Dog, Breed

# Register your models here.
class DogAdmin(admin.ModelAdmin):

    # Define the list of fields to display in the admin interface
    list_display = ('name', 'age', 'breed', 'gender', 'color', 'favoritetoy', 'favoritefood')

    # Add search functionality for specific fields
    search_fields = ('name', 'breed')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('age', 'breed')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name',)

    # Define how fields are displayed when editing a Dog instance
    fields = ('name', 'age', 'breed', 'gender', 'color', 'favoritetoy', 'favoritefood')

class BreedAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')

    # Add search functionality for specific fields
    search_fields = ('name', 'size')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('name', 'size')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name',)

    #Define how fields are displayed when entering a Breed instance
    fields = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')

admin.site.register(Dog,DogAdmin)
admin.site.register(Breed,BreedAdmin)