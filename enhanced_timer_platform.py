#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Educational Platform - Extended Timers for Class 10-12
With Warning System for Last 10 Seconds
"""

import json

def create_enhanced_timer_platform():
    """Create enhanced platform with extended timers and warnings"""
    
    platform = {
        "platform_info": {
            "name": "Learn Edu - Enhanced Timer Platform",
            "version": "3.0.0",
            "description": "TN State Board Mathematics with Extended Timers for Advanced Students",
            "target_grades": "Classes 10-12",
            "enhanced_features": "Extended timers with warning system"
        },
        
        "timer_configuration": {
            "class_specific_settings": {
                "Class 10": {
                    "base_timer_seconds": {
                        "easy": 45,
                        "medium": 60,
                        "hard": 90
                    },
                    "extra_time_seconds": {
                        "easy": 15,
                        "medium": 30,
                        "hard": 60
                    },
                    "total_timer_seconds": {
                        "easy": 60,
                        "medium": 90,
                        "hard": 150
                    }
                },
                "Class 11": {
                    "base_timer_seconds": {
                        "easy": 60,
                        "medium": 90,
                        "hard": 120
                    },
                    "extra_time_seconds": {
                        "easy": 30,
                        "medium": 45,
                        "hard": 90
                    },
                    "total_timer_seconds": {
                        "easy": 90,
                        "medium": 135,
                        "hard": 210
                    }
                },
                "Class 12": {
                    "base_timer_seconds": {
                        "easy": 75,
                        "medium": 120,
                        "hard": 180
                    },
                    "extra_time_seconds": {
                        "easy": 45,
                        "medium": 60,
                        "hard": 120
                    },
                    "total_timer_seconds": {
                        "easy": 120,
                        "medium": 180,
                        "hard": 300
                    }
                }
            },
            
            "warning_system": {
                "warning_threshold_seconds": 10,
                "warning_messages": [
                    "⏰ Time is running out! Only 10 seconds remaining!",
                    "⚠️ Hurry! 10 seconds left to answer!",
                    "🔔 Warning: 10 seconds remaining!",
                    "⌛ Last 10 seconds - make your choice now!"
                ],
                "warning_colors": {
                    "background": "#FFF3CD",
                    "text": "#856404",
                    "border": "#FFC107"
                },
                "warning_animation": "pulse",
                "sound_enabled": True,
                "vibration_enabled": True
            },
            
            "time_display": {
                "show_seconds": True,
                "show_progress_bar": True,
                "color_coding": {
                    "plenty_of_time": "#28A745",  # Green
                    "moderate_time": "#FFC107",   # Yellow  
                    "running_out": "#DC3545",     # Red
                    "warning": "#FF6B6B"           # Light Red
                },
                "time_thresholds": {
                    "plenty_of_time": 0.5,        # More than 50% time remaining
                    "moderate_time": 0.25,        # 25-50% time remaining
                    "running_out": 0.15,         # 15-25% time remaining
                    "warning": 0.10              # Less than 15% time remaining
                }
            }
        },
        
        "enhanced_class10_curriculum": {
            "class": "10",
            "subject": "Mathematics",
            "chapters": [
                {
                    "chapter_name": "RELATIONS AND FUNCTIONS",
                    "modules": [
                        {
                            "module_id": "10.1.1",
                            "topic_name": "Ordered Pair and Cartesian Product",
                            "explanation": "Ordered pairs are like coordinates on a map - the order matters! (2,3) is different from (3,2). Cartesian product combines two sets to create all possible ordered pairs, like pairing every shirt with every pant in your wardrobe. If Set A has 3 elements and Set B has 4 elements, their Cartesian product A×B has 3×4=12 ordered pairs. This concept is fundamental for understanding relations and functions!",
                            "difficulty": "medium",
                            "total_timer_minutes": 15,  # Extended from 12
                            "questions": [
                                {
                                    "question_id": "10_1_1_1",
                                    "question_text": "What is an ordered pair?",
                                    "options": ["A pair of elements where order matters", "A pair of elements where order doesn't matter", "A single element", "A set of two elements"],
                                    "correct_answer": "A pair of elements where order matters",
                                    "rationale": "In an ordered pair (a,b), the position of a and b is significant, making (a,b) different from (b,a).",
                                    "timer_per_question_seconds": 90,  # Extended from 45
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Time running out! Choose your answer carefully!"
                                },
                                {
                                    "question_id": "10_1_1_2",
                                    "question_text": "If A = {1, 2} and B = {3, 4}, what is A × B?",
                                    "options": ["{(1,3), (1,4), (2,3), (2,4)}", "{(3,1), (3,2), (4,1), (4,2)}", "{1, 2, 3, 4}", "{(1,2), (3,4)}"],
                                    "correct_answer": "{(1,3), (1,4), (2,3), (2,4)}",
                                    "rationale": "Cartesian product A×B pairs each element of A with each element of B in that order.",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ 10 seconds left! Think carefully about Cartesian products!"
                                },
                                {
                                    "question_id": "10_1_1_3",
                                    "question_text": "If A has 3 elements and B has 4 elements, how many ordered pairs are in A × B?",
                                    "options": ["12", "7", "3", "4"],
                                    "correct_answer": "12",
                                    "rationale": "Number of ordered pairs in A × B = |A| × |B| = 3 × 4 = 12.",
                                    "timer_per_question_seconds": 60,  # Medium difficulty
                                    "warning_enabled": True,
                                    "warning_message": "🔔 Hurry! 10 seconds remaining to solve this!"
                                },
                                {
                                    "question_id": "10_1_1_4",
                                    "question_text": "What is B × A if A = {1, 2} and B = {3, 4}?",
                                    "options": ["{(3,1), (3,2), (4,1), (4,2)}", "{(1,3), (1,4), (2,3), (2,4)}", "{(1,2), (3,4)}", "{(1,3), (2,4)}"],
                                    "correct_answer": "{(3,1), (3,2), (4,1), (4,2)}",
                                    "rationale": "B × A pairs each element of B with each element of A: (3,1), (3,2), (4,1), (4,2).",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⌛ Last 10 seconds! Make your choice now!"
                                },
                                {
                                    "question_id": "10_1_1_5",
                                    "question_text": "When is A × B equal to B × A?",
                                    "options": ["When A = B", "Never", "When A and B have one element each", "Always"],
                                    "correct_answer": "When A = B",
                                    "rationale": "A × B = B × A only when sets A and B are equal.",
                                    "timer_per_question_seconds": 60,
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Time warning! 10 seconds left!"
                                },
                                {
                                    "question_id": "10_1_1_6",
                                    "question_text": "If A = ∅ and B = {1, 2, 3}, what is A × B?",
                                    "options": ["∅", "{∅}", "{(∅,1), (∅,2), (∅,3)}", "{1,2,3}"],
                                    "correct_answer": "∅",
                                    "rationale": "Cartesian product with empty set is always empty set.",
                                    "timer_per_question_seconds": 45,  # Easy question
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ 10 seconds remaining!"
                                },
                                {
                                    "question_id": "10_1_1_7",
                                    "question_text": "What is the first element of the ordered pair (5,8)?",
                                    "options": ["5", "8", "13", "40"],
                                    "correct_answer": "5",
                                    "rationale": "In ordered pair (a,b), a is the first element and b is the second element.",
                                    "timer_per_question_seconds": 45,
                                    "warning_enabled": True,
                                    "warning_message": "🔔 Hurry up! 10 seconds left!"
                                },
                                {
                                    "question_id": "10_1_1_8",
                                    "question_text": "If A = {a, b} and B = {1, 2, 3}, how many elements are in A × B?",
                                    "options": ["6", "5", "3", "2"],
                                    "correct_answer": "6",
                                    "rationale": "|A × B| = |A| × |B| = 2 × 3 = 6 elements.",
                                    "timer_per_question_seconds": 60,
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Time running out! Choose quickly!"
                                },
                                {
                                    "question_id": "10_1_1_9",
                                    "question_text": "Which coordinate represents the point where x=4 and y=2?",
                                    "options": ["(4,2)", "(2,4)", "(4,4)", "(2,2)"],
                                    "correct_answer": "(4,2)",
                                    "rationale": "Point with x-coordinate 4 and y-coordinate 2 is (4,2).",
                                    "timer_per_question_seconds": 45,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ 10 seconds warning!"
                                },
                                {
                                    "question_id": "10_1_1_10",
                                    "question_text": "What is the Cartesian product of {1} and {a, b, c}?",
                                    "options": ["{(1,a), (1,b), (1,c)}", "{(a,1), (b,1), (c,1)}", "{1, a, b, c}", "{(1,a,b,c)}"],
                                    "correct_answer": "{(1,a), (1,b), (1,c)}",
                                    "rationale": "{1} × {a,b,c} = {(1,a), (1,b), (1,c)} - pairing 1 with each element.",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⌛ Last 10 seconds! Final chance!"
                                }
                            ]
                        },
                        {
                            "module_id": "10.1.2",
                            "topic_name": "Relations",
                            "explanation": "Relations are like connections between people in a social network! A relation is a subset of Cartesian product that shows which pairs are 'related' or connected. For example, in the relation 'is less than' from {1,2,3} to {4,5,6}, only pairs like (1,4), (1,5), (1,6), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6) are included. Relations help us understand how elements from different sets are connected!",
                            "difficulty": "medium",
                            "total_timer_minutes": 15,
                            "questions": [
                                {
                                    "question_id": "10_1_2_1",
                                    "question_text": "What is a relation?",
                                    "options": ["A subset of Cartesian product", "The entire Cartesian product", "A single ordered pair", "An empty set"],
                                    "correct_answer": "A subset of Cartesian product",
                                    "rationale": "A relation is any subset of the Cartesian product of two sets.",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Time warning! 10 seconds remaining!"
                                },
                                {
                                    "question_id": "10_1_2_2",
                                    "question_text": "If A = {1, 2, 3} and B = {4, 5}, which of these is a valid relation from A to B?",
                                    "options": ["{(1,4), (2,5)}", "{(4,1), (5,2)}", "{1, 2, 3, 4, 5}", "{(1,2), (3,4)}"],
                                    "correct_answer": "{(1,4), (2,5)}",
                                    "rationale": "A relation from A to B must have ordered pairs where first element is from A and second from B.",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ Hurry! 10 seconds left to answer!"
                                },
                                {
                                    "question_id": "10_1_2_3",
                                    "question_text": "What is the domain of the relation R = {(1,4), (2,5), (3,6)}?",
                                    "options": ["{1, 2, 3}", "{4, 5, 6}", "{1, 4, 2, 5, 3, 6}", "{1, 2, 3, 4, 5, 6}"],
                                    "correct_answer": "{1, 2, 3}",
                                    "rationale": "Domain is the set of all first elements of the ordered pairs in the relation.",
                                    "timer_per_question_seconds": 75,
                                    "warning_enabled": True,
                                    "warning_message": "🔔 10 seconds remaining!"
                                },
                                {
                                    "question_id": "10_1_2_4",
                                    "question_text": "What is the range of the relation R = {(1,4), (2,5), (3,6)}?",
                                    "options": ["{4, 5, 6}", "{1, 2, 3}", "{1, 4, 2, 5, 3, 6}", "{1, 2, 3, 4, 5, 6}"],
                                    "correct_answer": "{4, 5, 6}",
                                    "rationale": "Range is the set of all second elements of the ordered pairs in the relation.",
                                    "timer_per_question_seconds": 75,
                                    "warning_enabled": True,
                                    "warning_message": "⌛ Last 10 seconds! Choose now!"
                                },
                                {
                                    "question_id": "10_1_2_5",
                                    "question_text": "How many relations are possible from a set with 2 elements to a set with 3 elements?",
                                    "options": ["64", "6", "8", "32"],
                                    "correct_answer": "64",
                                    "rationale": "Total possible ordered pairs = 2 × 3 = 6. Number of relations = 2^6 = 64.",
                                    "timer_per_question_seconds": 120,  # Extended for complex question
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Complex question! Take your time - 10 seconds warning when needed!"
                                },
                                {
                                    "question_id": "10_1_2_6",
                                    "question_text": "What is the empty relation?",
                                    "options": ["A relation with no ordered pairs", "A relation with all ordered pairs", "A relation with one ordered pair", "A relation that is a function"],
                                    "correct_answer": "A relation with no ordered pairs",
                                    "rationale": "Empty relation contains no ordered pairs - it's the empty set.",
                                    "timer_per_question_seconds": 60,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ 10 seconds warning!"
                                },
                                {
                                    "question_id": "10_1_2_7",
                                    "question_text": "What is the universal relation?",
                                    "options": ["A relation containing all ordered pairs", "A relation with no ordered pairs", "A relation with one ordered pair", "A relation that is a function"],
                                    "correct_answer": "A relation containing all ordered pairs",
                                    "rationale": "Universal relation contains all possible ordered pairs from A × B.",
                                    "timer_per_question_seconds": 75,
                                    "warning_enabled": True,
                                    "warning_message": "🔔 Hurry! 10 seconds left!"
                                },
                                {
                                    "question_id": "10_1_2_8",
                                    "question_text": "If R = {(x,y) | x² = y} where x ∈ {1,2,3}, what is R?",
                                    "options": ["{(1,1), (2,4), (3,9)}", "{(1,1), (2,2), (3,3)}", "{(1,1), (4,2), (9,3)}", "{(1,1)}"],
                                    "correct_answer": "{(1,1), (2,4), (3,9)}",
                                    "rationale": "1²=1, 2²=4, 3²=9, so pairs are (1,1), (2,4), (3,9).",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⌛ Last 10 seconds! Final choice!"
                                },
                                {
                                    "question_id": "10_1_2_9",
                                    "question_text": "If R = {(1,2), (1,3), (2,4)}, is R a function?",
                                    "options": ["No", "Yes", "Sometimes", "Cannot determine"],
                                    "correct_answer": "No",
                                    "rationale": "R is not a function because 1 is related to both 2 and 3 (one input has multiple outputs).",
                                    "timer_per_question_seconds": 60,
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Time warning! 10 seconds left!"
                                },
                                {
                                    "question_id": "10_1_2_10",
                                    "question_text": "What is the inverse relation of R = {(1,4), (2,5), (3,6)}?",
                                    "options": ["{(4,1), (5,2), (6,3)}", "{(1,4), (2,5), (3,6)}", "{(6,3), (5,2), (4,1)}", "{(1,6), (2,5), (3,4)}"],
                                    "correct_answer": "{(4,1), (5,2), (6,3)}",
                                    "rationale": "Inverse relation swaps each ordered pair: (a,b) becomes (b,a).",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ 10 seconds remaining! Choose wisely!"
                                }
                            ]
                        },
                        {
                            "module_id": "10.1.3",
                            "topic_name": "Functions",
                            "explanation": "Functions are like special machines - you put in an input and get exactly one output! A function is a relation where each element in the domain is paired with exactly one element in the range. Think of a vending machine: press button A (input) and you always get the same snack (output). Functions are everywhere - from calculating grades to predicting weather, they help us understand how one quantity depends on another!",
                            "difficulty": "hard",
                            "total_timer_minutes": 20,  # Extended for complex topic
                            "questions": [
                                {
                                    "question_id": "10_1_3_1",
                                    "question_text": "What is the defining property of a function?",
                                    "options": ["Each input has exactly one output", "Each output has exactly one input", "All inputs are related", "All outputs are unique"],
                                    "correct_answer": "Each input has exactly one output",
                                    "rationale": "A function assigns exactly one output to each input in its domain.",
                                    "timer_per_question_seconds": 120,  # Extended for complex question
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Complex concept! 10 seconds warning when needed!"
                                },
                                {
                                    "question_id": "10_1_3_2",
                                    "question_text": "Which of these relations is a function?",
                                    "options": ["{(1,2), (2,3), (3,4)}", "{(1,2), (1,3), (2,4)}", "{(1,2), (2,1), (1,3)}", "{(1,1), (2,2), (3,3), (1,4)}"],
                                    "correct_answer": "{(1,2), (2,3), (3,4)}",
                                    "rationale": "Each input (1,2,3) has exactly one output, satisfying the function definition.",
                                    "timer_per_question_seconds": 120,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ Think carefully! 10 seconds warning!"
                                },
                                {
                                    "question_id": "10_1_3_3",
                                    "question_text": "What is the domain of f(x) = 2x + 1?",
                                    "options": ["All real numbers", "All positive numbers", "All integers", "All natural numbers"],
                                    "correct_answer": "All real numbers",
                                    "rationale": "For any real x, 2x + 1 is defined, so domain is all real numbers.",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "🔔 10 seconds remaining!"
                                },
                                {
                                    "question_id": "10_1_3_4",
                                    "question_text": "What is the range of f(x) = x² where x ∈ ℝ?",
                                    "options": ["All non-negative real numbers", "All real numbers", "All positive real numbers", "All integers"],
                                    "correct_answer": "All non-negative real numbers",
                                    "rationale": "x² is always ≥ 0 for real x, so range is [0, ∞).",
                                    "timer_per_question_seconds": 120,
                                    "warning_enabled": True,
                                    "warning_message": "⌛ Last 10 seconds! Make your choice!"
                                },
                                {
                                    "question_id": "10_1_3_5",
                                    "question_text": "If f(x) = 3x - 2, what is f(4)?",
                                    "options": ["10", "14", "6", "12"],
                                    "correct_answer": "10",
                                    "rationale": "f(4) = 3(4) - 2 = 12 - 2 = 10.",
                                    "timer_per_question_seconds": 75,
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Time warning! 10 seconds left!"
                                },
                                {
                                    "question_id": "10_1_3_6",
                                    "question_text": "What type of function is f(x) = 2x + 3?",
                                    "options": ["Linear function", "Quadratic function", "Cubic function", "Reciprocal function"],
                                    "correct_answer": "Linear function",
                                    "rationale": "f(x) = 2x + 3 has the form ax + b, which is a linear function.",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ 10 seconds remaining!"
                                },
                                {
                                    "question_id": "10_1_3_7",
                                    "question_text": "What is the domain of f(x) = 1/(x-2)?",
                                    "options": ["All real numbers except 2", "All real numbers", "All positive numbers", "All numbers except 0"],
                                    "correct_answer": "All real numbers except 2",
                                    "rationale": "Division by zero is undefined, so x-2 ≠ 0, meaning x ≠ 2.",
                                    "timer_per_question_seconds": 120,
                                    "warning_enabled": True,
                                    "warning_message": "🔔 Hurry! 10 seconds left!"
                                },
                                {
                                    "question_id": "10_1_3_8",
                                    "question_text": "If f(x) = x² and g(x) = x + 1, what is f(g(2))?",
                                    "options": ["9", "5", "4", "7"],
                                    "correct_answer": "9",
                                    "rationale": "g(2) = 2 + 1 = 3. Then f(g(2)) = f(3) = 3² = 9.",
                                    "timer_per_question_seconds": 150,  # Extended for composition
                                    "warning_enabled": True,
                                    "warning_message": "⌛ Composition question! 10 seconds warning!"
                                },
                                {
                                    "question_id": "10_1_3_9",
                                    "question_text": "Which function has a parabola as its graph?",
                                    "options": ["f(x) = x²", "f(x) = 2x + 1", "f(x) = 1/x", "f(x) = √x"],
                                    "correct_answer": "f(x) = x²",
                                    "rationale": "Quadratic functions like x² have parabolic graphs.",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Time warning! 10 seconds left!"
                                },
                                {
                                    "question_id": "10_1_3_10",
                                    "question_text": "What is the range of f(x) = -x² + 4?",
                                    "options": ["(-∞, 4]", "[4, ∞)", "(-∞, ∞)", "[0, 4]"],
                                    "correct_answer": "(-∞, 4]",
                                    "rationale": "Since coefficient of x² is negative, parabola opens downward with maximum at y = 4.",
                                    "timer_per_question_seconds": 150,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ Complex range question! 10 seconds warning!"
                                },
                                {
                                    "question_id": "10_1_3_11",
                                    "question_text": "If f: ℝ → ℝ is defined by f(x) = 2x + 5, what is f⁻¹(x)?",
                                    "options": ["(x - 5)/2", "(x + 5)/2", "2x - 5", "(x/2) + 5"],
                                    "correct_answer": "(x - 5)/2",
                                    "rationale": "To find inverse: y = 2x + 5. Solve for x: x = (y - 5)/2. So f⁻¹(x) = (x - 5)/2.",
                                    "timer_per_question_seconds": 180,  # Extended for inverse
                                    "warning_enabled": True,
                                    "warning_message": "🔔 Inverse function! 10 seconds warning!"
                                },
                                {
                                    "question_id": "10_1_3_12",
                                    "question_text": "What type of function is f(x) = 1/x?",
                                    "options": ["Reciprocal function", "Linear function", "Quadratic function", "Cubic function"],
                                    "correct_answer": "Reciprocal function",
                                    "rationale": "f(x) = 1/x is a reciprocal function, also called hyperbola.",
                                    "timer_per_question_seconds": 90,
                                    "warning_enabled": True,
                                    "warning_message": "⌛ Last 10 seconds! Choose now!"
                                },
                                {
                                    "question_id": "10_1_3_13",
                                    "question_text": "If f(x) = x³, what is the range when domain is ℝ?",
                                    "options": ["All real numbers", "All non-negative numbers", "All positive numbers", "All negative numbers"],
                                    "correct_answer": "All real numbers",
                                    "rationale": "Cubic function x³ takes all real values as x varies over real numbers.",
                                    "timer_per_question_seconds": 120,
                                    "warning_enabled": True,
                                    "warning_message": "⏰ Time warning! 10 seconds left!"
                                },
                                {
                                    "question_id": "10_1_3_14",
                                    "question_text": "What is the composition (f∘g)(x) if f(x) = x + 2 and g(x) = 3x?",
                                    "options": ["3x + 2", "3(x + 2)", "x + 6", "3x + 6"],
                                    "correct_answer": "3x + 2",
                                    "rationale": "(f∘g)(x) = f(g(x)) = f(3x) = 3x + 2.",
                                    "timer_per_question_seconds": 150,
                                    "warning_enabled": True,
                                    "warning_message": "⚠️ Composition! 10 seconds warning!"
                                },
                                {
                                    "question_id": "10_1_3_15",
                                    "question_text": "Which function is one-to-one but not onto from ℝ to ℝ?",
                                    "options": ["f(x) = eˣ", "f(x) = x²", "f(x) = sin x", "f(x) = x³"],
                                    "correct_answer": "f(x) = eˣ",
                                    "rationale": "eˣ is one-to-one but its range is (0, ∞), not all ℝ, so not onto.",
                                    "timer_per_question_seconds": 180,
                                    "warning_enabled": True,
                                    "warning_message": "🔔 Advanced concept! 10 seconds warning!"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        
        "warning_system_implementation": {
            "frontend_integration": {
                "html_structure": """
                    <div class="timer-container">
                        <div class="timer-display" id="timer">
                            <span class="time-remaining">90</span>s
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="progress"></div>
                        </div>
                        <div class="warning-message" id="warning" style="display: none;">
                            <span class="warning-icon">⏰</span>
                            <span class="warning-text">Time is running out! Only 10 seconds remaining!</span>
                        </div>
                    </div>
                """,
                
                "css_styles": """
                    .timer-container {
                        position: fixed;
                        top: 20px;
                        right: 20px;
                        background: white;
                        padding: 15px;
                        border-radius: 10px;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                        z-index: 1000;
                        min-width: 200px;
                    }
                    
                    .timer-display {
                        font-size: 24px;
                        font-weight: bold;
                        text-align: center;
                        margin-bottom: 10px;
                    }
                    
                    .progress-bar {
                        width: 100%;
                        height: 8px;
                        background: #e0e0e0;
                        border-radius: 4px;
                        overflow: hidden;
                    }
                    
                    .progress-fill {
                        height: 100%;
                        background: linear-gradient(90deg, #28A745, #FFC107, #DC3545);
                        transition: width 1s linear;
                    }
                    
                    .warning-message {
                        background: #FFF3CD;
                        border: 2px solid #FFC107;
                        border-radius: 5px;
                        padding: 10px;
                        margin-top: 10px;
                        animation: pulse 1s infinite;
                    }
                    
                    .warning-icon {
                        font-size: 20px;
                        margin-right: 10px;
                    }
                    
                    .warning-text {
                        font-weight: bold;
                        color: #856404;
                    }
                    
                    @keyframes pulse {
                        0% { transform: scale(1); }
                        50% { transform: scale(1.05); }
                        100% { transform: scale(1); }
                    }
                    
                    .time-plenty { color: #28A745; }
                    .time-moderate { color: #FFC107; }
                    .time-low { color: #DC3545; }
                    .time-warning { color: #FF6B6B; animation: blink 0.5s infinite; }
                    
                    @keyframes blink {
                        0%, 50% { opacity: 1; }
                        25%, 75% { opacity: 0.5; }
                    }
                """,
                
                "javascript_logic": """
                    class EnhancedTimer {
                        constructor(totalSeconds, warningCallback) {
                            this.totalSeconds = totalSeconds;
                            this.remainingSeconds = totalSeconds;
                            this.warningCallback = warningCallback;
                            this.warningShown = false;
                            this.intervalId = null;
                        }
                        
                        start() {
                            this.intervalId = setInterval(() => this.update(), 1000);
                        }
                        
                        update() {
                            this.remainingSeconds--;
                            this.updateDisplay();
                            
                            if (this.remainingSeconds === 10 && !this.warningShown) {
                                this.showWarning();
                                this.warningShown = true;
                                this.playWarningSound();
                                this.vibrate();
                            }
                            
                            if (this.remainingSeconds <= 0) {
                                this.stop();
                                this.warningCallback();
                            }
                        }
                        
                        updateDisplay() {
                            const timerElement = document.getElementById('timer');
                            const progressElement = document.getElementById('progress');
                            
                            if (timerElement) {
                                timerElement.textContent = this.remainingSeconds;
                                
                                // Update color based on time remaining
                                timerElement.className = 'time-remaining';
                                const percentage = this.remainingSeconds / this.totalSeconds;
                                
                                if (percentage > 0.5) {
                                    timerElement.classList.add('time-plenty');
                                } else if (percentage > 0.25) {
                                    timerElement.classList.add('time-moderate');
                                } else if (percentage > 0.15) {
                                    timerElement.classList.add('time-low');
                                } else {
                                    timerElement.classList.add('time-warning');
                                }
                            }
                            
                            if (progressElement) {
                                const percentage = (this.totalSeconds - this.remainingSeconds) / this.totalSeconds * 100;
                                progressElement.style.width = percentage + '%';
                            }
                        }
                        
                        showWarning() {
                            const warningElement = document.getElementById('warning');
                            if (warningElement) {
                                warningElement.style.display = 'block';
                                warningElement.style.animation = 'pulse 1s infinite';
                            }
                        }
                        
                        playWarningSound() {
                            // Play warning sound if enabled
                            if (this.soundEnabled) {
                                const audio = new Audio('warning.mp3');
                                audio.play().catch(e => console.log('Could not play sound'));
                            }
                        }
                        
                        vibrate() {
                            // Vibrate if enabled
                            if (this.vibrationEnabled && navigator.vibrate) {
                                navigator.vibrate([200, 100, 200]);
                            }
                        }
                        
                        stop() {
                            if (this.intervalId) {
                                clearInterval(this.intervalId);
                                this.intervalId = null;
                            }
                        }
                    }
                    
                    // Usage in question component:
                    const timer = new EnhancedTimer(90, () => {
                        // Time's up - submit answer or move to next question
                        submitAnswer();
                    });
                    timer.start();
                """
            }
        },
        
        "mobile_optimizations": {
            "touch_feedback": {
                "haptic_feedback": True,
                "vibration_patterns": {
                    "warning": [200, 100, 200],
                    "correct_answer": [50],
                    "wrong_answer": [100, 50]
                }
            },
            "responsive_design": {
                "mobile_timer": {
                    "position": "top",
                    "size": "compact",
                    "always_visible": True
                },
                "tablet_timer": {
                    "position": "top-right",
                    "size": "medium",
                    "auto_hide": False
                }
            },
            "battery_optimization": {
                "reduced_animations": True,
                "simplified_warnings": True,
                "optimized_colors": True
            }
        }
    }
    
    return platform

def save_enhanced_platform():
    """Save the enhanced platform with extended timers"""
    platform = create_enhanced_timer_platform()
    
    with open('enhanced_timer_platform.json', 'w', encoding='utf-8') as f:
        json.dump(platform, f, indent=2, ensure_ascii=False)
    
    print("Enhanced Timer Platform saved to 'enhanced_timer_platform.json'")
    
    print(f"\n🎯 Enhanced Timer Features:")
    print(f"  ✅ Extended timers for Classes 10-12")
    print(f"  ✅ 10-second warning system")
    print(f"  ✅ Visual and audio warnings")
    print(f"  ✅ Progress bars with color coding")
    print(f"  ✅ Mobile haptic feedback")
    print(f"  ✅ Responsive design")
    
    print(f"\n⏰ Timer Configuration:")
    print(f"  Class 10: Easy (60s), Medium (90s), Hard (150s)")
    print(f"  Class 11: Easy (90s), Medium (135s), Hard (210s)")
    print(f"  Class 12: Easy (120s), Medium (180s), Hard (300s)")
    
    print(f"\n⚠️ Warning System:")
    print(f"  - Activates at 10 seconds remaining")
    print(f"  - Multiple warning messages")
    print(f"  - Visual pulse animation")
    print(f"  - Audio notification")
    print(f"  - Haptic vibration")
    
    print(f"\n📱 Mobile Features:")
    print(f"  - Touch feedback")
    print(f"  - Vibration patterns")
    print(f"  - Responsive design")
    print(f"  - Battery optimization")

if __name__ == "__main__":
    save_enhanced_platform()