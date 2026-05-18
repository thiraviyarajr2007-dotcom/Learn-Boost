import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "class12_cbse_ncert_duolingo_curriculum.json"


CHAPTERS = [
    ("Relations and Functions", ["Types of Relations", "Types of Functions", "Composition of Functions and Invertible Functions", "Binary Operations"]),
    ("Inverse Trigonometric Functions", ["Basic Concepts", "Principal Value Branches", "Properties of Inverse Trigonometric Functions"]),
    ("Matrices", ["Matrix Basics", "Types of Matrices", "Operations on Matrices", "Transpose of a Matrix", "Symmetric and Skew Symmetric Matrices", "Elementary Operations", "Invertible Matrices"]),
    ("Determinants", ["Determinant Basics", "Properties of Determinants", "Area of a Triangle", "Minors and Cofactors", "Adjoint and Inverse of a Matrix", "Applications of Determinants and Matrices"]),
    ("Continuity and Differentiability", ["Continuity", "Differentiability", "Exponential and Logarithmic Functions", "Logarithmic Differentiation", "Parametric Form Derivatives", "Second Order Derivative", "Mean Value Theorem"]),
    ("Application of Derivatives", ["Rate of Change of Quantities", "Increasing and Decreasing Functions", "Tangents and Normals", "Approximations", "Maxima and Minima"]),
    ("Integrals", ["Integration as Inverse of Differentiation", "Integration by Substitution", "Integrals of Particular Functions", "Integration by Partial Fractions", "Integration by Parts", "Definite Integrals", "Fundamental Theorem of Calculus", "Definite Integrals by Substitution", "Properties of Definite Integrals"]),
    ("Application of Integrals", ["Area under Simple Curves", "Area between Two Curves"]),
    ("Differential Equations", ["Basic Concepts", "General and Particular Solutions", "Formation of Differential Equations", "First Order First Degree Equations", "Variable Separable Method", "Homogeneous Differential Equations", "Linear Differential Equations"]),
    ("Vector Algebra", ["Basic Vector Concepts", "Types of Vectors", "Addition of Vectors", "Scalar Multiplication", "Dot Product", "Cross Product"]),
    ("Three Dimensional Geometry", ["Direction Cosines and Ratios", "Equation of a Line in Space", "Angle between Two Lines", "Shortest Distance between Two Lines", "Plane", "Coplanarity of Two Lines", "Angle between Two Planes", "Distance of a Point from a Plane", "Angle between a Line and a Plane"]),
    ("Linear Programming", ["Mathematical Formulation", "Feasible Region", "Objective Function", "Corner Point Method", "Types of LPP Problems"]),
    ("Probability", ["Conditional Probability", "Multiplication Theorem", "Independent Events", "Bayes Theorem", "Random Variables and Probability Distributions", "Bernoulli Trials", "Binomial Distribution"]),
]


