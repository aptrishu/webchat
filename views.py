from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

from documents.models import Document
from jchat.models import Room

@login_required
def index(request):
    """Index page, force login here"""
    return render_to_response('index.html', {'documents':Document.objects.all()})

@login_required
def simple(request):
    """Simple chat room demo, it is not attached to any other models"""
    # get the chat instance that was created by the fixture, pass the id to the template and you're done!
    return render_to_response('simple.html', {'chat_id':Room.objects.get(id=1).id}) 

@login_required
def complex(request, id):
    """Complex chat room demo, it uses the RoomManager to get the instance associated to the object"""
    
    # get the document requested by the url
    doc = get_object_or_404(Document, id=id)
    # get *or create* a chat room attached to this document
    room = Room.objects.get_or_create(doc)
    
    return render_to_response('complex.html', {'document':doc, 'chat_id':room.id})  