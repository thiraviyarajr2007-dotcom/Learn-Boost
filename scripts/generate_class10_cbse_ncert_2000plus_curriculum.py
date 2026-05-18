import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "class10_cbse_ncert_duolingo_curriculum_2000plus.json"


CHAPTERS = [
    ("Real Numbers", ["Euclid Division Lemma", "Euclid Division Algorithm", "Fundamental Theorem of Arithmetic", "Prime Factorisation", "HCF and LCM", "Irrational Numbers", "Decimal Expansions", "Terminating Decimals", "Non-terminating Recurring Decimals", "Number Theory Applications"]),
    ("Polynomials", ["Polynomial Basics", "Zeroes of a Polynomial", "Graph of a Polynomial", "Quadratic Polynomial Zeroes", "Relationship of Zeroes and Coefficients", "Finding Polynomial from Zeroes", "Division Algorithm", "Remainder Thinking", "Factorisation of Polynomials", "Polynomial Applications"]),
    ("Pair of Linear Equations in Two Variables", ["Linear Pair Basics", "Graphical Method", "Consistent Systems", "Inconsistent Systems", "Substitution Method", "Elimination Method", "Cross Multiplication Method", "Reducible Linear Equations", "Word Problems", "Equation Modelling"]),
    ("Quadratic Equations", ["Quadratic Equation Form", "Roots of a Quadratic", "Factorisation Method", "Completing the Square", "Quadratic Formula", "Discriminant", "Nature of Roots", "Word Problems", "Number Problems", "Geometry Problems"]),
    ("Arithmetic Progressions", ["AP Basics", "Common Difference", "nth Term", "Finding Terms", "Sum of First n Terms", "AP Word Problems", "Middle Term", "Finite AP", "Pattern Recognition", "AP Applications"]),
    ("Triangles", ["Similarity Basics", "Similar Figures", "Basic Proportionality Theorem", "Converse of BPT", "Criteria for Similarity", "Areas of Similar Triangles", "Pythagoras Theorem", "Converse of Pythagoras", "Triangle Applications", "Proof Practice"]),
    ("Coordinate Geometry", ["Distance Formula", "Distance Between Points", "Section Formula", "Midpoint Formula", "Internal Division", "Collinearity", "Area of Triangle", "Coordinate Applications", "Quadrilateral Problems", "Graph Interpretation"]),
    ("Introduction to Trigonometry", ["Trigonometric Ratios", "Sine and Cosine", "Tangent", "Ratios of Special Angles", "Complementary Angles", "Trigonometric Identities", "Using sin2 plus cos2", "Simplifying Expressions", "Right Triangle Problems", "Trigonometry Applications"]),
    ("Some Applications of Trigonometry", ["Heights and Distances", "Angle of Elevation", "Angle of Depression", "Line of Sight", "Single Observation Problems", "Two Observation Problems", "Shadow Problems", "Tower Problems", "Observer Movement Problems", "Real-life Modelling"]),
    ("Circles", ["Tangent to a Circle", "Secant and Tangent", "Tangent at a Point", "Radius Perpendicular to Tangent", "Lengths of Tangents", "Two Tangents from a Point", "Circle Theorems", "Tangent Construction Ideas", "Proof Problems", "Applications of Tangents"]),
    ("Areas Related to Circles", ["Circumference and Area", "Sector of a Circle", "Segment of a Circle", "Length of Arc", "Area of Sector", "Area of Segment", "Combination of Figures", "Shaded Regions", "Perimeter of Circular Figures", "Circle Area Applications"]),
    ("Surface Areas and Volumes", ["Surface Area of Cuboid and Cube", "Surface Area of Cylinder", "Surface Area of Cone", "Surface Area of Sphere", "Volume of Cuboid", "Volume of Cylinder", "Volume of Cone", "Volume of Sphere", "Combination of Solids", "Conversion of Solids"]),
    ("Statistics", ["Grouped Data", "Class Marks", "Mean by Direct Method", "Mean by Assumed Mean Method", "Mean by Step Deviation", "Mode of Grouped Data", "Median of Grouped Data", "Cumulative Frequency", "Ogive", "Interpreting Central Tendency"]),
    ("Probability", ["Classical Probability", "Outcomes and Events", "Equally Likely Outcomes", "Coin Problems", "Dice Problems", "Card Problems", "Complementary Events", "Impossible and Certain Events", "Simple Probability Applications", "Probability Reasoning"]),
]