EXPLAIN = {
    "Relations and Functions": "Relations connect elements through ordered pairs, while functions are special relations where each input has exactly one output. Class 12 goes deeper into reflexive, symmetric, transitive and equivalence relations, plus one-one, onto, composition and invertible functions. Think of a function as a dependable machine: one input should produce one clear output.",
    "Inverse Trigonometric Functions": "Inverse trigonometric functions reverse the usual trigonometric process. Instead of asking for a ratio from an angle, we ask for the angle from a ratio. Principal value branches keep answers unique, like choosing one official address from many possible angle locations.",
    "Matrices": "Matrices are rectangular arrays of numbers arranged in rows and columns. They help organise data and solve equations compactly. Operations like addition, multiplication, transpose and inverse follow special rules, so matrices behave like number tables with their own grammar.",
    "Determinants": "A determinant is a number linked to a square matrix. It helps decide invertibility, solve linear equations and find area of a triangle. Determinants use row and column patterns, and their properties make large calculations faster.",
    "Continuity and Differentiability": "Continuity means a graph can be traced near a point without a break. Differentiability means the graph has a well-defined tangent slope. This chapter builds powerful derivative tools, including logarithmic differentiation, parametric derivatives, second derivatives and mean value theorems.",
    "Application of Derivatives": "Derivatives measure change, so they help study speed, growth, slopes, approximations and optimisation. A derivative can tell whether a function is increasing, decreasing, at a maximum, or at a minimum. It turns curves into readable behaviour maps.",
    "Integrals": "Integration is the reverse process of differentiation and also a tool for accumulation. Class 12 includes substitution, partial fractions, integration by parts, definite integrals and properties. Think of integration as adding infinitely many tiny pieces to recover a whole.",
    "Application of Integrals": "Definite integrals can measure area under curves and area between curves. Instead of counting squares roughly, integration slices a region into thin strips and adds them exactly. This connects calculus with geometry in a visual way.",
    "Differential Equations": "A differential equation connects a function with its derivatives. It models changing quantities such as growth, motion and decay. Solving it means finding the original function or family of functions that satisfies the given rate relationship.",
    "Vector Algebra": "Vectors have both magnitude and direction. They can be added, scaled and multiplied using dot product or cross product. Vectors are useful for movement, force, geometry and three-dimensional thinking because they describe direction clearly.",
    "Three Dimensional Geometry": "Three-dimensional geometry studies lines and planes in space using vectors, direction ratios, direction cosines and equations. It helps find angles, distances, coplanarity and shortest paths, extending coordinate geometry beyond a flat surface.",
    "Linear Programming": "Linear programming finds the best value of an objective function under linear constraints. Feasible regions show all possible solutions, and the optimum usually occurs at a corner point. It is useful for diet, manufacturing and transport decisions.",
    "Probability": "Probability studies chance using conditional probability, independence, Bayes theorem, random variables and distributions. It helps update information when new evidence appears and model repeated yes-no experiments through Bernoulli trials and binomial distribution.",
}


DIFFICULTY = {
    "Relations and Functions": "Hard",
    "Inverse Trigonometric Functions": "Medium",
    "Matrices": "Medium",
    "Determinants": "Hard",
    "Continuity and Differentiability": "Hard",
    "Application of Derivatives": "Hard",
    "Integrals": "Hard",
    "Application of Integrals": "Hard",
    "Differential Equations": "Hard",
    "Vector Algebra": "Medium",
    "Three Dimensional Geometry": "Hard",
    "Linear Programming": "Medium",
    "Probability": "Hard",
}


def opts(answer, b, c, d):
    return [answer, b, c, d], answer


