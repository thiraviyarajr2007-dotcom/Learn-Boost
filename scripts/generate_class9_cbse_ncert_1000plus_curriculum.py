import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "class9_cbse_ncert_duolingo_curriculum_1000plus.json"


CHAPTERS = [
    ("Number Systems", ["Introduction to Number Systems", "Irrational Numbers", "Real Numbers and Decimal Expansions", "Real Numbers on the Number Line", "Operations on Real Numbers", "Laws of Exponents for Real Numbers"]),
    ("Polynomials", ["Polynomials in One Variable", "Zeroes of a Polynomial", "Remainder Theorem", "Factorisation of Polynomials", "Algebraic Identities"]),
    ("Coordinate Geometry", ["Cartesian System", "Coordinates and Quadrants", "Plotting Points in the Plane"]),
    ("Linear Equations in Two Variables", ["Linear Equations", "Solutions of a Linear Equation", "Graph of a Linear Equation", "Lines Parallel to Axes"]),
    ("Introduction to Euclid's Geometry", ["Euclid's Definitions", "Axioms and Postulates", "Fifth Postulate and Equivalent Versions"]),
    ("Lines and Angles", ["Basic Terms and Definitions", "Intersecting and Non-intersecting Lines", "Pairs of Angles", "Parallel Lines and a Transversal", "Lines Parallel to the Same Line", "Angle Sum Property of a Triangle", "Exterior Angle Property"]),
    ("Triangles", ["Congruence of Triangles", "SSS, SAS and ASA Criteria", "Properties of Isosceles Triangles", "RHS Congruence", "Inequalities in a Triangle", "Applications of Triangle Congruence"]),
    ("Quadrilaterals", ["Angle Sum Property of a Quadrilateral", "Types of Quadrilaterals", "Properties of a Parallelogram", "Conditions for Parallelograms", "Mid-point Theorem", "Special Quadrilaterals"]),
    ("Areas of Parallelograms and Triangles", ["Same Base and Same Parallels", "Parallelograms on Same Base", "Triangles on Same Base", "Area Relationships"]),
    ("Circles", ["Circle Terms", "Angle Subtended by a Chord", "Perpendicular from Centre to Chord", "Circle Through Three Points", "Equal Chords and Distances", "Angle Subtended by an Arc", "Cyclic Quadrilaterals"]),
    ("Constructions", ["Basic Constructions", "Constructing Triangles", "Angle Bisectors and Perpendiculars"]),
    ("Heron's Formula", ["Area by Heron's Formula", "Semi-perimeter", "Areas of Quadrilaterals"]),
    ("Surface Areas and Volumes", ["Surface Area of Cuboid and Cube", "Surface Area of Cylinder", "Surface Area of Cone", "Surface Area of Sphere", "Volume of Cuboid", "Volume of Cylinder", "Volume of Cone", "Volume of Sphere"]),
    ("Statistics", ["Collection of Data", "Presentation of Data", "Graphical Representation of Data", "Mean, Median and Mode", "Choosing a Measure of Central Tendency"]),
    ("Probability", ["Experimental Probability", "Trials and Events", "Interpreting Probability"]),
]


DIFFICULTY = {
    "Number Systems": "Hard",
    "Polynomials": "Hard",
    "Coordinate Geometry": "Medium",
    "Linear Equations in Two Variables": "Hard",
    "Introduction to Euclid's Geometry": "Medium",
    "Lines and Angles": "Hard",
    "Triangles": "Hard",
    "Quadrilaterals": "Hard",
    "Areas of Parallelograms and Triangles": "Medium",
    "Circles": "Hard",
    "Constructions": "Medium",
    "Heron's Formula": "Hard",
    "Surface Areas and Volumes": "Hard",
    "Statistics": "Medium",
    "Probability": "Medium",
}


