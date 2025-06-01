from ai import call_gpt

def main():
    # TODO: your code here
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    # Create a prompt for the AI
    ai_prompt = f"Write a haiku about {topic}. Follow the 5-7-5 syllable format."

    # Generate the haiku using AI
    haiku = call_gpt(ai_prompt)

    # Display the output
    print(f"{name}, here is your haiku:\n{haiku}")



if __name__ == "__main__":
    main()