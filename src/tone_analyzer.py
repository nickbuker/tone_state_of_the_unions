import json
from watson_developer_cloud import ToneAnalyzerV3

# BEGIN of python-dotenv section
from os.path import join, dirname
from dotenv import load_dotenv
import os


def tone_analyzer(text, save_path='', prints=True):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    # END of python-dotenv section

    tone_analyzer = ToneAnalyzerV3(
        username=os.environ.get("TONE_USERNAME"),
        password=os.environ.get("TONE_PASSWORD"),
        version='2016-05-19')

    json_response = tone_analyzer.tone(text=text)
    if save_path != '':
        json.dump(json_response, save_path)
    json_tones = json_response['document_tone']['tone_categories'][0]['tones']
    if prints:
        for tone in json_tones:
            print(tone['tone_name'], tone['score'])
    elif not prints:
        return {tone['tone_name']: tone['score'] for tone in json_tones}
