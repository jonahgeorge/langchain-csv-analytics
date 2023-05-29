import argparse
from langchain import OpenAI
from langchain.agents import create_csv_agent


parser = argparse.ArgumentParser()
parser.add_argument("--csv", help="CSV file")
parser.add_argument("-v", "--verbose", action="store_true", help="Print debug messages")
parser.add_argument(
    "--openapi_key",
    help="""OpenAPI API key\nhttps://platform.openai.com/account/api-keys""",
)
args = parser.parse_args()

llm = OpenAI(openai_api_key=args.openapi_key, verbose=args.verbose)
agent = create_csv_agent(llm, args.csv, verbose=args.verbose)

while True:
    prompt = input("> ")
    print(f"{agent.run(prompt)}\n")
