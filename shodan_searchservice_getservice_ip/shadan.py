import shodan
import sys
SHODAN_API_KEY = "DWn1ucKcvhDzRNVk3Lfu4dmDRTSRxKoq"
api = shodan.Shodan(SHODAN_API_KEY)
if len(sys.argv)<2:
 print("Usage:python shodan1.py apache")
 exit()
print("Searching Stirng:%s"%(sys.argv[1]))
file_object = open('ip.txt', 'w')
results = api.search(sys.argv[1])
print('Results found: %s'%results['total'])
for result in results['matches']:
 print("%s:%s|%s|%s"%(result['ip_str'],result['port'],result['location']['country_name'],result['hostnames']))         
 file_object.writelines(result['ip_str']+':')
 file_object.writelines(str(result['port'])+'\n')
file_object.close()
