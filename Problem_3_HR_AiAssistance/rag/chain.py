from rag.retriever import HRRetriever
from rag.generator import HRGenerator
from rag.prompts import HR_PROMPT


class HRPolicyAssistant:

    def __init__(self):

        self.retriever = HRRetriever()
        self.generator = HRGenerator()

    def ask(self, question: str):

        results = self.retriever.retrieve(question)

        docs = [doc for doc, score in results]

        context = "\n\n".join(
            doc.page_content
            for doc , score in results
        )

        prompt = HR_PROMPT.format(
            context=context,
            question=question
        )
        print("\n")
        print("=" * 100)
        print("RETRIEVED CONTEXT")
        print("=" * 100)
        print(context)
        print("=" * 100)
        answer = self.generator.generate(prompt)

        return {
            "question": question,
            "answer": answer,
            "sources": [
                doc.page_content[:150]
                for doc in docs
            ]
        }