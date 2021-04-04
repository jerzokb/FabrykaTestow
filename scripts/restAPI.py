import requests

r = requests.get('https://fabrykatestow.pl')

print(r)

post = requests.post('http://httpbin.org/post')
put = requests.put('http://httpbin.org/put')
delete = requests.delete('http://httpbin.org/delete')

print(post)
print(put)
print(delete)

parameters = {'key1':'value1', 'key2':'value2'}

r1 = requests.get('https://fabrykatestow.pl', params=parameters)
print(r1.url)
print(r.text)
print(r.encoding)