EXPLANATIONS = {
    "Number Systems": "This module grows the number family from natural numbers to real numbers. Students compare rational and irrational numbers, understand decimal expansions, place real numbers on the number line, and use exponent laws. Think of the number line as a long road: rationals and irrationals together fill every point on it.",
    "Polynomials": "Polynomials are algebraic expressions made from variables and powers with numerical coefficients. In this module, students identify degree, terms and zeroes, then use the remainder theorem, factor theorem and identities. Polynomials are like algebraic machines: put in a value, and they produce an output.",
    "Coordinate Geometry": "Coordinate geometry locates points using ordered pairs. The x-coordinate tells horizontal movement and the y-coordinate tells vertical movement. The plane is divided into four quadrants by the axes. Like a map grid, coordinates help us describe exact positions clearly.",
    "Linear Equations in Two Variables": "A linear equation in two variables has many solution pairs. Each solution pair becomes a point, and all such points form a straight line on the graph. This module connects algebra with geometry, showing how equations can be seen as lines.",
    "Introduction to Euclid's Geometry": "Euclid built geometry from definitions, axioms and postulates. Axioms are accepted truths, and postulates are basic assumptions for geometry. This module helps students see that mathematical results are not guesses; they are built step by step from agreed foundations.",
    "Lines and Angles": "Lines and angles form the grammar of geometry. Students use angle pairs, parallel lines, transversals and triangle angle facts to find unknown angles. The key idea is simple: once one angle is known, connected angle relationships reveal many others.",
    "Triangles": "Triangles are rigid shapes with powerful congruence rules. Students learn when two triangles are exactly the same using SSS, SAS, ASA and RHS. They also explore isosceles triangle properties and triangle inequalities. These results help prove geometric statements confidently.",
    "Quadrilaterals": "Quadrilaterals are four-sided figures with rich structure. Students study angle sums, parallelogram properties, special quadrilaterals and the mid-point theorem. A parallelogram is especially useful because opposite sides, angles and diagonals follow predictable rules.",
    "Areas of Parallelograms and Triangles": "Area relationships become easier when figures stand on the same base and lie between the same parallels. Such figures share the same height, so their areas can be compared without measuring everything. This module builds proof-style thinking about area.",
    "Circles": "A circle has one centre but many beautiful relationships. Chords, arcs, angles and cyclic quadrilaterals follow strong rules. Students learn how equal chords relate to distances, how arcs create angles, and why opposite angles of a cyclic quadrilateral are supplementary.",
    "Constructions": "Constructions use compass and straightedge to draw accurate figures. Students construct perpendiculars, bisectors, angles and triangles using given measurements. The focus is not decoration; it is precision, sequence and understanding why each construction step works.",
    "Heron's Formula": "Heron's formula finds the area of a triangle when all three sides are known. First find the semi-perimeter, then use the formula with side lengths. It is especially useful when height is not given. Quadrilaterals can be split into triangles and handled similarly.",
    "Surface Areas and Volumes": "Mensuration connects formulas with real objects. Surface area measures outer covering, while volume measures space inside. Students work with cuboids, cubes, cylinders, cones and spheres. The formulas help solve problems about boxes, tanks, pipes, balls and containers.",
    "Statistics": "Statistics turns raw information into meaning. Students collect data, arrange it in tables, draw graphs, and calculate mean, median and mode. Each measure tells a different story: mean balances, median finds the middle, and mode shows what occurs most often.",
    "Probability": "Probability measures chance through experiments. In Class 9, the focus is experimental probability: repeated trials show how likely an event is. The value lies between 0 and 1, where 0 means impossible and 1 means certain.",
}


def opt(correct, *wrongs):
    values = [str(correct), *map(str, wrongs)]
    return values[:4], str(correct)


