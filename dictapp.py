import subprocess
import platform
import time

def compare_sentences(sentence1, sentence2):
    """Function to compare words between two sentences"""
    # Split the sentences into words
    words1 = sentence1.split()
    words2 = sentence2.split()

    # Calculate the lengths of the sentences
    len1 = len(words1)
    len2 = len(words2)
    
    # Find the maximum length between the two sentences
    max_len = max(len1, len2)
    
    # Calculate the number of matching words
    matches = sum(1 for word1, word2 in zip(words1[:max_len], words2[:max_len]) if word1 == word2)
    
    # Calculate the percentage of mismatch
    mismatch_percentage = ((max_len - matches) / max_len) * 100
    
    return mismatch_percentage

def introduce_text(text, speed=1000):
    """Function to introduce text with adjustable speed"""
    print("You entered:", text)
    # Adjust the speech rate using the -r option
    command = ['say', '-r', str(speed), text]
    
    # Determine the command based on the operating system
    if platform.system() == 'Windows':
        command = ['PowerShell', '-Command', 'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("%s")' % text]
    elif platform.system() == 'Darwin':
        command = ['say', text]
    elif platform.system() == 'Linux':
        command = ['espeak', text]
    else:
        print("Unsupported platform")
        return
    
    # Delay before playing the text
    time.sleep(3)
    
    # Execute the command to speak the text
    subprocess.run(command)

    # Ask the user to write what they heard
    transcription = input("")
    print("You transcribed:", transcription)

    # Compare transcription with input text
    
    sentence1 = transcription.lower()
    sentence2 = text.lower()
    mismatch_percentage = compare_sentences(sentence1, sentence2)
    print("Percentage of mismatch:", mismatch_percentage)

    if transcription.lower() == text.lower():
        print("Transcription matches the input text.")
    else:
        print("Transcription does not match the input text.")
    
# Continuous text-to-speech loop
while True:
    # Taking user input
    user_input = input("Please enter some text: ")
    
    # Calling the function to introduce the text
    introduce_text(user_input)
    
    # Ask user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Exiting the text-to-speech program. Goodbye!")
        break