# LangChain CSV Analytics

## Getting Started

1. Setup environment

   ```sh
   cp .env.example .env
   # Add your OPENAPI_KEY to .env
   pip install -r requirements.txt
   ```

1. Run the program

   ```sh
   $ python main.py city.csv
   What would you like to know?
   What's the p90 of city population?
   
   
   > Entering new AgentExecutor chain...
   Thought: I need to calculate the p90 of the population column
   Action: python_repl_ast
   Action Input: df['population'].quantile(0.9)
   Observation: 522224.3000000004
   Thought: I now know the final answer
   Final Answer: 522224
   ```

## Resources

- <https://www.sqlitetutorial.net/sqlite-import-csv/>
- <https://python.langchain.com/en/latest/getting_started/getting_started.html>
- <https://python.langchain.com/en/latest/modules/chains/examples/sqlite.html>
