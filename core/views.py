import csv
import io
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CSVUploadForm
from .models import Antenna
from django.http import JsonResponse
import pandas as pd

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file')
                return redirect('upload_csv')
            
            try:
                # Use pandas for robust parsing
                df = pd.read_csv(csv_file)
                
                # Check required columns
                required_cols = ['NomeEntidade', 'NumServico', 'NumEstacao', 'Latitude', 'Longitude', 'Tecnologia', 'FreqTxMHz', 'Municipio.NomeMunicipio']
                missing_cols = [col for col in required_cols if col not in df.columns]
                
                if missing_cols:
                    messages.error(request, f"Missing columns: {', '.join(missing_cols)}")
                    return redirect('upload_csv')

                # Clear existing data
                Antenna.objects.all().delete()

                # Clean and prepare data
                # Replace comma with dot and convert to numeric, coercing errors to NaN
                df['Latitude'] = df['Latitude'].astype(str).str.replace(',', '.', regex=False)
                df['Longitude'] = df['Longitude'].astype(str).str.replace(',', '.', regex=False)
                
                df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
                df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

                # Drop rows with invalid Latitude or Longitude
                df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

                if df.empty:
                    messages.error(request, "No valid data found in the CSV file.")
                    return redirect('upload_csv')

                # Create Antenna objects
                antennas = []
                for _, row in df.iterrows():
                    antennas.append(Antenna(
                        entity_name=row['NomeEntidade'],
                        service_number=str(row['NumServico']),
                        station_id=str(row['NumEstacao']),
                        latitude=row['Latitude'],
                        longitude=row['Longitude'],
                        technology=row['Tecnologia'],
                        frequency=str(row['FreqTxMHz']),
                        city=row['Municipio.NomeMunicipio']
                    ))
                                
                Antenna.objects.bulk_create(antennas)
                messages.success(request, f'Successfully uploaded {len(antennas)} antennas.')
                return redirect('map_view')
                
            except Exception as e:
                messages.error(request, f"Error processing file: {e}")
                return redirect('upload_csv')
    else:
        form = CSVUploadForm()
    
    return render(request, 'core/upload.html', {'form': form})

def map_view(request):
    return render(request, 'core/map.html')

def antenna_data(request):
    antennas = Antenna.objects.all().order_by('latitude', 'longitude')
    sites = {}
    
    for antenna in antennas:
        key = (float(antenna.latitude), float(antenna.longitude))
        if key not in sites:
            sites[key] = {
                'latitude': key[0],
                'longitude': key[1],
                'city': antenna.city,
                'antennas': []
            }
        
        sites[key]['antennas'].append({
            'entity_name': antenna.entity_name,
            'technology': antenna.technology,
            'frequency': antenna.frequency
        })
    
    return JsonResponse(list(sites.values()), safe=False)
