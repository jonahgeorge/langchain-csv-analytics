# LangChain CSV Analytics

## Getting Started

1. Setup environment

   ```sh
   pip install -r requirements.txt
   ```

1. Run the program

   ```sh
   python main.py -h
   usage: main.py [-h] [--csv CSV] [-v] [--openapi_key OPENAPI_KEY]

   options:
   -h, --help            show this help message and exit
   --csv CSV             CSV file
   -v, --verbose         Print debug messages
   --openapi_key OPENAPI_KEY
                           OpenAPI API key <https://platform.openai.com/account/api-keys>
   ```

## Examples

   ```sh
   python main.py --csv examples/city.csv --openapi_key "sk-XXX"
   ```

   ```text
   > How many cities start with 'P'
   There are 18 cities that start with 'P'

   > What's the p90 of city population?
   The 90th percentile of city population is 522224.3000000004
   ```

## Resources

- <https://www.sqlitetutorial.net/sqlite-import-csv/>
- <https://python.langchain.com/en/latest/getting_started/getting_started.html>
- <https://python.langchain.com/en/latest/modules/chains/examples/sqlite.html>
