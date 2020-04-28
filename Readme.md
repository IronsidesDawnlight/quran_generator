# Qur'an Generator

## What Is This?

The Qur'an verse generator is a text-generating network using Textgenrnn by minimaxir.

## How to Use

Please ensure you installed **TensorFlow** and **Textgenrnn**(use pip install). Then, run **generate.py**.

`python generate.py`

## How to Train

The model is already trained. However, If you want to continue training the model (which seems really unnecessary ) or retrain the model, edit **quran_train.py** and run it.

`python quran_train.py`

## Dataset

The dataset is downloaded from [The Koran](https://www.gutenberg.org/ebooks/2800) of Project Gutenberg. All the footnotes, prefaces, introductions, etc. are deleted so that only the verses remain for learning. Format is adjusted, phrase marks are eliminated and empty lines are deleted too.

Also, I only keep a few dozens of Surats in the dataset and delete all the rest for time's sake. I am planning train on the complete version later.

## History and Issues

1. The model keeps copying the original verses without generating anything new. 

   Possible cause: I have trained the model for 90 epochs and this may cause over-fitting. Also is it because the dataset is too small?

   Solution: Re-train.

2. Some specific words, such as "compassionate" and "impulse", failed to show up. This results in the model outputting sentences like "In the name of God the the Merciful".

   Possible cause: This has nothing to do with word length. Also I checked the vocab file and verify that the number of vocabulary has not exceed maximum. I still don't know why this happened. Seems that they are in vocab together with phrase marks?

   Solution: Delete all phrase marks and re-train.



