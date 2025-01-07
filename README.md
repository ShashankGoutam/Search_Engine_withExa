
# Search Engine using EXA API

This project demonstrates a streamlined search engine leveraging the EXA API to provide targeted results with fewer clicks. The goal is to simplify the process of finding specific information by presenting concise, high-quality search results.

## Features
- **Efficient Search**: Retrieves up to 5 relevant results based on the user's query.
- **Keyword-based Search**: Optimized for precision using a keyword-centric approach.
- **Autoprompt Support**: Enhances queries automatically for better results.
- **Key Information Display**: Displays titles, URLs, and publication dates of the results.

## How It Works
1. **Input Query**: The user inputs a search query via the console.
2. **Query Processing**: The query is sent to the EXA API for processing with the following parameters:
   - `num_results`: Limits the results to a maximum of 5.
   - `type`: Utilizes a keyword-focused search.
   - `use_autoprompt`: Enables auto-suggestion for refining the query.
3. **Result Display**: The search results are displayed with the title, URL, and publication date.

## Code Overview
The main script integrates with the EXA API and is simple to use. Key components include:
- **Initialization**: Connect to the EXA API using an API key.
- **Query Execution**: Perform the search with specified parameters.
- **Result Formatting**: Parse and display the results in a readable format.

### Code Example
```python
from exa_py import Exa

exa = Exa('your-api-key-here')

query = input('Search : ')

response = exa.search(query, 
                      num_results=5, type='keyword', use_autoprompt=True) 

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print(f'Published Date: {result.published_date}')
  print()
```

## Requirements
- Python 3.7 or higher
- EXA API Key
- `exa_py` library installed (`pip install exa_py`)

## Installation
1. Clone the repository or download the script.
2. Install the required library:
   ```bash
   pip install exa_py
   ```
3. Replace `'your-api-key-here'` with your EXA API key in the script.
4. Run the script:
   ```bash
   python main.py
   ```

## Usage
1. Run the script in a terminal or command prompt.
2. Enter a search query when prompted.
3. View the top results directly in the terminal.

## Benefits
- Reduces clicks and time spent navigating search results.
- Simplifies information retrieval with targeted, high-quality outputs.

## Future Improvements
- Add a graphical user interface (GUI) for enhanced usability.
- Enable integration with other APIs for more diverse search options.
- Support for additional languages and search result types.
