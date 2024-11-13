import os
from dotenv import load_dotenv
from openai import OpenAI
INPUT_FILE_NAME = 'tresc_artykulu.txt'
OUTPUT_FILE_NAME = 'something.html'


class Solution:
    def __init__(self, input_file: str, output_file: str, prompt: str) -> None:
        self.prompt: str = prompt
        self.file_content: str = ''
        self.input_file: str = input_file
        self.output_file: str = output_file
        self.client: OpenAI = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    def generate_article(self) -> None:
        completion = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    "role": "system",
                    "content": "You're a web developer assistant who can create a website based on a context provided by a user."
                },
                {
                    "role": "user",
                    "content": "Based on a text file's content that I provide, generate an HTML site following these rules: 1. Use appropriate tags to structure the site (e.g., <h1> for the main title, <h2> for headings, <p> for paragraphs, etc.). 2. Group text into <section> tags for better organization. 3. Include placeholders for images at suitable points using <img src='image_placeholder.jpg' alt=''/>. In the alt attribute, provide a description for the image. 4. After the main article content, generate a dictionary that stores the image placeholder names and descriptions that can be used to generate suitable images via DALL-E. 5. Read any UTF-8 characters correctly from the file. 6. Do not translate the article from Polish. Additional restrictions: - Do not include CSS or JavaScript. - Provide code that is ready to be placed inside the <body> tags without including the tags themselves. The content from the text file is as follows: {self.file_content}"
                }]
        )
        print(completion)

    def read_from_file(self, file_name: str) -> None:
        if file_name == '':
            raise ValueError('Invalid File Name')

        with open(file_name, 'r', encoding='utf-8') as file:
            self.file_content = file.read()
            file.close()

    def write_to_file(self, file_content: str, file_name: str) -> None:
        if file_name == '':
            raise ValueError('Invalid File Name')

        with open(file_name, 'wt') as file:
            file.write(file_content)
            file.close()


if __name__ == '__main__':
    load_dotenv()
    s = Solution(INPUT_FILE_NAME, OUTPUT_FILE_NAME, '')
    s.generate_article()
