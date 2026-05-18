import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "class11_cbse_ncert_duolingo_curriculum_2500plus.json"


CHAPTERS = [
    ("Sets", ["Set Basics", "Roster Form", "Set-builder Form", "Empty Set", "Finite and Infinite Sets", "Equal Sets", "Subsets", "Power Set", "Universal Set", "Venn Diagrams", "Union, Intersection and Complement"]),
    ("Relations and Functions", ["Cartesian Product", "Ordered Pairs", "Relations", "Domain and Range", "Function Basics", "Function Notation", "Real-valued Functions", "Identity and Constant Functions", "Polynomial and Rational Functions", "Modulus and Signum Functions", "Function Applications"]),
    ("Trigonometric Functions", ["Angles and Radian Measure", "Degree and Radian Conversion", "Trigonometric Functions", "Signs in Quadrants", "Trigonometric Values", "Allied Angles", "Sum and Difference Formulae", "Double Angle Ideas", "Trigonometric Identities", "Trigonometric Equations", "General Solutions"]),
    ("Principle of Mathematical Induction", ["Motivation for Induction", "Induction Statement", "Base Case", "Inductive Hypothesis", "Inductive Step", "Natural Number Proofs", "Series Proofs", "Divisibility Proofs", "Inequality Proofs", "Pattern Proofs", "Induction Applications"]),
    ("Complex Numbers and Quadratic Equations", ["Need for Complex Numbers", "Imaginary Unit", "Algebra of Complex Numbers", "Addition and Subtraction", "Multiplication", "Division", "Modulus", "Conjugate", "Argand Plane", "Polar Form", "Quadratic Equations"]),
    ("Linear Inequalities", ["Inequality Basics", "Number Line Representation", "One-variable Inequalities", "Solving Linear Inequalities", "Compound Inequalities", "Graphical Representation", "Two-variable Inequalities", "Half-planes", "System of Inequalities", "Feasible Region", "Inequality Applications"]),
    ("Permutations and Combinations", ["Counting Principle", "Factorial Notation", "Permutations Basics", "Permutations of Distinct Objects", "Permutations with Restrictions", "Circular Arrangement Ideas", "Combinations Basics", "nCr Formula", "Relation between nPr and nCr", "Selection Problems", "Counting Applications"]),
    ("Binomial Theorem", ["Binomial Expansion", "Positive Integral Indices", "Binomial Coefficients", "Pascal Triangle", "General Term", "Middle Term", "Coefficient Problems", "Term Independent of x", "Expansion Applications", "Approximation Ideas", "Binomial Patterns"]),
    ("Sequences and Series", ["Sequence Basics", "Series Basics", "Arithmetic Progression", "nth Term of AP", "Sum of AP", "Arithmetic Mean", "Geometric Progression", "nth Term of GP", "Sum of GP", "AM and GM", "Special Series"]),
    ("Straight Lines", ["Slope of a Line", "Angle Between Lines", "Point-slope Form", "Two-point Form", "Slope-intercept Form", "Intercept Form", "Normal Form", "General Equation", "Distance of Point from Line", "Parallel and Perpendicular Lines", "Line Applications"]),
    ("Conic Sections", ["Sections of a Cone", "Circle", "Standard Circle Equation", "Parabola", "Parabola Terms", "Ellipse", "Ellipse Terms", "Hyperbola", "Hyperbola Terms", "Eccentricity", "Conic Applications"]),
    ("Introduction to Three Dimensional Geometry", ["3D Coordinate Axes", "Coordinate Planes", "Octants", "Coordinates of a Point", "Distance Formula in 3D", "Section Formula in 3D", "Midpoint in 3D", "Points on Axes", "Points on Planes", "3D Geometry Applications", "Spatial Reasoning"]),
    ("Limits and Derivatives", ["Intuitive Idea of Derivative", "Limit Basics", "Algebra of Limits", "Standard Limits", "Limits of Trigonometric Functions", "Derivative Basics", "Derivative from First Principle", "Derivative Rules", "Derivatives of Polynomial Functions", "Derivatives of Trigonometric Functions", "Derivative Applications"]),
    ("Mathematical Reasoning", ["Statements", "Truth Values", "Negation", "Compound Statements", "And Statements", "Or Statements", "Implications", "Converse and Contrapositive", "Special Words", "Validating Statements", "Reasoning Applications"]),
    ("Statistics", ["Dispersion Basics", "Range", "Mean Deviation from Mean", "Mean Deviation from Median", "Variance", "Standard Deviation", "Grouped Data", "Coefficient of Variation", "Comparing Distributions", "Frequency Distribution Analysis", "Statistics Applications"]),
    ("Probability", ["Random Experiments", "Sample Space", "Events", "Types of Events", "Algebra of Events", "Axiomatic Probability", "Probability of Complement", "Mutually Exclusive Events", "Exhaustive Events", "Addition Rule", "Probability Applications"]),
]


