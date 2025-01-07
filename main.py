from exa_py import Exa

exa = Exa('b53ea196-4b39-45e5-9b06-c5b53ad2b73f')

query =  input('Search : ')

response = exa.search(query, 
                      num_results = 5 , type= 'keyword', use_autoprompt= True) 

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print(f'Published Date : {result.published_date}')
  print()

