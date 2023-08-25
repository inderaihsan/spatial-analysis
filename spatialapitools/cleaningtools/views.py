from django.shortcuts import render
from rest_framework.decorators import api_view  
from rest_framework.response import Response
import pandas as pd
import numpy as np
import json
import geopandas as gpd
from shapely.geometry import Point
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import pandas as pd
import tempfile
import os

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
def radius_filter(request) :
    file = request.FILES.get('file') 
    print('Radius_filter')
    df = pd.read_excel(file)
    geometry = gpd.points_from_xy(df['longitude'], df['latitude'])
    data = gpd.GeoDataFrame(df, geometry =geometry)
    data.set_crs(epsg = 32749, inplace = True)
    data.to_crs(epsg = 32749, inplace = True)
    latitue = request.data['latitude']
    longtitude = request.data ['longitude']
    radius = float (request.data ['radius'])
    geometry = [Point(longtitude, latitue)]
    gdf = gpd.GeoDataFrame(geometry=geometry, crs="EPSG:4326")
    recreate = gdf.to_crs("EPSG:32749")
    jarak = recreate.geometry.sindex.nearest(data.geometry, return_all = True, return_distance = True)[1]
    data['jarak'] = jarak
    filter_data = data[data['jarak']<= radius]
    tempe = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
    data.to_excel(tempe.name, index=False)
    tempe.close()

        # Read the Excel data back for response
    with open(tempe.name, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response["Content-Disposition"] = 'attachment; filename="data.xlsx"'

        # Clean up the temporary file
    os.unlink(tempe.name)

    return response
    




    

