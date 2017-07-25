import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

visual_recognition = VisualRecognition('2016-05-20',
    api_key='561af6fbe99635bb0a7b15f0865de0f4b3f847fe')

print(json.dumps(visual_recognition.delete_classifier(classifier_id='allowedvsnot_1280760193'), indent=2))
