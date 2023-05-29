import os
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

db = SQLDatabase.from_uri("sqlite:///data.db")
llm = OpenAI(openai_api_key=OPENAI_API_KEY, verbose=True)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
db_chain.run("How many cities are there?")