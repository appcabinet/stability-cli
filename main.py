import requests
import subprocess
import sys
import argparse
import os
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()

def open_image(filename):
    subprocess.call(["open", filename])

def main():
    API_KEY = os.getenv('STABILITY_API_KEY')

    parser = argparse.ArgumentParser(description="Trigger the API to generate an image")
    parser.add_argument("--ratio", type=str, help="The aspect ratio of the image")
    parser.add_argument("--seed", type=str, help="The seed for the image. Can be between 0 (random) -> 4294967294")
    parser.add_argument("prompt", type=str, help="The prompt for the image")

    args = parser.parse_args()

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
        headers={
            "authorization": API_KEY,
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": args.prompt,
            "ratio": args.ratio or "1:1",
            "output_format": "png",
        },
    )

    if response.status_code == 200:
        download_dir = os.path.expanduser("~/Downloads")
        filename = os.path.join(download_dir, f"{uuid4()}.png")
        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"Image generated successfully: {filename}")
        open_image(filename)
    else:
        raise Exception(str(response.json()))

if __name__ == "__main__":
    main()
