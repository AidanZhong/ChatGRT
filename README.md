# How to use

Just run the MainProcess.py, then follow the prompt

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

### 2. Utility Modules
- **intent_matching.py**  
  Contains logic for detecting user intent.  
  - Includes rule-based, similarity-based, or ML-based approaches.

- **identity_management.py**  
  Handles user identification (e.g., storing and recalling names).

- **nlp_utils.py**  
  Tokenization, stemming, lemmatization, and other text-processing utilities.

- **database.py**  
  Mock or actual database to store user information, transactions, and other data.

- **config.py**  
  Configurable settings for prompts, error messages, and other constants.

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
     - Optional ML-based intent classifier.

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

## 7-Day Plan

### Day 1: Planning & Setup
- **Goal**: Set up the project structure and environment.
- **Tasks**:
  - Create the folder structure and initialize Python files.
  - Install dependencies (e.g., NLTK, scikit-learn).
  - Mock intents, responses, and sample transactions.

### Day 2: Intent Matching
- **Goal**: Build and test the intent-matching system.
- **Tasks**:
  - Implement a rule-based intent matcher.
  - Add basic intents (e.g., "book", "order", "help").
  - Test intent detection on various inputs.

### Day 3: Core Functionalities
- **Goal**: Implement identity management and transaction handling.
- **Tasks**:
  - Write logic for recognizing and storing user names.
  - Design a multi-turn dialogue flow for transactions.
  - Test the transaction logic for one scenario (e.g., booking a ticket).

### Day 4: NLP Enhancements
- **Goal**: Add natural language processing features.
- **Tasks**:
  - Implement preprocessing (tokenization, stemming).
  - Improve intent matching with similarity-based techniques (e.g., TF-IDF).
  - Integrate small talk responses.

### Day 5: Error Handling & Personalization
- **Goal**: Enhance user experience.
- **Tasks**:
  - Add error-handling mechanisms for invalid inputs.
  - Implement personalized responses using stored user data.

### Day 6: Testing & Refinement
- **Goal**: Ensure robustness and usability.
- **Tasks**:
  - Test the system end-to-end with different scenarios.
  - Log and fix bugs.
  - Enhance conversational design (e.g., confirmations, contextual prompts).

### Day 7: Demo Video & Documentation
- **Goal**: Finalize deliverables.
- **Tasks**:
  - Record a demo video showcasing all features.
  - Write the report draft, including system architecture and evaluation.
  - Review and submit the project.
