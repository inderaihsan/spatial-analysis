from django.shortcuts import render
from rest_framework.decorators import api_view  
from rest_framework.response import Response
import pandas as pd
import numpy as np
import json 
import geopandas

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
def read_data(request) : 
    file = request.FILES.get('data') 
    df = pd.read_excel(file) 
    numeric_data = df.select_dtypes(include='number')
    numeric_data = numeric_data.columns.to_list()
    categorical_data = df.select_dtypes(exclude='number')
    categorical_data = categorical_data.columns.to_list()
    df = df.to_json(orient='records') 
    df = json.loads(df) 
    respon_data = {
        'data' : df, 
        'numerical' : numeric_data,
        'categorical_data' : categorical_data
    }
    return Response(respon_data)  

@api_view(['POST']) 
def filter_radius(request) : 
    #read -> data uwis 
    #ubah jadi geopandas -> uwis 
    #ubah crs -> 32749 uwis 
    #nangkep request dari postman -> koordinat 
    # longitude = request.data['longitude']
    # latitude = request.data['latitude']
    # #nangkep request dari postman -> radius 
    # radius = request.data['radius']
    #ngitung jarak dari radius ke file geopandas 
    #filter jaraknya sesuai radius -> 
    #return 
    return Response({'data' : 'radius filter'})


    

