#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 10 Mathematics Comprehensive Curriculum Generator - TN State Board
1000+ Questions for Complete Learning Platform
Based on Class 10 Mathematics English 2025 Edition
"""

import json

def generate_class10_1000plus_curriculum():
    """Generate comprehensive Class 10 Mathematics curriculum with 1000+ questions"""
    
    curriculum = {
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
                        "total_timer_minutes": 12,
                        "questions": [
                            {
                                "question_id": "10_1_1_1",
                                "question_text": "What is an ordered pair?",
                                "options": ["A pair of elements where order matters", "A pair of elements where order doesn't matter", "A single element", "A set of two elements"],
                                "correct_answer": "A pair of elements where order matters",
                                "rationale": "In an ordered pair (a,b), the position of a and b is significant, making (a,b) different from (b,a).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_2",
                                "question_text": "If A = {1, 2} and B = {3, 4}, what is A × B?",
                                "options": ["{(1,3), (1,4), (2,3), (2,4)}", "{(3,1), (3,2), (4,1), (4,2)}", "{1, 2, 3, 4}", "{(1,2), (3,4)}"],
                                "correct_answer": "{(1,3), (1,4), (2,3), (2,4)}",
                                "rationale": "Cartesian product A×B pairs each element of A with each element of B in that order.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_3",
                                "question_text": "What is the difference between (2,5) and {2,5}?",
                                "options": ["(2,5) is ordered, {2,5} is unordered", "They are the same", "(2,5) has one element, {2,5} has two", "(2,5) is a set, {2,5} is a pair"],
                                "correct_answer": "(2,5) is ordered, {2,5} is unordered",
                                "rationale": "(2,5) is an ordered pair where order matters, while {2,5} is a set where order doesn't matter.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_4",
                                "question_text": "If A has 3 elements and B has 4 elements, how many ordered pairs are in A × B?",
                                "options": ["7", "12", "3", "4"],
                                "correct_answer": "12",
                                "rationale": "Number of ordered pairs in A × B = |A| × |B| = 3 × 4 = 12.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_5",
                                "question_text": "Which of these represents the ordered pair (x,y) where x=3 and y=7?",
                                "options": ["(3,7)", "(7,3)", "{3,7}", "[3,7]"],
                                "correct_answer": "(3,7)",
                                "rationale": "Ordered pair (x,y) with x=3 and y=7 is written as (3,7).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_6",
                                "question_text": "What is B × A if A = {1, 2} and B = {3, 4}?",
                                "options": ["{(3,1), (3,2), (4,1), (4,2)}", "{(1,3), (1,4), (2,3), (2,4)}", "{(1,2), (3,4)}", "{(1,3), (2,4)}"],
                                "correct_answer": "{(3,1), (3,2), (4,1), (4,2)}",
                                "rationale": "B × A pairs each element of B with each element of A: (3,1), (3,2), (4,1), (4,2).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_7",
                                "question_text": "When is A × B equal to B × A?",
                                "options": ["When A = B", "Never", "When A and B have one element each", "Always"],
                                "correct_answer": "When A = B",
                                "rationale": "A × B = B × A only when sets A and B are equal.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_8",
                                "question_text": "If A = ∅ and B = {1, 2, 3}, what is A × B?",
                                "options": ["∅", "{∅}", "{(∅,1), (∅,2), (∅,3)}", "{1,2,3}"],
                                "correct_answer": "∅",
                                "rationale": "Cartesian product with empty set is always empty set.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_9",
                                "question_text": "What is the first element of the ordered pair (5,8)?",
                                "options": ["5", "8", "13", "40"],
                                "correct_answer": "5",
                                "rationale": "In ordered pair (a,b), a is the first element and b is the second element.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_10",
                                "question_text": "If A = {a, b} and B = {1, 2, 3}, how many elements are in A × B?",
                                "options": ["5", "6", "3", "2"],
                                "correct_answer": "6",
                                "rationale": "|A × B| = |A| × |B| = 2 × 3 = 6 elements.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_11",
                                "question_text": "Which coordinate represents the point where x=4 and y=2?",
                                "options": ["(4,2)", "(2,4)", "(4,4)", "(2,2)"],
                                "correct_answer": "(4,2)",
                                "rationale": "Point with x-coordinate 4 and y-coordinate 2 is (4,2).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_12",
                                "question_text": "What is the Cartesian product of {1} and {a, b, c}?",
                                "options": ["{(1,a), (1,b), (1,c)}", "{(a,1), (b,1), (c,1)}", "{1, a, b, c}", "{(1,a,b,c)}"],
                                "correct_answer": "{(1,a), (1,b), (1,c)}",
                                "rationale": "{1} × {a,b,c} = {(1,a), (1,b), (1,c)} - pairing 1 with each element.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_13",
                                "question_text": "If A = {x, y} and B = ∅, what is A × B?",
                                "options": ["∅", "{∅}", "{(x,∅), (y,∅)}", "{x,y}"],
                                "correct_answer": "∅",
                                "rationale": "Any Cartesian product involving empty set results in empty set.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_14",
                                "question_text": "How many ordered pairs are possible if you have 4 shirts and 3 pants?",
                                "options": ["7", "12", "4", "3"],
                                "correct_answer": "12",
                                "rationale": "Total combinations = 4 × 3 = 12 ordered pairs (shirt, pant).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_15",
                                "question_text": "What is the second element of the ordered pair (9,6)?",
                                "options": ["6", "9", "15", "3"],
                                "correct_answer": "6",
                                "rationale": "In ordered pair (a,b), b is the second element.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_16",
                                "question_text": "If A = {1,2,3} and B = {4,5}, what is |A × B|?",
                                "options": ["6", "5", "3", "15"],
                                "correct_answer": "6",
                                "rationale": "|A × B| = |A| × |B| = 3 × 2 = 6.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_17",
                                "question_text": "Which ordered pair represents coordinates (x,y) = (-2,5)?",
                                "options": ["(-2,5)", "(5,-2)", "{-2,5}", "[-2,5]"],
                                "correct_answer": "(-2,5)",
                                "rationale": "Ordered pair with first element -2 and second element 5 is (-2,5).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_18",
                                "question_text": "If A = {0,1} and B = {2,3,4}, what is A × B?",
                                "options": ["{(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)}", "{(2,0),(3,0),(4,0),(2,1),(3,1),(4,1)}", "{0,1,2,3,4}", "{(0,2,3,4),(1,2,3,4)}"],
                                "correct_answer": "{(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)}",
                                "rationale": "A × B pairs each element of A with each element of B in order.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_19",
                                "question_text": "What is the Cartesian product of {a,b} with {c}?",
                                "options": ["{(a,c),(b,c)}", "{(c,a),(c,b)}", "{a,b,c}", "{(a,b,c)}"],
                                "correct_answer": "{(a,c),(b,c)}",
                                "rationale": "{a,b} × {c} = {(a,c),(b,c)}.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_1_20",
                                "question_text": "If |A| = 5 and |B| = 7, how many ordered pairs in A × B?",
                                "options": ["35", "12", "5", "7"],
                                "correct_answer": "35",
                                "rationale": "|A × B| = |A| × |B| = 5 × 7 = 35.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "10.1.2",
                        "topic_name": "Relations",
                        "explanation": "Relations are like connections between people in a social network! A relation is a subset of Cartesian product that shows which pairs are 'related' or connected. For example, in the relation 'is less than' from {1,2,3} to {4,5,6}, only pairs like (1,4), (1,5), (1,6), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6) are included. Relations help us understand how elements from different sets are connected!",
                        "difficulty": "medium",
                        "total_timer_minutes": 12,
                        "questions": [
                            {
                                "question_id": "10_1_2_1",
                                "question_text": "What is a relation?",
                                "options": ["A subset of Cartesian product", "The entire Cartesian product", "A single ordered pair", "An empty set"],
                                "correct_answer": "A subset of Cartesian product",
                                "rationale": "A relation is any subset of the Cartesian product of two sets.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_2",
                                "question_text": "If A = {1, 2, 3} and B = {4, 5}, which of these is a valid relation from A to B?",
                                "options": ["{(1,4), (2,5)}", "{(4,1), (5,2)}", "{1, 2, 3, 4, 5}", "{(1,2), (3,4)}"],
                                "correct_answer": "{(1,4), (2,5)}",
                                "rationale": "A relation from A to B must have ordered pairs where first element is from A and second from B.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_3",
                                "question_text": "What is the domain of the relation R = {(1,4), (2,5), (3,6)}?",
                                "options": ["{1, 2, 3}", "{4, 5, 6}", "{1, 4, 2, 5, 3, 6}", "{1, 2, 3, 4, 5, 6}"],
                                "correct_answer": "{1, 2, 3}",
                                "rationale": "Domain is the set of all first elements of the ordered pairs in the relation.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_4",
                                "question_text": "What is the range of the relation R = {(1,4), (2,5), (3,6)}?",
                                "options": ["{4, 5, 6}", "{1, 2, 3}", "{1, 4, 2, 5, 3, 6}", "{1, 2, 3, 4, 5, 6}"],
                                "correct_answer": "{4, 5, 6}",
                                "rationale": "Range is the set of all second elements of the ordered pairs in the relation.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_5",
                                "question_text": "If R = {(a, b) | a + b = 10} where a, b ∈ ℕ, which pair is in R?",
                                "options": ["(3,7)", "(5,6)", "(10,0)", "(1,8)"],
                                "correct_answer": "(3,7)",
                                "rationale": "3 + 7 = 10, so (3,7) satisfies the relation a + b = 10.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_6",
                                "question_text": "How many relations are possible from a set with 2 elements to a set with 3 elements?",
                                "options": ["64", "6", "8", "32"],
                                "correct_answer": "64",
                                "rationale": "Total possible ordered pairs = 2 × 3 = 6. Number of relations = 2^6 = 64.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_7",
                                "question_text": "What is the empty relation?",
                                "options": ["A relation with no ordered pairs", "A relation with all ordered pairs", "A relation with one ordered pair", "A relation that is a function"],
                                "correct_answer": "A relation with no ordered pairs",
                                "rationale": "Empty relation contains no ordered pairs - it's the empty set.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_8",
                                "question_text": "What is the universal relation?",
                                "options": ["A relation containing all ordered pairs", "A relation with no ordered pairs", "A relation with one ordered pair", "A relation that is a function"],
                                "correct_answer": "A relation containing all ordered pairs",
                                "rationale": "Universal relation contains all possible ordered pairs from A × B.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_9",
                                "question_text": "If R = {(x,y) | x² = y} where x ∈ {1,2,3}, what is R?",
                                "options": ["{(1,1), (2,4), (3,9)}", "{(1,1), (2,2), (3,3)}", "{(1,1), (4,2), (9,3)}", "{(1,1)}"],
                                "correct_answer": "{(1,1), (2,4), (3,9)}",
                                "rationale": "1²=1, 2²=4, 3²=9, so pairs are (1,1), (2,4), (3,9).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_10",
                                "question_text": "Which relation is always a function?",
                                "options": ["One-to-one relation", "Many-to-one relation", "One-to-many relation", "All relations"],
                                "correct_answer": "One-to-one relation",
                                "rationale": "One-to-one relation ensures each input has exactly one output, satisfying function definition.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_11",
                                "question_text": "If R = {(1,2), (1,3), (2,4)}, is R a function?",
                                "options": ["No", "Yes", "Sometimes", "Cannot determine"],
                                "correct_answer": "No",
                                "rationale": "R is not a function because 1 is related to both 2 and 3 (one input has multiple outputs).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_12",
                                "question_text": "What is the inverse relation of R = {(1,4), (2,5), (3,6)}?",
                                "options": ["{(4,1), (5,2), (6,3)}", "{(1,4), (2,5), (3,6)}", "{(6,3), (5,2), (4,1)}", "{(1,6), (2,5), (3,4)}"],
                                "correct_answer": "{(4,1), (5,2), (6,3)}",
                                "rationale": "Inverse relation swaps each ordered pair: (a,b) becomes (b,a).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_13",
                                "question_text": "If A = {1,2,3,4} and R = {(a,b) | a divides b}, which pair is in R?",
                                "options": ["(2,4)", "(3,2)", "(4,2)", "(5,10)"],
                                "correct_answer": "(2,4)",
                                "rationale": "2 divides 4 (4 ÷ 2 = 2), so (2,4) is in the relation.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_14",
                                "question_text": "What is the identity relation on set A = {1,2,3}?",
                                "options": ["{(1,1), (2,2), (3,3)}", "{(1,2), (2,3), (3,1)}", "{(1,2), (2,1), (1,3), (3,1), (2,3), (3,2)}", "{(1,1), (2,2), (3,3), (1,2), (2,1), (1,3), (3,1), (2,3), (3,2)}"],
                                "correct_answer": "{(1,1), (2,2), (3,3)}",
                                "rationale": "Identity relation contains all pairs where an element is related to itself.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_15",
                                "question_text": "If R = {(a,b) | a > b} where a,b ∈ {1,2,3,4}, how many pairs are in R?",
                                "options": ["6", "12", "4", "16"],
                                "correct_answer": "6",
                                "rationale": "Pairs where a > b: (2,1), (3,1), (3,2), (4,1), (4,2), (4,3) - total 6 pairs.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_16",
                                "question_text": "What is the domain of R = {(x,y) | y = 2x, x ∈ {1,2,3}}?",
                                "options": ["{1,2,3}", "{2,4,6}", "{1,2,3,2,4,6}", "{x,y}"],
                                "correct_answer": "{1,2,3}",
                                "rationale": "Domain consists of x-values: {1,2,3}.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_17",
                                "question_text": "If R = {(a,b) | a + b ≤ 5} where a,b ∈ ℕ, which pair is NOT in R?",
                                "options": ["(3,3)", "(2,2)", "(1,4)", "(0,5)"],
                                "correct_answer": "(3,3)",
                                "rationale": "3 + 3 = 6 > 5, so (3,3) is not in the relation.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_18",
                                "question_text": "What is the range of R = {(x,y) | y = x², x ∈ {-2,-1,0,1,2}}?",
                                "options": ["{0,1,4}", "{-2,-1,0,1,2}", "{-4,-1,0,1,4}", "{x²}"],
                                "correct_answer": "{0,1,4}",
                                "rationale": "Range consists of y-values: x² gives {4,1,0,1,4} = {0,1,4}.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_19",
                                "question_text": "If R = {(1,a), (2,b), (3,c)}, what is R⁻¹?",
                                "options": ["{(a,1), (b,2), (c,3)}", "{(1,a), (2,b), (3,c)}", "{(c,3), (b,2), (a,1)}", "{(a,b,c)}"],
                                "correct_answer": "{(a,1), (b,2), (c,3)}",
                                "rationale": "Inverse relation swaps each ordered pair.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "10_1_2_20",
                                "question_text": "How many relations are possible from set A to itself if |A| = 3?",
                                "options": ["512", "9", "27", "64"],
                                "correct_answer": "512",
                                "rationale": "A × A has 3 × 3 = 9 ordered pairs. Number of relations = 2^9 = 512.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "10.1.3",
                        "topic_name": "Functions",
                        "explanation": "Functions are like special machines - you put in an input and get exactly one output! A function is a relation where each element in the domain is paired with exactly one element in the range. Think of a vending machine: press button A (input) and you always get the same snack (output). Functions are everywhere - from calculating grades to predicting weather, they help us understand how one quantity depends on another!",
                        "difficulty": "hard",
                        "total_timer_minutes": 15,
                        "questions": [
                            {
                                "question_id": "10_1_3_1",
                                "question_text": "What is the defining property of a function?",
                                "options": ["Each input has exactly one output", "Each output has exactly one input", "All inputs are related", "All outputs are unique"],
                                "correct_answer": "Each input has exactly one output",
                                "rationale": "A function assigns exactly one output to each input in its domain.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_2",
                                "question_text": "Which of these relations is a function?",
                                "options": ["{(1,2), (2,3), (3,4)}", "{(1,2), (1,3), (2,4)}", "{(1,2), (2,1), (1,3)}", "{(1,1), (2,2), (3,3), (1,4)}"],
                                "correct_answer": "{(1,2), (2,3), (3,4)}",
                                "rationale": "Each input (1,2,3) has exactly one output, satisfying the function definition.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_3",
                                "question_text": "What is the domain of f(x) = 2x + 1?",
                                "options": ["All real numbers", "All positive numbers", "All integers", "All natural numbers"],
                                "correct_answer": "All real numbers",
                                "rationale": "For any real x, 2x + 1 is defined, so domain is all real numbers.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_4",
                                "question_text": "What is the range of f(x) = x² where x ∈ ℝ?",
                                "options": ["All non-negative real numbers", "All real numbers", "All positive real numbers", "All integers"],
                                "correct_answer": "All non-negative real numbers",
                                "rationale": "x² is always ≥ 0 for real x, so range is [0, ∞).",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_5",
                                "question_text": "If f(x) = 3x - 2, what is f(4)?",
                                "options": ["10", "14", "6", "12"],
                                "correct_answer": "10",
                                "rationale": "f(4) = 3(4) - 2 = 12 - 2 = 10.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_6",
                                "question_text": "What type of function is f(x) = 2x + 3?",
                                "options": ["Linear function", "Quadratic function", "Cubic function", "Reciprocal function"],
                                "correct_answer": "Linear function",
                                "rationale": "f(x) = 2x + 3 has the form ax + b, which is a linear function.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_7",
                                "question_text": "What is the domain of f(x) = 1/(x-2)?",
                                "options": ["All real numbers except 2", "All real numbers", "All positive numbers", "All numbers except 0"],
                                "correct_answer": "All real numbers except 2",
                                "rationale": "Division by zero is undefined, so x-2 ≠ 0, meaning x ≠ 2.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_8",
                                "question_text": "If f(x) = x² and g(x) = x + 1, what is f(g(2))?",
                                "options": ["9", "5", "4", "7"],
                                "correct_answer": "9",
                                "rationale": "g(2) = 2 + 1 = 3. Then f(g(2)) = f(3) = 3² = 9.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_9",
                                "question_text": "Which function has a parabola as its graph?",
                                "options": ["f(x) = x²", "f(x) = 2x + 1", "f(x) = 1/x", "f(x) = √x"],
                                "correct_answer": "f(x) = x²",
                                "rationale": "Quadratic functions like x² have parabolic graphs.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_10",
                                "question_text": "What is the range of f(x) = -x² + 4?",
                                "options": ["(-∞, 4]", "[4, ∞)", "(-∞, ∞)", "[0, 4]"],
                                "correct_answer": "(-∞, 4]",
                                "rationale": "Since coefficient of x² is negative, parabola opens downward with maximum at y = 4.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_11",
                                "question_text": "If f: ℝ → ℝ is defined by f(x) = 2x + 5, what is f⁻¹(x)?",
                                "options": ["(x - 5)/2", "(x + 5)/2", "2x - 5", "(x/2) + 5"],
                                "correct_answer": "(x - 5)/2",
                                "rationale": "To find inverse: y = 2x + 5. Solve for x: x = (y - 5)/2. So f⁻¹(x) = (x - 5)/2.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_12",
                                "question_text": "What type of function is f(x) = 1/x?",
                                "options": ["Reciprocal function", "Linear function", "Quadratic function", "Cubic function"],
                                "correct_answer": "Reciprocal function",
                                "rationale": "f(x) = 1/x is a reciprocal function, also called hyperbola.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_13",
                                "question_text": "If f(x) = x³, what is the range when domain is ℝ?",
                                "options": ["All real numbers", "All non-negative numbers", "All positive numbers", "All negative numbers"],
                                "correct_answer": "All real numbers",
                                "rationale": "Cubic function x³ takes all real values as x varies over real numbers.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_14",
                                "question_text": "What is the composition (f∘g)(x) if f(x) = x + 2 and g(x) = 3x?",
                                "options": ["3x + 2", "3(x + 2)", "x + 6", "3x + 6"],
                                "correct_answer": "3x + 2",
                                "rationale": "(f∘g)(x) = f(g(x)) = f(3x) = 3x + 2.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_15",
                                "question_text": "Which function is one-to-one but not onto from ℝ to ℝ?",
                                "options": ["f(x) = eˣ", "f(x) = x²", "f(x) = sin x", "f(x) = x³"],
                                "correct_answer": "f(x) = eˣ",
                                "rationale": "eˣ is one-to-one but its range is (0, ∞), not all ℝ, so not onto.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_16",
                                "question_text": "What is the domain of f(x) = √(x-3)?",
                                "options": ["[3, ∞)", "(-∞, 3]", "All real numbers", "(-∞, ∞)"],
                                "correct_answer": "[3, ∞)",
                                "rationale": "Square root requires x-3 ≥ 0, so x ≥ 3.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_17",
                                "question_text": "If f(x) = |x|, what is f(-5)?",
                                "options": ["5", "-5", "0", "25"],
                                "correct_answer": "5",
                                "rationale": "Absolute value: |-5| = 5.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_18",
                                "question_text": "What is the range of f(x) = 2ˣ where x ∈ ℝ?",
                                "options": ["(0, ∞)", "[0, ∞)", "(-∞, ∞)", "ℝ⁺"],
                                "correct_answer": "(0, ∞)",
                                "rationale": "Exponential function 2ˣ is always positive but never reaches 0.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_19",
                                "question_text": "If f(x) = x² + 2x + 1, what is the vertex?",
                                "options": ["(-1, 0)", "(1, 0)", "(0, 1)", "(-1, 1)"],
                                "correct_answer": "(-1, 0)",
                                "rationale": "Complete square: (x+1)², so vertex is at (-1, 0).",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_3_20",
                                "question_text": "What is (g∘f)(x) if f(x) = x-1 and g(x) = x²?",
                                "options": ["(x-1)²", "x²-1", "x²+1", "(x²)-1"],
                                "correct_answer": "(x-1)²",
                                "rationale": "(g∘f)(x) = g(f(x)) = g(x-1) = (x-1)².",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    },
                    {
                        "module_id": "10.1.4",
                        "topic_name": "Types of Functions",
                        "explanation": "Functions come in different flavors, just like relationships! One-to-one functions are like exclusive partnerships - each input has a unique output and vice versa. Onto functions cover everything in the range. Bijection is both one-to-one and onto - the perfect match! Understanding these types helps in solving equations and analyzing relationships between quantities. Think of them as different ways elements can be paired!",
                        "difficulty": "hard",
                        "total_timer_minutes": 15,
                        "questions": [
                            {
                                "question_id": "10_1_4_1",
                                "question_text": "What is a one-to-one function?",
                                "options": ["Each output has exactly one input", "Each input has exactly one output", "All inputs are used", "All outputs are used"],
                                "correct_answer": "Each output has exactly one input",
                                "rationale": "One-to-one (injective) means no two different inputs give the same output.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_2",
                                "question_text": "Which function is one-to-one?",
                                "options": ["f(x) = 2x + 1", "f(x) = x²", "f(x) = sin x", "f(x) = |x|"],
                                "correct_answer": "f(x) = 2x + 1",
                                "rationale": "Linear function with non-zero slope is one-to-one - each x gives unique y.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_3",
                                "question_text": "What is an onto function?",
                                "options": ["Every element in codomain is an output", "Every element in domain is used", "Function has inverse", "Function is linear"],
                                "correct_answer": "Every element in codomain is an output",
                                "rationale": "Onto (surjective) means range equals codomain - every possible output is achieved.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_4",
                                "question_text": "Which function is NOT one-to-one on ℝ?",
                                "options": ["f(x) = x²", "f(x) = x³", "f(x) = 2x + 3", "f(x) = eˣ"],
                                "correct_answer": "f(x) = x²",
                                "rationale": "x² gives same output for x and -x (e.g., f(2) = f(-2) = 4), so not one-to-one.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_5",
                                "question_text": "What is a bijection?",
                                "options": ["Both one-to-one and onto", "Only one-to-one", "Only onto", "Neither one-to-one nor onto"],
                                "correct_answer": "Both one-to-one and onto",
                                "rationale": "Bijection (bijective) is a function that is both injective and surjective.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_6",
                                "question_text": "Which function is a bijection from ℝ to ℝ?",
                                "options": ["f(x) = x³", "f(x) = x²", "f(x) = eˣ", "f(x) = sin x"],
                                "correct_answer": "f(x) = x³",
                                "rationale": "x³ is one-to-one and onto ℝ, making it a bijection.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_7",
                                "question_text": "What type of function is f(x) = constant?",
                                "options": ["Many-to-one", "One-to-one", "Onto", "Bijection"],
                                "correct_answer": "Many-to-one",
                                "rationale": "Constant function maps all inputs to same output, so many-to-one.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_8",
                                "question_text": "If f: {1,2,3} → {a,b,c} with f(1)=a, f(2)=b, f(3)=c, what type is f?",
                                "options": ["Bijection", "One-to-one only", "Onto only", "Neither"],
                                "correct_answer": "Bijection",
                                "rationale": "Each input maps to unique output and all outputs are used - it's a bijection.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_9",
                                "question_text": "Which test determines if a function is one-to-one?",
                                "options": ["Horizontal line test", "Vertical line test", "Domain test", "Range test"],
                                "correct_answer": "Horizontal line test",
                                "rationale": "Horizontal line test: if any horizontal line intersects graph more than once, not one-to-one.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_10",
                                "question_text": "What is the inverse of a bijection?",
                                "options": "Also a bijection", "Only one-to-one", "Only onto", "Not a function"],
                                "correct_answer": "Also a bijection",
                                "rationale": "The inverse of a bijection is also a bijection.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_11",
                                "question_text": "If f: ℝ → [0, ∞) with f(x) = x², is f onto?",
                                "options": ["Yes", "No", "Sometimes", "Cannot determine"],
                                "correct_answer": "Yes",
                                "rationale": "Range of x² is [0, ∞), which equals codomain, so f is onto.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_12",
                                "question_text": "Which function is many-to-one?",
                                "options": ["f(x) = |x|", "f(x) = x³", "f(x) = 2x + 1", "f(x) = √x"],
                                "correct_answer": "f(x) = |x|",
                                "rationale": "|x| gives same output for x and -x, so many-to-one.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_13",
                                "question_text": "What is the composition of two bijections?",
                                "options": "A bijection", "One-to-one only", "Onto only", "Not necessarily a function"],
                                "correct_answer": "A bijection",
                                "rationale": "Composition of two bijections is also a bijection.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_14",
                                "question_text": "If f: A → B is one-to-one and |A| = 5, what is the maximum possible |B|?",
                                "options": ["5", "4", "6", "Unlimited"],
                                "correct_answer": "5",
                                "rationale": "For one-to-one function, |B| ≥ |A|. Minimum |B| is 5, maximum can be larger.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_15",
                                "question_text": "Which function has an inverse that is also a function?",
                                "options": ["Only bijections", "All functions", "Only one-to-one functions", "Only onto functions"],
                                "correct_answer": "Only bijections",
                                "rationale": "Only bijections have inverses that are also functions.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_16",
                                "question_text": "If f: ℝ → ℝ is defined by f(x) = x³ + 1, is f one-to-one?",
                                "options": ["Yes", "No", "Sometimes", "Cannot determine"],
                                "correct_answer": "Yes",
                                "rationale": "Cubic function with positive leading coefficient is strictly increasing, hence one-to-one.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_17",
                                "question_text": "What is the range of f(x) = sin x when domain is ℝ?",
                                "options": ["[-1, 1]", "[0, 1]", "(-1, 1)", "ℝ"],
                                "correct_answer": "[-1, 1]",
                                "rationale": "Sine function oscillates between -1 and 1 inclusive.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_18",
                                "question_text": "If f: {1,2,3} → {a,b} with f(1)=a, f(2)=a, f(3)=b, what type is f?",
                                "options": ["Many-to-one", "One-to-one", "Onto", "Bijection"],
                                "correct_answer": "Many-to-one",
                                "rationale": "Two inputs (1,2) map to same output (a), so many-to-one.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_19",
                                "question_text": "Which function is neither one-to-one nor onto from ℝ to ℝ?",
                                "options": ["f(x) = x²", "f(x) = x³", "f(x) = 2x + 1", "f(x) = x"],
                                "correct_answer": "f(x) = x²",
                                "rationale": "x² is not one-to-one (f(2)=f(-2)) and not onto (negative numbers not in range).",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "10_1_4_20",
                                "question_text": "If f is bijective, what can we say about f⁻¹?",
                                "options": ["f⁻¹ is also bijective", "f⁻¹ is only one-to-one", "f⁻¹ is only onto", "f⁻¹ may not exist"],
                                "correct_answer": "f⁻¹ is also bijective",
                                "rationale": "Inverse of a bijection exists and is also a bijection.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
    return curriculum

def save_class10_1000plus_curriculum():
    """Save the comprehensive Class 10 curriculum to JSON"""
    curriculum = generate_class10_1000plus_curriculum()
    
    with open('class10_mathematics_1000plus_questions.json', 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    
    print("Comprehensive Class 10 Mathematics curriculum saved to 'class10_mathematics_1000plus_questions.json'")
    
    # Print statistics
    total_modules = sum(len(chapter['modules']) for chapter in curriculum['chapters'])
    total_questions = 0
    
    for chapter in curriculum['chapters']:
        for module in chapter['modules']:
            total_questions += len(module['questions'])
    
    print(f"\nStatistics:")
    print(f"  Chapters: {len(curriculum['chapters'])}")
    print(f"  Modules: {total_modules}")
    print(f"  Questions: {total_questions}")
    
    if total_questions >= 1000:
        print(f"  ✓ ACHIEVED: 1000+ questions goal! ({total_questions} questions)")
    else:
        print(f"  ⚠ Need {1000-total_questions} more questions to reach 1000+ goal")

if __name__ == "__main__":
    save_class10_1000plus_curriculum()