EXPLAIN = {
    "Real Numbers": "Real numbers include rational and irrational numbers. This chapter uses Euclid's division lemma, prime factorisation, HCF, LCM and decimal expansions to understand number structure. Think of every number as having an ID card: prime factors, divisibility and decimal form help us recognise it clearly.",
    "Polynomials": "Polynomials are algebraic expressions built from variables and powers. Class 10 focuses on zeroes, graphs, relationships between zeroes and coefficients, and the division algorithm. A polynomial is like an input-output machine: when a value makes the output zero, it becomes a zero of the polynomial.",
    "Pair of Linear Equations in Two Variables": "A pair of linear equations represents two straight lines. Their graphs may meet at one point, never meet, or overlap completely. Algebraic methods such as substitution, elimination and cross multiplication help find solutions without drawing every graph.",
    "Quadratic Equations": "A quadratic equation has degree two and can have two, one or no real roots. Students solve them by factorisation, completing the square and the quadratic formula. The discriminant acts like a root detector, telling the nature of roots before solving fully.",
    "Arithmetic Progressions": "An arithmetic progression is a number pattern where each term increases or decreases by the same common difference. Once the first term and common difference are known, any term and the sum of many terms can be found quickly.",
    "Triangles": "This chapter studies similarity, proportionality and right-triangle relationships. Similar triangles have the same shape but possibly different sizes. Theorems like BPT and Pythagoras turn geometric diagrams into logical, solvable relationships.",
    "Coordinate Geometry": "Coordinate geometry links algebra and geometry using points on a plane. Distance formula measures length, section formula finds dividing points, and area formula checks triangle area. Coordinates work like a map grid for solving geometry with numbers.",
    "Introduction to Trigonometry": "Trigonometry connects angles of a right triangle with ratios of sides. Sine, cosine and tangent help find unknown lengths and angles. Special angle values and identities make calculations faster and prepare students for real-life height and distance problems.",
    "Some Applications of Trigonometry": "This chapter applies trigonometry to heights and distances. Angles of elevation and depression describe how we look up or down. With a right triangle model, we can estimate heights of towers, trees and buildings without measuring them directly.",
    "Circles": "A tangent touches a circle at exactly one point. The radius to the point of contact is perpendicular to the tangent, and tangent lengths from an external point are equal. These simple rules unlock many circle proof and application problems.",
    "Areas Related to Circles": "Circular area problems use circumference, area, sectors and segments. A sector is like a slice of pizza, while a segment is the region between a chord and an arc. Many questions combine circles with squares, rectangles and triangles.",
    "Surface Areas and Volumes": "Surface area measures outer covering and volume measures space inside. This chapter works with cubes, cuboids, cylinders, cones, spheres and combinations of solids. The formulas help solve problems about containers, pipes, balls and reshaped solids.",
    "Statistics": "Statistics organises data and finds representative values. For grouped data, mean, median and mode are calculated using class intervals and frequencies. Ogives show cumulative frequency visually, helping locate medians and compare distributions.",
    "Probability": "Probability measures chance. In Class 10, students use favourable outcomes divided by total equally likely outcomes. The value lies between 0 and 1, where 0 means impossible and 1 means certain.",
}


DIFF = {
    "Real Numbers": "Hard", "Polynomials": "Hard", "Pair of Linear Equations in Two Variables": "Hard",
    "Quadratic Equations": "Hard", "Arithmetic Progressions": "Medium", "Triangles": "Hard",
    "Coordinate Geometry": "Medium", "Introduction to Trigonometry": "Hard", "Some Applications of Trigonometry": "Hard",
    "Circles": "Medium", "Areas Related to Circles": "Hard", "Surface Areas and Volumes": "Hard",
    "Statistics": "Medium", "Probability": "Medium",
}


def pack(answer, *wrong):
    return [str(answer), *[str(w) for w in wrong]][:4], str(answer)


