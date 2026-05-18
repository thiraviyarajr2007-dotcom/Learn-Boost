#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 1 Mathematics Curriculum Generator - TN State Board
Transforms textbook content into Duolingo-style learning modules
Based on TN State Board Class 1 Mathematics syllabus
"""

import json

def generate_class1_curriculum():
    """Generate comprehensive Class 1 Mathematics curriculum"""
    
    curriculum = {
        "class": "1",
        "subject": "Mathematics",
        "chapters": [
            {
                "chapter_name": "NUMBERS 1 TO 10",
                "modules": [
                    {
                        "module_id": "1.1.1",
                        "topic_name": "Learning Numbers 1 to 5",
                        "explanation": "Numbers are like counting friends! Let's learn numbers 1 to 5 by counting our fingers, toys, and things around us. Each number has a special shape and sound. 1 looks like a straight line, 2 like a swan, 3 like two curves, 4 like a triangle missing one side, and 5 like a hat! Counting helps us know how many things we have!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "1_1_1_1",
                                "question_text": "How many fingers do you see? 👍",
                                "options": ["1", "2", "3", "4"],
                                "correct_answer": "1",
                                "rationale": "There is 1 thumb up in the picture.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_1_1_2",
                                "question_text": "Which number comes after 2?",
                                "options": ["1", "3", "4", "5"],
                                "correct_answer": "3",
                                "rationale": "When counting, 3 comes after 2.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_1_1_3",
                                "question_text": "How many apples are there? 🍎🍎🍎",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "rationale": "Count the apples: 1, 2, 3. There are 3 apples.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_1_1_4",
                                "question_text": "Which number is missing: 1, 2, __, 4, 5?",
                                "options": ["1", "2", "3", "4"],
                                "correct_answer": "3",
                                "rationale": "The missing number between 2 and 4 is 3.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_1_1_5",
                                "question_text": "How many eyes do you have?",
                                "options": ["1", "2", "3", "4"],
                                "correct_answer": "2",
                                "rationale": "Everyone has 2 eyes.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "1.1.2",
                        "topic_name": "Learning Numbers 6 to 10",
                        "explanation": "Let's continue our number adventure with 6 to 10! These numbers help us count bigger groups of things. 6 looks like an upside-down 9, 7 like a hockey stick, 8 like two circles stacked, 9 like a balloon on a string, and 10 like 1 and 0 holding hands! We can count our toes, crayons, and friends in class!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "1_1_2_1",
                                "question_text": "How many fingers are on one hand?",
                                "options": ["4", "5", "6", "7"],
                                "correct_answer": "5",
                                "rationale": "One hand has 5 fingers.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_1_2_2",
                                "question_text": "What comes after 7?",
                                "options": ["6", "8", "9", "10"],
                                "correct_answer": "8",
                                "rationale": "When counting, 8 comes after 7.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_1_2_3",
                                "question_text": "How many flowers? 🌸🌸🌸🌸🌸🌸",
                                "options": ["5", "6", "7", "8"],
                                "correct_answer": "6",
                                "rationale": "Count the flowers: 1, 2, 3, 4, 5, 6. There are 6 flowers.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_1_2_4",
                                "question_text": "Which is the biggest number: 3, 7, 2, 9?",
                                "options": ["3", "7", "2", "9"],
                                "correct_answer": "9",
                                "rationale": "9 is the largest number among these options.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_1_2_5",
                                "question_text": "How many total fingers on both hands?",
                                "options": ["8", "9", "10", "11"],
                                "correct_answer": "10",
                                "rationale": "Both hands together have 10 fingers (5 + 5 = 10).",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "ADDITION",
                "modules": [
                    {
                        "module_id": "1.2.1",
                        "topic_name": "Adding with Pictures",
                        "explanation": "Addition is like putting things together! When we add, we combine groups to find out how many we have in total. If you have 2 balls and get 1 more, you have 3 balls total! We can use pictures, fingers, and objects to help us add. The plus sign (+) means 'add' or 'put together'!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "1_2_1_1",
                                "question_text": "2 apples + 1 apple = ? 🍎🍎 + 🍎",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "rationale": "2 + 1 = 3. Count all apples: 1, 2, 3.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_2_1_2",
                                "question_text": "What is 3 + 2?",
                                "options": ["4", "5", "6", "7"],
                                "correct_answer": "5",
                                "rationale": "3 + 2 = 5. Start at 3 and count 2 more: 4, 5.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_2_1_3",
                                "question_text": "4 stars + 1 star = ? ⭐⭐⭐⭐ + ⭐",
                                "options": ["4", "5", "6", "7"],
                                "correct_answer": "5",
                                "rationale": "4 + 1 = 5. Count all stars: 1, 2, 3, 4, 5.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_2_1_4",
                                "question_text": "What does the + sign mean?",
                                "options": ["Take away", "Put together", "Same as", "Different from"],
                                "correct_answer": "Put together",
                                "rationale": "The + sign means to add or put groups together.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_2_1_5",
                                "question_text": "1 + 1 + 1 = ?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "rationale": "1 + 1 + 1 = 3. Count: 1, 2, 3.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "SUBTRACTION",
                "modules": [
                    {
                        "module_id": "1.3.1",
                        "topic_name": "Taking Away",
                        "explanation": "Subtraction is like taking things away! If you have 5 cookies and eat 2, you have 3 left. The minus sign (-) means 'take away' or 'remove'. We can cross out pictures, use fingers, or count backwards to help us subtract. Subtraction helps us find out what's left!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "1_3_1_1",
                                "question_text": "5 balls - 2 balls = ? ⚽⚽⚽⚽⚽ - ⚽⚽",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "rationale": "5 - 2 = 3. Take away 2 from 5, you have 3 left.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_3_1_2",
                                "question_text": "What is 4 - 1?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "rationale": "4 - 1 = 3. Take 1 away from 4, you have 3 left.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_3_1_3",
                                "question_text": "What does the - sign mean?",
                                "options": ["Add", "Take away", "Same", "Different"],
                                "correct_answer": "Take away",
                                "rationale": "The - sign means to subtract or take away.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_3_1_4",
                                "question_text": "6 - 3 = ?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "rationale": "6 - 3 = 3. Take 3 away from 6, you have 3 left.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_3_1_5",
                                "question_text": "If you have 7 candies and give 2 to a friend, how many do you have left?",
                                "options": ["4", "5", "6", "7"],
                                "correct_answer": "5",
                                "rationale": "7 - 2 = 5. You have 5 candies left.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "SHAPES",
                "modules": [
                    {
                        "module_id": "1.4.1",
                        "topic_name": "Basic Shapes",
                        "explanation": "Shapes are all around us! Circles are round like balls and wheels, squares have 4 equal sides like dice, rectangles have 4 sides like books, triangles have 3 sides like pizza slices, and ovals are egg-shaped! Learning shapes helps us describe and organize the world around us. Look for shapes everywhere!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "1_4_1_1",
                                "question_text": "What shape is a ball? ⚽",
                                "options": ["Square", "Circle", "Triangle", "Rectangle"],
                                "correct_answer": "Circle",
                                "rationale": "A ball is round like a circle.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_4_1_2",
                                "question_text": "How many sides does a triangle have? 🔺",
                                "options": ["1", "2", "3", "4"],
                                "correct_answer": "3",
                                "rationale": "A triangle has 3 sides.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_4_1_3",
                                "question_text": "What shape looks like a dice? 🎲",
                                "options": ["Circle", "Triangle", "Square", "Oval"],
                                "correct_answer": "Square",
                                "rationale": "A dice has the shape of a square.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_4_1_4",
                                "question_text": "Which shape is NOT a basic shape?",
                                "options": ["Circle", "Square", "Star", "Triangle"],
                                "correct_answer": "Star",
                                "rationale": "Star is not one of the basic shapes we're learning (circle, square, triangle, rectangle).",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "1_4_1_5",
                                "question_text": "What shape is a book? 📖",
                                "options": ["Circle", "Rectangle", "Triangle", "Oval"],
                                "correct_answer": "Rectangle",
                                "rationale": "A book has the shape of a rectangle.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
    return curriculum

def save_class1_curriculum_to_json():
    """Save the curriculum to a JSON file"""
    curriculum = generate_class1_curriculum()
    
    with open('class1_mathematics_curriculum.json', 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    
    print("Class 1 Mathematics curriculum saved to 'class1_mathematics_curriculum.json'")
    
    # Print statistics
    total_modules = sum(len(chapter['modules']) for chapter in curriculum['chapters'])
    total_questions = 0
    
    for chapter in curriculum['chapters']:
        for module in chapter['modules']:
            total_questions += len(module['questions'])
    
    print(f"Statistics:")
    print(f"  Chapters: {len(curriculum['chapters'])}")
    print(f"  Modules: {total_modules}")
    print(f"  Questions: {total_questions}")

if __name__ == "__main__":
    save_class1_curriculum_to_json()