EXPLAIN = {
    "Sets": "Sets are well-defined collections of objects. They can be written in roster form, set-builder form, or shown using Venn diagrams. Operations like union, intersection and complement help compare collections. Think of sets as labelled boxes: each object either belongs inside or does not.",
    "Relations and Functions": "Relations connect elements of one set with elements of another through ordered pairs. A function is a special relation where each input has exactly one output. This chapter builds the language for modelling rules, graphs and real-world input-output situations.",
    "Trigonometric Functions": "Trigonometric functions connect angles with numbers. Class 11 extends trigonometry from right triangles to all real angles using radians, quadrants, identities and equations. It is like a circular language for describing rotation, waves and periodic patterns.",
    "Principle of Mathematical Induction": "Mathematical induction proves statements for all natural numbers. First prove the starting case, then show that if one case is true, the next case must be true. It works like a row of dominoes: one push starts an endless chain.",
    "Complex Numbers and Quadratic Equations": "Complex numbers extend the number system using i, where i squared equals -1. They help solve equations that have no real roots. Complex numbers can be added, multiplied, represented on the Argand plane and used in quadratic equations.",
    "Linear Inequalities": "Inequalities compare quantities using signs like less than and greater than. Solutions may be intervals on a number line or regions in a plane. Unlike equations, inequalities often describe a whole range of possible answers.",
    "Permutations and Combinations": "Counting methods help answer how many arrangements or selections are possible. Permutations care about order, while combinations do not. Factorials, nPr and nCr are powerful shortcuts for counting without listing every possibility.",
    "Binomial Theorem": "The binomial theorem expands powers of expressions like (a+b)^n. Coefficients follow Pascal's triangle and the general term helps find any required term directly. It turns long multiplication into a neat pattern.",
    "Sequences and Series": "A sequence is an ordered list and a series is the sum of its terms. Arithmetic and geometric progressions describe common patterns. Their formulas help find terms and sums quickly, which is useful in growth, savings and repeated patterns.",
    "Straight Lines": "Straight lines can be described by slope, intercepts and equations. Different forms of a line suit different information. The chapter connects coordinate geometry with algebra, helping students measure inclination, distance and relationships between lines.",
    "Conic Sections": "Conic sections come from slicing a cone: circles, parabolas, ellipses and hyperbolas. Each has a standard equation and geometric meaning. These curves appear in mirrors, orbits, bridges and many natural paths.",
    "Introduction to Three Dimensional Geometry": "Three-dimensional geometry locates points in space using x, y and z coordinates. Axes, planes, octants, distance and section formula extend coordinate geometry beyond a flat page into spatial thinking.",
    "Limits and Derivatives": "Limits describe what a function approaches, and derivatives describe rate of change. This chapter introduces calculus through slopes, first principles and derivative rules. It is the mathematics of motion, change and instant behaviour.",
    "Mathematical Reasoning": "Mathematical reasoning studies statements, truth values and logical connections. Words like and, or, implies, every and there exists must be handled carefully. It trains students to decide when an argument is valid.",
    "Statistics": "Statistics measures how data varies. Range, mean deviation, variance and standard deviation describe spread, not just centre. These tools help compare consistency between data sets, such as marks, heights or production values.",
    "Probability": "Probability studies chance using sample spaces and events. The axiomatic approach gives rules for assigning probabilities. Events may be complementary, mutually exclusive or exhaustive, and probability values always lie between 0 and 1.",
}


DIFF = {name: ("Medium" if name in {"Sets", "Relations and Functions", "Mathematical Reasoning", "Statistics", "Probability"} else "Hard") for name, _ in CHAPTERS}


def pack(answer, *wrong):
    return [str(answer), *[str(w) for w in wrong]][:4], str(answer)


