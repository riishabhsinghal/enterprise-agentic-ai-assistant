import re

def math_agent(query: str) -> str:
    try:
        # Extract numbers and operators
        expression = re.findall(r"[0-9\.\+\-\*\/\(\) ]+", query)
        if not expression:
            return "Sorry, I couldn't calculate that."

        result = eval(expression[0])
        return f"Result: {result}"
    except:
        return "Sorry, I couldn't calculate that."
