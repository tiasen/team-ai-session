import sys
from tools.image_2_text import generate as image2Text
from chains.generate_story_chain import generate_story
from tools.tts import tts_processor

def main():

    args_count = len(sys.argv)

    if args_count > 1:
        image_url = sys.argv[1]
    else:
        image_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 

    text = image2Text(image_url)
    story = generate_story(text)
    tts_processor(story)

    print("Done!")


if __name__ == "__main__":
    main()