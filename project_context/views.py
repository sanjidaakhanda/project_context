from django.shortcuts import render
import datetime
# Create your views here.


def home(request):
    d = {
        'author': "Himi ", 'age': 15,
        'lst': ['I', 'am', 'best'],
        'today': datetime.datetime.now(),
        'v': ["I'm sanjida"],
        'c': ["I am a mother"],
        'n': [" "],
        'names': [

            {'name': 'meher', 'age': 20},
            {'name': 'summer', 'age': 13},
            {'name': 'dua', 'age': 1},
        ],
        'file_sizes': [1024, 4194304, 123],
        'value': ['welcome '],





    }
    return render(request, ('home.html'), d)
