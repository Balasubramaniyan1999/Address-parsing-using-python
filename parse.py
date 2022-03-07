import re
import pgeocode

import pandas as pd

address = input("Enter the Full address:")
result = re.findall(r'\b\d{6}',address)

Countryname = pgeocode.Nominatim('IN')
extracted = Countryname.query_postal_code(result)

data=pd.DataFrame(extracted,columns=['place_name','state_name','country_code','postal_code'])
print(data)