def bank(chapter, seed):
    n = seed % 7 + 2
    if chapter == "Sets":
        return [
            ("A set is a", *pack("well-defined collection", "vague collection", "single number only", "graph only"), "A set must be well-defined."),
            ("The symbol for belongs to is", *pack("in", "not in", "subset", "empty"), "The membership idea is denoted by belongs to; in JSON text we write 'in'."),
            ("The empty set has", *pack("no element", "one element", "two elements", "infinite elements always"), "The empty set contains no element."),
            ("Roster form lists", *pack("all elements", "only property", "only diagram", "only complement"), "Roster form writes elements inside braces."),
            ("Set-builder form describes", *pack("a common property", "only order", "only graph", "only count"), "Set-builder form uses a defining property."),
            ("A finite set has", *pack("countable limited elements", "unlimited elements", "no elements always", "only variables"), "Finite sets have a definite number of elements."),
            ("Equal sets have", *pack("same elements", "same order only", "same name only", "same diagram colour"), "Order does not matter, elements do."),
            ("If every element of A is in B, A is a", *pack("subset of B", "universal set always", "empty set always", "power set"), "This is the definition of subset."),
            ("Power set contains", *pack("all subsets", "all elements only", "only empty set", "only universal set"), "Power set is the set of all subsets."),
            ("Universal set contains", *pack("all objects under discussion", "no objects", "only numbers", "only vowels"), "Universal set is the reference set."),
            ("A union B contains elements in", *pack("A or B or both", "A and B only", "A but not B", "neither A nor B"), "Union combines both sets."),
            ("A intersection B contains elements in", *pack("both A and B", "A only", "B only", "neither"), "Intersection keeps common elements."),
            ("Complement of A contains elements", *pack("in universal set but not A", "only in A", "in A and B", "in empty set only"), "Complement is outside A within U."),
            ("If A has " + str(n) + " elements, power set has", *pack(str(2**n), str(n), str(n*n), str(n+2)), "A set with n elements has 2^n subsets."),
            ("Venn diagrams use", *pack("closed curves", "only straight lines", "only axes", "only tables"), "Venn diagrams show sets with regions."),
        ]
    if chapter == "Relations and Functions":
        return [
            ("An ordered pair is written as", *pack("(a,b)", "{a,b}", "ab only", "a:b only"), "Order matters in ordered pairs."),
            ("Cartesian product A x B contains", *pack("ordered pairs", "only common elements", "only subsets", "only functions"), "A x B pairs each element of A with each element of B."),
            ("If |A|=2 and |B|=3, |A x B| is", *pack("6", "5", "3", "2"), "Cardinality multiplies."),
            ("A relation from A to B is a subset of", *pack("A x B", "A union B", "A intersection B", "power set of A only"), "Relations are sets of ordered pairs."),
            ("Domain contains", *pack("first components", "second components", "all unused elements", "only numbers"), "Domain is the set of inputs."),
            ("Range contains", *pack("actual outputs", "all possible inputs", "only first components", "empty set always"), "Range is made of second components used."),
            ("A function maps each input to", *pack("exactly one output", "two outputs always", "no output", "all outputs"), "This is the key function rule."),
            ("Identity function sends x to", *pack("x", "0", "1", "-x"), "Identity leaves input unchanged."),
            ("Constant function sends every input to", *pack("same value", "itself", "different values always", "no value"), "The output is fixed."),
            ("The graph of y=x is", *pack("identity function", "constant function", "empty relation", "modulus only"), "y=x represents identity."),
            ("The modulus function gives", *pack("non-negative output", "negative output always", "zero only", "undefined output"), "Absolute value is never negative."),
            ("A real-valued function has outputs in", *pack("real numbers", "only natural numbers", "only empty set", "only ordered pairs"), "Real-valued means range is real."),
            ("If f(x)=x+2, f(" + str(n) + ") is", *pack(str(n+2), str(n), str(n-2), str(2*n)), "Substitute x=n."),
            ("A vertical input having two outputs violates", *pack("function rule", "set rule", "union rule", "complement rule"), "One input cannot have two outputs in a function."),
            ("Function notation f(x) means", *pack("value of function at x", "f times x always", "only a set", "only a coordinate"), "f(x) denotes output for input x."),
        ]
    if chapter == "Trigonometric Functions":
        return trig_bank(n)
    if chapter == "Principle of Mathematical Induction":
        return induction_bank(n)
    if chapter == "Complex Numbers and Quadratic Equations":
        return complex_bank(n)
    if chapter == "Linear Inequalities":
        return inequalities_bank(n)
    if chapter == "Permutations and Combinations":
        return counting_bank(n)
    if chapter == "Binomial Theorem":
        return binomial_bank(n)
    if chapter == "Sequences and Series":
        return sequences_bank(n)
    if chapter == "Straight Lines":
        return lines_bank(n)
    if chapter == "Conic Sections":
        return conics_bank(n)
    if chapter == "Introduction to Three Dimensional Geometry":
        return geometry3d_bank(n)
    if chapter == "Limits and Derivatives":
        return calculus_bank(n)
    if chapter == "Mathematical Reasoning":
        return reasoning_bank(n)
    if chapter == "Statistics":
        return statistics_bank(n)
    if chapter == "Probability":
        return probability_bank(n)
    raise ValueError(chapter)


def trig_bank(n):
    return [
        ("180 degrees equals", *pack("pi radians", "2 pi radians", "pi/2 radians", "1 radian"), "A straight angle is pi radians."),
        ("1 radian is the angle subtended by arc length", *pack("equal to radius", "twice radius", "zero", "diameter squared"), "Radian measure is arc/radius."),
        ("sin x has period", *pack("2 pi", "pi", "pi/2", "1"), "Sine repeats every 2 pi."),
        ("tan x has period", *pack("pi", "2 pi", "pi/2", "4 pi"), "Tangent repeats every pi."),
        ("sin^2 x + cos^2 x equals", *pack("1", "0", "tan x", "2"), "This is the basic identity."),
        ("sin(-x) equals", *pack("-sin x", "sin x", "cos x", "-cos x"), "Sine is odd."),
        ("cos(-x) equals", *pack("cos x", "-cos x", "sin x", "-sin x"), "Cosine is even."),
        ("sin(A+B) equals", *pack("sinA cosB + cosA sinB", "sinA sinB", "cosA cosB", "tanA+tanB"), "This is the sum formula."),
        ("cos(A+B) equals", *pack("cosA cosB - sinA sinB", "cosA cosB + sinA sinB", "sinA cosB", "tanA tanB"), "This is the cosine sum formula."),
        ("tan(A+B) equals", *pack("(tanA+tanB)/(1-tanA tanB)", "tanA+tanB", "tanA tanB", "1-tanA tanB"), "This is the tangent sum formula."),
        ("sin 0 equals", *pack("0", "1", "-1", "1/2"), "Sine of zero is zero."),
        ("cos 0 equals", *pack("1", "0", "-1", "1/2"), "Cosine of zero is one."),
        ("General solution of sin x = 0 is", *pack("x=n pi", "x=2n only", "x=pi/2", "x=1"), "Sine is zero at integral multiples of pi."),
        ("In quadrant II, sine is", *pack("positive", "negative", "zero always", "undefined"), "Sine is positive in quadrants I and II."),
        ("In quadrant III, tangent is", *pack("positive", "negative", "zero always", "undefined"), "Tangent is positive in quadrants I and III."),
    ]