def bank(chapter):
    data = {
        "Relations and Functions": [
            ("A relation R on a set A is reflexive if", *opts("(a, a) is in R for every a in A", "(a, b) implies (b, a)", "(a, b) and (b, c) imply (a, c)", "R is empty"), "Reflexive means every element is related to itself."),
            ("A relation is symmetric if", *opts("(a, b) in R implies (b, a) in R", "every element relates to itself", "R has no ordered pairs", "R is a function"), "Symmetry reverses each related pair."),
            ("A relation is transitive if", *opts("(a, b) and (b, c) imply (a, c)", "(a, b) implies (b, a)", "all pairs are absent", "each input has one output"), "Transitivity links two steps into one."),
            ("A function is one-one if different inputs have", *opts("different images", "same image always", "no image", "two images"), "One-one functions do not merge distinct inputs."),
            ("A function is onto if its range equals its", *opts("codomain", "domain", "graph", "inverse only"), "Onto means every codomain element is hit."),
            ("An invertible function must be", *opts("one-one and onto", "only one-one", "only onto", "constant"), "A function has an inverse when it is bijective."),
        ],
        "Inverse Trigonometric Functions": [
            ("sin inverse x is defined for x in", *opts("[-1, 1]", "all real numbers", "[0, infinity)", "R minus 0"), "The input to inverse sine must be between -1 and 1."),
            ("Principal value of sin inverse x lies in", *opts("[-pi/2, pi/2]", "[0, pi]", "[-pi, pi]", "[0, 2pi]"), "This interval makes inverse sine single-valued."),
            ("Principal value of cos inverse x lies in", *opts("[0, pi]", "[-pi/2, pi/2]", "all real numbers", "[-pi, 0]"), "This is the principal range of inverse cosine."),
            ("tan inverse x is defined for", *opts("all real x", "only [-1,1]", "only positive x", "only integers"), "Tangent inverse accepts every real number."),
            ("tan inverse x has principal values in", *opts("(-pi/2, pi/2)", "[0, pi]", "[-pi, pi]", "[0, 2pi]"), "This interval avoids repeated tangent values."),
        ],
        "Matrices": [
            ("A matrix is an arrangement of numbers in", *opts("rows and columns", "only one row", "only a circle", "random order"), "Matrices are rectangular arrays."),
            ("A square matrix has", *opts("same number of rows and columns", "one row only", "all entries zero", "no diagonal"), "Order n square matrix has n rows and n columns."),
            ("A zero matrix has", *opts("all entries zero", "all diagonal entries one", "only one row", "no entries"), "Every element of a zero matrix is zero."),
            ("Transpose of a matrix is obtained by interchanging", *opts("rows and columns", "only signs", "only diagonal entries", "only zero entries"), "Transpose flips rows into columns."),
            ("A symmetric matrix satisfies", *opts("A transpose = A", "A transpose = -A", "A = 0", "A inverse = A"), "Symmetric matrices equal their transpose."),
            ("Matrix multiplication is possible when columns of first equal", *opts("rows of second", "columns of second", "determinant", "order always"), "The inner dimensions must match."),
        ],
        "Determinants": [
            ("A determinant is defined for", *opts("square matrices", "only row matrices", "only column matrices", "all rectangular matrices"), "Only square matrices have determinants."),
            ("A 2 by 2 determinant |a b; c d| equals", *opts("ad - bc", "ab - cd", "ac - bd", "a+b+c+d"), "The determinant is product of main diagonal minus other diagonal."),
            ("If two rows of a determinant are identical, determinant is", *opts("0", "1", "-1", "unchanged nonzero"), "Equal rows make determinant zero."),
            ("Area of triangle using determinant is half of", *opts("absolute determinant value", "trace", "matrix order", "cofactor only"), "The coordinate area formula uses determinant magnitude."),
            ("Cofactor includes a sign factor", *opts("(-1)^(i+j)", "i+j", "ij", "2i+j"), "Cofactors use alternating signs."),
            ("A matrix is invertible if its determinant is", *opts("non-zero", "zero", "one only", "negative only"), "Non-zero determinant means inverse exists."),
        ],
        "Continuity and Differentiability": [
            ("A function is continuous at x=a when limit equals", *opts("function value at a", "derivative at a", "zero always", "infinity"), "Continuity requires limit and value to match."),
            ("Differentiability at a point implies", *opts("continuity at that point", "discontinuity", "constant function only", "zero derivative always"), "Every differentiable function is continuous there."),
            ("Derivative of e^x is", *opts("e^x", "x e^x", "1/x", "0"), "Exponential e^x differentiates to itself."),
            ("Derivative of log x is", *opts("1/x", "x", "e^x", "0"), "Natural logarithm derivative is 1/x."),
            ("Logarithmic differentiation is useful when functions involve", *opts("products, quotients or powers", "only constants", "only matrices", "only sets"), "Taking logs simplifies complicated products and powers."),
            ("Second order derivative is derivative of", *opts("first derivative", "original constant only", "matrix inverse", "definite integral only"), "It measures change of the derivative."),
        ],
        "Application of Derivatives": [
            ("Derivative represents rate of change of", *opts("one quantity with respect to another", "set size", "matrix order", "probability only"), "Derivatives measure rates."),
            ("A function is increasing where derivative is", *opts("positive", "negative", "zero always", "undefined always"), "Positive slope means increasing."),
            ("A function is decreasing where derivative is", *opts("negative", "positive", "one", "infinite always"), "Negative slope means decreasing."),
            ("Slope of tangent to y=f(x) is", *opts("dy/dx", "x/y", "area under curve", "determinant"), "Derivative gives tangent slope."),
            ("Normal to a curve is perpendicular to", *opts("tangent", "x-axis always", "y-axis always", "radius only"), "Normal meets tangent at right angle."),
            ("Maxima and minima are used for", *opts("optimisation", "set notation", "matrix transpose", "Venn diagrams"), "They help find best or extreme values."),
        ],
        "Integrals": [
            ("Integration is inverse process of", *opts("differentiation", "matrix addition", "probability", "set union"), "Antiderivatives reverse derivatives."),
            ("Indefinite integral includes", *opts("constant of integration", "upper limit only", "lower limit only", "determinant"), "A constant C is added."),
            ("Integration by substitution uses", *opts("change of variable", "row operation", "Bayes theorem", "binary operation"), "Substitution transforms the variable."),
            ("Integration by parts is based on derivative of", *opts("product of functions", "constant only", "matrix inverse", "empty set"), "It reverses product rule."),
            ("Definite integral has", *opts("limits of integration", "constant C always", "only variables", "no bounds"), "Definite integrals evaluate over an interval."),
            ("Fundamental theorem of calculus links integration with", *opts("differentiation", "matrix transpose", "linear programming", "Venn diagrams"), "It connects area accumulation and derivatives."),
        ],
        "Application of Integrals": [
            ("Area under y=f(x) from a to b is given by", *opts("definite integral of f(x)", "derivative of f only", "determinant of f", "matrix inverse"), "Definite integrals compute area under curves."),
            ("Area between two curves is found by integrating", *opts("upper curve minus lower curve", "sum always", "product always", "derivative only"), "Vertical strips have height top minus bottom."),
            ("The x-axis boundary usually means y equals", *opts("0", "1", "x", "infinity"), "The x-axis has equation y=0."),
            ("If a region lies below x-axis, area is taken as", *opts("positive magnitude", "negative always", "zero", "undefined"), "Area is non-negative."),
            ("Integration finds area by adding many thin", *opts("strips", "matrices", "relations", "events"), "Areas are built from small strips."),
        ],
        "Differential Equations": [
            ("A differential equation contains", *opts("derivatives", "only sets", "only matrices", "only probabilities"), "It relates derivatives and variables."),
            ("Order of a differential equation is order of", *opts("highest derivative", "lowest derivative", "constant term", "degree of variable only"), "Order is based on the highest derivative present."),
            ("Degree is power of highest derivative after equation is", *opts("polynomial in derivatives", "integrated only", "graphed", "converted to matrix"), "Degree is defined when derivatives form a polynomial."),
            ("General solution contains", *opts("arbitrary constants", "no constants", "only numbers", "only matrices"), "General solutions represent a family of curves."),
            ("Particular solution is obtained by using", *opts("given conditions", "only graph colour", "random value", "set complement"), "Conditions determine constants."),
            ("Variable separable method separates", *opts("x terms and y terms", "rows and columns", "sets and subsets", "events only"), "Each variable is moved to its own side."),
        ],
        "Vector Algebra": [
            ("A vector has", *opts("magnitude and direction", "magnitude only", "direction only", "no direction"), "Vectors describe size and direction."),
            ("A scalar has", *opts("magnitude only", "direction only", "magnitude and direction", "no value"), "Scalars are ordinary quantities with magnitude."),
            ("Zero vector has magnitude", *opts("0", "1", "-1", "infinity"), "The zero vector has no length."),
            ("Unit vector has magnitude", *opts("1", "0", "2", "-1"), "Unit vectors have length one."),
            ("Dot product of perpendicular vectors is", *opts("0", "1", "-1", "infinite"), "cos 90 degrees is zero."),
            ("Cross product of two vectors gives a vector perpendicular to", *opts("both vectors", "only first vector", "only second vector", "neither vector"), "The cross product direction is normal to the plane of the vectors."),
        ],
        "Three Dimensional Geometry": [
            ("Direction cosines of a line satisfy", *opts("l^2 + m^2 + n^2 = 1", "l+m+n=0", "lmn=1", "l=m=n=0"), "Direction cosines obey this identity."),
            ("Direction ratios are proportional to", *opts("direction cosines", "coordinates only", "determinants", "probabilities"), "They describe direction up to scale."),
            ("Vector equation of a line uses a point and", *opts("direction vector", "normal distribution", "binary operation", "minor only"), "A line in space needs position and direction."),
            ("Shortest distance between skew lines is along a line perpendicular to", *opts("both lines", "only x-axis", "only one line", "neither line"), "Shortest connector is common perpendicular."),
            ("A plane can be described using a point and", *opts("normal vector", "sample space", "matrix transpose", "Venn region"), "A normal vector fixes plane orientation."),
            ("Coplanar lines lie in", *opts("same plane", "different planes always", "no plane", "only xy-plane"), "Coplanarity means sharing a plane."),
        ],
        "Linear Programming": [
            ("Linear programming optimises", *opts("objective function", "trigonometric identity", "matrix transpose", "inverse sine"), "The objective function is maximised or minimised."),
            ("Constraints in LPP are usually", *opts("linear inequalities", "quadratic equations only", "trigonometric equations", "determinants"), "Constraints define the feasible region."),
            ("Feasible region contains", *opts("all points satisfying constraints", "only origin", "no solution always", "only maximum point"), "Every feasible point satisfies all constraints."),
            ("Corner point method checks values at", *opts("vertices of feasible region", "all real numbers", "only midpoint", "only intercepts never"), "Optimum occurs at a corner under usual conditions."),
            ("Non-negativity constraints mean variables are", *opts("greater than or equal to zero", "less than zero", "equal to one", "unrestricted always"), "Many real quantities cannot be negative."),
        ],
        "Probability": [
            ("Conditional probability P(A|B) means probability of A given", *opts("B has occurred", "A has not occurred", "sample space is empty", "events are impossible"), "It updates probability with known condition B."),
            ("Multiplication theorem gives probability of", *opts("intersection of events", "union only", "complement only", "empty set only"), "It helps calculate P(A and B)."),
            ("Independent events satisfy", *opts("P(A and B)=P(A)P(B)", "P(A)=P(B) always", "P(A)=0", "P(B)=1 always"), "Independence means one event does not affect the other."),
            ("Bayes theorem is useful for", *opts("reversing conditional probability", "matrix inversion only", "finding derivatives", "area under curve"), "It updates causes from observed evidence."),
            ("A random variable assigns numbers to", *opts("outcomes", "only matrices", "only functions", "only tangents"), "Random variables numerically describe outcomes."),
            ("A binomial distribution applies to repeated", *opts("Bernoulli trials", "matrix multiplications", "integrations", "set complements"), "Binomial distribution counts successes in independent trials."),
        ],
    }
    return data[chapter]


