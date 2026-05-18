import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "src" / "data"
OUTPUT_JSON = DATA_DIR / "cbse_class7_mathematics_learning_journey.json"
OUTPUT_MANIFEST = DATA_DIR / "cbse_class7_mathematics_validation_manifest.json"

PDF_SOURCE = (
    "C:/Users/thira/OneDrive - Rathinam Group Of Institutions/Desktop/My carrier/"
    "projects/Learning edu/7 to 12/ncert-books-for-class-7-maths.pdf"
)

TIMERS = {"Easy": 30, "Medium": 45, "Hard": 60}
TOTAL_TIMERS = {"Easy": 4, "Medium": 5, "Hard": 6}


def choices(correct, wrongs):
    values = [correct]
    for wrong in wrongs:
        if wrong != correct and wrong not in values:
            values.append(wrong)
        if len(values) == 4:
            break
    fallback = ["Cannot be decided", "All of these", "None of these"]
    while len(values) < 4:
        values.append(fallback[len(values) - 1])
    return [values[1], values[3], values[0], values[2]]


def make_question(question_id, prompt, correct, wrongs, rationale, timer):
    return {
        "question_id": question_id,
        "question_text": prompt,
        "options": choices(correct, wrongs),
        "correct_answer": correct,
        "rationale": rationale,
        "timer_per_question_seconds": timer,
    }


def slug(value):
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def fact(prompt, correct, wrongs, rationale):
    return {
        "prompt": prompt,
        "correct": correct,
        "wrongs": wrongs,
        "rationale": rationale,
    }


