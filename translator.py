import click
import pyttsx3
from mtranslate import translate as mtranslate
import langid

VERSION = "1.0.1"

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust the speaking rate if needed

# Mapping of language codes for translation
language_mapping = {
    'en': 'es',
    'es': 'en'
}

@click.command()
@click.version_option(version=VERSION)
def translate_cli():
    """Drakkar Interactive Translator - Console App"""

    click.clear()

    click.secho("============================================", fg="blue", bold=True)
    click.secho("=         Drakkar Interactive Translator   =", fg="blue", bold=True)
    click.secho("============================================\n", fg="blue", bold=True)

    enable_speech = True
    while True:
        click.echo(f"Speech is {click.style('enabled', fg='green') if enable_speech else click.style('disabled', fg='red')}.\n")

        text = click.prompt(click.style("Enter the text to be translated (or 'q' to quit, 'toggle' to enable/disable speech)", fg="yellow"))

        if text.lower() == 'q':
            break

        if not text.strip():
            click.echo(click.style("Please enter the text to be translated.\n", fg="red"))
            continue

        text_lower = text.lower()

        if text_lower == 'toggle':
            enable_speech = not enable_speech
            continue

        original_lang = langid.classify(text)[0]
        dest_lang = language_mapping.get(original_lang)
        if dest_lang:
            translated_text = mtranslate(text, dest_lang, original_lang)
            click.echo("\n--------------------------------------------")
            click.echo(f"Translated Text: {click.style(translated_text, bold=True)}")
            click.echo("--------------------------------------------\n")
            if enable_speech:
                engine.say(translated_text)
                engine.runAndWait()
        else:
            click.echo(click.style("\nUnsupported language detected. Please enter text in English or Spanish.\n", fg="red"))

if __name__ == "__main__":
    translate_cli()
