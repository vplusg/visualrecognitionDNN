import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

visual_recognition = VisualRecognition('2016-05-20',
    api_key='561af6fbe99635bb0a7b15f0865de0f4b3f847fe')

with open(join(dirname(__file__), './milkbottlewithmilkimages.zip'), 'rb') as milkbottles, open(join(dirname(__file__),'./babyformula.zip'), 'rb') as babyformula, open(join(dirname(__file__),'./alchohol.zip'), 'rb') as alchohol:
	print(json.dumps(visual_recognition.create_classifier('allowedvsnot', milkbottles_positive_examples=milkbottles, babyformula_positive_examples=babyformula, negative_examples=alchohol), indent=2))