CHAPTERS = [
    {
        "name": "Integers",
        "source_chapter": "Chapter 1: Integers",
        "modules": [
            {
                "topic": "Integer Recall and Number Line",
                "difficulty": "Easy",
                "explanation": "Integers are whole numbers with direction: positive, zero, and negative. A number line is like a road with zero as the starting point. Moving right means positive movement, and moving left means negative movement. This chapter uses temperature, quiz scores, and money changes to show how integers help us describe real-life ups and downs.",
                "facts": [
                    fact("Which number is neither positive nor negative?", "0", ["1", "-1", "10"], "Zero is the middle point on the integer number line."),
                    fact("When we add a positive integer on a number line, we move to the ____.", "Right", ["Left", "Same place", "Down"], "NCERT explains addition of a positive integer as movement to the right."),
                    fact("When we add a negative integer on a number line, we move to the ____.", "Left", ["Right", "Same place", "Up"], "Adding a negative integer is shown by moving left."),
                    fact("The additive inverse of 8 is ____.", "-8", ["8", "0", "16"], "A number and its additive inverse add to zero."),
                    fact("Which integer is greater: -3 or -8?", "-3", ["-8", "Both are equal", "Cannot be compared"], "-3 lies to the right of -8 on the number line."),
                ],
            },
            {
                "topic": "Addition and Subtraction of Integers",
                "difficulty": "Medium",
                "explanation": "Adding and subtracting integers is like combining gains and losses. Two gains make a bigger gain, two losses make a bigger loss, and a gain with a loss is decided by the larger size. Subtraction can be changed into adding the opposite number, which makes difficult-looking sums much easier.",
                "facts": [
                    fact("-6 + -7 = ____.", "-13", ["13", "1", "-1"], "Adding two negative integers gives a negative integer."),
                    fact("56 - 73 = ____.", "-17", ["17", "129", "-129"], "NCERT writes 56 - 73 as 56 + (-73), which is -17."),
                    fact("10 + (-4) = ____.", "6", ["14", "-6", "-14"], "Adding a negative integer is the same as subtracting its positive value."),
                    fact("Subtracting -5 from 2 gives ____.", "7", ["-3", "3", "-7"], "2 - (-5) = 2 + 5 = 7."),
                    fact("Which property says a + b = b + a for integers?", "Commutative property of addition", ["Closure of division", "Associative property of multiplication", "Distributive property"], "The order of addends can be changed in integer addition."),
                ],
            },
            {
                "topic": "Multiplication and Division of Integers",
                "difficulty": "Medium",
                "explanation": "Integer multiplication and division follow simple sign rules. Same signs give a positive answer, and different signs give a negative answer. Think of the sign as the direction of the final result, while the numbers tell the size. These rules help with quick calculations in later algebra.",
                "facts": [
                    fact("(-4) x 6 = ____.", "-24", ["24", "-10", "10"], "A negative integer multiplied by a positive integer gives a negative product."),
                    fact("(-5) x (-3) = ____.", "15", ["-15", "8", "-8"], "The product of two negative integers is positive."),
                    fact("36 divided by (-6) = ____.", "-6", ["6", "-30", "30"], "Different signs in division give a negative quotient."),
                    fact("(-42) divided by (-7) = ____.", "6", ["-6", "49", "-49"], "Same signs in division give a positive quotient."),
                    fact("Which operation on integers is not always commutative?", "Division", ["Addition", "Multiplication", "Adding zero"], "Changing the order in division can change the result."),
                ],
            },
        ],
    },
    {
        "name": "Fractions and Decimals",
        "source_chapter": "Chapter 2: Fractions and Decimals",
        "modules": [
            {
                "topic": "Multiplication of Fractions",
                "difficulty": "Medium",
                "explanation": "Multiplying fractions means taking a part of a part. If half a chocolate is shared again into two equal parts, each piece is one-fourth of the whole. In multiplication, we multiply numerators together and denominators together, then simplify if possible.",
                "facts": [
                    fact("1/2 x 1/3 = ____.", "1/6", ["2/5", "1/5", "2/6"], "Multiply numerators and denominators: 1 x 1 over 2 x 3."),
                    fact("2/5 x 3 = ____.", "6/5", ["5/8", "2/15", "3/10"], "Write 3 as 3/1 and multiply."),
                    fact("In fraction multiplication, numerators are ____.", "Multiplied", ["Added", "Subtracted", "Divided by zero"], "The rule multiplies numerator with numerator."),
                    fact("3/4 of 20 is ____.", "15", ["12", "20", "80"], "3/4 x 20 = 60/4 = 15."),
                    fact("A proper fraction multiplied by a whole number can become ____.", "Greater than 1", ["Always zero", "Always negative", "Always unchanged"], "For example, 3/4 x 20 = 15."),
                ],
            },
            {
                "topic": "Division of Fractions",
                "difficulty": "Medium",
                "explanation": "Dividing by a fraction asks how many such parts fit into a number. NCERT teaches us to multiply by the reciprocal of the divisor. The reciprocal flips numerator and denominator, turning division into a familiar multiplication step.",
                "facts": [
                    fact("The reciprocal of 2/3 is ____.", "3/2", ["2/3", "1/3", "3"], "A reciprocal interchanges numerator and denominator."),
                    fact("1/2 divided by 1/4 = ____.", "2", ["1/8", "1/2", "4"], "1/2 x 4/1 = 2."),
                    fact("To divide by a fraction, multiply by its ____.", "Reciprocal", ["Numerator only", "Denominator only", "Square"], "NCERT uses reciprocal to divide fractions."),
                    fact("3 divided by 1/2 = ____.", "6", ["3/2", "1/6", "2/3"], "3 x 2 = 6."),
                    fact("The reciprocal of 5 is ____.", "1/5", ["5/1", "0", "-5"], "A whole number 5 is 5/1, so its reciprocal is 1/5."),
                ],
            },
            {
                "topic": "Decimal Multiplication and Division",
                "difficulty": "Medium",
                "explanation": "Decimals are fractions written with place value. Multiplying by 10, 100, or 1000 shifts the decimal point right; dividing shifts it left. For other decimal operations, first calculate like whole numbers, then place the decimal carefully using the number of decimal places.",
                "facts": [
                    fact("0.2 x 10 = ____.", "2", ["0.02", "20", "0.12"], "Multiplying by 10 shifts the decimal one place right."),
                    fact("2.5 x 4 = ____.", "10", ["1.0", "6.5", "100"], "25 x 4 = 100, and one decimal place gives 10.0."),
                    fact("12.5 divided by 10 = ____.", "1.25", ["125", "0.125", "12.50"], "Dividing by 10 shifts the decimal one place left."),
                    fact("0.6 x 0.7 = ____.", "0.42", ["4.2", "0.13", "42"], "6 x 7 = 42 with two decimal places."),
                    fact("When dividing a decimal by 100, the decimal point moves ____ places left.", "2", ["1", "3", "100"], "Dividing by 100 moves the decimal two places left."),
                ],
            },
        ],
    },
    {
        "name": "Data Handling",
        "source_chapter": "Chapter 3: Data Handling",
        "modules": [
            {
                "topic": "Collecting and Organising Data",
                "difficulty": "Easy",
                "explanation": "Data is information collected to answer a question. A raw list can feel messy, so we organise it in tables, tally marks, and groups. Once arranged neatly, data tells a story: which value occurs often, which is largest, and what pattern we can notice.",
                "facts": [
                    fact("Information collected for study is called ____.", "Data", ["Equation", "Triangle", "Exponent"], "NCERT begins data handling by collecting data."),
                    fact("Tally marks help us count data by making ____.", "Groups", ["Angles", "Fractions only", "Solids"], "Tally marks organise repeated counts."),
                    fact("The difference between the highest and lowest observations is the ____.", "Range", ["Mean", "Mode", "Median"], "Range measures spread in a simple data set."),
                    fact("Raw data should be organised to make it easier to ____.", "Interpret", ["Hide", "Erase", "Rotate"], "Organised data is easier to read and understand."),
                    fact("A table is useful because it presents data ____.", "Neatly", ["Randomly", "Without values", "As only pictures"], "Tables arrange data in rows and columns."),
                ],
            },
            {
                "topic": "Mean, Mode and Median",
                "difficulty": "Medium",
                "explanation": "Representative values describe a data set with one useful number. Mean is the fair-share average, mode is the most common value, and median is the middle value after arranging data. Each one helps answer a different question about the same information.",
                "facts": [
                    fact("The average is also called the ____.", "Mean", ["Range", "Chance", "Bar"], "NCERT introduces average as mean."),
                    fact("Mean of 2, 4 and 6 is ____.", "4", ["3", "6", "12"], "The sum is 12, and 12 divided by 3 is 4."),
                    fact("The value that occurs most often is the ____.", "Mode", ["Median", "Mean", "Range"], "Mode is the most frequent observation."),
                    fact("The middle observation after arranging data is the ____.", "Median", ["Mode", "Range", "Tally"], "Median is found from ordered data."),
                    fact("For 3, 5, 5, 8, the mode is ____.", "5", ["3", "8", "21"], "5 appears more often than the other values."),
                ],
            },
            {
                "topic": "Bar Graphs and Probability",
                "difficulty": "Medium",
                "explanation": "Bar graphs show data with bars of different heights or lengths. They make comparisons quick, like seeing which class has more students. Probability describes chance, from impossible to certain. Together, graphs and probability help us read data and make simple predictions.",
                "facts": [
                    fact("A bar graph represents data using ____.", "Bars", ["Circles only", "Equations only", "Nets"], "Bar graphs use rectangular bars."),
                    fact("Probability describes the ____ of an event.", "Chance", ["Area", "Perimeter", "Median only"], "NCERT connects probability with chance."),
                    fact("A sure event has probability ____.", "1", ["0", "2", "-1"], "A certain event has probability 1."),
                    fact("An impossible event has probability ____.", "0", ["1", "10", "-1"], "An impossible event cannot happen."),
                    fact("Bar graphs are useful for ____ data.", "Comparing", ["Dividing fractions", "Constructing triangles only", "Solving x only"], "Bar lengths make comparison easy."),
                ],
            },
        ],
    },
    {
        "name": "Simple Equations",
        "source_chapter": "Chapter 4: Simple Equations",
        "modules": [
            {
                "topic": "Setting Up Equations",
                "difficulty": "Easy",
                "explanation": "An equation is a mathematical sentence with an equal sign. It often uses a letter, such as x, to stand for an unknown number. Setting up an equation is like translating a word sentence into maths, keeping both sides balanced.",
                "facts": [
                    fact("An equation must contain an ____ sign.", "Equal", ["Greater than", "Less than", "Approximately"], "Equations state that two expressions are equal."),
                    fact("In x + 5 = 12, the unknown is ____.", "x", ["5", "12", "+"], "The letter x stands for the unknown value."),
                    fact("'A number plus 3 is 10' can be written as ____.", "x + 3 = 10", ["x - 3 = 10", "3x = 10", "x/3 = 10"], "The words 'plus 3 is 10' translate to x + 3 = 10."),
                    fact("A letter used for an unknown number is called a ____.", "Variable", ["Median", "Triangle", "Bar"], "Variables represent unknown or changing values."),
                    fact("Both sides of an equation are separated by the ____.", "Equal sign", ["Decimal point", "Comma", "Bracket only"], "The equal sign shows balance."),
                ],
            },
            {
                "topic": "Solving Simple Equations",
                "difficulty": "Medium",
                "explanation": "Solving means finding the value that makes an equation true. We keep the equation balanced by doing the same operation on both sides. If something was added, subtract it; if something was multiplied, divide by it.",
                "facts": [
                    fact("x + 5 = 12 gives x = ____.", "7", ["17", "5", "12"], "Subtract 5 from both sides."),
                    fact("2x = 18 gives x = ____.", "9", ["16", "20", "36"], "Divide both sides by 2."),
                    fact("x - 4 = 11 gives x = ____.", "15", ["7", "-15", "44"], "Add 4 to both sides."),
                    fact("x/3 = 5 gives x = ____.", "15", ["8", "2", "5/3"], "Multiply both sides by 3."),
                    fact("The value that satisfies an equation is its ____.", "Solution", ["Perimeter", "Numerator", "Graph"], "A solution makes the equation true."),
                ],
            },
            {
                "topic": "Applications of Simple Equations",
                "difficulty": "Medium",
                "explanation": "Simple equations help solve story problems. We choose a variable for the unknown, write the relationship as an equation, solve it, and check the answer in the story. This turns everyday puzzles into clear, step-by-step maths.",
                "facts": [
                    fact("If a number increased by 8 is 20, the number is ____.", "12", ["28", "8", "160"], "Let x + 8 = 20, so x = 12."),
                    fact("If twice a number is 30, the number is ____.", "15", ["60", "28", "32"], "Let 2x = 30, so x = 15."),
                    fact("If x - 7 = 9, then x represents ____.", "16", ["2", "-16", "63"], "Adding 7 to both sides gives 16."),
                    fact("To check a solution, substitute it back into the ____.", "Equation", ["Title", "Bar graph", "Compass"], "Substitution confirms whether both sides match."),
                    fact("The first step in a word problem is to choose a ____ for the unknown.", "Variable", ["Colour", "Shape", "Unit square only"], "A variable lets us write the unknown quantity."),
                ],
            },
        ],
    },
    {
        "name": "Lines and Angles",
        "source_chapter": "Chapter 5: Lines and Angles",
        "modules": [
            {
                "topic": "Related Angles",
                "difficulty": "Medium",
                "explanation": "Angles can be related by their sums or positions. Complementary angles make 90 degrees, supplementary angles make 180 degrees, and a linear pair also forms a straight angle. Vertically opposite angles are equal when two lines intersect.",
                "facts": [
                    fact("Two angles whose sum is 90 degrees are ____ angles.", "Complementary", ["Supplementary", "Vertically opposite", "Linear pair"], "Complementary angles add to 90 degrees."),
                    fact("Two angles whose sum is 180 degrees are ____ angles.", "Supplementary", ["Complementary", "Acute", "Right"], "Supplementary angles add to 180 degrees."),
                    fact("Angles in a linear pair add to ____.", "180 degrees", ["90 degrees", "360 degrees", "45 degrees"], "A linear pair forms a straight angle."),
                    fact("Vertically opposite angles are ____.", "Equal", ["Always unequal", "Always 90 degrees", "Always 180 degrees"], "Intersecting lines form equal vertically opposite angles."),
                    fact("If one angle in a linear pair is 70 degrees, the other is ____.", "110 degrees", ["70 degrees", "20 degrees", "290 degrees"], "180 - 70 = 110 degrees."),
                ],
            },
            {
                "topic": "Intersecting Lines and Transversals",
                "difficulty": "Medium",
                "explanation": "When two lines cross, they form angle pairs. A transversal is a line that cuts two or more lines. It creates corresponding, alternate interior, and interior angle pairs, which become especially useful when the two lines are parallel.",
                "facts": [
                    fact("A line that intersects two or more lines is called a ____.", "Transversal", ["Median", "Altitude", "Hypotenuse"], "NCERT defines such a line as a transversal."),
                    fact("Two lines crossing at one point are ____ lines.", "Intersecting", ["Parallel", "Skew only", "Coincident only"], "Intersecting lines meet at a point."),
                    fact("Corresponding angles are formed when a transversal cuts ____ lines.", "Two", ["No", "Only curved", "Only one"], "The chapter discusses pairs from two lines and a transversal."),
                    fact("Alternate interior angles lie on ____ sides of the transversal.", "Opposite", ["Same", "Outside only", "No"], "Alternate interior angles are inside the two lines on opposite sides."),
                    fact("Interior angles on the same side of a transversal are called ____ angles.", "Co-interior", ["Complementary always", "Median", "RHS"], "These are the interior angle pair on one side of a transversal."),
                ],
            },
            {
                "topic": "Checking Parallel Lines",
                "difficulty": "Hard",
                "explanation": "Parallel lines never meet, and their angle patterns reveal this. If corresponding angles are equal, or alternate interior angles are equal, lines are parallel. If co-interior angles add to 180 degrees, that also confirms parallel lines.",
                "facts": [
                    fact("If corresponding angles are equal, the two lines are ____.", "Parallel", ["Perpendicular", "Curved", "Always equal length"], "This is one test for parallel lines."),
                    fact("If alternate interior angles are equal, the lines are ____.", "Parallel", ["Intersecting at 90 degrees", "Not comparable", "Always vertical"], "Equal alternate interior angles show parallel lines."),
                    fact("Co-interior angles on parallel lines add to ____.", "180 degrees", ["90 degrees", "360 degrees", "0 degrees"], "Interior angles on the same side of a transversal are supplementary."),
                    fact("Parallel lines are lines in a plane that ____ meet.", "Never", ["Always", "Sometimes", "Must"], "Parallel lines do not meet."),
                    fact("If one corresponding angle is 65 degrees, its matching corresponding angle on parallel lines is ____.", "65 degrees", ["115 degrees", "25 degrees", "180 degrees"], "Corresponding angles are equal for parallel lines."),
                ],
            },
        ],
    },
    {
        "name": "The Triangle and its Properties",
        "source_chapter": "Chapter 6: The Triangle and its Properties",
        "modules": [
            {
                "topic": "Medians and Altitudes",
                "difficulty": "Medium",
                "explanation": "A triangle has special line segments. A median joins a vertex to the midpoint of the opposite side, so it splits that side equally. An altitude is drawn from a vertex perpendicular to the opposite side. These lines help us study a triangle more carefully.",
                "facts": [
                    fact("A median joins a vertex to the midpoint of the ____ side.", "Opposite", ["Same", "Parallel", "Exterior"], "A median connects a vertex to the midpoint of the opposite side."),
                    fact("An altitude is ____ to the opposite side.", "Perpendicular", ["Parallel", "Equal always", "Curved"], "An altitude makes a right angle with the opposite side."),
                    fact("A triangle has ____ medians.", "3", ["1", "2", "4"], "Each vertex can have one median."),
                    fact("A triangle has ____ altitudes.", "3", ["1", "2", "6"], "Each vertex can have one altitude."),
                    fact("The midpoint divides a side into ____ equal parts.", "2", ["3", "4", "0"], "A midpoint is exactly halfway along a segment."),
                ],
            },
            {
                "topic": "Exterior Angle and Angle Sum",
                "difficulty": "Hard",
                "explanation": "Triangle angles follow two powerful rules. The three interior angles add to 180 degrees. An exterior angle equals the sum of the two opposite interior angles. These properties let us find missing angles without measuring every angle.",
                "facts": [
                    fact("The sum of the angles of a triangle is ____.", "180 degrees", ["90 degrees", "270 degrees", "360 degrees"], "NCERT states the angle sum property."),
                    fact("An exterior angle of a triangle equals the sum of two ____ interior angles.", "Opposite", ["Adjacent", "Right", "Equal only"], "The exterior angle property uses the two interior opposite angles."),
                    fact("If two angles of a triangle are 50 degrees and 60 degrees, the third is ____.", "70 degrees", ["110 degrees", "10 degrees", "170 degrees"], "180 - 50 - 60 = 70 degrees."),
                    fact("If opposite interior angles are 40 degrees and 75 degrees, the exterior angle is ____.", "115 degrees", ["35 degrees", "105 degrees", "180 degrees"], "40 + 75 = 115 degrees."),
                    fact("The exterior angle is formed by extending a ____ of the triangle.", "Side", ["Median only", "Vertex only", "Circle"], "Extending a side forms an exterior angle."),
                ],
            },
            {
                "topic": "Special Triangles and Pythagoras Property",
                "difficulty": "Hard",
                "explanation": "Some triangles have special names. An equilateral triangle has three equal sides, and an isosceles triangle has two equal sides. A right triangle has one 90-degree angle. In a right triangle, the Pythagoras property connects the squares of the two legs and the hypotenuse.",
                "facts": [
                    fact("An equilateral triangle has ____ equal sides.", "3", ["1", "2", "0"], "Equilateral means all three sides are equal."),
                    fact("An isosceles triangle has at least ____ equal sides.", "2", ["0", "1", "4"], "Isosceles triangles have two equal sides."),
                    fact("In a right triangle, the side opposite the right angle is the ____.", "Hypotenuse", ["Median", "Base always", "Altitude"], "The hypotenuse is opposite the 90-degree angle."),
                    fact("Pythagoras property applies to a ____ triangle.", "Right-angled", ["Scalene only", "Obtuse only", "Any quadrilateral"], "NCERT gives the property for right-angled triangles."),
                    fact("The sum of lengths of any two sides of a triangle is ____ the third side.", "Greater than", ["Less than", "Equal to always", "Unrelated to"], "This is the triangle inequality property."),
                ],
            },
        ],
    },
    {
        "name": "Congruence of Triangles",
        "source_chapter": "Chapter 7: Congruence of Triangles",
        "modules": [
            {
                "topic": "Meaning of Congruence",
                "difficulty": "Easy",
                "explanation": "Congruent figures are exact copies. They may be moved, turned, or flipped, but their shape and size stay the same. The chapter first builds this idea with plane figures, line segments, and angles before applying it to triangles.",
                "facts": [
                    fact("Congruent figures have the same shape and ____.", "Size", ["Colour", "Position only", "Name"], "Congruence means same shape and same size."),
                    fact("Two congruent line segments have equal ____.", "Lengths", ["Colours", "Labels only", "Areas"], "Line segment congruence compares length."),
                    fact("Two congruent angles have equal ____.", "Measures", ["Side lengths", "Names only", "Areas"], "Angle congruence compares angle measure."),
                    fact("A figure can remain congruent after a ____.", "Turn", ["Change in size", "Stretch", "Shrink"], "Turning does not change shape or size."),
                    fact("Congruence is stronger than just looking ____.", "Similar", ["Different", "Named", "Coloured"], "Congruent figures must match in size too."),
                ],
            },
            {
                "topic": "Triangle Congruence Criteria",
                "difficulty": "Hard",
                "explanation": "We do not need to check every side and angle to prove triangles congruent. NCERT gives useful criteria: SSS, SAS, ASA, and RHS. These rules tell us which matching parts are enough to guarantee two triangles are exact copies.",
                "facts": [
                    fact("SSS congruence means three corresponding ____ are equal.", "Sides", ["Angles", "Areas", "Medians"], "SSS stands for Side-Side-Side."),
                    fact("SAS congruence uses two sides and the included ____.", "Angle", ["Median", "Area", "Perimeter"], "SAS stands for Side-Angle-Side."),
                    fact("ASA congruence uses two angles and the included ____.", "Side", ["Area", "Median", "Hypotenuse only"], "ASA stands for Angle-Side-Angle."),
                    fact("The angle in SAS must be the ____ angle between the two sides.", "Included", ["Exterior", "Random", "Right always"], "SAS requires the angle contained between the two sides."),
                    fact("In congruent triangles, corresponding parts are ____.", "Equal", ["Always different", "Ignored", "Negative"], "Corresponding sides and angles match exactly."),
                ],
            },
            {
                "topic": "RHS Congruence",
                "difficulty": "Hard",
                "explanation": "RHS is a special congruence rule for right-angled triangles. If two right triangles have equal hypotenuse and one equal side, the triangles are congruent. It saves time because the right angle is already known in both triangles.",
                "facts": [
                    fact("RHS congruence applies to ____ triangles.", "Right-angled", ["Equilateral only", "Any triangle", "No triangle"], "RHS is for right-angled triangles."),
                    fact("In RHS, H stands for ____.", "Hypotenuse", ["Height", "Half", "Horizontal"], "RHS means Right angle-Hypotenuse-Side."),
                    fact("In RHS, S stands for ____.", "Side", ["Sum", "Scale", "Square"], "RHS uses one corresponding side."),
                    fact("The hypotenuse is opposite the ____ angle.", "Right", ["Smallest", "Exterior", "Obtuse always"], "The hypotenuse lies opposite the right angle."),
                    fact("RHS needs one right angle, equal hypotenuse, and one equal ____.", "Side", ["Mode", "Bar", "Expression"], "Those are the matching parts for RHS."),
                ],
            },
        ],
    },
    {
        "name": "Comparing Quantities",
        "source_chapter": "Chapter 8: Comparing Quantities",
        "modules": [
            {
                "topic": "Equivalent Ratios and Percentages",
                "difficulty": "Medium",
                "explanation": "Ratios compare two quantities, and equivalent ratios say the same comparison in different numbers. Percent means per hundred. It is like converting comparisons into a common language out of 100, which makes marks, discounts, and increases easy to compare.",
                "facts": [
                    fact("Percent means per ____.", "Hundred", ["Ten", "Thousand", "One"], "Percent literally means out of 100."),
                    fact("1/2 as a percentage is ____.", "50%", ["25%", "75%", "100%"], "1/2 equals 50 out of 100."),
                    fact("The ratio 2:3 is equivalent to ____.", "4:6", ["3:2", "2:6", "6:4"], "Multiplying both terms by 2 gives 4:6."),
                    fact("25% as a fraction is ____.", "1/4", ["1/2", "3/4", "1/25"], "25 out of 100 simplifies to 1/4."),
                    fact("To compare fractions as percentages, express them out of ____.", "100", ["10 only", "2", "0"], "Percentages use 100 as the base."),
                ],
            },
            {
                "topic": "Profit, Loss and Discount",
                "difficulty": "Hard",
                "explanation": "Buying and selling use comparison. Profit happens when selling price is greater than cost price; loss happens when selling price is smaller. Discount reduces the marked price. These ideas help us understand shop bills and sale offers.",
                "facts": [
                    fact("Profit = selling price - ____ price.", "Cost", ["Marked", "Discount", "Mean"], "Profit compares selling price with cost price."),
                    fact("Loss happens when selling price is ____ cost price.", "Less than", ["Greater than", "Equal to always", "Double"], "Selling for less than cost creates loss."),
                    fact("If cost price is Rs 80 and selling price is Rs 100, profit is ____.", "Rs 20", ["Rs 180", "Rs 80", "Rs 100"], "100 - 80 = 20."),
                    fact("Discount is reduction from the ____ price.", "Marked", ["Mean", "Median", "Hypotenuse"], "NCERT discusses discount on marked price."),
                    fact("Profit percentage is usually calculated on ____ price.", "Cost", ["Selling only", "Marked only", "Mode"], "Profit or loss percent is based on cost price."),
                ],
            },
            {
                "topic": "Simple Interest",
                "difficulty": "Hard",
                "explanation": "Simple interest is the extra money paid for borrowing or earned by lending. It depends on principal, rate, and time. The NCERT formula SI = P x R x T / 100 is a compact way to calculate this charge.",
                "facts": [
                    fact("In simple interest, P stands for ____.", "Principal", ["Percentage", "Perimeter", "Profit only"], "Principal is the original borrowed or invested amount."),
                    fact("Simple Interest = P x R x T / ____.", "100", ["10", "1000", "2"], "The textbook formula divides by 100."),
                    fact("Rate of interest is usually given as a ____.", "Percentage", ["Triangle", "Decimal point only", "Bar graph"], "Interest rate is expressed per hundred."),
                    fact("If P = 1000, R = 10%, T = 1 year, SI is ____.", "100", ["10", "1100", "10000"], "1000 x 10 x 1 / 100 = 100."),
                    fact("Amount = principal + ____.", "Interest", ["Loss only", "Median", "Altitude"], "The final amount includes the original principal and interest."),
                ],
            },
        ],
    },
    {
        "name": "Rational Numbers",
        "source_chapter": "Chapter 9: Rational Numbers",
        "modules": [
            {
                "topic": "Need and Meaning of Rational Numbers",
                "difficulty": "Medium",
                "explanation": "Rational numbers include integers and fractions, positive and negative. A rational number can be written as p/q, where p and q are integers and q is not zero. They help us describe parts, debts, temperatures, and exact divisions.",
                "facts": [
                    fact("A rational number can be written as ____.", "p/q", ["p x q", "p + q", "q/0"], "NCERT defines rational numbers in the form p/q."),
                    fact("In p/q, q must not be ____.", "0", ["1", "-1", "10"], "Division by zero is not defined."),
                    fact("-3/5 is a ____ rational number.", "Negative", ["Positive", "Zero", "Not a"], "Its numerator and denominator have unlike signs."),
                    fact("5 can be written as a rational number ____.", "5/1", ["1/5", "5/0", "0/5"], "Every integer can be written with denominator 1."),
                    fact("0 is a ____ number.", "Rational", ["Not rational", "Only irrational", "Undefined"], "0 can be written as 0/1."),
                ],
            },
            {
                "topic": "Standard Form, Number Line and Comparison",
                "difficulty": "Medium",
                "explanation": "Rational numbers can be placed on the number line just like integers. Standard form keeps the denominator positive and common factors removed. For comparison, we can use common denominators or think about positions on the number line.",
                "facts": [
                    fact("In standard form, the denominator is ____.", "Positive", ["Negative", "Zero", "Always 100"], "Standard form uses a positive denominator."),
                    fact("The rational number -2/3 lies between ____.", "-1 and 0", ["0 and 1", "1 and 2", "-3 and -2"], "-2/3 is negative but greater than -1."),
                    fact("Which is greater: -1/2 or -3/4?", "-1/2", ["-3/4", "Both equal", "Cannot compare"], "-1/2 is to the right of -3/4 on the number line."),
                    fact("A rational number equivalent to 1/2 is ____.", "2/4", ["2/3", "1/4", "3/2"], "Multiplying numerator and denominator by 2 gives 2/4."),
                    fact("To compare 2/3 and 3/4, using a common denominator gives ____.", "8/12 and 9/12", ["5/7 and 5/7", "6/6 and 6/6", "2/12 and 3/12"], "The common denominator 12 gives 8/12 and 9/12."),
                ],
            },
            {
                "topic": "Operations on Rational Numbers",
                "difficulty": "Hard",
                "explanation": "Operations on rational numbers combine fraction rules with sign rules. Use common denominators for addition and subtraction, multiply numerators and denominators for multiplication, and use the reciprocal for division. The same integer sign rules still guide the final answer.",
                "facts": [
                    fact("1/2 + 1/3 = ____.", "5/6", ["2/5", "1/6", "3/6"], "Use common denominator 6: 3/6 + 2/6 = 5/6."),
                    fact("3/4 - 1/4 = ____.", "1/2", ["2/4", "4/4", "3/16"], "3/4 - 1/4 = 2/4 = 1/2."),
                    fact("(-2/3) x (3/5) = ____.", "-2/5", ["2/5", "-6/8", "1/5"], "Cancel 3 and multiply with the negative sign."),
                    fact("(1/2) divided by (3/4) = ____.", "2/3", ["3/8", "4/6", "1/6"], "1/2 x 4/3 = 4/6 = 2/3."),
                    fact("To divide rational numbers, multiply by the divisor's ____.", "Reciprocal", ["Mode", "Median", "Square root"], "Division by a rational number uses its reciprocal."),
                ],
            },
        ],
    },
    {
        "name": "Practical Geometry",
        "source_chapter": "Chapter 10: Practical Geometry",
        "modules": [
            {
                "topic": "Constructing a Parallel Line",
                "difficulty": "Medium",
                "explanation": "Practical geometry is drawing with accuracy, not guessing. To construct a line parallel to a given line through a point outside it, NCERT uses the idea of copying an angle with ruler and compass. Equal corresponding angles create parallel lines.",
                "facts": [
                    fact("A line parallel to a given line through an outside point can be made by copying a ____.", "Corresponding angle", ["Median", "Fraction", "Decimal"], "Equal corresponding angles show the new line is parallel."),
                    fact("The main tools used in practical geometry are ruler and ____.", "Compass", ["Calculator", "Abacus only", "Scale pan"], "NCERT constructions use ruler and compass."),
                    fact("Parallel lines in a plane ____ meet.", "Never", ["Always", "Sometimes", "Must"], "Parallel lines do not intersect."),
                    fact("A point not on the line is called an ____ point for this construction.", "External", ["Interior only", "Midpoint", "Vertex only"], "The construction uses a point outside the given line."),
                    fact("Copying an angle helps make matching ____ angles.", "Corresponding", ["Vertical only", "Right only", "Reflex only"], "The parallel-line construction copies a corresponding angle."),
                ],
            },
            {
                "topic": "Triangle Construction: SSS and SAS",
                "difficulty": "Hard",
                "explanation": "Triangles can be constructed when enough exact measurements are known. In SSS, all three side lengths are given. In SAS, two sides and the included angle are given. The included angle must sit between the two known sides.",
                "facts": [
                    fact("SSS construction needs ____ side lengths.", "3", ["1", "2", "4"], "SSS means Side-Side-Side."),
                    fact("SAS construction needs two sides and the included ____.", "Angle", ["Median", "Area", "Altitude"], "SAS means Side-Angle-Side."),
                    fact("The angle in SAS must be ____ the two given sides.", "Between", ["Outside", "Unrelated to", "Opposite any side only"], "Included angle means the angle between the two sides."),
                    fact("A compass helps draw arcs to locate a triangle's ____.", "Vertex", ["Mean", "Percentage", "Mode"], "Arcs from known endpoints locate the third vertex in SSS."),
                    fact("If all three sides are known, the suitable construction criterion is ____.", "SSS", ["ASA", "RHS", "SI"], "SSS uses three sides."),
                ],
            },
            {
                "topic": "Triangle Construction: ASA and RHS",
                "difficulty": "Hard",
                "explanation": "ASA construction uses two angles and the included side. RHS construction is for right triangles when the hypotenuse and one side are known. These criteria match the congruence rules, so the triangle we construct is fixed by the given information.",
                "facts": [
                    fact("ASA construction needs two angles and the included ____.", "Side", ["Area", "Hypotenuse always", "Median"], "ASA means Angle-Side-Angle."),
                    fact("RHS construction is used for ____ triangles.", "Right-angled", ["Equilateral only", "Obtuse only", "Any quadrilateral"], "RHS is for right-angled triangles."),
                    fact("In RHS, H stands for ____.", "Hypotenuse", ["Height", "Half", "Horizontal"], "RHS means Right angle-Hypotenuse-Side."),
                    fact("The side included in ASA lies ____ the two given angles.", "Between", ["Away from", "Outside", "Above only"], "The included side connects the vertices of the two known angles."),
                    fact("The right angle in RHS measures ____.", "90 degrees", ["60 degrees", "180 degrees", "45 degrees"], "Right angle means 90 degrees."),
                ],
            },
        ],
    },
    {
        "name": "Perimeter and Area",
        "source_chapter": "Chapter 11: Perimeter and Area",
        "modules": [
            {
                "topic": "Squares and Rectangles",
                "difficulty": "Easy",
                "explanation": "Perimeter is the distance around a shape, like a fence. Area is the space inside, like floor tiles. For rectangles and squares, the formulas are simple because opposite sides are equal and corners are right angles.",
                "facts": [
                    fact("Perimeter means distance ____ a closed figure.", "Around", ["Inside only", "Above", "Across only"], "Perimeter measures the boundary length."),
                    fact("Area of a rectangle = length x ____.", "Breadth", ["Perimeter", "Height only", "Diagonal"], "Rectangle area is length multiplied by breadth."),
                    fact("Area of a square = side x ____.", "Side", ["Four", "Diagonal", "Radius"], "A square has equal side lengths."),
                    fact("Perimeter of a square = 4 x ____.", "Side", ["Area", "Radius", "Height"], "All four sides of a square are equal."),
                    fact("A rectangle of length 5 cm and breadth 3 cm has area ____.", "15 sq cm", ["8 sq cm", "16 sq cm", "30 sq cm"], "5 x 3 = 15 square centimetres."),
                ],
            },
            {
                "topic": "Parallelograms and Triangles",
                "difficulty": "Medium",
                "explanation": "A parallelogram's area depends on its base and height, not its slant. A triangle is half of a matching parallelogram with the same base and height. These formulas show how shapes can be rearranged without changing area.",
                "facts": [
                    fact("Area of a parallelogram = base x ____.", "Height", ["Side", "Perimeter", "Radius"], "The perpendicular height is used."),
                    fact("Area of a triangle = 1/2 x base x ____.", "Height", ["Radius", "Diameter", "Perimeter"], "A triangle is half a parallelogram with the same base and height."),
                    fact("The height used in area formulas must be ____ to the base.", "Perpendicular", ["Parallel", "Equal always", "Curved"], "Height is the perpendicular distance."),
                    fact("A triangle with base 10 cm and height 6 cm has area ____.", "30 sq cm", ["60 sq cm", "16 sq cm", "20 sq cm"], "1/2 x 10 x 6 = 30."),
                    fact("A parallelogram with base 8 cm and height 5 cm has area ____.", "40 sq cm", ["13 sq cm", "20 sq cm", "80 sq cm"], "8 x 5 = 40."),
                ],
            },
            {
                "topic": "Circles, Units and Applications",
                "difficulty": "Hard",
                "explanation": "Circles use radius and diameter. Circumference is the boundary length, and area is the space inside. NCERT also connects area to unit conversion and real-life applications like paths, fields, and borders, where using the correct unit matters.",
                "facts": [
                    fact("The distance around a circle is its ____.", "Circumference", ["Diameter", "Radius", "Median"], "Circumference is the perimeter of a circle."),
                    fact("Diameter of a circle = 2 x ____.", "Radius", ["Area", "Circumference", "Height"], "Diameter is twice the radius."),
                    fact("Area of a circle = pi x r x ____.", "r", ["d", "2", "h"], "The formula is pi r squared."),
                    fact("1 square metre = ____ square centimetres.", "10000", ["100", "1000", "10"], "Since 1 m = 100 cm, area conversion squares the factor."),
                    fact("If radius is 7 cm, diameter is ____.", "14 cm", ["7 cm", "21 cm", "49 cm"], "Diameter is twice the radius."),
                ],
            },
        ],
    },
    {
        "name": "Algebraic Expressions",
        "source_chapter": "Chapter 12: Algebraic Expressions",
        "modules": [
            {
                "topic": "Terms, Factors and Coefficients",
                "difficulty": "Medium",
                "explanation": "Algebraic expressions are built from numbers, variables, and operation signs. A term is a piece of an expression, and a coefficient is the number multiplying a variable. This language helps us describe patterns without writing every case separately.",
                "facts": [
                    fact("In 5x, the coefficient of x is ____.", "5", ["x", "1", "0"], "The numerical factor multiplying x is 5."),
                    fact("In 3a + 2, the terms are ____.", "3a and 2", ["3 and a only", "a and + only", "2 only"], "Terms are separated by plus or minus signs."),
                    fact("A letter such as x or y in algebra is a ____.", "Variable", ["Constant only", "Median", "Bar"], "Variables represent changing or unknown numbers."),
                    fact("A number without a variable is called a ____.", "Constant", ["Coefficient only", "Triangle", "Factor always"], "Constants have fixed values."),
                    fact("In -7y, the coefficient is ____.", "-7", ["7", "y", "0"], "The sign belongs to the coefficient."),
                ],
            },
            {
                "topic": "Like Terms and Polynomials",
                "difficulty": "Medium",
                "explanation": "Like terms have the same variable part, so they can be combined. Expressions are also named by the number of terms: monomial, binomial, trinomial, or polynomial. These names help us organise algebra before simplifying it.",
                "facts": [
                    fact("3x and 5x are ____ terms.", "Like", ["Unlike", "Constant", "Zero"], "They have the same variable part x."),
                    fact("3x and 3y are ____ terms.", "Unlike", ["Like", "Equal always", "Constants"], "The variable parts are different."),
                    fact("An expression with one term is a ____.", "Monomial", ["Binomial", "Trinomial", "Equation"], "Mono means one."),
                    fact("An expression with two terms is a ____.", "Binomial", ["Monomial", "Trinomial", "Constant only"], "Bi means two."),
                    fact("An expression with three terms is a ____.", "Trinomial", ["Monomial", "Binomial", "Ratio"], "Tri means three."),
                ],
            },
            {
                "topic": "Adding, Subtracting and Evaluating Expressions",
                "difficulty": "Hard",
                "explanation": "To add or subtract algebraic expressions, combine only like terms. To find the value of an expression, substitute the given number for the variable and calculate carefully. Algebra becomes a machine: put in a number, follow the rule, and get an output.",
                "facts": [
                    fact("3x + 5x = ____.", "8x", ["15x", "8", "2x"], "Like terms are added by adding coefficients."),
                    fact("7a - 2a = ____.", "5a", ["9a", "5", "14a"], "Subtract coefficients of like terms."),
                    fact("The value of 2x + 3 when x = 4 is ____.", "11", ["8", "9", "14"], "2 x 4 + 3 = 11."),
                    fact("To evaluate an expression, replace the variable with the given ____.", "Value", ["Angle", "Bar", "Radius"], "Substitution gives the value of the expression."),
                    fact("Unlike terms can be ____ directly.", "Not combined", ["Always added", "Erased", "Multiplied into one term only"], "Only like terms can be combined by addition or subtraction."),
                ],
            },
        ],
    },
    {
        "name": "Exponents and Powers",
        "source_chapter": "Chapter 13: Exponents and Powers",
        "modules": [
            {
                "topic": "Exponents and Powers",
                "difficulty": "Medium",
                "explanation": "Exponents are shortcuts for repeated multiplication. In 2^3, the base is 2 and the exponent is 3, meaning 2 is multiplied three times. Powers help write very large or very small numbers neatly.",
                "facts": [
                    fact("2^3 means ____.", "2 x 2 x 2", ["2 + 3", "3 x 3", "2 x 3"], "The exponent tells how many times the base is multiplied."),
                    fact("In 5^4, the base is ____.", "5", ["4", "20", "9"], "The base is the number being repeatedly multiplied."),
                    fact("In 5^4, the exponent is ____.", "4", ["5", "20", "1"], "The exponent shows the number of factors."),
                    fact("10^2 = ____.", "100", ["20", "12", "1000"], "10 x 10 = 100."),
                    fact("A power is a compact way to show repeated ____.", "Multiplication", ["Addition", "Subtraction", "Division by zero"], "Exponents shorten repeated multiplication."),
                ],
            },
            {
                "topic": "Laws of Exponents",
                "difficulty": "Hard",
                "explanation": "Exponent laws make calculations faster. When multiplying powers with the same base, add exponents. When dividing them, subtract exponents. A power raised to another power multiplies exponents. These rules are like shortcuts for long repeated multiplication.",
                "facts": [
                    fact("a^m x a^n = ____.", "a^(m+n)", ["a^(m-n)", "a^(mn)", "a^(m/n)"], "For the same base, multiplication adds exponents."),
                    fact("a^m divided by a^n = ____.", "a^(m-n)", ["a^(m+n)", "a^(mn)", "a^0 always"], "For the same base, division subtracts exponents."),
                    fact("(a^m)^n = ____.", "a^(mn)", ["a^(m+n)", "a^(m-n)", "a/mn"], "Power of a power multiplies exponents."),
                    fact("2^3 x 2^2 = ____.", "2^5", ["2^6", "4^5", "2^1"], "Same base multiplication adds 3 and 2."),
                    fact("5^4 divided by 5^2 = ____.", "5^2", ["5^6", "1", "25^2"], "Same base division subtracts 2 from 4."),
                ],
            },
            {
                "topic": "Decimal System and Standard Form",
                "difficulty": "Hard",
                "explanation": "Standard form writes very large or very small numbers using powers of 10. This makes numbers easier to read, compare, and calculate. In science and measurement, standard form keeps long strings of zeros from taking over the page.",
                "facts": [
                    fact("1000 can be written as ____.", "10^3", ["10^2", "10^4", "3^10"], "1000 = 10 x 10 x 10."),
                    fact("1,00,000 can be written as ____.", "10^5", ["10^4", "10^6", "5^10"], "One lakh has five zeros."),
                    fact("Standard form commonly uses powers of ____.", "10", ["2", "3", "0"], "The chapter connects standard form with powers of 10."),
                    fact("10^0 is equal to ____.", "1", ["0", "10", "-10"], "Any non-zero number to the power 0 is 1."),
                    fact("Writing 5,000 as 5 x 10^3 is an example of ____ form.", "Standard", ["Fraction", "Congruent", "Median"], "Standard form uses a number multiplied by a power of 10."),
                ],
            },
        ],
    },
    {
        "name": "Symmetry",
        "source_chapter": "Chapter 14: Symmetry",
        "modules": [
            {
                "topic": "Lines of Symmetry",
                "difficulty": "Easy",
                "explanation": "A line of symmetry divides a shape into two matching halves. If you fold the shape along that line, both halves cover each other exactly. Many regular polygons have symmetry, which makes them look balanced and patterned.",
                "facts": [
                    fact("A line of symmetry divides a figure into ____ matching halves.", "Two", ["Three", "No", "Unequal"], "The two halves match exactly."),
                    fact("A square has ____ lines of symmetry.", "4", ["1", "2", "3"], "A square has two diagonal and two midline symmetries."),
                    fact("An equilateral triangle has ____ lines of symmetry.", "3", ["1", "2", "0"], "Each vertex-to-midpoint line is a symmetry line."),
                    fact("A regular pentagon has ____ lines of symmetry.", "5", ["2", "3", "10"], "A regular polygon has as many symmetry lines as sides."),
                    fact("Folding is a useful way to test ____ symmetry.", "Line", ["Rotational only", "Decimal", "Rational"], "Line symmetry can be checked by folding."),
                ],
            },
            {
                "topic": "Rotational Symmetry",
                "difficulty": "Medium",
                "explanation": "Rotational symmetry means a shape looks the same after being turned around a fixed point. The number of times it matches in one full turn is called its order of rotational symmetry. A square, for example, matches several times as it turns.",
                "facts": [
                    fact("Rotational symmetry is checked by ____ a shape.", "Turning", ["Folding only", "Subtracting", "Dividing"], "Rotational symmetry depends on turns."),
                    fact("One full turn measures ____ degrees.", "360", ["90", "180", "45"], "A complete rotation is 360 degrees."),
                    fact("The order of rotational symmetry counts how many times a shape ____ itself in a full turn.", "Matches", ["Shrinks", "Changes size", "Vanishes"], "Order is the number of matching positions."),
                    fact("A square has rotational symmetry of order ____.", "4", ["1", "2", "8"], "A square matches at 90, 180, 270, and 360 degrees."),
                    fact("A shape with no smaller matching turn still has rotational symmetry of order ____.", "1", ["0", "2", "360"], "Every shape matches after one full turn."),
                ],
            },
            {
                "topic": "Line Symmetry and Rotational Symmetry Together",
                "difficulty": "Medium",
                "explanation": "Some shapes have line symmetry, some have rotational symmetry, and some have both. Regular polygons often have both kinds. Comparing the two helps students see that folding symmetry and turning symmetry are related but not the same.",
                "facts": [
                    fact("Line symmetry is tested by folding, while rotational symmetry is tested by ____.", "Turning", ["Counting only", "Adding", "Measuring weight"], "The two symmetries use different actions."),
                    fact("A square has both line symmetry and ____ symmetry.", "Rotational", ["Decimal", "Rational", "Equation"], "A square folds and turns onto itself."),
                    fact("A regular polygon has equal sides and equal ____.", "Angles", ["Areas only", "Heights only", "Modes"], "Regular polygons have equal sides and angles."),
                    fact("A rectangle has rotational symmetry of order ____.", "2", ["1", "3", "4"], "It matches after 180 and 360 degrees."),
                    fact("A circle has many lines of ____.", "Symmetry", ["Equation", "Congruence only", "Probability"], "Every diameter is a line of symmetry."),
                ],
            },
        ],
    },
    {
        "name": "Visualising Solid Shapes",
        "source_chapter": "Chapter 15: Visualising Solid Shapes",
        "modules": [
            {
                "topic": "Plane Figures and Solid Shapes",
                "difficulty": "Easy",
                "explanation": "Plane figures are flat shapes like triangles and squares. Solid shapes are three-dimensional, like cubes, cuboids, cones, and cylinders. Solids have faces, edges, and vertices, which help us describe and compare them clearly.",
                "facts": [
                    fact("A square is a ____ figure.", "Plane", ["Solid", "3D only", "Curved only"], "A square is flat and two-dimensional."),
                    fact("A cube is a ____ shape.", "Solid", ["Plane", "Line", "Angle"], "A cube is three-dimensional."),
                    fact("A cube has ____ faces.", "6", ["4", "8", "12"], "A cube has six square faces."),
                    fact("A cube has ____ edges.", "12", ["6", "8", "4"], "The twelve line segments are its edges."),
                    fact("A cube has ____ vertices.", "8", ["6", "12", "4"], "A cube has eight corners."),
                ],
            },
            {
                "topic": "Nets for 3D Shapes",
                "difficulty": "Medium",
                "explanation": "A net is a flat pattern that can be folded to make a solid. It is like opening a box carefully and laying it flat. Nets connect 2D drawings with 3D shapes and help us imagine how faces join together.",
                "facts": [
                    fact("A net is a flat pattern of a ____ shape.", "Solid", ["Number line", "Equation", "Fraction"], "A net folds to form a solid."),
                    fact("A cube net is made of ____ squares.", "6", ["4", "8", "12"], "A cube has six square faces."),
                    fact("Folding a correct cube net forms a ____.", "Cube", ["Circle", "Triangle only", "Bar graph"], "The net's six squares fold into a cube."),
                    fact("Nets help us connect 2D figures with ____ shapes.", "3D", ["1D", "Only decimal", "No"], "Nets are flat layouts of solids."),
                    fact("A cuboid net contains rectangular ____.", "Faces", ["Angles only", "Medians", "Probabilities"], "A cuboid is made from rectangular faces."),
                ],
            },
            {
                "topic": "Sketches, Views and Sections",
                "difficulty": "Medium",
                "explanation": "We can draw solids on flat paper using oblique or isometric sketches. We can also view solids from the front, side, or top, and study sections made by slicing. These skills train the mind to turn objects around without touching them.",
                "facts": [
                    fact("An isometric sketch is used to draw ____ shapes on paper.", "3D", ["Only 1D", "Only fractions", "Only equations"], "Isometric sketches represent solids on flat paper."),
                    fact("Viewing a solid from above gives the ____ view.", "Top", ["Front", "Side", "Inside only"], "The top view is seen from above."),
                    fact("Viewing a solid from the front gives the ____ view.", "Front", ["Top", "Side", "Bottom only"], "Front view is seen from the front direction."),
                    fact("Cutting a solid to see a face is called taking a ____.", "Section", ["Mode", "Percentage", "Ratio"], "A section can be seen by slicing a solid."),
                    fact("A shadow gives information about a solid's ____.", "View", ["Interest only", "Mean", "Equation"], "NCERT uses shadow play to understand views of solids."),
                ],
            },
        ],
    },
]


