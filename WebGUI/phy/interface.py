from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django_range_slider.fields import RangeSliderField


class WebInt(forms.Form):
    # Slider Button for angle range
    slider = RangeSliderField(label="Select angle range", minimum=0, maximum=360)

    # Radio Button to select plot option
    select_an_option = forms.ChoiceField(choices=[
        ('seperate', 'Seperate'),
        ('overlap', 'Overlap')],
        widget=forms.RadioSelect)

    # Choice Field to Select the Plot
    select_the_plot = forms.ChoiceField(choices=[
        ('Polarizer angle vs Unit Intensity', 'Polarizer angle vs Unit Intensity'),
        ('HWP angle vs Unit Intensity', 'HWP angle vs Unit Intensity'),
        ('QWP angle vs Unit Intensity', 'QWP angle vs Unit Intensity'),
        ('P3 angle vs Unit Intensity', 'P3 angle vs Unit Intensity'),
        ('P4 angle vs Unit Intensity', 'P4 angle vs Unit Intensity'),
    ]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'select_an_option',
            'select_the_plot',
            'slider',
            Submit('submit', 'OK', css_class='btn-success')
        )
