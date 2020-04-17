from django.shortcuts import render

# Create your views here.

def home_screen_view(request):

     context = {}
     list_of_values=[]
     list_of_values.append("first entry")
     list_of_values.append("second entry")
     list_of_values.append("third entry")
     list_of_values.append("fourth entry")
     context['list_of_values'] = list_of_values

     #context['some_string']="This is some string that Im passing to the view"
     #context['some_number']=860623

    



     return render (request, "personal/home.html", context )
