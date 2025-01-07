import requests
import os
import base64
from PIL import Image
import io

def generate_images(prompts_json, output_dir, api_key, api_url, number):
    """
    Generate images based on a JSON input of prompts.

    Args:
        prompts_json (dict): A dictionary containing an "images" key with a list of prompts.
        output_dir (str): Directory to save the generated images.
        api_key (str): API key for the DeepInfra service.
        api_url (str): API URL for the DeepInfra service.
    Returns:
        list: Paths to the generated image files.
    """
    # Define the headers for the API request
    headers = {"Authorization": f"Bearer {api_key}"}

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Extract the list of prompts from the JSON
    prompts = prompts_json.get("images", [])
    if not prompts:
        raise ValueError("The input JSON does not contain valid 'images' prompts.")

    images = []
    for i, prompt in enumerate(prompts):
        # Prepare the data payload for the API request
        image_data = {
            "prompt": prompt.lower(),
            "width": 1080,
            "height": 1080,
            "num_images": 1,
            "num_inference_steps": 35,
        }

        print(f"Generating image {i + 1}/{len(prompts)} for prompt: {prompt}")

        # Send the request to the DeepInfra API
        response = requests.post(api_url, headers=headers, json=image_data)
        if response.status_code == 200:
            image_result = response.json()
            if "images" in image_result and image_result["images"]:
                try:
                    # Decode the base64 image data
                    image_base64 = image_result["images"][0].split(",")[1]  # Remove "data:image/png;base64,"
                    image_bytes = base64.b64decode(image_base64)

                    # Convert to an image using Pillow
                    image = Image.open(io.BytesIO(image_bytes))

                    # Save the image file in a standard format
                    file_name = f"image_{(len(prompts) - i):02d}.png"
                    file_path = os.path.join(output_dir, file_name)
                    image.save(file_path, format="PNG", optimize=True)
                    images.append(file_path)
                    print(f"Image saved to {file_path}")
                except Exception as e:
                    print(f"Error processing image for prompt '{prompt}': {e}")
            else:
                print(f"Failed to generate image for prompt: {prompt}")
        else:
            print(f"API request failed with status code {response.status_code} and message: {response.text}")

    return images