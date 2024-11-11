from tqdm import tqdm
import json
import spacy
from spacy.tokens import DocBin

def convertor():

    nlp = spacy.blank("en")
    db = DocBin()

    with open("./Input/new_data_annot.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for text, annot in tqdm(data): # data in previous format
        doc = nlp.make_doc(text) # create doc object from text
        ents = []
        for start, end, label in annot["entities"]: # add character indexes
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents # label the text with the ents
        db.add(doc)

    db.to_disk("./Output/new_data.spacy") # save the docbin obj

if __name__ == '__main__':
    convertor()
    print("\n Training Dataset Created Successfully For The Spacy Format.")