def bank(chapter, seed):
    n = seed % 9 + 2
    banks = {
        "Real Numbers": [
            ("Euclid's division lemma says a = bq + r where r is", *pack("0 <= r < b", "r > b", "r = b always", "r < 0"), "The remainder is non-negative and less than the divisor."),
            ("HCF of 18 and 24 is", *pack("6", "3", "12", "72"), "6 is the greatest common factor."),
            ("LCM of 6 and 8 is", *pack("24", "2", "14", "48"), "24 is the smallest common multiple."),
            ("HCF x LCM equals product of numbers for", *pack("two positive integers", "all irrational numbers", "only primes", "decimals only"), "For two positive integers, HCF x LCM = product."),
            ("sqrt(2) is", *pack("irrational", "natural", "whole", "terminating decimal"), "sqrt(2) cannot be expressed as p/q."),
            ("A rational number has decimal expansion that is", *pack("terminating or recurring", "always non-recurring", "never terminating", "always irrational"), "Rational decimals terminate or repeat."),
            ("A terminating decimal occurs when denominator has prime factors only", *pack("2 and/or 5", "3 and 7", "2 and 3", "5 and 7"), "In lowest form, only 2 and 5 allow termination."),
            ("Prime factorisation of 60 is", *pack("2 x 2 x 3 x 5", "2 x 30", "6 x 10", "3 x 20"), "Prime factors must all be prime."),
            ("Every composite number can be expressed as product of", *pack("primes", "irrationals", "decimals only", "zeroes"), "This is the fundamental theorem of arithmetic."),
            ("The HCF of two co-prime numbers is", *pack("1", "0", "their product", "their sum"), "Co-prime numbers have no common factor except 1."),
            ("If p is prime and p divides a^2, then p divides", *pack("a", "2 only", "a+1", "a-1 only"), "This idea is used in irrationality proofs."),
            ("The decimal 0.333... is", *pack("rational", "irrational", "integer", "natural"), "Repeating decimals are rational."),
            ("The product of a non-zero rational and irrational number is usually", *pack("irrational", "always rational", "always zero", "natural"), "A non-zero rational times an irrational is irrational."),
            ("For numbers " + str(n*6) + " and " + str(n*8) + ", HCF is", *pack(str(n*2), str(n), str(n*4), str(n*14)), "The common factor scales with n."),
            ("For numbers " + str(n*3) + " and " + str(n*5) + ", LCM is", *pack(str(n*15), str(n*8), str(n), str(15)), "The numbers are n times co-prime factors 3 and 5."),
        ],
        "Polynomials": [
            ("Degree of 3x^2 + 5x + 7 is", *pack("2", "1", "3", "7"), "The highest power of x is 2."),
            ("A zero of p(x) makes p(x) equal to", *pack("0", "1", "x", "degree"), "Zeroes are input values giving output zero."),
            ("If p(x)=x-5, its zero is", *pack("5", "-5", "0", "1"), "p(5)=0."),
            ("For ax^2+bx+c, sum of zeroes is", *pack("-b/a", "c/a", "b/a", "-c/a"), "The sum of zeroes is -b/a."),
            ("For ax^2+bx+c, product of zeroes is", *pack("c/a", "-b/a", "b/a", "-c/a"), "The product of zeroes is c/a."),
            ("A quadratic polynomial has degree", *pack("2", "1", "3", "0"), "Quadratic means degree 2."),
            ("If zeroes are 2 and 3, a monic quadratic is", *pack("x^2-5x+6", "x^2+5x+6", "x^2-x+6", "x^2-6x+5"), "Sum is 5 and product is 6."),
            ("Division algorithm is dividend =", *pack("divisor x quotient + remainder", "divisor + quotient", "quotient - remainder", "remainder only"), "This is the polynomial division form."),
            ("Remainder degree is less than degree of", *pack("divisor", "dividend", "quotient", "zero"), "The remainder has lower degree than divisor."),
            ("x^2 - 9 factorises as", *pack("(x-3)(x+3)", "(x-9)(x+1)", "(x-3)^2", "x(x-9)"), "It is a difference of squares."),
            ("Graph of a linear polynomial is a", *pack("straight line", "parabola", "circle", "hyperbola"), "Degree 1 polynomial graphs as a line."),
            ("Graph of a quadratic polynomial is a", *pack("parabola", "straight line", "circle", "point only"), "Quadratic graphs are parabolas."),
            ("A polynomial with three terms is a", *pack("trinomial", "monomial", "binomial", "constant"), "Tri means three."),
            ("For p(x)=x^2-" + str(n*n) + ", one zero is", *pack(str(n), str(n+1), "0", str(n*n)), "x=n makes x^2-n^2 equal zero."),
            ("Coefficient of x in 4x^2 - 7x + 1 is", *pack("-7", "4", "1", "2"), "The x-term is -7x."),
        ],
        "Pair of Linear Equations in Two Variables": [
            ("A pair of linear equations may represent", *pack("two lines", "two circles", "two parabolas", "two spheres"), "Linear equations graph as lines."),
            ("If two lines intersect at one point, the pair is", *pack("consistent with unique solution", "inconsistent", "dependent only", "parallel only"), "Intersecting lines have one solution."),
            ("Parallel distinct lines give", *pack("no solution", "one solution", "infinitely many solutions", "two solutions"), "Parallel distinct lines never meet."),
            ("Coincident lines give", *pack("infinitely many solutions", "no solution", "one solution", "zero only"), "Every point on the line satisfies both."),
            ("Substitution method means", *pack("express one variable and substitute", "only add equations", "only graph", "ignore variables"), "One variable is substituted into the other equation."),
            ("Elimination method removes", *pack("one variable", "both variables always", "constant only", "graphs"), "Elimination combines equations to remove a variable."),
            ("The solution of x+y=5 and x-y=1 is", *pack("(3, 2)", "(2, 3)", "(1, 5)", "(5, 1)"), "Adding gives 2x=6, so x=3 and y=2."),
            ("For coincident lines, ratios a1/a2, b1/b2, c1/c2 are", *pack("equal", "all different", "zero", "not comparable"), "Equal ratios indicate dependent equations."),
            ("For parallel lines with no solution, a1/a2 equals b1/b2 but not", *pack("c1/c2", "a1", "b1", "x"), "This condition gives inconsistency."),
            ("Graphical solution is the", *pack("point of intersection", "slope only", "area", "midpoint always"), "The intersection point satisfies both equations."),
            ("A linear equation in two variables has", *pack("infinitely many solutions", "only one solution", "no solution always", "only two solutions"), "A single line has infinitely many points."),
            ("x=3 is a line parallel to", *pack("y-axis", "x-axis", "both axes", "no axis"), "x=constant is vertical."),
            ("y=4 is a line parallel to", *pack("x-axis", "y-axis", "both axes", "no axis"), "y=constant is horizontal."),
            ("If x+y=" + str(n+5) + " and x=" + str(n) + ", y is", *pack("5", str(n+5), str(n), str(n-5)), "Substitute x=n."),
            ("The cross multiplication method is used to solve", *pack("linear pair", "only triangles", "only AP", "only probability"), "It is an algebraic method for linear pairs."),
        ],
        "Quadratic Equations": [
            ("A quadratic equation has degree", *pack("2", "1", "3", "0"), "Quadratic equations have highest power 2."),
            ("Standard form is", *pack("ax^2+bx+c=0", "ax+b=0", "a/x+b=0", "x+y=0"), "The standard quadratic form is ax^2+bx+c=0."),
            ("In ax^2+bx+c=0, a must not be", *pack("0", "1", "-1", "2"), "If a=0, it is not quadratic."),
            ("Quadratic formula is x =", *pack("(-b +- sqrt(b^2-4ac))/(2a)", "-b/a", "c/a", "b^2-4ac"), "This formula gives the roots."),
            ("Discriminant D equals", *pack("b^2-4ac", "b^2+4ac", "a^2-4bc", "2a"), "D tells the nature of roots."),
            ("If D > 0, roots are", *pack("real and distinct", "real and equal", "not real", "zero only"), "Positive discriminant gives two distinct real roots."),
            ("If D = 0, roots are", *pack("real and equal", "real and distinct", "not real", "imaginary only"), "Zero discriminant gives equal roots."),
            ("If D < 0, roots are", *pack("not real", "real and equal", "real and distinct", "always zero"), "Negative discriminant gives no real roots."),
            ("Roots of x^2 - 5x + 6 = 0 are", *pack("2 and 3", "1 and 6", "-2 and -3", "0 and 6"), "The factors are (x-2)(x-3)."),
            ("x^2 - " + str(n*n) + " = 0 has roots", *pack(str(n) + " and -" + str(n), str(n) + " only", "0 and " + str(n), "1 and " + str(n)), "It is a difference of squares."),
            ("Completing the square changes a quadratic into", *pack("square form", "linear form only", "AP form", "probability form"), "It creates a perfect square expression."),
            ("Product of roots of ax^2+bx+c=0 is", *pack("c/a", "-b/a", "b/a", "-c/a"), "Product is c/a."),
            ("Sum of roots of ax^2+bx+c=0 is", *pack("-b/a", "c/a", "b/a", "-c/a"), "Sum is -b/a."),
            ("A root of an equation is a value that", *pack("satisfies the equation", "is always positive", "is always zero", "is coefficient only"), "Substitution makes the equation true."),
            ("Factorisation method uses", *pack("splitting middle term", "only graphs", "only compass", "only median"), "Many quadratics are solved by factorising."),
        ],
    }
    if chapter in banks:
        return banks[chapter]
    if chapter == "Arithmetic Progressions":
        return ap_bank(n)
    if chapter == "Triangles":
        return triangles_bank(n)
    if chapter == "Coordinate Geometry":
        return coordinate_bank(n)
    if chapter == "Introduction to Trigonometry":
        return trig_bank(n)
    if chapter == "Some Applications of Trigonometry":
        return trig_apps_bank(n)
    if chapter == "Circles":
        return circles_bank(n)
    if chapter == "Areas Related to Circles":
        return circle_area_bank(n)
    if chapter == "Surface Areas and Volumes":
        return mensuration_bank(n)
    if chapter == "Statistics":
        return statistics_bank(n)
    if chapter == "Probability":
        return probability_bank(n)
    raise ValueError(chapter)


