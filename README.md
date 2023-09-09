# Drakkar_Spanish_To_English

This is a Python script that implements a console application for a translator. It uses the click library for command-line interface functionality and the pyttsx3 library for text-to-speech conversion. It also imports the mtranslate library for translation functionality and the langid library for language detection.

The script defines a function translate_cli decorated with @click.command(), which serves as the entry point for the command-line application. It clears the console and displays a header.

The application provides a loop that prompts the user to enter text to be translated. It also allows the user to toggle speech output on or off. The text is then translated using the mtranslate library, based on the detected language using the langid library. The translated text is displayed and, if speech output is enabled, the translated text is spoken using the pyttsx3 library.

The script can be run directly by calling translate_cli() if it is the main module being executed.
