from agents.hr_agent import hr_agent
from agents.math_agent import math_agent

def route_query(query: str) -> str:
    query_lower = query.lower()

    if any(word in query_lower for word in ["leave", "policy", "hr"]):
        return hr_agent(query)

    if any(word in query_lower for word in ["calculate", "+", "-", "*", "/"]):
        return math_agent(query)

    return "I'm not sure which department handles this query."
