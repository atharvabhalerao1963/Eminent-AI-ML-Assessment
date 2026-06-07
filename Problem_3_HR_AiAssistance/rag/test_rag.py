from rag.chain import HRPolicyAssistant

assistant = HRPolicyAssistant()

response = assistant.ask(
    "in how many types the employess are classified"
)

print("\nANSWER:")
print(response["answer"])

print("\n" + "=" * 100)
print("SOURCES")
print("=" * 100)

for idx, source in enumerate(response["sources"], start=1):

    print(f"\nSource {idx}")
    print("-" * 100)

    # Convert multiline text to a single horizontal line
    source_text = " ".join(str(source).split())

    print(source_text)