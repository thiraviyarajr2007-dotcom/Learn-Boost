#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 7 Mathematics Curriculum Generator - TN State Board
Transforms textbook content into Duolingo-style learning modules
"""

import json

def generate_class7_curriculum():
    """Generate comprehensive Class 7 Mathematics curriculum"""
    
    curriculum = {
        "class": "7",
        "subject": "Mathematics",
        "chapters": [
            {
                "chapter_name": "Number System",
                "modules": [
                    {
                        "module_id": "7.1.1",
                        "topic_name": "Integers and Their Properties",
                        "explanation": "Integers are like a complete number family that includes positive numbers, negative numbers, and zero! They extend infinitely in both directions on the number line. Think of temperature: positive for hot, negative for cold, zero for freezing point. Integers help us understand gains and losses, above and below sea level, and so much more!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_1_1_1",
                                "question_text": "Which of these is NOT an integer?",
                                "options": ["-5", "0", "3.5", "12"],
                                "correct_answer": "3.5",
                                "explanation": "3.5 is not an integer because it has a decimal part. Integers are whole numbers without fractions or decimals.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_1_2",
                                "question_text": "What is the opposite of -8?",
                                "options": ["8", "-8", "0", "1"],
                                "correct_answer": "8",
                                "explanation": "The opposite (additive inverse) of -8 is 8 because -8 + 8 = 0.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_1_3",
                                "question_text": "Arrange in ascending order: -3, 0, 2, -1",
                                "options": ["-3, -1, 0, 2", "2, 0, -1, -3", "-1, -3, 0, 2", "0, -1, -3, 2"],
                                "correct_answer": "-3, -1, 0, 2",
                                "explanation": "Ascending order means from smallest to largest. Negative numbers are smaller than zero, and -3 is smaller than -1.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_1_4",
                                "question_text": "What is the absolute value of -12?",
                                "options": ["-12", "12", "0", "24"],
                                "correct_answer": "12",
                                "explanation": "The absolute value of -12 is 12. Absolute value is always positive and represents the distance from zero.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_1_5",
                                "question_text": "Which integer is closest to zero?",
                                "options": ["-10", "-3", "5", "-1"],
                                "correct_answer": "-1",
                                "explanation": "-1 is closest to zero because the absolute value | -1 | = 1, which is the smallest among the options.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_1_6",
                                "question_text": "If temperature is -5°C and rises by 3°C, what's the new temperature?",
                                "options": ["-2°C", "-8°C", "2°C", "8°C"],
                                "correct_answer": "-2°C",
                                "explanation": "-5°C + 3°C = -2°C. Starting from -5 and moving 3 units toward zero gives us -2.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "7.1.2",
                        "topic_name": "Operations on Integers",
                        "explanation": "Integer operations follow special rules! Addition: same signs add, different signs subtract. Subtraction: add the opposite. Multiplication and division: same signs give positive, different signs give negative. Think of it like a game where positive is 'gain' and negative is 'loss' - these rules help you calculate the final result!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "7_1_2_1",
                                "question_text": "What is (-7) + (-3)?",
                                "options": ["-10", "10", "-4", "4"],
                                "correct_answer": "-10",
                                "explanation": "(-7) + (-3) = -10. When adding two negative integers, add their absolute values and keep the negative sign.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_1_2_2",
                                "question_text": "What is 8 - (-5)?",
                                "options": ["3", "13", "-3", "-13"],
                                "correct_answer": "13",
                                "explanation": "8 - (-5) = 8 + 5 = 13. Subtracting a negative is the same as adding its positive.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_1_2_3",
                                "question_text": "What is (-4) × 6?",
                                "options": ["24", "-24", "10", "-10"],
                                "correct_answer": "-24",
                                "explanation": "(-4) × 6 = -24. Different signs give a negative result in multiplication.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_1_2_4",
                                "question_text": "What is (-15) ÷ (-3)?",
                                "options": ["5", "-5", "12", "-12"],
                                "correct_answer": "5",
                                "explanation": "(-15) ÷ (-3) = 5. Same signs give a positive result in division.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_1_2_5",
                                "question_text": "If a = -2 and b = 3, what is a² + b?",
                                "options": ["1", "7", "-1", "-7"],
                                "correct_answer": "1",
                                "explanation": "a² + b = (-2)² + 3 = 4 + 3 = 7. Remember that the square of a negative number is positive.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_1_2_6",
                                "question_text": "What is the result of (-2)³?",
                                "options": ["6", "-6", "8", "-8"],
                                "correct_answer": "-8",
                                "explanation": "(-2)³ = (-2) × (-2) × (-2) = 4 × (-2) = -8. Odd power of negative gives negative result.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_1_2_7",
                                "question_text": "If x = -4 and y = -1, what is x - y?",
                                "options": ["-3", "3", "-5", "5"],
                                "correct_answer": "-3",
                                "explanation": "x - y = (-4) - (-1) = (-4) + 1 = -3. Remember to add the opposite when subtracting.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    },
                    {
                        "module_id": "7.1.3",
                        "topic_name": "Fractions and Decimals",
                        "explanation": "Fractions and decimals are different ways to show parts of a whole! Fractions use numerator/denominator (like 3/4 = three-fourths), while decimals use place value (like 0.75 = seventy-five hundredths). They're like two languages saying the same thing - you can translate between them and use whichever is more convenient!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_1_3_1",
                                "question_text": "Convert 3/4 to decimal form",
                                "options": ["0.34", "0.75", "0.25", "0.43"],
                                "correct_answer": "0.75",
                                "explanation": "3/4 = 0.75. Divide 3 by 4 to get the decimal equivalent.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_3_2",
                                "question_text": "Which fraction is equivalent to 0.6?",
                                "options": ["1/6", "3/5", "6/10", "2/3"],
                                "correct_answer": "3/5",
                                "explanation": "0.6 = 6/10 = 3/5. Simplify the fraction by dividing numerator and denominator by 2.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_3_3",
                                "question_text": "What is 2.35 as a mixed fraction?",
                                "options": ["2 35/100", "2 7/20", "2 3/5", "2 1/2"],
                                "correct_answer": "2 7/20",
                                "explanation": "2.35 = 2 + 0.35 = 2 + 35/100 = 2 + 7/20 = 2 7/20. Simplify 35/100 by dividing by 5.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_3_4",
                                "question_text": "Arrange in descending order: 1/2, 0.75, 1/4, 0.9",
                                "options": ["0.9, 0.75, 1/2, 1/4", "0.75, 0.9, 1/2, 1/4", "1/2, 0.75, 0.9, 1/4", "0.9, 1/2, 0.75, 1/4"],
                                "correct_answer": "0.9, 0.75, 1/2, 1/4",
                                "explanation": "Convert all to decimals: 0.9, 0.75, 0.5, 0.25. Then arrange from largest to smallest.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_3_5",
                                "question_text": "What is 0.125 as a fraction in simplest form?",
                                "options": ["1/8", "1/4", "1/5", "5/8"],
                                "correct_answer": "1/8",
                                "explanation": "0.125 = 125/1000 = 1/8. Divide numerator and denominator by 125 to simplify.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_1_3_6",
                                "question_text": "If you eat 3/8 of a pizza, what fraction remains?",
                                "options": ["5/8", "3/8", "1/2", "1/4"],
                                "correct_answer": "5/8",
                                "explanation": "Remaining fraction = 1 - 3/8 = 8/8 - 3/8 = 5/8.",
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
                        "module_id": "7.2.1",
                        "topic_name": "Area and Perimeter",
                        "explanation": "Area is the space inside a shape (like carpet covering a floor), while perimeter is the distance around the edge (like fence around a garden). Rectangle: Area = length × width, Perimeter = 2 × (length + width). Square: Area = side², Perimeter = 4 × side. These measurements help in construction, landscaping, and everyday planning!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_2_1_1",
                                "question_text": "What is the area of a rectangle with length 8 cm and width 5 cm?",
                                "options": ["13 cm²", "40 cm²", "26 cm²", "16 cm²"],
                                "correct_answer": "40 cm²",
                                "explanation": "Area = length × width = 8 cm × 5 cm = 40 cm².",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_2_1_2",
                                "question_text": "What is the perimeter of a square with side 6 m?",
                                "options": ["24 m", "36 m", "12 m", "18 m"],
                                "correct_answer": "24 m",
                                "explanation": "Perimeter of square = 4 × side = 4 × 6 m = 24 m.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_2_1_3",
                                "question_text": "If a rectangle has perimeter 30 cm and length 10 cm, what is its width?",
                                "options": ["5 cm", "10 cm", "15 cm", "20 cm"],
                                "correct_answer": "5 cm",
                                "explanation": "Perimeter = 2 × (length + width). 30 = 2 × (10 + width). 15 = 10 + width. Width = 5 cm.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_2_1_4",
                                "question_text": "Which shape has the largest area if both have perimeter 20 cm: square or rectangle 8 cm × 2 cm?",
                                "options": ["Square", "Rectangle", "Both equal", "Cannot determine"],
                                "correct_answer": "Square",
                                "explanation": "Square with perimeter 20 cm has side 5 cm, area = 25 cm². Rectangle area = 8 × 2 = 16 cm². Square has larger area.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_2_1_5",
                                "question_text": "What is the area of a square field with perimeter 80 m?",
                                "options": ["400 m²", "1600 m²", "6400 m²", "100 m²"],
                                "correct_answer": "400 m²",
                                "explanation": "Side = perimeter ÷ 4 = 80 ÷ 4 = 20 m. Area = side² = 20² = 400 m².",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "7.2.2",
                        "topic_name": "Volume and Surface Area",
                        "explanation": "Volume is the space inside a 3D shape (how much it can hold), while surface area is the total area of all faces (how much material needed to cover it). Cube: Volume = side³, Surface Area = 6 × side². These concepts are crucial for packaging, construction, and understanding capacity of containers!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "7_2_2_1",
                                "question_text": "What is the volume of a cube with side 4 cm?",
                                "options": ["16 cm³", "64 cm³", "24 cm³", "12 cm³"],
                                "correct_answer": "64 cm³",
                                "explanation": "Volume of cube = side³ = 4³ = 4 × 4 × 4 = 64 cm³.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_2_2_2",
                                "question_text": "What is the surface area of a cube with side 3 cm?",
                                "options": ["54 cm²", "36 cm²", "9 cm²", "27 cm²"],
                                "correct_answer": "54 cm²",
                                "explanation": "Surface area = 6 × side² = 6 × 3² = 6 × 9 = 54 cm².",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_2_2_3",
                                "question_text": "If a cuboid has dimensions 5 cm × 3 cm × 2 cm, what is its volume?",
                                "options": ["30 cm³", "10 cm³", "15 cm³", "60 cm³"],
                                "correct_answer": "30 cm³",
                                "explanation": "Volume of cuboid = length × width × height = 5 × 3 × 2 = 30 cm³.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_2_2_4",
                                "question_text": "How many small cubes of side 2 cm can fit in a box of size 8 cm × 6 cm × 4 cm?",
                                "options": ["12", "24", "48", "96"],
                                "correct_answer": "24",
                                "explanation": "Box volume = 8 × 6 × 4 = 192 cm³. Small cube volume = 2³ = 8 cm³. Number = 192 ÷ 8 = 24.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_2_2_5",
                                "question_text": "If the surface area of a cube is 150 cm², what is the length of each side?",
                                "options": ["5 cm", "25 cm", "10 cm", "2.5 cm"],
                                "correct_answer": "5 cm",
                                "explanation": "Surface area = 6 × side². 150 = 6 × side². side² = 25. side = 5 cm.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Algebra",
                "modules": [
                    {
                        "module_id": "7.3.1",
                        "topic_name": "Algebraic Expressions",
                        "explanation": "Algebraic expressions are mathematical phrases with variables! They combine numbers, variables, and operations like 2x + 3y - 5. Variables are like mystery boxes that can hold different values. These expressions help us describe patterns and solve problems where exact numbers aren't known yet. Think of them as recipes for calculations!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_3_1_1",
                                "question_text": "In the expression 3x - 7, what is the constant term?",
                                "options": ["3", "x", "-7", "3x"],
                                "correct_answer": "-7",
                                "explanation": "The constant term is -7 because it doesn't contain any variable. 3x is the variable term.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_3_1_2",
                                "question_text": "If x = 4, what is the value of 2x + 5?",
                                "options": ["13", "21", "8", "17"],
                                "correct_answer": "13",
                                "explanation": "2x + 5 = 2(4) + 5 = 8 + 5 = 13. Substitute x = 4 and calculate.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_3_1_3",
                                "question_text": "How many terms are in the expression 4x² - 3xy + 2y - 7?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "4",
                                "explanation": "The expression has 4 terms: 4x², -3xy, 2y, and -7. Each term is separated by + or - signs.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_3_1_4",
                                "question_text": "What is the coefficient of x in the expression 5x² - 2x + 8?",
                                "options": ["5", "-2", "8", "0"],
                                "correct_answer": "-2",
                                "explanation": "The coefficient of x is -2. 5 is the coefficient of x², and 8 is the constant term.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_3_1_5",
                                "question_text": "If a = 3 and b = 2, what is a² + 2ab?",
                                "options": ["15", "21", "12", "18"],
                                "correct_answer": "21",
                                "explanation": "a² + 2ab = 3² + 2(3)(2) = 9 + 12 = 21.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "7.3.2",
                        "topic_name": "Linear Equations",
                        "explanation": "Linear equations are like balance scales where we need to find the unknown value! They have variables to the power of 1, like 2x + 3 = 11. We solve them by doing the same operation to both sides to keep the balance. It's like a detective game where x is the mystery we need to uncover!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "7_3_2_1",
                                "question_text": "What is the solution to x + 7 = 15?",
                                "options": ["x = 8", "x = 22", "x = -8", "x = 2"],
                                "correct_answer": "x = 8",
                                "explanation": "x + 7 = 15. Subtract 7 from both sides: x = 15 - 7 = 8.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_3_2_2",
                                "question_text": "Solve for x: 3x - 4 = 11",
                                "options": ["x = 5", "x = 7", "x = 3", "x = 15"],
                                "correct_answer": "x = 5",
                                "explanation": "3x - 4 = 11. Add 4 to both sides: 3x = 15. Divide by 3: x = 5.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_3_2_3",
                                "question_text": "What is the value of x in 2x + 3 = x + 8?",
                                "options": ["x = 5", "x = 11", "x = -5", "x = 1"],
                                "correct_answer": "x = 5",
                                "explanation": "2x + 3 = x + 8. Subtract x from both sides: x + 3 = 8. Subtract 3: x = 5.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_3_2_4",
                                "question_text": "If 4(x - 2) = 12, what is x?",
                                "options": ["x = 5", "x = 8", "x = 1", "x = 3"],
                                "correct_answer": "x = 5",
                                "explanation": "4(x - 2) = 12. Divide by 4: x - 2 = 3. Add 2: x = 5.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_3_2_5",
                                "question_text": "The sum of a number and 5 is 20. What is the number?",
                                "options": ["15", "25", "10", "20"],
                                "correct_answer": "15",
                                "explanation": "Let the number be x. x + 5 = 20. x = 20 - 5 = 15.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_3_2_6",
                                "question_text": "If 3x - 7 = 2x + 1, what is x?",
                                "options": ["x = 8", "x = 6", "x = 4", "x = 10"],
                                "correct_answer": "x = 8",
                                "explanation": "3x - 7 = 2x + 1. Subtract 2x from both sides: x - 7 = 1. Add 7: x = 8.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Direct and Inverse Proportion",
                "modules": [
                    {
                        "module_id": "7.4.1",
                        "topic_name": "Direct Proportion",
                        "explanation": "Direct proportion is like a perfect partnership - when one quantity increases, the other increases by the same ratio! If you buy twice as many apples, you pay twice as much. The relationship is y = kx, where k is constant. This helps in cooking recipes, speed-distance problems, and many real-life situations!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_4_1_1",
                                "question_text": "If 5 pens cost ₹40, how much do 8 pens cost?",
                                "options": ["₹64", "₹48", "₹56", "₹72"],
                                "correct_answer": "₹64",
                                "explanation": "Cost is directly proportional to number of pens. 5 pens = ₹40, so 1 pen = ₹8. 8 pens = 8 × ₹8 = ₹64.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_4_1_2",
                                "question_text": "A car travels 180 km in 3 hours. How far will it travel in 5 hours at the same speed?",
                                "options": ["300 km", "250 km", "350 km", "400 km"],
                                "correct_answer": "300 km",
                                "explanation": "Speed = 180 ÷ 3 = 60 km/hour. In 5 hours: 60 × 5 = 300 km.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_4_1_3",
                                "question_text": "If 6 workers can complete a job in 10 days, how many workers are needed to complete it in 5 days?",
                                "options": ["12", "8", "15", "20"],
                                "correct_answer": "12",
                                "explanation": "Work is inversely proportional to workers. 6 × 10 = 60 worker-days. For 5 days: 60 ÷ 5 = 12 workers.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_4_1_4",
                                "question_text": "The cost of 3 kg of rice is ₹120. What is the cost of 7 kg?",
                                "options": ["₹280", "₹240", "₹320", "₹200"],
                                "correct_answer": "₹280",
                                "explanation": "Cost per kg = ₹120 ÷ 3 = ₹40. For 7 kg: 7 × ₹40 = ₹280.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_4_1_5",
                                "question_text": "If a machine produces 240 items in 4 hours, how many items will it produce in 7 hours?",
                                "options": ["420", "360", "480", "560"],
                                "correct_answer": "420",
                                "explanation": "Production rate = 240 ÷ 4 = 60 items/hour. In 7 hours: 60 × 7 = 420 items.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "7.4.2",
                        "topic_name": "Inverse Proportion",
                        "explanation": "Inverse proportion is like a seesaw - when one quantity goes up, the other goes down! If more workers share the same job, it takes less time. The relationship is xy = k (constant). This applies to speed-time, worker-time problems, and resource allocation scenarios!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "7_4_2_1",
                                "question_text": "If 8 machines can complete a task in 6 days, how many days will 12 machines take?",
                                "options": ["4 days", "3 days", "9 days", "5 days"],
                                "correct_answer": "4 days",
                                "explanation": "Work = machines × days = 8 × 6 = 48 machine-days. With 12 machines: 48 ÷ 12 = 4 days.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_4_2_2",
                                "question_text": "A car travels at 60 km/hour and takes 4 hours for a journey. How long will it take at 80 km/hour?",
                                "options": ["3 hours", "2.5 hours", "5 hours", "3.5 hours"],
                                "correct_answer": "3 hours",
                                "explanation": "Distance = speed × time = 60 × 4 = 240 km. At 80 km/hour: 240 ÷ 80 = 3 hours.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_4_2_3",
                                "question_text": "If 15 students can clean a room in 20 minutes, how many students are needed to clean it in 12 minutes?",
                                "options": ["25", "20", "30", "18"],
                                "correct_answer": "25",
                                "explanation": "Work = students × minutes = 15 × 20 = 300 student-minutes. For 12 minutes: 300 ÷ 12 = 25 students.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_4_2_4",
                                "question_text": "A water tank fills in 8 hours with 3 pipes. How long will it take with 4 pipes?",
                                "options": ["6 hours", "4 hours", "10 hours", "12 hours"],
                                "correct_answer": "6 hours",
                                "explanation": "Work = pipes × hours = 3 × 8 = 24 pipe-hours. With 4 pipes: 24 ÷ 4 = 6 hours.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_4_2_5",
                                "question_text": "If 6 people can paint a fence in 10 days, how many days will 4 people take?",
                                "options": ["15 days", "12 days", "8 days", "20 days"],
                                "correct_answer": "15 days",
                                "explanation": "Work = people × days = 6 × 10 = 60 person-days. With 4 people: 60 ÷ 4 = 15 days.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Geometry",
                "modules": [
                    {
                        "module_id": "7.5.1",
                        "topic_name": "Lines and Angles",
                        "explanation": "Lines and angles are the building blocks of geometry! Lines can be parallel (never meet) or intersecting. Angles measure rotation: acute (< 90°), right (90°), obtuse (> 90°, < 180°), straight (180°), reflex (> 180°, < 360°). Understanding these helps in construction, design, and navigation!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_5_1_1",
                                "question_text": "What type of angle is 120°?",
                                "options": ["Acute", "Right", "Obtuse", "Straight"],
                                "correct_answer": "Obtuse",
                                "explanation": "120° is an obtuse angle because it's greater than 90° but less than 180°.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_5_1_2",
                                "question_text": "If two lines are parallel, what can we say about them?",
                                "options": ["They intersect at one point", "They never intersect", "They intersect at many points", "They are perpendicular"],
                                "correct_answer": "They never intersect",
                                "explanation": "Parallel lines are always the same distance apart and never intersect, no matter how far they extend.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_5_1_3",
                                "question_text": "What is the complement of 35°?",
                                "options": ["55°", "65°", "145°", "125°"],
                                "correct_answer": "55°",
                                "explanation": "Complementary angles add up to 90°. So complement of 35° = 90° - 35° = 55°.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_5_1_4",
                                "question_text": "What is the supplement of 110°?",
                                "options": ["70°", "80°", "90°", "100°"],
                                "correct_answer": "70°",
                                "explanation": "Supplementary angles add up to 180°. So supplement of 110° = 180° - 110° = 70°.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_5_1_5",
                                "question_text": "If two angles are vertically opposite and one is 45°, what is the other?",
                                "options": ["45°", "135°", "90°", "180°"],
                                "correct_answer": "45°",
                                "explanation": "Vertically opposite angles are always equal. So the other angle is also 45°.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "7.5.2",
                        "topic_name": "Triangles and Their Properties",
                        "explanation": "Triangles are amazing shapes with special properties! By sides: equilateral (all equal), isosceles (two equal), scalene (all different). By angles: acute (all < 90°), right (one = 90°), obtuse (one > 90°). The sum of angles is always 180°. These properties help in construction, engineering, and art!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_5_2_1",
                                "question_text": "In an equilateral triangle, what is each angle?",
                                "options": ["45°", "60°", "90°", "120°"],
                                "correct_answer": "60°",
                                "explanation": "In an equilateral triangle, all angles are equal. Since sum is 180°, each angle = 180° ÷ 3 = 60°.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_5_2_2",
                                "question_text": "If two angles of a triangle are 50° and 60°, what is the third angle?",
                                "options": ["50°", "60°", "70°", "80°"],
                                "correct_answer": "70°",
                                "explanation": "Third angle = 180° - (50° + 60°) = 180° - 110° = 70°.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_5_2_3",
                                "question_text": "Which triangle has exactly two equal sides?",
                                "options": ["Equilateral", "Isosceles", "Scalene", "Right"],
                                "correct_answer": "Isosceles",
                                "explanation": "An isosceles triangle has exactly two equal sides and two equal angles.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_5_2_4",
                                "question_text": "What makes a triangle a right triangle?",
                                "options": ["All angles are 90°", "One angle is 90°", "Two angles are 90°", "No angles are 90°"],
                                "correct_answer": "One angle is 90°",
                                "explanation": "A right triangle has exactly one angle that measures 90 degrees.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_5_2_5",
                                "question_text": "In a right triangle, if one acute angle is 30°, what is the other acute angle?",
                                "options": ["30°", "45°", "60°", "90°"],
                                "correct_answer": "60°",
                                "explanation": "Other acute angle = 180° - 90° - 30° = 60°.",
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
                        "module_id": "7.6.1",
                        "topic_name": "Data Handling and Representation",
                        "explanation": "Data handling is like being a detective with numbers! We collect, organize, and interpret data to find patterns. Data can be shown in tables, bar graphs, pie charts, or line graphs. Each type has its strengths - tables for exact values, graphs for visual patterns. This helps in making informed decisions!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "7_6_1_1",
                                "question_text": "What is the first step in data handling?",
                                "options": ["Drawing graphs", "Collecting data", "Calculating averages", "Making conclusions"],
                                "correct_answer": "Collecting data",
                                "explanation": "The first step is collecting relevant data. Without data, we can't do any analysis.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "7_6_1_2",
                                "question_text": "Which graph is best for showing parts of a whole?",
                                "options": ["Bar graph", "Line graph", "Pie chart", "Scatter plot"],
                                "correct_answer": "Pie chart",
                                "explanation": "Pie charts are best for showing how a whole is divided into parts or percentages.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "7_6_1_3",
                                "question_text": "What is the mode of the data: 2, 3, 5, 3, 4, 3, 6?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "explanation": "The mode is the value that appears most frequently. 3 appears 3 times, more than any other number.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "7_6_1_4",
                                "question_text": "What is the median of: 7, 2, 9, 4, 6?",
                                "options": ["4", "6", "7", "9"],
                                "correct_answer": "6",
                                "explanation": "Arrange in order: 2, 4, 6, 7, 9. The median (middle value) is 6.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "7_6_1_5",
                                "question_text": "Which type of graph shows trends over time?",
                                "options": ["Bar graph", "Pie chart", "Line graph", "Pictograph"],
                                "correct_answer": "Line graph",
                                "explanation": "Line graphs are excellent for showing how data changes over time or trends.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "7.6.2",
                        "topic_name": "Probability Basics",
                        "explanation": "Probability is like predicting the future with math! It measures how likely something is to happen, from 0 (impossible) to 1 (certain). Probability = (Number of favorable outcomes) ÷ (Total possible outcomes). It helps in games, weather forecasting, and decision-making!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_6_2_1",
                                "question_text": "What is the probability of getting heads when tossing a fair coin?",
                                "options": ["0", "1/2", "1", "1/4"],
                                "correct_answer": "1/2",
                                "explanation": "A fair coin has 2 equally likely outcomes (heads or tails). P(heads) = 1/2.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_6_2_2",
                                "question_text": "If you roll a die, what's the probability of getting an even number?",
                                "options": ["1/6", "1/3", "1/2", "2/3"],
                                "correct_answer": "1/2",
                                "explanation": "Even numbers on a die: 2, 4, 6 (3 outcomes). Total outcomes: 6. P(even) = 3/6 = 1/2.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_6_2_3",
                                "question_text": "What is the probability of an impossible event?",
                                "options": ["0", "1/2", "1", "Cannot determine"],
                                "correct_answer": "0",
                                "explanation": "An impossible event has probability 0 because it can never happen.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_6_2_4",
                                "question_text": "If a bag contains 3 red and 2 blue balls, what's the probability of drawing a red ball?",
                                "options": ["3/5", "2/5", "1/2", "3/2"],
                                "correct_answer": "3/5",
                                "explanation": "Red balls = 3, Total balls = 5. P(red) = 3/5.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_6_2_5",
                                "question_text": "What is the probability of a certain event?",
                                "options": ["0", "1/2", "1", "Cannot determine"],
                                "correct_answer": "1",
                                "explanation": "A certain event is guaranteed to happen, so its probability is 1.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Percentage and Simple Interest",
                "modules": [
                    {
                        "module_id": "7.7.1",
                        "topic_name": "Percentage Calculations",
                        "explanation": "Percentage is like a universal language for comparing quantities! It means 'per hundred' - 25% means 25 out of 100. To convert fraction to percentage, multiply by 100. To find percentage of a number, multiply the number by the percentage ÷ 100. This helps in discounts, grades, and statistics!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "7_7_1_1",
                                "question_text": "What is 25% of 80?",
                                "options": ["20", "25", "30", "40"],
                                "correct_answer": "20",
                                "explanation": "25% of 80 = 80 × (25/100) = 80 × 0.25 = 20.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_7_1_2",
                                "question_text": "Convert 3/4 to percentage",
                                "options": ["25%", "50%", "75%", "80%"],
                                "correct_answer": "75%",
                                "explanation": "3/4 = 0.75 = 75%. Multiply by 100 to convert fraction to percentage.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_7_1_3",
                                "question_text": "If 40 students took a test and 32 passed, what percentage passed?",
                                "options": ["70%", "75%", "80%", "85%"],
                                "correct_answer": "80%",
                                "explanation": "Percentage passed = (32/40) × 100 = 0.8 × 100 = 80%.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_7_1_4",
                                "question_text": "What is 15% of 200?",
                                "options": ["30", "25", "35", "40"],
                                "correct_answer": "30",
                                "explanation": "15% of 200 = 200 × (15/100) = 200 × 0.15 = 30.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "7_7_1_5",
                                "question_text": "A price increased from ₹50 to ₹60. What is the percentage increase?",
                                "options": ["10%", "15%", "20%", "25%"],
                                "correct_answer": "20%",
                                "explanation": "Increase = ₹60 - ₹50 = ₹10. Percentage increase = (10/50) × 100 = 20%.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "7.7.2",
                        "topic_name": "Simple Interest",
                        "explanation": "Simple interest is like earning rent on money! It's calculated only on the original amount (principal). Formula: SI = (P × R × T) ÷ 100, where P is principal, R is rate per year, T is time in years. This helps in understanding bank loans, savings accounts, and financial planning!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "7_7_2_1",
                                "question_text": "What is the simple interest on ₹1000 for 2 years at 5% per annum?",
                                "options": ["₹50", "₹100", "₹150", "₹200"],
                                "correct_answer": "₹100",
                                "explanation": "SI = (1000 × 5 × 2) ÷ 100 = 10000 ÷ 100 = ₹100.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_7_2_2",
                                "question_text": "If simple interest on ₹500 for 3 years is ₹90, what is the rate of interest?",
                                "options": ["4%", "5%", "6%", "7%"],
                                "correct_answer": "6%",
                                "explanation": "90 = (500 × R × 3) ÷ 100. 90 × 100 = 1500 × R. 9000 = 1500 × R. R = 6%.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_7_2_3",
                                "question_text": "At what rate will ₹2000 amount to ₹2400 in 2 years with simple interest?",
                                "options": ["8%", "10%", "12%", "15%"],
                                "correct_answer": "10%",
                                "explanation": "Interest = ₹2400 - ₹2000 = ₹400. 400 = (2000 × R × 2) ÷ 100. 40000 = 4000 × R. R = 10%.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_7_2_4",
                                "question_text": "How long will it take for ₹1500 to earn ₹300 interest at 8% per annum?",
                                "options": ["2 years", "2.5 years", "3 years", "4 years"],
                                "correct_answer": "2.5 years",
                                "explanation": "300 = (1500 × 8 × T) ÷ 100. 30000 = 12000 × T. T = 2.5 years.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "7_7_2_5",
                                "question_text": "What amount will ₹800 become in 3 years at 6% simple interest?",
                                "options": ["₹944", "₹960", "₹1000", "₹1050"],
                                "correct_answer": "₹944",
                                "explanation": "SI = (800 × 6 × 3) ÷ 100 = 14400 ÷ 100 = ₹144. Amount = 800 + 144 = ₹944.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
    return curriculum

def save_curriculum_to_json():
    """Save the curriculum to a JSON file"""
    curriculum = generate_class7_curriculum()
    
    with open('class7_mathematics_curriculum.json', 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    
    print("Class 7 Mathematics curriculum saved to 'class7_mathematics_curriculum.json'")
    
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
    save_curriculum_to_json()