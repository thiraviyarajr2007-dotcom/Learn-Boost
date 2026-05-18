import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "src" / "data"
OUTPUT_JSON = DATA_DIR / "class12_mathematics_learning_journey.json"
OUTPUT_MANIFEST = DATA_DIR / "class12_mathematics_validation_manifest.json"


CHAPTERS = [
    {
        "number": 1,
        "volume": "Volume 1",
        "month": "June",
        "title": "Applications of Matrices and Determinants",
        "difficulty": "Hard",
        "weight": 1.25,
        "topics": [
            ("1.1", "Introduction", 1),
            ("1.2", "Inverse of a Non-Singular Square Matrix", 2),
            ("1.3", "Elementary Transformations of a Matrix", 16),
            ("1.4", "Applications of Matrices: Solving System of Linear Equations", 28),
            ("1.5", "Applications of Matrices: Consistency of System of Linear Equations", 42),
        ],
        "concepts": [
            ("A square matrix has an inverse only when its determinant is non-zero.", "when its determinant is non-zero"),
            ("Elementary row or column transformations preserve equivalence while simplifying a matrix.", "simplifying a matrix"),
            ("Matrix methods convert simultaneous linear equations into an organized algebra table.", "simultaneous linear equations"),
            ("Consistency tells whether a system has no solution, one solution, or infinitely many solutions.", "solution behaviour"),
            ("The inverse matrix method solves AX = B by writing X = A inverse B.", "X = A inverse B"),
        ],
    },
    {
        "number": 2,
        "volume": "Volume 1",
        "month": "July",
        "title": "Complex Numbers",
        "difficulty": "Medium",
        "weight": 1.05,
        "topics": [
            ("2.1", "Introduction to Complex Numbers", 52),
            ("2.2", "Complex Numbers", 54),
            ("2.3", "Basic Algebraic Properties of Complex Numbers", 58),
            ("2.4", "Conjugate of a Complex Number", 60),
            ("2.5", "Modulus of a Complex Number", 66),
            ("2.6", "Geometry and Locus of Complex Numbers", 73),
            ("2.7", "Polar and Euler Form of a Complex Number", 75),
            ("2.8", "de Moivre's Theorem and its Applications", 83),
        ],
        "concepts": [
            ("A complex number is written as a + ib, where i squared is -1.", "a + ib"),
            ("The conjugate of a + ib is a - ib.", "a - ib"),
            ("The modulus of a + ib is the distance from the origin in the complex plane.", "distance from the origin"),
            ("Polar form expresses a complex number using modulus and argument.", "modulus and argument"),
            ("de Moivre's theorem helps find powers and roots of complex numbers.", "powers and roots"),
        ],
    },
    {
        "number": 3,
        "volume": "Volume 1",
        "month": "July",
        "title": "Theory of Equations",
        "difficulty": "Hard",
        "weight": 1.15,
        "topics": [
            ("3.1", "Introduction", 97),
            ("3.2", "Basics of Polynomial Equations", 99),
            ("3.3", "Vieta's Formulae and Formation of Polynomial Equations", 100),
            ("3.4", "Nature of Roots and Nature of Coefficients of Polynomial Equations", 106),
            ("3.5", "Applications of Polynomial Equation in Geometry", 111),
            ("3.6", "Roots of Higher Degree Polynomial Equations", 112),
            ("3.7", "Polynomials with Additional Information", 113),
            ("3.8", "Polynomial Equations with No Additional Information", 118),
            ("3.9", "Descartes Rule", 124),
        ],
        "concepts": [
            ("A polynomial equation is solved by finding values that make the polynomial zero.", "values that make the polynomial zero"),
            ("Vieta's formulae connect roots of an equation with its coefficients.", "roots with coefficients"),
            ("The nature of roots depends on the coefficients and discriminant-like conditions.", "nature of roots"),
            ("Higher degree equations often use factorisation and known root relations.", "factorisation and known root relations"),
            ("Descartes' rule gives information about possible positive and negative roots.", "possible positive and negative roots"),
        ],
    },
    {
        "number": 4,
        "volume": "Volume 1",
        "month": "July/August",
        "title": "Inverse Trigonometric Functions",
        "difficulty": "Hard",
        "weight": 1.15,
        "topics": [
            ("4.1", "Introduction", 129),
            ("4.2", "Some Fundamental Concepts", 130),
            ("4.3", "Sine Function and Inverse Sine Function", 133),
            ("4.4", "Cosine Function and Inverse Cosine Function", 138),
            ("4.5", "Tangent Function and Inverse Tangent Function", 143),
            ("4.6", "Cosecant Function and Inverse Cosecant Function", 148),
            ("4.7", "Secant Function and Inverse Secant Function", 149),
            ("4.8", "Cotangent Function and Inverse Cotangent Function", 151),
            ("4.9", "Principal Value of Inverse Trigonometric Functions", 153),
            ("4.10", "Properties of Inverse Trigonometric Functions", 155),
        ],
        "concepts": [
            ("Inverse trigonometric functions return angles from trigonometric ratios.", "angles from ratios"),
            ("Principal values keep inverse trigonometric answers single-valued.", "single-valued answers"),
            ("The inverse sine function uses a restricted range to become one-one.", "restricted range"),
            ("Identities of inverse trigonometric functions simplify expressions and equations.", "simplify expressions"),
            ("Domain and range control whether an inverse trigonometric expression is valid.", "domain and range"),
        ],
    },
    {
        "number": 5,
        "volume": "Volume 1",
        "month": "August",
        "title": "Two Dimensional Analytical Geometry-II",
        "difficulty": "Hard",
        "weight": 1.2,
        "topics": [
            ("5.1", "Introduction", 172),
            ("5.2", "Circle", 173),
            ("5.3", "Conics", 182),
            ("5.4", "Conic Sections", 197),
            ("5.5", "Parametric Form of Conics", 199),
            ("5.6", "Tangents and Normals to Conics", 201),
            ("5.7", "Real Life Applications of Conics", 207),
        ],
        "concepts": [
            ("Analytical geometry studies curves using coordinates and equations.", "coordinates and equations"),
            ("A circle is the locus of points at a fixed distance from a fixed point.", "fixed distance from a fixed point"),
            ("Conics arise from slicing a cone and include parabola, ellipse, and hyperbola.", "parabola, ellipse, and hyperbola"),
            ("Parametric form represents curve points using a parameter.", "using a parameter"),
            ("Tangents touch a curve at a point, while normals are perpendicular to tangents.", "perpendicular to tangents"),
        ],
    },
    {
        "number": 6,
        "volume": "Volume 1",
        "month": "August/September",
        "title": "Applications of Vector Algebra",
        "difficulty": "Hard",
        "weight": 1.2,
        "topics": [
            ("6.1", "Introduction", 221),
            ("6.2", "Geometric Introduction to Vectors", 222),
            ("6.3", "Scalar Product and Vector Product", 224),
            ("6.4", "Scalar Triple Product", 231),
            ("6.5", "Vector Triple Product", 238),
            ("6.6", "Jacobi's Identity and Lagrange's Identity", 239),
            ("6.7", "Application of Vectors to 3-Dimensional Geometry", 242),
            ("6.8", "Different Forms of Equation of a Plane", 255),
            ("6.9", "Image of a Point in a Plane", 273),
            ("6.10", "Meeting Point of a Line and a Plane", 274),
        ],
        "concepts": [
            ("Vectors have both magnitude and direction.", "magnitude and direction"),
            ("Scalar product measures projection and gives a scalar.", "a scalar"),
            ("Vector product gives a vector perpendicular to the two given vectors.", "perpendicular vector"),
            ("Scalar triple product represents the volume of a parallelepiped.", "volume of a parallelepiped"),
            ("Planes and lines in 3D can be described compactly with vectors.", "3D lines and planes"),
        ],
    },
    {
        "number": 7,
        "volume": "Volume 2",
        "month": "October",
        "title": "Applications of Differential Calculus",
        "difficulty": "Hard",
        "weight": 1.35,
        "topics": [
            ("7.1", "Introduction", 1),
            ("7.2", "Meaning of Derivatives", 2),
            ("7.3", "Mean Value Theorem", 15),
            ("7.4", "Series Expansions", 22),
            ("7.5", "Indeterminate Forms", 25),
            ("7.6", "Applications of First Derivative", 32),
            ("7.7", "Applications of Second Derivative", 40),
            ("7.8", "Applications in Optimization", 44),
            ("7.9", "Symmetry and Asymptotes", 47),
            ("7.10", "Sketching of Curves", 50),
        ],
        "concepts": [
            ("A derivative measures instantaneous rate of change.", "instantaneous rate of change"),
            ("Mean value theorems connect average change with instantaneous change.", "average and instantaneous change"),
            ("Series expansions approximate functions near a point.", "approximate functions"),
            ("Indeterminate forms are evaluated using limiting techniques.", "limiting techniques"),
            ("First and second derivatives help study monotonicity, extrema, concavity, and optimization.", "extrema and concavity"),
        ],
    },
    {
        "number": 8,
        "volume": "Volume 2",
        "month": "October/November",
        "title": "Differentials and Partial Derivatives",
        "difficulty": "Hard",
        "weight": 1.15,
        "topics": [
            ("8.1", "Introduction", 58),
            ("8.2", "Linear Approximation and Differentials", 60),
            ("8.3", "Functions of Several Variables", 68),
            ("8.4", "Limit and Continuity of Functions of Two Variables", 70),
            ("8.5", "Partial Derivatives", 74),
            ("8.6", "Linear Approximation and Differential of a Function of Several Variables", 82),
        ],
        "concepts": [
            ("Differentials estimate small changes using derivatives.", "estimate small changes"),
            ("A function of several variables depends on more than one input.", "more than one input"),
            ("Limits and continuity in two variables depend on behaviour near a point from all paths.", "all paths"),
            ("Partial derivatives differentiate with respect to one variable while keeping others fixed.", "keeping others fixed"),
            ("Linear approximation replaces a complicated surface locally with a tangent plane.", "tangent plane"),
        ],
    },
    {
        "number": 9,
        "volume": "Volume 2",
        "month": "November/December",
        "title": "Applications of Integration",
        "difficulty": "Hard",
        "weight": 1.3,
        "topics": [
            ("9.1", "Introduction", 90),
            ("9.2", "Definite Integral as the Limit of a Sum", 92),
            ("9.3", "Fundamental Theorems of Integral Calculus and Their Applications", 101),
            ("9.4", "Bernoulli's Formula", 113),
            ("9.5", "Improper Integrals", 115),
            ("9.6", "Reduction Formulae", 117),
            ("9.7", "Gamma Integral", 120),
            ("9.8", "Evaluation of Bounded Plane Area by Integration", 122),
            ("9.9", "Volume of a Solid Obtained by Revolving Area", 135),
        ],
        "concepts": [
            ("A definite integral can be understood as the limit of a sum.", "limit of a sum"),
            ("The fundamental theorem links differentiation and integration.", "differentiation and integration"),
            ("Improper integrals handle infinite limits or unbounded functions.", "infinite or unbounded cases"),
            ("Reduction formulae simplify repeated families of integrals.", "families of integrals"),
            ("Integration finds bounded areas and volumes of revolution.", "areas and volumes"),
        ],
    },
    {
        "number": 10,
        "volume": "Volume 2",
        "month": "December/January",
        "title": "Ordinary Differential Equations",
        "difficulty": "Hard",
        "weight": 1.25,
        "topics": [
            ("10.1", "Introduction", 144),
            ("10.2", "Differential Equation, Order, and Degree", 145),
            ("10.3", "Classification of Differential Equations", 149),
            ("10.4", "Formation of Differential Equations", 151),
            ("10.5", "Solution of Ordinary Differential Equations", 155),
            ("10.6", "Solution of First Order and First Degree Differential Equations", 159),
            ("10.7", "First Order Linear Differential Equations", 166),
            ("10.8", "Applications of First Order Ordinary Differential Equations", 171),
        ],
        "concepts": [
            ("A differential equation relates a function and its derivatives.", "function and derivatives"),
            ("Order is the highest derivative present in a differential equation.", "highest derivative"),
            ("Degree is the power of the highest order derivative after clearing radicals and fractions.", "power of highest order derivative"),
            ("Forming a differential equation often removes arbitrary constants.", "removes arbitrary constants"),
            ("First order linear differential equations are solved using an integrating factor.", "integrating factor"),
        ],
    },
    {
        "number": 11,
        "volume": "Volume 2",
        "month": "January",
        "title": "Probability Distributions",
        "difficulty": "Medium",
        "weight": 1.05,
        "topics": [
            ("11.1", "Introduction", 179),
            ("11.2", "Random Variable", 179),
            ("11.3", "Types of Random Variable", 184),
            ("11.4", "Continuous Distributions", 195),
            ("11.5", "Mathematical Expectation", 203),
            ("11.6", "Theoretical Distributions: Some Special Discrete Distributions", 210),
        ],
        "concepts": [
            ("A random variable assigns a number to each outcome of a random experiment.", "number to each outcome"),
            ("Discrete random variables take countable values.", "countable values"),
            ("Continuous random variables take values over intervals.", "values over intervals"),
            ("Mathematical expectation represents the long-run average value.", "long-run average"),
            ("Theoretical distributions model repeated random situations.", "repeated random situations"),
        ],
    },
    {
        "number": 12,
        "volume": "Volume 2",
        "month": "January",
        "title": "Discrete Mathematics",
        "difficulty": "Medium",
        "weight": 1.0,
        "topics": [
            ("12.1", "Introduction", 224),
            ("12.2", "Binary Operations", 225),
            ("12.3", "Mathematical Logic", 237),
        ],
        "concepts": [
            ("Discrete mathematics studies separate, countable structures.", "separate, countable structures"),
            ("A binary operation combines two elements to produce one element.", "combines two elements"),
            ("Closure means the result of an operation remains in the same set.", "result remains in the same set"),
            ("Mathematical logic studies statements, connectives, and truth values.", "statements and truth values"),
            ("Truth tables organize the truth values of compound statements.", "truth values"),
        ],
    },
]