def build():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    chapters = []
    manifest = {
        "board": "CBSE",
        "class": 7,
        "subject": "Mathematics",
        "source_pdf": PDF_SOURCE,
        "schema": "learn_edu_strict_chapter_modules_v1",
        "content_rule": "Questions are derived from NCERT Class 7 Mathematics chapter sections, definitions, formulas, examples, and exercise patterns.",
        "chapters": [],
    }

    for chapter_index, chapter in enumerate(CHAPTERS, start=1):
        module_entries = []
        manifest_modules = []
        for module_index, module in enumerate(chapter["modules"], start=1):
            difficulty = module["difficulty"]
            timer = TIMERS[difficulty]
            facts = module["facts"]
            questions = [
                make_question(
                    question_id=index,
                    prompt=item["prompt"],
                    correct=item["correct"],
                    wrongs=item["wrongs"],
                    rationale=item["rationale"],
                    timer=timer,
                )
                for index, item in enumerate(facts, start=1)
            ]
            module_entries.append(
                {
                    "module_id": module_index,
                    "topic_name": module["topic"],
                    "explanation": module["explanation"],
                    "difficulty": difficulty,
                    "total_timer_minutes": TOTAL_TIMERS[difficulty],
                    "questions": questions,
                }
            )
            manifest_modules.append(
                {
                    "module_id": module_index,
                    "topic_name": module["topic"],
                    "source_section_basis": chapter["source_chapter"],
                    "difficulty": difficulty,
                    "question_count": len(questions),
                    "trace_id": f"cbse-class7-{chapter_index:02d}-{slug(module['topic'])}",
                }
            )
        chapters.append({"chapter_name": chapter["name"], "modules": module_entries})
        manifest["chapters"].append(
            {
                "chapter_name": chapter["name"],
                "source_chapter": chapter["source_chapter"],
                "module_count": len(module_entries),
                "question_count": sum(len(module["questions"]) for module in module_entries),
                "modules": manifest_modules,
            }
        )

    manifest["total_chapters"] = len(chapters)
    manifest["total_modules"] = sum(len(chapter["modules"]) for chapter in chapters)
    manifest["total_questions"] = sum(
        len(module["questions"]) for chapter in chapters for module in chapter["modules"]
    )
    return chapters, manifest


