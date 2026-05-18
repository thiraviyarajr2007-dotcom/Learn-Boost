#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 6 Mathematics Curriculum Generator - TN State Board
Transforms textbook content into Duolingo-style learning modules
"""

import json

def generate_class6_curriculum():
    """Generate comprehensive Class 6 Mathematics curriculum"""
    
    curriculum = {
        "class": "6",
        "subject": "Mathematics",
        "chapters": [
            {
                "chapter_name": "Numbers",
                "modules": [
                    {
                        "module_id": "6.1.1",
                        "topic_name": "Prime and Composite Numbers",
                        "explanation": "Numbers are like building blocks! Prime numbers are special numbers that can only be divided by 1 and themselves (like 2, 3, 5, 7). Composite numbers have more factors (like 4, 6, 8, 9). Think of prime numbers as 'lonely' numbers that only like themselves and 1 as friends!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "6_1_1_1",
                                "question_text": "Which of these is a prime number?",
                                "options": ["4", "6", "7", "9"],
                                "correct_answer": "7",
                                "explanation": "7 is prime because it can only be divided by 1 and 7. The others can be divided by other numbers too.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_1_1_2",
                                "question_text": "What makes a number composite?",
                                "options": ["Only divisible by 1 and itself", "Has more than two factors", "Is an odd number", "Is greater than 10"],
                                "correct_answer": "Has more than two factors",
                                "explanation": "Composite numbers have more than two factors, unlike prime numbers which only have two factors (1 and itself).",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_1_1_3",
                                "question_text": "Which number is NOT prime?",
                                "options": ["11", "13", "15", "17"],
                                "correct_answer": "15",
                                "explanation": "15 is not prime because it can be divided by 1, 3, 5, and 15. It has more than two factors.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_1_1_4",
                                "question_text": "How many prime numbers are there between 1 and 10?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "4",
                                "explanation": "The prime numbers between 1 and 10 are 2, 3, 5, and 7. That's 4 prime numbers!",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_1_1_5",
                                "question_text": "What is the smallest prime number?",
                                "options": ["0", "1", "2", "3"],
                                "correct_answer": "2",
                                "explanation": "2 is the smallest prime number. It's also the only even prime number!",
                                "timer_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "6.1.2",
                        "topic_name": "Rules for Test of Divisibility",
                        "explanation": "Divisibility rules are like magic tricks to quickly check if a number can be divided by another! For 2: last digit must be even (0,2,4,6,8). For 3: sum of digits must be divisible by 3. For 5: last digit must be 0 or 5. For 10: last digit must be 0. These rules save time in math!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "6_1_2_1",
                                "question_text": "Which number is divisible by 2?",
                                "options": ["123", "247", "456", "789"],
                                "correct_answer": "456",
                                "explanation": "456 is divisible by 2 because its last digit (6) is even. Even numbers end in 0,2,4,6,8.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_2_2",
                                "question_text": "Is 123 divisible by 3?",
                                "options": ["Yes, because 1+2+3=6", "No, because it's odd", "Yes, because it ends with 3", "No, because 1+2+3=6"],
                                "correct_answer": "Yes, because 1+2+3=6",
                                "explanation": "123 is divisible by 3 because the sum of its digits (1+2+3=6) is divisible by 3.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_2_3",
                                "question_text": "Which number is divisible by both 2 and 5?",
                                "options": ["25", "30", "35", "40"],
                                "correct_answer": "30",
                                "explanation": "30 is divisible by both 2 (ends with 0) and 5 (ends with 0). Numbers divisible by both 2 and 5 must end with 0.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_2_4",
                                "question_text": "What is the divisibility rule for 9?",
                                "options": ["Last digit must be 9", "Sum of digits must be divisible by 9", "Number must be odd", "First digit must be 9"],
                                "correct_answer": "Sum of digits must be divisible by 9",
                                "explanation": "A number is divisible by 9 if the sum of its digits is divisible by 9. For example, 189: 1+8+9=18, and 18 is divisible by 9.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_2_5",
                                "question_text": "Which number is NOT divisible by 4?",
                                "options": ["124", "236", "348", "459"],
                                "correct_answer": "459",
                                "explanation": "459 is not divisible by 4 because its last two digits (59) are not divisible by 4. The rule for 4: last two digits must be divisible by 4.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_2_6",
                                "question_text": "Is 1000 divisible by 8?",
                                "options": ["Yes, last 3 digits are 000", "No, it's too big", "Yes, it ends with 0", "No, sum is 1"],
                                "correct_answer": "Yes, last 3 digits are 000",
                                "explanation": "1000 is divisible by 8 because its last three digits (000) are divisible by 8. The rule for 8: last three digits must be divisible by 8.",
                                "timer_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "6.1.3",
                        "topic_name": "Prime Factorisation",
                        "explanation": "Prime factorisation is like breaking down a number into its smallest prime building blocks! It's like finding the DNA of a number. For example, 12 = 2 × 2 × 3. We use factor trees or division method to find these prime factors. Every number has a unique prime factorisation!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "6_1_3_1",
                                "question_text": "What is the prime factorisation of 12?",
                                "options": ["2 × 6", "3 × 4", "2 × 2 × 3", "1 × 12"],
                                "correct_answer": "2 × 2 × 3",
                                "explanation": "The prime factorisation of 12 is 2 × 2 × 3. We break it down until all factors are prime numbers.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_3_2",
                                "question_text": "Which of these is the prime factorisation of 18?",
                                "options": ["2 × 9", "3 × 6", "2 × 3 × 3", "1 × 18"],
                                "correct_answer": "2 × 3 × 3",
                                "explanation": "18 = 2 × 3 × 3. We break it down: 18 = 2 × 9, then 9 = 3 × 3, so 18 = 2 × 3 × 3.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_3_3",
                                "question_text": "How many prime factors does 30 have?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "explanation": "30 = 2 × 3 × 5, so it has 3 prime factors: 2, 3, and 5.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_3_4",
                                "question_text": "What is the prime factorisation of 100?",
                                "options": ["2 × 2 × 5 × 5", "10 × 10", "4 × 25", "2 × 50"],
                                "correct_answer": "2 × 2 × 5 × 5",
                                "explanation": "100 = 2 × 2 × 5 × 5. We break it down: 100 = 10 × 10 = (2 × 5) × (2 × 5) = 2 × 2 × 5 × 5.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_1_3_5",
                                "question_text": "Which number has prime factorisation 2 × 2 × 2?",
                                "options": ["4", "6", "8", "12"],
                                "correct_answer": "8",
                                "explanation": "8 = 2 × 2 × 2. When we multiply 2 × 2 × 2, we get 8.",
                                "timer_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "6.1.4",
                        "topic_name": "HCF and LCM",
                        "explanation": "HCF (Highest Common Factor) is the biggest number that divides two or more numbers. LCM (Least Common Multiple) is the smallest number that two or more numbers divide into. Think of HCF as the 'greatest common divisor' and LCM as the 'smallest common multiple'. Use prime factorisation to find both!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "6_1_4_1",
                                "question_text": "What is the HCF of 12 and 18?",
                                "options": ["2", "3", "6", "12"],
                                "correct_answer": "6",
                                "explanation": "The HCF of 12 and 18 is 6. Factors of 12: 1,2,3,4,6,12. Factors of 18: 1,2,3,6,9,18. The highest common factor is 6.",
                                "timer_seconds": 60
                            },
                            {
                                "question_id": "6_1_4_2",
                                "question_text": "What is the LCM of 4 and 6?",
                                "options": ["12", "24", "8", "10"],
                                "correct_answer": "12",
                                "explanation": "The LCM of 4 and 6 is 12. Multiples of 4: 4,8,12,16... Multiples of 6: 6,12,18... The least common multiple is 12.",
                                "timer_seconds": 60
                            },
                            {
                                "question_id": "6_1_4_3",
                                "question_text": "If HCF of two numbers is 4 and LCM is 24, what could the numbers be?",
                                "options": ["4 and 24", "8 and 12", "6 and 16", "2 and 48"],
                                "correct_answer": "8 and 12",
                                "explanation": "8 and 12 have HCF = 4 and LCM = 24. Check: factors of 8: 1,2,4,8; factors of 12: 1,2,3,4,6,12. HCF = 4. Multiples of 8: 8,16,24... Multiples of 12: 12,24... LCM = 24.",
                                "timer_seconds": 60
                            },
                            {
                                "question_id": "6_1_4_4",
                                "question_text": "What is the HCF of 15, 25, and 35?",
                                "options": ["1", "5", "15", "25"],
                                "correct_answer": "5",
                                "explanation": "The HCF of 15, 25, and 35 is 5. All three numbers are divisible by 5, and 5 is the highest number that divides all three.",
                                "timer_seconds": 60
                            },
                            {
                                "question_id": "6_1_4_5",
                                "question_text": "Two bells ring every 15 and 20 minutes. When will they ring together?",
                                "options": ["Every 5 minutes", "Every 60 minutes", "Every 35 minutes", "Every 300 minutes"],
                                "correct_answer": "Every 60 minutes",
                                "explanation": "They will ring together every LCM(15,20) = 60 minutes. 15 = 3×5, 20 = 2²×5, so LCM = 2²×3×5 = 60.",
                                "timer_seconds": 60
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Measurements",
                "modules": [
                    {
                        "module_id": "6.2.1",
                        "topic_name": "Metric System Conversions",
                        "explanation": "The metric system is like a family of measurements that work together! Length: km→hm→dam→m→dm→cm→mm (each step is ×10 or ÷10). Weight: t→q→kg→hg→dag→g→dg→cg→mg. Capacity: kl→hl→dal→l→dl→cl→ml. Remember: King Henry Died By Drinking Chocolate Milk!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "6_2_1_1",
                                "question_text": "How many meters are in 3 kilometers?",
                                "options": ["30", "300", "3000", "0.3"],
                                "correct_answer": "3000",
                                "explanation": "1 km = 1000 m, so 3 km = 3000 m. To convert km to m, multiply by 1000.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_2_1_2",
                                "question_text": "Convert 2500 grams to kilograms",
                                "options": ["0.25 kg", "2.5 kg", "25 kg", "250 kg"],
                                "correct_answer": "2.5 kg",
                                "explanation": "1000 g = 1 kg, so 2500 g = 2.5 kg. To convert grams to kilograms, divide by 1000.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_2_1_3",
                                "question_text": "How many centimeters are in 2.5 meters?",
                                "options": ["25", "250", "0.25", "2500"],
                                "correct_answer": "250",
                                "explanation": "1 m = 100 cm, so 2.5 m = 250 cm. To convert meters to centimeters, multiply by 100.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_2_1_4",
                                "question_text": "Convert 3.75 liters to milliliters",
                                "options": ["375 ml", "3750 ml", "37.5 ml", "0.375 ml"],
                                "correct_answer": "3750 ml",
                                "explanation": "1 L = 1000 ml, so 3.75 L = 3750 ml. To convert liters to milliliters, multiply by 1000.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_2_1_5",
                                "question_text": "Which is heavier: 2 kg or 2000 g?",
                                "options": ["2 kg", "2000 g", "They are equal", "Cannot determine"],
                                "correct_answer": "They are equal",
                                "explanation": "2 kg = 2000 g. They are exactly the same weight, just expressed in different units.",
                                "timer_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "6.2.2",
                        "topic_name": "Measures of Time",
                        "explanation": "Time measurement helps us organize our day! 60 seconds = 1 minute, 60 minutes = 1 hour, 24 hours = 1 day. For larger units: 7 days = 1 week, about 30 days = 1 month, 12 months = 1 year, 365 days = 1 year (366 in leap year). Time conversion helps in planning and scheduling!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "6_2_2_1",
                                "question_text": "How many minutes are in 3 hours?",
                                "options": ["60", "120", "180", "240"],
                                "correct_answer": "180",
                                "explanation": "1 hour = 60 minutes, so 3 hours = 3 × 60 = 180 minutes.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_2_2_2",
                                "question_text": "Convert 150 seconds to minutes",
                                "options": ["1.5 minutes", "2 minutes", "2.5 minutes", "3 minutes"],
                                "correct_answer": "2.5 minutes",
                                "explanation": "60 seconds = 1 minute, so 150 seconds = 150 ÷ 60 = 2.5 minutes.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_2_2_3",
                                "question_text": "How many days are in 2 weeks?",
                                "options": ["7", "14", "21", "28"],
                                "correct_answer": "14",
                                "explanation": "1 week = 7 days, so 2 weeks = 2 × 7 = 14 days.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_2_2_4",
                                "question_text": "If a movie starts at 2:30 PM and lasts 2 hours 15 minutes, when does it end?",
                                "options": ["4:15 PM", "4:30 PM", "4:45 PM", "5:00 PM"],
                                "correct_answer": "4:45 PM",
                                "explanation": "2:30 PM + 2 hours 15 minutes = 4:45 PM. Add 2 hours to get 4:30 PM, then add 15 more minutes.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_2_2_5",
                                "question_text": "How many hours are in a day?",
                                "options": ["12", "24", "36", "48"],
                                "correct_answer": "24",
                                "explanation": "There are 24 hours in one day. This is divided into day and night periods.",
                                "timer_seconds": 30
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Life Mathematics",
                "modules": [
                    {
                        "module_id": "6.3.1",
                        "topic_name": "Bill and Shopping",
                        "explanation": "Shopping bills are like treasure maps that show what you bought and how much you paid! A bill includes: date, items purchased, quantity, price per item, total cost, and sometimes tax. Understanding bills helps you manage money wisely and check if you're charged correctly. Always check your bill before paying!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "6_3_1_1",
                                "question_text": "If you buy 3 notebooks at ₹20 each, what is the total cost?",
                                "options": ["₹20", "₹40", "₹60", "₹80"],
                                "correct_answer": "₹60",
                                "explanation": "3 × ₹20 = ₹60. Multiply the quantity by the price per item to get the total cost.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_3_1_2",
                                "question_text": "A bill shows 5 pencils at ₹8 each and 2 erasers at ₹5 each. What is the total?",
                                "options": ["₹40", "₹50", "₹60", "₹70"],
                                "correct_answer": "₹50",
                                "explanation": "Pencils: 5 × ₹8 = ₹40. Erasers: 2 × ₹5 = ₹10. Total = ₹40 + ₹10 = ₹50.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_3_1_3",
                                "question_text": "If you pay ₹100 for items costing ₹85, how much change should you get?",
                                "options": ["₹5", "₹10", "₹15", "₹20"],
                                "correct_answer": "₹15",
                                "explanation": "Change = Amount paid - Cost = ₹100 - ₹85 = ₹15.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_3_1_4",
                                "question_text": "What information is NOT usually found on a shopping bill?",
                                "options": ["Date of purchase", "Your age", "Item names", "Total amount"],
                                "correct_answer": "Your age",
                                "explanation": "Shopping bills typically don't include personal information like age. They show purchase details, items, and costs.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_3_1_5",
                                "question_text": "If 2 kg of apples cost ₹120, what is the price per kg?",
                                "options": ["₹40", "₹50", "₹60", "₹70"],
                                "correct_answer": "₹60",
                                "explanation": "Price per kg = Total cost ÷ Quantity = ₹120 ÷ 2 = ₹60 per kg.",
                                "timer_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "6.3.2",
                        "topic_name": "Profit and Loss",
                        "explanation": "Profit and loss are like a game of buying and selling! Profit = Selling Price - Cost Price (when SP > CP). Loss = Cost Price - Selling Price (when CP > SP). Think of profit as 'earning extra money' and loss as 'losing some money'. Business people use this to make smart decisions!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "6_3_2_1",
                                "question_text": "If a shopkeeper buys a pen for ₹15 and sells it for ₹20, what is the profit?",
                                "options": ["₹5", "₹10", "₹15", "₹20"],
                                "correct_answer": "₹5",
                                "explanation": "Profit = Selling Price - Cost Price = ₹20 - ₹15 = ₹5. The shopkeeper earned ₹5 extra.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_3_2_2",
                                "question_text": "A book is bought for ₹80 and sold for ₹65. What is the loss?",
                                "options": ["₹10", "₹15", "₹20", "₹25"],
                                "correct_answer": "₹15",
                                "explanation": "Loss = Cost Price - Selling Price = ₹80 - ₹65 = ₹15. The seller lost ₹15.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_3_2_3",
                                "question_text": "If profit is ₹25 and selling price is ₹100, what was the cost price?",
                                "options": ["₹50", "₹75", "₹125", "₹150"],
                                "correct_answer": "₹75",
                                "explanation": "Cost Price = Selling Price - Profit = ₹100 - ₹25 = ₹75.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_3_2_4",
                                "question_text": "A toy is sold at a loss of ₹12. If the cost price was ₹48, what is the selling price?",
                                "options": ["₹30", "₹36", "₹40", "₹60"],
                                "correct_answer": "₹36",
                                "explanation": "Selling Price = Cost Price - Loss = ₹48 - ₹12 = ₹36.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_3_2_5",
                                "question_text": "If there is no profit and no loss, what can we say about the selling price?",
                                "options": ["SP = CP", "SP > CP", "SP < CP", "Cannot determine"],
                                "correct_answer": "SP = CP",
                                "explanation": "When there is no profit and no loss, the selling price equals the cost price.",
                                "timer_seconds": 45
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Geometry",
                "modules": [
                    {
                        "module_id": "6.4.1",
                        "topic_name": "Basic Elements of a Triangle",
                        "explanation": "Triangles are the strongest shapes in nature! A triangle has 3 sides, 3 angles, and 3 vertices (corners). The sum of all angles in any triangle is always 180°. Triangles are used in bridges, roofs, and even in nature (like mountain peaks). They're everywhere!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "6_4_1_1",
                                "question_text": "How many sides does a triangle have?",
                                "options": ["2", "3", "4", "5"],
                                "correct_answer": "3",
                                "explanation": "A triangle has exactly 3 sides. The word 'tri' means three!",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_4_1_2",
                                "question_text": "What is the sum of angles in any triangle?",
                                "options": ["90°", "120°", "180°", "360°"],
                                "correct_answer": "180°",
                                "explanation": "The sum of all three angles in any triangle is always 180 degrees, no matter what type of triangle it is.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_4_1_3",
                                "question_text": "What are the corners of a triangle called?",
                                "options": ["Edges", "Vertices", "Faces", "Sides"],
                                "correct_answer": "Vertices",
                                "explanation": "The corners of a triangle are called vertices. A triangle has 3 vertices.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_4_1_4",
                                "question_text": "If two angles of a triangle are 60° and 70°, what is the third angle?",
                                "options": ["40°", "50°", "60°", "70°"],
                                "correct_answer": "50°",
                                "explanation": "Third angle = 180° - (60° + 70°) = 180° - 130° = 50°. The sum must be 180°.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_4_1_5",
                                "question_text": "Which of these is NOT a property of triangles?",
                                "options": ["Has 3 sides", "Sum of angles is 180°", "Has 4 vertices", "Has 3 angles"],
                                "correct_answer": "Has 4 vertices",
                                "explanation": "Triangles have 3 vertices, not 4. They have 3 sides, 3 angles, and 3 vertices.",
                                "timer_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "6.4.2",
                        "topic_name": "Types and Properties of Triangles",
                        "explanation": "Triangles come in different flavors! By sides: Equilateral (all sides equal), Isosceles (2 sides equal), Scalene (no sides equal). By angles: Acute (all angles < 90°), Right (one angle = 90°), Obtuse (one angle > 90°). Each type has special properties that make them unique!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "6_4_2_1",
                                "question_text": "In an equilateral triangle, what is the measure of each angle?",
                                "options": ["45°", "60°", "90°", "120°"],
                                "correct_answer": "60°",
                                "explanation": "In an equilateral triangle, all angles are equal. Since the sum is 180°, each angle = 180° ÷ 3 = 60°.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_4_2_2",
                                "question_text": "Which triangle has exactly two equal sides?",
                                "options": ["Equilateral", "Isosceles", "Scalene", "Right"],
                                "correct_answer": "Isosceles",
                                "explanation": "An isosceles triangle has exactly two equal sides and two equal angles.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_4_2_3",
                                "question_text": "What makes a triangle a right triangle?",
                                "options": ["All angles are 90°", "One angle is 90°", "All sides are equal", "No angles are 90°"],
                                "correct_answer": "One angle is 90°",
                                "explanation": "A right triangle has exactly one angle that measures 90 degrees (a right angle).",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_4_2_4",
                                "question_text": "In a scalene triangle, what can we say about the sides and angles?",
                                "options": ["All sides equal", "Two sides equal", "No sides equal", "One side equal"],
                                "correct_answer": "No sides equal",
                                "explanation": "In a scalene triangle, all three sides have different lengths, and all three angles have different measures.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_4_2_5",
                                "question_text": "If a triangle has angles 30°, 60°, and 90°, what type is it?",
                                "options": ["Acute", "Right", "Obtuse", "Equilateral"],
                                "correct_answer": "Right",
                                "explanation": "This is a right triangle because it has one 90° angle. It's also a scalene triangle since all angles are different.",
                                "timer_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "6.4.3",
                        "topic_name": "Construction of Perpendicular and Parallel Lines",
                        "explanation": "Geometric construction is like drawing with rules! Perpendicular lines meet at 90° (like the letter T). Parallel lines never meet (like railway tracks). We use compass and ruler to construct these perfectly. These constructions help in architecture, engineering, and art!",
                        "difficulty": "hard",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "6_4_3_1",
                                "question_text": "What angle do perpendicular lines make when they intersect?",
                                "options": ["45°", "60°", "90°", "180°"],
                                "correct_answer": "90°",
                                "explanation": "Perpendicular lines always intersect at a right angle, which measures exactly 90 degrees.",
                                "timer_seconds": 60
                            },
                            {
                                "question_id": "6_4_3_2",
                                "question_text": "Which statement is true about parallel lines?",
                                "options": ["They intersect at one point", "They never intersect", "They intersect at many points", "They are perpendicular"],
                                "correct_answer": "They never intersect",
                                "explanation": "Parallel lines are always the same distance apart and never intersect, no matter how far they extend.",
                                "timer_seconds": 60
                            },
                            {
                                "question_id": "6_4_3_3",
                                "question_text": "What tool is essential for constructing perpendicular lines?",
                                "options": ["Only ruler", "Only compass", "Compass and ruler", "Only protractor"],
                                "correct_answer": "Compass and ruler",
                                "explanation": "Both compass and ruler are needed for precise geometric constructions of perpendicular lines.",
                                "timer_seconds": 60
                            },
                            {
                                "question_id": "6_4_3_4",
                                "question_text": "If line A is perpendicular to line B, and line B is perpendicular to line C, what is the relationship between A and C?",
                                "options": ["Perpendicular", "Parallel", "They intersect at 45°", "Cannot determine"],
                                "correct_answer": "Parallel",
                                "explanation": "If A ⊥ B and B ⊥ C, then A ∥ C. Lines perpendicular to the same line are parallel to each other.",
                                "timer_seconds": 60
                            },
                            {
                                "question_id": "6_4_3_5",
                                "question_text": "How many right angles are formed when two perpendicular lines intersect?",
                                "options": ["1", "2", "3", "4"],
                                "correct_answer": "4",
                                "explanation": "When two perpendicular lines intersect, they form 4 right angles (each 90°) around the intersection point.",
                                "timer_seconds": 60
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Algebra",
                "modules": [
                    {
                        "module_id": "6.5.1",
                        "topic_name": "Introduction to Algebra",
                        "explanation": "Algebra is like a secret code where letters represent numbers! Variables (like x, y, a, b) stand for unknown values. We use expressions like 2x + 3 to describe relationships. Algebra helps us solve puzzles and real-world problems. It's like being a detective finding missing numbers!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "6_5_1_1",
                                "question_text": "In the expression 3x + 5, what is the variable?",
                                "options": ["3", "x", "5", "+"],
                                "correct_answer": "x",
                                "explanation": "x is the variable - it represents an unknown value that can change. 3 and 5 are constants.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_5_1_2",
                                "question_text": "If x = 4, what is the value of 2x + 1?",
                                "options": ["7", "8", "9", "10"],
                                "correct_answer": "9",
                                "explanation": "2x + 1 = 2(4) + 1 = 8 + 1 = 9. Replace x with 4 and calculate.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_5_1_3",
                                "question_text": "Which of these is an algebraic expression?",
                                "options": ["5 + 3 = 8", "2x - 4", "7 > 3", "Square of 4"],
                                "correct_answer": "2x - 4",
                                "explanation": "2x - 4 is an algebraic expression because it contains a variable (x). The others are numerical statements or descriptions.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_5_1_4",
                                "question_text": "What does the expression 'a + b' represent?",
                                "options": ["Two numbers added together", "A multiplied by b", "A divided by b", "A minus b"],
                                "correct_answer": "Two numbers added together",
                                "explanation": "a + b represents the sum of two numbers, where a and b can be any values.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_5_1_5",
                                "question_text": "If y = 10, what is 3y?",
                                "options": ["13", "30", "103", "1000"],
                                "correct_answer": "30",
                                "explanation": "3y = 3 × y = 3 × 10 = 30. The expression means 3 times the value of y.",
                                "timer_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "6.5.2",
                        "topic_name": "Tree Diagrams and Algebraic Expressions",
                        "explanation": "Tree diagrams are visual maps that show how algebraic expressions are built! They break down expressions into parts like branches on a tree. For 2x + 3, the tree shows addition at the top, with branches for 2x and 3. This helps understand the structure and order of operations in algebra!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "6_5_2_1",
                                "question_text": "In the expression 4x + 2y, what operation is at the top of the tree diagram?",
                                "options": ["Multiplication", "Addition", "Subtraction", "Division"],
                                "correct_answer": "Addition",
                                "explanation": "The main operation in 4x + 2y is addition, so it appears at the top of the tree diagram with branches for 4x and 2y.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_5_2_2",
                                "question_text": "What would be the branches for the expression 3(x + 2)?",
                                "options": ["3 and (x + 2)", "x and 2", "3x and 6", "3 and x and 2"],
                                "correct_answer": "3 and (x + 2)",
                                "explanation": "In 3(x + 2), multiplication is the main operation, so the tree has branches for 3 and (x + 2).",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_5_2_3",
                                "question_text": "If a tree diagram shows subtraction at the top with branches 5x and 3, what is the expression?",
                                "options": ["5x + 3", "5x - 3", "3 - 5x", "5x × 3"],
                                "correct_answer": "5x - 3",
                                "explanation": "Subtraction at the top with branches 5x and 3 represents the expression 5x - 3.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_5_2_4",
                                "question_text": "How many main branches does the expression a + b + c have in its tree diagram?",
                                "options": ["1", "2", "3", "4"],
                                "correct_answer": "2",
                                "explanation": "a + b + c has a tree with addition at the top and two main branches: one for 'a' and another for 'b + c'.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_5_2_5",
                                "question_text": "What does a tree diagram help us understand about algebraic expressions?",
                                "options": ["Only the answer", "The structure and order", "Just the variables", "Only the numbers"],
                                "correct_answer": "The structure and order",
                                "explanation": "Tree diagrams help visualize the structure of expressions and understand the order in which operations should be performed.",
                                "timer_seconds": 45
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "Statistics",
                "modules": [
                    {
                        "module_id": "6.6.1",
                        "topic_name": "Data Collection and Organization",
                        "explanation": "Statistics is like being a data detective! We collect information (data), organize it in tables, and find patterns. Data can be numbers, measurements, or counts. Organizing data helps us understand it better and make smart decisions. It's used in sports, weather, and business!",
                        "difficulty": "easy",
                        "total_timer_minutes": 6,
                        "questions": [
                            {
                                "question_id": "6_6_1_1",
                                "question_text": "What is the first step in statistical work?",
                                "options": ["Drawing graphs", "Collecting data", "Calculating averages", "Making conclusions"],
                                "correct_answer": "Collecting data",
                                "explanation": "The first step in statistics is collecting data. Without data, we can't do any analysis.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_6_1_2",
                                "question_text": "Which of these is an example of data?",
                                "options": ["5 students", "Height of students", "Tall", "Numbers are boring"],
                                "correct_answer": "Height of students",
                                "explanation": "Data is collected information. 'Height of students' represents measurable information we can collect and analyze.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_6_1_3",
                                "question_text": "Why do we organize data in tables?",
                                "options": ["To make it confusing", "To see patterns easily", "To waste time", "To make it look nice"],
                                "correct_answer": "To see patterns easily",
                                "explanation": "Organizing data in tables helps us see patterns, compare values, and understand the information better.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_6_1_4",
                                "question_text": "What is raw data?",
                                "options": ["Cooked data", "Unorganized collected information", "Only numbers", "Graphed information"],
                                "correct_answer": "Unorganized collected information",
                                "explanation": "Raw data is information that has been collected but not yet organized or processed.",
                                "timer_seconds": 30
                            },
                            {
                                "question_id": "6_6_1_5",
                                "question_text": "Which field uses statistics the most?",
                                "options": ["Only mathematics", "Only science", "Many fields", "Only business"],
                                "correct_answer": "Many fields",
                                "explanation": "Statistics is used in many fields including sports, weather forecasting, business, medicine, and social sciences.",
                                "timer_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "6.6.2",
                        "topic_name": "Pictographs and Bar Graphs",
                        "explanation": "Graphs turn boring numbers into exciting pictures! Pictographs use icons or pictures to represent data (each picture = certain quantity). Bar graphs use bars of different heights to show comparisons. Both make it easy to see patterns and compare data at a glance. A picture is worth a thousand numbers!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "6_6_2_1",
                                "question_text": "In a pictograph, if each 🍎 represents 5 apples, how many apples do 3 🍎 represent?",
                                "options": ["3 apples", "5 apples", "15 apples", "8 apples"],
                                "correct_answer": "15 apples",
                                "explanation": "3 🍎 × 5 apples per 🍎 = 15 apples. Multiply the number of symbols by the value each represents.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_6_2_2",
                                "question_text": "What do bar graphs use to show data?",
                                "options": ["Pictures", "Bars of different heights", "Numbers only", "Colors"],
                                "correct_answer": "Bars of different heights",
                                "explanation": "Bar graphs use bars of different heights (or lengths) to represent and compare different quantities.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_6_2_3",
                                "question_text": "If a bar graph shows a bar reaching 8 on the scale, and each unit represents 10 students, how many students does it represent?",
                                "options": ["8 students", "10 students", "18 students", "80 students"],
                                "correct_answer": "80 students",
                                "explanation": "8 units × 10 students per unit = 80 students. Multiply the bar height by the scale value.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_6_2_4",
                                "question_text": "What is the advantage of pictographs over tables?",
                                "options": ["They are more accurate", "They are visually appealing", "They use less space", "They are faster to make"],
                                "correct_answer": "They are visually appealing",
                                "explanation": "Pictographs are more visually appealing and easier to understand at a glance compared to tables of numbers.",
                                "timer_seconds": 45
                            },
                            {
                                "question_id": "6_6_2_5",
                                "question_text": "When would you use a bar graph instead of a pictograph?",
                                "options": ["For exact numbers", "For visual appeal", "For large quantities", "For small children"],
                                "correct_answer": "For exact numbers",
                                "explanation": "Bar graphs are better for showing exact numerical values, while pictographs are better for visual appeal and general comparisons.",
                                "timer_seconds": 45
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
    curriculum = generate_class6_curriculum()
    
    with open('class6_mathematics_curriculum.json', 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    
    print("Class 6 Mathematics curriculum saved to 'class6_mathematics_curriculum.json'")
    
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