MODULE_KINDS = [
    ("concept", "Concept Sprint"),
    ("worked", "Worked Example Builder"),
    ("practice", "Board Practice"),
]

DISTRACTORS = [
    "memorising the chapter title only",
    "ignoring the given condition",
    "changing the topic into an unrelated formula",
    "using a rule from a different chapter",
    "skipping the definition before solving",
]


def slug(value):
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def difficulty_for(chapter, kind, topic_title):
    if topic_title.lower() == "introduction":
        return "Easy"
    if kind == "concept" and chapter["difficulty"] == "Medium":
        return "Medium"
    if kind == "concept":
        return "Medium"
    return chapter["difficulty"]


def timer_for(difficulty):
    return {"Easy": 30, "Medium": 45, "Hard": 60}[difficulty]


def question_count_for(chapter, difficulty, kind):
    base = {"Easy": 6, "Medium": 10, "Hard": 12}[difficulty]
    if kind == "practice":
        base += 2
    if chapter["weight"] >= 1.25 and difficulty == "Hard":
        base += 1
    return min(15, base)


def option_set(correct, wrongs):
    options = [correct]
    for item in wrongs:
        if item != correct and item not in options:
            options.append(item)
        if len(options) == 4:
            break
    while len(options) < 4:
        options.append(DISTRACTORS[len(options)])
    # deterministic shuffle without randomness
    return [options[i] for i in [1, 3, 0, 2]]


