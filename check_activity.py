## FILE - The access log file for the nginx web server
FILE = '/var/log/nginx/access.log'

## A list to store all the entries in FILE
emails = []

## Open the file and store all the lines in a list
with open(FILE) as f:
    content = f.readlines()
contents = [x.strip() for x in content] 

## Iterate over the list and parse each line to get suitable information
for content in contents:
    email = {}
    email['ip'] = content.split(',')[0]
    email['time'] = content.split(',')[1]
    email['req'] = content.split(',')[2]
    email['ref'] = content.split(',')[3]
    email['agent'] = content.split(',')[4]
    emails.append(email)

## Print the Info
for email in emails:
    print("\nAn Email was opened at {0} by {1} having IP Address {2}. User Info is as follows:\nHTTP Referrer: {3}\nUser Agent: {4}\n".format(email['time'], email['req'], email['ip'], email['ref'], email['agent']))
