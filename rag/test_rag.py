from rag.qa_chain import answer_question

query = "What is the leave policy?"
response = answer_question(query)

print("Answer:", response)
