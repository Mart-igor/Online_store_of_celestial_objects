from django import forms

CELESTIAL_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]

class CartAddCelestialForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CELESTIAL_QUANTITY_CHOICES,
                                      coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)