def bank(chapter, seed):
    s = seed + 2
    if chapter == "Number Systems":
        return [
            ("Which set is denoted by N?", *opt("Natural numbers", "Whole numbers", "Integers", "Real numbers"), "N represents the natural numbers."),
            ("Which number is irrational?", *opt("sqrt(2)", "3/4", "-5", "0.25"), "sqrt(2) cannot be expressed as p/q."),
            ("The decimal expansion of 1/3 is", *opt("non-terminating recurring", "terminating", "non-terminating non-recurring", "integer"), "1/3 = 0.333..., which repeats."),
            ("The decimal expansion of an irrational number is", *opt("non-terminating non-recurring", "terminating", "always recurring", "always zero"), "Irrational decimals neither terminate nor repeat."),
            ("Which is a real number?", *opt("sqrt(5)", "only natural numbers", "only integers", "only fractions"), "Real numbers include rational and irrational numbers."),
            ("sqrt(9) equals", *opt("3", "9", "81", "1/3"), "3 squared is 9."),
            ("a^m x a^n equals", *opt("a^(m+n)", "a^(m-n)", "a^(mn)", "a/(m+n)"), "Same bases are multiplied by adding exponents."),
            ("a^m divided by a^n equals", *opt("a^(m-n)", "a^(m+n)", "a^(mn)", "a^0 always"), "Same bases are divided by subtracting exponents."),
            ("Between any two rational numbers there are", *opt("infinitely many rational numbers", "no rational numbers", "only one integer", "only irrational numbers"), "There are infinitely many rationals between two rationals."),
            ("Which number is rational?", *opt(f"{s}/{s+1}", "sqrt(3)", "pi", "sqrt(7)"), "A number of the form p/q with q non-zero is rational."),
            ("The number line represents", *opt("real numbers", "only natural numbers", "only prime numbers", "only polygons"), "Every real number has a point on the number line."),
            ("The reciprocal of 5 is", *opt("1/5", "5", "-5", "0"), "The reciprocal of a non-zero number a is 1/a."),
            ("Which is not a rational representation?", *opt("4/0", "4/1", "-3/5", "0/7"), "The denominator of a rational number cannot be zero."),
            ("sqrt(2) + sqrt(2) equals", *opt("2sqrt(2)", "sqrt(4)", "4", "2"), "Like radicals combine as 2sqrt(2)."),
        ]
    if chapter == "Polynomials":
        return [
            ("The degree of 5x^3 + 2x + 1 is", *opt("3", "1", "2", "5"), "The highest power of x is 3."),
            ("A polynomial with one term is called a", *opt("monomial", "binomial", "trinomial", "constant only"), "Mono means one term."),
            ("A zero of p(x) is a value where p(x) equals", *opt("0", "1", "x", "degree"), "A zero makes the polynomial value zero."),
            ("For p(x)=x-4, the zero is", *opt("4", "-4", "0", "1"), "p(4)=4-4=0."),
            ("By remainder theorem, remainder on dividing p(x) by x-a is", *opt("p(a)", "p(0)", "a", "0 always"), "The theorem says the remainder is p(a)."),
            ("If p(a)=0, then x-a is a", *opt("factor of p(x)", "degree of p(x)", "coefficient only", "remainder only"), "This is the factor theorem."),
            ("(a+b)^2 equals", *opt("a^2+2ab+b^2", "a^2+b^2", "a^2-b^2", "2a+2b"), "This is a standard identity."),
            ("(a-b)^2 equals", *opt("a^2-2ab+b^2", "a^2+2ab+b^2", "a^2-b^2", "a-b^2"), "The middle term is negative."),
            ("a^2-b^2 equals", *opt("(a+b)(a-b)", "(a-b)^2", "(a+b)^2", "a(a-b)"), "This is the difference of squares identity."),
            (f"For p(x)=x+{s}, p(0) equals", *opt(str(s), str(s+1), "0", f"-{s}"), "Substitute x=0."),
            ("A polynomial in one variable contains", *opt("one variable", "two variables only", "no variable", "only decimals"), "The chapter studies polynomials in one variable."),
            ("The coefficient of x in 7x^2 + 3x - 5 is", *opt("3", "7", "-5", "2"), "The x-term is 3x."),
            ("A constant polynomial has degree", *opt("0", "1", "2", "undefined always"), "A non-zero constant polynomial has degree 0."),
            ("x^2 + 5x + 6 factorises as", *opt("(x+2)(x+3)", "(x+1)(x+6)", "(x-2)(x-3)", "x(x+6)"), "The factors multiply to x^2+5x+6."),
        ]
    if chapter == "Coordinate Geometry":
        return [
            ("The horizontal axis is called the", *opt("x-axis", "y-axis", "origin", "quadrant"), "The x-axis is horizontal."),
            ("The vertical axis is called the", *opt("y-axis", "x-axis", "origin", "abscissa"), "The y-axis is vertical."),
            ("The point where axes meet is the", *opt("origin", "quadrant", "ordinate", "unit point"), "The axes intersect at the origin."),
            ("Coordinates of the origin are", *opt("(0, 0)", "(1, 0)", "(0, 1)", "(1, 1)"), "Both coordinates are zero at the origin."),
            ("In (4, -3), the abscissa is", *opt("4", "-3", "1", "0"), "The x-coordinate is the abscissa."),
            ("In (4, -3), the ordinate is", *opt("-3", "4", "1", "0"), "The y-coordinate is the ordinate."),
            ("A point with coordinates (+, +) lies in", *opt("Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"), "Both coordinates positive means Quadrant I."),
            ("A point with coordinates (-, +) lies in", *opt("Quadrant II", "Quadrant I", "Quadrant III", "Quadrant IV"), "Negative x and positive y means Quadrant II."),
            ("A point on the x-axis has", *opt("y-coordinate 0", "x-coordinate 0", "both coordinates equal", "no coordinates"), "Every point on x-axis has y=0."),
            ("A point on the y-axis has", *opt("x-coordinate 0", "y-coordinate 0", "both coordinates positive", "no coordinates"), "Every point on y-axis has x=0."),
            (f"The point ({s}, {s+1}) has y-coordinate", *opt(str(s+1), str(s), "0", "-1"), "The second coordinate is y."),
            ("An ordered pair is written as", *opt("(x, y)", "(y, x) only", "x/y", "xy without order"), "Coordinates are written as (x, y)."),
            ("The coordinate plane is divided into", *opt("four quadrants", "two quadrants", "three quadrants", "six quadrants"), "The axes divide the plane into four regions."),
            ("The signs in Quadrant III are", *opt("(-, -)", "(+, +)", "(-, +)", "(+, -)"), "Both coordinates are negative in Quadrant III."),
        ]
    if chapter == "Linear Equations in Two Variables":
        return [
            ("A linear equation in two variables has graph as a", *opt("straight line", "circle", "parabola", "triangle"), "Its graph is a straight line."),
            ("Which is linear in two variables?", *opt("2x+3y=6", "x^2+y=5", "xy=4", "x^2+y^2=1"), "2x+3y=6", "Both variables have power 1 and are not multiplied."),
            ("A solution of 2x+y=5 is", *opt("(1,3)", "(2,2)", "(0,0)", "(5,5)"), "2(1)+3=5."),
            ("How many solutions can a linear equation in two variables have?", *opt("infinitely many", "only one", "only two", "none always"), "A line has infinitely many points."),
            ("The equation y=0 represents the", *opt("x-axis", "y-axis", "origin only", "line x=1"), "All points on x-axis have y=0."),
            ("The equation x=0 represents the", *opt("y-axis", "x-axis", "line y=1", "origin only"), "All points on y-axis have x=0."),
            ("The graph of x=3 is parallel to the", *opt("y-axis", "x-axis", "both axes", "no axis"), "x=constant is a vertical line."),
            ("The graph of y=4 is parallel to the", *opt("x-axis", "y-axis", "both axes", "no axis"), "y=constant is a horizontal line."),
            (f"For x+y={s}, if x=1 then y equals", *opt(str(s-1), str(s), "1", str(s+1)), "Substitute x=1."),
            ("In ax+by+c=0, if a and b are not both zero, it is", *opt("linear equation", "quadratic equation", "identity only", "circle equation"), "This is the general linear form."),
            ("The point (0, b) on a line is called", *opt("y-intercept point", "x-intercept point", "origin always", "quadrant point"), "At x=0, the graph meets the y-axis."),
            ("The point (a, 0) on a line is called", *opt("x-intercept point", "y-intercept point", "origin always", "midpoint"), "At y=0, the graph meets the x-axis."),
            ("To draw a line, minimum number of points needed is", *opt("2", "1", "3", "4"), "Two distinct points determine a line."),
            ("The solution pair of an equation is written as", *opt("(x, y)", "(y, x) only", "x/y", "x+y only"), "Solutions are ordered pairs."),
        ]
    if chapter == "Introduction to Euclid's Geometry":
        return [
            ("Euclid's geometry begins with", *opt("definitions, axioms and postulates", "statistics only", "probability only", "polynomials only"), "Euclid built geometry from basic assumptions."),
            ("An axiom is a statement accepted as", *opt("true without proof", "false always", "a construction", "a graph"), "Axioms are accepted truths."),
            ("A point has", *opt("no part", "length only", "breadth only", "area"), "Euclid described a point as that which has no part."),
            ("A line has", *opt("breadthless length", "area", "volume", "only endpoints"), "Euclid described a line as breadthless length."),
            ("Things equal to the same thing are", *opt("equal to one another", "always unequal", "parallel only", "circles"), "This is a common notion."),
            ("The whole is", *opt("greater than the part", "less than the part", "equal to every part", "not comparable"), "This is one of Euclid's common notions."),
            ("A postulate is a basic assumption used in", *opt("geometry", "only statistics", "only probability", "tax calculation"), "Postulates are accepted geometric assumptions."),
            ("Euclid's fifth postulate is linked to", *opt("parallel lines", "mean", "volume", "factorisation"), "The fifth postulate concerns parallels."),
            ("A terminated line can be produced", *opt("indefinitely", "only once", "never", "as a circle only"), "This is one of Euclid's postulates."),
            ("All right angles are", *opt("equal to one another", "unequal", "not angles", "always acute"), "Euclid accepts all right angles as equal."),
            ("A theorem is a statement that is", *opt("proved", "accepted without proof always", "a drawing tool", "a raw data set"), "Theorems require proof."),
            ("A definition explains", *opt("meaning of a term", "experimental chance", "tax value", "frequency only"), "Definitions clarify mathematical terms."),
            ("Parallel lines are lines that", *opt("do not meet", "meet at right angle", "are always curved", "have endpoints"), "Parallel lines never intersect."),
            ("Euclid's work is mainly associated with", *opt("geometry", "biology", "chemistry", "music"), "Euclid is famous for geometry."),
        ]
    if chapter in {"Lines and Angles", "Triangles", "Quadrilaterals", "Areas of Parallelograms and Triangles", "Circles", "Constructions"}:
        return geometry_bank(chapter, s)
    if chapter == "Heron's Formula":
        return [
            ("Heron's formula is used to find area of a triangle when", *opt("three sides are known", "only one angle is known", "only radius is known", "only mean is known"), "It uses side lengths."),
            ("Semi-perimeter s of sides a,b,c is", *opt("(a+b+c)/2", "a+b+c", "abc", "2(a+b+c)"), "Semi-perimeter is half the perimeter."),
            ("For sides 3,4,5, semi-perimeter is", *opt("6", "12", "5", "10"), "s=(3+4+5)/2=6."),
            ("Area by Heron's formula is", *opt("sqrt(s(s-a)(s-b)(s-c))", "s(a+b+c)", "abc", "1/2 perimeter"), "This is Heron's formula."),
            ("A quadrilateral area can be found by", *opt("splitting into triangles", "ignoring diagonal", "using only one side", "counting vertices"), "Split into triangles and apply area formulas."),
            ("For an equilateral triangle side a, Heron's formula leads to area", *opt("sqrt(3)/4 a^2", "a^2", "2a", "3a"), "This is the standard equilateral area."),
            ("Heron's formula does not require", *opt("height", "side lengths", "semi-perimeter", "square root"), "It works without height."),
            ("Perimeter of triangle with sides 5,6,7 is", *opt("18", "9", "30", "42"), "Add all side lengths."),
            ("Semi-perimeter of 5,6,7 is", *opt("9", "18", "7", "6"), "Half of 18 is 9."),
            (f"For sides {s}, {s}, {s}, the triangle is", *opt("equilateral", "scalene", "right angled always", "not a triangle"), "All three sides are equal."),
            ("Heron's formula includes a", *opt("square root", "cube root only", "coordinate axis", "probability"), "The formula begins with a square root."),
            ("A valid triangle must satisfy", *opt("sum of two sides greater than third", "sum of sides equals zero", "all sides unequal", "one side greater than perimeter"), "This is the triangle inequality."),
            ("Area is measured in", *opt("square units", "cubic units", "degrees", "linear units only"), "Area measures surface."),
            ("A diagonal of a quadrilateral helps create", *opt("two triangles", "two circles", "three axes", "no figure"), "A diagonal divides a quadrilateral into two triangles."),
        ]
    if chapter == "Surface Areas and Volumes":
        return mensuration_bank(s)
    if chapter == "Statistics":
        return statistics_bank(s)
    if chapter == "Probability":
        return probability_bank(s)
    raise ValueError(chapter)