def induction_bank(n):
    return [
        ("Mathematical induction proves statements for", *pack("natural numbers", "only real numbers", "only triangles", "only sets"), "Induction works over natural numbers."),
        ("First step of induction is", *pack("base case", "last case", "graph case", "contradiction only"), "The base case starts the proof."),
        ("Inductive hypothesis assumes truth for", *pack("n=k", "n=0 always", "all real numbers", "no value"), "We assume the statement for k."),
        ("Inductive step proves truth for", *pack("n=k+1", "n=k-1", "n=1 only", "n=0 only"), "The next case must follow."),
        ("Induction is often compared to", *pack("falling dominoes", "circle area", "random guessing", "coordinate axes"), "One true case triggers the next."),
        ("To prove 1+2+...+n=n(n+1)/2, base case n=1 gives", *pack("1=1", "0=1", "2=1", "1=2"), "Both sides equal 1."),
        ("If P(k) implies P(k+1), this is the", *pack("inductive step", "base case", "definition", "counterexample"), "It links consecutive cases."),
        ("A proof by induction needs", *pack("base case and inductive step", "only base case", "only examples", "only diagram"), "Both parts are necessary."),
        ("The variable in induction usually belongs to", *pack("N", "only complex numbers", "empty set", "only intervals"), "Induction is for natural-number-indexed statements."),
        ("Checking first 5 cases alone is", *pack("not a proof for all n", "always complete proof", "same as induction", "invalid for any case"), "Examples do not prove all cases."),
        ("Induction can prove divisibility statements like", *pack("expression divisible by an integer", "angle construction only", "probability always", "circle tangent only"), "Divisibility is a common induction topic."),
        ("For sum of first n odd numbers, result is", *pack("n^2", "n(n+1)/2", "2n", "n^3"), "1+3+...+(2n-1)=n^2."),
        ("The induction assumption should be used to prove", *pack("next case", "previous chapter", "only base case", "a diagram"), "P(k) helps prove P(k+1)."),
        ("Induction is a form of", *pack("deductive proof", "measurement", "estimation", "survey"), "It is a logical proof method."),
        ("If base case fails, induction proof is", *pack("incomplete", "always true", "stronger", "not needed"), "The chain cannot start without base case."),
    ]


def complex_bank(n):
    return [
        ("i^2 equals", *pack("-1", "1", "0", "i"), "The imaginary unit satisfies i^2=-1."),
        ("sqrt(-1) is denoted by", *pack("i", "e", "pi", "z"), "i is the imaginary unit."),
        ("A complex number is written as", *pack("a+ib", "a/b only", "(a,b,c)", "ax+b=0"), "Standard form is a+ib."),
        ("Real part of 3+4i is", *pack("3", "4", "i", "7"), "The real part is 3."),
        ("Imaginary part of 3+4i is", *pack("4", "3", "4i only", "7"), "The imaginary part coefficient is 4."),
        ("Conjugate of a+ib is", *pack("a-ib", "-a+ib", "b+ia", "-a-ib"), "Change sign of imaginary part."),
        ("Modulus of 3+4i is", *pack("5", "7", "1", "25"), "sqrt(3^2+4^2)=5."),
        ("(2+i)+(3+4i) equals", *pack("5+5i", "5+4i", "6+4i", "1+3i"), "Add real and imaginary parts separately."),
        ("(1+i)(1-i) equals", *pack("2", "0", "2i", "-2"), "It is 1-i^2=2."),
        ("Argand plane represents complex numbers as", *pack("points", "sets only", "probabilities", "inequalities"), "a+ib is plotted as (a,b)."),
        ("Purely real number has imaginary part", *pack("0", "1", "-1", "i"), "No imaginary component means b=0."),
        ("Purely imaginary number has real part", *pack("0", "1", "-1", "i"), "No real component means a=0."),
        ("Quadratic x^2+1=0 has roots", *pack("i and -i", "1 and -1", "0 and 1", "2 and -2"), "x^2=-1 gives x=+-i."),
        ("Polar form uses modulus and", *pack("argument", "mean", "variance", "subset"), "Polar form uses r and theta."),
        ("Division by complex number often uses", *pack("conjugate", "Venn diagram", "induction base", "factorial"), "Multiplying by conjugate removes imaginary denominator."),
    ]


def inequalities_bank(n):
    return [
        ("The solution of x > 3 is shown on number line to the", *pack("right of 3", "left of 3", "only at 3", "nowhere"), "Greater values lie to the right."),
        ("Multiplying an inequality by a negative number", *pack("reverses sign", "keeps sign", "removes variable", "makes equality"), "The inequality direction changes."),
        ("x < 5 includes numbers", *pack("less than 5", "greater than 5", "equal to 5 only", "all numbers"), "The symbol means less than."),
        ("x <= 5 means x is", *pack("less than or equal to 5", "only less than 5", "only greater than 5", "not comparable"), "The equality case is included."),
        ("Open circle on number line means endpoint is", *pack("not included", "included", "largest always", "smallest always"), "Open dot excludes endpoint."),
        ("Closed circle on number line means endpoint is", *pack("included", "excluded", "infinite", "empty"), "Closed dot includes endpoint."),
        ("A linear inequality in two variables represents a", *pack("half-plane", "single point always", "circle", "parabola"), "A boundary line divides the plane into half-planes."),
        ("The boundary of ax+by<c is", *pack("ax+by=c", "ax+by=0 only", "x=0 only", "y=0 only"), "Replace inequality with equality."),
        ("A system of inequalities may have solution as", *pack("common region", "only one integer", "only empty set always", "only a line"), "Solutions satisfy all inequalities."),
        ("The feasible region is", *pack("common solution region", "outside every line", "only origin", "only x-axis"), "It is the intersection of solution regions."),
        ("For x+2 > 5, x is", *pack("greater than 3", "less than 3", "equal to 3 only", "less than -3"), "Subtract 2 from both sides."),
        ("For 2x <= 8, x is", *pack("<= 4", ">= 4", "<= 8", ">= 8"), "Divide by positive 2."),
        ("For -x < 2, x is", *pack("> -2", "< -2", "> 2", "< 2"), "Multiplying by -1 reverses sign."),
        ("The graph of y > x is region", *pack("above line y=x", "below line y=x", "on x-axis only", "on y-axis only"), "Greater y-values lie above the line."),
        ("A strict inequality uses", *pack("< or >", "<= or >=", "= only", "not equal only"), "Strict inequalities exclude equality."),
    ]


