from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/company_faq.txt")
documents = loader.load()

print(documents)
