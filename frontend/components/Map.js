import React, { useEffect, useRef } from 'react';
import { map, tileLayer, Browser } from 'leaflet';

import './Map.css';

const MyMap = ({
  mapIsReadyCallback /* To be triggered when a map object is created */,
}) => {
  const mapContainer = useRef(null);

  useEffect(() => {
    const initialState = {
      lng: 11,
      lat: 49,
      zoom: 4,
    };

    const leafletMap = map(mapContainer.current).setView(
      [initialState.lat, initialState.lng],
      initialState.zoom
    );

    const myAPIKey = 'YOUR_API_KEY';
    const isRetina = Browser.retina;
    let baseUrl = `https://maps.geoapify.com/v1/tile/osm-bright/{z}/{x}/{y}.png?apiKey=${myAPIKey}`;
    let retinaUrl = `https://maps.geoapify.com/v1/tile/osm-bright/{z}/{x}/{y}@2x.png?apiKey=${myAPIKey}`;

    tileLayer(isRetina ? retinaUrl : baseUrl, {
      attribution:
        'Powered by <a href="https://www.geoapify.com/" target="_blank">Geoapify</a> | <a href="https://openmaptiles.org/" rel="nofollow" target="_blank">© OpenMapTiles</a> <a href="https://www.openstreetmap.org/copyright" rel="nofollow" target="_blank">© OpenStreetMap</a> contributors',
      maxZoom: 20,
      id: 'osm-bright',
    }).addTo(leafletMap);

    mapIsReadyCallback(leafletMap);
  }, [mapContainer.current]);

  return <div className="map-container" ref={mapContainer}></div>;
};

export default MyMap;