def counting_bank(n):
    return [
        ("n! means", *pack("n(n-1)...1", "n+n", "n^2", "n/2"), "Factorial is descending product."),
        ("0! equals", *pack("1", "0", "undefined", "-1"), "By definition, 0!=1."),
        ("Fundamental principle of counting multiplies choices when tasks are", *pack("successive", "same only", "impossible", "unordered only"), "Independent successive choices multiply."),
        ("Permutation means", *pack("arrangement", "selection", "probability", "mean"), "Permutations care about order."),
        ("Combination means", *pack("selection", "arrangement", "ordered pair", "angle"), "Combinations ignore order."),
        ("nPr formula is", *pack("n!/(n-r)!", "n!/r!(n-r)!", "r!/n!", "n+r"), "This is permutation formula."),
        ("nCr formula is", *pack("n!/(r!(n-r)!)", "n!/(n-r)!", "n+r", "nr"), "This is combination formula."),
        ("5! equals", *pack("120", "25", "20", "10"), "5x4x3x2x1=120."),
        ("Number of arrangements of 3 distinct objects is", *pack("6", "3", "9", "1"), "3! = 6."),
        ("Choosing 2 from 5 is", *pack("10", "20", "5", "2"), "5C2=10."),
        ("nC0 equals", *pack("1", "0", "n", "2n"), "There is one way to choose nothing."),
        ("nCn equals", *pack("1", "0", "n", "n!"), "There is one way to choose all."),
        ("nCr equals", *pack("nC(n-r)", "nPr", "rCn", "n! always"), "This is symmetry of combinations."),
        ("Arranging letters of ABC gives", *pack("6 ways", "3 ways", "9 ways", "1 way"), "There are 3! arrangements."),
        ("If order matters, use", *pack("permutation", "combination", "mean", "variance"), "Order-sensitive counting is permutation."),
    ]


def binomial_bank(n):
    return [
        ("(a+b)^n expansion is given by", *pack("binomial theorem", "Pythagoras theorem", "Euclid lemma", "Bayes rule"), "The chapter is Binomial Theorem."),
        ("Coefficient pattern appears in", *pack("Pascal triangle", "Venn diagram", "Argand plane", "histogram"), "Pascal triangle gives binomial coefficients."),
        ("General term in (a+b)^n is", *pack("T(r+1)=nCr a^(n-r)b^r", "nPr", "a+b", "r/n"), "This is the general term."),
        ("Middle term depends on whether n is", *pack("even or odd", "prime only", "negative", "zero only"), "Number of terms changes with parity of n."),
        ("Number of terms in (a+b)^n is", *pack("n+1", "n", "2n", "n-1"), "Powers run from 0 to n."),
        ("Sum of binomial coefficients in (a+b)^n is", *pack("2^n", "n^2", "n!", "0"), "Put a=b=1."),
        ("Coefficient of a^n in (a+b)^n is", *pack("1", "n", "n^2", "0"), "First term coefficient is 1."),
        ("Coefficient of a^(n-1)b is", *pack("n", "1", "n^2", "2^n"), "It is nC1=n."),
        ("(1+x)^2 equals", *pack("1+2x+x^2", "1+x^2", "2+2x", "1-x^2"), "Use binomial expansion."),
        ("(a+b)^3 has coefficient of a^2b equal to", *pack("3", "1", "2", "6"), "3C1=3."),
        ("The term independent of x has power of x", *pack("0", "1", "n", "-1 always"), "Independent means x^0."),
        ("nC0 equals", *pack("1", "0", "n", "n!"), "First binomial coefficient is 1."),
        ("nCn equals", *pack("1", "0", "n", "n!"), "Last binomial coefficient is 1."),
        ("Binomial theorem in this chapter is for", *pack("positive integral indices", "all real indices primarily", "only n=0", "only negative n"), "NCERT section focuses on positive integral indices."),
        ("Coefficients in expansion are", *pack("combinations", "permutations only", "means", "standard deviations"), "Binomial coefficients are nCr."),
    ]


def sequences_bank(n):
    return [
        ("A sequence is", *pack("ordered list", "unordered set", "single equation", "circle"), "Order matters in sequences."),
        ("A series is", *pack("sum of terms", "only first term", "only common difference", "empty set"), "Series adds sequence terms."),
        ("AP has constant", *pack("difference", "ratio", "variance", "angle"), "Arithmetic progression uses common difference."),
        ("GP has constant", *pack("ratio", "difference", "sum", "median"), "Geometric progression uses common ratio."),
        ("nth term of AP is", *pack("a+(n-1)d", "ar^(n-1)", "n/2(a+l)", "a/(n-1)d"), "AP term formula."),
        ("nth term of GP is", *pack("ar^(n-1)", "a+(n-1)d", "a+nd", "nr"), "GP term formula."),
        ("Sum of first n AP terms is", *pack("n/2[2a+(n-1)d]", "ar^n", "a+(n-1)d", "n!"), "AP sum formula."),
        ("Sum of first n GP terms for r not 1 is", *pack("a(r^n-1)/(r-1)", "a+(n-1)d", "n/2(a+l)", "nCr"), "This is a GP sum form."),
        ("AM of a and b is", *pack("(a+b)/2", "sqrt(ab)", "ab", "a/b"), "Arithmetic mean is average."),
        ("GM of a and b is", *pack("sqrt(ab)", "(a+b)/2", "a-b", "a+b"), "Geometric mean is square root of product."),
        ("For positive a,b, AM is", *pack(">= GM", "< GM always", "=0 always", "not defined"), "AM-GM relation."),
        ("Sequence 2,4,6,8 is", *pack("AP", "GP only", "neither", "constant"), "Difference is 2."),
        ("Sequence 3,6,12,24 is", *pack("GP", "AP only", "neither", "constant"), "Ratio is 2."),
        ("Sum 1^2+2^2+...+n^2 equals", *pack("n(n+1)(2n+1)/6", "n(n+1)/2", "n^2", "2^n"), "This is a special series."),
        ("Sum 1+2+...+n equals", *pack("n(n+1)/2", "n^2", "2^n", "n!"), "Standard natural number sum."),
    ]


