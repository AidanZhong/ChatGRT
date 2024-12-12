# How to use

Just run the main.py, then follow the prompt

# Architecture

1. Identity matching (required to every time we use it)
2. Greetings to the user
3. Intent matching (Asking the user what he wants to do)

## All the intent could function

1. Answering question (Query weather, answer something like what is xxx?)
2. Book a flight ticket
3. Small talk

# COMP3074 Coursework Plan

## Code Structure

### 1. Main Modules
- **MainProcess.py**  
  Entry point for the chatbot.  
  - Initializes modules like intent matching, transactions, etc.  
  - Main interaction loop.

- **FlightTicketBooking.py**  
  Handle the transaction of booking a flight.

- **SmallTalk.py**  
  Handles predefined conversational responses for small talk.

- **Greetings.py**  
  Handle greetings.

- **QandA.py**  
  Handle question and answers.

### 2. Utility Modules
- **intent_matching.py**  
  Contains logic for detecting user intent.  
  - Includes rule-based, similarity-based, or ML-based approaches.

- **identity_management.py**  
  Handles user identification (e.g., storing and recalling names).

- **similarity.py**  
  Handles similarity checking.

### 3. Data Files
- **data/**  
  Contains datasets, predefined intents, and small talk responses.

- **logs/**  
  Stores interaction logs for debugging or evaluation.

### 4. Testing
- **tests/**  
  Unit tests for each module.

### 5. Documentation
- **README.md**  
  Overview of the system, setup instructions, and usage.

- **report/**  
  Stores diagrams and text files to support the report writing.

---

### 6. Transactional function (flight ticket booking)


## Functional Structure

1. **Initialization**
   - Load configurations and intents.
   - Initialize database or mock data.

2. **Input Processing**
   - Preprocess the user input using `nlp_utils.py`.

3. **Intent Matching**
   - Predict user intent using:
     - Rule-based patterns (e.g., regex).
     - Similarity-based methods (e.g., cosine similarity with TF-IDF).

4. **Intent Handling**
   - Route user input to the relevant handler (e.g., transaction, identity management).
   - Handle invalid or unrecognized intents.

5. **Identity Management**
   - Recognize phrases like “My name is [name]” or “Call me [nickname].”
   - Store and recall the user’s name for personalization.

6. **Transaction Processing**
   - Engage in multi-turn dialogues for task completion.
   - Validate user inputs and handle edge cases (e.g., ambiguous dates).

7. **Small Talk**
   - Provide predefined responses for casual questions.

8. **Error Handling**
   - Suggest valid commands or re-prompt the user.

9. **Output Generation**
   - Generate and display responses in a user-friendly format.

---
