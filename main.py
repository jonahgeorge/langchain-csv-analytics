import os
import argparse
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.agents import create_csv_agent

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=OPENAI_API_KEY, verbose=True)

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

agent = create_csv_agent(llm, args.filename, verbose=True)

while True:
	prompt = input("What would you like to know?\n")
	agent.run(prompt)

