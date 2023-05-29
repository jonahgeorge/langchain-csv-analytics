# LangChain CSV Analytics

## Getting Started

1. Setup environment

   ```sh
   pip install -r requirements.txt
   ```

1. Run the program

   ```sh
   python main.py --csv examples/city.csv --openapi_key "sk-XXX"

   # Optionally, run in verbose mode to see the Pandas code
   python main.py --csv examples/city.csv --verbose --openapi_key "sk-XXX"
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
