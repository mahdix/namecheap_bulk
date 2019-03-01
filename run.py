#!/usr/bin/env python

from namecheap import Api
from namecheap import ApiError
from xml.etree import ElementTree
import sys
import re

username = 'my_namecheap_user'
api_key='none_of_your_business'
ip_address='whitelisted_ip'

api = Api(username, api_key, username, ip_address, debug = False, sandbox = True)

domain = sys.argv[1]

result = ''
try:
    result = api.domains_create(
        DomainName = domain,
        FirstName = 'FirstName',
        LastName = 'LastName',
        Address1 = 'address',
        City = 'London',
        StateProvince = 'London',
        PostalCode = 'postal_code',
        Country = 'GB',
        Phone = 'number',
        EmailAddress = 'email@abc.com',
        WhoisGuard=True
    )
except ApiError as err:
    print "Error: " + err.text
    exit(1)


status=result.get("Status")
print status
if status=="OK":
    exit(0)
else:
    exit(1)