def ap_bank(n):
    return [
        ("An AP has a constant", *pack("common difference", "common ratio", "area", "probability"), "AP terms differ by a fixed amount."),
        ("nth term of an AP is", *pack("a+(n-1)d", "a+nd", "2a+(n-1)d", "a/d"), "This is the nth term formula."),
        ("Sum of first n terms is", *pack("n/2[2a+(n-1)d]", "a+(n-1)d", "nd", "a^n"), "This is the AP sum formula."),
        ("For AP 2,5,8,... common difference is", *pack("3", "2", "5", "8"), "5-2=3."),
        ("For AP 7,4,1,... common difference is", *pack("-3", "3", "4", "7"), "4-7=-3."),
        ("The 5th term of AP 3,6,9,... is", *pack("15", "12", "18", "9"), "a5=3+(5-1)3=15."),
        ("If common difference is 0, all AP terms are", *pack("equal", "increasing", "decreasing", "prime"), "No change means all terms are same."),
        ("An AP is finite if it has", *pack("limited number of terms", "infinite terms", "no first term", "no common difference"), "Finite AP ends after a fixed number of terms."),
        ("Arithmetic mean of a and b is", *pack("(a+b)/2", "ab", "a/b", "a-b"), "The middle AP term between two numbers is their average."),
        ("For AP " + str(n) + ", " + str(n+2) + ", " + str(n+4) + ", d is", *pack("2", str(n), str(n+2), "4"), "Consecutive terms differ by 2."),
        ("If a=5 and d=2, a10 is", *pack("23", "25", "20", "27"), "a10=5+9x2=23."),
        ("If a=1, d=1, sum of first 10 terms is", *pack("55", "10", "45", "100"), "1+2+...+10=55."),
        ("In an AP, consecutive terms are obtained by adding", *pack("d", "n", "a", "S"), "The common difference d is repeatedly added."),
        ("The sequence 2,4,8,16 is not an AP because differences are", *pack("not equal", "equal", "zero", "negative only"), "Differences are 2,4,8."),
        ("The first term of an AP is usually denoted by", *pack("a", "d", "n", "S"), "a denotes the first term."),
    ]


