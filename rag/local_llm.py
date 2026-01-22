from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class LocalLLM:
    def __init__(self):
        model_name = "google/flan-t5-base"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        self.pipeline = pipeline(
            "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_length=256
        )

    def generate(self, prompt: str) -> str:
        result = self.pipeline(prompt)
        return result[0]["generated_text"]
