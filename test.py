import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

visual_recognition = VisualRecognition('2016-05-20',
    api_key='561af6fbe99635bb0a7b15f0865de0f4b3f847fe')

print("----ALCHOHOL-TEST--")
print(json.dumps(visual_recognition.classify(images_url="https://res.cloudinary.com/saucey/image/upload/v1490394315/tgrfmmbxhu9l7nxohi0p.jpg", classifier_ids=["allowedvsnot_1765920808", "default"]),indent=2))
print("----ALCHOHOL-TEST--")
print(json.dumps(visual_recognition.classify(images_url="http://www.spiritsandwine.lv/img/items/28/2807.png", classifier_ids=["allowedvsnot_1765920808", "default"]),indent=2))
print("---MILKBOTTLE-TEST---")
print(json.dumps(visual_recognition.classify(images_url="https://thumbs.dreamstime.com/z/baby-milk-bottle-vector-eps-41789045.jpg", classifier_ids=["allowedvsnot_1765920808"]),indent=2))
print("---BABYFORMULA-TEST--")
print(json.dumps(visual_recognition.classify(images_url="http://assets.reviews.com/uploads/2016/08/11130419/Product-Card-Enfamil-Enspire.jpg", classifier_ids=["allowedvsnot_1765920808"]),indent=2))
print("-------")
