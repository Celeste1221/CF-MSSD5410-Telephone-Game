# references:
# deep-translator: https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5
# deep-translator docs: https://deep-translator.readthedocs.io/en/latest/
# for googletrans.Translator:
# https://py-googletrans.readthedocs.io/en/latest/#:~:text=Quick%20search-,Googletrans%3A%20Free%20and%20Unlimited%20Google%20translate%20API%20for%20Python,that%20implemented%20Google%20Translate%20API.
# for google_trans_new:
# https://pypi.org/project/google-trans-new/
# for my memory translator
# https://mymemory.translated.net/

from functools import lru_cache
from functions import *
from deep_translator import LibreTranslator
# from tkinter import *

# libre examples
# translated = LibreTranslator(source='german', target='english').translate(text=text)
# translated = LibreTranslator(source='auto', target='en').translate_batch(texts)
# translated = LibreTranslator(source='auto', target='en').translate_file('path/to/file')


# translate to Spanish, use lru_cache to limit api calls
@lru_cache()
def target_spanish(input_text):
    return LibreTranslator(source='auto', target='es').translate(text=input_text)


# translate to German
@lru_cache()
def target_german(input_text):
    return LibreTranslator(source='auto', target='de').translate(text=input_text)


# translate back to English
@lru_cache()
def back_to_eng(input_text):
    return LibreTranslator(source='auto', target='en').translate(text=input_text)


def get_user_input():
    text = input("Enter a message in English to translate (or enter 'q' to quit): ")
    return text


## the following was an attempt to do this through a tkinter form but was unable to get it to work
# def make_tk_form():
    # parent = Tk()
    # parent.geometry("600x400")
    # parent.config(bg="lightBlue")
    # Label(parent, bg="lightBlue", text="Enter message in English.").place(x=50, y=20)
    # input1 = Text(parent, width=100, height=7).place(x=50, y=50)
    #
    # Label(parent, bg="lightBlue", text="Here are your intermediate message translation(s).") \
    #     .place(x=50, y=180)
    # output1 = Message(parent, text="", width=100, bg="lightBlue").place(x=50, y=210)
    #
    # Label(parent, bg="lightBlue", text="Here is your message back in the original language after passing through\
    # the translators.") \
    #     .place(x=50, y=340)
    #
    # output2 = Message(parent, text="", width=100, bg="lightBlue").place(x=50, y=370)
    #
    # engbtn = Button(parent, text="Back to English", command=original_lang)
    # engbtn.pack(side=BOTTOM, fill='x')
    # spanbtn = Button(parent, text="Spanish", command=target_spanish)
    # spanbtn.pack(side=BOTTOM, fill='x')
    # germanbtn = Button(parent, text="German", command=target_german)
    # germanbtn.pack(side=BOTTOM, fill='x')
    # parent.mainloop()


def main():
    # ask user for text to translate
    # translations are limited by number or characters. I think Libre's limit is 5000. It will not
    # take a whole sonnet
    # initial_text = get_user_input()
    initial_text = get_user_input()
    while initial_text != 'q':

        # play telephone
        print("\nYou entered: {0}".format(initial_text))
        span = target_spanish(initial_text)
        print("\nOriginal English to Spanish translation: {0}".format(span))
        german = target_german(span)
        print("\nSpanish to German translation: {0}".format(german))
        final_text = back_to_eng(german)
        print("\nGerman back to English translation: {0}".format(final_text))

        # remove white space, caps, and punctuation in order to run LCS and edit distance algorithms on data
        initial_text = clean_str(initial_text)
        # to get the lcs and edit dist by character
        # initial_text = ''.join(initial_text)
        end_text = clean_str(final_text)
        # to get the lcs and edit dist by character
        # end_text = ''.join(end_text)
        print(initial_text)
        print(end_text)

        original_length = len(initial_text)
        translated_length = len(final_text)

        # get longest common substring between beginning English text and final English text
        lcs = LCSubStr(initial_text, end_text, original_length, translated_length)

        # get the edit distance between beginning English text and final English text
        edit_dist = editDistDP(initial_text, end_text, len(initial_text), len(end_text))

        # let user know results
        print("Original text has {0} words. The end result has {1} words. "
              "\nThe edit distance by word is {2} and the longest common substring is {3}"
              .format(original_length, translated_length, edit_dist, lcs))
        get_user_input()
    print("Goodbye")


if __name__ == "__main__":
    main()

