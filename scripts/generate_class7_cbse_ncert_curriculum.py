import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "class7_cbse_ncert_duolingo_curriculum.json"


def question(question_id, text, options, answer, rationale, seconds):
    return {
        "question_id": question_id,
        "question_text": text,
        "options": options,
        "correct_answer": answer,
        "rationale": rationale,
        "timer_per_question_seconds": seconds,
    }


def module(module_id, topic_name, explanation, difficulty, minutes, questions):
    seconds = {"Easy": 30, "Medium": 45, "Hard": 60}[difficulty]
    return {
        "module_id": module_id,
        "topic_name": topic_name,
        "explanation": explanation,
        "difficulty": difficulty,
        "total_timer_minutes": minutes,
        "questions": [
            question(i + 1, q[0], q[1], q[2], q[3], seconds)
            for i, q in enumerate(questions)
        ],
    }


chapters = [
    {
        "chapter_name": "Integers",
        "modules": [
            module(
                1,
                "Addition, Subtraction and Properties of Integers",
                "Integers are whole numbers with signs: positive, negative, and zero. Imagine a lift: going up is positive and going down is negative. Adding a positive integer moves right on the number line, while adding a negative integer moves left. Subtraction can be changed into addition of the opposite number. Properties such as closure, commutativity, associativity, and additive identity help us calculate faster and check whether a statement is always true.",
                "Medium",
                8,
                [
                    ("What is 7 + (-3)?", ["10", "4", "-4", "-10"], "4", "Adding -3 means moving 3 steps left from 7."),
                    ("Which expression is equal to 5 - (-2)?", ["5 + 2", "5 - 2", "-5 + 2", "-5 - 2"], "5 + 2", "Subtracting a negative is the same as adding its opposite."),
                    ("Which property is shown by 3 + (-5) = (-5) + 3?", ["Closure", "Commutative property", "Associative property", "Identity property"], "Commutative property", "The order of addends changes but the sum remains the same."),
                    ("Which operation is not commutative for integers?", ["Addition", "Subtraction", "Multiplication", "Adding zero"], "Subtraction", "For example, 5 - 2 is not equal to 2 - 5."),
                    ("Which integer is the additive identity?", ["1", "-1", "0", "10"], "0", "Adding zero does not change an integer."),
                ],
            ),
            module(
                2,
                "Multiplication and Division of Integers",
                "Multiplication and division of integers follow simple sign rules. Same signs give a positive answer, while different signs give a negative answer. Multiplying by zero always gives zero, and multiplying by one leaves a number unchanged. The distributive property lets us break a difficult multiplication into easier parts. These rules help in situations like repeated gains, repeated losses, temperatures, and debts.",
                "Medium",
                9,
                [
                    ("What is (-4) x 6?", ["24", "-24", "10", "-10"], "-24", "Different signs give a negative product."),
                    ("What is (-7) x (-3)?", ["-21", "21", "10", "-10"], "21", "Same signs give a positive product."),
                    ("What is (-36) ÷ 9?", ["4", "-4", "27", "-27"], "-4", "Different signs give a negative quotient."),
                    ("What is 0 x (-15)?", ["15", "-15", "0", "1"], "0", "Any integer multiplied by zero is zero."),
                    ("Which property is shown by 3 x (4 + 5) = 3 x 4 + 3 x 5?", ["Closure", "Distributive property", "Additive identity", "Commutative subtraction"], "Distributive property", "Multiplication is distributed over addition."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "Fractions and Decimals",
        "modules": [
            module(
                1,
                "Multiplication and Division of Fractions",
                "Multiplying fractions is like taking a part of a part. To multiply, multiply numerators and denominators. Dividing by a fraction asks how many of that part fit into the quantity. For division, we multiply by the reciprocal of the divisor. These ideas are useful in sharing, recipes, lengths, and comparing parts of whole objects.",
                "Hard",
                10,
                [
                    ("What is 1/2 x 1/3?", ["1/5", "1/6", "2/3", "3/2"], "1/6", "Multiply numerators and denominators: 1 x 1 over 2 x 3."),
                    ("What is 3 x 2/5?", ["5/6", "6/5", "2/15", "3/10"], "6/5", "Three groups of 2/5 make 6/5."),
                    ("What is the reciprocal of 3/5?", ["3/5", "5/3", "-3/5", "2/5"], "5/3", "The reciprocal interchanges numerator and denominator."),
                    ("What is 2 ÷ 1/2?", ["1", "2", "4", "1/4"], "4", "There are four halves in 2."),
                    ("What is 3/4 ÷ 1/2?", ["3/8", "2/3", "3/2", "1/6"], "3/2", "Multiply 3/4 by the reciprocal 2/1."),
                ],
            ),
            module(
                2,
                "Multiplication and Division of Decimals",
                "Decimals are fractions written with place value. When multiplying by 10, 100, or 1000, the decimal point shifts right. When dividing by them, it shifts left. Decimal multiplication uses whole-number multiplication first, then careful decimal placement. Decimal division becomes easier when we convert or shift decimals sensibly.",
                "Medium",
                9,
                [
                    ("What is 2.5 x 10?", ["0.25", "2.50", "25", "250"], "25", "Multiplying by 10 shifts the decimal one place right."),
                    ("What is 3.75 ÷ 100?", ["375", "37.5", "0.375", "0.0375"], "0.0375", "Dividing by 100 shifts the decimal two places left."),
                    ("What is 1.2 x 0.3?", ["0.36", "3.6", "36", "0.036"], "0.36", "12 x 3 = 36, with two decimal places total."),
                    ("What is 4.8 ÷ 2?", ["2.4", "24", "0.24", "9.6"], "2.4", "48 divided by 2 is 24, so 4.8 divided by 2 is 2.4."),
                    ("What is 0.6 x 1000?", ["0.006", "6", "60", "600"], "600", "Multiplying by 1000 shifts the decimal three places right."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "Data Handling",
        "modules": [
            module(
                1,
                "Collecting Data and Representative Values",
                "Data is information collected to answer a question. Raw data can look messy, so we organise it using tables, tally marks, or lists. Mean, median, mode, and range help describe the data with useful summary values. Mean is the fair-share average, median is the middle value, mode is most frequent, and range shows spread.",
                "Hard",
                10,
                [
                    ("What is data?", ["Only numbers", "Collected information", "Only a graph", "A ruler"], "Collected information", "Data means information gathered for a purpose."),
                    ("Which tool is useful for counting repeated observations?", ["Tally marks", "Compass", "Protractor", "Divider"], "Tally marks", "Tally marks make repeated counting quick and clear."),
                    ("Find the mean of 2, 4, 6.", ["3", "4", "6", "12"], "4", "Mean is 12 divided by 3."),
                    ("What is the mode of 5, 7, 5, 9, 5?", ["5", "7", "9", "31"], "5", "5 occurs most often."),
                    ("What is the range of 4, 10, 6, 2?", ["2", "6", "8", "10"], "8", "Range is largest minus smallest: 10 - 2."),
                ],
            ),
            module(
                2,
                "Bar Graphs, Chance and Probability",
                "A bar graph uses bars to compare data. The scale tells what each unit length represents, so a good scale makes graphs easier to read. Chance describes how likely something is to happen. Some events are certain, some are impossible, and some may or may not happen, such as the result of tossing a coin.",
                "Medium",
                8,
                [
                    ("In a bar graph, bars are used to", ["measure angles", "compare data", "draw circles", "solve equations"], "compare data", "Bar heights or lengths represent quantities."),
                    ("The scale of a graph tells", ["colour of bars", "what each unit represents", "only the title", "the median"], "what each unit represents", "Scale connects graph length to data value."),
                    ("Tossing a coin has how many common outcomes?", ["1", "2", "3", "4"], "2", "A coin has head and tail outcomes."),
                    ("An event that cannot happen is", ["certain", "impossible", "likely", "average"], "impossible", "Impossible events have no chance of occurring."),
                    ("Which is a chance situation?", ["Measuring a fixed ruler", "Tossing a coin", "Writing 2 + 3 = 5", "Counting sides of a square"], "Tossing a coin", "The outcome is not known in advance."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "Simple Equations",
        "modules": [
            module(
                1,
                "Setting Up and Solving Equations",
                "An equation is like a balance scale: both sides must have equal value. A variable such as x represents an unknown number. We can turn a word problem into an equation by identifying the unknown and the relationship given. To solve, we perform the same operation on both sides until the variable is alone.",
                "Medium",
                9,
                [
                    ("In x + 5 = 12, x is called a", ["constant", "variable", "fraction", "angle"], "variable", "A variable represents an unknown value."),
                    ("Which is an equation?", ["x + 3", "7 > 5", "x + 2 = 9", "4, 5, 6"], "x + 2 = 9", "An equation has an equality sign."),
                    ("Solve x + 7 = 15.", ["7", "8", "15", "22"], "8", "Subtract 7 from both sides."),
                    ("Solve 3x = 18.", ["3", "6", "15", "21"], "6", "Divide both sides by 3."),
                    ("Solve x/5 = 4.", ["1", "5", "9", "20"], "20", "Multiply both sides by 5."),
                ],
            )
        ],
    },
    {
        "chapter_name": "Lines and Angles",
        "modules": [
            module(
                1,
                "Related Angles",
                "Angles can work in pairs. Complementary angles add to 90 degrees, while supplementary angles add to 180 degrees. Adjacent angles share a vertex and an arm. A linear pair forms a straight line and always adds to 180 degrees. Recognising these relationships helps us find unknown angles without measuring each one.",
                "Medium",
                8,
                [
                    ("Complementary angles add to", ["45°", "90°", "180°", "360°"], "90°", "Complementary angles form a right angle together."),
                    ("Supplementary angles add to", ["90°", "100°", "180°", "360°"], "180°", "Supplementary angles form a straight angle together."),
                    ("If one complementary angle is 35°, the other is", ["35°", "55°", "65°", "145°"], "55°", "90° - 35° = 55°."),
                    ("A linear pair adds to", ["90°", "180°", "270°", "360°"], "180°", "A linear pair forms a straight line."),
                    ("Adjacent angles must have", ["no common point", "a common vertex and arm", "equal measures always", "parallel arms always"], "a common vertex and arm", "Adjacent angles share a vertex and a common arm."),
                ],
            ),
            module(
                2,
                "Intersecting Lines, Transversals and Parallel Lines",
                "When two lines meet, they form angles around the intersection. Vertically opposite angles are always equal. A transversal is a line that cuts two or more lines. When it cuts parallel lines, angle pairs such as corresponding and alternate interior angles show useful equalities. These are geometry clues for checking whether lines are parallel.",
                "Hard",
                10,
                [
                    ("Vertically opposite angles are", ["always equal", "always supplementary", "always zero", "always unequal"], "always equal", "Angles opposite each other at an intersection are equal."),
                    ("A transversal is a line that", ["never meets any line", "cuts two or more lines", "is always curved", "is always vertical"], "cuts two or more lines", "A transversal intersects two or more lines."),
                    ("If two parallel lines are cut by a transversal, corresponding angles are", ["equal", "always 90°", "always 180°", "not related"], "equal", "Corresponding angles are equal for parallel lines."),
                    ("If one angle in a linear pair is 120°, the other is", ["60°", "90°", "120°", "240°"], "60°", "Linear pair angles sum to 180°."),
                    ("Alternate interior angles of parallel lines are", ["equal", "supplementary only", "always acute", "always exterior"], "equal", "They are equal when lines are parallel."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "The Triangle and its Properties",
        "modules": [
            module(
                1,
                "Medians, Altitudes and Angle Properties",
                "A median joins a vertex of a triangle to the midpoint of the opposite side. An altitude is a perpendicular line segment from a vertex to the opposite side or its extension. Every triangle’s three angles add to 180 degrees. An exterior angle equals the sum of the two opposite interior angles, helping us find missing angles quickly.",
                "Medium",
                9,
                [
                    ("A median joins a vertex to", ["any point", "midpoint of opposite side", "another vertex only", "centre of circle"], "midpoint of opposite side", "That is the definition of a median."),
                    ("How many medians does a triangle have?", ["1", "2", "3", "4"], "3", "Each vertex can have one median."),
                    ("An altitude is drawn", ["parallel to a side", "perpendicular to the opposite side", "only outside always", "only in squares"], "perpendicular to the opposite side", "Altitude represents height from a vertex."),
                    ("The sum of angles in a triangle is", ["90°", "180°", "270°", "360°"], "180°", "This is the angle sum property."),
                    ("If two angles are 50° and 60°, the third angle is", ["30°", "70°", "110°", "180°"], "70°", "180° - 50° - 60° = 70°."),
                ],
            ),
            module(
                2,
                "Triangle Inequality and Pythagoras Property",
                "The sides of a triangle follow an important rule: the sum of any two sides must be greater than the third side. This helps decide whether a triangle can be formed. In a right-angled triangle, the Pythagoras property says that the square on the hypotenuse equals the sum of squares on the other two sides.",
                "Hard",
                10,
                [
                    ("Can sides 2 cm, 3 cm, 6 cm form a triangle?", ["Yes", "No", "Only right triangle", "Only equilateral"], "No", "2 + 3 is not greater than 6."),
                    ("In a right triangle, the side opposite the right angle is called", ["median", "altitude", "hypotenuse", "base only"], "hypotenuse", "The hypotenuse is opposite the 90° angle."),
                    ("For a right triangle with legs 3 and 4, hypotenuse is", ["5", "6", "7", "25"], "5", "3² + 4² = 25, so the hypotenuse is 5."),
                    ("Which set can form a triangle?", ["1, 2, 3", "2, 3, 6", "4, 5, 6", "2, 2, 5"], "4, 5, 6", "The sum of any two sides is greater than the third."),
                    ("Pythagoras property applies to", ["all triangles", "right-angled triangles", "only squares", "circles"], "right-angled triangles", "The property is for right-angled triangles."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "Congruence of Triangles",
        "modules": [
            module(
                1,
                "Congruence and Criteria for Triangles",
                "Congruent figures are exact copies in shape and size. For triangles, we use special rules instead of checking every part: SSS, SAS, ASA, and RHS. SSS uses three sides, SAS uses two sides and the included angle, ASA uses two angles and the included side, and RHS works for right-angled triangles.",
                "Hard",
                10,
                [
                    ("Congruent figures have", ["same shape and size", "same colour only", "same position only", "different sizes"], "same shape and size", "Congruence means exact matching."),
                    ("SSS congruence uses", ["three sides", "two sides only", "three angles only", "one right angle only"], "three sides", "SSS means side-side-side."),
                    ("SAS congruence needs", ["two sides and included angle", "two angles only", "three sides", "one side only"], "two sides and included angle", "SAS means side-angle-side with included angle."),
                    ("RHS congruence is used for", ["right triangles", "all circles", "bar graphs", "parallel lines"], "right triangles", "RHS stands for Right angle-Hypotenuse-Side."),
                    ("AAA is not a congruence criterion because it fixes", ["shape but not size", "size only", "colour only", "nothing"], "shape but not size", "Triangles may have the same angles but different sizes."),
                ],
            )
        ],
    },
    {
        "chapter_name": "Comparing Quantities",
        "modules": [
            module(
                1,
                "Ratios, Percentages and Percent Change",
                "Ratios compare two quantities, while percentages compare a quantity with 100. Fractions, decimals, and percentages are connected, so we can convert between them. Percent increase and decrease help describe real-life changes in prices, marks, and quantities. These tools make comparison simpler and fairer.",
                "Medium",
                8,
                [
                    ("Percent means per", ["10", "100", "1000", "1"], "100", "Percent means out of hundred."),
                    ("1/2 as a percentage is", ["25%", "50%", "75%", "100%"], "50%", "1/2 = 50/100 = 50%."),
                    ("0.25 as a percentage is", ["2.5%", "25%", "250%", "0.25%"], "25%", "0.25 x 100 = 25%."),
                    ("25% as a fraction is", ["1/4", "1/2", "3/4", "1/25"], "1/4", "25/100 simplifies to 1/4."),
                    ("A 10% increase on 200 equals", ["10", "20", "100", "210"], "20", "10/100 of 200 is 20."),
                ],
            ),
            module(
                2,
                "Profit, Loss and Simple Interest",
                "Buying and selling use cost price and selling price. If selling price is more than cost price, there is profit. If it is less, there is loss. Simple interest is extra money paid for using borrowed money. It depends on principal, rate, and time, and is calculated using SI = P x R x T / 100.",
                "Hard",
                10,
                [
                    ("If CP = Rs 100 and SP = Rs 120, profit is", ["Rs 20", "Rs 120", "Rs 100", "Rs 220"], "Rs 20", "Profit = SP - CP."),
                    ("If CP = Rs 80 and SP = Rs 60, there is", ["profit", "loss", "no change", "interest"], "loss", "Selling price is less than cost price."),
                    ("Profit percentage is calculated on", ["selling price", "cost price", "marked price only", "discount only"], "cost price", "Profit percent compares profit with cost price."),
                    ("In simple interest, P stands for", ["Profit", "Principal", "Percent only", "Price tag"], "Principal", "Principal is the original borrowed or invested amount."),
                    ("Find SI on Rs 1000 at 10% for 1 year.", ["Rs 10", "Rs 100", "Rs 1000", "Rs 1100"], "Rs 100", "1000 x 10 x 1 / 100 = 100."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "Rational Numbers",
        "modules": [
            module(
                1,
                "Meaning, Standard Form and Comparison",
                "Rational numbers are numbers that can be written as p/q, where p and q are integers and q is not zero. Standard form keeps the denominator positive and removes common factors. Rational numbers can be placed on a number line, where values to the right are greater and values to the left are smaller.",
                "Medium",
                9,
                [
                    ("A rational number can be written as", ["p/q, q not 0", "p/q, q = 0", "only whole number", "only decimal"], "p/q, q not 0", "The denominator cannot be zero."),
                    ("In standard form, denominator is", ["negative", "positive", "zero", "always 1"], "positive", "Standard form uses a positive denominator."),
                    ("0 can be written as", ["0/5", "5/0", "0/0", "not rational"], "0/5", "0 divided by a non-zero integer is rational."),
                    ("Which is greater: -1/2 or 1/2?", ["-1/2", "1/2", "Both equal", "Cannot compare"], "1/2", "Positive numbers are greater than negative numbers."),
                    ("On the number line, negative rational numbers lie", ["right of zero", "left of zero", "only at zero", "above the line"], "left of zero", "Negative values are placed left of zero."),
                ],
            ),
            module(
                2,
                "Operations on Rational Numbers",
                "Rational numbers can be added, subtracted, multiplied, and divided. Addition and subtraction often need common denominators. Multiplication uses numerator times numerator and denominator times denominator. Division uses the reciprocal of the divisor. The sign rules from integers still apply.",
                "Hard",
                10,
                [
                    ("What is 1/3 + 1/3?", ["1/6", "2/3", "2/6", "1"], "2/3", "Same denominators: add numerators."),
                    ("What is 1/2 - 1/4?", ["1/4", "2/4", "3/4", "0"], "1/4", "1/2 = 2/4, and 2/4 - 1/4 = 1/4."),
                    ("What is (-2/3) x (3/4)?", ["-1/2", "1/2", "-6/7", "6/12"], "-1/2", "Different signs give negative; 6/12 simplifies to 1/2."),
                    ("What is 2/5 ÷ 4/5?", ["1/2", "8/25", "10/20", "2"], "1/2", "2/5 x 5/4 = 10/20 = 1/2."),
                    ("To divide rational numbers, multiply by", ["zero", "the reciprocal of divisor", "same denominator only", "100"], "the reciprocal of divisor", "Division by a rational number uses reciprocal."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "Practical Geometry",
        "modules": [
            module(
                1,
                "Constructing Parallel Lines and Triangles",
                "Practical geometry uses ruler and compass to draw accurate figures. To construct a parallel line, we copy an angle made by a transversal. Triangles can be constructed when enough measurements are given: SSS, SAS, ASA, or RHS. Each construction follows steps, like a recipe, to locate points accurately.",
                "Hard",
                10,
                [
                    ("To draw accurate geometry, we commonly use", ["ruler and compass", "calculator only", "bar graph", "dice"], "ruler and compass", "Practical geometry constructions use these tools."),
                    ("Parallel lines", ["meet at one point", "never meet", "are always curved", "always form triangles"], "never meet", "Parallel lines do not intersect."),
                    ("SSS construction needs", ["three sides", "two angles only", "one side only", "a circle radius only"], "three sides", "SSS means all three side lengths are given."),
                    ("SAS construction needs", ["two sides and included angle", "three angles", "one angle only", "no side"], "two sides and included angle", "SAS data locates the triangle."),
                    ("RHS construction is for", ["right-angled triangle", "equilateral only", "bar graph", "circle"], "right-angled triangle", "RHS uses right angle, hypotenuse, and one side."),
                ],
            )
        ],
    },
    {
        "chapter_name": "Perimeter and Area",
        "modules": [
            module(
                1,
                "Area and Perimeter of Plane Figures",
                "Perimeter is the distance around a shape, while area is the surface covered. Rectangles, squares, triangles, parallelograms, and circles each have useful formulas. The height used in area formulas must be perpendicular to the base. These ideas help measure fields, floors, paper, paths, and round objects.",
                "Hard",
                10,
                [
                    ("Area of a rectangle is", ["l + b", "2(l + b)", "l x b", "l - b"], "l x b", "Rectangle area equals length times breadth."),
                    ("Perimeter of a square of side s is", ["s²", "4s", "2s", "s/4"], "4s", "A square has four equal sides."),
                    ("Area of a triangle is", ["base x height", "1/2 x base x height", "2 x base x height", "base + height"], "1/2 x base x height", "A triangle is half of a related rectangle or parallelogram."),
                    ("Area of a parallelogram is", ["base x height", "base + height", "side x side", "1/2 base x height"], "base x height", "The perpendicular height is used."),
                    ("Circumference of a circle is", ["2πr", "πr²", "l x b", "4s"], "2πr", "Circumference is the boundary length of a circle."),
                ],
            ),
            module(
                2,
                "Conversion of Units and Applications",
                "Before calculating area or perimeter, units should match. Metres and centimetres cannot be mixed directly. Area units convert as squares: 1 square metre equals 10,000 square centimetres because 1 metre is 100 centimetres in both length and breadth. Careful conversion keeps real-life measurement problems accurate.",
                "Medium",
                8,
                [
                    ("1 m equals", ["10 cm", "100 cm", "1000 cm", "1 cm"], "100 cm", "A metre has 100 centimetres."),
                    ("1 m² equals", ["100 cm²", "1000 cm²", "10000 cm²", "10 cm²"], "10000 cm²", "100 cm x 100 cm = 10000 cm²."),
                    ("Before calculating area with mixed units, first", ["ignore units", "make units same", "add pi", "draw a bar graph"], "make units same", "Common units are needed for correct calculation."),
                    ("Area of a rectangular field tells", ["boundary length only", "surface covered", "angle measure", "probability"], "surface covered", "Area measures covered surface."),
                    ("A path around a garden is related to", ["perimeter", "median", "mode", "exponent"], "perimeter", "Perimeter measures distance around."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "Algebraic Expressions",
        "modules": [
            module(
                1,
                "Terms, Like Terms and Values of Expressions",
                "Algebraic expressions are built using variables, constants, and operations. Terms are parts separated by plus or minus signs. Like terms have the same variables raised to the same powers, so only like terms can be combined. To find the value of an expression, substitute the given number for the variable and simplify.",
                "Hard",
                10,
                [
                    ("In 5x + 3, x is", ["constant", "variable", "coefficient", "term only"], "variable", "A variable can take different values."),
                    ("In 7y, coefficient of y is", ["7", "y", "0", "1"], "7", "The numerical factor multiplying y is 7."),
                    ("Which are like terms?", ["3x and 5x", "3x and 5y", "x and x²", "2a and 2b"], "3x and 5x", "They have the same variable x with the same power."),
                    ("Simplify 3x + 2x.", ["5x", "6x", "5x²", "x"], "5x", "Like terms are added by adding coefficients."),
                    ("Value of x + 5 when x = 4 is", ["5", "4", "9", "20"], "9", "Substitute x = 4: 4 + 5 = 9."),
                ],
            )
        ],
    },
    {
        "chapter_name": "Exponents and Powers",
        "modules": [
            module(
                1,
                "Exponents and Laws of Exponents",
                "Exponents are a short way to write repeated multiplication. In 2³, 2 is the base and 3 is the exponent. Laws of exponents help simplify powers: multiply same bases by adding exponents, divide same bases by subtracting exponents, and raise a power to a power by multiplying exponents.",
                "Hard",
                10,
                [
                    ("2³ means", ["2 + 3", "2 x 2 x 2", "3 x 3", "2 x 3"], "2 x 2 x 2", "The exponent 3 means 2 is multiplied three times."),
                    ("In 5², the base is", ["5", "2", "10", "25"], "5", "The base is the repeated factor."),
                    ("a^m x a^n equals", ["a^(m+n)", "a^(m-n)", "a^(mn)", "a/(m+n)"], "a^(m+n)", "Same bases are multiplied by adding exponents."),
                    ("a^m ÷ a^n equals", ["a^(m+n)", "a^(m-n)", "a^(mn)", "a^0 only"], "a^(m-n)", "Same bases are divided by subtracting exponents."),
                    ("(a^m)^n equals", ["a^(m+n)", "a^(m-n)", "a^(mn)", "a/mn"], "a^(mn)", "Power of a power multiplies exponents."),
                ],
            ),
            module(
                2,
                "Decimal Number System and Standard Form",
                "Standard form helps write very large numbers compactly using powers of 10. Instead of writing many zeros, we write a number between 1 and 10 multiplied by a power of 10. For example, 50,000 becomes 5 x 10⁴. This is useful in science, astronomy, and measurement.",
                "Medium",
                8,
                [
                    ("100000 equals", ["10²", "10³", "10⁴", "10⁵"], "10⁵", "There are five zeros, so it is 10 to the power 5."),
                    ("50,000 in standard form is", ["5 x 10⁴", "50 x 10³", "0.5 x 10⁵", "5 x 10³"], "5 x 10⁴", "5 x 10,000 = 50,000."),
                    ("Standard form uses a number between", ["0 and 1", "1 and 10", "10 and 100", "100 and 1000"], "1 and 10", "The coefficient is at least 1 and less than 10."),
                    ("7 x 10³ equals", ["70", "700", "7000", "70000"], "7000", "10³ = 1000, so 7 x 1000 = 7000."),
                    ("Powers of 10 are useful because they", ["avoid place value", "write large numbers shortly", "remove multiplication", "make all numbers zero"], "write large numbers shortly", "They reduce repeated zeros."),
                ],
            ),
        ],
    },
    {
        "chapter_name": "Symmetry",
        "modules": [
            module(
                1,
                "Line Symmetry and Rotational Symmetry",
                "A line of symmetry divides a figure into two matching halves. Regular polygons often have several lines of symmetry because their sides and angles are equal. Rotational symmetry means a figure looks the same after being turned by an angle less than 360 degrees. The order tells how many times it matches in one full turn.",
                "Medium",
                8,
                [
                    ("A line of symmetry divides a figure into", ["two matching halves", "three random parts", "only unequal parts", "a circle"], "two matching halves", "The halves overlap exactly."),
                    ("How many lines of symmetry does a square have?", ["1", "2", "4", "8"], "4", "A square has two diagonals and two midlines as symmetry lines."),
                    ("An equilateral triangle has how many lines of symmetry?", ["1", "2", "3", "0"], "3", "Each vertex-to-midpoint line is a symmetry line."),
                    ("Rotational symmetry means a figure matches after", ["turning", "only folding", "measuring area", "adding angles"], "turning", "The figure is rotated about a point."),
                    ("Order of rotational symmetry of a square is", ["1", "2", "3", "4"], "4", "A square matches four times in a full turn."),
                ],
            )
        ],
    },
    {
        "chapter_name": "Visualising Solid Shapes",
        "modules": [
            module(
                1,
                "Faces, Edges, Vertices and Nets",
                "Solid shapes are three-dimensional objects. A face is a flat surface, an edge is where two faces meet, and a vertex is a corner. A net is a flat pattern that can be folded to make a solid, like opening a cardboard box and laying it flat. Nets help us connect 2-D drawings with 3-D objects.",
                "Medium",
                8,
                [
                    ("A face of a solid is", ["a flat surface", "a corner", "a line only", "a shadow"], "a flat surface", "Faces are surfaces of solids."),
                    ("An edge is where", ["two faces meet", "two numbers add", "angles vanish", "data is counted"], "two faces meet", "Edges are line segments joining faces."),
                    ("A vertex is", ["a corner", "a face", "a curved surface", "a net"], "a corner", "Vertices are corner points of solids."),
                    ("A cube has how many faces?", ["4", "6", "8", "12"], "6", "A cube has six square faces."),
                    ("A cube net is made of", ["six squares", "four triangles", "one circle", "two rectangles only"], "six squares", "A cube has six square faces."),
                ],
            ),
            module(
                2,
                "Sketches, Sections and Views of Solids",
                "Solids can look different depending on how we view them. Oblique and isometric sketches show 3-D objects on flat paper. We can understand solids by slicing them, watching their shadows, or looking from the front, side, and top. These activities build spatial thinking and help students imagine shapes clearly.",
                "Medium",
                8,
                [
                    ("Oblique and isometric sketches are used to", ["draw solids on flat paper", "calculate interest", "find mode", "compare fractions"], "draw solids on flat paper", "They represent 3-D shapes in 2-D drawings."),
                    ("One way to view a solid is by", ["cutting or slicing", "finding mean", "adding exponents", "using profit"], "cutting or slicing", "The chapter discusses sections formed by slicing."),
                    ("A shadow of a 3-D object is usually", ["2-D", "4-D", "always a cube", "always a triangle"], "2-D", "A shadow appears on a flat surface."),
                    ("Top view means looking", ["from above", "from below only", "from inside", "through data"], "from above", "Top view shows what is seen from the top."),
                    ("Different views of a solid can be", ["front, side and top", "mean, median, mode", "profit, loss, interest", "base, exponent, power"], "front, side and top", "These are standard views of solids."),
                ],
            ),
        ],
    },
]


curriculum = {
    "class": "7",
    "board": "CBSE",
    "subject": "Mathematics",
    "source_pdf": "ncert-books-for-class-7-maths.pdf",
    "chapters": chapters,
}

OUT.write_text(json.dumps(curriculum, indent=2, ensure_ascii=False), encoding="utf-8")
print(OUT)
print(f"chapters={len(chapters)}")
print(f"modules={sum(len(chapter['modules']) for chapter in chapters)}")
print(f"questions={sum(len(module['questions']) for chapter in chapters for module in chapter['modules'])}")