def make_question(qid, text, correct, wrongs, rationale, timer):
    return {
        "question_id": qid,
        "question_text": text,
        "options": option_set(correct, wrongs),
        "correct_answer": correct,
        "rationale": rationale,
        "timer_per_question_seconds": timer,
    }


def generated_questions(chapter, section, topic, kind, difficulty):
    timer = timer_for(difficulty)
    count = question_count_for(chapter, difficulty, kind)
    concepts = chapter["concepts"]
    wrong_topics = [t[1] for c in CHAPTERS for t in c["topics"] if t[1] != topic]
    questions = []

    for idx in range(count):
        fact, answer = concepts[idx % len(concepts)]
        pattern = idx % 8
        qid = idx + 1
        if pattern == 0:
            questions.append(make_question(
                qid,
                f"In Chapter {chapter['number']} ({chapter['title']}), what is the key idea used in the section '{topic}'?",
                answer,
                [w for _, w in concepts if w != answer] + DISTRACTORS,
                fact,
                timer,
            ))
        elif pattern == 1:
            questions.append(make_question(
                qid,
                f"Which textbook section number is assigned to '{topic}' in Class 12 Mathematics?",
                section,
                [t[0] for t in chapter["topics"] if t[0] != section] + ["7.7", "11.4", "4.2"],
                f"The table of contents lists '{topic}' as section {section}.",
                timer,
            ))
        elif pattern == 2:
            questions.append(make_question(
                qid,
                f"'{topic}' belongs to which Class 12 Mathematics chapter?",
                chapter["title"],
                [c["title"] for c in CHAPTERS if c["title"] != chapter["title"]],
                f"The PDF table of contents places '{topic}' under Chapter {chapter['number']}: {chapter['title']}.",
                timer,
            ))
        elif pattern == 3:
            questions.append(make_question(
                qid,
                f"When solving a board-style problem from '{topic}', which habit best matches the textbook approach?",
                "identify the relevant definition or theorem first",
                DISTRACTORS + ["guess the answer from the options"],
                "The textbook builds each topic from definitions, formulae, worked examples, and then exercises.",
                timer,
            ))
        elif pattern == 4:
            questions.append(make_question(
                qid,
                f"Which statement is most accurate for the concept used in '{topic}'?",
                fact,
                [f for f, _ in concepts if f != fact] + [
                    "The topic is solved without using any mathematical condition.",
                    "The topic is unrelated to Class 12 Mathematics.",
                ],
                fact,
                timer,
            ))
        elif pattern == 5:
            questions.append(make_question(
                qid,
                f"The section '{topic}' appears in which textbook volume and month plan?",
                f"{chapter['volume']} - {chapter['month']}",
                [f"{c['volume']} - {c['month']}" for c in CHAPTERS if c != chapter],
                f"The textbook contents place Chapter {chapter['number']} in {chapter['volume']} for {chapter['month']}.",
                timer,
            ))
        elif pattern == 6:
            questions.append(make_question(
                qid,
                f"Which topic is from the same chapter as '{topic}'?",
                chapter["topics"][(idx + 1) % len(chapter["topics"])][1],
                wrong_topics,
                f"Both topics are listed under Chapter {chapter['number']}: {chapter['title']}.",
                timer,
            ))
        else:
            questions.append(make_question(
                qid,
                f"For the '{kind}' module on '{topic}', what should a student focus on before attempting MCQs?",
                "understand the concept and then practise the textbook pattern",
                [
                    "skip directly to unrelated chapters",
                    "memorise only the page number",
                    "avoid checking the rationale",
                    "change every problem into mental arithmetic",
                ],
                "The learning journey is designed as explanation, example, practice, and quiz, matching the textbook progression.",
                timer,
            ))

    return questions


