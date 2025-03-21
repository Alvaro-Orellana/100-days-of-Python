# question_data = [
#    {"text": "A slug's blood is green.", "answer": "True"},
#    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
#    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
#    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

question_data = [

    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "In the movie The Revenant, DiCaprio&#039;s character hunts down the killer of his son.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "In the original Star Wars trilogy, David Prowse was the actor who physically portrayed Darth Vader.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "George Lucas directed the entire original Star Wars trilogy.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "Leonardo DiCaprio won an Oscar for Best Actor in 2004&#039;s &quot;The Aviator&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "Actor Tommy Chong served prison time.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "In Alfred Hitchcock&#039;s film &#039;Psycho&#039; it is said he used chocolate syrup to simulate the blood in the famous shower scene from ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "The word &quot;Inception&quot; came from the 2010 blockbuster hit &quot;Inception&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "In the original script of &quot;The Matrix&quot;, the machines used humans as additional computing power instead of batteries.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "Brandon Routh plays the titular character in the movie &quot;John Wick&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "Samuel L. Jackson had the words, &#039;Bad Motherf*cker&#039; in-scripted on his lightsaber during the filming of Star Wars.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]

from question_model import Question

questions = [Question(q["question"], q["correct_answer"]) for q in question_data]