def geometry_bank(chapter, s):
    common = [
        ("A straight angle measures", *opt("180 degrees", "90 degrees", "60 degrees", "360 degrees"), "A straight line forms 180 degrees."),
        ("Vertically opposite angles are", *opt("equal", "supplementary always", "zero", "unequal always"), "Opposite angles at an intersection are equal."),
        ("If a transversal cuts parallel lines, corresponding angles are", *opt("equal", "always 90 degrees", "always 180 degrees", "unrelated"), "Corresponding angles are equal for parallel lines."),
        ("The sum of angles of a triangle is", *opt("180 degrees", "90 degrees", "270 degrees", "360 degrees"), "This is the triangle angle sum property."),
        ("SSS congruence uses", *opt("three sides", "two angles", "one side", "one right angle only"), "SSS means side-side-side."),
        ("SAS congruence uses", *opt("two sides and included angle", "three angles", "one side only", "two non-included angles"), "SAS needs included angle."),
        ("RHS congruence applies to", *opt("right triangles", "all circles", "all quadrilaterals", "polynomials"), "RHS is for right-angled triangles."),
        ("A parallelogram has opposite sides", *opt("parallel and equal", "curved", "always unequal", "perpendicular only"), "Opposite sides of a parallelogram are equal and parallel."),
        ("Diagonals of a parallelogram", *opt("bisect each other", "never meet", "are always sides", "are always perpendicular"), "Each diagonal cuts the other into two equal parts."),
        ("Mid-point theorem relates a segment joining midpoints to the", *opt("third side of a triangle", "circle radius", "mean", "probability"), "The segment is parallel to the third side."),
        ("Equal chords of a circle are", *opt("equidistant from the centre", "always diameters", "never parallel", "outside circle"), "Equal chords have equal distances from the centre."),
        ("Opposite angles of a cyclic quadrilateral are", *opt("supplementary", "equal always", "zero", "acute always"), "They add to 180 degrees."),
        ("Figures on the same base and between same parallels have same", *opt("height", "perimeter always", "number of sides", "radius"), "The distance between parallels is common."),
        ("A construction should use", *opt("given measurements accurately", "rough guessing", "only colour", "only mental math"), "Practical geometry depends on accurate steps."),
    ]
    if chapter == "Lines and Angles":
        common[4] = ("A linear pair of angles is", *opt("supplementary", "always equal", "always acute", "always zero"), "A linear pair adds to 180 degrees.")
    if chapter == "Circles":
        common[0] = ("A radius joins centre to", *opt("a point on the circle", "outside point only", "two chords", "an axis"), "Radius is the distance from centre to circle.")
    if chapter == "Constructions":
        common[0] = ("The perpendicular bisector of a segment makes", *opt("90 degrees and two equal parts", "60 degrees only", "a circle only", "a graph"), "It is perpendicular and bisects the segment.")
    return common