def triangles_bank(n):
    return [
        ("Similar triangles have same", *pack("shape", "size always", "area always", "perimeter always"), "Similar figures have same shape."),
        ("Corresponding angles of similar triangles are", *pack("equal", "supplementary", "zero", "unrelated"), "Equal angles are part of similarity."),
        ("Corresponding sides of similar triangles are", *pack("proportional", "always equal", "always zero", "perpendicular"), "Side ratios are equal."),
        ("BPT is also called", *pack("Thales theorem", "Pythagoras theorem", "Euclid lemma", "Heron formula"), "Basic proportionality theorem is Thales theorem."),
        ("If a line is parallel to one side of a triangle, it divides other two sides", *pack("in same ratio", "equally always", "at right angles", "randomly"), "This is BPT."),
        ("SSS similarity uses", *pack("three proportional sides", "three equal angles only", "one side", "one right angle"), "All three side ratios must match."),
        ("AA similarity uses", *pack("two equal angles", "two equal sides", "three equal sides", "one median"), "Two equal angles imply similarity."),
        ("Area ratio of similar triangles equals", *pack("square of side ratio", "side ratio", "cube of side ratio", "sum of sides"), "Areas scale by square of corresponding side ratio."),
        ("Pythagoras theorem applies to", *pack("right triangle", "all triangles", "only equilateral triangles", "circles"), "It is for right triangles."),
        ("In a right triangle, hypotenuse is", *pack("longest side", "shortest side", "height always", "median"), "It lies opposite the right angle."),
        ("If legs are 3 and 4, hypotenuse is", *pack("5", "6", "7", "12"), "3-4-5 is a Pythagorean triplet."),
        ("Converse of Pythagoras helps prove a triangle is", *pack("right angled", "equilateral", "isosceles always", "obtuse always"), "If a^2+b^2=c^2, the triangle is right angled."),
        ("Congruent triangles are always", *pack("similar", "not similar", "larger", "smaller"), "Same shape and size implies same shape."),
        ("If side ratio is 2:3, area ratio is", *pack("4:9", "2:3", "8:27", "3:2"), "Area ratio is square of side ratio."),
        ("Similarity symbol is commonly written as", *pack("~", "=", ">", "||"), "The tilde symbol denotes similarity."),
    ]


def coordinate_bank(n):
    return [
        ("Distance between (x1,y1) and (x2,y2) is", *pack("sqrt((x2-x1)^2+(y2-y1)^2)", "x2-x1", "y2-y1", "x1+y1"), "This is the distance formula."),
        ("Distance between (0,0) and (3,4) is", *pack("5", "7", "1", "25"), "sqrt(3^2+4^2)=5."),
        ("Midpoint of (x1,y1), (x2,y2) is", *pack("((x1+x2)/2,(y1+y2)/2)", "(x1+x2,y1+y2)", "(x2-x1,y2-y1)", "(x1y1,x2y2)"), "Average the coordinates."),
        ("Midpoint of (2,4) and (6,8) is", *pack("(4,6)", "(8,12)", "(2,6)", "(6,4)"), "Average x and y coordinates."),
        ("Section formula is used to find a point that", *pack("divides a segment in a given ratio", "draws a circle", "finds mean", "finds probability"), "It locates division points."),
        ("Area of triangle with collinear points is", *pack("0", "1", "2", "cannot be zero"), "Collinear points form no triangle area."),
        ("The x-coordinate is also called", *pack("abscissa", "ordinate", "origin", "quadrant"), "Abscissa means x-coordinate."),
        ("The y-coordinate is also called", *pack("ordinate", "abscissa", "origin", "axis"), "Ordinate means y-coordinate."),
        ("Point (0,0) is called", *pack("origin", "quadrant", "midpoint", "vertex"), "The axes meet at the origin."),
        ("A point on x-axis has y-coordinate", *pack("0", "1", "-1", "any non-zero"), "All x-axis points have y=0."),
        ("A point on y-axis has x-coordinate", *pack("0", "1", "-1", "any non-zero"), "All y-axis points have x=0."),
        ("Distance between (" + str(n) + ",0) and (0,0) is", *pack(str(n), str(n*n), "0", str(n+1)), "It is n units from the origin on x-axis."),
        ("The coordinate plane uses", *pack("ordered pairs", "only ratios", "only sectors", "only tangents"), "Points are represented by ordered pairs."),
        ("Area formula in coordinate geometry uses", *pack("determinant-like expression", "only radius", "only HCF", "only AP sum"), "Triangle area can be found from coordinates."),
        ("If three points make zero area, they are", *pack("collinear", "concyclic always", "similar", "tangent"), "Zero area means they lie on one line."),
    ]


