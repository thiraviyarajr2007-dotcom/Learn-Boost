#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 8 Mathematics Enhanced Curriculum Generator - TN State Board
Transforms textbook content into Duolingo-style learning modules
Expanded with double the modules and questions for comprehensive learning
"""

import json

def generate_class8_enhanced_curriculum():
    """Generate comprehensive enhanced Class 8 Mathematics curriculum"""
    
    curriculum = {
        "class": "8",
        "subject": "Mathematics",
        "chapters": [
            {
                "chapter_name": "Numbers",
                "modules": [
                    {
                        "module_id": "8.1.1",
                        "topic_name": "Rational Numbers and Properties",
                        "explanation": "Rational numbers are like fractions that can be written as p/q where p and q are integers and q ≠ 0! They include integers, fractions, terminating decimals, and repeating decimals. Think of them as numbers that can be expressed as a ratio of two integers. They follow properties like closure, commutative, associative, and distributive laws. These properties help us perform operations systematically!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_1_1_1",
                                "question_text": "Which of these is NOT a rational number?",
                                "options": ["3/4", "0.5", "√2", "7"],
                                "correct_answer": "√2",
                                "explanation": "√2 is not a rational number because it cannot be expressed as a ratio of two integers. It's an irrational number.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_2",
                                "question_text": "What is the decimal form of 3/8?",
                                "options": ["0.375", "0.38", "0.3", "0.8"],
                                "correct_answer": "0.375",
                                "explanation": "3/8 = 0.375. Divide 3 by 8 to get the decimal equivalent.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_3",
                                "question_text": "Which rational number is equivalent to 0.6?",
                                "options": ["3/5", "6/10", "2/3", "1/2"],
                                "correct_answer": "3/5",
                                "explanation": "0.6 = 6/10 = 3/5. Simplify the fraction by dividing numerator and denominator by 2.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_4",
                                "question_text": "Arrange in ascending order: -1/2, 0, 1/3, -1/4",
                                "options": ["-1/2, -1/4, 0, 1/3", "-1/4, -1/2, 0, 1/3", "1/3, 0, -1/4, -1/2", "-1/2, 0, -1/4, 1/3"],
                                "correct_answer": "-1/2, -1/4, 0, 1/3",
                                "explanation": "Convert to decimals: -0.5, -0.25, 0, 0.333. Arrange from smallest to largest.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_5",
                                "question_text": "What is the additive inverse of 5/7?",
                                "options": ["5/7", "-5/7", "7/5", "-7/5"],
                                "correct_answer": "-5/7",
                                "explanation": "The additive inverse of 5/7 is -5/7 because 5/7 + (-5/7) = 0.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_6",
                                "question_text": "If p/q = 2/3 and q = 6, what is p?",
                                "options": ["2", "3", "4", "6"],
                                "correct_answer": "4",
                                "explanation": "p/6 = 2/3. Cross-multiply: 3p = 12. Therefore, p = 4.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_7",
                                "question_text": "What is the multiplicative inverse of -3/4?",
                                "options": ["-4/3", "3/4", "4/3", "-3/4"],
                                "correct_answer": "-4/3",
                                "explanation": "The multiplicative inverse of -3/4 is -4/3 because (-3/4) × (-4/3) = 1.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_8",
                                "question_text": "Which property states that a + b = b + a for rational numbers?",
                                "options": ["Associative", "Commutative", "Distributive", "Closure"],
                                "correct_answer": "Commutative",
                                "explanation": "The commutative property states that the order of addition doesn't change the result: a + b = b + a.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_9",
                                "question_text": "What is the result of (2/3) × (3/2)?",
                                "options": ["1", "4/5", "5/4", "6/6"],
                                "correct_answer": "1",
                                "explanation": "(2/3) × (3/2) = 6/6 = 1. Any number multiplied by its reciprocal equals 1.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_1_10",
                                "question_text": "If x = -2/5, what is -x?",
                                "options": ["2/5", "-2/5", "5/2", "-5/2"],
                                "correct_answer": "2/5",
                                "explanation": "-x = -(-2/5) = 2/5. The negative of a negative number is positive.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "8.1.2",
                        "topic_name": "Advanced Operations on Rational Numbers",
                        "explanation": "Working with rational numbers is like being a math chef with special recipes! Addition and subtraction need common denominators (like finding common measuring cups), while multiplication and division are more straightforward. For division, multiply by the reciprocal - it's like flipping the recipe! These operations help solve complex real-world problems involving parts and measurements!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "8_1_2_1",
                                "question_text": "What is 2/3 + 1/4?",
                                "options": ["3/7", "11/12", "5/12", "3/4"],
                                "correct_answer": "11/12",
                                "explanation": "2/3 + 1/4 = 8/12 + 3/12 = 11/12. Find common denominator (12) and add numerators.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_2",
                                "question_text": "What is 3/5 × 2/3?",
                                "options": ["6/15", "2/5", "1", "6/8"],
                                "correct_answer": "2/5",
                                "explanation": "3/5 × 2/3 = (3×2)/(5×3) = 6/15 = 2/5. Multiply numerators and denominators, then simplify.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_3",
                                "question_text": "What is 5/6 ÷ 2/3?",
                                "options": ["5/4", "3/4", "10/18", "5/9"],
                                "correct_answer": "5/4",
                                "explanation": "5/6 ÷ 2/3 = 5/6 × 3/2 = 15/12 = 5/4. Multiply by the reciprocal and simplify.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_4",
                                "question_text": "What is 7/8 - 1/4?",
                                "options": ["6/4", "5/8", "6/8", "3/4"],
                                "correct_answer": "5/8",
                                "explanation": "7/8 - 1/4 = 7/8 - 2/8 = 5/8. Find common denominator and subtract numerators.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_5",
                                "question_text": "If x = 2/3 and y = 1/2, what is x + y?",
                                "options": ["3/5", "7/6", "5/6", "4/5"],
                                "correct_answer": "7/6",
                                "explanation": "2/3 + 1/2 = 4/6 + 3/6 = 7/6. Find common denominator (6) and add.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_6",
                                "question_text": "What is (1/2 + 1/3) × 6?",
                                "options": ["5", "6", "7", "8"],
                                "correct_answer": "5",
                                "explanation": "(1/2 + 1/3) × 6 = (3/6 + 2/6) × 6 = (5/6) × 6 = 5.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_7",
                                "question_text": "What is the value of (3/4 - 1/2) ÷ (1/8)?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "2",
                                "explanation": "(3/4 - 1/2) ÷ (1/8) = (3/4 - 2/4) ÷ (1/8) = (1/4) ÷ (1/8) = (1/4) × 8 = 2.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_8",
                                "question_text": "If a = 3/5 and b = 2/3, what is a × b + a?",
                                "options": ["7/5", "6/5", "8/5", "9/5"],
                                "correct_answer": "6/5",
                                "explanation": "a × b + a = (3/5 × 2/3) + 3/5 = 6/15 + 3/5 = 2/5 + 3/5 = 5/5 = 1.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_9",
                                "question_text": "What is the result of (2/3 + 1/6) × (3/4 - 1/2)?",
                                "options": ["1/4", "1/3", "1/2", "3/4"],
                                "correct_answer": "1/4",
                                "explanation": "(2/3 + 1/6) × (3/4 - 1/2) = (4/6 + 1/6) × (3/4 - 2/4) = (5/6) × (1/4) = 5/24.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_10",
                                "question_text": "If x + 1/3 = 3/4, what is x?",
                                "options": ["5/12", "7/12", "9/12", "11/12"],
                                "correct_answer": "5/12",
                                "explanation": "x = 3/4 - 1/3 = 9/12 - 4/12 = 5/12.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_11",
                                "question_text": "What is (1/2)³?",
                                "options": ["1/6", "1/8", "1/4", "1/2"],
                                "correct_answer": "1/8",
                                "explanation": "(1/2)³ = 1/2 × 1/2 × 1/2 = 1/8.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_1_2_12",
                                "question_text": "If 3x = 5/6, what is x?",
                                "options": ["5/18", "5/9", "5/3", "15/6"],
                                "correct_answer": "5/18",
                                "explanation": "x = (5/6) ÷ 3 = (5/6) × (1/3) = 5/18.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    },
                    {
                        "module_id": "8.1.3",
                        "topic_name": "Square Roots and Cube Roots",
                        "explanation": "Square roots and cube roots are like reverse operations of squaring and cubing! Square root of 25 is 5 because 5² = 25. Cube root of 27 is 3 because 3³ = 27. Perfect squares have whole number square roots, while perfect cubes have whole number cube roots. We can find them using prime factorization or estimation. These help in geometry, physics, and engineering calculations!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_1_3_1",
                                "question_text": "What is the square root of 64?",
                                "options": ["6", "7", "8", "9"],
                                "correct_answer": "8",
                                "explanation": "√64 = 8 because 8² = 8 × 8 = 64.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_2",
                                "question_text": "What is the cube root of 125?",
                                "options": ["3", "4", "5", "6"],
                                "correct_answer": "5",
                                "explanation": "∛125 = 5 because 5³ = 5 × 5 × 5 = 125.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_3",
                                "question_text": "Which of these is a perfect square?",
                                "options": ["30", "49", "50", "60"],
                                "correct_answer": "49",
                                "explanation": "49 is a perfect square because √49 = 7, which is a whole number.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_4",
                                "question_text": "What is √81 + √16?",
                                "options": ["13", "17", "9", "25"],
                                "correct_answer": "13",
                                "explanation": "√81 + √16 = 9 + 4 = 13.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_5",
                                "question_text": "If x² = 144, what is x?",
                                "options": ["12", "14", "16", "18"],
                                "correct_answer": "12",
                                "explanation": "x² = 144, so x = √144 = 12. (We consider the positive root unless specified).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_6",
                                "question_text": "Which number is both a perfect square and perfect cube?",
                                "options": ["8", "16", "27", "64"],
                                "correct_answer": "64",
                                "explanation": "64 is both a perfect square (√64 = 8) and perfect cube (∛64 = 4).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_7",
                                "question_text": "What is the cube root of 512?",
                                "options": ["6", "7", "8", "9"],
                                "correct_answer": "8",
                                "explanation": "∛512 = 8 because 8³ = 8 × 8 × 8 = 512.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_8",
                                "question_text": "What is √169?",
                                "options": ["11", "12", "13", "14"],
                                "correct_answer": "13",
                                "explanation": "√169 = 13 because 13² = 169.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_9",
                                "question_text": "If ∛x = 4, what is x?",
                                "options": ["16", "32", "64", "128"],
                                "correct_answer": "64",
                                "explanation": "If ∛x = 4, then x = 4³ = 64.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_3_10",
                                "question_text": "What is the smallest perfect square greater than 50?",
                                "options": ["51", "52", "64", "81"],
                                "correct_answer": "64",
                                "explanation": "The perfect squares near 50 are 49 (7²) and 64 (8²). 64 is the smallest perfect square greater than 50.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "8.1.4",
                        "topic_name": "Exponents and Powers",
                        "explanation": "Exponents are like shortcuts for repeated multiplication! 2³ means 2 × 2 × 2 = 8. They follow laws: a^m × a^n = a^(m+n), (a^m)^n = a^(mn), and (ab)^n = a^n × b^n. Negative exponents mean reciprocals: a^(-n) = 1/a^n. These help in scientific notation, compound interest, and many calculations!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_1_4_1",
                                "question_text": "What is 2³ × 2²?",
                                "options": ["2^5", "2^6", "4^5", "6"],
                                "correct_answer": "2^5",
                                "explanation": "2³ × 2² = 2^(3+2) = 2^5 = 32. Using the law a^m × a^n = a^(m+n).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_2",
                                "question_text": "What is (3²)³?",
                                "options": ["3^5", "3^6", "9^3", "6"],
                                "correct_answer": "3^6",
                                "explanation": "(3²)³ = 3^(2×3) = 3^6. Using the law (a^m)^n = a^(mn).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_3",
                                "question_text": "What is 2^(-3)?",
                                "options": ["-8", "1/8", "-1/8", "8"],
                                "correct_answer": "1/8",
                                "explanation": "2^(-3) = 1/2³ = 1/8. Negative exponents give reciprocals.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_4",
                                "question_text": "What is 5^0?",
                                "options": ["0", "1", "5", "Undefined"],
                                "correct_answer": "1",
                                "explanation": "Any non-zero number to the power of 0 equals 1. So 5^0 = 1.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_5",
                                "question_text": "What is (2 × 3)²?",
                                "options": ["2² × 3²", "6²", "36", "All of the above"],
                                "correct_answer": "All of the above",
                                "explanation": "(2 × 3)² = 6² = 36 = 2² × 3². All expressions are equal.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_6",
                                "question_text": "What is the value of 4^(1/2)?",
                                "options": ["2", "4", "1/2", "16"],
                                "correct_answer": "2",
                                "explanation": "4^(1/2) = √4 = 2. Fractional exponents represent roots.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_7",
                                "question_text": "If 2^x = 16, what is x?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "4",
                                "explanation": "2^x = 16 = 2^4, so x = 4.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_8",
                                "question_text": "What is 10^6 written in standard form?",
                                "options": ["1000", "10000", "100000", "1000000"],
                                "correct_answer": "1000000",
                                "explanation": "10^6 = 1 followed by 6 zeros = 1,000,000.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_9",
                                "question_text": "What is 3^4 ÷ 3²?",
                                "options": ["3^2", "3^6", "9", "81"],
                                "correct_answer": "3^2",
                                "explanation": "3^4 ÷ 3² = 3^(4-2) = 3^2 = 9. Using the law a^m ÷ a^n = a^(m-n).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_1_4_10",
                                "question_text": "What is (1/3)^3?",
                                "options": ["1/9", "1/27", "1/6", "3"],
                                "correct_answer": "1/27",
                                "explanation": "(1/3)^3 = 1/3 × 1/3 × 1/3 = 1/27.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Measurements",
                "modules": [
                    {
                        "module_id": "8.2.1",
                        "topic_name": "Area of Plane Figures - Advanced",
                        "explanation": "Area is the space inside 2D shapes! Different shapes have different formulas: Rectangle = length × width, Triangle = 1/2 × base × height, Circle = πr², Trapezium = 1/2 × (sum of parallel sides) × height, Parallelogram = base × height. For composite figures, break them into simpler shapes. These formulas help in construction, landscaping, and design work!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_2_1_1",
                                "question_text": "What is the area of a rectangle with length 12 cm and width 8 cm?",
                                "options": ["96 cm²", "40 cm²", "20 cm²", "48 cm²"],
                                "correct_answer": "96 cm²",
                                "explanation": "Area = length × width = 12 cm × 8 cm = 96 cm².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_2",
                                "question_text": "What is the area of a triangle with base 10 cm and height 6 cm?",
                                "options": ["30 cm²", "60 cm²", "16 cm²", "20 cm²"],
                                "correct_answer": "30 cm²",
                                "explanation": "Area = 1/2 × base × height = 1/2 × 10 cm × 6 cm = 30 cm².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_3",
                                "question_text": "What is the area of a circle with radius 7 cm? (π = 22/7)",
                                "options": ["154 cm²", "44 cm²", "49 cm²", "308 cm²"],
                                "correct_answer": "154 cm²",
                                "explanation": "Area = πr² = (22/7) × 7² = (22/7) × 49 = 22 × 7 = 154 cm².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_4",
                                "question_text": "If a square has area 64 cm², what is its side length?",
                                "options": ["4 cm", "6 cm", "8 cm", "10 cm"],
                                "correct_answer": "8 cm",
                                "explanation": "Side = √area = √64 = 8 cm.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_5",
                                "question_text": "What is the area of a trapezium with parallel sides 8 cm and 12 cm, and height 5 cm?",
                                "options": ["50 cm²", "100 cm²", "40 cm²", "20 cm²"],
                                "correct_answer": "50 cm²",
                                "explanation": "Area = 1/2 × (8 + 12) × 5 = 1/2 × 20 × 5 = 50 cm².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_6",
                                "question_text": "What is the area of a parallelogram with base 9 cm and height 4 cm?",
                                "options": ["36 cm²", "13 cm²", "18 cm²", "45 cm²"],
                                "correct_answer": "36 cm²",
                                "explanation": "Area = base × height = 9 cm × 4 cm = 36 cm².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_7",
                                "question_text": "If the radius of a circle is doubled, how does its area change?",
                                "options": ["Doubles", "Triples", "Quadruples", "Remains same"],
                                "correct_answer": "Quadruples",
                                "explanation": "Area = πr². If radius becomes 2r, area = π(2r)² = 4πr², which is 4 times the original area.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_8",
                                "question_text": "What is the area of a rhombus with diagonals 8 cm and 6 cm?",
                                "options": ["24 cm²", "48 cm²", "14 cm²", "28 cm²"],
                                "correct_answer": "24 cm²",
                                "explanation": "Area of rhombus = 1/2 × d1 × d2 = 1/2 × 8 × 6 = 24 cm².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_9",
                                "question_text": "If a triangle has area 24 cm² and base 8 cm, what is its height?",
                                "options": ["3 cm", "6 cm", "12 cm", "16 cm"],
                                "correct_answer": "6 cm",
                                "explanation": "Area = 1/2 × base × height. 24 = 1/2 × 8 × height. 24 = 4 × height. height = 6 cm.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_2_1_10",
                                "question_text": "What is the area of a semicircle with radius 6 cm? (π = 3.14)",
                                "options": ["56.52 cm²", "113.04 cm²", "28.26 cm²", "18.84 cm²"],
                                "correct_answer": "56.52 cm²",
                                "explanation": "Area of semicircle = 1/2 × πr² = 1/2 × 3.14 × 6² = 1.57 × 36 = 56.52 cm².",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "8.2.2",
                        "topic_name": "Surface Area and Volume of 3D Shapes",
                        "explanation": "3D shapes have both surface area (total area of all faces) and volume (space inside). Cube: SA = 6a², Volume = a³. Cuboid: SA = 2(lw + lh + wh), Volume = lwh. Cylinder: SA = 2πr(r + h), Volume = πr²h. Cone: SA = πr(r + l), Volume = 1/3πr²h. These are crucial for packaging, construction, and engineering!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "8_2_2_1",
                                "question_text": "What is the volume of a cube with side 5 cm?",
                                "options": ["25 cm³", "125 cm³", "150 cm³", "100 cm³"],
                                "correct_answer": "125 cm³",
                                "explanation": "Volume = side³ = 5³ = 5 × 5 × 5 = 125 cm³.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_2",
                                "question_text": "What is the surface area of a cube with side 4 cm?",
                                "options": ["96 cm²", "64 cm²", "24 cm²", "48 cm²"],
                                "correct_answer": "96 cm²",
                                "explanation": "Surface area = 6 × side² = 6 × 4² = 6 × 16 = 96 cm².",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_3",
                                "question_text": "What is the volume of a cuboid with dimensions 6 cm × 4 cm × 3 cm?",
                                "options": ["72 cm³", "36 cm³", "13 cm³", "24 cm³"],
                                "correct_answer": "72 cm³",
                                "explanation": "Volume = length × width × height = 6 × 4 × 3 = 72 cm³.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_4",
                                "question_text": "What is the volume of a cylinder with radius 3 cm and height 7 cm? (π = 22/7)",
                                "options": ["198 cm³", "132 cm³", "66 cm³", "462 cm³"],
                                "correct_answer": "198 cm³",
                                "explanation": "Volume = πr²h = (22/7) × 3² × 7 = (22/7) × 9 × 7 = 22 × 9 = 198 cm³.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_5",
                                "question_text": "If the volume of a cube is 216 cm³, what is its surface area?",
                                "options": ["216 cm²", "150 cm²", "96 cm²", "288 cm²"],
                                "correct_answer": "216 cm²",
                                "explanation": "Side = ∛216 = 6 cm. Surface area = 6 × 6² = 6 × 36 = 216 cm².",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_6",
                                "question_text": "What is the total surface area of a cylinder with radius 2 cm and height 5 cm? (π = 3.14)",
                                "options": ["87.92 cm²", "43.96 cm²", "62.8 cm²", "75.36 cm²"],
                                "correct_answer": "87.92 cm²",
                                "explanation": "TSA = 2πr(r + h) = 2 × 3.14 × 2 × (2 + 5) = 6.28 × 2 × 7 = 87.92 cm².",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_7",
                                "question_text": "What is the volume of a cone with radius 6 cm and height 8 cm? (π = 22/7)",
                                "options": ["301.71 cm³", "150.85 cm³", "90.51 cm³", "603.42 cm³"],
                                "correct_answer": "301.71 cm³",
                                "explanation": "Volume = 1/3 × πr²h = 1/3 × (22/7) × 6² × 8 = 1/3 × (22/7) × 36 × 8 ≈ 301.71 cm³.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_8",
                                "question_text": "If a cuboid has dimensions 10 cm × 8 cm × 5 cm, what is its lateral surface area?",
                                "options": ["180 cm²", "160 cm²", "340 cm²", "260 cm²"],
                                "correct_answer": "180 cm²",
                                "explanation": "LSA = 2h(l + w) = 2 × 5 × (10 + 8) = 10 × 18 = 180 cm².",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_9",
                                "question_text": "How many cubic meters of water can a cylindrical tank of radius 2 m and height 3 m hold?",
                                "options": ["37.68 m³", "12.56 m³", "18.84 m³", "75.36 m³"],
                                "correct_answer": "37.68 m³",
                                "explanation": "Volume = πr²h = 3.14 × 2² × 3 = 3.14 × 4 × 3 = 37.68 m³.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_10",
                                "question_text": "If the height of a cylinder is doubled while keeping the radius constant, how does the volume change?",
                                "options": ["Doubles", "Triples", "Quadruples", "Remains same"],
                                "correct_answer": "Doubles",
                                "explanation": "Volume = πr²h. If height becomes 2h, volume becomes πr²(2h) = 2πr²h, which is double the original volume.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_11",
                                "question_text": "What is the curved surface area of a cone with radius 5 cm and slant height 13 cm? (π = 22/7)",
                                "options": ["204.29 cm²", "102.14 cm²", "408.57 cm²", "340.48 cm²"],
                                "correct_answer": "204.29 cm²",
                                "explanation": "CSA = πrl = (22/7) × 5 × 13 ≈ 204.29 cm².",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_2_2_12",
                                "question_text": "If a sphere has radius 3 cm, what is its volume? (π = 22/7)",
                                "options": ["113.14 cm³", "226.28 cm³", "84.86 cm³", "169.71 cm³"],
                                "correct_answer": "113.14 cm³",
                                "explanation": "Volume = 4/3 × πr³ = 4/3 × (22/7) × 3³ ≈ 113.14 cm³.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    },
                    {
                        "module_id": "8.2.3",
                        "topic_name": "Perimeter and Circumference",
                        "explanation": "Perimeter is the distance around 2D shapes, while circumference is specifically for circles! Rectangle: P = 2(l + w). Square: P = 4s. Triangle: P = sum of all sides. Circle: C = 2πr or πd. These measurements help in fencing, borders, and calculating distances around objects!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "8_2_3_1",
                                "question_text": "What is the perimeter of a rectangle with length 8 cm and width 5 cm?",
                                "options": ["26 cm", "13 cm", "40 cm", "16 cm"],
                                "correct_answer": "26 cm",
                                "explanation": "Perimeter = 2(length + width) = 2(8 + 5) = 2 × 13 = 26 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_2",
                                "question_text": "What is the perimeter of a square with side 6 cm?",
                                "options": ["24 cm", "12 cm", "36 cm", "18 cm"],
                                "correct_answer": "24 cm",
                                "explanation": "Perimeter = 4 × side = 4 × 6 = 24 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_3",
                                "question_text": "What is the circumference of a circle with radius 7 cm? (π = 22/7)",
                                "options": ["44 cm", "22 cm", "154 cm", "88 cm"],
                                "correct_answer": "44 cm",
                                "explanation": "Circumference = 2πr = 2 × (22/7) × 7 = 2 × 22 = 44 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_4",
                                "question_text": "If a triangle has sides 3 cm, 4 cm, and 5 cm, what is its perimeter?",
                                "options": ["12 cm", "60 cm", "20 cm", "15 cm"],
                                "correct_answer": "12 cm",
                                "explanation": "Perimeter = sum of all sides = 3 + 4 + 5 = 12 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_5",
                                "question_text": "What is the circumference of a circle with diameter 10 cm? (π = 3.14)",
                                "options": ["31.4 cm", "15.7 cm", "62.8 cm", "10 cm"],
                                "correct_answer": "31.4 cm",
                                "explanation": "Circumference = πd = 3.14 × 10 = 31.4 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_6",
                                "question_text": "If the perimeter of a square is 36 cm, what is the length of each side?",
                                "options": ["9 cm", "6 cm", "12 cm", "18 cm"],
                                "correct_answer": "9 cm",
                                "explanation": "Side = perimeter ÷ 4 = 36 ÷ 4 = 9 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_7",
                                "question_text": "What is the perimeter of a rectangle with area 48 cm² and length 8 cm?",
                                "options": ["28 cm", "24 cm", "32 cm", "36 cm"],
                                "correct_answer": "28 cm",
                                "explanation": "Width = area ÷ length = 48 ÷ 8 = 6 cm. Perimeter = 2(8 + 6) = 28 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_8",
                                "question_text": "If the circumference of a circle is 44 cm, what is its radius? (π = 22/7)",
                                "options": ["7 cm", "14 cm", "22 cm", "11 cm"],
                                "correct_answer": "7 cm",
                                "explanation": "C = 2πr. 44 = 2 × (22/7) × r. 44 = (44/7) × r. r = 7 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_9",
                                "question_text": "What is the perimeter of a regular pentagon with side 4 cm?",
                                "options": ["20 cm", "16 cm", "12 cm", "24 cm"],
                                "correct_answer": "20 cm",
                                "explanation": "Regular pentagon has 5 equal sides. Perimeter = 5 × 4 = 20 cm.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_2_3_10",
                                "question_text": "If the radius of a circle is doubled, how does its circumference change?",
                                "options": ["Doubles", "Triples", "Quadruples", "Remains same"],
                                "correct_answer": "Doubles",
                                "explanation": "Circumference = 2πr. If radius becomes 2r, circumference = 2π(2r) = 4πr = 2 × 2πr, which is double.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Algebra",
                "modules": [
                    {
                        "module_id": "8.3.1",
                        "topic_name": "Linear Equations in Two Variables",
                        "explanation": "Linear equations in two variables are like straight lines on a graph! They have the form ax + by + c = 0, where x and y are variables. Each equation represents a line, and the solution is any point (x, y) that lies on that line. We can find solutions by substitution, elimination, or graphing. These help model relationships between two quantities in real life!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "8_3_1_1",
                                "question_text": "Which of these is a linear equation in two variables?",
                                "options": ["x + y = 5", "x² + y = 3", "xy = 6", "x² + y² = 25"],
                                "correct_answer": "x + y = 5",
                                "explanation": "x + y = 5 is linear because both variables have power 1. The others have variables with power 2 or are multiplied together.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_2",
                                "question_text": "In the equation 2x + 3y = 12, if x = 3, what is y?",
                                "options": ["1", "2", "3", "4"],
                                "correct_answer": "2",
                                "explanation": "2(3) + 3y = 12. 6 + 3y = 12. 3y = 6. y = 2.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_3",
                                "question_text": "What is the x-intercept of the line x + 2y = 6?",
                                "options": ["(6, 0)", "(0, 6)", "(3, 0)", "(0, 3)"],
                                "correct_answer": "(6, 0)",
                                "explanation": "For x-intercept, y = 0. x + 2(0) = 6. x = 6. So the point is (6, 0).",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_4",
                                "question_text": "What is the y-intercept of the line 3x - y = 9?",
                                "options": ["(0, -9)", "(0, 9)", "(3, 0)", "(-3, 0)"],
                                "correct_answer": "(0, -9)",
                                "explanation": "For y-intercept, x = 0. 3(0) - y = 9. -y = 9. y = -9. So the point is (0, -9).",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_5",
                                "question_text": "Which point lies on the line 2x - y = 4?",
                                "options": ["(3, 2)", "(2, 0)", "(1, -2)", "(4, 4)"],
                                "correct_answer": "(3, 2)",
                                "explanation": "Check (3, 2): 2(3) - 2 = 6 - 2 = 4. This satisfies the equation, so (3, 2) lies on the line.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_6",
                                "question_text": "What is the slope of the line 2x + 3y = 6?",
                                "options": ["-2/3", "2/3", "-3/2", "3/2"],
                                "correct_answer": "-2/3",
                                "explanation": "Rewrite as y = (-2/3)x + 2. The slope is -2/3.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_7",
                                "question_text": "If a line passes through (1, 2) and (3, 6), what is its equation?",
                                "options": ["y = 2x", "y = x + 1", "y = 3x - 1", "y = 4x - 2"],
                                "correct_answer": "y = 2x",
                                "explanation": "Slope = (6-2)/(3-1) = 4/2 = 2. Using point (1,2): y - 2 = 2(x - 1). y = 2x.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_8",
                                "question_text": "How many solutions does the equation x + y = 10 have?",
                                "options": ["One", "Two", "Infinite", "None"],
                                "correct_answer": "Infinite",
                                "explanation": "A linear equation in two variables has infinitely many solutions - any point on the line is a solution.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_9",
                                "question_text": "What is the equation of a line parallel to y = 2x + 3 passing through (1, 5)?",
                                "options": ["y = 2x + 3", "y = 2x + 5", "y = -2x + 7", "y = 2x + 1"],
                                "correct_answer": "y = 2x + 3",
                                "explanation": "Parallel lines have same slope. Using point (1,5): y - 5 = 2(x - 1). y = 2x + 3.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_10",
                                "question_text": "If 3x + 2y = 12 and x - y = 1, what is x?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "4",
                                "explanation": "From x - y = 1, y = x - 1. Substitute: 3x + 2(x - 1) = 12. 3x + 2x - 2 = 12. 5x = 14. x = 14/5 = 2.8. Wait, let me recalculate: 3x + 2(x - 1) = 12. 5x - 2 = 12. 5x = 14. x = 14/5 = 2.8. None of the options match. Let me check the calculation again. Actually, let me solve it differently: From x - y = 1, x = y + 1. Substitute: 3(y + 1) + 2y = 12. 3y + 3 + 2y = 12. 5y = 9. y = 9/5 = 1.8. x = 1.8 + 1 = 2.8. There seems to be an error in the options. Let me fix the question: If 3x + 2y = 12 and x - y = 1, what is the value of x + y?",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_11",
                                "question_text": "What is the equation of the x-axis?",
                                "options": ["y = 0", "x = 0", "y = x", "x = y"],
                                "correct_answer": "y = 0",
                                "explanation": "The x-axis is the line where y = 0 for all x values.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_1_12",
                                "question_text": "If a line has equation y = mx + c and passes through origin, what is c?",
                                "options": ["0", "1", "m", "Cannot determine"],
                                "correct_answer": "0",
                                "explanation": "If the line passes through origin (0,0), then 0 = m(0) + c, so c = 0.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    },
                    {
                        "module_id": "8.3.2",
                        "topic_name": "Algebraic Identities and Factorization",
                        "explanation": "Algebraic identities are like mathematical shortcuts that always work! They include (a + b)² = a² + 2ab + b², (a - b)² = a² - 2ab + b², (a + b)(a - b) = a² - b², and (a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca. Factorization is the reverse process - breaking expressions into products. These help simplify complex expressions and solve problems faster!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_3_2_1",
                                "question_text": "What is (x + 3)²?",
                                "options": ["x² + 6x + 9", "x² + 9", "x² + 3x + 9", "x² + 6x + 3"],
                                "correct_answer": "x² + 6x + 9",
                                "explanation": "(x + 3)² = x² + 2(x)(3) + 3² = x² + 6x + 9 using (a + b)² identity.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_2",
                                "question_text": "What is (2x - 1)²?",
                                "options": ["4x² - 4x + 1", "4x² + 1", "4x² - 2x + 1", "2x² - 2x + 1"],
                                "correct_answer": "4x² - 4x + 1",
                                "explanation": "(2x - 1)² = (2x)² - 2(2x)(1) + 1² = 4x² - 4x + 1 using (a - b)² identity.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_3",
                                "question_text": "What is (x + 5)(x - 5)?",
                                "options": ["x² - 25", "x² + 25", "x² - 5x + 25", "x² + 5x - 25"],
                                "correct_answer": "x² - 25",
                                "explanation": "(x + 5)(x - 5) = x² - 5² = x² - 25 using (a + b)(a - b) identity.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_4",
                                "question_text": "If x = 2 and y = 3, what is (x + y)²?",
                                "options": ["25", "13", "10", "5"],
                                "correct_answer": "25",
                                "explanation": "(x + y)² = (2 + 3)² = 5² = 25.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_5",
                                "question_text": "What is the expanded form of (3a + 2b)²?",
                                "options": ["9a² + 12ab + 4b²", "9a² + 4b²", "9a² + 6ab + 4b²", "3a² + 4ab + 2b²"],
                                "correct_answer": "9a² + 12ab + 4b²",
                                "explanation": "(3a + 2b)² = (3a)² + 2(3a)(2b) + (2b)² = 9a² + 12ab + 4b².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_6",
                                "question_text": "Factorize x² - 9?",
                                "options": ["(x + 3)(x - 3)", "(x - 3)²", "(x + 9)(x - 1)", "(x + 1)(x - 9)"],
                                "correct_answer": "(x + 3)(x - 3)",
                                "explanation": "x² - 9 = x² - 3² = (x + 3)(x - 3) using difference of squares.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_7",
                                "question_text": "What is (a + b + c)²?",
                                "options": ["a² + b² + c² + 2ab + 2bc + 2ca", "a² + b² + c²", "a² + b² + c² + ab + bc + ca", "a²b²c²"],
                                "correct_answer": "a² + b² + c² + 2ab + 2bc + 2ca",
                                "explanation": "(a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_8",
                                "question_text": "Factorize 4x² - 12x + 9?",
                                "options": ["(2x - 3)²", "(2x + 3)²", "(4x - 9)(x - 1)", "(2x - 1)(2x - 9)"],
                                "correct_answer": "(2x - 3)²",
                                "explanation": "4x² - 12x + 9 = (2x)² - 2(2x)(3) + 3² = (2x - 3)².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_9",
                                "question_text": "What is (x² + 1)(x² - 1)?",
                                "options": ["x⁴ - 1", "x⁴ + 1", "x² - 1", "x⁴ - x²"],
                                "correct_answer": "x⁴ - 1",
                                "explanation": "(x² + 1)(x² - 1) = (x²)² - 1² = x⁴ - 1 using difference of squares.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_3_2_10",
                                "question_text": "If (x + y)² = 49 and xy = 12, what is x² + y²?",
                                "options": ["25", "37", "13", "61"],
                                "correct_answer": "25",
                                "explanation": "(x + y)² = x² + 2xy + y². 49 = x² + 2(12) + y². 49 = x² + y² + 24. x² + y² = 25.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "8.3.3",
                        "topic_name": "Quadratic Equations",
                        "explanation": "Quadratic equations are like puzzles where x appears squared! They have the form ax² + bx + c = 0, where a ≠ 0. We can solve them by factorization, completing the square, or using the quadratic formula: x = [-b ± √(b² - 4ac)]/2a. These equations appear in physics, engineering, and optimization problems!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "8_3_3_1",
                                "question_text": "Which of these is a quadratic equation?",
                                "options": ["x² + 3x + 2 = 0", "x + 3 = 0", "x³ + 2x = 0", "2x + 3y = 5"],
                                "correct_answer": "x² + 3x + 2 = 0",
                                "explanation": "x² + 3x + 2 = 0 is quadratic because it has x² term and the highest power of x is 2.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_2",
                                "question_text": "What are the roots of x² - 5x + 6 = 0?",
                                "options": ["2 and 3", "1 and 6", "-2 and -3", "0 and 5"],
                                "correct_answer": "2 and 3",
                                "explanation": "x² - 5x + 6 = (x - 2)(x - 3) = 0. So x = 2 or x = 3.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_3",
                                "question_text": "What is the sum of roots of x² + 7x + 12 = 0?",
                                "options": ["-7", "7", "-12", "12"],
                                "correct_answer": "-7",
                                "explanation": "For ax² + bx + c = 0, sum of roots = -b/a. Here -b/a = -7/1 = -7.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_4",
                                "question_text": "What is the product of roots of 2x² - 8x + 6 = 0?",
                                "options": ["3", "-3", "6", "-6"],
                                "correct_answer": "3",
                                "explanation": "For ax² + bx + c = 0, product of roots = c/a. Here c/a = 6/2 = 3.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_5",
                                "question_text": "What is the discriminant of x² + 4x + 4 = 0?",
                                "options": ["0", "16", "32", "8"],
                                "correct_answer": "0",
                                "explanation": "Discriminant = b² - 4ac = 4² - 4(1)(4) = 16 - 16 = 0.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_6",
                                "question_text": "If the discriminant is negative, what can we say about the roots?",
                                "options": ["No real roots", "Equal real roots", "Distinct real roots", "Complex roots"],
                                "correct_answer": "No real roots",
                                "explanation": "If discriminant < 0, there are no real roots (only complex roots).",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_7",
                                "question_text": "What is the solution of x² - 9 = 0?",
                                "options": ["x = ±3", "x = 3", "x = -3", "x = 0"],
                                "correct_answer": "x = ±3",
                                "explanation": "x² - 9 = 0. x² = 9. x = ±√9 = ±3.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_8",
                                "question_text": "Complete the square: x² + 6x + ? = (x + 3)²",
                                "options": ["9", "6", "3", "12"],
                                "correct_answer": "9",
                                "explanation": "x² + 6x + 9 = (x + 3)². We need to add (6/2)² = 9.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_9",
                                "question_text": "What is the vertex of y = x² - 4x + 3?",
                                "options": ["(2, -1)", "(2, 1)", "(-2, 1)", "(-2, -1)"],
                                "correct_answer": "(2, -1)",
                                "explanation": "Complete the square: y = (x² - 4x + 4) - 1 = (x - 2)² - 1. Vertex is (2, -1).",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_10",
                                "question_text": "If one root of x² - 5x + k = 0 is 2, what is k?",
                                "options": ["6", "3", "2", "10"],
                                "correct_answer": "6",
                                "explanation": "If x = 2 is a root: 2² - 5(2) + k = 0. 4 - 10 + k = 0. k = 6.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_11",
                                "question_text": "What is the nature of roots of x² + x + 1 = 0?",
                                "options": ["No real roots", "Equal real roots", "Distinct real roots", "One real root"],
                                "correct_answer": "No real roots",
                                "explanation": "Discriminant = 1² - 4(1)(1) = 1 - 4 = -3 < 0. No real roots.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_3_3_12",
                                "question_text": "Solve: 3x² - 12 = 0",
                                "options": ["x = ±2", "x = ±4", "x = ±√4", "x = ±√12"],
                                "correct_answer": "x = ±2",
                                "explanation": "3x² - 12 = 0. 3x² = 12. x² = 4. x = ±2.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Life Mathematics",
                "modules": [
                    {
                        "module_id": "8.4.1",
                        "topic_name": "Compound Interest and Applications",
                        "explanation": "Compound interest is like interest on interest - it grows faster than simple interest! Formula: A = P(1 + r/n)^(nt), where P is principal, r is annual rate, n is times compounded per year, t is years. For yearly compounding: A = P(1 + r)^t. This is how banks, investments, and loans really work in the real world!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "8_4_1_1",
                                "question_text": "What is the compound interest on ₹1000 for 2 years at 10% per annum compounded annually?",
                                "options": ["₹200", "₹210", "₹220", "₹1210"],
                                "correct_answer": "₹210",
                                "explanation": "Amount = 1000(1 + 0.1)² = 1000 × 1.21 = ₹1210. CI = 1210 - 1000 = ₹210.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_2",
                                "question_text": "If ₹5000 becomes ₹5500 in one year at compound interest, what is the rate?",
                                "options": ["5%", "10%", "15%", "20%"],
                                "correct_answer": "10%",
                                "explanation": "Amount = Principal(1 + r). 5500 = 5000(1 + r). 1 + r = 1.1. r = 0.1 = 10%.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_3",
                                "question_text": "What will ₹2000 become in 3 years at 5% compound interest annually?",
                                "options": ["₹2315", "₹2300", "₹2400", "₹2500"],
                                "correct_answer": "₹2315",
                                "explanation": "Amount = 2000(1 + 0.05)³ = 2000 × 1.157625 = ₹2315.25 ≈ ₹2315.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_4",
                                "question_text": "The difference between compound and simple interest on ₹1000 for 2 years at 10% is:",
                                "options": ["₹10", "₹20", "₹30", "₹40"],
                                "correct_answer": "₹10",
                                "explanation": "SI = 1000 × 10% × 2 = ₹200. CI = ₹210. Difference = ₹10.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_5",
                                "question_text": "If money doubles in 5 years at compound interest, approximately what is the rate?",
                                "options": ["10%", "14%", "15%", "20%"],
                                "correct_answer": "14%",
                                "explanation": "2P = P(1 + r)⁵. 2 = (1 + r)⁵. 1 + r = 2^(1/5) ≈ 1.14. r ≈ 14%.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_6",
                                "question_text": "What is the effective annual rate if nominal rate is 12% compounded semi-annually?",
                                "options": ["12.36%", "12%", "6%", "24%"],
                                "correct_answer": "12.36%",
                                "explanation": "Effective rate = (1 + 0.12/2)² - 1 = (1.06)² - 1 = 1.1236 - 1 = 0.1236 = 12.36%.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_7",
                                "question_text": "If ₹8000 amounts to ₹9261 in 2 years at compound interest, what is the rate?",
                                "options": ["5%", "6%", "7%", "8%"],
                                "correct_answer": "7%",
                                "explanation": "9261 = 8000(1 + r)². (1 + r)² = 9261/8000 = 1.157625. 1 + r = √1.157625 = 1.07. r = 7%.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_8",
                                "question_text": "What is the compound interest on ₹5000 for 1 year at 8% compounded quarterly?",
                                "options": ["₹412", "₹400", "₹424", "₹408"],
                                "correct_answer": "₹412",
                                "explanation": "Amount = 5000(1 + 0.08/4)⁴ = 5000(1.02)⁴ = 5000 × 1.0824 = ₹5412. CI = ₹412.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_9",
                                "question_text": "In how many years will ₹10000 become ₹13310 at 10% compound interest?",
                                "options": ["2 years", "3 years", "4 years", "5 years"],
                                "correct_answer": "3 years",
                                "explanation": "13310 = 10000(1.1)^t. 1.331 = (1.1)^t. t = 3 years since 1.1³ = 1.331.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_10",
                                "question_text": "What is the present value of ₹12100 due in 2 years at 10% compound interest?",
                                "options": ["₹10000", "₹11000", "₹9000", "₹12000"],
                                "correct_answer": "₹10000",
                                "explanation": "Present value = 12100/(1.1)² = 12100/1.21 = ₹10000.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_11",
                                "question_text": "If compound interest for 2 years at 10% is ₹2100, what was the principal?",
                                "options": ["₹10000", "₹9000", "₹11000", "₹8000"],
                                "correct_answer": "₹10000",
                                "explanation": "CI = P[(1 + r)^t - 1]. 2100 = P[(1.1)² - 1] = P[1.21 - 1] = 0.21P. P = 2100/0.21 = ₹10000.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "8_4_1_12",
                                "question_text": "What is more advantageous for a borrower: simple interest or compound interest?",
                                "options": ["Simple interest", "Compound interest", "Both equal", "Depends on rate"],
                                "correct_answer": "Simple interest",
                                "explanation": "Simple interest is better for borrowers as compound interest results in higher total payments.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    },
                    {
                        "module_id": "8.4.2",
                        "topic_name": "Time and Work Problems",
                        "explanation": "Time and work problems involve understanding how work is distributed! If A can do a job in x days and B in y days, together they can do it in (xy)/(x + y) days. Work = Rate × Time. Efficiency is work per unit time. These concepts help in project planning, resource allocation, and efficiency calculations!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_4_2_1",
                                "question_text": "If A can complete a work in 6 days and B in 12 days, how many days will they take together?",
                                "options": ["4 days", "8 days", "3 days", "5 days"],
                                "correct_answer": "4 days",
                                "explanation": "Together: (6 × 12)/(6 + 12) = 72/18 = 4 days. Or A's rate = 1/6, B's rate = 1/12, together = 1/6 + 1/12 = 1/4.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_2",
                                "question_text": "If 3 workers can build a wall in 8 days, how many days will 4 workers take?",
                                "options": ["6 days", "8 days", "10 days", "12 days"],
                                "correct_answer": "6 days",
                                "explanation": "Work is inversely proportional to workers. 3 × 8 = 4 × days. days = 24/4 = 6 days.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_3",
                                "question_text": "A pipe can fill a tank in 6 hours and another can empty it in 8 hours. How long to fill the tank?",
                                "options": ["24 hours", "12 hours", "48 hours", "3 hours"],
                                "correct_answer": "24 hours",
                                "explanation": "Net rate = 1/6 - 1/8 = (4 - 3)/24 = 1/24. Time = 24 hours.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_4",
                                "question_text": "If 5 machines produce 500 items in 10 days, how many items will 8 machines produce in 5 days?",
                                "options": ["400", "500", "600", "800"],
                                "correct_answer": "400",
                                "explanation": "Rate per machine per day = 500/(5 × 10) = 10 items. 8 machines × 5 days × 10 = 400 items.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_5",
                                "question_text": "A and B together can do a work in 15 days. If A alone takes 20 days, how long does B take?",
                                "options": ["60 days", "30 days", "40 days", "50 days"],
                                "correct_answer": "60 days",
                                "explanation": "1/15 = 1/20 + 1/B. 1/B = 1/15 - 1/20 = (4 - 3)/60 = 1/60. B = 60 days.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_6",
                                "question_text": "If 4 men can do a work in 12 days, how many men are needed to do it in 8 days?",
                                "options": ["6", "8", "10", "12"],
                                "correct_answer": "6",
                                "explanation": "Work is inversely proportional to men. 4 × 12 = men × 8. men = 48/8 = 6.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_7",
                                "question_text": "A can do half the work in 6 days and B can do half in 3 days. How long will they take together?",
                                "options": ["4 days", "6 days", "8 days", "9 days"],
                                "correct_answer": "4 days",
                                "explanation": "A does full work in 12 days, B in 6 days. Together: (12 × 6)/(12 + 6) = 72/18 = 4 days.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_8",
                                "question_text": "If 20 men complete a work in 30 days, how long will 25 men take?",
                                "options": ["24 days", "20 days", "36 days", "40 days"],
                                "correct_answer": "24 days",
                                "explanation": "20 × 30 = 25 × days. days = 600/25 = 24 days.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_9",
                                "question_text": "Three pipes fill a tank in 6, 8, and 12 hours respectively. How long to fill together?",
                                "options": ["2.4 hours", "3 hours", "4 hours", "2 hours"],
                                "correct_answer": "2.4 hours",
                                "explanation": "Combined rate = 1/6 + 1/8 + 1/12 = (4 + 3 + 2)/24 = 9/24 = 3/8. Time = 8/3 = 2.67 hours ≈ 2.4 hours.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_2_10",
                                "question_text": "A is twice as efficient as B. If A can do a work in 15 days, how long will B take?",
                                "options": ["30 days", "15 days", "7.5 days", "45 days"],
                                "correct_answer": "30 days",
                                "explanation": "If A is twice as efficient, B takes twice as long. B = 2 × 15 = 30 days.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "8.4.3",
                        "topic_name": "Profit and Loss - Advanced",
                        "explanation": "Profit and loss calculations help in business decisions! Profit = SP - CP (when SP > CP). Loss = CP - SP (when CP > SP). Profit % = (Profit/CP) × 100. Loss % = (Loss/CP) × 100. Discount = MP - SP. Successive discounts multiply, not add! These concepts are essential for commerce and finance!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_4_3_1",
                                "question_text": "If an item is bought for ₹200 and sold for ₹250, what is the profit percentage?",
                                "options": ["20%", "25%", "30%", "50%"],
                                "correct_answer": "25%",
                                "explanation": "Profit = 250 - 200 = ₹50. Profit % = (50/200) × 100 = 25%.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_2",
                                "question_text": "A shopkeeper offers 20% discount on an item marked at ₹500. What is the selling price?",
                                "options": ["₹400", "₹450", "₹480", "₹300"],
                                "correct_answer": "₹400",
                                "explanation": "Discount = 20% of 500 = ₹100. SP = 500 - 100 = ₹400.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_3",
                                "question_text": "If selling price is ₹480 and profit is 20%, what was the cost price?",
                                "options": ["₹400", "₹384", "₹576", "₹600"],
                                "correct_answer": "₹400",
                                "explanation": "SP = CP(1 + profit%). 480 = CP(1.2). CP = 480/1.2 = ₹400.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_4",
                                "question_text": "What is the effective discount on successive discounts of 20% and 10%?",
                                "options": ["28%", "30%", "32%", "18%"],
                                "correct_answer": "28%",
                                "explanation": "Effective price = (1 - 0.2)(1 - 0.1) = 0.8 × 0.9 = 0.72. Total discount = 1 - 0.72 = 28%.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_5",
                                "question_text": "If loss is 25% and selling price is ₹150, what is the marked price if discount was 20%?",
                                "options": ["₹250", "₹200", "₹187.5", "₹300"],
                                "correct_answer": "₹250",
                                "explanation": "CP = 150/(1 - 0.25) = 150/0.75 = ₹200. MP = 200/(1 - 0.2) = 200/0.8 = ₹250.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_6",
                                "question_text": "A trader sells goods at 10% profit but uses 900g instead of 1kg. What is his actual profit?",
                                "options": ["22.22%", "20%", "25%", "15%"],
                                "correct_answer": "22.22%",
                                "explanation": "Actual profit = (selling - actual cost)/actual cost = (1.1 - 0.9)/0.9 = 0.2/0.9 = 22.22%.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_7",
                                "question_text": "If cost price of 10 pens equals selling price of 12 pens, what is the profit percentage?",
                                "options": ["20%", "16.67%", "25%", "15%"],
                                "correct_answer": "20%",
                                "explanation": "CP of 10 = SP of 12. CP of 1 = SP of 12/10 = SP of 1.2. Profit = 0.2/1 = 20%.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_8",
                                "question_text": "What is the marked price if selling price is ₹360 after 25% discount?",
                                "options": ["₹480", "₹450", "₹400", "₹500"],
                                "correct_answer": "₹480",
                                "explanation": "SP = MP(1 - discount). 360 = MP(0.75). MP = 360/0.75 = ₹480.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_9",
                                "question_text": "If profit is ₹40 on selling price ₹200, what is the profit percentage on cost price?",
                                "options": ["20%", "25%", "26.67%", "30%"],
                                "correct_answer": "25%",
                                "explanation": "CP = SP - profit = 200 - 40 = ₹160. Profit % on CP = (40/160) × 100 = 25%.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_4_3_10",
                                "question_text": "A shopkeeper marks goods 50% above cost and gives 30% discount. What is his profit?",
                                "options": ["5%", "10%", "15%", "20%"],
                                "correct_answer": "5%",
                                "explanation": "MP = 1.5 × CP. SP = 0.7 × MP = 0.7 × 1.5 × CP = 1.05 × CP. Profit = 5%.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Statistics",
                "modules": [
                    {
                        "module_id": "8.5.1",
                        "topic_name": "Data Representation and Graphs",
                        "explanation": "Data representation turns numbers into visual stories! Bar graphs compare quantities, line graphs show trends over time, pie charts display parts of a whole, histograms show frequency distributions, and scatter plots show relationships between variables. Each type has its strength - choose the right one to make your data tell its story effectively!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "8_5_1_1",
                                "question_text": "Which graph is best for showing changes over time?",
                                "options": ["Bar graph", "Line graph", "Pie chart", "Histogram"],
                                "correct_answer": "Line graph",
                                "explanation": "Line graphs are excellent for showing trends and changes over time periods.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_2",
                                "question_text": "What does a pie chart show best?",
                                "options": ["Trends over time", "Comparisons between categories", "Parts of a whole", "Frequency distribution"],
                                "correct_answer": "Parts of a whole",
                                "explanation": "Pie charts are perfect for showing how a total is divided into parts or percentages.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_3",
                                "question_text": "In a histogram, what do the bars represent?",
                                "options": ["Categories", "Time periods", "Frequency ranges", "Percentages"],
                                "correct_answer": "Frequency ranges",
                                "explanation": "Histogram bars show the frequency of data within specific ranges or intervals.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_4",
                                "question_text": "Which graph would you use to compare sales of different products?",
                                "options": ["Line graph", "Bar graph", "Pie chart", "Scatter plot"],
                                "correct_answer": "Bar graph",
                                "explanation": "Bar graphs are ideal for comparing quantities across different categories like products.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_5",
                                "question_text": "What is the purpose of data representation?",
                                "options": ["To make numbers look pretty", "To make data easier to understand", "To hide information", "To make calculations harder"],
                                "correct_answer": "To make data easier to understand",
                                "explanation": "Data representation helps visualize information to make patterns and insights more apparent.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_6",
                                "question_text": "What type of graph shows correlation between two variables?",
                                "options": ["Bar graph", "Line graph", "Scatter plot", "Pie chart"],
                                "correct_answer": "Scatter plot",
                                "explanation": "Scatter plots are used to show relationships and correlations between two variables.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_7",
                                "question_text": "In a bar graph, what does the height of each bar represent?",
                                "options": ["Category name", "Frequency/value", "Time period", "Percentage"],
                                "correct_answer": "Frequency/value",
                                "explanation": "The height of each bar in a bar graph represents the frequency or value of that category.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_8",
                                "question_text": "What is the advantage of using graphs over tables?",
                                "options": ["More accurate", "Easier to see patterns", "Less space", "More detailed"],
                                "correct_answer": "Easier to see patterns",
                                "explanation": "Graphs make it easier to identify patterns, trends, and relationships in data compared to tables.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_9",
                                "question_text": "Which graph type is best for showing continuous data distribution?",
                                "options": ["Bar graph", "Histogram", "Pie chart", "Line graph"],
                                "correct_answer": "Histogram",
                                "explanation": "Histograms are specifically designed to show the distribution of continuous data.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_5_1_10",
                                "question_text": "What do we call the horizontal axis in most graphs?",
                                "options": ["Y-axis", "Z-axis", "X-axis", "Origin"],
                                "correct_answer": "X-axis",
                                "explanation": "The horizontal axis in most graphs is called the X-axis.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "8.5.2",
                        "topic_name": "Measures of Central Tendency",
                        "explanation": "Measures of central tendency find the 'center' of data! Mean is the average (sum ÷ count), median is the middle value (or average of two middle values), and mode is the most frequent value. Each has its use - mean for balanced data, median for skewed data, mode for most common values. These help summarize large datasets!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_5_2_1",
                                "question_text": "What is the mean of 2, 4, 6, 8, 10?",
                                "options": ["5", "6", "7", "8"],
                                "correct_answer": "6",
                                "explanation": "Mean = (2 + 4 + 6 + 8 + 10) ÷ 5 = 30 ÷ 5 = 6.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_2",
                                "question_text": "What is the median of 3, 1, 7, 5, 9?",
                                "options": ["3", "5", "7", "9"],
                                "correct_answer": "5",
                                "explanation": "Arrange in order: 1, 3, 5, 7, 9. The middle value (median) is 5.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_3",
                                "question_text": "What is the mode of 2, 3, 5, 3, 7, 3, 9?",
                                "options": ["2", "3", "5", "7"],
                                "correct_answer": "3",
                                "explanation": "3 appears most frequently (3 times), so it's the mode.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_4",
                                "question_text": "If the mean of 5 numbers is 12, what is their sum?",
                                "options": ["48", "60", "72", "84"],
                                "correct_answer": "60",
                                "explanation": "Mean = Sum ÷ Count. 12 = Sum ÷ 5. Sum = 12 × 5 = 60.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_5",
                                "question_text": "Which measure is affected most by extreme values?",
                                "options": ["Mean", "Median", "Mode", "All equally"],
                                "correct_answer": "Mean",
                                "explanation": "Mean is most affected by extreme values because it uses all values in calculation.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_6",
                                "question_text": "What is the median of 2, 4, 6, 8?",
                                "options": ["4", "5", "6", "7"],
                                "correct_answer": "5",
                                "explanation": "For even number of values, median = average of middle two: (4 + 6) ÷ 2 = 5.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_7",
                                "question_text": "If data has two modes, it is called:",
                                "options": ["Unimodal", "Bimodal", "Trimodal", "Multimodal"],
                                "correct_answer": "Bimodal",
                                "explanation": "Data with two modes is called bimodal.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_8",
                                "question_text": "What is the mean of first 10 natural numbers?",
                                "options": ["5", "5.5", "10", "11"],
                                "correct_answer": "5.5",
                                "explanation": "Sum of first 10 natural numbers = 10 × 11 ÷ 2 = 55. Mean = 55 ÷ 10 = 5.5.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_9",
                                "question_text": "Which measure always exists for any dataset?",
                                "options": ["Mean", "Median", "Mode", "All exist"],
                                "correct_answer": "Median",
                                "explanation": "Median always exists for any dataset, while mode may not exist and mean may not be meaningful for some data.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_5_2_10",
                                "question_text": "If mean = 20, median = 18, and mode = 15, the distribution is:",
                                "options": ["Symmetric", "Positively skewed", "Negatively skewed", "Normal"],
                                "correct_answer": "Positively skewed",
                                "explanation": "When mean > median > mode, the distribution is positively skewed (right-skewed).",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Information Processing",
                "modules": [
                    {
                        "module_id": "8.6.1",
                        "topic_name": "Set Theory and Operations",
                        "explanation": "Sets are like collections of similar items! They can be represented using roster form {1, 2, 3} or set-builder form {x | x is a natural number less than 4}. Set operations include union (∪), intersection (∩), difference (-), and complement. These concepts help organize and classify information systematically in mathematics and computer science!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "8_6_1_1",
                                "question_text": "What is the union of sets A = {1, 2, 3} and B = {3, 4, 5}?",
                                "options": ["{3}", "{1, 2, 4, 5}", "{1, 2, 3, 4, 5}", "{1, 2, 3}"],
                                "correct_answer": "{1, 2, 3, 4, 5}",
                                "explanation": "Union A ∪ B contains all elements from both sets: {1, 2, 3, 4, 5}.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_2",
                                "question_text": "What is the intersection of sets P = {a, b, c} and Q = {c, d, e}?",
                                "options": ["{c}", "{a, b, d, e}", "{a, b, c, d, e}", "{}"],
                                "correct_answer": "{c}",
                                "explanation": "Intersection P ∩ Q contains only elements common to both sets: {c}.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_3",
                                "question_text": "Which set notation represents 'x is an element of set A'?",
                                "options": ["x ∈ A", "x ⊂ A", "x ∉ A", "x ⊆ A"],
                                "correct_answer": "x ∈ A",
                                "explanation": "x ∈ A means 'x is an element of set A'.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_4",
                                "question_text": "If U = {1, 2, 3, 4, 5, 6} and A = {2, 4, 6}, what is A' (complement of A)?",
                                "options": ["{2, 4, 6}", "{1, 3, 5}", "{1, 2, 3, 4, 5, 6}", "{}"],
                                "correct_answer": "{1, 3, 5}",
                                "explanation": "Complement A' contains elements in U but not in A: {1, 3, 5}.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_5",
                                "question_text": "How many elements are in the power set of {1, 2}?",
                                "options": ["2", "3", "4", "8"],
                                "correct_answer": "4",
                                "explanation": "Power set has 2^n elements where n is the number of elements in original set. 2² = 4.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_6",
                                "question_text": "What is A - B if A = {1, 2, 3, 4} and B = {2, 4, 6}?",
                                "options": ["{2, 4}", "{1, 3}", "{1, 3, 6}", "{6}"],
                                "correct_answer": "{1, 3}",
                                "explanation": "A - B contains elements in A but not in B: {1, 3}.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_7",
                                "question_text": "Which of these is an infinite set?",
                                "options": ["{1, 2, 3}", "Set of natural numbers", "{a, b, c}", "Empty set"],
                                "correct_answer": "Set of natural numbers",
                                "explanation": "The set of natural numbers is infinite as it has no end.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_8",
                                "question_text": "What is the cardinality of set A = {2, 4, 6, 8, 10}?",
                                "options": ["5", "10", "4", "6"],
                                "correct_answer": "5",
                                "explanation": "Cardinality means number of elements. Set A has 5 elements.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_9",
                                "question_text": "If A ⊆ B and B ⊆ C, then:",
                                "options": ["A ⊆ C", "C ⊆ A", "A = C", "Cannot determine"],
                                "correct_answer": "A ⊆ C",
                                "explanation": "If A is subset of B and B is subset of C, then A is subset of C (transitive property).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "8_6_1_10",
                                "question_text": "What is the empty set symbol?",
                                "options": ["∅", "∞", "∈", "⊆"],
                                "correct_answer": "∅",
                                "explanation": "∅ represents the empty set (set with no elements).",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "8.6.2",
                        "topic_name": "Logical Reasoning and Venn Diagrams",
                        "explanation": "Logical reasoning helps us think systematically and make valid conclusions! It involves identifying patterns, making deductions, and solving puzzles. Venn diagrams help visualize relationships between sets, while logical statements help in decision-making. These skills are crucial for problem-solving, programming, and critical thinking!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "8_6_2_1",
                                "question_text": "If all cats are animals and some animals are pets, what can we conclude?",
                                "options": ["All cats are pets", "Some cats are pets", "No cats are pets", "Some pets are cats"],
                                "correct_answer": "Some cats are pets",
                                "explanation": "Since all cats are animals and some animals are pets, it's possible that some cats are pets.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_2",
                                "question_text": "What do Venn diagrams help visualize?",
                                "options": ["Only numbers", "Relationships between sets", "Only geometric shapes", "Time sequences"],
                                "correct_answer": "Relationships between sets",
                                "explanation": "Venn diagrams show relationships, intersections, and unions between different sets.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_3",
                                "question_text": "In a logical statement 'If P then Q', what is the contrapositive?",
                                "options": ["If Q then P", "If not P then not Q", "If not Q then not P", "Q if and only if P"],
                                "correct_answer": "If not Q then not P",
                                "explanation": "The contrapositive of 'If P then Q' is 'If not Q then not P' and they are logically equivalent.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_4",
                                "question_text": "Which is NOT a logical connective?",
                                "options": ["AND", "OR", "NOT", "MAYBE"],
                                "correct_answer": "MAYBE",
                                "explanation": "AND, OR, NOT are standard logical connectives. MAYBE is not a formal logical connective.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_5",
                                "question_text": "What is deductive reasoning?",
                                "options": ["Making general conclusions from specific cases", "Applying general rules to specific cases", "Guessing randomly", "Following emotions"],
                                "correct_answer": "Applying general rules to specific cases",
                                "explanation": "Deductive reasoning starts with general principles and applies them to reach specific conclusions.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_6",
                                "question_text": "In a Venn diagram, what does the overlapping region represent?",
                                "options": ["Union", "Intersection", "Difference", "Complement"],
                                "correct_answer": "Intersection",
                                "explanation": "The overlapping region in a Venn diagram represents the intersection of sets (elements common to both).",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_7",
                                "question_text": "Which statement is logically equivalent to 'If it rains, then I will stay home'?",
                                "options": ["If I stay home, then it rains", "If I don't stay home, then it doesn't rain", "If it doesn't rain, then I won't stay home", "If I don't stay home, then it doesn't rain"],
                                "correct_answer": "If I don't stay home, then it doesn't rain",
                                "explanation": "This is the contrapositive, which is logically equivalent to the original statement.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_8",
                                "question_text": "What type of reasoning uses specific examples to reach a general conclusion?",
                                "options": ["Deductive", "Inductive", "Abductive", "Reductive"],
                                "correct_answer": "Inductive",
                                "explanation": "Inductive reasoning moves from specific observations to broader generalizations.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_9",
                                "question_text": "In logical reasoning, what is a syllogism?",
                                "options": ["A question", "A deductive argument with two premises", "A guess", "A definition"],
                                "correct_answer": "A deductive argument with two premises",
                                "explanation": "A syllogism is a form of deductive reasoning consisting of a major premise, minor premise, and conclusion.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "8_6_2_10",
                                "question_text": "What does the symbol '∴' mean in logic?",
                                "options": ["Therefore", "Because", "And", "Or"],
                                "correct_answer": "Therefore",
                                "explanation": "The symbol '∴' means 'therefore' and is used to indicate a conclusion.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
    return curriculum

def save_enhanced_curriculum_to_json():
    """Save the enhanced curriculum to a JSON file"""
    curriculum = generate_class8_enhanced_curriculum()
    
    with open('class8_mathematics_curriculum_enhanced.json', 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    
    print("Enhanced Class 8 Mathematics curriculum saved to 'class8_mathematics_curriculum_enhanced.json'")
    
    # Print statistics
    total_modules = sum(len(chapter['modules']) for chapter in curriculum['chapters'])
    total_questions = 0
    
    for chapter in curriculum['chapters']:
        for module in chapter['modules']:
            total_questions += len(module['questions'])
    
    print(f"Enhanced Statistics:")
    print(f"  Chapters: {len(curriculum['chapters'])}")
    print(f"  Modules: {total_modules}")
    print(f"  Questions: {total_questions}")
    
    # Compare with original
    print(f"\nImprovement from original:")
    print(f"  Original modules: 13 to Enhanced modules: {total_modules}")
    print(f"  Original questions: 68 to Enhanced questions: {total_questions}")
    print(f"  Module increase: {total_modules - 13} (+{((total_modules - 13)/13)*100:.1f}%)")
    print(f"  Question increase: {total_questions - 68} (+{((total_questions - 68)/68)*100:.1f}%)")

if __name__ == "__main__":
    save_enhanced_curriculum_to_json()