from langchain_helper import get_few_shot_db_chain

# Initialize the DB chain
db_chain = get_few_shot_db_chain()

# Sample question to test
test_question = "How many t-shirts are there in total?"

try:
    # Use .invoke with correct input key (typically 'question')
    response = db_chain.invoke({"question": test_question})

    # Print full response
    print("✅ Model Response:")
    print(response["result"])

except Exception as e:
    print("❌ Error while running the model:")
    print(e)