def lines_bank(n):
    return [
        ("Slope of a line measures", *pack("inclination", "area", "volume", "probability"), "Slope shows steepness."),
        ("Slope of line through (x1,y1),(x2,y2) is", *pack("(y2-y1)/(x2-x1)", "(x2-x1)/(y2-y1)", "x1+x2", "y1+y2"), "Rise over run."),
        ("Slope of horizontal line is", *pack("0", "1", "undefined", "-1"), "No rise means slope 0."),
        ("Slope of vertical line is", *pack("undefined", "0", "1", "-1"), "Run is zero, so slope undefined."),
        ("Point-slope form is", *pack("y-y1=m(x-x1)", "y=mx+c", "x/a+y/b=1", "ax+by+c=0"), "Uses a point and slope."),
        ("Slope-intercept form is", *pack("y=mx+c", "y-y1=m(x-x1)", "x/a+y/b=1", "ax=by"), "c is y-intercept."),
        ("Intercept form is", *pack("x/a+y/b=1", "y=mx+c", "y-y1=m(x-x1)", "x=0"), "Uses x- and y-intercepts."),
        ("General form is", *pack("Ax+By+C=0", "y=mx+c only", "x/a+y/b", "m=y/x only"), "This is the general equation of a line."),
        ("Parallel lines have", *pack("equal slopes", "product slopes -1", "zero slopes only", "undefined always"), "Parallel non-vertical lines have same slope."),
        ("Perpendicular lines have slope product", *pack("-1", "1", "0", "2"), "For non-vertical perpendicular lines, m1m2=-1."),
        ("Distance of point from line uses", *pack("|Ax1+By1+C|/sqrt(A^2+B^2)", "mx+c", "sqrt(x^2+y^2)", "nCr"), "This is the distance formula."),
        ("Angle between lines depends on", *pack("slopes", "intercepts only", "area", "variance"), "Slope formula gives angle."),
        ("Line x=a is", *pack("vertical", "horizontal", "slant", "circle"), "x is fixed."),
        ("Line y=b is", *pack("horizontal", "vertical", "circle", "parabola"), "y is fixed."),
        ("Slope of line y=" + str(n) + "x+1 is", *pack(str(n), "1", str(n+1), "0"), "In y=mx+c, m is slope."),
    ]


def conics_bank(n):
    return [
        ("A circle is set of points at fixed distance from", *pack("centre", "directrix", "focus only", "axis only"), "Circle definition."),
        ("Standard circle equation is", *pack("x^2+y^2=r^2", "y^2=4ax", "x^2/a^2+y^2/b^2=1", "xy=1"), "Circle centred at origin."),
        ("A parabola is set of points equidistant from focus and", *pack("directrix", "centre", "minor axis", "asymptote"), "Parabola definition."),
        ("Standard parabola y^2=4ax opens", *pack("right if a>0", "left if a>0", "up always", "down always"), "Positive a opens right."),
        ("Ellipse has sum of distances from two foci", *pack("constant", "zero", "variable always", "infinite"), "Ellipse definition."),
        ("Hyperbola has difference of distances from two foci", *pack("constant", "sum constant", "zero always", "undefined"), "Hyperbola definition."),
        ("Eccentricity of circle is", *pack("0", "1", ">1", "<0"), "Circle has e=0."),
        ("Eccentricity of parabola is", *pack("1", "0", ">1", "<1"), "Parabola has e=1."),
        ("Ellipse eccentricity is", *pack("between 0 and 1", "equal 1", "greater than 1", "negative"), "Ellipse has 0<e<1."),
        ("Hyperbola eccentricity is", *pack(">1", "0", "between 0 and 1", "equal 1 always"), "Hyperbola has e>1."),
        ("Major axis belongs to", *pack("ellipse", "circle only", "line only", "set only"), "Ellipse has major and minor axes."),
        ("Asymptotes are associated with", *pack("hyperbola", "circle", "empty set", "AP"), "Hyperbola has asymptotes."),
        ("Latus rectum is a chord through", *pack("focus", "centre only", "vertex only", "origin always"), "Latus rectum passes through focus."),
        ("Conic sections are obtained by cutting a", *pack("cone", "cube", "sphere", "plane only"), "They are sections of a cone."),
        ("The distance from centre to any point on circle is", *pack("radius", "diameter", "focus", "directrix"), "Radius is fixed distance."),
    ]