def validate(chapters):
    total_questions = 0
    for chapter in chapters:
        assert chapter["chapter_name"]
        assert chapter["modules"]
        for module in chapter["modules"]:
            assert 5 <= len(module["questions"]) <= 15, module["topic_name"]
            assert len(module["explanation"].split()) <= 150, module["topic_name"]
            assert module["difficulty"] in TIMERS, module["topic_name"]
            assert module["total_timer_minutes"] == TOTAL_TIMERS[module["difficulty"]]
            for question in module["questions"]:
                assert len(question["options"]) == 4, question["question_text"]
                assert question["correct_answer"] in question["options"], question["question_text"]
                assert question["timer_per_question_seconds"] == TIMERS[module["difficulty"]]
                assert question["rationale"], question["question_text"]
            total_questions += len(module["questions"])
    assert total_questions >= 75


def main():
    chapters, manifest = build()
    validate(chapters)
    OUTPUT_JSON.write_text(json.dumps(chapters, indent=2), encoding="utf-8")
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(
        f"Wrote {OUTPUT_JSON} with {manifest['total_chapters']} chapters, "
        f"{manifest['total_modules']} modules, {manifest['total_questions']} questions."
    )
    print(f"Wrote {OUTPUT_MANIFEST}")


if __name__ == "__main__":
    main()
