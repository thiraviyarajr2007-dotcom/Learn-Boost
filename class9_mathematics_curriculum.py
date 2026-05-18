#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Mathematics Curriculum Generator - TN State Board
Transforms textbook content into Duolingo-style learning modules
Based on Class 9 Mathematics English 2025 Edition
"""

import json

def generate_class9_curriculum():
    """Generate comprehensive Class 9 Mathematics curriculum"""
    
    curriculum = {
        "class": "9",
        "subject": "Mathematics",
        "chapters": [
            {
                "chapter_name": "SET LANGUAGE",
                "modules": [
                    {
                        "module_id": "9.1.1",
                        "topic_name": "Introduction to Sets",
                        "explanation": "Sets are like organized collections of objects! Think of a set as a special box where you group similar items together - like a box of fruits, a collection of books, or a group of students in a class. In mathematics, sets help us organize and study collections of numbers, shapes, or other mathematical objects. Understanding sets is fundamental to modern mathematics and helps in logical thinking!",
                        "difficulty": "easy",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "9_1_1_1",
                                "question_text": "What is a set in mathematics?",
                                "options": ["A collection of well-defined objects", "A random group of items", "A single number", "A mathematical operation"],
                                "correct_answer": "A collection of well-defined objects",
                                "rationale": "A set is a well-defined collection of distinct objects, considered as an object in its own right.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "9_1_1_2",
                                "question_text": "Which of these is an example of a set?",
                                "options": ["All tall people", "Students in your class", "Beautiful paintings", "Good books"],
                                "correct_answer": "Students in your class",
                                "rationale": "Students in your class is a well-defined collection where we can clearly determine membership.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "9_1_1_3",
                                "question_text": "What symbol is used to denote 'belongs to' in set theory?",
                                "options": ["∈", "⊂", "∪", "∩"],
                                "correct_answer": "∈",
                                "rationale": "The symbol ∈ means 'belongs to' or 'is an element of' in set notation.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "9_1_1_4",
                                "question_text": "If 5 ∈ A, what does this mean?",
                                "options": ["5 is an element of set A", "5 is not in set A", "A contains 5 elements", "5 is the first element of A"],
                                "correct_answer": "5 is an element of set A",
                                "rationale": "The notation 5 ∈ A means that 5 is an element or member of set A.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "9_1_1_5",
                                "question_text": "Which of these is NOT a characteristic of a set?",
                                "options": ["Elements are well-defined", "Elements are distinct", "Order doesn't matter", "Elements must be numbers"],
                                "correct_answer": "Elements must be numbers",
                                "rationale": "Set elements can be any objects - numbers, letters, shapes, etc., not just numbers.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "9_1_1_6",
                                "question_text": "What do we call the objects in a set?",
                                "options": ["Elements", "Members", "Both elements and members", "Numbers"],
                                "correct_answer": "Both elements and members",
                                "rationale": "Objects in a set are called both elements and members - these terms are interchangeable.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "9_1_1_7",
                                "question_text": "If A = {a, b, c}, how many elements does set A have?",
                                "options": ["3", "2", "1", "0"],
                                "correct_answer": "3",
                                "rationale": "Set A has three elements: a, b, and c.",
                                "timer_per_question_seconds": 30
                            },
                            {
                                "question_id": "9_1_1_8",
                                "question_text": "What is the purpose of studying sets in mathematics?",
                                "options": ["To organize and classify objects", "To make calculations harder", "To memorize formulas", "To draw graphs"],
                                "correct_answer": "To organize and classify objects",
                                "rationale": "Sets help us organize, classify, and study collections of mathematical objects systematically.",
                                "timer_per_question_seconds": 30
                            }
                        ]
                    },
                    {
                        "module_id": "9.1.2",
                        "topic_name": "Representation of Sets",
                        "explanation": "Sets can be written in different ways, just like describing something in multiple languages! We use roster form (listing all elements), set-builder form (describing properties), and Venn diagrams (visual representation). Each method has its advantages - roster form is simple, set-builder form is precise, and Venn diagrams make relationships clear. Choose the method that best suits your needs!",
                        "difficulty": "medium",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "9_1_2_1",
                                "question_text": "What is roster form of set representation?",
                                "options": ["Listing all elements in curly braces", "Describing properties of elements", "Drawing circles", "Using inequalities"],
                                "correct_answer": "Listing all elements in curly braces",
                                "rationale": "Roster form lists all elements of a set within curly braces, separated by commas.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_2",
                                "question_text": "Which set is written in roster form?",
                                "options": ["{1, 2, 3, 4, 5}", "{x | x is a natural number ≤ 5}", "All prime numbers", "Numbers from 1 to 5"],
                                "correct_answer": "{1, 2, 3, 4, 5}",
                                "rationale": "This shows roster form with actual elements listed in curly braces.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_3",
                                "question_text": "What does {x | x is an even number} represent?",
                                "options": ["Set of all even numbers", "Only the number x", "The letter x", "Even and odd numbers"],
                                "correct_answer": "Set of all even numbers",
                                "rationale": "This is set-builder form meaning 'the set of all x such that x is an even number'.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_4",
                                "question_text": "How would you write the set of vowels in roster form?",
                                "options": ["{a, e, i, o, u}", "{x | x is a vowel}", "All vowels", "Vowel letters"],
                                "correct_answer": "{a, e, i, o, u}",
                                "rationale": "Roster form lists all the vowel letters in curly braces.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_5",
                                "question_text": "What is the set-builder form of {2, 4, 6, 8}?",
                                "options": ["{x | x is an even number ≤ 8}", "{x | x = 2n}", "{2, 4, 6, 8}", "Even numbers"],
                                "correct_answer": "{x | x is an even number ≤ 8}",
                                "rationale": "This describes the property that defines the elements of the set.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_6",
                                "question_text": "Which symbol separates the variable from the condition in set-builder form?",
                                "options": ["|", ":", ",", "-"],
                                "correct_answer": "|",
                                "rationale": "The vertical bar | means 'such that' in set-builder notation, separating the variable from its defining property.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_7",
                                "question_text": "What is the roster form of {x | x is a natural number < 4}?",
                                "options": ["{1, 2, 3}", "{0, 1, 2, 3}", "{1, 2, 3, 4}", "{0, 1, 2, 3, 4}"],
                                "correct_answer": "{1, 2, 3}",
                                "rationale": "Natural numbers less than 4 are 1, 2, and 3.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_8",
                                "question_text": "When is set-builder form more useful than roster form?",
                                "options": ["For infinite sets", "For small sets", "For empty sets", "For single-element sets"],
                                "correct_answer": "For infinite sets",
                                "rationale": "Set-builder form is better for infinite sets because you can't list all elements in roster form.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_9",
                                "question_text": "What does {} represent?",
                                "options": ["Empty set", "Set with zero", "Set containing nothing", "All of the above"],
                                "correct_answer": "All of the above",
                                "rationale": "Empty curly braces represent the empty set, which contains no elements.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_2_10",
                                "question_text": "How would you represent 'all integers greater than 5' in set-builder form?",
                                "options": ["{x | x ∈ ℤ, x > 5}", "{x | x > 5}", "{6, 7, 8, ...}", "ℤ⁺"],
                                "correct_answer": "{x | x ∈ ℤ, x > 5}",
                                "rationale": "This properly specifies that x is an integer and greater than 5.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "9.1.3",
                        "topic_name": "Types of Sets",
                        "explanation": "Sets come in different flavors, just like ice cream! Empty sets have no elements, singleton sets have exactly one element, finite sets have countable elements, and infinite sets go on forever. Universal sets contain all possible elements in a given context, and equal sets have exactly the same elements. Understanding these types helps you work with sets more effectively!",
                        "difficulty": "medium",
                        "total_timer_minutes": 10,
                        "questions": [
                            {
                                "question_id": "9_1_3_1",
                                "question_text": "What is an empty set?",
                                "options": ["A set with no elements", "A set with one element", "A set with many elements", "A set with zero"],
                                "correct_answer": "A set with no elements",
                                "rationale": "An empty set (or null set) contains no elements, denoted by {} or ∅.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_2",
                                "question_text": "Which symbol represents the empty set?",
                                "options": ["∅", "∞", "∈", "⊂"],
                                "correct_answer": "∅",
                                "rationale": "The symbol ∅ (phi) represents the empty set.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_3",
                                "question_text": "What is a singleton set?",
                                "options": ["A set with exactly one element", "An empty set", "A set with two elements", "A universal set"],
                                "correct_answer": "A set with exactly one element",
                                "rationale": "A singleton set contains exactly one element.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_4",
                                "question_text": "Which of these is a singleton set?",
                                "options": ["{5}", "{1, 2}", "{}", "ℕ"],
                                "correct_answer": "{5}",
                                "rationale": "{5} contains exactly one element (the number 5), making it a singleton set.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_5",
                                "question_text": "What is the difference between finite and infinite sets?",
                                "options": ["Countable vs uncountable elements", "Small vs large elements", "Numbered vs lettered elements", "Important vs unimportant elements"],
                                "correct_answer": "Countable vs uncountable elements",
                                "rationale": "Finite sets have countable elements, infinite sets have uncountably many elements.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_6",
                                "question_text": "Which of these is an infinite set?",
                                "options": ["Set of natural numbers", "Set of students in a class", "Set of days in a week", "Set of letters in alphabet"],
                                "correct_answer": "Set of natural numbers",
                                "rationale": "Natural numbers continue infinitely, making it an infinite set.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_7",
                                "question_text": "What is a universal set?",
                                "options": ["Set containing all elements in context", "Empty set", "Set with one element", "Set of all numbers"],
                                "correct_answer": "Set containing all elements in context",
                                "rationale": "Universal set contains all possible elements under consideration for a particular discussion.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_8",
                                "question_text": "When are two sets equal?",
                                "options": ["When they have exactly the same elements", "When they have the same number of elements", "When they have similar elements", "When they are both empty"],
                                "correct_answer": "When they have exactly the same elements",
                                "rationale": "Two sets are equal if and only if they contain exactly the same elements.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_9",
                                "question_text": "If A = {1, 2, 3} and B = {3, 2, 1}, what is the relationship between A and B?",
                                "options": ["A = B", "A ⊂ B", "B ⊂ A", "A ∩ B = ∅"],
                                "correct_answer": "A = B",
                                "rationale": "Sets A and B have exactly the same elements, so they are equal sets.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_1_3_10",
                                "question_text": "What is the cardinality of the empty set?",
                                "options": ["0", "1", "∞", "Undefined"],
                                "correct_answer": "0",
                                "rationale": "The cardinality (number of elements) of the empty set is 0.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    },
                    {
                        "module_id": "9.1.4",
                        "topic_name": "Set Operations",
                        "explanation": "Set operations are like mathematical tools for combining and comparing sets! Union (∪) combines all elements, intersection (∩) finds common elements, difference (-) removes elements, and complement finds what's missing. These operations help solve problems involving multiple groups and relationships. Think of them as ways to mix, match, and separate collections!",
                        "difficulty": "hard",
                        "total_timer_minutes": 12,
                        "questions": [
                            {
                                "question_id": "9_1_4_1",
                                "question_text": "What is the union of sets A and B?",
                                "options": ["All elements in A or B or both", "Only common elements", "Elements in A not in B", "Elements in B not in A"],
                                "correct_answer": "All elements in A or B or both",
                                "rationale": "Union A ∪ B contains all elements that are in A, or in B, or in both.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_2",
                                "question_text": "If A = {1, 2, 3} and B = {3, 4, 5}, what is A ∪ B?",
                                "options": ["{1, 2, 3, 4, 5}", "{1, 2, 4, 5}", "{3}", "{1, 2, 3}"],
                                "correct_answer": "{1, 2, 3, 4, 5}",
                                "rationale": "Union includes all unique elements from both sets: 1, 2, 3, 4, 5.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_3",
                                "question_text": "What is the intersection of sets A and B?",
                                "options": ["Elements common to both A and B", "All elements in A and B", "Elements in A not in B", "Elements in B not in A"],
                                "correct_answer": "Elements common to both A and B",
                                "rationale": "Intersection A ∩ B contains only elements that are in both A and B.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_4",
                                "question_text": "If A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, what is A ∩ B?",
                                "options": ["{3, 4}", "{1, 2, 5, 6}", "{1, 2, 3, 4, 5, 6}", "∅"],
                                "correct_answer": "{3, 4}",
                                "rationale": "The common elements between A and B are 3 and 4.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_5",
                                "question_text": "What does A - B represent?",
                                "options": ["Elements in A not in B", "Elements in B not in A", "Common elements", "All elements"],
                                "correct_answer": "Elements in A not in B",
                                "rationale": "Set difference A - B contains elements that are in A but not in B.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_6",
                                "question_text": "If A = {1, 2, 3, 4, 5} and B = {3, 4}, what is A - B?",
                                "options": ["{1, 2, 5}", "{3, 4}", "{1, 2, 3, 4, 5}", "∅"],
                                "correct_answer": "{1, 2, 5}",
                                "rationale": "Remove elements 3 and 4 from A, leaving {1, 2, 5}.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_7",
                                "question_text": "What is the complement of set A?",
                                "options": ["All elements not in A (in universal set)", "Elements in A", "Empty set", "Universal set"],
                                "correct_answer": "All elements not in A (in universal set)",
                                "rationale": "Complement of A contains all elements in the universal set that are not in A.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_8",
                                "question_text": "If U = {1, 2, 3, 4, 5, 6} and A = {1, 2, 3}, what is A'?",
                                "options": ["{4, 5, 6}", "{1, 2, 3}", "∅", "U"],
                                "correct_answer": "{4, 5, 6}",
                                "rationale": "Complement A' contains elements in U not in A: 4, 5, 6.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_9",
                                "question_text": "What is A ∩ A'?",
                                "options": ["∅", "A", "U", "A'"],
                                "correct_answer": "∅",
                                "rationale": "A set and its complement have no common elements, so their intersection is empty.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_10",
                                "question_text": "What is A ∪ A'?",
                                "options": ["U", "A", "∅", "A'"],
                                "correct_answer": "U",
                                "rationale": "A set and its complement together contain all elements of the universal set.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_11",
                                "question_text": "If A = {a, b, c, d} and B = {c, d, e, f}, what is (A ∪ B)'?",
                                "options": ["Elements not in {a, b, c, d, e, f}", "{a, b, e, f}", "{c, d}", "∅"],
                                "correct_answer": "Elements not in {a, b, c, d, e, f}",
                                "rationale": "First find A ∪ B = {a, b, c, d, e, f}, then take complement.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_4_12",
                                "question_text": "Which operation is distributive over union?",
                                "options": ["Intersection", "Difference", "Complement", "None"],
                                "correct_answer": "Intersection",
                                "rationale": "Intersection distributes over union: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    },
                    {
                        "module_id": "9.1.5",
                        "topic_name": "Properties of Set Operations",
                        "explanation": "Set operations follow beautiful rules that make them predictable and useful! Commutative means order doesn't matter (A ∪ B = B ∪ A), associative means grouping doesn't matter, distributive shows how operations interact, and De Morgan's laws connect unions and intersections with complements. These properties are like traffic rules for sets - they keep everything organized and consistent!",
                        "difficulty": "hard",
                        "total_timer_minutes": 12,
                        "questions": [
                            {
                                "question_id": "9_1_5_1",
                                "question_text": "What does the commutative property state for set union?",
                                "options": ["A ∪ B = B ∪ A", "A ∪ (B ∪ C) = (A ∪ B) ∪ C", "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)", "A ∪ A' = U"],
                                "correct_answer": "A ∪ B = B ∪ A",
                                "rationale": "Commutative property means the order of operands doesn't affect the result.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_2",
                                "question_text": "Which operation is NOT commutative?",
                                "options": ["Set difference", "Union", "Intersection", "Symmetric difference"],
                                "correct_answer": "Set difference",
                                "rationale": "A - B ≠ B - A in general, so set difference is not commutative.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_3",
                                "question_text": "What does the associative property allow?",
                                "options": ["Changing grouping of operations", "Changing order of operands", "Distributing operations", "Taking complements"],
                                "correct_answer": "Changing grouping of operations",
                                "rationale": "Associative property allows regrouping without changing the result.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_4",
                                "question_text": "Which is the associative law for union?",
                                "options": ["A ∪ (B ∪ C) = (A ∪ B) ∪ C", "A ∪ B = B ∪ A", "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)", "A ∪ A = A"],
                                "correct_answer": "A ∪ (B ∪ C) = (A ∪ B) ∪ C",
                                "rationale": "This shows that grouping doesn't matter in union operations.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_5",
                                "question_text": "What is the distributive property of intersection over union?",
                                "options": ["A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)", "A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)", "A ∩ B = B ∩ A", "A ∪ B = B ∪ A"],
                                "correct_answer": "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)",
                                "rationale": "This shows how intersection distributes over union operations.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_6",
                                "question_text": "What is De Morgan's first law?",
                                "options": ["(A ∪ B)' = A' ∩ B'", "(A ∩ B)' = A' ∪ B'", "A ∪ A' = U", "A ∩ A' = ∅"],
                                "correct_answer": "(A ∪ B)' = A' ∩ B'",
                                "rationale": "De Morgan's first law relates complement of union to intersection of complements.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_7",
                                "question_text": "What is De Morgan's second law?",
                                "options": ["(A ∩ B)' = A' ∪ B'", "(A ∪ B)' = A' ∩ B'", "A ∪ A' = U", "A ∩ A' = ∅"],
                                "correct_answer": "(A ∩ B)' = A' ∪ B'",
                                "rationale": "De Morgan's second law relates complement of intersection to union of complements.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_8",
                                "question_text": "What is the identity element for union?",
                                "options": ["Empty set", "Universal set", "Set itself", "Complement"],
                                "correct_answer": "Empty set",
                                "rationale": "A ∪ ∅ = A for any set A, so empty set is the identity for union.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_9",
                                "question_text": "What is the identity element for intersection?",
                                "options": ["Universal set", "Empty set", "Set itself", "Complement"],
                                "correct_answer": "Universal set",
                                "rationale": "A ∩ U = A for any set A, so universal set is the identity for intersection.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_10",
                                "question_text": "Which property states A ∪ A = A?",
                                "options": ["Idempotent", "Commutative", "Associative", "Distributive"],
                                "correct_answer": "Idempotent",
                                "rationale": "Idempotent property means an operation with itself yields the same result.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_11",
                                "question_text": "What does A ∩ A' always equal?",
                                "options": ["∅", "U", "A", "A'"],
                                "correct_answer": "∅",
                                "rationale": "A set and its complement have no common elements, so their intersection is always empty.",
                                "timer_per_question_seconds": 60
                            },
                            {
                                "question_id": "9_1_5_12",
                                "question_text": "What does A ∪ A' always equal?",
                                "options": ["U", "∅", "A", "A'"],
                                "correct_answer": "U",
                                "rationale": "A set and its complement together contain all elements of the universal set.",
                                "timer_per_question_seconds": 60
                            }
                        ]
                    }
                ]
            },
            {
                "chapter_name": "REAL NUMBERS",
                "modules": [
                    {
                        "module_id": "9.2.1",
                        "topic_name": "Introduction to Real Numbers",
                        "explanation": "Real numbers are like a complete number line that includes everything! They contain rational numbers (fractions and terminating/repeating decimals) and irrational numbers (non-repeating decimals like π and √2). Think of them as all the numbers you can find on a number line - from negative infinity to positive infinity, with no gaps!",
                        "difficulty": "medium",
                        "total_timer_minutes": 8,
                        "questions": [
                            {
                                "question_id": "9_2_1_1",
                                "question_text": "What are real numbers?",
                                "options": ["All numbers on the number line", "Only whole numbers", "Only fractions", "Only positive numbers"],
                                "correct_answer": "All numbers on the number line",
                                "rationale": "Real numbers include all numbers that can be represented on the number line.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_2_1_2",
                                "question_text": "Which of these is NOT a real number?",
                                "options": ["√-1", "π", "√2", "3.14"],
                                "correct_answer": "√-1",
                                "rationale": "√-1 is imaginary, not real. Real numbers don't include imaginary numbers.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_2_1_3",
                                "question_text": "What are the two main types of real numbers?",
                                "options": ["Rational and irrational", "Whole and decimal", "Positive and negative", "Integer and fraction"],
                                "correct_answer": "Rational and irrational",
                                "rationale": "Real numbers are classified as rational (can be expressed as fractions) or irrational (cannot).",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_2_1_4",
                                "question_text": "What makes a number rational?",
                                "options": ["Can be expressed as a fraction", "Cannot be expressed as a fraction", "Is always whole", "Is always decimal"],
                                "correct_answer": "Can be expressed as a fraction",
                                "rationale": "Rational numbers can be written as the ratio of two integers.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_2_1_5",
                                "question_text": "Which of these is an irrational number?",
                                "options": ["π", "3/4", "0.25", "-7"],
                                "correct_answer": "π",
                                "rationale": "π cannot be expressed as a fraction and has non-repeating, non-terminating decimal expansion.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_2_1_6",
                                "question_text": "What type of number is √9?",
                                "options": ["Rational", "Irrational", "Imaginary", "Complex"],
                                "correct_answer": "Rational",
                                "rationale": "√9 = 3, which is rational since it can be expressed as 3/1.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_2_1_7",
                                "question_text": "What type of number is √2?",
                                "options": ["Irrational", "Rational", "Integer", "Whole"],
                                "correct_answer": "Irrational",
                                "rationale": "√2 cannot be expressed as a fraction and has non-repeating decimal expansion.",
                                "timer_per_question_seconds": 45
                            },
                            {
                                "question_id": "9_2_1_8",
                                "question_text": "Are all integers real numbers?",
                                "options": ["Yes", "No", "Only positive integers", "Only negative integers"],
                                "correct_answer": "Yes",
                                "rationale": "All integers are real numbers since they can be represented on the number line.",
                                "timer_per_question_seconds": 45
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
    return curriculum

def save_class9_curriculum_to_json():
    """Save the curriculum to a JSON file"""
    curriculum = generate_class9_curriculum()
    
    with open('class9_mathematics_curriculum.json', 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    
    print("Class 9 Mathematics curriculum saved to 'class9_mathematics_curriculum.json'")
    
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
    save_class9_curriculum_to_json()