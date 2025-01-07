import os
from moviepy.audio.io.AudioFileClip import AudioFileClip
from text_to_speech import text_to_audio
from script_to_prompts import split_script
from generate_images import generate_images
from config import DEEPINFRA_API_KEY, DEEPINFRA_API_URL
import os

def get_audio_duration(audio_path):
    """
    Get the duration of an audio file in seconds using MoviePy.

    Args:
        audio_path (str): Path to the audio file.

    Returns:
        float: Duration of the audio file in seconds.
    """
    with AudioFileClip(audio_path) as audio_clip:
        return audio_clip.duration

def process_script(script, output_dir):
    # Create subdirectories for this script's output
    audio_dir = os.path.join(output_dir, "audio")
    images_dir = os.path.join(output_dir, "images")
    video_file = os.path.join(output_dir, "final_video.mp4")
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)

    # Step 1: Convert SCRIPT to AUDIO (DONE)
    audio_file = text_to_audio(script, os.path.join(audio_dir, "script_audio.mp3"))

    duration = get_audio_duration(audio_file)

    # Set the number of images based on audio duration (2 seconds per image)
    number_images = int(duration / 2) + 1
    print(number_images)

    # number_images = 25

    # Step 2: Convert SCRIPT to Prompts (DONE)
    prompts = split_script(script, number=number_images)

    # Step 3: Generate Images for Prompts (DONE)
    image_files = generate_images(prompts, images_dir, api_key=DEEPINFRA_API_KEY,api_url=DEEPINFRA_API_URL, number=number_images)

def main():
    # List of scripts to process
    scripts = [
        "Girl, let me tell you—don’t sleep on these. I wasn’t even planning to buy them, but I saw them on TikTok Shop, and I figured, why not? I just needed a little boost of energy. Little did I know they would *completely* change my life. Now, I’m like a whole new person. My patience? Unlimited. That energy I was craving? Times ten. No more mood swings, no more sugar cravings—gone. And just like that girl in the reviews said, I’m sleeping like a baby every single night. Sis, trust me. Run, don’t walk, to TikTok Shop and grab these while they’re still on sale. Your life will literally do a 180. Thank me later!"
        ,"Here’s what I’ve learned after one week of consistently taking sea moss: Take it on an empty stomach. First thing in the morning is the best time to get the most benefits from sea moss. Trust me, it makes a difference. Get creative with it. You don’t have to take it by the spoonful every day. Add it to a smoothie, use it in soup, or even as a face mask. Honestly, you can incorporate sea moss into almost anything. Make sure it’s authentic. Not all sea moss is created equal, so be mindful of where you’re buying it from. I’ve been using sea moss from the Purfect Fuel. It’s legit, authentic, and works perfectly. If you’re looking for a trusted and reliable sea moss brand, definitely check them out!"
        ,"Alright, guys, I finally tried sea moss for the first time, and let me tell you why I’m loving it. Sea moss is amazing for your health—especially for women. If you have PCOS, this could be a game-changer! Sea moss is also packed with nutrients—96 essential vitamins and minerals your body needs. I got mine from this Purfect Fuel company (I’ll link them here). It’s pure, with no added flavor, and honestly, the packaging was super cute! It even came with a cooling pack. Now, full disclosure: I struggled hard getting the plastic off the top—me and that lid had a whole battle. But once I got it open, the smell wasn’t bad at all—just pure sea moss. When I took my first taste, I won’t lie—it’s not the best thing flavor-wise. But we’re not here for the taste; we’re here for the benefits, and those are undeniable. So if you’re ready to improve your health, grab a jar today. It’s not about flavor—it’s about feeling your best!"
    ]

    # "After I had my baby, my hair was falling out in clumps—it was honestly terrifying. I tried everything—oils, masks, even scalp massages—but nothing seemed to help. Then a friend recommended these Purfect Fuel collagen vitamins, and I thought, why not? Within a month, I started noticing baby hairs growing back, and my hair felt thicker and stronger. But it wasn’t just that—I actually had more energy during the day, which, as a mom, is a game changer. If you’re struggling with hair loss or just feeling drained, you need to give this a try. I’ve linked it right here—don’t wait. Your hair and your energy will thank you!"
    
    # Root output directory
    output_root = "output/"
    os.makedirs(output_root, exist_ok=True)

    # Process each script and generate videos
    for idx, script in enumerate(scripts, start=1):
        script_output_dir = os.path.join(output_root, f"script_{idx}")
        process_script(script, script_output_dir)

if __name__ == "__main__":
    main()
