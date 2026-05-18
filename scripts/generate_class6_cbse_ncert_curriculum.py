import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "class6_cbse_ncert_duolingo_curriculum.json"


def make_question(qid, text, options, answer, rationale, seconds):
    return {
        "question_id": qid,
        "question_text": text,
        "options": options,
        "correct_answer": answer,
        "rationale": rationale,
        "timer_per_question_seconds": seconds,
    }


def make_module(mid, topic, explanation, difficulty, minutes, questions):
    seconds = {"Easy": 30, "Medium": 45, "Hard": 60}[difficulty]
    return {
        "module_id": mid,
        "topic_name": topic,
        "explanation": explanation,
        "difficulty": difficulty,
        "total_timer_minutes": minutes,
        "questions": [
            make_question(i + 1, item[0], item[1], item[2], item[3], seconds)
            for i, item in enumerate(questions)
        ],
    }


chapters = [
    {
        "chapter_name": "Knowing Our Numbers",
        "modules": [
            make_module(1, "Comparing, Arranging and Place Value",
                "Large numbers are easier when we read them place by place. Digits get their value from where they sit: ones, tens, hundreds, thousands, lakhs and crores. To compare numbers, first count digits; the number with more digits is greater. If digits are equal in number, compare from the left. Commas and place-value boxes help us read, write and expand big numbers clearly.",
                "Medium", 8, [
                    ("Which is the greatest number: 92, 392, 4456, 89742?", ["92", "392", "4456", "89742"], "89742", "It has the most digits, so it is greatest."),
                    ("The smallest 5-digit number is", ["9999", "10000", "100000", "1000"], "10000", "Adding 1 to 9999 gives 10000."),
                    ("In 45,278, the digit 4 is in the", ["ones place", "hundreds place", "thousands place", "ten thousands place"], "ten thousands place", "The leftmost digit 4 represents 4 ten thousands."),
                    ("Ascending order means arranging from", ["greatest to smallest", "smallest to greatest", "left to right only", "odd to even"], "smallest to greatest", "Ascending order goes upward from small to large."),
                    ("In Indian numeration, the first comma from the right comes after", ["one digit", "two digits", "three digits", "four digits"], "three digits", "The first comma marks thousands after the hundreds place."),
                ]),
            make_module(2, "Estimation, Brackets and Roman Numerals",
                "Estimation gives a quick, sensible answer without exact calculation. We round numbers to nearest tens, hundreds or thousands to make mental work easier. Brackets tell us which part to do first. Roman numerals use letters such as I, V, X, L and C to write numbers. These tools help in checking answers, simplifying expressions and reading older number systems.",
                "Medium", 8, [
                    ("Rounding 68 to the nearest ten gives", ["60", "70", "80", "100"], "70", "68 is closer to 70 than to 60."),
                    ("Rounding 348 to the nearest hundred gives", ["300", "340", "350", "400"], "300", "348 is less than halfway to 400."),
                    ("In 5 x (3 + 2), which part is done first?", ["5 x 3", "3 + 2", "5 + 2", "No part"], "3 + 2", "Brackets are solved first."),
                    ("The Roman numeral X stands for", ["5", "10", "50", "100"], "10", "X represents ten."),
                    ("The Roman numeral IV stands for", ["4", "6", "9", "11"], "4", "I before V means one less than five."),
                ]),
        ],
    },
    {
        "chapter_name": "Whole Numbers",
        "modules": [
            make_module(1, "Whole Numbers and Number Line",
                "Whole numbers are 0, 1, 2, 3 and so on. They begin at zero and continue forever. On a number line, numbers increase as we move right. Addition means jumping right, subtraction means jumping left, and multiplication can be shown as repeated equal jumps. The number line makes whole-number operations visible and friendly.",
                "Easy", 7, [
                    ("Which is the smallest whole number?", ["0", "1", "-1", "10"], "0", "Whole numbers begin from zero."),
                    ("The successor of 999 is", ["998", "999", "1000", "1001"], "1000", "Successor means the next number."),
                    ("The predecessor of 100 is", ["99", "100", "101", "0"], "99", "Predecessor means one less."),
                    ("On a number line, numbers increase when we move", ["left", "right", "down", "nowhere"], "right", "Greater whole numbers are to the right."),
                    ("3 + 4 on a number line means", ["4 jumps left from 3", "4 jumps right from 3", "3 jumps left from 4", "No jump"], "4 jumps right from 3", "Addition moves right."),
                ]),
            make_module(2, "Properties and Patterns in Whole Numbers",
                "Whole numbers follow useful properties. Addition and multiplication are closed, commutative and associative for whole numbers. Zero is the additive identity because adding zero changes nothing. One is the multiplicative identity because multiplying by one changes nothing. Patterns in whole numbers help us notice rules and build confidence with calculations.",
                "Medium", 8, [
                    ("Which is the additive identity for whole numbers?", ["0", "1", "10", "100"], "0", "Adding 0 leaves the number unchanged."),
                    ("Which is the multiplicative identity?", ["0", "1", "2", "10"], "1", "Multiplying by 1 leaves the number unchanged."),
                    ("Which property is shown by 4 + 7 = 7 + 4?", ["Closure", "Commutative property", "Associative property", "Distributive property"], "Commutative property", "The order changes but the sum is the same."),
                    ("What is 25 x 0?", ["0", "1", "25", "250"], "0", "Any whole number multiplied by zero is zero."),
                    ("Which operation is not closed for whole numbers?", ["Addition", "Multiplication", "Subtraction", "Adding zero"], "Subtraction", "For example, 3 - 5 is not a whole number."),
                ]),
        ],
    },
    {
        "chapter_name": "Playing With Numbers",
        "modules": [
            make_module(1, "Factors, Multiples, Prime and Composite Numbers",
                "Factors divide a number exactly, while multiples are products of a number. For example, factors of 6 are 1, 2, 3 and 6, and multiples of 6 include 6, 12 and 18. A prime number has exactly two factors, 1 and itself. A composite number has more than two factors. These ideas are like the building blocks of numbers.",
                "Medium", 8, [
                    ("Which is a factor of 12?", ["5", "7", "3", "10"], "3", "12 divided by 3 leaves no remainder."),
                    ("Which is a multiple of 8?", ["12", "16", "18", "22"], "16", "16 = 8 x 2."),
                    ("A prime number has exactly", ["one factor", "two factors", "three factors", "no factors"], "two factors", "A prime has factors 1 and itself."),
                    ("Which number is composite?", ["2", "3", "5", "9"], "9", "9 has factors 1, 3 and 9."),
                    ("1 is", ["prime", "composite", "neither prime nor composite", "even only"], "neither prime nor composite", "It has only one factor."),
                ]),
            make_module(2, "Divisibility, Prime Factorisation, HCF and LCM",
                "Divisibility rules help us check division quickly. Prime factorisation breaks a number into prime-number building blocks. HCF is the greatest common factor shared by numbers, while LCM is the smallest common multiple. These tools help solve sharing, grouping and timing problems without listing too many numbers.",
                "Hard", 10, [
                    ("A number is divisible by 2 if its ones digit is", ["odd", "even", "5", "9"], "even", "Numbers ending in 0, 2, 4, 6 or 8 are divisible by 2."),
                    ("A number is divisible by 5 if it ends in", ["0 or 5", "2 or 4", "3 or 6", "1 or 9"], "0 or 5", "This is the divisibility rule for 5."),
                    ("Prime factorisation of 12 is", ["2 x 2 x 3", "2 x 6", "3 x 4", "1 x 12"], "2 x 2 x 3", "All factors in prime factorisation must be prime."),
                    ("HCF of 6 and 8 is", ["1", "2", "6", "24"], "2", "2 is the greatest factor common to both."),
                    ("LCM of 4 and 6 is", ["2", "6", "12", "24"], "12", "12 is the smallest common multiple of 4 and 6."),
                ]),
        ],
    },
    {
        "chapter_name": "Basic Geometrical Ideas",
        "modules": [
            make_module(1, "Points, Lines, Line Segments and Curves",
                "Geometry begins with simple ideas. A point shows an exact position. A line segment has two end points, while a line extends endlessly in both directions. Intersecting lines meet, and parallel lines never meet. Curves may be open or closed. These basic ideas help us describe maps, drawings, shapes and objects around us.",
                "Easy", 7, [
                    ("A point shows", ["an exact position", "a long path", "a surface", "a solid"], "an exact position", "A point marks a location."),
                    ("A line segment has", ["no end points", "one end point", "two end points", "three end points"], "two end points", "A segment is a part of a line with two ends."),
                    ("Parallel lines", ["always meet", "never meet", "form circles", "have one endpoint"], "never meet", "Parallel lines remain the same distance apart."),
                    ("Intersecting lines", ["meet at a point", "never meet", "are always curved", "are always equal"], "meet at a point", "Intersecting means crossing or meeting."),
                    ("A closed curve", ["has open ends", "does not enclose space", "joins back to itself", "is always straight"], "joins back to itself", "A closed curve has no open end."),
                ]),
            make_module(2, "Polygons, Angles, Triangles and Quadrilaterals",
                "A polygon is a closed figure made of line segments. Triangles have three sides, quadrilaterals have four sides, and circles are not polygons because they are curved. An angle is formed when two rays meet at a point. These shape names are the vocabulary students need before measuring and constructing figures.",
                "Medium", 8, [
                    ("A polygon is made of", ["curves only", "line segments", "dots only", "numbers"], "line segments", "Polygons are closed figures made from line segments."),
                    ("A triangle has", ["2 sides", "3 sides", "4 sides", "5 sides"], "3 sides", "Tri means three."),
                    ("A quadrilateral has", ["3 sides", "4 sides", "5 sides", "6 sides"], "4 sides", "Quad means four."),
                    ("An angle is formed by", ["two rays with a common endpoint", "two numbers", "one point only", "a closed curve only"], "two rays with a common endpoint", "The common endpoint is the vertex."),
                    ("Which is not a polygon?", ["Triangle", "Rectangle", "Circle", "Pentagon"], "Circle", "A circle is curved, not made of line segments."),
                ]),
        ],
    },
    {
        "chapter_name": "Understanding Elementary Shapes",
        "modules": [
            make_module(1, "Measuring Line Segments and Angles",
                "To compare shapes, we measure them. A ruler measures line segments. Angles can be right, straight, acute, obtuse or reflex, and a protractor measures them in degrees. A right angle is 90 degrees and a straight angle is 180 degrees. Measurement turns a rough drawing into clear mathematical information.",
                "Medium", 8, [
                    ("A ruler is used to measure", ["angles", "line segments", "weight", "time"], "line segments", "Rulers measure length."),
                    ("A right angle measures", ["45 degrees", "90 degrees", "180 degrees", "360 degrees"], "90 degrees", "A right angle is one quarter turn."),
                    ("A straight angle measures", ["90 degrees", "120 degrees", "180 degrees", "360 degrees"], "180 degrees", "A straight angle makes a straight line."),
                    ("An acute angle is", ["less than 90 degrees", "equal to 90 degrees", "more than 90 and less than 180 degrees", "equal to 180 degrees"], "less than 90 degrees", "Acute angles are smaller than a right angle."),
                    ("A protractor measures", ["area", "angle", "mass", "volume"], "angle", "Angles are measured with a protractor."),
                ]),
            make_module(2, "Triangles, Quadrilaterals, Polygons and 3-D Shapes",
                "Shapes can be classified by sides, angles and surfaces. Triangles may be classified by sides or by angles. Quadrilaterals include squares, rectangles and other four-sided figures. Polygons are flat closed shapes made of line segments. Three-dimensional shapes such as cubes, cuboids, cones and cylinders have faces, edges and vertices.",
                "Medium", 9, [
                    ("An equilateral triangle has", ["all sides equal", "two sides equal", "no equal sides", "four sides"], "all sides equal", "Equilateral means all sides are equal."),
                    ("A scalene triangle has", ["all sides equal", "two equal sides", "no equal sides", "four equal sides"], "no equal sides", "Scalene triangles have all sides different."),
                    ("A rectangle is a", ["triangle", "quadrilateral", "circle", "line"], "quadrilateral", "It has four sides."),
                    ("A cube is a", ["2-D shape", "3-D shape", "line segment", "curve"], "3-D shape", "A cube has length, breadth and height."),
                    ("A polygon with five sides is called a", ["triangle", "quadrilateral", "pentagon", "hexagon"], "pentagon", "Penta means five."),
                ]),
        ],
    },
    {
        "chapter_name": "Integers",
        "modules": [
            make_module(1, "Integers and the Number Line",
                "Integers include positive numbers, negative numbers and zero. They help describe situations in opposite directions, such as profit and loss, above and below sea level, or temperatures above and below zero. On the number line, positive integers are to the right of zero and negative integers are to the left.",
                "Medium", 8, [
                    ("Which is an integer?", ["1/2", "-5", "0.4", "2.5"], "-5", "Negative whole numbers are integers."),
                    ("On a number line, -3 lies", ["right of 0", "left of 0", "at 0", "above 0"], "left of 0", "Negative integers lie to the left of zero."),
                    ("Which integer is greater: -2 or -5?", ["-2", "-5", "Both equal", "Cannot compare"], "-2", "-2 is closer to zero and lies to the right of -5."),
                    ("The opposite of 7 is", ["0", "1", "-7", "14"], "-7", "Opposite integers are the same distance from zero on opposite sides."),
                    ("Zero is", ["positive", "negative", "neither positive nor negative", "only negative"], "neither positive nor negative", "Zero separates positive and negative integers."),
                ]),
            make_module(2, "Addition and Subtraction of Integers",
                "Adding a positive integer moves right on the number line, and adding a negative integer moves left. Subtracting an integer can be understood as moving in the opposite direction. These rules make integer operations easier and connect directly to real-life gains, losses, climbs and drops.",
                "Medium", 9, [
                    ("What is 3 + (-5)?", ["8", "-8", "-2", "2"], "-2", "Move 5 steps left from 3."),
                    ("What is -4 + 6?", ["-10", "10", "2", "-2"], "2", "Move 6 steps right from -4."),
                    ("What is -3 + (-2)?", ["5", "-5", "1", "-1"], "-5", "Two negative jumps move farther left."),
                    ("What is 5 - 8?", ["13", "3", "-3", "-13"], "-3", "Moving 8 left from 5 reaches -3."),
                    ("Adding zero to an integer gives", ["zero always", "the same integer", "a positive number", "a negative number"], "the same integer", "Zero does not change the value."),
                ]),
        ],
    },
    {
        "chapter_name": "Fractions",
        "modules": [
            make_module(1, "Meaning, Number Line and Types of Fractions",
                "A fraction shows a part of a whole or a part of a group. The denominator tells how many equal parts the whole has, and the numerator tells how many parts are taken. Fractions can be shown on a number line. Proper fractions are less than one, while improper fractions are one or more than one and can be written as mixed fractions.",
                "Medium", 8, [
                    ("In 3/5, the denominator is", ["3", "5", "8", "2"], "5", "The denominator tells the number of equal parts."),
                    ("A proper fraction is", ["less than 1", "always more than 1", "always equal to 1", "never on a number line"], "less than 1", "In a proper fraction, numerator is less than denominator."),
                    ("Which is an improper fraction?", ["2/5", "3/7", "9/4", "1/8"], "9/4", "The numerator is greater than the denominator."),
                    ("2 1/3 is a", ["proper fraction", "mixed fraction", "decimal only", "integer"], "mixed fraction", "It has a whole number and a fraction."),
                    ("Fractions on a number line are placed between", ["only negative numbers", "whole numbers", "letters only", "angles"], "whole numbers", "Fractions divide intervals into equal parts."),
                ]),
            make_module(2, "Equivalent, Simplest, Like and Unlike Fractions",
                "Equivalent fractions name the same value, like 1/2 and 2/4. A fraction is in simplest form when numerator and denominator have no common factor except 1. Like fractions have the same denominator, so they are easy to compare, add and subtract. Unlike fractions first need common denominators.",
                "Hard", 10, [
                    ("Which fraction is equivalent to 1/2?", ["2/4", "1/3", "3/5", "4/5"], "2/4", "Multiplying numerator and denominator by 2 gives 2/4."),
                    ("The simplest form of 4/8 is", ["1/2", "2/4", "4/4", "8/4"], "1/2", "Divide numerator and denominator by 4."),
                    ("Like fractions have the same", ["numerator", "denominator", "value always", "mixed number"], "denominator", "Like fractions share a denominator."),
                    ("Which is greater: 3/7 or 5/7?", ["3/7", "5/7", "Both equal", "Cannot compare"], "5/7", "For like fractions, greater numerator means greater fraction."),
                    ("What is 2/9 + 4/9?", ["6/9", "6/18", "8/9", "2/4"], "6/9", "Add numerators when denominators are the same."),
                ]),
        ],
    },
    {
        "chapter_name": "Decimals",
        "modules": [
            make_module(1, "Tenths, Hundredths and Comparing Decimals",
                "Decimals are another way to write fractions with denominators 10, 100 and so on. One tenth is written as 0.1 and one hundredth as 0.01. Decimal place value helps us compare numbers carefully. Just like whole numbers, digits have value based on position, but here positions continue to the right of the decimal point.",
                "Medium", 8, [
                    ("One tenth is written as", ["0.1", "0.01", "1.0", "10.0"], "0.1", "One tenth means 1/10."),
                    ("One hundredth is written as", ["0.1", "0.01", "0.001", "1.00"], "0.01", "One hundredth means 1/100."),
                    ("Which is greater: 0.7 or 0.5?", ["0.7", "0.5", "Both equal", "Cannot compare"], "0.7", "Seven tenths is greater than five tenths."),
                    ("2.35 has 3 in the", ["ones place", "tenths place", "hundredths place", "thousands place"], "tenths place", "The first digit after the decimal point is tenths."),
                    ("0.09 means", ["nine tenths", "nine hundredths", "nine tens", "nine hundreds"], "nine hundredths", "The 9 is in the hundredths place."),
                ]),
            make_module(2, "Using, Adding and Subtracting Decimals",
                "Decimals appear in money, length and weight. Rupees and paise, metres and centimetres, and kilograms and grams can be written using decimals. To add or subtract decimals, line up the decimal points and then calculate as usual. This keeps tenths under tenths and hundredths under hundredths.",
                "Medium", 9, [
                    ("Rs 5 and 75 paise can be written as", ["Rs 5.75", "Rs 575", "Rs 0.575", "Rs 75.5"], "Rs 5.75", "75 paise is 0.75 rupee."),
                    ("What is 1.2 + 2.3?", ["3.5", "3.3", "2.5", "35"], "3.5", "Add tenths with tenths."),
                    ("What is 5.6 - 2.1?", ["3.5", "3.7", "7.7", "2.5"], "3.5", "Subtract after aligning decimal points."),
                    ("When adding decimals, we should align", ["last digits only", "decimal points", "largest digits only", "commas"], "decimal points", "Place values must match."),
                    ("3 kg 500 g is", ["3.5 kg", "35 kg", "0.35 kg", "3500 kg"], "3.5 kg", "500 g is half a kilogram."),
                ]),
        ],
    },
    {
        "chapter_name": "Data Handling",
        "modules": [
            make_module(1, "Recording, Organising and Interpreting Data",
                "Data is information collected from observations, surveys or counts. Raw data is easier to understand when it is organised in tables or tally marks. A pictograph uses pictures to represent data, and each picture may stand for more than one object. Interpreting data means reading it to answer questions.",
                "Easy", 7, [
                    ("Data means", ["collected information", "only shapes", "only angles", "a ruler"], "collected information", "Data is information gathered for a purpose."),
                    ("Tally marks help us", ["measure angles", "count repeated items", "draw circles", "find area"], "count repeated items", "Tallies organise counts quickly."),
                    ("A pictograph uses", ["pictures", "only decimals", "only variables", "only lines"], "pictures", "Pictures represent quantities."),
                    ("If one picture stands for 5 students, three pictures stand for", ["5", "10", "15", "20"], "15", "3 x 5 = 15."),
                    ("Organised data is easier to", ["hide", "read and compare", "erase", "make random"], "read and compare", "Organisation shows patterns clearly."),
                ]),
            make_module(2, "Bar Graphs",
                "A bar graph represents data with bars of equal width. The height or length of each bar shows the quantity. A scale tells what each step on the graph stands for. Bar graphs are useful when we want to compare categories such as favourite games, number of students or monthly rainfall.",
                "Medium", 8, [
                    ("A bar graph uses", ["bars", "only circles", "fractions only", "compass arcs"], "bars", "Bars show quantities."),
                    ("Bars in a bar graph should usually have equal", ["colour only", "width", "height always", "labels only"], "width", "Equal width keeps the graph clear."),
                    ("The scale of a graph tells", ["what each unit represents", "only the title", "only colour", "the smallest number only"], "what each unit represents", "Scale connects bar length to data value."),
                    ("A taller bar usually represents", ["smaller quantity", "larger quantity", "no quantity", "same quantity always"], "larger quantity", "Bar height or length shows value."),
                    ("Bar graphs help us", ["compare categories", "construct circles only", "find HCF only", "write Roman numerals"], "compare categories", "They make category comparison visual."),
                ]),
        ],
    },
    {
        "chapter_name": "Mensuration",
        "modules": [
            make_module(1, "Perimeter of Shapes",
                "Perimeter is the distance around a closed figure. Imagine walking along the boundary of a garden; the total distance walked is the perimeter. For a rectangle, perimeter is twice the sum of length and breadth. For a square, it is four times the side. Perimeter helps measure fencing, borders and paths.",
                "Medium", 8, [
                    ("Perimeter means", ["surface covered", "distance around a figure", "inside space", "angle measure"], "distance around a figure", "Perimeter is boundary length."),
                    ("Perimeter of a rectangle is", ["l x b", "2(l + b)", "4s", "l + b"], "2(l + b)", "Add all four sides of the rectangle."),
                    ("Perimeter of a square of side s is", ["s x s", "4s", "2s", "s + 4"], "4s", "A square has four equal sides."),
                    ("A regular shape has", ["all sides equal", "no sides", "only curves", "all angles zero"], "all sides equal", "Regular shapes have equal sides."),
                    ("Perimeter is measured in", ["square units", "linear units", "cubic units", "degrees"], "linear units", "It is a length."),
                ]),
            make_module(2, "Area of Rectangle and Square",
                "Area is the amount of surface covered by a figure. We measure area in square units because we count how many unit squares fit inside. The area of a rectangle is length times breadth. The area of a square is side times side. Area helps measure floors, walls, fields and notebook covers.",
                "Medium", 8, [
                    ("Area means", ["distance around", "surface covered", "angle size", "number name"], "surface covered", "Area measures the region inside a shape."),
                    ("Area is measured in", ["square units", "degrees", "litres", "rupees"], "square units", "Area counts unit squares."),
                    ("Area of a rectangle is", ["l + b", "2(l + b)", "l x b", "4l"], "l x b", "Rectangle area is length times breadth."),
                    ("Area of a square of side s is", ["4s", "s x s", "2s", "s + s"], "s x s", "Area of a square is side multiplied by side."),
                    ("A rectangle of length 5 cm and breadth 3 cm has area", ["8 sq cm", "15 sq cm", "16 sq cm", "30 sq cm"], "15 sq cm", "5 x 3 = 15 square centimetres."),
                ]),
        ],
    },
    {
        "chapter_name": "Algebra",
        "modules": [
            make_module(1, "Patterns, Variables and Expressions",
                "Algebra uses letters to stand for numbers. A variable can take different values, just like a box waiting to be filled. Matchstick patterns show how a rule can describe many cases at once. Expressions such as x + 3 or 2n help us write mathematical rules in a short and powerful way.",
                "Medium", 8, [
                    ("A variable is usually represented by", ["a letter", "only a ruler", "a fixed picture", "a comma"], "a letter", "Letters such as x or n can represent numbers."),
                    ("In x + 5, x is a", ["constant", "variable", "unit", "bar"], "variable", "x can take different values."),
                    ("An expression has", ["only an equal sign", "numbers, variables and operations", "only pictures", "only angles"], "numbers, variables and operations", "Expressions combine quantities without necessarily being equations."),
                    ("If n = 4, then n + 3 equals", ["3", "4", "7", "12"], "7", "Substitute 4 for n."),
                    ("2n means", ["2 + n", "2 x n", "n - 2", "2 divided by n"], "2 x n", "A number next to a variable means multiplication."),
                ]),
            make_module(2, "Equations and Solutions",
                "An equation is a mathematical sentence with an equal sign. It says both sides have the same value. A solution is the value of the variable that makes the equation true. We can find solutions by thinking, checking or using inverse operations. Equations turn number puzzles into clear steps.",
                "Medium", 9, [
                    ("Which is an equation?", ["x + 2", "x + 2 = 7", "7, 8, 9", "x only"], "x + 2 = 7", "An equation has an equal sign."),
                    ("A solution of an equation makes it", ["long", "true", "curved", "negative"], "true", "The value must satisfy the equation."),
                    ("Solve x + 3 = 8.", ["3", "5", "8", "11"], "5", "5 + 3 = 8."),
                    ("Solve y - 4 = 6.", ["2", "4", "6", "10"], "10", "10 - 4 = 6."),
                    ("In 2n = 12, n equals", ["2", "6", "10", "12"], "6", "2 x 6 = 12."),
                ]),
        ],
    },
    {
        "chapter_name": "Ratio and Proportion",
        "modules": [
            make_module(1, "Ratio",
                "A ratio compares two quantities of the same kind. If there are 2 red balls and 3 blue balls, the ratio of red to blue is 2:3. Ratios help us compare parts, not just count them. Before writing a ratio, quantities should be in the same units, such as centimetres with centimetres.",
                "Medium", 8, [
                    ("A ratio compares", ["two quantities", "only one number", "only angles", "only letters"], "two quantities", "Ratio shows how two quantities relate."),
                    ("The ratio of 2 red balls to 3 blue balls is", ["3:2", "2:3", "5:2", "2:5"], "2:3", "Write red first, then blue."),
                    ("Before comparing 1 m and 50 cm, first", ["ignore units", "make units same", "add both", "draw a circle"], "make units same", "Ratios need same units."),
                    ("1 m equals", ["10 cm", "100 cm", "1000 cm", "1 cm"], "100 cm", "A metre has 100 centimetres."),
                    ("The ratio 4:8 in simplest form is", ["1:2", "2:1", "4:4", "8:4"], "1:2", "Divide both terms by 4."),
                ]),
            make_module(2, "Proportion and Unitary Method",
                "Proportion means two ratios are equal. For example, 2:4 and 1:2 are in proportion because they express the same comparison. The unitary method first finds the value of one unit, then uses it to find the value of many units. It is useful for price, distance, work and sharing problems.",
                "Hard", 10, [
                    ("Two equal ratios are said to be in", ["area", "proportion", "symmetry", "perimeter"], "proportion", "Proportion means equality of ratios."),
                    ("Are 2:4 and 1:2 in proportion?", ["Yes", "No", "Only sometimes", "Cannot say"], "Yes", "2:4 simplifies to 1:2."),
                    ("If 3 pens cost Rs 30, one pen costs", ["Rs 3", "Rs 10", "Rs 30", "Rs 90"], "Rs 10", "Divide total cost by 3."),
                    ("If one notebook costs Rs 12, five notebooks cost", ["Rs 17", "Rs 24", "Rs 60", "Rs 120"], "Rs 60", "5 x 12 = 60."),
                    ("Unitary method first finds the value of", ["zero units", "one unit", "all units directly", "two ratios only"], "one unit", "Then we multiply for the required number of units."),
                ]),
        ],
    },
    {
        "chapter_name": "Symmetry",
        "modules": [
            make_module(1, "Line Symmetry and Reflection",
                "A figure has line symmetry if one line divides it into two matching halves. If folded along that line, both halves cover each other exactly. Reflection is like seeing a mirror image. Symmetry appears in letters, leaves, rangoli designs and many everyday objects. It helps us notice balance and beauty in shapes.",
                "Easy", 7, [
                    ("A line of symmetry divides a figure into", ["two matching halves", "three unequal parts", "only curves", "no parts"], "two matching halves", "The halves overlap exactly."),
                    ("A mirror image is related to", ["reflection", "ratio", "perimeter", "HCF"], "reflection", "Reflection produces a mirror image."),
                    ("A rectangle has how many lines of symmetry?", ["0", "1", "2", "4"], "2", "A non-square rectangle has two symmetry lines."),
                    ("A square has how many lines of symmetry?", ["1", "2", "4", "6"], "4", "It has two diagonals and two midlines."),
                    ("If a figure has no matching fold line, it has", ["no line symmetry", "four lines of symmetry", "only ratio", "only area"], "no line symmetry", "Line symmetry requires matching halves."),
                ]),
            make_module(2, "Figures With Multiple Lines of Symmetry",
                "Some figures have more than one line of symmetry. A square has four, an equilateral triangle has three, and a circle has many. More symmetry usually means the figure is very balanced. By drawing possible fold lines, students can test whether both sides match exactly.",
                "Medium", 8, [
                    ("An equilateral triangle has", ["1 line of symmetry", "2 lines of symmetry", "3 lines of symmetry", "0 lines of symmetry"], "3 lines of symmetry", "Each vertex-to-midpoint line is a symmetry line."),
                    ("A circle has", ["no line of symmetry", "only one", "only two", "many lines of symmetry"], "many lines of symmetry", "Every diameter is a line of symmetry."),
                    ("A figure has line symmetry if its halves", ["overlap exactly", "are different", "have different sizes", "are open"], "overlap exactly", "Matching halves show symmetry."),
                    ("Which shape has four lines of symmetry?", ["Square", "Scalene triangle", "Rectangle only", "Parallelogram always"], "Square", "A square has four symmetry lines."),
                    ("Symmetry is checked by imagining a", ["fold", "decimal point", "bar graph", "factor tree"], "fold", "Folding helps test matching halves."),
                ]),
        ],
    },
    {
        "chapter_name": "Practical Geometry",
        "modules": [
            make_module(1, "Constructing Circles and Line Segments",
                "Practical geometry teaches accurate drawing with tools. A compass draws circles when the radius is known. A ruler helps draw and measure line segments. We can also copy a given line segment using ruler and compass. These constructions train the hand and eye to create exact mathematical figures.",
                "Medium", 8, [
                    ("A compass is used to draw", ["circles", "bar graphs only", "ratios", "tally marks"], "circles", "A compass draws circles and arcs."),
                    ("To construct a circle, we need its", ["radius", "ratio", "HCF", "mode"], "radius", "The compass opening is set to the radius."),
                    ("A line segment has", ["two endpoints", "no endpoints", "one endpoint", "only curves"], "two endpoints", "A segment is bounded at both ends."),
                    ("A ruler is used to draw", ["straight line segments", "only circles", "only angles", "only pictures"], "straight line segments", "Rulers help draw straight lengths."),
                    ("Copying a line segment means making another segment of", ["different length", "same length", "zero length", "curved shape"], "same length", "The copy must match the original length."),
                ]),
            make_module(2, "Constructing Perpendiculars, Bisectors and Angles",
                "A perpendicular makes a right angle with a line. Practical geometry shows how to draw perpendiculars through points on or away from a line. A perpendicular bisector cuts a segment into two equal parts at right angles. We can also construct angles, copy angles and bisect angles using ruler and compass.",
                "Hard", 10, [
                    ("Perpendicular lines meet at", ["45 degrees", "60 degrees", "90 degrees", "180 degrees"], "90 degrees", "Perpendicular lines form right angles."),
                    ("A perpendicular bisector divides a line segment into", ["two equal parts", "three parts", "unequal parts", "curves"], "two equal parts", "A bisector cuts into two equal halves."),
                    ("An angle bisector divides an angle into", ["two equal angles", "two unequal angles", "a circle", "a line segment only"], "two equal angles", "Bisect means divide into two equal parts."),
                    ("A protractor is used to construct an angle of given", ["measure", "area", "weight", "ratio"], "measure", "Angles are measured in degrees."),
                    ("A right angle can be constructed using", ["ruler and compass", "tally marks", "bar graph", "decimal table"], "ruler and compass", "Practical geometry uses these tools for constructions."),
                ]),
        ],
    },
]


curriculum = {
    "class": "6",
    "board": "CBSE",
    "subject": "Mathematics",
    "source_pdf": "NCERT 6th maths book.pdf",
    "chapters": chapters,
}


OUT.write_text(json.dumps(curriculum, indent=2), encoding="utf-8")
print(OUT)
print(f"chapters={len(chapters)}")
print(f"modules={sum(len(chapter['modules']) for chapter in chapters)}")
print(f"questions={sum(len(module['questions']) for chapter in chapters for module in chapter['modules'])}")
