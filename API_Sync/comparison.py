#Class comparison

from HelloAnalytics import *

class Compare(object):

	def get_results(self, service, profile_id):
  	# Use the Analytics Service Object to query the Core Reporting API
		this_month = self.this_month
		this_day = self.this_day
		
  		self.this_month = service.data().ga().get(ids='ga:' + profile_id, start_date='30daysAgo', 
  	    		 	 	  end_date='today', metrics='ga:bouncerate').execute()
  
  		return self.this_month

  		self.this_day =  service.data().ga().get(ids='ga:' + profile_id, start_date='today', 
  			    		 end_date='today', metrics='ga:bouncerate').execute()
  			  
  		return self.this_day
  
	def print_results(self, results):  
  		if self.this_day < self.this_month:
    			print 'View (Profile): %s' % results.get('profileInfo').get('profileName')
    			print 'Total BounceRate: %s' % (self.this_day)
  
		else:
    			print 'a little bit higher today, not what you want'
    			print 'Total BounceRate: %s' % results.get('rows')[0][0]


	def main():
  		# Define the auth scopes to request.
  		scope = ['https://www.googleapis.com/auth/analytics.readonly']

  		# Authenticate and construct service.
  		service = get_service('analytics', 'v3', scope, 'client_secrets.json')
  		profile = get_first_profile_id(service)
  		print_results(get_results(service, profile))

	if __name__ == '__main__':
  		main()
