# LangChain CSV Analytics

## Getting Started

1. Install Sqlite

   ```sh
   brew install sqlite
   ```

1. Create your Sqlite database

   ```sh
   sqlite3
   > .open data.db
   > .import city.csv cities
   ```

1. Setup environment

   ```sh
   cp .env.example .env
   # Add your OPENAPI_KEY to .env
   pip install -r requirements.txt
   ```

1. Run the program

   ```sh
   python main.py
   ```

## Resources

- <https://www.sqlitetutorial.net/sqlite-import-csv/>
- <https://python.langchain.com/en/latest/getting_started/getting_started.html>
- <https://python.langchain.com/en/latest/modules/chains/examples/sqlite.html>
