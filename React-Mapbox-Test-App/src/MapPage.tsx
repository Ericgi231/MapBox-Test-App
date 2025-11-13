import { useState, useRef, useEffect } from 'react';
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import './Home.css';

function MapPage() {
  const [zipcode, setZipcode] = useState('');
  const [error, setError] = useState('');
  const mapRef = useRef<mapboxgl.Map | null>(null);
  const mapContainerRef = useRef<HTMLDivElement>(null);
  const markerRef = useRef<mapboxgl.Marker | null>(null);

  const MAPBOX_TOKEN = import.meta.env.VITE_MAPBOX_TOKEN;

  useEffect(() => {
    mapboxgl.accessToken = MAPBOX_TOKEN;
    
    mapRef.current = new mapboxgl.Map({
      container: mapContainerRef.current!,
      center: [-98.5795, 39.8283], // Center of US
      zoom: 4,
      style: 'mapbox://styles/mapbox/streets-v12'
    });

    return () => {
      mapRef.current?.remove();
    };
  }, []);

  const searchZipcode = async () => {
    setError('');
    const response = await fetch(`/api/geocode/${zipcode}`);
    const data = await response.json();
    
    if (data.error) {
      setError(data.error);
    } else {
      // Fly to the location
      mapRef.current?.flyTo({
        center: [data.longitude, data.latitude],
        zoom: 12
      });

      // Remove old marker if exists
      markerRef.current?.remove();

      // Add new marker
      markerRef.current = new mapboxgl.Marker({ color: 'red' })
        .setLngLat([data.longitude, data.latitude])
        .addTo(mapRef.current!);
    }
  };

  return (
    <div className="container">
      <h1>MapBox Geocoding</h1>
      
      <div className="section">
        <h3>Search by Zip Code</h3>
        <input 
          value={zipcode}
          onChange={(e) => setZipcode(e.target.value)}
          placeholder="Enter zip code"
          onKeyPress={(e) => e.key === 'Enter' && searchZipcode()}
        />
        <button onClick={searchZipcode}>Search</button>
        {error && <p style={{color: 'red'}}>{error}</p>}
      </div>

      <div style={{ marginTop: '20px', height: '500px', borderRadius: '8px', overflow: 'hidden' }}>
        <div ref={mapContainerRef} style={{ width: '100%', height: '100%' }} />
      </div>
    </div>
  );
}

export default MapPage;
