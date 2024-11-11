# chat-poc
_This project demonstrates custom NER model training & text-to-speech process through amazon polly service.

### Backend

Python 3.11
Django 5.1.3
Spacy 3.8.2
database - sqlite


### Project Set-Up
1. Clone the repository

   ```git clone url ```

2. Create Virtual environment

   ``` virtualenv env```

3. Install Dependencies

#### kindly make sure your virtual environment is active.

``` pip install -r requirements.tx  ```

4. Create & Run Migrations

```python manage.py makemigrations```
```python manage.py migrate ```

5. Create Database Admin User (Superuser)

```python manage.py createsuperuser```

6. Run Project

```python manage.py runserver```
```http://localhost:8000/```

#### Admin Panel
```http://localhost:8000/admin/```

### NER Training Steps:

1. Create dataset In ".txt" format
2. Annotate the dataset in ".json" format
3. Place the annotate file in the Input Folder
4. Convert json dataset to .spacy format
   ``` python convertor.py```
> - Make sure virtual enviornment is running.
> - The .spacy file will be available in the output directory.

5.Train custom NER Model
   ``` python ner_train.py ```

> Custom Entities Are:
> - Technology
> - Education
> - Person
> - City
> - Country
> - Organization
> - Year

> **__Please make necessary name changes in the above named files for training and testing purpose__**

# Thank you