def trig_bank(n):
    return [
        ("sin theta equals", *pack("opposite/hypotenuse", "adjacent/hypotenuse", "opposite/adjacent", "hypotenuse/opposite"), "Sine is opposite over hypotenuse."),
        ("cos theta equals", *pack("adjacent/hypotenuse", "opposite/hypotenuse", "opposite/adjacent", "hypotenuse/adjacent"), "Cosine is adjacent over hypotenuse."),
        ("tan theta equals", *pack("opposite/adjacent", "adjacent/hypotenuse", "opposite/hypotenuse", "hypotenuse/opposite"), "Tangent is opposite over adjacent."),
        ("sin 30 degrees equals", *pack("1/2", "sqrt(3)/2", "1", "0"), "This is a standard trigonometric value."),
        ("cos 60 degrees equals", *pack("1/2", "sqrt(3)/2", "1", "0"), "cos 60 = 1/2."),
        ("tan 45 degrees equals", *pack("1", "0", "sqrt(3)", "1/sqrt(3)"), "tan 45 = 1."),
        ("sin^2 theta + cos^2 theta equals", *pack("1", "0", "tan theta", "2"), "This is the main trigonometric identity."),
        ("sec theta is reciprocal of", *pack("cos theta", "sin theta", "tan theta", "cot theta"), "sec = 1/cos."),
        ("cosec theta is reciprocal of", *pack("sin theta", "cos theta", "tan theta", "sec theta"), "cosec = 1/sin."),
        ("cot theta is reciprocal of", *pack("tan theta", "sin theta", "cos theta", "sec theta"), "cot = 1/tan."),
        ("sin(90-A) equals", *pack("cos A", "sin A", "tan A", "sec A"), "Complementary angle identity."),
        ("cos(90-A) equals", *pack("sin A", "cos A", "tan A", "cot A"), "Complementary angle identity."),
        ("Trigonometric ratios are defined in", *pack("right triangle", "any quadrilateral", "circle only", "AP only"), "They begin with right triangles."),
        ("Hypotenuse is opposite the", *pack("right angle", "smallest angle always", "30 degree angle always", "base"), "The hypotenuse lies opposite 90 degrees."),
        ("If opposite=3 and hypotenuse=5, sin theta is", *pack("3/5", "4/5", "3/4", "5/3"), "sin is opposite over hypotenuse."),
    ]


def trig_apps_bank(n):
    return [
        ("Angle of elevation is measured when observer looks", *pack("up", "down", "horizontally only", "inside a circle"), "It is the angle above horizontal."),
        ("Angle of depression is measured when observer looks", *pack("down", "up", "at same level", "through a tangent"), "It is the angle below horizontal."),
        ("Line of sight is the line from eye to", *pack("object", "origin only", "circle centre", "median"), "It connects observer and object."),
        ("Heights and distances problems usually form", *pack("right triangles", "circles only", "AP only", "statistics tables"), "Trigonometry models them as right triangles."),
        ("If tan theta = height/distance, then height equals", *pack("distance x tan theta", "distance/tan theta", "tan theta/distance", "distance+tan theta"), "Rearrange tan theta = height/distance."),
        ("For angle 45 degrees, tan 45 equals", *pack("1", "0", "sqrt(3)", "1/sqrt(3)"), "tan 45 = 1."),
        ("If tan 45 = height/10, height is", *pack("10", "5", "20", "1"), "tan45=1, so height/10=1."),
        ("A shadow problem uses height and", *pack("horizontal distance", "volume", "mean", "probability"), "Shadow length is horizontal distance."),
        ("The horizontal line through observer is called", *pack("horizontal level", "hypotenuse always", "tangent", "axis of symmetry"), "Angles are measured from horizontal."),
        ("When object is above observer, angle is", *pack("elevation", "depression", "zero always", "obtuse always"), "Looking upward gives elevation."),
        ("When object is below observer, angle is", *pack("depression", "elevation", "right angle always", "straight angle"), "Looking downward gives depression."),
        ("The side opposite angle of elevation often represents", *pack("height", "ground distance", "probability", "radius only"), "In the right triangle, vertical side is height."),
        ("The ground distance is usually", *pack("adjacent side", "opposite side", "hypotenuse always", "radius"), "Horizontal distance is adjacent to ground angle."),
        ("Trigonometry avoids direct measurement of", *pack("inaccessible heights", "data frequency only", "HCF only", "polynomial degree"), "It estimates heights using angles and distances."),
        ("For a tower problem, the tower is usually assumed", *pack("vertical", "horizontal", "curved", "random"), "The tower forms a right angle with ground."),
    ]


def circles_bank(n):
    return [
        ("A tangent touches a circle at", *pack("one point", "two points", "no point", "all points"), "A tangent has exactly one point of contact."),
        ("A secant intersects a circle at", *pack("two points", "one point", "no point", "centre only"), "A secant cuts the circle at two points."),
        ("Radius to point of contact is", *pack("perpendicular to tangent", "parallel to tangent", "equal to tangent always", "not related"), "This is a key tangent theorem."),
        ("Tangents drawn from an external point are", *pack("equal in length", "unequal always", "parallel", "radii"), "Two tangents from the same external point are equal."),
        ("The point where tangent touches circle is", *pack("point of contact", "centre", "secant", "diameter"), "It is called point of contact."),
        ("Number of tangents at a point on circle is", *pack("1", "2", "0", "infinite"), "Exactly one tangent can be drawn at a point on the circle."),
        ("Number of tangents from a point inside circle is", *pack("0", "1", "2", "infinite"), "No tangent can be drawn from an interior point."),
        ("Number of tangents from an external point is", *pack("2", "0", "1", "infinite"), "Two tangents can be drawn."),
        ("A tangent is perpendicular to radius at", *pack("point of contact", "centre", "any secant point", "diameter end only"), "The perpendicularity occurs at contact."),
        ("If PA and PB are tangents from P, then", *pack("PA = PB", "PA > PB always", "PA < PB always", "PA + PB = 0"), "Tangents from an external point are equal."),
        ("A line through centre and point of contact is", *pack("radius", "tangent", "secant", "chord only"), "Centre to circle point is radius."),
        ("A tangent and radius form angle", *pack("90 degrees", "60 degrees", "45 degrees", "180 degrees"), "They are perpendicular."),
        ("The tangent theorem belongs to chapter", *pack("Circles", "Statistics", "AP", "Real Numbers"), "Tangents are studied in Circles."),
        ("A chord with endpoints on circle differs from tangent because it has", *pack("two circle points", "one circle point", "no circle point", "only centre"), "A chord joins two circle points."),
        ("A tangent is a special line related to", *pack("circle", "AP", "polynomial", "probability"), "Tangents are circle lines."),
    ]


