from phi.agent import Agent
from phi.model.google import Gemini
from phi.agent import Agent 
from phi.tools.yfinance import YFinanceTools 
from phi.tools.duckduckgo import DuckDuckGo 
from dotenv import load_dotenv
import os
import phi.api
from phi.playground import Playground , serve_playground_app
# loading the environment veriable from .env
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")
print(os.getenv("GROQ_API_KEY"))


## Live_web_search
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    agent_id="web-agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGo()],
    instruction=['Always include the source'],
    show_tool_calls=True,
    markdown = True
)

## Financial Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    agent_id="finance-agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instruction = ['use table to display the data'],
    show_tool_calls=True,
    markdown = True,
)

app = Playground(agents=[web_agent, finance_agent]).get_app(use_async=False)

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)