from django.shortcuts import render
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from django.http import JsonResponse
import pandas as pd
import json
import numpy as np
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

@api_view(['POST'])
def read_file(request):
    file = request.FILES.get('file')
    df = pd.read_excel(file)
    json_data = df.to_json(orient='records')
    df = json.loads(json_data)
    response_data = {
        'data': df,
    }

    return Response(response_data)
