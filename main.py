"""
Flashcard Quiz & Spaced Repetition Engine

This module serves as a CLI-based spaced repetition tool. It demonstrates the
practical application of AI/ML concepts like Loss Functions, Gradient Descent,
and Parameter Bounding (Regularization) through flashcard weighting adjustments.

Author: Senior Python Developer & AI/ML Instructor
"""

import os
import json
import random
from datetime import datetime
from typing import List, Dict, Tuple

# Database file paths
CARDS_FILE = "cards.json"
HISTORY_FILE = "quiz_history.txt"

# Spaced Repetition Bounding Constraints (similar to Parameter Bounding / Weight Clipping in AI)
MIN_WEIGHT = 1
MAX_WEIGHT = 15
INITIAL_WEIGHT = 5


def load_cards(filepath: str) -> List[Dict]:
    """
    Loads flashcards from a JSON file.

    AI/ML Analogy:
    This function loads our initial 'model parameters' (the card weights) 
    and 'training samples' (the flashcard questions and answers) from persistent storage.

    If the file does not exist, it should return a default set of flashcards
    or handle the error gracefully.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        List[Dict]: A list of flashcard dictionaries. Each dict contains:
                    'id' (int), 'question' (str), 'answer' (str), 'weight' (int).
    """
    default_cards = [
        {"id": 1, "question": "What keyword defines a function in Python?",
            "answer": "def", "weight": INITIAL_WEIGHT},
        {"id": 2, "question": "What built-in function returns the length of a list?",
            "answer": "len", "weight": INITIAL_WEIGHT},
        {"id": 3, "question": "Which module provides pseudo-random number generators?",
            "answer": "random", "weight": INITIAL_WEIGHT}
    ]
    # =========================================================================
    # TODO: Implement this function.
    # 1. Check if the file exists using os.path.exists()
    # 2. If it does, open and parse the JSON content using json.load()
    # 3. If it doesn't exist, return a default list or create the file with default values
    # Ensure to use standard try-except blocks for robust error handling.
    # =========================================================================
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError) as error:
            print(f"Error warning: {error}")
            return default_cards
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(default_cards, file, indent=4)
            print(f"Created new database file at '{filepath}'.")
    except OSError as error:
        print(f"Error writing to '{filepath}': {error}")
    return default_cards


def save_cards(cards: List[Dict], filepath: str) -> None:
    """
    Saves the flashcard database back to the JSON file to persist progress/weights.

    AI/ML Analogy:
    This represents checkpointing/saving our updated model parameters (weights) 
    to disk after training (practice session) so we don't lose the progress.

    Args:
        cards (List[Dict]): The list of flashcard dictionaries to save.
        filepath (str): Path to the JSON file.
    """
    # =========================================================================
    # TODO: Implement this function.
    # 1. Open the file in write mode ('w')
    # 2. Serialize the 'cards' list back to JSON (hint: json.dump with indent=4)
    # 3. Handle potential file I/O exceptions gracefully.
    # =========================================================================
    pass


def select_card(cards: List[Dict]) -> Dict:
    """
    Selects a flashcard using weighted random selection.

    AI/ML Analogy (Importance Sampling / Loss-weighted selection):
    In machine learning, we often sample training data points proportional to their loss.
    Samples with higher loss (harder examples that the model got wrong) are sampled 
    more frequently to force the model to optimize on them.

    Here:
    - card['weight'] acts as the 'Loss' (error metric).
    - Higher weight = higher loss = higher chance of being selected.

    Args:
        cards (List[Dict]): List of available flashcards.

    Returns:
        Dict: The selected flashcard dictionary.
    """
    # =========================================================================
    # TODO: Implement weighted random selection.
    # 1. Extract weights from all cards in the list.
    # 2. Use Python's built-in random.choices() passing the cards list and
    #    the list of weights as the 'weights' parameter.
    # 3. random.choices() returns a list containing the choice. Extract and return
    #    the single selected card dictionary.
    # Note: Handle empty card list cases gracefully.
    # =========================================================================
    pass


def update_weight(card: Dict, is_correct: bool) -> Dict:
    """
    Updates the weight of a flashcard based on the user's answer.

    AI/ML Analogy (Gradient Descent & Loss Minimization):
    - The weight of a card mimics the 'Loss' (error score) of a training sample.
    - If the user answers CORRECTLY:
      - This indicates low prediction error (low loss).
      - We decrease the weight by 1 (minimum bound = 1).
      - This acts like a Gradient Descent step moving the parameter *down* the loss landscape
        towards the global minimum (mastery/0 loss).
    - If the user answers INCORRECTLY:
      - This indicates high prediction error (high loss).
      - We increase the weight by 3 (maximum bound = 15).
      - This is a larger update step in the opposite direction (stepping *up* the loss)
        to make sure the model (user) encounters this difficult sample much sooner.
    - Bounding between MIN_WEIGHT (1) and MAX_WEIGHT (15) acts like 'Weight Clipping' 
      or 'Regularization' preventing parameters from exploding or vanishing.

    Args:
        card (Dict): The flashcard dictionary being reviewed.
        is_correct (bool): True if user answered correctly, False otherwise.

    Returns:
        Dict: The updated flashcard dictionary.
    """
    # =========================================================================
    # TODO: Implement the Spaced Repetition weight update logic.
    # 1. If is_correct is True: decrease card's weight by 1. Keep it >= MIN_WEIGHT.
    # 2. If is_correct is False: increase card's weight by 3. Keep it <= MAX_WEIGHT.
    # 3. Return the modified card.
    # =========================================================================
    pass


