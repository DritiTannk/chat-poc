from django.conf import settings
from django.core.files.base import ContentFile

import spacy
import boto3


nlp = spacy.load("./output/new_ner")

def predict_entities(user_text):
    """
    This method  tests the model.
    """
    doc = nlp(user_text)

    prediction = {}

    for ent in doc.ents:
        print(ent.text, ent.label_)
        prediction[ent.text] = ent.label_

    return prediction


def text_to_speech(bot_response, bot_instance):
    polly_client = boto3.Session(
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name='ap-south-1').client('polly')

    rec_id = bot_instance.id

    # Synthesize speech
    response = polly_client.synthesize_speech(
        Text= str(bot_response),
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    if 'AudioStream' in response:
        speech_syn = response['AudioStream'].read()
        bot_instance.polly_file.save(f'{rec_id}_file.mp3', ContentFile(speech_syn))
        bot_instance.save()
    else:
        print("Polly Audio Not Found !!")


