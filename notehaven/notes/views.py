from django.shortcuts import render

# Create your views here.
def home(request){
    return render(request,'/workspaces/NoteHaven/notehaven/notes/templates/notes/notehaven/public/index.html',{})
}