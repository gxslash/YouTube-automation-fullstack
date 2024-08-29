import os
import json
import prompt
from dotenv import load_dotenv
from gpt.builder import GPTClient

LANGUAGES = ['English', 'Turkish', 'Spanish']

PLAYLIST_LENGTH = 100
SUBTOPIC_COUNT = 50

SUBTOPIC_FIELD = 'subtopic'
TRANSCRIPT_FIELD = 'transcript'
INTRODUCTION_FIELD = 'introduction'
TITLE_FIELD = 'title'

class TextGenerator:

    def __init__(self, api_key: str):
        self._gpt = GPTClient(api_key)

class ContentGenerator(TextGenerator):

    def __init__(self, api_key: str):
        super().__init__(api_key)
        
    def _create_transcript(subtopic, language, length=PLAYLIST_LENGTH):
        return f"Generate me a youtube video transcript about {subtopic} in {language} language with {length} words at most."
   
    def generate_content(self, lang, subtopic):
        content_question = self._create_transcript(subtopic, language=lang)
        content = self._gpt.answer_question(content_question, prompt.TRANSCRIPT_GENERATOR_SYSTEM_PROMPT)
        title = content[TITLE_FIELD]
        transcript = content[TRANSCRIPT_FIELD]
        intro = content[INTRODUCTION_FIELD]
        return title, intro, transcript


def save_content_locally(content):
    with open('./content.json', 'w') as f:
        content = json.dumps(content, indent=4)
        f.write(content)


def runner(subtopic, language: str = 'English'):
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    generator = ContentGenerator(openai_api_key)
    content = generator.generate_content(language, subtopic)
    return content
    

if __name__ == '__main__':
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    subtopic = "Bitcoin"
    language = 'English'
    generator = ContentGenerator(openai_api_key)
    content = generator.generate_content(language, subtopic)
    save_content_locally(content)