def geometry3d_bank(n):
    return [
        ("A point in 3D is written as", *pack("(x,y,z)", "(x,y)", "(r,theta)", "{x,y,z}"), "Three coordinates locate a point in space."),
        ("The three coordinate axes are", *pack("x, y and z axes", "only x and y", "r and theta", "a and b"), "3D uses x, y, z."),
        ("The xy-plane has z-coordinate", *pack("0", "1", "x", "y"), "All points in xy-plane have z=0."),
        ("The yz-plane has x-coordinate", *pack("0", "1", "y", "z"), "All points in yz-plane have x=0."),
        ("The zx-plane has y-coordinate", *pack("0", "1", "z", "x"), "All points in zx-plane have y=0."),
        ("3D space is divided into", *pack("8 octants", "4 quadrants", "2 halves", "6 faces"), "Three coordinate planes form eight octants."),
        ("Distance between (x1,y1,z1) and (x2,y2,z2) is", *pack("sqrt((dx)^2+(dy)^2+(dz)^2)", "dx+dy+dz", "sqrt(dx+dy)", "dx/dy"), "This extends distance formula to 3D."),
        ("Distance from origin to (a,b,c) is", *pack("sqrt(a^2+b^2+c^2)", "a+b+c", "abc", "a^2+b^2"), "Use 3D distance formula."),
        ("Midpoint in 3D is found by", *pack("averaging coordinates", "multiplying coordinates", "subtracting only z", "using factorial"), "Average x, y and z separately."),
        ("Section formula in 3D finds", *pack("point dividing a segment", "area of circle", "probability", "variance"), "It locates division point in space."),
        ("A point on x-axis has", *pack("y=0 and z=0", "x=0 only", "z=0 only", "all coordinates equal"), "Only x may vary."),
        ("A point on y-axis has", *pack("x=0 and z=0", "y=0 only", "z=0 only", "all positive"), "Only y may vary."),
        ("A point on z-axis has", *pack("x=0 and y=0", "z=0 only", "x=y=z", "x=1"), "Only z may vary."),
        ("Coordinates of origin in 3D are", *pack("(0,0,0)", "(0,0)", "(1,1,1)", "(0,1,0)"), "All coordinates are zero."),
        ("3D coordinate geometry extends", *pack("2D coordinate geometry", "sets only", "statistics only", "logic only"), "It adds a z-coordinate."),
    ]


def calculus_bank(n):
    return [
        ("Limit describes value a function", *pack("approaches", "never approaches", "counts", "selects"), "A limit is an approached value."),
        ("Derivative represents", *pack("rate of change", "set complement", "sample space", "factorial"), "Derivative measures instantaneous rate."),
        ("Derivative geometrically gives slope of", *pack("tangent", "secant only", "circle radius", "axis only"), "Derivative is tangent slope."),
        ("lim x->a of constant c equals", *pack("c", "a", "0", "undefined always"), "Constant limit is the constant."),
        ("lim x->a of x equals", *pack("a", "x", "0", "1"), "The identity function approaches a."),
        ("Derivative of x^n is", *pack("n x^(n-1)", "x^n", "n x^n", "x^(n+1)"), "Power rule."),
        ("Derivative of constant is", *pack("0", "1", "constant", "undefined"), "Constant has no change."),
        ("Derivative of x is", *pack("1", "0", "x", "2x"), "Slope of y=x is 1."),
        ("Derivative from first principle uses", *pack("limit of difference quotient", "Venn diagram", "factorial", "sample space"), "It uses lim h->0 [f(x+h)-f(x)]/h."),
        ("lim x->0 sin x / x equals", *pack("1", "0", "infinity", "-1"), "This is a standard trigonometric limit."),
        ("lim x->0 (1-cos x)/x equals", *pack("0", "1", "2", "-1"), "This standard limit is 0."),
        ("Derivative of sin x is", *pack("cos x", "-sin x", "tan x", "sec x"), "Basic trigonometric derivative."),
        ("Derivative of cos x is", *pack("-sin x", "sin x", "cos x", "tan x"), "Basic trigonometric derivative."),
        ("Algebra of limits includes limit of sum as", *pack("sum of limits", "product only", "difference only", "undefined always"), "Limits distribute over sums when they exist."),
        ("Instantaneous velocity is an example of", *pack("derivative", "set", "combination", "mean deviation"), "Velocity is rate of change of position."),
    ]


def reasoning_bank(n):
    return [
        ("A statement is a sentence that is", *pack("true or false but not both", "always a question", "always a command", "neither true nor false"), "Mathematical statements have definite truth values."),
        ("Negation of a statement changes its", *pack("truth value", "font", "chapter", "variable only"), "Negation reverses truth."),
        ("The connective 'and' is true when", *pack("both parts are true", "one part is true", "both false", "first false"), "Conjunction requires both true."),
        ("The connective 'or' in mathematics is usually", *pack("inclusive", "exclusive only", "never true", "undefined"), "Mathematical or allows one or both."),
        ("p implies q is false when", *pack("p true and q false", "p false and q true", "both true", "both false"), "Only true -> false is false."),
        ("Converse of p implies q is", *pack("q implies p", "not p implies not q", "p and q", "not q implies not p"), "Converse swaps hypothesis and conclusion."),
        ("Contrapositive of p implies q is", *pack("not q implies not p", "q implies p", "not p implies not q", "p or q"), "Contrapositive reverses and negates."),
        ("The phrase 'there exists' means", *pack("at least one", "all", "none", "exactly zero"), "Existential statement needs one example."),
        ("The phrase 'for all' means", *pack("every element", "some element", "no element", "one element only"), "Universal statement covers all cases."),
        ("A counterexample disproves a", *pack("universal statement", "true example only", "definition", "notation"), "One counterexample is enough."),
        ("A valid argument has conclusion that follows from", *pack("premises", "diagrams only", "guessing", "sample space"), "Validity depends on logical form."),
        ("Truth value of a true statement is", *pack("T", "F", "0 only", "undefined"), "T denotes true."),
        ("Truth value of a false statement is", *pack("F", "T", "1 only", "undefined"), "F denotes false."),
        ("Negation of 'all' often becomes", *pack("there exists at least one not", "all not always", "same statement", "empty set"), "Negating universal gives existential counterclaim."),
        ("Reasoning helps validate", *pack("mathematical statements", "only drawings", "only tables", "only colours"), "The chapter focuses on logical validation."),
    ]


