# Add Azure OpenAI package
from openai import AzureOpenAI


# Initialize the Azure OpenAI client
client = AzureOpenAI(
        azure_endpoint = azure_oai_endpoint, 
        api_key=azure_oai_key,  
        api_version="2023-05-15"
        )

# Send request to Azure OpenAI model
response = client.chat.completions.create(
   model=azure_oai_model,
   temperature=0.7,
   max_tokens=120,
   messages=[
       {"role": "system", "content": "You are a helpful assistant."},
       {"role": "user", "content": "Summarize the following text in 20 words or less:\n" + text}
   ]
)

print("Summary: " + response.choices[0].message.content + "\n")
