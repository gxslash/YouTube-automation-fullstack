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

class SubtopicGenerator(TextGenerator):

    def __init__(self, api_key: str, topic: str):
        super().__init__(api_key)
        self._topic = topic

    @property
    def topic(self):
        return self._topic

    def _create_topic_question(topic, subtopic_count=SUBTOPIC_COUNT):
        return f"List me {subtopic_count} subtopics and video titles about {topic}"
    
     
    def generate_subtopics(self):
        topic_question = self._create_topic_question(self.topic)
        subtopics = self._gpt.answer_question(topic_question, prompt.SUBTOPIC_GENERATOR_SYSTEM_PROMT)
        return subtopics
    
def save_content_locally(content):
    with open('./content.json', 'w') as f:
        content = json.dumps(content, indent=4)
        f.write(content)


def runner(topic):
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    generator = SubtopicGenerator(openai_api_key, topic)
    content = generator.generate_subtopics()
    return content
    

if __name__ == '__main__':
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    topic = "cryptocurrency"
    generator = SubtopicGenerator(openai_api_key, topic)
    content = generator.generate_subtopics()
    save_content_locally(content)