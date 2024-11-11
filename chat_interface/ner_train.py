import spacy
from spacy.tokens import DocBin
from spacy.training import Example
from spacy.util import minibatch
import random

nlp = spacy.blank("en")

def load_data(data_path):
    """
    This method loads the spacy format training data.
    """
    doc_bin = DocBin().from_disk(data_path)
    return list(doc_bin.get_docs(nlp.vocab))


def model_training():
    """
    This method train the custom ner model.
    """
    train_data = load_data("./Output/new_data.spacy")

    # Set up NER component
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    for doc in train_data:
        for ent in doc.ents:
            ner.add_label(ent.label_)

    # Initialize optimizer
    optimizer = nlp.initialize()

    # Training parameters
    n_iter = 40
    batch_size = 2
    dropout = 0.5

    # Training loop
    for epoch in range(n_iter):
        random.shuffle(train_data)
        batches = minibatch(train_data, size=batch_size)

        for batch in batches:
            examples = [Example.from_dict(nlp.make_doc(doc.text),
                                          {"entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]})
                        for doc in batch]
            nlp.update(examples, drop=dropout, sgd=optimizer)

    # Save the trained model
    nlp.to_disk("./Output/new_ner")
    print("Training complete. Model saved to ./Output/new_ner")

def model_test():
    """
    This method  tests the model.
    """
    nlp = spacy.load("./output/new_ner")

    text = "John Doe is the python developer"
    print("Testing new model....")
    doc = nlp(text)

    for ent in doc.ents:
        print(ent.text, ent.label_)

if __name__ == '__main__':
    model_training()
    model_test()


