import os
import openai
import argparse

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    print('running')
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    userinput = args.input

    # print(f"Input is {userinput}")
    result = generate_branding_snippet(userinput)
    print(result)
    pass


def generate_branding_snippet(prompt: str) -> str:

    enriched_prompt = f"generate upbeat branding snippet for {prompt}"

    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003", prompt=enriched_prompt, temperature=0, max_tokens=32)

    # Extract ouptput text
    branding_text: str = response["choices"][0]["text"]
    branding_text = branding_text.strip()
    last_char = branding_text[-2]

    if last_char not in {'.', '!', "?"}:
        branding_text += "..."

    return branding_text


if __name__ == "__main__":
    main()
