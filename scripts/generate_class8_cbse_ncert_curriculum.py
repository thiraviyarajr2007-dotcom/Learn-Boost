import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "class8_cbse_ncert_duolingo_curriculum.json"


def q(qid, text, options, answer, rationale, seconds):
    return {
        "question_id": qid,
        "question_text": text,
        "options": options,
        "correct_answer": answer,
        "rationale": rationale,
        "timer_per_question_seconds": seconds,
    }


def m(mid, topic, explanation, difficulty, minutes, items):
    seconds = {"Easy": 30, "Medium": 45, "Hard": 60}[difficulty]
    return {
        "module_id": mid,
        "topic_name": topic,
        "explanation": explanation,
        "difficulty": difficulty,
        "total_timer_minutes": minutes,
        "questions": [q(i + 1, *item, seconds) for i, item in enumerate(items)],
    }


chapters = [
    {
        "chapter_name": "Rational Numbers",
        "modules": [
            m(1, "Properties of Rational Numbers",
              "Rational numbers are numbers that can be written as p/q, where q is not zero. They behave like a well-organised number family. Addition and multiplication are closed, commutative and associative for rational numbers. Zero is the additive identity and one is the multiplicative identity. Every rational number has a negative, and every non-zero rational number has a reciprocal.",
              "Hard", 10, [
                  ("Which number is rational?", ["3/5", "sqrt(2)", "pi only", "1/0"], "3/5", "3/5 is in the form p/q with q not zero."),
                  ("The additive identity for rational numbers is", ["0", "1", "-1", "10"], "0", "Adding zero does not change a rational number."),
                  ("The multiplicative identity is", ["0", "1", "-1", "100"], "1", "Multiplying by one leaves the number unchanged."),
                  ("The reciprocal of 2/3 is", ["2/3", "3/2", "-2/3", "5/3"], "3/2", "The reciprocal interchanges numerator and denominator."),
                  ("Which property is shown by a x (b + c) = a x b + a x c?", ["Closure", "Commutativity", "Distributivity", "Identity"], "Distributivity", "Multiplication is distributed over addition."),
              ]),
            m(2, "Number Line and Rational Numbers Between Two Numbers",
              "Rational numbers can be placed on a number line. Positive numbers lie to the right of zero and negative numbers to the left. Between any two rational numbers, there are many more rational numbers. This is different from whole numbers, where there may be no whole number between two neighbours like 4 and 5.",
              "Medium", 8, [
                  ("On the number line, -3/4 lies", ["right of zero", "left of zero", "at zero", "above one"], "left of zero", "Negative rational numbers lie to the left of zero."),
                  ("Which is greater: -1/2 or 1/4?", ["-1/2", "1/4", "Both equal", "Cannot compare"], "1/4", "A positive rational number is greater than a negative one."),
                  ("Between two rational numbers, there are", ["no rational numbers", "only one rational number", "many rational numbers", "only integers"], "many rational numbers", "Rational numbers are dense on the number line."),
                  ("A rational number between 1/2 and 1 is", ["1/4", "3/4", "2", "-1"], "3/4", "3/4 lies between 1/2 and 1."),
                  ("Which is smaller: -5/6 or -1/6?", ["-5/6", "-1/6", "Both equal", "0"], "-5/6", "The farther-left negative number is smaller."),
              ]),
        ],
    },
    {
        "chapter_name": "Linear Equations in One Variable",
        "modules": [
            m(1, "Solving Linear Equations",
              "A linear equation in one variable has only one unknown, usually with power one. It is like a balance: whatever we do to one side, we must do to the other. We solve by simplifying expressions, collecting variable terms, and isolating the variable. Equations may have variables on one side or both sides.",
              "Hard", 10, [
                  ("Solve x + 5 = 12.", ["5", "7", "12", "17"], "7", "Subtract 5 from both sides."),
                  ("Solve 3x = 21.", ["3", "7", "18", "24"], "7", "Divide both sides by 3."),
                  ("Solve 2x + 3 = 11.", ["3", "4", "7", "8"], "4", "2x = 8, so x = 4."),
                  ("Solve 5x - 2 = 3x + 6.", ["2", "3", "4", "8"], "4", "Move terms to get 2x = 8."),
                  ("A linear equation in one variable has variable power", ["0", "1", "2", "3"], "1", "Linear equations use first power of the variable."),
              ]),
            m(2, "Applications and Reducible Equations",
              "Word problems become easier when we translate them into equations. First choose a variable for the unknown, then write the relationship given in the problem. Some equations contain brackets or fractions and must be reduced to simpler linear form before solving. This method turns everyday puzzles into clear mathematical steps.",
              "Hard", 10, [
                  ("Twice a number is 18. The equation is", ["x + 2 = 18", "2x = 18", "x/2 = 18", "18x = 2"], "2x = 18", "Twice means multiplied by 2."),
                  ("If x/3 = 5, then x is", ["3", "5", "8", "15"], "15", "Multiply both sides by 3."),
                  ("In 3(x + 2) = 15, first expand to get", ["3x + 2 = 15", "3x + 6 = 15", "x + 6 = 15", "3x + 5 = 15"], "3x + 6 = 15", "Multiply 3 by both terms inside brackets."),
                  ("If a number increased by 9 is 20, the number is", ["9", "11", "20", "29"], "11", "x + 9 = 20, so x = 11."),
                  ("To solve equations, equality is kept by doing", ["same operation on both sides", "operation on left only", "operation on right only", "only multiplication"], "same operation on both sides", "An equation works like a balance."),
              ]),
        ],
    },
    {
        "chapter_name": "Understanding Quadrilaterals",
        "modules": [
            m(1, "Polygons and Angle Sum",
              "A polygon is a closed figure made of line segments. Polygons can be classified by number of sides and by shape, such as convex or concave, regular or irregular. Diagonals join non-adjacent vertices. The angle sum of a polygon depends on its number of sides, and the exterior angles of any polygon add up to 360 degrees.",
              "Hard", 10, [
                  ("A polygon is made of", ["curves", "line segments", "circles", "arcs only"], "line segments", "A polygon is a closed figure made of line segments."),
                  ("A diagonal joins", ["adjacent vertices", "non-adjacent vertices", "midpoints only", "curved sides"], "non-adjacent vertices", "Diagonals connect vertices that are not next to each other."),
                  ("Sum of exterior angles of a polygon is", ["90 degrees", "180 degrees", "270 degrees", "360 degrees"], "360 degrees", "The exterior angle sum is always 360 degrees."),
                  ("A regular polygon has", ["equal sides and equal angles", "only equal sides", "only one side", "no angles"], "equal sides and equal angles", "Regular means all sides and angles are equal."),
                  ("A quadrilateral has", ["3 sides", "4 sides", "5 sides", "6 sides"], "4 sides", "Quad means four."),
              ]),
            m(2, "Parallelograms and Special Quadrilaterals",
              "Quadrilaterals include trapeziums, kites, parallelograms, rhombuses, rectangles and squares. In a parallelogram, opposite sides are parallel and equal, opposite angles are equal, and diagonals bisect each other. A rectangle has right angles, a rhombus has equal sides, and a square combines both features.",
              "Hard", 10, [
                  ("In a parallelogram, opposite sides are", ["equal and parallel", "curved", "always unequal", "perpendicular only"], "equal and parallel", "This is a key property of parallelograms."),
                  ("Diagonals of a parallelogram", ["bisect each other", "are always equal only", "never meet", "are sides"], "bisect each other", "Each diagonal cuts the other into two equal parts."),
                  ("A rectangle has all angles equal to", ["45 degrees", "60 degrees", "90 degrees", "180 degrees"], "90 degrees", "A rectangle has four right angles."),
                  ("A rhombus has", ["all sides equal", "no equal sides", "only one right angle", "three sides"], "all sides equal", "A rhombus is a parallelogram with equal sides."),
                  ("A square is both a", ["rectangle and rhombus", "triangle and circle", "kite only", "trapezium only"], "rectangle and rhombus", "It has right angles and all sides equal."),
              ]),
        ],
    },
    {
        "chapter_name": "Practical Geometry",
        "modules": [
            m(1, "Constructing Quadrilaterals",
              "Practical geometry uses ruler, compass and protractor to construct exact figures. A quadrilateral can be constructed when enough measurements are known, such as four sides and a diagonal, three sides and two diagonals, two adjacent sides and three angles, or three sides and two included angles. Construction is like following a precise drawing recipe.",
              "Hard", 10, [
                  ("A quadrilateral can be constructed if four sides and one ___ are given.", ["radius", "diagonal", "median", "height only"], "diagonal", "Four sides and a diagonal give enough structure in the textbook construction."),
                  ("Which tools are commonly used in practical geometry?", ["Ruler, compass and protractor", "Only calculator", "Only graph paper", "Only tally marks"], "Ruler, compass and protractor", "These tools support accurate construction."),
                  ("A diagonal of a quadrilateral joins", ["opposite/non-adjacent vertices", "midpoints only", "curved sides", "same vertex"], "opposite/non-adjacent vertices", "A diagonal joins non-adjacent vertices."),
                  ("Construction should be done using", ["random guesses", "given measurements", "only colour", "only estimation"], "given measurements", "Accurate construction depends on the provided data."),
                  ("A special case of quadrilateral construction includes", ["square or rhombus", "bar graph", "pie chart", "cube root"], "square or rhombus", "The chapter includes special quadrilateral cases."),
              ]),
        ],
    },
    {
        "chapter_name": "Data Handling",
        "modules": [
            m(1, "Grouped Data, Bar Graphs and Pie Charts",
              "Data handling helps us collect, organise and understand information. Large data can be grouped into classes to make patterns easier to see. Bar graphs compare categories, while histograms show grouped numerical data. A pie chart represents a whole as a circle divided into sectors, where each sector shows a part of the total.",
              "Medium", 9, [
                  ("Grouped data is useful when data is", ["very small only", "large", "always zero", "not numerical"], "large", "Grouping makes large data easier to read."),
                  ("A pie chart represents data using", ["a circle", "a ruler", "a line segment only", "a compass box"], "a circle", "A pie chart divides a circle into sectors."),
                  ("A histogram is useful for", ["grouped data", "only angles", "only equations", "only factors"], "grouped data", "Histograms show frequency for class intervals."),
                  ("In a pie chart, the whole circle represents", ["half the data", "total data", "one category only", "zero"], "total data", "The full circle stands for the complete data set."),
                  ("A bar graph compares", ["categories", "only fractions", "only roots", "only identities"], "categories", "Bars make category comparison clear."),
              ]),
            m(2, "Chance and Probability",
              "Probability measures chance. Some outcomes are certain, some impossible, and some equally likely. When outcomes are equally likely, probability of an event is the number of favourable outcomes divided by the total number of outcomes. Tossing a coin, rolling a die and drawing a card are simple probability situations.",
              "Medium", 8, [
                  ("The probability of a certain event is", ["0", "1", "2", "10"], "1", "A certain event always happens."),
                  ("The probability of an impossible event is", ["0", "1", "1/2", "2"], "0", "An impossible event cannot happen."),
                  ("A coin has how many equally likely outcomes?", ["1", "2", "3", "6"], "2", "Head and tail are the two outcomes."),
                  ("On a die, probability of getting 3 is", ["1/2", "1/3", "1/6", "3/6"], "1/6", "There is one favourable outcome out of six."),
                  ("Probability is linked to", ["chance", "only area", "only perimeter", "only construction"], "chance", "Probability measures likelihood."),
              ]),
        ],
    },
    {
        "chapter_name": "Squares and Square Roots",
        "modules": [
            m(1, "Square Numbers and Patterns",
              "A square number is made by multiplying a number by itself, like 5 x 5 = 25. Square numbers form patterns: 1, 4, 9, 16 and so on. The chapter also connects square numbers with Pythagorean triplets, where three numbers can form the sides of a right triangle. Patterns make squares easier to recognise.",
              "Medium", 8, [
                  ("6 squared equals", ["12", "18", "36", "64"], "36", "6 x 6 = 36."),
                  ("Which is a perfect square?", ["20", "25", "30", "35"], "25", "25 = 5 x 5."),
                  ("The square of an even number is", ["always odd", "always even", "always prime", "always zero"], "always even", "Even times even gives even."),
                  ("A Pythagorean triplet is related to", ["right triangles", "pie charts", "discounts", "bar graphs"], "right triangles", "Triplets satisfy the Pythagoras relation."),
                  ("1, 4, 9, 16 are examples of", ["cube numbers", "square numbers", "prime numbers only", "linear equations"], "square numbers", "They are n x n values."),
              ]),
            m(2, "Finding Square Roots",
              "A square root reverses squaring. If 9 is 3 squared, then the square root of 9 is 3. Square roots can be found by repeated subtraction, prime factorisation, division method, and estimation. Decimal square roots also follow place value carefully. Square roots help in measurement and geometry.",
              "Hard", 10, [
                  ("Square root of 49 is", ["6", "7", "8", "9"], "7", "7 x 7 = 49."),
                  ("Square root is the reverse of", ["addition", "subtraction", "squaring", "division only"], "squaring", "It finds the number multiplied by itself."),
                  ("Prime factorisation of 36 is", ["2 x 2 x 3 x 3", "6 x 6 only", "4 x 9 only", "1 x 36 only"], "2 x 2 x 3 x 3", "Prime factors are grouped in pairs for square root."),
                  ("The square root of 0.25 is", ["0.05", "0.5", "5", "25"], "0.5", "0.5 x 0.5 = 0.25."),
                  ("The square root of 100 lies exactly at", ["5", "10", "20", "50"], "10", "10 x 10 = 100."),
              ]),
        ],
    },
    {
        "chapter_name": "Cubes and Cube Roots",
        "modules": [
            m(1, "Cubes and Cube Roots",
              "A cube number is made by multiplying a number by itself three times, such as 4 x 4 x 4 = 64. A cube root reverses this process. In prime factorisation, a perfect cube has prime factors grouped in triples. Cubes help students understand volume and number patterns.",
              "Medium", 9, [
                  ("3 cubed equals", ["6", "9", "27", "81"], "27", "3 x 3 x 3 = 27."),
                  ("Which is a perfect cube?", ["16", "25", "27", "50"], "27", "27 = 3 x 3 x 3."),
                  ("Cube root of 64 is", ["2", "4", "8", "16"], "4", "4 x 4 x 4 = 64."),
                  ("In prime factorisation, perfect cubes form groups of", ["2", "3", "4", "5"], "3", "Cube roots use triples of equal prime factors."),
                  ("The smallest perfect cube is", ["0", "1", "2", "3"], "1", "1 x 1 x 1 = 1."),
              ]),
        ],
    },
    {
        "chapter_name": "Comparing Quantities",
        "modules": [
            m(1, "Percentages, Discount, Profit and Loss",
              "Percent means out of 100. It helps compare increases, decreases, discounts, profit and loss. Discount reduces marked price. Profit happens when selling price is more than cost price, and loss happens when selling price is less. Percentages make shopping, marks and business calculations easier to compare.",
              "Hard", 10, [
                  ("20% of 200 is", ["20", "40", "100", "400"], "40", "20/100 x 200 = 40."),
                  ("Discount is calculated on", ["marked price", "selling price only", "profit only", "loss only"], "marked price", "Discount reduces the marked price."),
                  ("If CP = Rs 100 and SP = Rs 120, profit is", ["Rs 10", "Rs 20", "Rs 100", "Rs 220"], "Rs 20", "Profit = SP - CP."),
                  ("If SP is less than CP, there is", ["profit", "loss", "discount only", "tax only"], "loss", "Loss occurs when selling price is lower than cost price."),
                  ("A 10% decrease on 500 is", ["5", "10", "50", "100"], "50", "10/100 x 500 = 50."),
              ]),
            m(2, "Sales Tax, GST and Compound Interest",
              "Taxes such as sales tax, VAT or GST are added to the price of an item. Compound interest is interest calculated on the amount from the previous period, not just the original principal. This means money grows faster than in simple interest. The formula helps calculate repeated yearly or half-yearly growth.",
              "Hard", 10, [
                  ("GST is usually added to the", ["price of an item", "angle of a triangle", "area only", "cube root"], "price of an item", "GST is a tax on goods and services."),
                  ("In compound interest, interest is calculated on", ["only original principal forever", "updated amount", "zero", "discount"], "updated amount", "Each period uses the new amount."),
                  ("Amount means", ["principal + interest", "principal - interest", "rate only", "time only"], "principal + interest", "Amount is total money after interest."),
                  ("If interest is compounded annually, it is added", ["every month", "every year", "every day only", "never"], "every year", "Annually means once per year."),
                  ("Compound interest is generally greater than simple interest for same rate and time because", ["interest earns interest", "principal becomes zero", "rate disappears", "time is ignored"], "interest earns interest", "Interest is added to amount and then earns more interest."),
              ]),
        ],
    },
    {
        "chapter_name": "Algebraic Expressions and Identities",
        "modules": [
            m(1, "Terms, Like Terms and Operations",
              "Algebraic expressions are made from variables, constants and operations. Terms are separated by plus or minus signs. Like terms have the same variables with the same powers, so they can be added or subtracted. Multiplication can involve monomials, binomials and polynomials. Careful grouping keeps algebra neat.",
              "Hard", 10, [
                  ("In 5x, the coefficient of x is", ["x", "5", "0", "1"], "5", "The numerical factor is the coefficient."),
                  ("Which are like terms?", ["3x and 7x", "3x and 7y", "x and x^2", "2a and 2b"], "3x and 7x", "They have the same variable with same power."),
                  ("A monomial has", ["one term", "two terms", "three terms", "many equations"], "one term", "Mono means one."),
                  ("A binomial has", ["one term", "two terms", "three terms", "zero terms"], "two terms", "Bi means two."),
                  ("Simplify 4x + 3x.", ["7x", "12x", "7x^2", "x"], "7x", "Add coefficients of like terms."),
              ]),
            m(2, "Standard Identities",
              "An identity is an equation true for all allowed values of its variables. Standard identities such as (a + b)^2, (a - b)^2 and (a + b)(a - b) make algebraic multiplication faster. They are like reliable shortcuts, but they must be applied carefully with the right terms.",
              "Hard", 10, [
                  ("(a + b)^2 equals", ["a^2 + b^2", "a^2 + 2ab + b^2", "a^2 - b^2", "2a + 2b"], "a^2 + 2ab + b^2", "This is the standard square identity."),
                  ("(a - b)^2 equals", ["a^2 - 2ab + b^2", "a^2 + 2ab + b^2", "a^2 - b^2", "a - b^2"], "a^2 - 2ab + b^2", "The middle term is negative."),
                  ("(a + b)(a - b) equals", ["a^2 + b^2", "a^2 - b^2", "a^2 + 2ab + b^2", "b^2 - a^2"], "a^2 - b^2", "This is the difference of squares identity."),
                  ("An identity is true for", ["only one value", "all values of variables", "no value", "only zero"], "all values of variables", "Identities hold generally."),
                  ("Using identities can make multiplication", ["slower always", "faster and systematic", "impossible", "unrelated"], "faster and systematic", "Identities are algebraic shortcuts."),
              ]),
        ],
    },
    {
        "chapter_name": "Visualising Solid Shapes",
        "modules": [
            m(1, "Views, Maps, Faces, Edges and Vertices",
              "Solid shapes are three-dimensional, but we often draw or view them on flat surfaces. A 3-D object can have different front, side and top views. Maps represent space using symbols and directions. Solids also have faces, edges and vertices. Euler's relation connects these parts for many polyhedra.",
              "Medium", 8, [
                  ("A cube is a", ["2-D shape", "3-D shape", "line", "ray"], "3-D shape", "A cube has length, breadth and height."),
                  ("Top view means looking", ["from above", "from below only", "from inside", "from a calculator"], "from above", "Top view is seen from above."),
                  ("A face of a solid is", ["a flat surface", "a corner", "a ratio", "a tax"], "a flat surface", "Faces are surfaces of solids."),
                  ("An edge is where", ["two faces meet", "two taxes meet", "two roots meet", "two variables disappear"], "two faces meet", "Edges are line segments of solids."),
                  ("A vertex is a", ["corner", "surface", "graph scale", "discount"], "corner", "Vertices are corner points."),
              ]),
        ],
    },
    {
        "chapter_name": "Mensuration",
        "modules": [
            m(1, "Area of Trapezium, Quadrilaterals and Polygons",
              "Mensuration measures area, surface area and volume. A trapezium has one pair of parallel sides, and its area uses the sum of parallel sides and height. General quadrilaterals and polygons can be split into triangles and familiar shapes. Breaking complex figures into simpler parts makes area calculation manageable.",
              "Hard", 10, [
                  ("Area of a trapezium is", ["1/2 x sum of parallel sides x height", "length x breadth", "side x side", "2 pi r"], "1/2 x sum of parallel sides x height", "This is the trapezium area formula."),
                  ("A trapezium has", ["one pair of parallel sides", "no sides", "all sides curved", "three sides"], "one pair of parallel sides", "This is the defining feature used in the chapter."),
                  ("Complex polygons can be split into", ["simpler shapes", "taxes", "roots only", "commas"], "simpler shapes", "Area is easier after decomposition."),
                  ("Area is measured in", ["square units", "linear units", "cubic units", "degrees"], "square units", "Area covers surface."),
                  ("Height used in area formulas is usually", ["perpendicular distance", "slant side always", "largest number", "tax rate"], "perpendicular distance", "Area formulas use perpendicular height."),
              ]),
            m(2, "Surface Area and Volume of Solids",
              "Surface area measures the total outer covering of a solid, like wrapping paper around a box. Volume measures the space inside a solid, like water a container can hold. Cubes, cuboids and cylinders have formulas for surface area and volume. Capacity is closely related to volume and is often measured in litres.",
              "Hard", 10, [
                  ("Volume of a cuboid is", ["l x b x h", "2(l + b)", "side x side", "pi r^2"], "l x b x h", "Volume uses length, breadth and height."),
                  ("Volume is measured in", ["square units", "cubic units", "degrees", "percent"], "cubic units", "Volume measures space inside a solid."),
                  ("Surface area measures", ["outer covering", "only height", "only tax", "only probability"], "outer covering", "Surface area is total area of faces."),
                  ("A cylinder has circular", ["bases", "diagonals", "taxes", "variables"], "bases", "A cylinder has two circular bases."),
                  ("Capacity is commonly measured in", ["litres", "degrees", "square cm", "percent only"], "litres", "Capacity describes how much a container can hold."),
              ]),
        ],
    },
    {
        "chapter_name": "Exponents and Powers",
        "modules": [
            m(1, "Negative Exponents and Standard Form",
              "Exponents are shortcuts for repeated multiplication. Class 8 extends this idea to negative exponents: a negative exponent shows a reciprocal power. Powers of 10 help write very large and very small numbers in standard form. This is useful in science, measurements and comparing quantities of very different sizes.",
              "Medium", 8, [
                  ("10^-2 equals", ["100", "10", "1/10", "1/100"], "1/100", "A negative exponent gives reciprocal power."),
                  ("2^-1 equals", ["2", "1/2", "-2", "0"], "1/2", "a^-1 = 1/a for non-zero a."),
                  ("0.000007 in standard form is", ["7 x 10^-6", "7 x 10^6", "0.7 x 10^-5", "70 x 10^-7"], "7 x 10^-6", "Move decimal six places to make 7."),
                  ("Standard form is useful for", ["very large and very small numbers", "only polygons", "only bar graphs", "only taxes"], "very large and very small numbers", "It expresses numbers compactly."),
                  ("10^3 equals", ["30", "100", "1000", "10000"], "1000", "10 x 10 x 10 = 1000."),
              ]),
        ],
    },
    {
        "chapter_name": "Direct and Inverse Proportions",
        "modules": [
            m(1, "Direct Proportion",
              "Two quantities are in direct proportion when they increase or decrease together in the same ratio. If more notebooks cost more money at a fixed price, cost and number of notebooks are directly proportional. The ratio between corresponding values remains constant, making unitary method and tables useful.",
              "Medium", 8, [
                  ("In direct proportion, quantities", ["increase together in same ratio", "always move opposite", "never change", "are always zero"], "increase together in same ratio", "Direct proportion keeps the same ratio."),
                  ("If 1 pen costs Rs 5, 4 pens cost", ["Rs 5", "Rs 9", "Rs 20", "Rs 45"], "Rs 20", "Cost increases directly with number of pens."),
                  ("Direct proportion has a constant", ["sum", "ratio", "difference only", "angle"], "ratio", "Corresponding ratios are equal."),
                  ("More distance at same speed needs", ["more time", "less time always", "zero time", "same time always"], "more time", "Distance and time are direct at constant speed."),
                  ("Which pair is usually direct?", ["Number of items and total cost at fixed price", "Workers and time for same work", "Speed and time for same distance", "Discount and marked price always"], "Number of items and total cost at fixed price", "More items cost more at a fixed rate."),
              ]),
            m(2, "Inverse Proportion",
              "Two quantities are in inverse proportion when one increases as the other decreases, while the product remains constant. For the same work, more workers take less time. For the same distance, higher speed takes less time. Inverse proportion helps solve practical problems involving work, speed, time and sharing.",
              "Hard", 10, [
                  ("In inverse proportion, if one quantity increases, the other", ["also increases", "decreases", "becomes equal", "becomes zero always"], "decreases", "They move in opposite directions."),
                  ("For the same work, more workers need", ["more time", "less time", "same time always", "no time"], "less time", "Work is shared among more workers."),
                  ("In inverse proportion, the product is", ["constant", "always zero", "always increasing", "always decreasing"], "constant", "Corresponding products remain equal."),
                  ("For the same distance, higher speed means", ["less time", "more time", "same time always", "zero distance"], "less time", "Speed and time are inverse for fixed distance."),
                  ("Which pair is usually inverse?", ["Workers and time for same work", "Items and cost at fixed price", "Age and height always", "Radius and diameter"], "Workers and time for same work", "More workers reduce time for same work."),
              ]),
        ],
    },
    {
        "chapter_name": "Factorisation",
        "modules": [
            m(1, "Factorisation Methods",
              "Factorisation means writing an expression as a product of its factors. Just as 12 can be written as 3 x 4, algebraic expressions can also be broken into factors. Common factors, regrouping, identities and forms like (x + a)(x + b) help factorise expressions. Factorisation is the reverse of multiplication.",
              "Hard", 10, [
                  ("Factorisation is the reverse of", ["addition", "multiplication", "subtraction only", "division only"], "multiplication", "Multiplication expands; factorisation breaks into factors."),
                  ("Common factor of 6x and 9x is", ["3x", "6x", "9", "54x"], "3x", "3x divides both terms."),
                  ("x^2 - y^2 factorises as", ["(x + y)(x - y)", "(x + y)^2", "(x - y)^2", "x(x - y)"], "(x + y)(x - y)", "This uses the difference of squares identity."),
                  ("In factorisation by regrouping, we", ["group suitable terms", "draw pie charts", "find cube roots", "use tax rate"], "group suitable terms", "Regrouping reveals common factors."),
                  ("Factors of algebraic expressions multiply to give the", ["original expression", "probability", "graph only", "angle"], "original expression", "Factors are product parts."),
              ]),
            m(2, "Division of Algebraic Expressions",
              "Division of algebraic expressions uses factors. A monomial can be divided by another monomial by dividing coefficients and subtracting powers of like variables. A polynomial divided by a monomial is handled term by term. Factorisation makes division simpler and also helps detect common errors.",
              "Hard", 10, [
                  ("6x divided by 3x equals", ["2", "3", "2x", "18x"], "2", "Coefficients divide and x cancels."),
                  ("x^5 divided by x^2 equals", ["x^3", "x^7", "x^10", "x"], "x^3", "Subtract exponents for same base."),
                  ("(6x + 9) divided by 3 is", ["2x + 3", "6x + 3", "2x + 9", "18x + 27"], "2x + 3", "Divide each term by 3."),
                  ("Polynomial divided by monomial is divided", ["term by term", "only first term", "only last term", "never"], "term by term", "Each term is divided by the monomial."),
                  ("Factorisation helps division by showing", ["common factors", "pie sectors", "random digits", "views of solids"], "common factors", "Common factors can be cancelled."),
              ]),
        ],
    },
    {
        "chapter_name": "Introduction to Graphs",
        "modules": [
            m(1, "Types of Graphs and Coordinates",
              "Graphs show information visually. Bar graphs compare categories, pie graphs show parts of a whole, histograms show grouped data, and line graphs show change. Coordinates locate a point on a plane using an ordered pair (x, y). The x-coordinate tells horizontal movement and the y-coordinate tells vertical movement.",
              "Medium", 9, [
                  ("A line graph is useful to show", ["change over time", "only factors", "only solid faces", "only roots"], "change over time", "Line graphs show trends."),
                  ("A point is located using", ["coordinates", "tax", "discount", "surface area only"], "coordinates", "Coordinates identify position."),
                  ("In (3, 5), the x-coordinate is", ["3", "5", "8", "2"], "3", "The first number is the x-coordinate."),
                  ("In (3, 5), the y-coordinate is", ["3", "5", "8", "2"], "5", "The second number is the y-coordinate."),
                  ("A pie graph is also called a", ["circle graph", "line segment", "cube graph", "factor tree"], "circle graph", "Pie graphs divide a circle into sectors."),
              ]),
            m(2, "Linear Graphs and Applications",
              "A linear graph is a straight-line graph. It can show relationships such as cost versus number of items or distance versus time at a constant speed. To draw a graph, make a table of values, plot points using coordinates, and join them appropriately. Graphs turn number patterns into visible relationships.",
              "Medium", 8, [
                  ("A linear graph is usually a", ["straight line", "circle", "cube", "random curve only"], "straight line", "Linear relationships form straight-line graphs."),
                  ("To draw a graph, we first often make a", ["table of values", "tax receipt", "solid net", "factor only"], "table of values", "Tables give points to plot."),
                  ("The horizontal axis is commonly called the", ["x-axis", "y-axis", "z-axis only", "radius"], "x-axis", "The x-axis runs horizontally."),
                  ("The vertical axis is commonly called the", ["x-axis", "y-axis", "diameter", "base"], "y-axis", "The y-axis runs vertically."),
                  ("A graph of distance-time at constant speed is", ["linear", "always circular", "impossible", "a pie chart"], "linear", "Constant speed gives a straight-line relationship."),
              ]),
        ],
    },
    {
        "chapter_name": "Playing with Numbers",
        "modules": [
            m(1, "Numbers in General Form and Digit Games",
              "Numbers can be written in general form using place value. A two-digit number with tens digit a and ones digit b is 10a + b. This helps explain digit games and patterns logically. Letters can stand for digits, but each letter must represent a valid digit and follow place-value rules.",
              "Hard", 10, [
                  ("A two-digit number with tens digit a and ones digit b is", ["a + b", "10a + b", "ab only", "10b + a"], "10a + b", "The tens digit has value 10a."),
                  ("If a = 3 and b = 5, 10a + b equals", ["8", "35", "53", "350"], "35", "10 x 3 + 5 = 35."),
                  ("Reversing digits of 10a + b gives", ["10a + b", "10b + a", "a - b", "ab + 10"], "10b + a", "The ones digit becomes tens digit."),
                  ("Letters for digits must represent", ["digits", "angles", "graphs", "taxes"], "digits", "Each letter stands for a digit in such puzzles."),
                  ("Place value is important because digit position changes", ["value", "colour only", "shape only", "probability only"], "value", "A digit's value depends on its place."),
              ]),
            m(2, "Divisibility Tests",
              "Divisibility tests are quick rules for checking whether one number divides another exactly. A number ending in 0 is divisible by 10. A number ending in 0 or 5 is divisible by 5. A number ending in an even digit is divisible by 2. For 3 and 9, we use the sum of digits.",
              "Medium", 8, [
                  ("A number divisible by 10 ends in", ["0", "5", "2", "9"], "0", "The divisibility test for 10 checks the ones digit."),
                  ("A number divisible by 5 ends in", ["0 or 5", "2 or 4", "3 or 9", "1 only"], "0 or 5", "This is the divisibility rule for 5."),
                  ("A number divisible by 2 has ones digit", ["odd", "even", "5", "9"], "even", "Even endings are divisible by 2."),
                  ("For divisibility by 9, check the", ["sum of digits", "first digit only", "last two digits only", "number of zeros"], "sum of digits", "If digit sum is divisible by 9, the number is divisible by 9."),
                  ("For divisibility by 3, digit sum should be divisible by", ["2", "3", "5", "10"], "3", "The rule for 3 uses digit sum."),
              ]),
        ],
    },
]


curriculum = {
    "class": "8",
    "board": "CBSE",
    "subject": "Mathematics",
    "source_pdf": "ncert-books-for-class-8-maths.pdf",
    "chapters": chapters,
}


OUT.write_text(json.dumps(curriculum, indent=2), encoding="utf-8")
print(OUT)
print(f"chapters={len(chapters)}")
print(f"modules={sum(len(chapter['modules']) for chapter in chapters)}")
print(f"questions={sum(len(module['questions']) for chapter in chapters for module in chapter['modules'])}")
