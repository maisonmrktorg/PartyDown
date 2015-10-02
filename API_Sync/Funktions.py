#Simple comparative reports: Bounce 


from HelloAnalytics import *
	  
def get_results(service, profile_id):
  # Use the Analytics Service Object to query the Core Reporting API

  this_month = service.data().ga().get(ids='ga:' + profile_id, start_date='30daysAgo', 
  			   end_date='today', metrics='ga:bouncerate').execute()
  
  return this_month

  this_day =  service.data().ga().get(ids='ga:' + profile_id, start_date='today', 
  			  end_date='today', metrics='ga:bouncerate').execute()
  			  
  return this_day
  
def print_results(results):  
  if 'this_day' > 'this_month':
    print 'Congrats %s! Your bounce rate is below avg today' % results.get('profileInfo').get('profileName')
    print 'Today the Bounce Rate is %s' % results.get('rows')[0][0]
  
  else:
    print 'a little bit higher today, not what you want'
    print 'Total Bounce Rate: %s' % results.get('rows')[0][0]

def main():
  # Define the auth scopes to request.
  scope = ['https://www.googleapis.com/auth/analytics.readonly']

  # Authenticate and construct service.
  service = get_service('analytics', 'v3', scope, 'client_secrets.json')
  profile = get_first_profile_id(service)
  print_results(get_results(service, profile))

if __name__ == '__main__':
  main()
