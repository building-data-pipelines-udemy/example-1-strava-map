# Example 1: Strava Map

This app creates and updates a visualization of all Stefan's Strava uploads. Using the Strava API[url] and Mapbox, we can download Strava data and visualizes it on a beautiful, customized map. The Strava API extraction is run in a GCP VM, scheduled to run every Sunday at 7:00pm EST, and the React app itself is hosted on Google Cloud's App Engine. 

In order to utilize this app yourself, you can use the dummy account's credentials, provided in the config.json file in the repository, or create your own Strava account and add your configurations. 

For the Mapbox map, you will need to create a Mapbox account and provide your own API key, which can be done here: After retrieving your API key, add it to .env.local file in the format:

REACT_APP_MAPBOX_TOKEN='[YOUR KEY HERE]'

Restarting the app and refreshing it a few times will allow the app to successfully connect to the Mapbox API and display the Mapbox map. If you'd like to change the map style, head on over to Mapbox Studio, create a new style, and add the style to the .env.local file, where my public style is currently showing. 

MAP_STYLE='[YOUR STYLE HERE']



