import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "src" / "data"
OUTPUT_JSON = DATA_DIR / "cbse_class5_mathematics_learning_journey.json"
OUTPUT_MANIFEST = DATA_DIR / "cbse_class5_mathematics_validation_manifest.json"


def choices(correct, wrongs):
    values = [correct]
    for wrong in wrongs:
        if wrong != correct and wrong not in values:
            values.append(wrong)
        if len(values) == 4:
            break
    while len(values) < 4:
        values.append(["Not sure", "Both", "None"][len(values) - 1])
    return [values[i] for i in [1, 3, 0, 2]]


def q(question_id, text, correct, wrongs, rationale, timer):
    return {
        "question_id": question_id,
        "question_text": text,
        "options": choices(correct, wrongs),
        "correct_answer": correct,
        "rationale": rationale,
        "timer_per_question_seconds": timer,
    }


def slug(value):
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


CHAPTERS = [
    ("We the Travellers - I", "eemm101.pdf", [
        ("Large Numbers and Ten Thousands", "Medium", "Large numbers are built by grouping tens. Ten ones make a ten, ten tens make a hundred, ten hundreds make a thousand, and ten thousands make 10,000. The chapter adds a TTh column for ten thousand and uses commas to make large numbers easier to read.",
         [("10 thousands make ____.", "Ten thousand", ["One thousand", "One hundred", "One lakh"], "The PDF says 10 Thousands = Ten Thousand = 10,000."),
          ("Ten thousand is written as ____.", "10,000", ["1,000", "100", "9,000"], "The chapter asks how to write ten thousand."),
          ("TTh stands for ____.", "Ten Thousand", ["Thousand", "Ten", "Hundred"], "The place value chart adds a TTh column."),
          ("We use a comma to read large numbers ____.", "Easily", ["As fractions", "As angles", "As weights"], "The PDF states commas help us read large numbers easily."),
          ("Adding 1,000 to 9,000 gives ____.", "10,000", ["9,100", "8,000", "1,000"], "9,000 + 1,000 = 10,000.")]),
        ("Indian Place Value Reading", "Medium", "The Indian place value system uses the same digits 0-9 in different places. A number like 1,380 is 1 thousand, 3 hundreds, 8 tens, and 0 ones. Place value is like an address: a digit's value depends on where it stands.",
         [("1,380 has ____ thousand.", "1", ["3", "8", "0"], "The PDF writes 1,380 as 1 Thousand + 3 Hundreds + 8 Tens + 0 Ones."),
          ("1,380 has ____ hundreds.", "3", ["1", "8", "0"], "The hundreds digit in 1,380 is 3."),
          ("9,123 has ____ thousands.", "9", ["1", "2", "3"], "The PDF writes 9,123 as 9 Thousands + 1 Hundred + 2 Tens + 3 Ones."),
          ("9,123 has ____ tens.", "2", ["9", "1", "3"], "The tens digit is 2."),
          ("A digit's value depends on its ____.", "Place", ["Colour", "Shape", "Weight"], "Place value gives meaning to each digit.")]),
    ]),
    ("Fractions", "eemm102.pdf", [
        ("Comparing Fractions of Wholes", "Medium", "A fraction is a part of a whole, but the whole matters. Tamanna compares parts of two different chocolates. One-third of a large chocolate can be bigger than one-half of a small chocolate. Fractions are fairly compared when the wholes are the same size.",
         [("To compare fractions of two wholes, the wholes should be ____.", "Same", ["Different", "Hidden", "Unequal always"], "The PDF says the wholes must be the same."),
          ("Tamanna has two chocolates of different ____.", "Sizes", ["Colours only", "Dates", "Weights only"], "The chapter says the chocolates are of different sizes."),
          ("1/2 of a small whole can be ____ than 1/3 of a big whole.", "Smaller", ["Always bigger", "Always equal", "Not a fraction"], "The whole size affects the part size."),
          ("In Grid A, children shade ____ in red.", "1/8", ["1/6", "1/12", "1/2"], "The PDF says shade 1/8 of Grid A in red."),
          ("In Grid B, children shade ____ in blue.", "1/6", ["1/8", "1/12", "1/3"], "The PDF says shade 1/6 of Grid B in blue.")]),
        ("Equivalent Fractions", "Medium", "Equivalent fractions name the same amount in different ways. In the fraction kit, one half can be made by two one-fourth pieces, so 1/2 = 2/4. The chapter also shows 1/3 = 2/6. Equivalent fractions are like different names for the same part.",
         [("Two pieces of 1/4 are equal to ____.", "1/2", ["1/3", "1/5", "1/8"], "The PDF states 2 pieces of 1/4 are equal to 1/2."),
          ("1/2 is equivalent to ____.", "2/4", ["1/4", "3/4", "2/3"], "The chapter writes 1/2 = 2/4."),
          ("1/3 is equivalent to ____.", "2/6", ["1/6", "3/6", "2/3"], "The PDF says 1/3 = 2/6."),
          ("How many 1/5 pieces make a whole?", "5", ["2", "4", "10"], "Five fifths make one whole."),
          ("Equivalent fractions show the ____ amount.", "Same", ["Double always", "Smaller always", "Hidden"], "Equivalent means equal in value.")]),
    ]),
    ("Angles as Turns", "eemm103.pdf", [
        ("Full, Half and Quarter Turns", "Medium", "Angles can be understood as turns. A full turn brings you back to the starting position, a half turn faces the opposite way, and a quarter turn is one-fourth of a full turn. The Statue game and giant wheel help children see turns in movement.",
         [("A full turn brings you back to the ____ position.", "Starting", ["Opposite", "Hidden", "Quarter"], "The chapter says a full turn comes back to the initial position."),
          ("Two half turns in the same direction make a ____ turn.", "Full", ["Quarter", "No", "One-eighth"], "Two halves make one full turn."),
          ("Two quarter turns make a ____ turn.", "Half", ["Full", "Three-quarter", "No"], "2 quarters = 1 half."),
          ("Four quarter turns make a ____ turn.", "Full", ["Half", "Quarter", "No"], "4 quarters = 1 full turn."),
          ("The minute hand makes a full turn when it returns to its ____ position.", "Initial", ["Quarter", "Different", "Hidden"], "The PDF mentions the minute hand returning to its initial position.")]),
        ("Turns in Everyday Objects", "Medium", "Many objects turn: taps, doors, tongs, scissors, clothes clips, and file covers. Some turn less than a quarter, some a quarter, and some more. Noticing turns helps children connect angles to actions they already know.",
         [("A door with a hinge shows a ____.", "Turn", ["Fraction only", "Weight", "Comma"], "The PDF lists door with hinge in the turn table."),
          ("The chapter asks whether objects make a ____ turn.", "Half", ["Lakh", "Gram", "Pictograph"], "The table asks which objects make a half turn."),
          ("A giant wheel makes a full turn when it returns to point ____.", "E", ["A", "B", "C"], "The sampled page says starting position E."),
          ("A quarter turn is ____ of a full turn.", "1/4", ["1/2", "1/3", "2/4"], "Quarter means one-fourth."),
          ("Angles as turns are seen through ____.", "Movement", ["Only money", "Only data", "Only weight"], "The chapter teaches angles through turning movement.")]),
    ]),
    ("We the Travellers - II", "eemm104.pdf", [
        ("Equal Sums and Number Swaps", "Medium", "This chapter begins with groups of numbers and asks what happens when numbers are interchanged. Swapping numbers can balance sums. It is like adjusting weights on two sides: if both totals become equal, the swap worked.",
         [("Interchanging numbers can make two sums ____.", "Equal", ["Always larger", "Always smaller", "Fractions"], "The PDF asks learners to interchange pairs to make sums equal."),
          ("Balancing sums means both totals are the ____.", "Same", ["Different", "Hidden", "Rounded"], "Equal sums have the same total."),
          ("If 2 and 5 are interchanged, the ____ may change.", "Sums", ["Fuel type", "Angle", "Weight"], "The opening task asks what happens to sums after interchanging."),
          ("A number swap is useful when comparing ____ groups.", "Two", ["Only one", "No", "Ten thousand"], "The task shows two groups of numbers."),
          ("Checking equality needs calculating each ____.", "Total", ["Turn", "Litre", "Icon"], "Equal sums require total comparison.")]),
        ("Fuel Arithmetic", "Medium", "Fuel arithmetic uses addition and subtraction with litres. A lorry with 28 litres gets 75 more litres, so the total is 28 l + 75 l. The chapter also reminds us to save fuel because it is limited and reducing fuel use lowers pollution.",
         [("A lorry has 28 litres and 75 litres more is filled. Total fuel is ____ litres.", "103", ["93", "75", "28"], "28 + 75 = 103."),
          ("Fuel quantity is measured in ____.", "Litres", ["Metres", "Grams", "Turns"], "The chapter uses litres for fuel."),
          ("Motorbikes may need about 5 to ____ litres of fuel.", "15", ["50", "500", "5000"], "The PDF says motorbikes vary from 5 to 15 litres."),
          ("A train may need about ____ litres of fuel.", "5000", ["50", "500", "15"], "The PDF says 5,000 litres in the case of a train."),
          ("Saving fuel helps reduce ____.", "Pollution", ["Fractions", "Symmetry", "Perimeter"], "The PDF links saving fuel with cutting down pollution.")]),
    ]),
    ("Far and Near", "eemm105.pdf", [
        ("Metres and Centimetres", "Medium", "Distance and length can be measured in metres or centimetres. One metre equals 100 centimetres, so 2 m equals 200 cm and 500 cm equals 5 m. Choosing the right unit makes measurements easier to read.",
         [("1 metre equals ____ centimetres.", "100", ["10", "1000", "50"], "The double number line shows 100 cm = 1 m."),
          ("2 metres equals ____ centimetres.", "200", ["20", "100", "500"], "2 × 100 cm = 200 cm."),
          ("500 cm equals ____ metres.", "5", ["50", "500", "2"], "500 cm = 5 m."),
          ("The height of India Gate is measured in ____.", "Metres", ["Centimetres only", "Grams", "Litres"], "A building height is suited to metres."),
          ("The length of a mobile phone is measured in ____.", "Centimetres", ["Kilometres", "Metres only", "Litres"], "A small object is suited to centimetres.")]),
        ("Comparing Lengths", "Medium", "Length comparison becomes easier when units match. For example, 456 cm is less than 5 m because 5 m is 500 cm. The chapter asks children to compare rods and statue heights using <, =, and > signs.",
         [("456 cm is ____ 5 m.", "Less than", ["Greater than", "Equal to", "Not comparable"], "5 m = 500 cm, so 456 cm is less."),
          ("55 cm + 200 cm is ____ 200 cm + 54 cm.", "Greater than", ["Less than", "Equal to", "Impossible"], "255 cm is greater than 254 cm."),
          ("6 m 5 cm is ____ 6 m 50 cm.", "Less than", ["Greater than", "Equal to", "Same"], "6 m 5 cm = 605 cm and 6 m 50 cm = 650 cm."),
          ("238 cm is ____ 138 cm + 1 m.", "Equal to", ["Less than", "Greater than", "No relation"], "138 cm + 100 cm = 238 cm."),
          ("Use <, =, > after converting to the same ____.", "Unit", ["Colour", "Angle", "Icon"], "Comparing lengths needs common units.")]),
    ]),
    ("The Dairy Farm", "eemm106.pdf", [
        ("Multiplication Facts and Factors", "Medium", "The Dairy Farm continues multiplication. Shapes hide numbers, and the same shape means the same number. Children use known facts like 30 × 2 = 60 to discover missing factors and build flexible multiplication thinking.",
         [("30 × 2 = ____.", "60", ["32", "30", "90"], "The PDF gives 30 × 2 = 60."),
          ("In the shape puzzles, the same shape denotes the same ____.", "Number", ["Unit", "Turn", "Icon"], "The PDF states the same shape denotes the same number."),
          ("A factor is a number that is ____ to get a product.", "Multiplied", ["Measured", "Folded", "Weighed"], "Factors multiply to make products."),
          ("If __ × 5 = 60, the missing number is ____.", "12", ["10", "15", "55"], "12 × 5 = 60."),
          ("Multiplication facts help solve hidden ____.", "Numbers", ["Calendars", "Directions", "Pictographs"], "The task asks learners to find numbers hidden in shapes.")]),
        ("Number Clues and Operations", "Hard", "The chapter asks 'Which number am I?' using clues like multiple, odd, greater than, less than, tens digit, and ones digit. This is mathematical detective work: remove impossible numbers until one number satisfies all clues.",
         [("A number that is a multiple of 9 and less than 50 could be ____.", "18", ["16", "22", "44"], "18 is a multiple of 9 and less than 50."),
          ("An odd number has ones digit ____.", "Odd", ["Even", "Zero always", "Ten"], "Odd numbers end in 1, 3, 5, 7, or 9."),
          ("A multiple of 4 is exactly divisible by ____.", "4", ["9", "11", "5"], "Multiples of 4 divide by 4 with no remainder."),
          ("4 - 2 forms the number ____.", "2", ["6", "8", "0"], "The PDF gives 2 can be formed as 4 - 2."),
          ("Clue-based problems require checking ____ clues.", "All", ["Only first", "No", "Random"], "The correct number must satisfy every clue.")]),
    ]),
    ("Shapes and Patterns", "eemm107.pdf", [
        ("Weaving Patterns", "Medium", "Woven mats use repeating over-under patterns. One row may go 1 under, 1 over, and the next may go 1 over, 1 under. Such alternating patterns create beautiful designs and help children describe repetition precisely.",
         [("Row 1 of the simple weave is 1 under, 1 ____.", "Over", ["Down", "Litre", "Half"], "The PDF describes Row 1 as 1 under, 1 over."),
          ("Row 2 begins 1 over, 1 ____.", "Under", ["Hundred", "Gram", "Angle"], "The PDF describes Row 2 as 1 over, 1 under."),
          ("The mat uses paper strips of ____ colours.", "Two", ["One", "Five", "Ten"], "The activity uses 8 strips of two colours."),
          ("The coloured paper is 30 cm long and ____ cm wide.", "20", ["3", "8", "100"], "The PDF gives 30 cm long and 20 cm wide."),
          ("A repeating over-under order is a ____.", "Pattern", ["Weight", "Distance", "Fraction"], "Repeating arrangements form patterns.")]),
        ("Geometric Designs with Strips", "Medium", "Paper weaving turns geometry into craft. Equal-width strips and equal slits create rows and columns. By changing the rule, such as 2 over and 1 under, children see how a small rule can produce a new pattern.",
         [("The strips are ____ cm wide.", "3", ["8", "20", "30"], "The PDF says strips are 3 cm wide."),
          ("The activity uses ____ paper strips.", "8", ["3", "20", "30"], "The PDF says cut 8 paper strips."),
          ("Changing from 1 over-1 under to 2 over-1 under changes the ____.", "Pattern", ["Unit", "Weight", "Time"], "A different rule creates a different design."),
          ("Equal slits help strips weave in ____ rows.", "Neat", ["Random", "Hidden", "Unequal"], "Equal distances create orderly weaving."),
          ("Weaving shows patterns using shape and ____.", "Colour", ["Fuel", "TV hours", "Coconut only"], "The mat uses two colours in patterns.")]),
    ]),
    ("Weight and Capacity", "eemm108.pdf", [
        ("Reading Weighing Scales", "Medium", "Weight tells how heavy something is. The chapter asks children to check recorded weights and read scales in kg and g. A bed may be in kilograms, but a sofa written as 30 g is unreasonable. Estimation and scale reading work together.",
         [("Kilogram is written as ____.", "kg", ["g", "cm", "l"], "The chapter uses kg for kilogram."),
          ("Gram is written as ____.", "g", ["kg", "m", "l"], "The chapter uses g for gram."),
          ("A bed recorded as 60 kg looks ____.", "Reasonable", ["Impossible", "A fraction", "A direction"], "A bed can be measured in kilograms."),
          ("An iron almirah recorded as 40 g looks ____.", "Incorrect", ["Correct", "A capacity", "A turn"], "40 g is too light for an iron almirah."),
          ("A weighing scale helps find ____.", "Weight", ["Length only", "Angles only", "Directions"], "The activity asks children to read scales.")]),
        ("Capacity and Unit Conversion", "Medium", "Capacity tells how much a container can hold, while weight tells how heavy it is. The chapter uses water bottles, buckets, grams, kilograms, and scale marks. Reading units carefully prevents mixing up kg, g, litre, and millilitre.",
         [("A water bottle recorded as 650 g is a measure of ____.", "Weight", ["Length", "Time", "Direction"], "650 g is a weight measure."),
          ("1 kg equals ____ g.", "1000", ["100", "10", "500"], "Standard conversion: 1 kg = 1000 g."),
          ("250 g + 250 g = ____ g.", "500", ["250", "1000", "750"], "Two 250 g parts make 500 g."),
          ("A bucket may be described using both weight and ____.", "Capacity", ["Angle", "Symmetry", "Pictograph"], "Buckets can be weighed and can hold liquid."),
          ("Correct measurement needs reading both number and ____.", "Unit", ["Colour", "Icon", "Turn"], "Units tell what is being measured.")]),
    ]),
    ("Coconut Farm", "eemm109.pdf", [
        ("Multiplication and Division Facts", "Hard", "Division and multiplication are partners. If 5 × 7 = 35, then 35 ÷ 5 = 7 and 35 ÷ 7 = 5. The coconut array helps children see groups, group size, dividend, divisor, and quotient.",
         [("If 5 × 7 = 35, then 35 ÷ 7 = ____.", "5", ["7", "35", "12"], "The PDF states 35 ÷ 7 = 5."),
          ("If 5 × 7 = 35, then 35 ÷ 5 = ____.", "7", ["5", "35", "1"], "The PDF states 35 ÷ 5 = 7."),
          ("35 ÷ 1 = ____.", "35", ["1", "5", "7"], "Any number divided by 1 is itself."),
          ("Dividend = Divisor × ____.", "Quotient", ["Remainder only", "Fraction", "Icon"], "The PDF states Dividend = Divisor × Quotient."),
          ("In 35 ÷ 7 = 5, the quotient is ____.", "5", ["35", "7", "1"], "The answer to division is the quotient.")]),
        ("Large Products and Related Division", "Hard", "The chapter asks learners to solve large multiplication problems and write two related division facts. For example, 30 × 30 = 900, so 900 ÷ 30 = 30. This strengthens the connection between products and quotients.",
         [("30 × 30 = ____.", "900", ["60", "300", "90"], "30 × 30 = 900."),
          ("400 × 8 = ____.", "3200", ["408", "320", "4008"], "400 multiplied by 8 is 3200."),
          ("15 × 60 = ____.", "900", ["75", "600", "150"], "15 × 60 = 900."),
          ("200 × 16 = ____.", "3200", ["216", "1600", "20016"], "200 × 16 = 3200."),
          ("From one multiplication fact we can write ____ division facts.", "Two", ["No", "One only", "Four always"], "The PDF asks for two division statements from each product.")]),
    ]),
    ("Symmetrical Designs", "eemm110.pdf", [
        ("Alphabet Symmetry", "Medium", "Symmetry helps make neat alphabet cutouts. The letter A has a vertical line of symmetry, and H has two lines of symmetry. Folding paper along a symmetry line lets children draw only half or one-fourth and open it to see the full letter.",
         [("The letter A has a ____ line of symmetry.", "Vertical", ["Horizontal only", "No", "Diagonal only"], "The PDF says A has a vertical line of symmetry."),
          ("The letter H has ____ lines of symmetry.", "Two", ["One", "Three", "No"], "The PDF says H has two lines of symmetry."),
          ("To cut A, draw half of the letter along the ____.", "Fold", ["Scale", "Clock", "Map"], "The steps say draw half along the fold."),
          ("A symmetrical cutout is made by folding ____.", "Paper", ["Water", "Fuel", "Milk"], "The activity uses folded paper."),
          ("Letters can have vertical, horizontal, or both lines of ____.", "Symmetry", ["Division", "Weight", "Capacity"], "The questions ask for horizontal and vertical lines of symmetry.")]),
        ("Firkis and Symmetric Designs", "Medium", "Firkis, diyas, boats, and paper designs can use symmetry. A square paper folded diagonally makes triangles and an X shape. Symmetry helps balance the design so it looks neat from matching sides.",
         [("A firki begins with a ____ paper.", "Square", ["Circular", "Triangular only", "Long strip"], "The PDF says take a square paper."),
          ("Folding the square diagonally makes two ____.", "Triangles", ["Circles", "Rectangles only", "Lines only"], "The steps say fold diagonally to make two triangles."),
          ("After folding both ways, an ____ shape appears.", "X", ["A", "H", "O"], "The PDF says you will see an X shape."),
          ("A balanced design often has ____.", "Symmetry", ["Incorrect units", "Only weight", "Only data"], "Symmetry creates matching sides."),
          ("The chapter asks children to make cutouts of diya and ____.", "Boat", ["TV", "Fuel tank", "Coconut"], "The PDF mentions diya, boat, and other designs.")]),
    ]),
    ("Grandmother's Quilt", "eemm111.pdf", [
        ("Perimeter of Shapes", "Medium", "Perimeter is the length of the border of a shape. Grandmother wants lace around a quilt, so she needs the perimeter. If all sides of a square are equal, add all sides to find the border length.",
         [("The length of the border of a shape is called ____.", "Perimeter", ["Area", "Capacity", "Factor"], "The PDF states this definition."),
          ("A square with side 4 cm has perimeter ____ cm.", "16", ["8", "12", "20"], "4 + 4 + 4 + 4 = 16."),
          ("A rectangle of 5 cm and 4 cm has perimeter ____ cm.", "18", ["9", "20", "16"], "5 + 4 + 5 + 4 = 18."),
          ("Lace around a quilt measures its ____.", "Perimeter", ["Area", "Weight", "Time"], "Lace covers the border."),
          ("Perimeter is measured in units of ____.", "Length", ["Weight", "Capacity", "Data"], "Perimeter is a length around a boundary.")]),
        ("Area and Tiling", "Medium", "Area is the region covered by a shape. The quilt and table activities use triangles, squares, and rectangles to cover without gaps or overlaps. Circles leave gaps, so they do not tile a flat region neatly.",
         [("The region covered by shapes is called ____.", "Area", ["Perimeter", "Weight", "Direction"], "The PDF defines the region covered as area."),
          ("Squares and rectangles can cover a table without ____.", "Gaps", ["Units", "Numbers", "Factors"], "The PDF discusses no gaps and overlaps."),
          ("Circles usually leave ____ when tiling a table.", "Gaps", ["No space", "Only borders", "Perimeter"], "The PDF asks whether circles tile and notes gaps."),
          ("Area can be counted in square ____.", "Units", ["Litres", "Kilograms", "Hours"], "Area is counted using unit shapes."),
          ("Tiles used for area should not ____.", "Overlap", ["Count", "Measure", "Touch at edges"], "Tiling means no gaps and no overlaps.")]),
    ]),
    ("Racing Seconds", "eemm112.pdf", [
        ("Elapsed Time", "Medium", "Elapsed time is how long an activity takes. Raghav's yoga and the painting table ask children to find start time, finish time, and duration. Think of time as a number line: jump from start to finish and count the hours and minutes.",
         [("Raghav practises ____ in the morning.", "Yoga", ["Weaving", "Fuel arithmetic", "Bird watching"], "The PDF says Raghav practices yoga in the morning."),
          ("01:15 p.m. to 01:42 p.m. is ____ minutes.", "27", ["17", "42", "57"], "42 - 15 = 27 minutes."),
          ("03:18 p.m. to 08:18 p.m. is ____ hours.", "5", ["3", "8", "11"], "The minutes match, so it is 5 hours."),
          ("Rani took 2 hours 10 minutes, Ritu 1 hour 35 minutes. Who took longer?", "Rani", ["Ritu", "Both same", "Raghav"], "2 h 10 min is longer than 1 h 35 min."),
          ("Elapsed time means time ____.", "Taken", ["Weighed", "Folded", "Pictured"], "Duration is the time taken.")]),
        ("12-Hour and 24-Hour Time", "Medium", "Time can be written in 12-hour format with a.m./p.m. or in 24-hour format. For afternoon and evening p.m. times, add 12 to the hour. So 02:30 p.m. becomes 14:30 hours.",
         [("02:30 p.m. is ____ hours in 24-hour format.", "14:30", ["02:30", "12:30", "24:30"], "The PDF table shows 02:30 p.m. = 14:30 hours."),
          ("05:30 a.m. is ____ hours.", "05:30", ["17:30", "15:30", "00:30"], "Morning a.m. times keep the same hour."),
          ("05:30 p.m. is ____ hours.", "17:30", ["05:30", "15:30", "07:30"], "For p.m., add 12 to 5."),
          ("09:35 p.m. is ____ hours.", "21:35", ["09:35", "19:35", "23:35"], "For p.m., 9 + 12 = 21."),
          ("24-hour time avoids using ____.", "a.m./p.m.", ["Minutes", "Hours", "Numbers"], "24-hour format does not need a.m. or p.m.")]),
    ]),
    ("Animal Jumps", "eemm113.pdf", [
        ("Factors and Multiples", "Hard", "Animal Jumps uses boxes, arrays, and jumps to explore factors and multiples. Factors multiply to make a number; multiples are products. For 12, the factors include 1, 2, 3, 4, 6, and 12 because each divides 12 completely.",
         [("1, 2, 3, 4, 6 and 12 are factors of ____.", "12", ["15", "28", "37"], "The PDF states these are all factors of 12."),
          ("3 × 4 = ____.", "12", ["7", "15", "34"], "The chapter shows 3 × 4 = 12."),
          ("2 × 6 = ____.", "12", ["8", "26", "14"], "The chapter shows 2 × 6 = 12."),
          ("The product of factors gives a ____.", "Multiple", ["Fraction", "Map", "Pictograph"], "The PDF says product of factors gives a multiple."),
          ("A factor divides a number ____.", "Completely", ["Partly always", "With a clock", "By direction"], "The PDF says factors divide 12 completely.")]),
        ("Prime Numbers and Common Multiples", "Hard", "Some numbers, like 13 and 37, are prime because they have only two factors: 1 and themselves. The chapter also uses rabbit and frog jumps to find common multiples of 3 and 4, with 12 as the first common multiple.",
         [("13 and 37 are called ____ numbers.", "Prime", ["Composite only", "Fraction", "Directional"], "The PDF asks why 13 and 37 are prime numbers."),
          ("The first common multiple of 3 and 4 is ____.", "12", ["7", "10", "15"], "The PDF states 12 is the first common multiple of 3 and 4."),
          ("A rabbit takes a jump of ____ each time.", "4", ["3", "5", "12"], "The PDF says the rabbit takes a jump of 4."),
          ("A frog takes a jump of ____ each time.", "3", ["4", "6", "12"], "The PDF says the frog takes a jump of 3."),
          ("A prime number has factors 1 and ____.", "Itself", ["2 always", "All numbers", "0 only"], "Prime numbers have exactly two factors.")]),
    ]),
    ("Maps and Locations", "eemm114.pdf", [
        ("Cardinal Directions", "Medium", "Maps and locations begin with directions. If Manu faces the rising Sun, he faces East. Then his left hand points North, his right hand points South, and West is behind him. Directions help us describe places clearly.",
         [("The rising Sun is in the ____.", "East", ["West", "North", "South"], "The chapter asks learners to face the rising Sun."),
          ("If Manu faces East, his left hand points ____.", "North", ["South", "East", "West"], "Facing East, left is North."),
          ("If Manu faces East, his right hand points ____.", "South", ["North", "East", "West"], "Facing East, right is South."),
          ("The direction opposite East is ____.", "West", ["North", "South", "Up"], "East and West are opposite directions."),
          ("North, South, East and West are ____ directions.", "Cardinal", ["Fraction", "Weight", "Data"], "The teacher note mentions the four cardinal directions.")]),
        ("Reading Locations on a Map", "Medium", "A map is like a bird's-eye view of a place. In the bird-watching camp, children use clues such as west of the road to colour tents. Location language like north, south, east, west, left, and right helps us follow map clues.",
         [("The chapter has a bird-watching ____.", "Camp", ["Museum", "Dairy", "Quilt"], "The sampled page says children are at a bird-watching camp."),
          ("The tent west of the road is located using a ____ clue.", "Direction", ["Weight", "Fraction", "Factor"], "West is a direction."),
          ("The Siberian Crane flies from Siberia to ____.", "India", ["Australia", "Africa", "Moon"], "The PDF says these birds fly to India."),
          ("A map usually shows a place from ____.", "Above", ["Inside", "Underground only", "Behind only"], "Maps are top-view representations."),
          ("Directions help us find a ____.", "Path", ["Weight", "Product only", "TV hour"], "The chapter asks how birds and humans find paths.")]),
    ]),
    ("Data Through Pictures", "eemm115.pdf", [
        ("Collecting and Reading Data", "Medium", "Samaira and Kabir act like reporters and collect data from 35 friends about TV watching. Data begins with a question, then responses are recorded in a table so we can compare categories like half an hour, one hour, two hours, and more than two hours.",
         [("Samaira and Kabir collected data from ____ friends.", "35", ["15", "30", "50"], "The PDF says they collected data from 35 friends."),
          ("Their question is about hours spent watching ____.", "TV", ["Birds", "Fuel", "Coconuts"], "The chapter asks how many hours a day children watch TV."),
          ("Data collection begins with a ____.", "Question", ["Weight scale", "Compass", "Turn"], "Reporters ask a question to collect information."),
          ("A table helps organise ____.", "Responses", ["Directions only", "Angles only", "Fractions only"], "The TV data is recorded in a table."),
          ("Watching TV for a long time can be harmful to the ____.", "Eyes", ["Map", "Fuel", "Quilt"], "The page asks whether long TV watching harms eyes.")]),
        ("Pictographs and Icons", "Medium", "A pictograph uses pictures or icons to show data. Joseph Uncle has too many toys and sports items to draw one picture for every item, so one icon can represent many items. This makes large data easier to read.",
         [("A pictograph shows data using ____.", "Pictures", ["Only words", "Only fractions", "Only directions"], "The chapter title is Data Through Pictures."),
          ("Joseph Uncle takes stock of play items in his ____.", "Store", ["Dairy farm", "Museum only", "Map"], "The PDF says he takes stock in his store."),
          ("One icon can represent ____ item or many items.", "One", ["No", "Only half", "Only prime"], "The chapter discusses using one picture for items."),
          ("Using one picture for every item is hard when there are ____ items.", "Too many", ["No", "Only two", "Equal halves"], "Joseph notices too many items make one-picture-per-item difficult."),
          ("A pictograph key tells what each ____ means.", "Icon", ["Direction", "Factor", "Turn"], "A key explains the value of each picture.")]),
    ]),
]


