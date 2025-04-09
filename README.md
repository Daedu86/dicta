# Text-to-Speech Typing Accuracy Game

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run)
- [Example](#example)

## Overview

This Python program is a fun and interactive way to practice listening and typing accuracy. It reads aloud a sentence you provide and then asks you to type what you heard. After you input your transcription, the program compares your text to the original and calculates the mismatch percentage.

The program continues running in a loop until you decide to exit.

## Features
- **Text-to-Speech (TTS)**: Converts input text to speech.
- **Cross-platform support**:
  - Windows: Uses PowerShell and SpeechSynthesizer.
  - macOS: Uses the `say` command.
  - Linux: Uses `espeak`.
- **Typing Accuracy Check**: Compares your transcription to the original and calculates mismatch percentage.
- **Continuous Loop**: Allows multiple rounds of practice.

## Prerequisites
- Python 3.x installed
- For Linux users: Ensure `espeak` is installed using:
  ```bash
  sudo apt install espeak
  ```

## How It Works
1. The program asks you to enter a sentence.
2. It reads the sentence aloud after a short delay.
3. You type what you heard.
4. The program compares your typed text with the original.
5. It displays the percentage of mismatch and whether it matches exactly.
6. It asks if you want to play again.

## How to Run

1. Save the Python code into a file, e.g., `text_to_speech_game.py`.
2. Open the terminal or command prompt.
3. Navigate to the folder where you saved the file.
4. Run the script:
   ```bash
   python text_to_speech_game.py
   ```

## Example

Below is a screenshot of a successful run on Windows:

![Example Run](https://github.com/Daedu86/dicta/blob/main/Dicta.jpg)

In this example, the user entered "Tell me more about it" and transcribed it correctly with 0.0% mismatch.

---

Enjoy practicing your listening and typing skills!

