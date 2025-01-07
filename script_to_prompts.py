import requests
import re
import json
from config import PROMPT_API_URL

def split_script(script, number):
  API_KEY = PROMPT_API_URL
  url = "https://api.deepinfra.com/v1/openai/chat/completions"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  data = {
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "messages": [
        {
            "role": "user",
            "content": """
                I'm having a presentation about a sample product.
                Well, I'm going to make a video from images and script (I will use Eleven Labs to generate the script to audio). 
                I'm having its script right now. I want you to read the script carefully to know its meaning, I mean the whole script's sentences meaning. 
                I really want you to give me """ + f"{number}" + """ image descriptions, just descriptions, so that I can use those descriptions to generate images with AI tools such as DALL-E or deepinfra. 
                I will not be on the video so the main things on the video were just images and script (I mean the voice that I generated using the script). Yeah, so please give me a series of image descriptions so that it can help me present the script and make my presentation more lively and attractive. Can you help me with that?

            """ + script + """

                The passage above is the script of my video. Please generate images description for me. I also want the images to relevant to showing a medicine that is good for human health so I want the person in the image descriptions (if the image description has a person) to look healthy and strong (it should be a man with strong muscles or a woman with a healthy life style).

                For example, the image descriptions could be write like this (this is for another script):
                - A strong, muscular man holding a bunch of sea moss, with a friendly smile, standing in front of a beautiful ocean background.
                - A close-up of a person's hand holding a handful of sea moss, with a few leaves of the plant on their head, symbolizing its healing properties.
                - A medical professional (male) in a white coat, giving a thumbs-up to the viewer, with a tablet or computer screen showing the composition of 92 vital minerals in the background.
                - A bottle of sea moss powder with a label on it, surrounded by images of the different health benefits it provides (e.g. energy, immunity, blood pressure).
                - A beautiful illustration of a human body with a healthy, glowing complexion, surrounded by waves and sea life, representing the connection to the sea.
                - A fit, muscular man applying black seed oil to his hair, with a comb in hand, and a charming smile.
                - A dermatologist (male) examining a person's clear, healthy skin, with a bottle of black seed oil on the table.
                - A person rubbing black seed oil into their scalp, with a few strands of healthy, thick hair escaping from the treatment.
                - A comparison image: a before-and-after shot of someone with dull, thinning hair, versus a person with thick, luscious locks after using black seed oil.
                - A beautiful illustration of a hair follicle, with a droplet of black seed oil nourishing it, surrounded by vibrant, healthy hair.

                I think those examples will give you enough information to give me the best image descriptions.

                Please give me the answer base on this json structure:
                {
                    "images": [
                        "",
                        "",
                        "",
                        "",
                        ""
                    ]
                }

                Please just give me the JSON file, you don't need to give me anything else.
            """
        }
    ],
    "max_tokens": 15000,
    "temperature": 0.7
  }

  response = requests.post(url, headers=headers, data=json.dumps(data))

  # Process response to extract JSON data
  if response.status_code == 200:
      result = response.json()
      content = result['choices'][0]['message']['content']
      code_block = re.search(r'```(.*?)```', content, re.DOTALL)
      print(content)
      print(code_block)
      if code_block:
        return json.loads(code_block.group(1).strip())
      else:
        return json.loads(content)

  else:
      print(f"Error: {response.status_code}")
      print(response.json())