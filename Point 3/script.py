import google.generativeai as genai
import os

API_KEY = "AIzaSyC5L93vD_yXeVTKg__v1YbhnXALYA3LgAw"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def send_prompt(prompt_type, prompt_text, filename):
    print(f"Sending {prompt_type} prompt:")
    print(prompt_text)

    response = model.generate_content(prompt_text)
    print(f"\nResponse:\n{response.text}")

    # Create a directory if it doesn't exist
    results_folder = "results"
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # Construct the full path for the file
    full_path = os.path.join(results_folder, filename)

    # Save the results
    with open(full_path, "w") as f:
        f.write(f"{prompt_type} Prompt:\n{prompt_text}\n\nResponse:\n{response.text}")

few_shot_prompt = """
In the following examples, identify the emotion:

* She slammed the door and stormed out. (Angry)
* He jumped for joy. (Happy)

What emotion is expressed in the following sentence:
The news left him feeling numb.
"""

send_prompt("Few-shot", few_shot_prompt, "few_shot_prompt.txt")

cot_prompt = """
**Step 1: Understand the situation**

A chef is trying to decide on a dessert for a special occasion. They have the following ingredients: chocolate, strawberries, and cream.

**Step 2: Consider options**

List two possible desserts the chef could make with these ingredients.

**Step 3: Decide on the best option**

Explain why one dessert might be a better choice than the other.
"""

send_prompt("CoT", cot_prompt, "cot_prompt.txt")

prompt_chain = """
**Prompt 1:** Write a short poem about a cat.

**Prompt 2:** Based on the poem, write a story about the cat's adventures.
"""

send_prompt("Prompt Chain", prompt_chain, "prompt_chain.txt")

mystery_prompt = """
Write a limerick that includes a programmer, a bug, and a sigh of relief.
"""

send_prompt("Mystery", mystery_prompt, "mystery_prompt.txt")

print("\nAll prompts sent and results saved in the 'results' folder!")