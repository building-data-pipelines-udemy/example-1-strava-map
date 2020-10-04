import pandas as pd
import requests

## acknowledgment: with help from article: 
## https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86

def main():

    config = pd.read_json('config.json') ## strava-example-bucket/ bucket update
    strava_config = config['strava'] 

    client_id = strava_config['client_id']
    client_secret = strava_config['client_secret']
    access_token = strava_config['access_token']
    url_code = strava_config['url_code']


    print('looking for authorization code - make sure to update!')
    authorization_code_config = pd.read_json('authorization_code.json') ## strava-example-bucket/ bucket update
    authorization_code = authorization_code_config['authorization']['authorization_code']

    ## Send post request to Strava API to receive new access_token
    auth_url = 'https://www.strava.com/oauth/token'
    response = requests.post(
                        url = auth_url,
                        data = {
                                'client_id': client_id,
                                'client_secret': client_secret,
                                'code': authorization_code,
                                'grant_type': 'authorization_code'
                                }
                    )
    
    ## Save json response as a variable
    strava_tokens = response.json()

    ## Loop through all activities
    page = 1
    url = 'https://www.strava.com/api/v3/activities'
    access_token = strava_tokens['access_token']
    
    ## Create empty dataframe to loop over 
    activities = pd.DataFrame()

    while True:
        
        ## get page of activities from Strava
        r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
        r = r.json()
        
        ## if no results then exit loop
        if (not r):
            break
        
        ## otherwise add new data to dataframe
        for x in range(len(r)):
            activities.loc[x + (page-1)*200,'id'] = r[x]['id']
            activities.loc[x + (page-1)*200,'name'] = r[x]['name']
            activities.loc[x + (page-1)*200,'start_date_local'] = r[x]['start_date_local']
            activities.loc[x + (page-1)*200,'type'] = r[x]['type']
            activities.loc[x + (page-1)*200,'distance'] = r[x]['distance']
            activities.loc[x + (page-1)*200,'moving_time'] = r[x]['moving_time']
            activities.loc[x + (page-1)*200,'elapsed_time'] = r[x]['elapsed_time']
            activities.loc[x + (page-1)*200,'total_elevation_gain'] = r[x]['total_elevation_gain']
            activities.loc[x + (page-1)*200,'lat'] = str(r[x]['start_latitude'])
            activities.loc[x + (page-1)*200,'lon'] = str(r[x]['start_longitude'])
            activities.loc[x + (page-1)*200,'external_id'] = r[x]['external_id']
            activities.loc[x + (page-1)*200,'average_speed'] = r[x]['average_speed']
            activities.loc[x + (page-1)*200,'max_speed'] = r[x]['max_speed']
            
            
        ## increment page
        page += 1

        print('# of rows in dataset: {}'.format(activities.shape[0]))
        activities.to_csv('mapbox_map/src/data/strava_activities.csv')
        
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error found: {}'.format(e))