def circle_area_bank(n):
    return [
        ("Circumference of a circle is", *pack("2 pi r", "pi r^2", "pi r l", "4 pi r^2"), "Circumference is boundary length."),
        ("Area of a circle is", *pack("pi r^2", "2 pi r", "pi r l", "l b"), "Circle area formula."),
        ("Arc length for angle theta is", *pack("theta/360 x 2 pi r", "theta/360 x pi r^2", "2 pi r h", "pi r l"), "Arc is part of circumference."),
        ("Area of sector for angle theta is", *pack("theta/360 x pi r^2", "theta/360 x 2 pi r", "pi r l", "4 pi r^2"), "Sector is part of circle area."),
        ("A sector is like a", *pack("slice of circle", "full rectangle", "solid cone", "line only"), "A sector is bounded by two radii and an arc."),
        ("A segment is bounded by", *pack("a chord and an arc", "two radii only", "two tangents", "two axes"), "Segment lies between chord and arc."),
        ("If radius doubles, circle area becomes", *pack("four times", "two times", "half", "same"), "Area depends on r squared."),
        ("If radius doubles, circumference becomes", *pack("two times", "four times", "half", "same"), "Circumference depends linearly on r."),
        ("Diameter equals", *pack("2r", "r/2", "pi r", "r^2"), "Diameter is twice radius."),
        ("Area of semicircle is", *pack("1/2 pi r^2", "2 pi r", "pi r^2", "4 pi r^2"), "A semicircle is half a circle."),
        ("Perimeter of semicircle is", *pack("pi r + 2r", "pi r only", "2 pi r", "pi r^2"), "It includes arc plus diameter."),
        ("Shaded region problems often require", *pack("subtracting areas", "adding probabilities", "finding HCF", "solving AP only"), "Find large area minus smaller area."),
        ("pi is commonly taken as", *pack("22/7 or 3.14", "2.71", "1.41", "0"), "These are common approximations."),
        ("A quadrant is sector of angle", *pack("90 degrees", "180 degrees", "60 degrees", "360 degrees"), "One-fourth circle is 90 degrees."),
        ("Area related to circles uses", *pack("radius", "mean", "common difference", "discriminant only"), "Most circle formulas use radius."),
    ]


def mensuration_bank(n):
    return [
        ("TSA of cuboid is", *pack("2(lb+bh+hl)", "lbh", "6a^2", "pi r^2 h"), "Total surface area of cuboid."),
        ("Volume of cuboid is", *pack("lbh", "2(lb+bh+hl)", "4 pi r^2", "pi r l"), "Volume uses length, breadth and height."),
        ("Surface area of cube is", *pack("6a^2", "a^3", "4a", "2a"), "A cube has six square faces."),
        ("Volume of cube is", *pack("a^3", "6a^2", "4a", "a^2"), "Cube volume is side cubed."),
        ("CSA of cylinder is", *pack("2 pi r h", "pi r^2 h", "pi r l", "4 pi r^2"), "Curved surface area of cylinder."),
        ("Volume of cylinder is", *pack("pi r^2 h", "2 pi r h", "pi r l", "1/3 pi r^2 h"), "Base area times height."),
        ("CSA of cone is", *pack("pi r l", "pi r^2 h", "2 pi r h", "4 pi r^2"), "Cone curved area uses slant height."),
        ("Volume of cone is", *pack("1/3 pi r^2 h", "pi r^2 h", "pi r l", "2 pi r h"), "Cone volume is one third cylinder."),
        ("Surface area of sphere is", *pack("4 pi r^2", "pi r^2", "2 pi r h", "pi r l"), "Sphere surface area."),
        ("Volume of sphere is", *pack("4/3 pi r^3", "4 pi r^2", "pi r^2 h", "1/3 pi r^2 h"), "Sphere volume formula."),
        ("Hemisphere curved surface area is", *pack("2 pi r^2", "4 pi r^2", "3 pi r^2", "pi r^2"), "Half of sphere surface area."),
        ("Hemisphere total surface area is", *pack("3 pi r^2", "2 pi r^2", "4 pi r^2", "pi r^2"), "CSA plus circular base."),
        ("Volume is measured in", *pack("cubic units", "square units", "degrees", "percent"), "Volume measures space."),
        ("Surface area is measured in", *pack("square units", "cubic units", "linear units", "litres only"), "Surface area covers surface."),
        ("When a solid is melted and recast, volume is", *pack("conserved", "doubled always", "zero", "ignored"), "Recasting keeps volume same."),
    ]