def statistics_bank(n):
    return [
        ("Dispersion measures", *pack("spread of data", "only centre", "only chance", "only arrangement"), "Dispersion describes variability."),
        ("Range equals", *pack("maximum - minimum", "mean + median", "variance squared", "sum/count"), "Range measures total spread."),
        ("Mean deviation uses", *pack("absolute deviations", "squared deviations only", "factorials", "trig ratios"), "Mean deviation averages absolute distances."),
        ("Variance uses", *pack("squared deviations", "absolute deviations only", "sets", "radians"), "Variance averages squared deviations."),
        ("Standard deviation is square root of", *pack("variance", "range", "mean", "median"), "SD is root variance."),
        ("Lower standard deviation means data is", *pack("more consistent", "more spread", "always zero", "impossible"), "Less spread means more consistency."),
        ("Coefficient of variation compares", *pack("relative variability", "only centre", "only range", "sample space"), "CV compares consistency."),
        ("CV formula uses", *pack("standard deviation and mean", "median and mode", "range only", "probability only"), "CV = SD/mean x 100."),
        ("Grouped data uses", *pack("class intervals", "only single values", "only events", "only axes"), "Data is grouped into classes."),
        ("Mean deviation can be computed about", *pack("mean or median", "only origin", "only mode never", "only radius"), "The chapter covers mean deviation about mean and median."),
        ("Variance is always", *pack("non-negative", "negative", "zero only", "undefined"), "Squared deviations cannot give negative variance."),
        ("If all observations are equal, SD is", *pack("0", "1", "mean", "infinite"), "There is no spread."),
        ("Analysis of frequency distributions compares", *pack("mean and variability", "only diagrams", "only functions", "only induction"), "Both central value and spread matter."),
        ("Range is affected strongly by", *pack("extreme values", "middle value only", "frequency labels only", "class names"), "Range uses max and min."),
        ("Statistics helps summarise", *pack("data", "only angles", "only complex numbers", "only conics"), "Statistics studies data."),
    ]


def probability_bank(n):
    return [
        ("A random experiment has", *pack("uncertain outcome", "fixed outcome always", "no outcome", "only one impossible result"), "The exact outcome is not known in advance."),
        ("Sample space is set of", *pack("all possible outcomes", "only favourable outcomes", "only impossible outcomes", "means"), "Sample space contains every outcome."),
        ("An event is a subset of", *pack("sample space", "universal chapter", "mean", "standard deviation"), "Events are collections of outcomes."),
        ("Probability value lies between", *pack("0 and 1", "1 and 2", "-1 and 1 only", "10 and 100"), "Axiomatic probability ranges from 0 to 1."),
        ("Probability of sample space is", *pack("1", "0", "1/2", "2"), "Something in the sample space must occur."),
        ("Probability of impossible event is", *pack("0", "1", "1/2", "2"), "Impossible event has no outcomes."),
        ("Complement of event A is", *pack("not A", "A itself", "sample space only", "empty set always"), "Complement contains outcomes not in A."),
        ("P(A complement) equals", *pack("1-P(A)", "P(A)+1", "P(A)-1", "2P(A)"), "Complement rule."),
        ("Mutually exclusive events have", *pack("no common outcome", "all common outcomes", "same probability always", "probability 1 always"), "They cannot occur together."),
        ("Exhaustive events cover", *pack("entire sample space", "empty set", "one outcome only", "complement only"), "Together they include all possibilities."),
        ("For a fair coin, sample space is", *pack("{H,T}", "{1,2,3}", "{0}", "{HH only}"), "A coin has head and tail."),
        ("For a die, sample space has", *pack("6 outcomes", "2 outcomes", "4 outcomes", "52 outcomes"), "A standard die has six faces."),
        ("If A and B are disjoint, P(A union B) is", *pack("P(A)+P(B)", "P(A)P(B)", "P(A)-P(B)", "1 always"), "Addition rule for mutually exclusive events."),
        ("Axiomatic probability was introduced by", *pack("Kolmogorov", "Euclid", "Cantor", "Newton only"), "The axiomatic approach is associated with Kolmogorov."),
        ("Probability of an event with no outcomes is", *pack("0", "1", "1/2", "undefined always"), "Empty event has probability 0."),
    ]


def build():
    module_id = 1
    chapters = []
    for chapter, topics in CHAPTERS:
        diff = DIFF[chapter]
        timer = {"Easy": 30, "Medium": 45, "Hard": 60}[diff]
        modules = []
        for topic in topics:
            questions = []
            for i, item in enumerate(bank(chapter, module_id), start=1):
                questions.append({
                    "question_id": i,
                    "question_text": f"{topic}: {item[0]}",
                    "options": item[1],
                    "correct_answer": item[2],
                    "rationale": item[3],
                    "timer_per_question_seconds": timer,
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
        "class": "11",
        "board": "CBSE",
        "subject": "Mathematics",
        "source_pdf": "ncert-books-for-class-11-maths.pdf",
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
