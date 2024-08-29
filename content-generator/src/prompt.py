SUBTOPIC_GENERATOR_SYSTEM_PROMT = """
        You will be asked to generate n different subtopics on a given topic. Provide your answers in JSON format.
        Example response (for the topics "Artificial Intelligence"):
        [
            {
                "subtopic": "Generative AI"
            },
            {
                "subtopic": "Neural Networks"
            }
            ...
        ]
        """

TRANSCRIPT_GENERATOR_SYSTEM_PROMPT = """
    Your role is to generate the most informative, the most engaging, and the most interesting short Youtube video transcripts.
    There are two parts: 
    1. Youtube video title 
    2. the introduction that tries to catch the user by providing the most interesting facts about the subject 
    3. the actual transcript explaining the subject as it is
    Introductions MUST BE definetely shorter than the actual transcripts.
    Provide your answers in JSON format.
    Example response:
    {
        "title": "..."
        "introduction": "..."
        "transcript": "Hi, Welcome to my Youtube channel. Today's video is about ..."
    }
"""