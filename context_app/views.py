from django.shortcuts import render

# Create your views here.
def home(request):
    d = {
        'author':"rahim ",'age':15,'courses' : [

{
    'id': 1,
    'name':'python',
    'fee':5000,
},
{
    'id': 2,
    'name':'django',
    'fee':10000,
}
        ],
        'lst':['python','is','best']
            
    }
    return render(request,('home.html'),d)