def explanation_for(chapter, topic, kind_label, difficulty):
    lead = {
        "Concept Sprint": "Think of this module as the warm-up lap.",
        "Worked Example Builder": "Here we slow down and watch the method move step by step.",
        "Board Practice": "Now the idea becomes exam practice.",
    }[kind_label]
    concept_text = " ".join(item[0] for item in chapter["concepts"][:2])
    text = (
        f"{lead} In '{topic}', you connect the textbook idea from Chapter {chapter['number']} "
        f"to a clear solving habit. {concept_text} Treat each formula like a tool: first notice "
        f"when it applies, then use it carefully, and finally check whether the answer fits the condition."
    )
    words = text.split()
    return " ".join(words[:150])


def build():
    curriculum = []
    manifest = {
        "source": "TN State Board Class 12 Mathematics English Medium PDFs, Volume 1 2024 Edition and Volume 2 2025 Edition",
        "question_total": 0,
        "module_total": 0,
        "chapters": [],
    }

    for chapter in CHAPTERS:
        chapter_obj = {
            "chapter_name": chapter["title"],
            "modules": [],
        }
        chapter_manifest = {
            "chapter_name": chapter["title"],
            "chapter_number": chapter["number"],
            "volume": chapter["volume"],
            "month": chapter["month"],
            "modules": [],
        }

        for topic_index, (section, topic, page) in enumerate(chapter["topics"], start=1):
            for kind, kind_label in MODULE_KINDS:
                difficulty = difficulty_for(chapter, kind, topic)
                module_id = f"c12_ch{chapter['number']:02d}_{slug(section)}_{kind}"
                questions = generated_questions(chapter, section, topic, kind, difficulty)
                module = {
                    "module_id": module_id,
                    "topic_name": f"{section} {topic} - {kind_label}",
                    "explanation": explanation_for(chapter, topic, kind_label, difficulty),
                    "difficulty": difficulty,
                    "total_timer_minutes": max(5, round((len(questions) * timer_for(difficulty)) / 60)),
                    "questions": questions,
                }
                chapter_obj["modules"].append(module)
                chapter_manifest["modules"].append({
                    "module_id": module_id,
                    "section": section,
                    "topic": topic,
                    "page": page,
                    "volume": chapter["volume"],
                    "month": chapter["month"],
                    "question_count": len(questions),
                    "source_basis": "PDF table of contents, chapter topic sequence, chapter concept summary, textbook exercise pattern",
                    "question_ids": [q["question_id"] for q in questions],
                })
                manifest["question_total"] += len(questions)
                manifest["module_total"] += 1

        review_difficulty = chapter["difficulty"]
        review_questions = []
        for idx, (section, topic, page) in enumerate(chapter["topics"], start=1):
            fact, answer = chapter["concepts"][(idx - 1) % len(chapter["concepts"])]
            review_questions.append(make_question(
                idx,
                f"Chapter review: which idea best supports '{section} {topic}'?",
                answer,
                [w for _, w in chapter["concepts"] if w != answer] + DISTRACTORS,
                fact,
                timer_for(review_difficulty),
            ))
        while len(review_questions) < 15:
            idx = len(review_questions) + 1
            section, topic, page = chapter["topics"][(idx - 1) % len(chapter["topics"])]
            review_questions.append(make_question(
                idx,
                f"Chapter review: '{topic}' is placed under which chapter in the Class 12 textbook?",
                chapter["title"],
                [c["title"] for c in CHAPTERS if c["title"] != chapter["title"]],
                f"The table of contents places section {section} under Chapter {chapter['number']}: {chapter['title']}.",
                timer_for(review_difficulty),
            ))
        review_module_id = f"c12_ch{chapter['number']:02d}_chapter_review"
        review_module = {
            "module_id": review_module_id,
            "topic_name": f"Chapter {chapter['number']} Review - {chapter['title']}",
            "explanation": explanation_for(chapter, chapter["title"], "Board Practice", review_difficulty),
            "difficulty": review_difficulty,
            "total_timer_minutes": round((len(review_questions) * timer_for(review_difficulty)) / 60),
            "questions": review_questions,
        }
        chapter_obj["modules"].append(review_module)
        chapter_manifest["modules"].append({
            "module_id": review_module_id,
            "section": f"Chapter {chapter['number']}",
            "topic": "Chapter Review",
            "page": chapter["topics"][0][2],
            "volume": chapter["volume"],
            "month": chapter["month"],
            "question_count": len(review_questions),
            "source_basis": "Full chapter review generated from textbook chapter sections",
            "question_ids": [q["question_id"] for q in review_questions],
        })
        manifest["question_total"] += len(review_questions)
        manifest["module_total"] += 1
        curriculum.append(chapter_obj)
        manifest["chapters"].append(chapter_manifest)

    validate(curriculum, manifest)
    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(curriculum, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MANIFEST}")
    print(f"Modules: {manifest['module_total']}; Questions: {manifest['question_total']}")


def validate(curriculum, manifest):
    assert len(curriculum) == 12, "Expected 12 chapters"
    assert manifest["question_total"] >= 2500, "Question target not met"
    module_ids = set()
    for chapter in curriculum:
        assert "chapter_name" in chapter and chapter["modules"], "Invalid chapter"
        for module in chapter["modules"]:
            assert module["module_id"] not in module_ids, f"Duplicate module id {module['module_id']}"
            module_ids.add(module["module_id"])
            assert module["difficulty"] in {"Easy", "Medium", "Hard"}
            assert len(module["explanation"].split()) <= 150
            assert 5 <= len(module["questions"]) <= 15, module["module_id"]
            for question in module["questions"]:
                assert len(question["options"]) == 4
                assert question["correct_answer"] in question["options"]
                assert question["timer_per_question_seconds"] in {30, 45, 60}


if __name__ == "__main__":
    build()
