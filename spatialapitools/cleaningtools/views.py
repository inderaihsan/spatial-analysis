from django.shortcuts import render
from rest_framework.decorators import api_view  
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def init(request) :   
    respons_json = {
        'pesan' : 'Django sudah online', 
        'pesan2' : 'Django sudah bisa beroperasi'
    }
    return Response(respons_json)     

@api_view(['POST']) 
def luas_segitiga(request) : 
    alas = request.data['alas']
    tinggi = request.data['tinggi'] 
    luas = 0.5 * alas * tinggi  
    if (luas < 5) : 
        pesan = "lingakaran tidak cukup besar" 
    else : 
        pesan = "lingakaran cukup besar"
    return Response({'pesan' : 'berhasil dihitung!', 
                     'luas' : luas, 
                     'pesanSegitiga' : pesan}) 
    
    
