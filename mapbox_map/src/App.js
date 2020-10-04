import React, {Component} from 'react';
import MapGL, {Marker} from 'react-map-gl';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import StravaData from './data/strava_activities.json'

import './App.css';

class App extends Component {
  
  state = {
    viewport: {
      latitude: 35,
      longitude: -80,
      zoom: 3,
      bearing: 0,
      pitch: 0,
      minZoom:1.5
    },
  };

componentDidMount() {
  this.setState({
    data: StravaData
  })
}

mapRef = React.createRef();

handleViewportChange = viewport => {
  this.setState({
    viewport: { ...this.state.viewport, ...viewport }
  });
};

  render() { 

    const {viewport, data} = this.state;

    return ( 
      <div style={{height:"100vh"}}> 
        <MapGL
          {...viewport}
          width="100%"
          height="100%"
          ref = {this.mapRef}
          mapStyle={process.env.REACT_APP_MAP_STYLE}
          onViewportChange={this.handleViewportChange}
          mapboxApiAccessToken= {process.env.REACT_APP_MAPBOX_TOKEN}
        >
          {data && data.features.map(location =>
            <Marker
            key = {location.properties.name + location.properties.elapsed_time}
            latitude={location.geometry.coordinates[1]}
            longitude={location.geometry.coordinates[0]}
            captureDrag={false}
            captureDoubleClick={false}
            >
              <div className="marker">
                <span>{location.properties.type}: {(Math.round((location.properties.distance)/1000 * 100) / 100).toFixed(2)} km ({location.properties.total_elevation_gain} ft. Elevation Gain )</span>
              </div>
            </Marker>
          )}

        </MapGL>
      </div>
     );
  }
}
 
export default App;