def mensuration_bank(s):
    return [
        ("Total surface area of a cuboid is", *opt("2(lb+bh+hl)", "lbh", "4πr^2", "πr^2h"), "Cuboid TSA is 2(lb+bh+hl)."),
        ("Volume of a cuboid is", *opt("lbh", "2(lb+bh+hl)", "πr^2", "4/3πr^3"), "Volume uses three dimensions."),
        ("Surface area of a cube of side a is", *opt("6a^2", "a^3", "4a", "2a^2"), "A cube has six square faces."),
        ("Volume of a cube of side a is", *opt("a^3", "6a^2", "4a", "3a"), "Cube volume is side cubed."),
        ("Curved surface area of cylinder is", *opt("2πrh", "πr^2h", "4πr^2", "1/3πr^2h"), "Cylinder CSA is 2πrh."),
        ("Volume of a cylinder is", *opt("πr^2h", "2πrh", "πrl", "4/3πr^3"), "Base area times height gives πr^2h."),
        ("Curved surface area of cone is", *opt("πrl", "πr^2h", "2πrh", "4πr^2"), "Cone CSA uses slant height l."),
        ("Volume of a cone is", *opt("1/3πr^2h", "πr^2h", "2πrh", "πrl"), "Cone volume is one-third cylinder of same base and height."),
        ("Surface area of a sphere is", *opt("4πr^2", "πr^2", "2πrh", "πr^2h"), "Sphere surface area is 4πr^2."),
        ("Volume of a sphere is", *opt("4/3πr^3", "4πr^2", "πr^2h", "1/3πr^2h"), "Sphere volume is 4/3πr^3."),
        ("A right circular cylinder has bases that are", *opt("circles", "squares", "triangles", "parallelograms"), "Cylinder bases are circular."),
        ("Slant height is used in surface area of a", *opt("cone", "cuboid", "cube", "sphere only"), "Cone curved surface area uses slant height."),
        ("Volume is measured in", *opt("cubic units", "square units", "degrees", "percent"), "Volume measures space occupied."),
        ("Surface area is measured in", *opt("square units", "cubic units", "linear units only", "radians"), "Surface area covers outer surface."),
    ]


