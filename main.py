from langchain.agents import create_agent
from pprint import pprint

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    print(f"🌤️ TOOL CALLED! City: {city}")
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="ollama:llama3.2",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in Denver?"}]}
)
pprint(result, indent=2, width=100)