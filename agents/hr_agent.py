from rag.qa_chain import answer_question

def hr_agent(query: str) -> str:
    return answer_question(query)