def statistics_bank(s):
    return [
        ("Raw data means", *opt("data as collected", "only mean", "only graph", "only median"), "Raw data is unorganised collected data."),
        ("Class mark is", *opt("midpoint of a class interval", "highest frequency", "sum of all data", "range only"), "Class mark is average of limits."),
        ("Mean equals", *opt("sum of observations / number of observations", "middle value always", "most frequent value", "largest-smallest"), "This is arithmetic mean."),
        ("Median is", *opt("middle value", "most frequent value", "sum of data", "class width"), "Median is central positional value."),
        ("Mode is", *opt("most frequent value", "middle value", "average", "smallest value"), "Mode occurs most often."),
        ("A histogram represents", *opt("grouped frequency data", "only equations", "only constructions", "only circles"), "Histograms display grouped data."),
        ("A bar graph uses", *opt("bars", "arcs only", "solids", "equations only"), "Bars represent quantities."),
        ("Frequency means", *opt("number of times an observation occurs", "largest observation", "smallest observation", "sum divided by count"), "Frequency counts occurrence."),
        (f"Mean of {s}, {s+2}, {s+4} is", *opt(str(s+2), str(s), str(s+4), str(3*s+6)), "The average of equally spaced values is the middle value."),
        ("Range equals", *opt("highest value - lowest value", "mean + median", "frequency x class mark", "mode - mean"), "Range measures spread."),
        ("A frequency polygon can be related to", *opt("histogram", "sphere", "cone", "triangle congruence only"), "Frequency polygons are graph forms for distributions."),
        ("Grouped data is organised into", *opt("class intervals", "radii", "axioms", "chords only"), "Class intervals group observations."),
        ("Central tendency refers to", *opt("typical central value", "outer surface", "angle sum", "coordinate axis"), "Mean, median and mode are central measures."),
        ("The mode of 2,3,3,4,5 is", *opt("3", "2", "4", "5"), "3 occurs most often."),
    ]