def build():
    output = []
    manifest = {
        "source": "NCERT Maths Mela Grade 5 PDFs, reprint 2026-27",
        "syllabus": "CBSE",
        "class": "Class 5",
        "subject": "Mathematics",
        "chapters": [],
        "module_total": 0,
        "question_total": 0,
    }
    counter = 1
    for chapter_name, pdf, modules in CHAPTERS:
        chapter_obj = {"chapter_name": chapter_name, "modules": []}
        chapter_manifest = {"chapter_name": chapter_name, "pdf": pdf, "modules": []}
        for topic, difficulty, explanation, facts in modules:
            timer = {"Easy": 30, "Medium": 45, "Hard": 60}[difficulty]
            questions = [q(i + 1, *fact, timer) for i, fact in enumerate(facts)]
            module_id = f"cbse_c5_m{counter:03d}_{slug(topic)}"
            counter += 1
            module = {
                "module_id": module_id,
                "topic_name": topic,
                "explanation": explanation,
                "difficulty": difficulty,
                "total_timer_minutes": max(4, round((len(questions) * timer) / 60)),
                "questions": questions,
            }
            chapter_obj["modules"].append(module)
            chapter_manifest["modules"].append({
                "module_id": module_id,
                "topic_name": topic,
                "question_count": len(questions),
                "source_basis": "PDF contents page, chapter opening activity, and sampled textbook problem context",
            })
            manifest["module_total"] += 1
            manifest["question_total"] += len(questions)
        output.append(chapter_obj)
        manifest["chapters"].append(chapter_manifest)
    validate(output)
    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MANIFEST}")
    print(f"Chapters: {len(output)}; Modules: {manifest['module_total']}; Questions: {manifest['question_total']}")


def validate(output):
    assert len(output) == 15
    ids = set()
    for chapter in output:
        assert chapter["chapter_name"]
        assert chapter["modules"]
        for module in chapter["modules"]:
            assert module["module_id"] not in ids
            ids.add(module["module_id"])
            assert module["difficulty"] in {"Easy", "Medium", "Hard"}
            assert len(module["explanation"].split()) <= 150
            assert 5 <= len(module["questions"]) <= 15
            for question in module["questions"]:
                assert len(question["options"]) == 4
                assert question["correct_answer"] in question["options"]
                assert question["timer_per_question_seconds"] in {30, 45, 60}


if __name__ == "__main__":
    build()