def make_module(module_id, chapter, topic):
    difficulty = DIFFICULTY[chapter]
    seconds = {"Easy": 30, "Medium": 45, "Hard": 60}[difficulty]
    items = bank(chapter)
    return {
        "module_id": module_id,
        "topic_name": topic,
        "explanation": EXPLAIN[chapter],
        "difficulty": difficulty,
        "total_timer_minutes": 12 if difficulty == "Hard" else 8,
        "questions": [
            {
                "question_id": index,
                "question_text": f"{topic}: {item[0]}",
                "options": item[1],
                "correct_answer": item[2],
                "rationale": item[3],
                "timer_per_question_seconds": seconds,
            }
            for index, item in enumerate(items, start=1)
        ],
    }


def build():
    module_id = 1
    chapters = []
    for chapter_name, topics in CHAPTERS:
        modules = []
        for topic in topics:
            modules.append(make_module(module_id, chapter_name, topic))
            module_id += 1
        chapters.append({"chapter_name": chapter_name, "modules": modules})
    return {
        "class": "12",
        "board": "CBSE",
        "subject": "Mathematics",
        "source_pdf": "ncert-books-for-class-12-maths.pdf",
        "chapters": chapters,
    }


if __name__ == "__main__":
    data = build()
    OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
    modules = sum(len(chapter["modules"]) for chapter in data["chapters"])
    questions = sum(len(module["questions"]) for chapter in data["chapters"] for module in chapter["modules"])
    print(OUT)
    print(f"chapters={len(data['chapters'])}")
    print(f"modules={modules}")
    print(f"questions={questions}")