def statistics_bank(n):
    return [
        ("Class mark is", *pack("(lower limit + upper limit)/2", "upper-lower", "frequency/class", "mean/median"), "Class mark is midpoint."),
        ("Mean by direct method is", *pack("sum fi xi / sum fi", "sum fi / sum xi", "highest frequency", "middle class"), "Grouped mean formula."),
        ("Median is found using", *pack("cumulative frequency", "only HCF", "only tangent", "common difference"), "Median class is located by cumulative frequency."),
        ("Mode is the value with", *pack("maximum frequency", "minimum frequency", "middle position", "zero frequency"), "Mode is most frequent."),
        ("Modal class has", *pack("highest frequency", "lowest frequency", "middle value", "largest class width always"), "Mode formula uses modal class."),
        ("Ogive is a graph of", *pack("cumulative frequency", "polynomial", "circle area", "trigonometric ratio"), "Ogives plot cumulative frequencies."),
        ("Less than ogive uses", *pack("upper class limits", "lower class limits", "class marks only", "frequencies only"), "Less-than cumulative frequency pairs with upper limits."),
        ("More than ogive uses", *pack("lower class limits", "upper class limits", "midpoints only", "mean only"), "More-than cumulative frequency pairs with lower limits."),
        ("Median from ogives is found at their", *pack("intersection", "radius", "tangent point", "origin only"), "Intersection gives median estimate."),
        ("Step deviation method is useful when class marks have", *pack("common width", "no pattern", "zero frequency", "negative area"), "It simplifies arithmetic."),
        ("Mean is affected by", *pack("all observations", "only middle observation", "only modal class", "only zero"), "Mean uses every value."),
        ("Median divides data into", *pack("two equal parts", "three equal parts", "classes only", "sectors"), "Half data lies below and half above."),
        ("For data 2,3,4, mean is", *pack("3", "2", "4", "9"), "Average is 9/3=3."),
        ("For data 2,3,3,4, mode is", *pack("3", "2", "4", "12"), "3 occurs most often."),
        ("Statistics helps to", *pack("interpret data", "draw tangents only", "find roots only", "construct triangles only"), "Statistics is about data handling."),
    ]


def probability_bank(n):
    return [
        ("Probability of an event equals", *pack("favourable outcomes/total outcomes", "total/favourable always", "mean/median", "area/volume"), "Classical probability formula."),
        ("Probability of impossible event is", *pack("0", "1", "1/2", "2"), "Impossible event never occurs."),
        ("Probability of certain event is", *pack("1", "0", "1/2", "2"), "Certain event always occurs."),
        ("Probability always lies between", *pack("0 and 1", "1 and 2", "-1 and 1 only", "10 and 100"), "Probability range is 0 to 1."),
        ("A coin toss has outcomes", *pack("H and T", "1 and 2", "red and black only", "0 and 6"), "A coin has head and tail."),
        ("Probability of head in fair coin toss is", *pack("1/2", "1", "0", "2"), "One favourable out of two."),
        ("A die has total outcomes", *pack("6", "2", "4", "52"), "A standard die has six faces."),
        ("Probability of getting 5 on a die is", *pack("1/6", "5/6", "1/2", "1"), "One favourable outcome out of six."),
        ("Probability of getting an even number on die is", *pack("1/2", "1/3", "1/6", "2/3"), "Even outcomes are 2,4,6: three out of six."),
        ("A deck of cards has", *pack("52 cards", "26 cards", "13 cards", "4 cards"), "Standard deck has 52 cards."),
        ("Number of kings in a deck is", *pack("4", "13", "26", "52"), "There is one king in each suit."),
        ("Probability of drawing a king is", *pack("1/13", "1/4", "4/13", "13/52"), "4/52 simplifies to 1/13."),
        ("Complementary event probability is", *pack("1 - P(E)", "P(E)+1", "P(E)-1", "2P(E)"), "P(not E)=1-P(E)."),
        ("If P(E)=0.3, P(not E) is", *pack("0.7", "0.3", "1.3", "0"), "1-0.3=0.7."),
        ("Equally likely outcomes have", *pack("same chance", "different chance always", "zero chance", "probability greater than 1"), "They are equally possible."),
    ]


def build():
    module_id = 1
    chapters = []
    for chapter, topics in CHAPTERS:
        modules = []
        diff = DIFF[chapter]
        seconds = {"Easy": 30, "Medium": 45, "Hard": 60}[diff]
        for topic in topics:
            questions = []
            for i, item in enumerate(bank(chapter, module_id), start=1):
                questions.append({
                    "question_id": i,
                    "question_text": f"{topic}: {item[0]}",
                    "options": item[1],
                    "correct_answer": item[2],
                    "rationale": item[3],
                    "timer_per_question_seconds": seconds,
                })
            modules.append({
                "module_id": module_id,
                "topic_name": topic,
                "explanation": EXPLAIN[chapter],
                "difficulty": diff,
                "total_timer_minutes": 15 if diff == "Hard" else 10,
                "questions": questions,
            })
            module_id += 1
        chapters.append({"chapter_name": chapter, "modules": modules})
    return {
        "class": "10",
        "board": "CBSE",
        "subject": "Mathematics",
        "source_pdf": "NCERT-10th-New-Maths-Textbook-CBSE-2024-25-min.pdf",
        "chapters": chapters,
    }


if __name__ == "__main__":
    data = build()
    OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
    modules = sum(len(c["modules"]) for c in data["chapters"])
    questions = sum(len(m["questions"]) for c in data["chapters"] for m in c["modules"])
    print(OUT)
    print(f"chapters={len(data['chapters'])}")
    print(f"modules={modules}")
    print(f"questions={questions}")
