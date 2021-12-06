"""Working with Elasticsearch"""
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

host, port = 'localhost', 9200
es = Elasticsearch([{'host': host, 'port': port}])
if not es.ping():#check if have connection
    raise SystemExit('error: cannot connect to elastic on {host}:{port}')

# How many food violations in O'Hare?
query = 'zip:60656 OR zip:60666'#O airpoty zipcode
result = es.search(index='food', q=query)#index is food
count = result['hits']['total']['value'] #how many hits dow e have in Ohiro
print(f'total of {count} hits')

# First location
doc = result['hits']['hits'][0]['_source']
print('first location:', doc['name'])


# All results, use scan helper
counts = []
for hit in scan(es, index='food', q=query):
    doc = hit['_source']
    # violations is a | separated
    count = len(doc['violations'].split('|'))
    counts.append(count)

avg = sum(counts) / len(counts)
print(f'avg number of violations: {avg:.2f}')
