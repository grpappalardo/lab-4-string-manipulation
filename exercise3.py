'''
In this exercise I used RegEx to find parts of the URL that are numerical, @, ., or -. Then I indexed to take off the
@, split at the comma, and printed the latitude/longitude with concatenation.

'''

import re
url = 'https://www.google.com/maps/@42.2509428,-71.8249939,17z'
# x = re.findall('@[0-9\.-]+,[0-9\.-]+', url)
x = re.findall('@[0-9\.-]+,[0-9\.-]+', url)

x_str = ''.join(x)

xstr = x[0]
print(xstr)

xstr = xstr[1:len(xstr)]
print(xstr)
xsplit = xstr.split(',')
print(xsplit)

print('Latitude: ' + xsplit[0] + '\n' + 'Longitude: ' + xsplit[1])

latlong_output('https://www.google.com/maps/@42.2509428,-71.8249939,17z')