def probability_bank(s):
    return [
        ("Experimental probability is based on", *opt("actual trials", "only formulas without trials", "surface area", "coordinates"), "Class 9 introduces experimental probability."),
        ("Probability of an impossible event is", *opt("0", "1", "2", "10"), "Impossible events never occur."),
        ("Probability of a certain event is", *opt("1", "0", "1/2", "2"), "Certain events always occur."),
        ("Probability lies between", *opt("0 and 1", "1 and 2", "-5 and 5 only", "10 and 100"), "Probability values range from 0 to 1."),
        ("In a coin toss, possible outcomes are", *opt("Head and Tail", "1 and 2", "Red and Blue", "0 and 6"), "A coin has two outcomes."),
        ("For a die, probability of getting 4 experimentally is close to", *opt("1/6", "1/2", "1", "0"), "A fair die has six equally likely outcomes theoretically."),
        ("An event is a", *opt("collection of outcomes", "solid shape", "polynomial degree", "coordinate axis"), "Events consist of outcomes."),
        ("More trials usually make experimental probability", *opt("more stable", "always zero", "always one", "meaningless"), "More trials often give better estimates."),
        ("If an event happens 20 times in 100 trials, experimental probability is", *opt("1/5", "1/2", "5", "20"), "20/100 = 1/5."),
        ("Probability of an event cannot be", *opt("greater than 1", "0", "1/2", "1"), "Probability values do not exceed 1."),
        ("A trial is", *opt("one performance of an experiment", "a theorem", "a graph axis", "a chord"), "Each repetition is a trial."),
        ("Outcome means", *opt("result of a trial", "mean of data", "area of circle", "factor of polynomial"), "An outcome is the result observed."),
        ("If an event never occurs in trials, its experimental probability is", *opt("0", "1", "2", "10"), "Frequency 0 gives probability 0."),
        ("Experimental probability is calculated as", *opt("number of times event occurs / total trials", "total trials / event occurs always", "mean + mode", "area / volume"), "This is the experimental probability formula."),
    ]


def make_module(module_id, chapter, topic):
    diff = DIFFICULTY[chapter]
    timer = {"Easy": 30, "Medium": 45, "Hard": 60}[diff]
    return {
        "module_id": module_id,
        "topic_name": topic,
        "explanation": EXPLANATIONS[chapter],
        "difficulty": diff,
        "total_timer_minutes": 14 if diff == "Hard" else 10,
        "questions": [
            {
                "question_id": i + 1,
                "question_text": f"{topic}: {item[0]}",
                "options": item[1],
                "correct_answer": item[2],
                "rationale": item[3],
                "timer_per_question_seconds": timer,
            }
            for i, item in enumerate(bank(chapter, module_id))
        ],
    }


def build():
    chapters = []
    module_id = 1
    for chapter_name, topics in CHAPTERS:
        modules = []
        for topic in topics:
            modules.append(make_module(module_id, chapter_name, topic))
            module_id += 1
        chapters.append({"chapter_name": chapter_name, "modules": modules})
    return {
        "class": "9",
        "board": "CBSE",
        "subject": "Mathematics",
        "source_pdf": "ncert-books-for-class-9-maths.pdf",
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
