# /// script
# requires-python = ">=3.8"
# ///

import json

def create_class4_curriculum():
    """Create the complete curriculum structure for Class 4 Mathematics"""
    
    curriculum = {
        "class": "4",
        "subject": "Mathematics",
        "board": "TN State Board",
        "terms": [
            {
                "term_name": "Term 1",
                "chapters": [
                    {
                        "chapter_name": "Geometry",
                        "modules": [
                            {
                                "module_id": 1,
                                "topic_name": "Properties of 2D Shapes",
                                "explanation": "2D shapes are flat like drawings on paper! A square has 4 equal sides and 4 right angles. A rectangle has opposite sides equal and 4 right angles. A triangle has 3 sides and 3 angles that add up to 180°. A circle has no sides or corners but has a center and radius. Understanding these properties helps you identify and work with shapes!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "How many right angles does a square have?",
                                        "options": ["2", "3", "4", "5"],
                                        "correct_answer": "4",
                                        "rationale": "A square has 4 right angles, one at each corner.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is true about a rectangle's sides?",
                                        "options": ["All sides equal", "Opposite sides equal", "No sides equal", "Only one pair equal"],
                                        "correct_answer": "Opposite sides equal",
                                        "rationale": "In a rectangle, opposite sides are equal in length.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What do the angles in a triangle add up to?",
                                        "options": ["90°", "180°", "270°", "360°"],
                                        "correct_answer": "180°",
                                        "rationale": "The sum of angles in any triangle is always 180°.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "Which shape has no corners?",
                                        "options": ["Square", "Triangle", "Circle", "Rectangle"],
                                        "correct_answer": "Circle",
                                        "rationale": "A circle has no corners or vertices.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "How many sides does a quadrilateral have?",
                                        "options": ["3", "4", "5", "6"],
                                        "correct_answer": "4",
                                        "rationale": "A quadrilateral is a four-sided polygon.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is the distance from the center of a circle to any point on the circle called?",
                                        "options": ["Diameter", "Radius", "Circumference", "Chord"],
                                        "correct_answer": "Radius",
                                        "rationale": "The radius is the distance from the center to any point on the circle.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            },
                            {
                                "module_id": 2,
                                "topic_name": "3D Shapes and Their Nets",
                                "explanation": "3D shapes are solid objects you can hold! A cube's net is 6 squares arranged in a cross pattern. A cuboid's net has 6 rectangles. A cylinder's net has 2 circles and 1 rectangle. A cone's net has 1 circle and 1 sector. Understanding nets helps you see how 3D shapes are built from 2D shapes!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "How many squares are in a cube's net?",
                                        "options": ["4", "5", "6", "8"],
                                        "correct_answer": "6",
                                        "rationale": "A cube has 6 faces, so its net has 6 squares.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What shapes are in a cylinder's net?",
                                        "options": ["3 circles", "2 circles and 1 rectangle", "3 rectangles", "1 circle and 2 rectangles"],
                                        "correct_answer": "2 circles and 1 rectangle",
                                        "rationale": "A cylinder's net consists of 2 circular faces and 1 rectangular curved surface.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is a net of a 3D shape?",
                                        "options": ["The 3D shape itself", "A 2D pattern that folds into the 3D shape", "A measurement of the shape", "A shadow of the shape"],
                                        "correct_answer": "A 2D pattern that folds into the 3D shape",
                                        "rationale": "A net is a 2D pattern that can be folded to form a 3D shape.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "How many faces does a cuboid have?",
                                        "options": ["4", "5", "6", "8"],
                                        "correct_answer": "6",
                                        "rationale": "A cuboid has 6 rectangular faces.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What shapes are in a cone's net?",
                                        "options": ["2 circles", "1 circle and 1 triangle", "1 circle and 1 sector", "2 triangles"],
                                        "correct_answer": "1 circle and 1 sector",
                                        "rationale": "A cone's net consists of 1 circular base and 1 sector (curved surface).",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "Which 3D shape has a net with only squares?",
                                        "options": ["Cuboid", "Cube", "Cylinder", "Cone"],
                                        "correct_answer": "Cube",
                                        "rationale": "Only a cube has all square faces, so its net contains only squares.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Numbers",
                        "modules": [
                            {
                                "module_id": 3,
                                "topic_name": "Numbers up to 99999",
                                "explanation": "Let's explore even bigger numbers! Numbers up to 99999 have five places: ten thousands, thousands, hundreds, tens, and ones. In 45678, 4 is ten thousands (40000), 5 is thousands (5000), 6 is hundreds (600), 7 is tens (70), and 8 is ones (8). These large numbers help us count thousands of things!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 12,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What comes after 9999?",
                                        "options": ["9990", "10000", "99999", "100000"],
                                        "correct_answer": "10000",
                                        "rationale": "The number after 9999 is 10000.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is the value of 6 in 67890?",
                                        "options": ["6", "60", "600", "60000"],
                                        "correct_answer": "60000",
                                        "rationale": "6 is in the ten thousands place, so it's worth 6 × 10000 = 60000.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What digit is in the thousands place in 54321?",
                                        "options": ["5", "4", "3", "2"],
                                        "correct_answer": "4",
                                        "rationale": "In 54321, the thousands place is the fourth digit from the right, which is 4.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 20000 + 3000 + 400 + 50 + 6?",
                                        "options": ["23456", "24356", "32456", "54326"],
                                        "correct_answer": "23456",
                                        "rationale": "20000 + 3000 + 400 + 50 + 6 = 23456.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "Which number has 8 in the ten thousands place?",
                                        "options": ["12345", "23456", "34567", "89012"],
                                        "correct_answer": "89012",
                                        "rationale": "In 89012, the ten thousands digit is 8.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is the value of 0 in 50678?",
                                        "options": ["0", "10", "100", "1000"],
                                        "correct_answer": "0",
                                        "rationale": "0 in the thousands place has a value of 0.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 45678 + 10000?",
                                        "options": ["45679", "55678", "45688", "65678"],
                                        "correct_answer": "55678",
                                        "rationale": "45678 + 10000 = 55678.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "Which is smallest: 23456, 34567, 45678?",
                                        "options": ["23456", "34567", "45678", "All equal"],
                                        "correct_answer": "23456",
                                        "rationale": "23456 has the smallest ten thousands digit (2).",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            },
                            {
                                "module_id": 4,
                                "topic_name": "Roman Numerals",
                                "explanation": "Roman numerals are like ancient number codes! I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000. When a smaller numeral comes before a larger one, you subtract (IV = 4). When it comes after, you add (VI = 6). They're still used on clocks and in book chapters!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What does V represent in Roman numerals?",
                                        "options": ["1", "5", "10", "50"],
                                        "correct_answer": "5",
                                        "rationale": "V represents 5 in Roman numerals.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is IX in Hindu-Arabic numerals?",
                                        "options": ["9", "10", "11", "14"],
                                        "correct_answer": "9",
                                        "rationale": "IX = 10 - 1 = 9 (I before X means subtract).",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What does L represent in Roman numerals?",
                                        "options": ["10", "50", "100", "500"],
                                        "correct_answer": "50",
                                        "rationale": "L represents 50 in Roman numerals.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is XV in Hindu-Arabic numerals?",
                                        "options": ["10", "15", "20", "25"],
                                        "correct_answer": "15",
                                        "rationale": "XV = 10 + 5 = 15 (X before V means add).",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What does C represent in Roman numerals?",
                                        "options": ["50", "100", "500", "1000"],
                                        "correct_answer": "100",
                                        "rationale": "C represents 100 in Roman numerals.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is XL in Hindu-Arabic numerals?",
                                        "options": ["40", "50", "60", "90"],
                                        "correct_answer": "40",
                                        "rationale": "XL = 50 - 10 = 40 (X before L means subtract).",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Addition",
                        "modules": [
                            {
                                "module_id": 5,
                                "topic_name": "Addition of Five Digit Numbers",
                                "explanation": "Adding big numbers is like building towers! When adding 23456 + 12345, we add ones (6+5=11, carry 1), tens (5+4+1=10, carry 1), hundreds (4+3+1=8), thousands (3+2=5), and ten thousands (2+1=3). Practice makes you a math champion!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 12,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is 12345 + 23456?",
                                        "options": ["35791", "35701", "35801", "36791"],
                                        "correct_answer": "35701",
                                        "rationale": "12345 + 23456 = 35701.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is 34567 + 12345?",
                                        "options": ["45912", "46912", "45812", "46812"],
                                        "correct_answer": "46912",
                                        "rationale": "34567 + 12345 = 46912.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 45678 + 10000?",
                                        "options": ["45679", "55678", "45688", "55688"],
                                        "correct_answer": "55678",
                                        "rationale": "45678 + 10000 = 55678.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 23456 + 54321?",
                                        "options": ["76777", "77777", "78777", "79777"],
                                        "correct_answer": "77777",
                                        "rationale": "23456 + 54321 = 77777.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 12345 + 12345?",
                                        "options": ["24680", "24690", "23690", "25690"],
                                        "correct_answer": "24690",
                                        "rationale": "12345 + 12345 = 24690.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 56789 + 43210?",
                                        "options": ["98999", "99999", "100099", "101099"],
                                        "correct_answer": "99999",
                                        "rationale": "56789 + 43210 = 99999.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 20000 + 30000 + 40000?",
                                        "options": ["80000", "90000", "100000", "110000"],
                                        "correct_answer": "90000",
                                        "rationale": "20000 + 30000 + 40000 = 90000.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "What is 11111 + 22222 + 33333?",
                                        "options": ["65666", "66666", "67666", "68666"],
                                        "correct_answer": "66666",
                                        "rationale": "11111 + 22222 + 33333 = 66666.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Subtraction",
                        "modules": [
                            {
                                "module_id": 6,
                                "topic_name": "Subtraction of Five Digit Numbers",
                                "explanation": "Subtracting big numbers is like taking away blocks! When subtracting 56789 - 23456, we subtract ones (9-6=3), tens (8-5=3), hundreds (7-4=3), thousands (6-3=3), and ten thousands (5-2=3). Sometimes we need to borrow when the top digit is smaller!",
                                "difficulty": "Hard",
                                "total_timer_minutes": 15,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is 56789 - 23456?",
                                        "options": ["32333", "33333", "34333", "35333"],
                                        "correct_answer": "33333",
                                        "rationale": "56789 - 23456 = 33333.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is 98765 - 54321?",
                                        "options": ["43444", "44444", "45444", "46444"],
                                        "correct_answer": "44444",
                                        "rationale": "98765 - 54321 = 44444.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 80000 - 30000?",
                                        "options": ["40000", "50000", "60000", "70000"],
                                        "correct_answer": "50000",
                                        "rationale": "80000 - 30000 = 50000.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 65432 - 12345?",
                                        "options": ["52087", "53087", "54087", "55087"],
                                        "correct_answer": "53087",
                                        "rationale": "65432 - 12345 = 53087.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 90000 - 10000?",
                                        "options": ["70000", "80000", "90000", "100000"],
                                        "correct_answer": "80000",
                                        "rationale": "90000 - 10000 = 80000.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 75324 - 45213?",
                                        "options": ["20111", "30111", "40111", "50111"],
                                        "correct_answer": "30111",
                                        "rationale": "75324 - 45213 = 30111.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 60000 - 20000 - 10000?",
                                        "options": ["20000", "30000", "40000", "50000"],
                                        "correct_answer": "30000",
                                        "rationale": "60000 - 20000 - 10000 = 30000.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "What is 88888 - 44444?",
                                        "options": ["42444", "43444", "44444", "45444"],
                                        "correct_answer": "44444",
                                        "rationale": "88888 - 44444 = 44444.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 9,
                                        "question_text": "What is 50000 - 25000?",
                                        "options": ["20000", "25000", "30000", "35000"],
                                        "correct_answer": "25000",
                                        "rationale": "50000 - 25000 = 25000.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 10,
                                        "question_text": "What is 76543 - 32109?",
                                        "options": ["42434", "43434", "44434", "45434"],
                                        "correct_answer": "44434",
                                        "rationale": "76543 - 32109 = 44434.",
                                        "timer_per_question_seconds": 60
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Multiplication",
                        "modules": [
                            {
                                "module_id": 7,
                                "topic_name": "Multiplication of Three Digit Numbers",
                                "explanation": "Multiplying three-digit numbers is like building with blocks! When you multiply 234 × 123, you multiply 234 × 3 (ones), 234 × 20 (tens), and 234 × 100 (hundreds), then add them together. Breaking big problems into smaller steps makes them easy!",
                                "difficulty": "Hard",
                                "total_timer_minutes": 15,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is 123 × 321?",
                                        "options": ["39483", "40483", "41483", "42483"],
                                        "correct_answer": "39483",
                                        "rationale": "123 × 321 = 39483.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is 234 × 123?",
                                        "options": ["28782", "29782", "30782", "31782"],
                                        "correct_answer": "28782",
                                        "rationale": "234 × 123 = 28782.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 345 × 100?",
                                        "options": ["3450", "34500", "345000", "3450000"],
                                        "correct_answer": "34500",
                                        "rationale": "345 × 100 = 34500.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 456 × 200?",
                                        "options": ["9120", "91200", "912000", "9120000"],
                                        "correct_answer": "91200",
                                        "rationale": "456 × 200 = 91200.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 567 × 111?",
                                        "options": ["61937", "62937", "63937", "64937"],
                                        "correct_answer": "62937",
                                        "rationale": "567 × 111 = 62937.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 678 × 10?",
                                        "options": ["678", "6780", "67800", "678000"],
                                        "correct_answer": "6780",
                                        "rationale": "678 × 10 = 6780.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 789 × 222?",
                                        "options": ["175158", "176158", "177158", "178158"],
                                        "correct_answer": "175158",
                                        "rationale": "789 × 222 = 175158.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "What is 333 × 333?",
                                        "options": ["110889", "111889", "112889", "113889"],
                                        "correct_answer": "110889",
                                        "rationale": "333 × 333 = 110889.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 9,
                                        "question_text": "What is 444 × 111?",
                                        "options": ["49284", "50284", "51284", "52284"],
                                        "correct_answer": "49284",
                                        "rationale": "444 × 111 = 49284.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 10,
                                        "question_text": "What is 555 × 222?",
                                        "options": ["123210", "124210", "125210", "126210"],
                                        "correct_answer": "123210",
                                        "rationale": "555 × 222 = 123210.",
                                        "timer_per_question_seconds": 60
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Time",
                        "modules": [
                            {
                                "module_id": 8,
                                "topic_name": "Time Calculations",
                                "explanation": "Time calculations help you plan your day! To add time, add minutes first (carry over 60 minutes = 1 hour), then add hours. To subtract time, sometimes you need to borrow 1 hour = 60 minutes. Understanding time helps you manage schedules and be punctual!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is 2 hours 30 minutes + 1 hour 45 minutes?",
                                        "options": ["3 hours 75 minutes", "4 hours 15 minutes", "4 hours 25 minutes", "3 hours 15 minutes"],
                                        "correct_answer": "4 hours 15 minutes",
                                        "rationale": "2:30 + 1:45 = 4:15 (30+45=75 minutes = 1 hour 15 minutes, 2+1+1=4 hours).",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is 3 hours 20 minutes - 1 hour 45 minutes?",
                                        "options": ["1 hour 25 minutes", "1 hour 35 minutes", "2 hours 25 minutes", "2 hours 35 minutes"],
                                        "correct_answer": "1 hour 35 minutes",
                                        "rationale": "3:20 - 1:45 = 1:35 (borrow 1 hour = 60 minutes, 80-45=35, 2-1=1).",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "How many minutes in 2 hours 30 minutes?",
                                        "options": ["120 minutes", "150 minutes", "180 minutes", "210 minutes"],
                                        "correct_answer": "150 minutes",
                                        "rationale": "2 hours 30 minutes = 2×60 + 30 = 120 + 30 = 150 minutes.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 4 hours 15 minutes + 2 hours 50 minutes?",
                                        "options": ["6 hours 65 minutes", "7 hours 5 minutes", "7 hours 15 minutes", "6 hours 5 minutes"],
                                        "correct_answer": "7 hours 5 minutes",
                                        "rationale": "4:15 + 2:50 = 7:05 (15+50=65 minutes = 1 hour 5 minutes, 4+2+1=7 hours).",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 5 hours 10 minutes - 2 hours 25 minutes?",
                                        "options": ["2 hours 35 minutes", "2 hours 45 minutes", "3 hours 35 minutes", "3 hours 45 minutes"],
                                        "correct_answer": "2 hours 45 minutes",
                                        "rationale": "5:10 - 2:25 = 2:45 (borrow 1 hour = 60 minutes, 70-25=45, 4-2=2).",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "How many hours and minutes in 185 minutes?",
                                        "options": ["2 hours 5 minutes", "3 hours 5 minutes", "2 hours 25 minutes", "3 hours 25 minutes"],
                                        "correct_answer": "3 hours 5 minutes",
                                        "rationale": "185 minutes = 3×60 + 5 = 180 + 5 = 3 hours 5 minutes.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Money",
                        "modules": [
                            {
                                "module_id": 9,
                                "topic_name": "Money Transactions and Problems",
                                "explanation": "Money problems help you shop smart! When buying multiple items, add their prices for the total cost. When paying with a larger amount, subtract to find change. Understanding money helps you make good purchasing decisions and save for the future!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 12,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "If a book costs ₹125 and a pen costs ₹35, what's the total cost?",
                                        "options": ["₹150", "₹160", "₹170", "₹180"],
                                        "correct_answer": "₹160",
                                        "rationale": "₹125 + ₹35 = ₹160.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "If you have ₹500 and buy something for ₹275, how much is left?",
                                        "options": ["₹215", "₹225", "₹235", "₹245"],
                                        "correct_answer": "₹225",
                                        "rationale": "₹500 - ₹275 = ₹225.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "If you buy 3 notebooks at ₹45 each, what's the total cost?",
                                        "options": ["₹125", "₹135", "₹145", "₹155"],
                                        "correct_answer": "₹135",
                                        "rationale": "3 × ₹45 = ₹135.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "If a toy costs ₹180 and you pay with ₹200, what change do you get?",
                                        "options": ["₹15", "₹20", "₹25", "₹30"],
                                        "correct_answer": "₹20",
                                        "rationale": "₹200 - ₹180 = ₹20 change.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is ₹350 + ₹450?",
                                        "options": ["₹700", "₹800", "₹900", "₹1000"],
                                        "correct_answer": "₹800",
                                        "rationale": "₹350 + ₹450 = ₹800.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "If you buy 2 pencils at ₹12 each and 1 eraser at ₹8, what's the total?",
                                        "options": ["₹28", "₹30", "₹32", "₹34"],
                                        "correct_answer": "₹32",
                                        "rationale": "2×₹12 + ₹8 = ₹24 + ₹8 = ₹32.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is ₹750 - ₹325?",
                                        "options": ["₹415", "₹425", "₹435", "₹445"],
                                        "correct_answer": "₹425",
                                        "rationale": "₹750 - ₹325 = ₹425.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "If you have ₹1000 and buy items costing ₹250, ₹175, and ₹125, how much is left?",
                                        "options": ["₹400", "₹450", "₹500", "₹550"],
                                        "correct_answer": "₹450",
                                        "rationale": "Total cost = ₹250 + ₹175 + ₹125 = ₹550. Remaining = ₹1000 - ₹550 = ₹450.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "term_name": "Term 2",
                "chapters": [
                    {
                        "chapter_name": "Division",
                        "modules": [
                            {
                                "module_id": 10,
                                "topic_name": "Division of Three Digit Numbers",
                                "explanation": "Division is sharing equally! When dividing 456 ÷ 3, you divide hundreds (4÷3=1 remainder 1), then tens (15÷3=5), then ones (6÷3=2). Long division helps you organize the steps. Practice makes division easy and helps you solve real-life sharing problems!",
                                "difficulty": "Hard",
                                "total_timer_minutes": 15,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is 456 ÷ 3?",
                                        "options": ["142", "152", "162", "172"],
                                        "correct_answer": "152",
                                        "rationale": "456 ÷ 3 = 152.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is 789 ÷ 3?",
                                        "options": ["243", "253", "263", "273"],
                                        "correct_answer": "263",
                                        "rationale": "789 ÷ 3 = 263.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 864 ÷ 4?",
                                        "options": ["206", "216", "226", "236"],
                                        "correct_answer": "216",
                                        "rationale": "864 ÷ 4 = 216.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 999 ÷ 9?",
                                        "options": ["101", "111", "121", "131"],
                                        "correct_answer": "111",
                                        "rationale": "999 ÷ 9 = 111.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 625 ÷ 5?",
                                        "options": ["115", "125", "135", "145"],
                                        "correct_answer": "125",
                                        "rationale": "625 ÷ 5 = 125.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 444 ÷ 4?",
                                        "options": ["101", "111", "121", "131"],
                                        "correct_answer": "111",
                                        "rationale": "444 ÷ 4 = 111.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 777 ÷ 7?",
                                        "options": ["101", "111", "121", "131"],
                                        "correct_answer": "111",
                                        "rationale": "777 ÷ 7 = 111.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "What is 888 ÷ 8?",
                                        "options": ["101", "111", "121", "131"],
                                        "correct_answer": "111",
                                        "rationale": "888 ÷ 8 = 111.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 9,
                                        "question_text": "What is 555 ÷ 5?",
                                        "options": ["101", "111", "121", "131"],
                                        "correct_answer": "111",
                                        "rationale": "555 ÷ 5 = 111.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 10,
                                        "question_text": "What is 666 ÷ 6?",
                                        "options": ["101", "111", "121", "131"],
                                        "correct_answer": "111",
                                        "rationale": "666 ÷ 6 = 111.",
                                        "timer_per_question_seconds": 60
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Fractions",
                        "modules": [
                            {
                                "module_id": 11,
                                "topic_name": "Equivalent Fractions",
                                "explanation": "Equivalent fractions are different names for the same amount! 1/2 = 2/4 = 3/6 because they represent the same portion. To find equivalent fractions, multiply or divide both numerator and denominator by the same number. They help you compare and work with fractions easily!",
                                "difficulty": "Hard",
                                "total_timer_minutes": 15,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "Which fraction is equivalent to 1/2?",
                                        "options": ["2/3", "2/4", "3/5", "4/6"],
                                        "correct_answer": "2/4",
                                        "rationale": "2/4 = 1/2 (divide both numerator and denominator by 2).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "Which fraction is equivalent to 2/3?",
                                        "options": ["3/4", "4/5", "4/6", "5/6"],
                                        "correct_answer": "4/6",
                                        "rationale": "4/6 = 2/3 (divide both numerator and denominator by 2).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 3/4 equivalent to?",
                                        "options": ["4/5", "5/6", "6/8", "7/8"],
                                        "correct_answer": "6/8",
                                        "rationale": "6/8 = 3/4 (divide both numerator and denominator by 2).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "Which fraction is NOT equivalent to 1/3?",
                                        "options": ["2/6", "3/9", "2/5", "4/12"],
                                        "correct_answer": "2/5",
                                        "rationale": "2/5 ≠ 1/3 (2×3 ≠ 1×5).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 2/5 equivalent to with denominator 10?",
                                        "options": ["3/10", "4/10", "5/10", "6/10"],
                                        "correct_answer": "4/10",
                                        "rationale": "2/5 = 4/10 (multiply both numerator and denominator by 2).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "Which fractions are equivalent: 3/4 and ?",
                                        "options": ["4/5", "5/6", "6/8", "7/9"],
                                        "correct_answer": "6/8",
                                        "rationale": "3/4 = 6/8 (multiply both numerator and denominator by 2).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 4/6 in simplest form?",
                                        "options": ["1/2", "2/3", "3/4", "4/5"],
                                        "correct_answer": "2/3",
                                        "rationale": "4/6 = 2/3 (divide both numerator and denominator by 2).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "Which fraction is equivalent to 5/10?",
                                        "options": ["1/2", "1/3", "2/3", "3/4"],
                                        "correct_answer": "1/2",
                                        "rationale": "5/10 = 1/2 (divide both numerator and denominator by 5).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 9,
                                        "question_text": "What is 3/5 equivalent to with denominator 15?",
                                        "options": ["6/15", "7/15", "8/15", "9/15"],
                                        "correct_answer": "9/15",
                                        "rationale": "3/5 = 9/15 (multiply both numerator and denominator by 3).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 10,
                                        "question_text": "Which fraction is equivalent to 7/8?",
                                        "options": ["8/9", "14/16", "15/16", "16/17"],
                                        "correct_answer": "14/16",
                                        "rationale": "7/8 = 14/16 (multiply both numerator and denominator by 2).",
                                        "timer_per_question_seconds": 60
                                    }
                                ]
                            },
                            {
                                "module_id": 12,
                                "topic_name": "Addition and Subtraction of Fractions",
                                "explanation": "Adding and subtracting fractions is like working with puzzle pieces! To add or subtract fractions with the same denominator, just add or subtract the numerators. With different denominators, first find equivalent fractions with the same denominator, then add or subtract!",
                                "difficulty": "Hard",
                                "total_timer_minutes": 15,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is 1/4 + 2/4?",
                                        "options": ["1/4", "2/4", "3/4", "4/4"],
                                        "correct_answer": "3/4",
                                        "rationale": "1/4 + 2/4 = 3/4 (add numerators, keep denominator).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is 3/5 + 1/5?",
                                        "options": ["2/5", "3/5", "4/5", "5/5"],
                                        "correct_answer": "4/5",
                                        "rationale": "3/5 + 1/5 = 4/5 (add numerators, keep denominator).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 3/4 - 1/4?",
                                        "options": ["1/4", "2/4", "3/4", "4/4"],
                                        "correct_answer": "2/4",
                                        "rationale": "3/4 - 1/4 = 2/4 (subtract numerators, keep denominator).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 5/6 - 2/6?",
                                        "options": ["1/6", "2/6", "3/6", "4/6"],
                                        "correct_answer": "3/6",
                                        "rationale": "5/6 - 2/6 = 3/6 (subtract numerators, keep denominator).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 1/2 + 1/4?",
                                        "options": ["1/4", "2/4", "3/4", "4/4"],
                                        "correct_answer": "3/4",
                                        "rationale": "1/2 + 1/4 = 2/4 + 1/4 = 3/4.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 3/4 - 1/2?",
                                        "options": ["1/4", "2/4", "3/4", "4/4"],
                                        "correct_answer": "1/4",
                                        "rationale": "3/4 - 1/2 = 3/4 - 2/4 = 1/4.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 2/3 + 1/6?",
                                        "options": ["3/6", "4/6", "5/6", "6/6"],
                                        "correct_answer": "5/6",
                                        "rationale": "2/3 + 1/6 = 4/6 + 1/6 = 5/6.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "What is 5/8 + 1/8?",
                                        "options": ["4/8", "5/8", "6/8", "7/8"],
                                        "correct_answer": "6/8",
                                        "rationale": "5/8 + 1/8 = 6/8 (add numerators, keep denominator).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 9,
                                        "question_text": "What is 7/10 - 3/10?",
                                        "options": ["2/10", "3/10", "4/10", "5/10"],
                                        "correct_answer": "4/10",
                                        "rationale": "7/10 - 3/10 = 4/10 (subtract numerators, keep denominator).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 10,
                                        "question_text": "What is 1/3 + 1/6?",
                                        "options": ["2/6", "3/6", "4/6", "5/6"],
                                        "correct_answer": "3/6",
                                        "rationale": "1/3 + 1/6 = 2/6 + 1/6 = 3/6.",
                                        "timer_per_question_seconds": 60
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Decimals",
                        "modules": [
                            {
                                "module_id": 13,
                                "topic_name": "Introduction to Decimals",
                                "explanation": "Decimals are like fractions with powers of 10! 0.1 means one-tenth, 0.01 means one-hundredth, and 0.001 means one-thousandth. The decimal point separates whole numbers from fractions. Decimals help you work with money and measurements precisely!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What does 0.5 represent?",
                                        "options": ["One-half", "One-third", "One-fourth", "One-fifth"],
                                        "correct_answer": "One-half",
                                        "rationale": "0.5 = 5/10 = 1/2 = one-half.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What does 0.25 represent?",
                                        "options": ["One-half", "One-third", "One-fourth", "One-fifth"],
                                        "correct_answer": "One-fourth",
                                        "rationale": "0.25 = 25/100 = 1/4 = one-fourth.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 0.1 as a fraction?",
                                        "options": ["1/10", "1/100", "1/2", "1/5"],
                                        "correct_answer": "1/10",
                                        "rationale": "0.1 = 1/10 = one-tenth.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 0.75 as a fraction?",
                                        "options": ["1/2", "2/3", "3/4", "4/5"],
                                        "correct_answer": "3/4",
                                        "rationale": "0.75 = 75/100 = 3/4 = three-fourths.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "Which place value is the 5 in 0.52?",
                                        "options": ["Tenths", "Hundredths", "Thousandths", "Ones"],
                                        "correct_answer": "Tenths",
                                        "rationale": "In 0.52, the 5 is in the tenths place.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 0.01 as a fraction?",
                                        "options": ["1/10", "1/100", "1/2", "1/5"],
                                        "correct_answer": "1/100",
                                        "rationale": "0.01 = 1/100 = one-hundredth.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            },
                            {
                                "module_id": 14,
                                "topic_name": "Addition and Subtraction of Decimals",
                                "explanation": "Adding and subtracting decimals is like working with money! Line up the decimal points, then add or subtract as usual. Fill in empty places with zeros. This helps you calculate prices, measurements, and other real-world values accurately!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 12,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is 0.5 + 0.3?",
                                        "options": ["0.2", "0.8", "0.15", "0.35"],
                                        "correct_answer": "0.8",
                                        "rationale": "0.5 + 0.3 = 0.8.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is 0.75 + 0.25?",
                                        "options": ["0.50", "1.00", "1.25", "1.50"],
                                        "correct_answer": "1.00",
                                        "rationale": "0.75 + 0.25 = 1.00.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 0.8 - 0.3?",
                                        "options": ["0.3", "0.5", "0.7", "0.9"],
                                        "correct_answer": "0.5",
                                        "rationale": "0.8 - 0.3 = 0.5.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 1.2 + 0.8?",
                                        "options": ["1.0", "1.5", "2.0", "2.5"],
                                        "correct_answer": "2.0",
                                        "rationale": "1.2 + 0.8 = 2.0.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 2.5 - 1.3?",
                                        "options": ["1.1", "1.2", "1.3", "1.4"],
                                        "correct_answer": "1.2",
                                        "rationale": "2.5 - 1.3 = 1.2.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 0.45 + 0.55?",
                                        "options": ["0.90", "1.00", "1.10", "1.20"],
                                        "correct_answer": "1.00",
                                        "rationale": "0.45 + 0.55 = 1.00.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 3.75 - 2.25?",
                                        "options": ["1.25", "1.50", "1.75", "2.00"],
                                        "correct_answer": "1.50",
                                        "rationale": "3.75 - 2.25 = 1.50.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "What is 0.1 + 0.01 + 0.001?",
                                        "options": ["0.011", "0.101", "0.111", "0.121"],
                                        "correct_answer": "0.111",
                                        "rationale": "0.1 + 0.01 + 0.001 = 0.111.",
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
                                "module_id": 15,
                                "topic_name": "Conversion of Units",
                                "explanation": "Unit conversion is like translating between languages! 1 km = 1000 m, 1 m = 100 cm, 1 kg = 1000 g, 1 l = 1000 ml. Knowing these conversions helps you work with different measurement systems and solve real-world problems!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "How many meters are in 2 kilometers?",
                                        "options": ["20", "200", "2000", "20000"],
                                        "correct_answer": "2000",
                                        "rationale": "2 km = 2 × 1000 = 2000 meters.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "How many centimeters are in 3 meters?",
                                        "options": ["30", "300", "3000", "30000"],
                                        "correct_answer": "300",
                                        "rationale": "3 m = 3 × 100 = 300 centimeters.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "How many grams are in 2.5 kilograms?",
                                        "options": ["250", "2500", "25000", "250000"],
                                        "correct_answer": "2500",
                                        "rationale": "2.5 kg = 2.5 × 1000 = 2500 grams.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "How many milliliters are in 1.5 liters?",
                                        "options": ["150", "1500", "15000", "150000"],
                                        "correct_answer": "1500",
                                        "rationale": "1.5 l = 1.5 × 1000 = 1500 milliliters.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 3500 meters in kilometers?",
                                        "options": ["0.35 km", "3.5 km", "35 km", "350 km"],
                                        "correct_answer": "3.5 km",
                                        "rationale": "3500 m ÷ 1000 = 3.5 kilometers.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 450 centimeters in meters?",
                                        "options": ["0.45 m", "4.5 m", "45 m", "450 m"],
                                        "correct_answer": "4.5 m",
                                        "rationale": "450 cm ÷ 100 = 4.5 meters.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "term_name": "Term 3",
                "chapters": [
                    {
                        "chapter_name": "Geometry",
                        "modules": [
                            {
                                "module_id": 16,
                                "topic_name": "Angles",
                                "explanation": "Angles are like corners that tell us how much something turns! A right angle is 90°, like the corner of a book. An acute angle is less than 90°, like a sharp corner. An obtuse angle is more than 90° but less than 180°, like a wide corner. Angles help us understand shapes and directions!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "How many degrees is a right angle?",
                                        "options": ["45°", "90°", "180°", "360°"],
                                        "correct_answer": "90°",
                                        "rationale": "A right angle measures exactly 90 degrees.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What type of angle is 60°?",
                                        "options": ["Right angle", "Acute angle", "Obtuse angle", "Straight angle"],
                                        "correct_answer": "Acute angle",
                                        "rationale": "60° is less than 90°, so it's an acute angle.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What type of angle is 120°?",
                                        "options": ["Right angle", "Acute angle", "Obtuse angle", "Straight angle"],
                                        "correct_answer": "Obtuse angle",
                                        "rationale": "120° is more than 90° but less than 180°, so it's an obtuse angle.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "How many degrees is a straight angle?",
                                        "options": ["90°", "180°", "270°", "360°"],
                                        "correct_answer": "180°",
                                        "rationale": "A straight angle measures exactly 180 degrees.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What type of angle is 45°?",
                                        "options": ["Right angle", "Acute angle", "Obtuse angle", "Straight angle"],
                                        "correct_answer": "Acute angle",
                                        "rationale": "45° is less than 90°, so it's an acute angle.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What type of angle is 90°?",
                                        "options": ["Right angle", "Acute angle", "Obtuse angle", "Straight angle"],
                                        "correct_answer": "Right angle",
                                        "rationale": "90° is exactly a right angle.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            },
                            {
                                "module_id": 17,
                                "topic_name": "Perimeter and Area",
                                "explanation": "Perimeter is the fence around a shape, and area is the space inside! Perimeter = distance around the outside. Area of rectangle = length × width. Area of square = side × side. These concepts help you measure rooms, gardens, and playgrounds!",
                                "difficulty": "Hard",
                                "total_timer_minutes": 15,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is the perimeter of a rectangle 8 cm by 5 cm?",
                                        "options": ["13 cm", "26 cm", "40 cm", "53 cm"],
                                        "correct_answer": "26 cm",
                                        "rationale": "Perimeter = 2 × (8 + 5) = 2 × 13 = 26 cm.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is the area of a rectangle 6 cm by 4 cm?",
                                        "options": ["10 cm²", "20 cm²", "24 cm²", "30 cm²"],
                                        "correct_answer": "24 cm²",
                                        "rationale": "Area = 6 × 4 = 24 cm².",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is the perimeter of a square with side 7 cm?",
                                        "options": ["14 cm", "21 cm", "28 cm", "35 cm"],
                                        "correct_answer": "28 cm",
                                        "rationale": "Perimeter = 4 × 7 = 28 cm.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is the area of a square with side 9 cm?",
                                        "options": ["36 cm²", "49 cm²", "64 cm²", "81 cm²"],
                                        "correct_answer": "81 cm²",
                                        "rationale": "Area = 9 × 9 = 81 cm².",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is the perimeter of a rectangle 12 cm by 3 cm?",
                                        "options": ["15 cm", "30 cm", "36 cm", "45 cm"],
                                        "correct_answer": "30 cm",
                                        "rationale": "Perimeter = 2 × (12 + 3) = 2 × 15 = 30 cm.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is the area of a rectangle 10 cm by 7 cm?",
                                        "options": ["17 cm²", "50 cm²", "70 cm²", "100 cm²"],
                                        "correct_answer": "70 cm²",
                                        "rationale": "Area = 10 × 7 = 70 cm².",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is the perimeter of a square with side 11 cm?",
                                        "options": ["22 cm", "33 cm", "44 cm", "55 cm"],
                                        "correct_answer": "44 cm",
                                        "rationale": "Perimeter = 4 × 11 = 44 cm.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 8,
                                        "question_id": 8,
                                        "question_text": "What is the area of a square with side 8 cm?",
                                        "options": ["16 cm²", "32 cm²", "64 cm²", "80 cm²"],
                                        "correct_answer": "64 cm²",
                                        "rationale": "Area = 8 × 8 = 64 cm².",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 9,
                                        "question_text": "What is the perimeter of a rectangle 15 cm by 4 cm?",
                                        "options": ["19 cm", "38 cm", "60 cm", "79 cm"],
                                        "correct_answer": "38 cm",
                                        "rationale": "Perimeter = 2 × (15 + 4) = 2 × 19 = 38 cm.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 10,
                                        "question_text": "What is the area of a rectangle 9 cm by 6 cm?",
                                        "options": ["15 cm²", "45 cm²", "54 cm²", "63 cm²"],
                                        "correct_answer": "54 cm²",
                                        "rationale": "Area = 9 × 6 = 54 cm².",
                                        "timer_per_question_seconds": 60
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Data Handling",
                        "modules": [
                            {
                                "module_id": 18,
                                "topic_name": "Pictographs and Bar Graphs",
                                "explanation": "Graphs tell stories with pictures and bars! Pictographs use pictures to represent quantities. Bar graphs use bars of different heights to compare values. Both help you see patterns and compare information at a glance. They make data easy to understand and remember!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "In a pictograph, if 🍎 = 5 apples, what do 🍎🍎🍎 represent?",
                                        "options": ["10 apples", "15 apples", "20 apples", "25 apples"],
                                        "correct_answer": "15 apples",
                                        "rationale": "3 pictures × 5 apples each = 15 apples.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What do taller bars in a bar graph represent?",
                                        "options": ["Less quantity", "More quantity", "Equal quantity", "No pattern"],
                                        "correct_answer": "More quantity",
                                        "rationale": "Taller bars represent larger quantities or values.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "In a pictograph, if ⚽ = 3 balls, how many balls is ⚽⚽⚽⚽?",
                                        "options": ["9 balls", "12 balls", "15 balls", "18 balls"],
                                        "correct_answer": "12 balls",
                                        "rationale": "4 pictures × 3 balls each = 12 balls.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What should bars in a bar graph have?",
                                        "options": ["Different widths", "Same width", "Random heights", "No labels"],
                                        "correct_answer": "Same width",
                                        "rationale": "Bars in a bar graph should have the same width for accurate comparison.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "If one bar reaches 20 and another reaches 35, which represents more?",
                                        "options": ["The bar at 20", "The bar at 35", "They are equal", "Cannot say"],
                                        "correct_answer": "The bar at 35",
                                        "rationale": "The bar reaching 35 represents a larger quantity than the one at 20.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is the advantage of using graphs?",
                                        "options": ["To confuse data", "To make data visual", "To hide information", "To make calculations harder"],
                                        "correct_answer": "To make data visual",
                                        "rationale": "Graphs make data visual and easier to understand.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Patterns",
                        "modules": [
                            {
                                "module_id": 19,
                                "topic_name": "Number and Shape Patterns",
                                "explanation": "Patterns are like secret codes that repeat! Number patterns: 2, 4, 6, 8... (add 2 each time). Shape patterns: circle, square, circle, square... (repeat sequence). Some patterns grow, some shrink, and some rotate. Finding patterns helps you predict what comes next!",
                                "difficulty": "Medium",
                                "total_timer_minutes": 10,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What comes next: 5, 10, 15, 20, ?",
                                        "options": ["21", "22", "23", "25"],
                                        "correct_answer": "25",
                                        "rationale": "The pattern increases by 5 each time, so 20 + 5 = 25.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What comes next: 3, 6, 9, 12, ?",
                                        "options": ["13", "14", "15", "16"],
                                        "correct_answer": "15",
                                        "rationale": "The pattern increases by 3 each time, so 12 + 3 = 15.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What comes next: Circle, Triangle, Circle, Triangle, ?",
                                        "options": ["Circle", "Triangle", "Square", "Rectangle"],
                                        "correct_answer": "Circle",
                                        "rationale": "The pattern is Circle, Triangle, so Circle comes next.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What comes next: 100, 90, 80, 70, ?",
                                        "options": ["50", "60", "65", "75"],
                                        "correct_answer": "60",
                                        "rationale": "The pattern decreases by 10 each time, so 70 - 10 = 60.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What comes next: Red, Blue, Green, Red, Blue, ?",
                                        "options": ["Red", "Blue", "Green", "Yellow"],
                                        "correct_answer": "Green",
                                        "rationale": "The pattern is Red, Blue, Green, so Green comes next.",
                                        "timer_per_question_seconds": 45
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What comes next: 2, 4, 8, 16, ?",
                                        "options": ["20", "24", "30", "32"],
                                        "correct_answer": "32",
                                        "rationale": "The pattern doubles each time: 16 × 2 = 32.",
                                        "timer_per_question_seconds": 45
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "chapter_name": "Mental Mathematics",
                        "modules": [
                            {
                                "module_id": 20,
                                "topic_name": "Quick Calculation Strategies",
                                "explanation": "Mental math makes you a human calculator! For addition: 47 + 23 = (47 + 3) + 20 = 70. For multiplication: 25 × 4 = 100 (because 4 × 25 = 100). These tricks help you solve problems quickly and build confidence in math!",
                                "difficulty": "Hard",
                                "total_timer_minutes": 15,
                                "questions": [
                                    {
                                        "question_id": 1,
                                        "question_text": "What is 67 + 33 using mental math?",
                                        "options": ["90", "100", "110", "120"],
                                        "correct_answer": "100",
                                        "rationale": "67 + 33 = (67 + 3) + 30 = 70 + 30 = 100.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 2,
                                        "question_text": "What is 25 × 4 using mental math?",
                                        "options": ["50", "75", "100", "125"],
                                        "correct_answer": "100",
                                        "rationale": "25 × 4 = 100 (4 quarters make a dollar).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 3,
                                        "question_text": "What is 125 × 8 using mental math?",
                                        "options": ["500", "750", "1000", "1250"],
                                        "correct_answer": "1000",
                                        "rationale": "125 × 8 = 1000 (8 × 125 = 1000).",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 4,
                                        "question_text": "What is 82 - 47 using mental math?",
                                        "options": ["25", "35", "45", "55"],
                                        "correct_answer": "35",
                                        "rationale": "82 - 47 = (82 - 40) - 7 = 42 - 7 = 35.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 5,
                                        "question_text": "What is 50 × 20 using mental math?",
                                        "options": ["500", "1000", "1500", "2000"],
                                        "correct_answer": "1000",
                                        "rationale": "50 × 20 = 5 × 2 × 100 = 10 × 100 = 1000.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 6,
                                        "question_text": "What is 91 - 53 using mental math?",
                                        "options": ["28", "38", "48", "58"],
                                        "correct_answer": "38",
                                        "rationale": "91 - 53 = (91 - 50) - 3 = 41 - 3 = 38.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 7,
                                        "question_text": "What is 75 × 4 using mental math?",
                                        "options": ["200", "250", "300", "350"],
                                        "correct_answer": "300",
                                        "rationale": "75 × 4 = (50 + 25) × 4 = 200 + 100 = 300.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 8,
                                        "question_text": "What is 150 × 6 using mental math?",
                                        "options": ["700", "800", "900", "1000"],
                                        "correct_answer": "900",
                                        "rationale": "150 × 6 = (100 + 50) × 6 = 600 + 300 = 900.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 9,
                                        "question_text": "What is 73 - 28 using mental math?",
                                        "options": ["35", "45", "55", "65"],
                                        "correct_answer": "45",
                                        "rationale": "73 - 28 = (73 - 20) - 8 = 53 - 8 = 45.",
                                        "timer_per_question_seconds": 60
                                    },
                                    {
                                        "question_id": 10,
                                        "question_text": "What is 125 × 4 × 2 using mental math?",
                                        "options": ["500", "750", "1000", "1500"],
                                        "correct_answer": "1000",
                                        "rationale": "125 × 4 × 2 = 500 × 2 = 1000.",
                                        "timer_per_question_seconds": 60
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
    return curriculum

# Generate and save the curriculum
curriculum = create_class4_curriculum()
output_file = r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\learn-edu\class4_mathematics_curriculum.json"

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(curriculum, f, ensure_ascii=False, indent=2)

print(f"Class 4 Mathematics curriculum saved to {output_file}")
total_modules = sum(len(term['chapters']) for term in curriculum['terms'])
total_chapters = sum(len(chapter['modules']) for term in curriculum['terms'] for chapter in term['chapters'])
print(f"Total chapters created: {total_modules}")
print(f"Total modules created: {total_chapters}")

# Count actual questions
actual_questions = 0
for term in curriculum['terms']:
    for chapter in term['chapters']:
        for module in chapter['modules']:
            actual_questions += len(module['questions'])
print(f"Total questions generated: {actual_questions}")