def log_score(total_asked: int, correct_count: int, filepath: str = HISTORY_FILE) -> None:
    """
    Logs session statistics to a local text file.

    AI/ML Analogy:
    This function mimics logging 'epoch statistics' or training metrics
    (e.g., Training Accuracy, Total Epochs) to track model convergence over time.

    The log format should be appended as:
    Timestamp, Questions Asked, Correct Answers, Accuracy %
    e.g., "2026-08-02 15:45:00, 10, 8, 80.00%"

    Args:
        total_asked (int): Total questions encountered in the session.
        correct_count (int): Number of correct answers in the session.
        filepath (str): The text file where history is logged.
    """
    # =========================================================================
    # TODO: Implement score logging.
    # 1. Calculate accuracy percentage (handle division by zero if total_asked is 0).
    # 2. Get the current timestamp (hint: datetime.now().strftime("%Y-%m-%d %H:%M:%S")).
    # 3. Open filepath in append mode ('a') and write/append the formatted session summary.
    # =========================================================================
    pass


def practice_session(cards: List[Dict]) -> Tuple[int, int]:
    """
    Runs a practice loop asking questions until the user decides to return to the main menu.

    Args:
        cards (List[Dict]): The list of flashcards.

    Returns:
        Tuple[int, int]: (questions_asked, correct_answers)
    """
    asked = 0
    correct_count = 0

    print("\n" + "=" * 50)
    print("             PRACTICE SESSION STARTED             ")
    print("Type 'exit' or 'quit' to return to the main menu.")
    print("=" * 50 + "\n")

    while True:
        # Select a card using our weighted selection
        # (This calls the select_card function you will implement)
        card = select_card(cards)
        if not card:
            # Fallback if select_card is not implemented yet or returns None
            print(
                "[Warning] No card selected. Please implement select_card() or ensure card list is non-empty.")
            break

        print(f"Question: {card['question']}")
        user_ans = input("Your Answer: ")

        # Check for session exit command
        if user_ans.strip().lower() in ['exit', 'quit']:
            print("\nEnding practice session...")
            break

        # Clean user input (trim whitespace, case-insensitive check)
        cleaned_user_ans = user_ans.strip().lower()
        cleaned_card_ans = card['answer'].strip().lower()

        # =========================================================================
        # TODO: Compare clean user answer with correct answer
        # 1. Determine if the answer is correct (True/False).
        # 2. Print feedback to the user (e.g., "Correct! 🎉" or "Incorrect. Correct Answer: ...")
        # 3. Update the card's weight using update_weight() based on correctness.
        # 4. Increment the 'asked' and 'correct_count' variables appropriately.
        # 5. Print the updated weight to help visualize the "Gradient Step".
        # 6. Save the cards list state to CARDS_FILE to ensure persistent weights.
        # =========================================================================

        print(
            f"--- (Visualizing loss update: Weight changed to {card['weight']}) ---\n")

    return asked, correct_count


def show_weights(cards: List[Dict]) -> None:
    """
    Displays the current weight distribution of all cards.

    AI/ML Analogy:
    Shows the current parameter weights (loss values) across the database.
    Cards with higher weights are our 'hard examples' that need optimization.
    """
    if not cards:
        print("No cards available to display weights.")
        return

    print("\n" + "=" * 76)
    print(f" {'ID':<5} | {'Weight (Loss)':<15} | {'Question':<50}")
    print("-" * 76)

    # =========================================================================
    # TODO: Print card details formatted cleanly.
    # Loop through 'cards' and print: card['id'], card['weight'], and card['question']
    # structured matching the header above.
    # =========================================================================

    print("-" * 76)
    print("* Tip: Cards with higher weights (higher loss) are prioritized by the sampler.")
    print("=" * 76 + "\n")


def main():
    """
    Main program entry point handling CLI navigation.
    """
    print("=" * 70)
    print("   Welcome to the AI-Inspired Spaced Repetition Flashcard Quiz Engine!  ")
    print("     Optimize your knowledge weights by minimizing learning loss.      ")
    print("=" * 70)

    # Load cards database
    cards = load_cards(CARDS_FILE)

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Start Practice Session")
        print("2. View Card Weight Distributions (Loss Map)")
        print("3. Quit Engine")

        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            if not cards:
                print(
                    "No cards loaded! Please make sure cards.json contains valid flashcards.")
                continue
            asked, correct = practice_session(cards)
            if asked > 0:
                log_score(asked, correct)
                # Persist the final weights after the session concludes
                save_cards(cards, CARDS_FILE)
                print(
                    f"\n[Session Complete] Logged statistics to {HISTORY_FILE}.")

        elif choice == '2':
            show_weights(cards)

        elif choice == '3':
            # Save final card state before exit
            save_cards(cards, CARDS_FILE)
            print(
                "\nExiting Flashcard Engine. Keep optimizing your model parameter weights!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
