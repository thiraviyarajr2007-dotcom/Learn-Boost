import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "src" / "data"
OUTPUT_JSON = DATA_DIR / "cbse_class3_mathematics_learning_journey.json"
OUTPUT_MANIFEST = DATA_DIR / "cbse_class3_mathematics_validation_manifest.json"


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
    {
        "chapter_name": "What's in a Name?",
        "pdf": "cemm101.pdf",
        "modules": [
            ("Counting with Marks and Tallies", "Easy", "Before numbers were easy to write, people could still count by making marks. In this story, Deba and Deep mark one line for each cow going out and strike one line when a cow returns. Marks act like a memory helper: one mark stands for one object.",
             [
                 ("Deba and Deep used marks to keep track of ____.", "Cows", ["Calendars", "Beads", "Juice"], "The story says they made a mark for each cow leaving the gate."),
                 ("One mark on the wall stood for ____ cow.", "1", ["10", "100", "0"], "Each cow was matched with one mark."),
                 ("When a cow returned, they ____ one mark.", "Struck out", ["Added ten", "Coloured", "Folded"], "The story says they struck out one mark for each cow re-entering."),
                 ("If two marks are left, ____ cows are missing.", "2", ["20", "12", "0"], "Marks left over show cows not yet returned."),
                 ("This method helps count without first using ____.", "Number symbols", ["Walls", "Cows", "Friends"], "The note encourages strategies to count without using numbers."),
             ]),
            ("Tracking Groups of Animals", "Medium", "Counting marks can also track bigger groups, like Hemant's 36 cows and 23 sheep. First make a mark for each animal, then group marks to count more easily. This builds the idea that a number names how many objects are in a collection.",
             [
                 ("Hemant had 36 cows and ____ sheep.", "23", ["32", "13", "63"], "The PDF says Hemant had 36 cows and 23 sheep."),
                 ("36 is made of 3 tens and ____ ones.", "6", ["3", "9", "0"], "36 = 30 + 6."),
                 ("23 is made of 2 tens and ____ ones.", "3", ["2", "5", "0"], "23 = 20 + 3."),
                 ("36 cows are ____ than 23 sheep.", "More", ["Less", "Equal", "Half"], "36 is greater than 23."),
                 ("Keeping track means checking that nothing is ____.", "Lost", ["Folded", "Measured", "Painted"], "The story asks how to know cows were not lost."),
             ]),
        ],
    },
    {
        "chapter_name": "Toy Joy",
        "pdf": "cemm102.pdf",
        "modules": [
            ("3D Shapes in Toys", "Easy", "Boxes, bottles, cans, cones, cubes, cuboids, and cylinders can become toys. In Toy Joy, children make animal and bird faces on old boxes and bottles. This helps them see 3D shapes as real objects with faces, corners, and edges.",
             [
                 ("Jaya builds a rocket using different ____.", "Shapes", ["Calendars", "Marks", "Rupees"], "The PDF asks what shapes Jaya used in the rocket."),
                 ("A box can look like a ____.", "Cube or cuboid", ["Calendar", "Half", "Clock"], "The PDF mentions old boxes as cubes and cuboids."),
                 ("A bottle can look like a ____.", "Cylinder", ["Cone only", "Triangle", "Line"], "The PDF mentions bottles as cylinders."),
                 ("A cone has a ____ beak in the bird face example.", "Pointed", ["Flat", "Square", "Calendar"], "The page says the cone bird has a pointed beak."),
                 ("3D shapes have faces, corners and ____.", "Edges", ["Months", "Dates", "Rakhis"], "The page labels face, corner, and edge."),
             ]),
            ("Position and Arrangement of Solids", "Easy", "Shapes can be arranged above, under, between, and on top of one another. The rocket picture asks which shape is between two cuboids, on top of a cylinder, or under a cone. Shape arrangement helps children describe models clearly.",
             [
                 ("Which word describes a shape placed between two shapes?", "Between", ["Hundred", "Half", "Litre"], "The PDF asks which shape is between the red and yellow cuboids."),
                 ("Which word describes a shape above another shape?", "On the top", ["Under only", "Less than", "Yesterday"], "The PDF asks which shape is on top of the orange cylinder."),
                 ("Which word describes a shape below another shape?", "Under", ["After", "Calendar", "Capacity"], "The PDF asks which shape is under the pink cone."),
                 ("Children are asked to build houses, towers and ____.", "Rockets", ["Calendars", "Crows", "Juice"], "The chapter asks children to build houses, towers, rockets, etc."),
                 ("Looking from a distance helps us see visible ____ of shapes.", "Parts", ["Weeks", "Rupees", "Marks only"], "The activity asks what part of shapes can be seen from a distance."),
             ]),
        ],
    },
    {
        "chapter_name": "Double Century",
        "pdf": "cemm103.pdf",
        "modules": [
            ("Numbers up to 200", "Medium", "Double Century takes children beyond 100. They estimate objects like oranges, bangles, laddoos, barfi, bindis, and bananas, then count and check. Estimation is a thoughtful guess, while counting verifies the exact number.",
             [
                 ("Double Century focuses on numbers up to ____.", "200", ["20", "50", "1000"], "The chapter title and activities move beyond 100 toward 200."),
                 ("The first activity asks children to estimate oranges and ____.", "Bangles", ["Calendars", "Parathas", "Juice"], "The PDF lists oranges, bangles, laddoos, barfi, bindis, and bananas."),
                 ("A thoughtful guess before counting is called ____.", "Estimation", ["Folding", "Sharing", "Symmetry"], "The page asks children to estimate and write numbers."),
                 ("Counting after estimating helps us ____ the guess.", "Check", ["Hide", "Fold", "Decorate"], "Children estimate first and then count."),
                 ("Which number is more than 100?", "156", ["56", "99", "80"], "156 is beyond 100."),
             ]),
            ("Number Board and Place Value", "Medium", "The snakes and ladders board helps children read numbers, fill missing numbers, and move forward or backward. Bundles and loose sticks show place value: tens and ones help us build and compare numbers clearly.",
             [
                 ("A snakes and ladders board helps practise ____.", "Number order", ["Capacity only", "Calendar only", "Folding only"], "The PDF asks questions based on the snakes and ladders board."),
                 ("A ladder usually moves a player ____.", "Up", ["Down", "Sideways only", "Nowhere"], "In snakes and ladders, ladders take players upward."),
                 ("A snake usually moves a player ____.", "Down", ["Up", "To a calendar", "To a glass"], "Snake mouths send players down."),
                 ("96 plus 4 reaches ____.", "100", ["90", "104", "86"], "96 + 4 = 100."),
                 ("Bundles and loose sticks show ____ value.", "Place", ["Festival", "Capacity", "Symmetry"], "Bundles and loose sticks represent tens and ones."),
             ]),
        ],
    },
    {
        "chapter_name": "Vacation with My Nani Maa",
        "pdf": "cemm104.pdf",
        "modules": [
            ("Hidden Seeds and Complements", "Medium", "Nani Maa's magic trick uses the idea of a missing part. If total seeds are known and some are on the table, the hidden seeds are the remaining part. This is subtraction as finding the missing number.",
             [
                 ("If total seeds are 15 and 12 are on the table, hidden seeds are ____.", "3", ["27", "12", "5"], "15 - 12 = 3."),
                 ("If total seeds are 20 and 9 are on the table, hidden seeds are ____.", "11", ["29", "9", "10"], "20 - 9 = 11."),
                 ("The trick finds the ____ seeds.", "Hidden", ["Painted", "Measured", "Calendar"], "The table has Total Seeds, Seeds on the Table, and Hidden Seeds."),
                 ("Finding a missing part often uses ____.", "Subtraction", ["Only symmetry", "Only capacity", "Only calendar"], "Total minus known part gives hidden part."),
                 ("To make 10 from 7, we need ____ more.", "3", ["17", "7", "2"], "7 + 3 = 10."),
             ]),
            ("Addition and Subtraction Stories", "Medium", "The chapter continues with sweets and everyday situations. Children learn to combine, take away, and find what is left. Story problems become easier when you ask: What is the total? What is known? What is missing?",
             [
                 ("If Nandini had 7 balushahi and got 3 more, she has ____.", "10", ["4", "7", "13"], "7 + 3 = 10."),
                 ("If 17 total seeds have 10 on the table, hidden seeds are ____.", "7", ["27", "10", "17"], "17 - 10 = 7."),
                 ("If 19 total seeds have 8 on the table, hidden seeds are ____.", "11", ["27", "9", "8"], "19 - 8 = 11."),
                 ("A story problem should be read ____.", "Carefully", ["Without numbers", "Only backwards", "Never"], "Careful reading reveals total, known, and missing parts."),
                 ("The missing number is the part we need to ____.", "Find", ["Fold", "Measure", "Paint"], "Missing-part problems ask us to find the unknown amount."),
             ]),
        ],
    },
    {
        "chapter_name": "Fun with Shapes",
        "pdf": "cemm105.pdf",
        "modules": [
            ("Rangoli with Dots and Shapes", "Easy", "Rangoli designs use dots, straight lines, curved lines, and repeated shapes. Children copy Amma's rangoli, name the shapes, and count shapes made with curved and straight lines. This turns art into geometry.",
             [
                 ("Amma made a rangoli with dots and ____.", "Shapes", ["Calendars", "Juice", "Saplings"], "The PDF says Amma made a rangoli with dots and shapes."),
                 ("A circle is made with a ____ line.", "Curved", ["Straight only", "Calendar", "Hundred"], "Circles use curved lines."),
                 ("A square is made with ____ lines.", "Straight", ["Curved only", "Juice", "Months"], "Squares have straight sides."),
                 ("Children are asked to use shape cutouts to make a ____ design.", "Rangoli", ["Calendar", "Number line", "Glass"], "The PDF asks children to make a rangoli design with cutouts."),
                 ("Comparing two rangolis helps find similarities and ____.", "Differences", ["Litres", "Weeks", "Cows"], "The teacher note says compare similarities and differences."),
             ]),
            ("Folding, Nets and Shape Cutouts", "Medium", "When a box is opened carefully, its flat faces make a net. Children fold paper to make envelopes and use shape cutouts to build objects. Folding helps us see how flat shapes can become useful things.",
             [
                 ("Opening cardboard boxes shows flat ____.", "Shapes", ["Months", "Juice", "Marks"], "The PDF asks what shapes are seen in flattened boxes."),
                 ("An envelope can be made from a square piece of ____.", "Paper", ["Water", "Sand", "Glass"], "The PDF says use a square piece of paper."),
                 ("A flattened box can show a ____.", "Net", ["Calendar", "Crow", "Rakhi"], "A net is a flat layout of a solid."),
                 ("Folding changes a flat paper into a useful ____.", "Object", ["Month", "Capacity", "Number only"], "The envelope activity uses folding."),
                 ("Shape cutouts help children make ____.", "Objects", ["Only weeks", "Only litres", "Only crows"], "The PDF asks children to make objects using shape cutouts."),
             ]),
        ],
    },
    {
        "chapter_name": "House of Hundreds - I",
        "pdf": "cemm106.pdf",
        "modules": [
            ("Counting Beyond 200", "Medium", "At the mela, children count triangular torans, bangles, and toffees beyond 200. They count by hundreds, tens, and ones, such as 200 and 80 more is 280. Big numbers become easy when we group them.",
             [
                 ("Total triangles are 50 more than 200, which is ____.", "250", ["205", "300", "150"], "The PDF states 50 more than 200 is 250."),
                 ("200 and 80 more is ____.", "280", ["208", "180", "300"], "The PDF states total bangles are 280."),
                 ("298 + 1 = ____.", "299", ["300", "297", "288"], "The PDF shows 298 + 1 = 299."),
                 ("299 + 1 = ____.", "300", ["298", "310", "200"], "The PDF shows 299 + 1 = 300."),
                 ("Counting by hundreds, tens and ones helps with ____ numbers.", "Big", ["Only tiny", "No", "Calendar"], "Grouping makes large counts easier."),
             ]),
            ("Comparing Numbers Near 300", "Medium", "Numbers near 300 can be compared by asking how many more or less they are from 300. If there are 250 triangles, 50 more make 300. If there are 280 bangles, 20 more make 300. This builds flexible number sense.",
             [
                 ("How many more from 250 to make 300?", "50", ["20", "30", "250"], "300 - 250 = 50."),
                 ("How many more from 280 to make 300?", "20", ["80", "30", "200"], "300 - 280 = 20."),
                 ("Which is more: 280 or 250?", "280", ["250", "Both equal", "200"], "280 is greater than 250."),
                 ("Which number is just before 300?", "299", ["301", "290", "200"], "299 comes before 300."),
                 ("Which number is just after 298?", "299", ["297", "300", "288"], "298 + 1 = 299."),
             ]),
        ],
    },
    {
        "chapter_name": "Raksha Bandhan",
        "pdf": "cemm107.pdf",
        "modules": [
            ("Equal Groups in Rakhis", "Medium", "Making rakhis introduces multiplication. If one rakhi needs 1 flower, 2 threads, and some beads, then 5 rakhis need 5 times each material. Equal groups help us count quickly using multiplication.",
             [
                 ("For 5 rakhis, 1 flower each means ____ flowers.", "5", ["1", "10", "25"], "The PDF shows 5 times 1 = 5."),
                 ("Each rakhi uses 2 threads. For 5 rakhis, threads needed are ____.", "10", ["5", "7", "25"], "5 × 2 = 10."),
                 ("5 times 1 is written as ____.", "5 × 1", ["5 - 1", "5 + 0", "1 ÷ 5"], "The PDF writes 5 times 1 as 5 × 1."),
                 ("Equal groups help with ____.", "Multiplication", ["Calendar", "Capacity", "Folding only"], "Rakhi materials are counted as repeated equal groups."),
                 ("A festival in this chapter is ____.", "Raksha Bandhan", ["Deepawali only", "Holi only", "Makar Sankranti only"], "The chapter title is Raksha Bandhan."),
             ]),
            ("Arrays and Repeated Addition", "Medium", "Repeated addition is a bridge to multiplication. Adding 2 + 2 + 2 + 2 + 2 is the same as 5 times 2. Children see how repeated groups of flowers, threads, and beads can be written as multiplication facts.",
             [
                 ("2 + 2 + 2 + 2 + 2 = ____.", "10", ["5", "12", "20"], "Five groups of 2 make 10."),
                 ("5 × 2 = ____.", "10", ["7", "25", "3"], "Five times two equals ten."),
                 ("Repeated addition means adding the same number ____.", "Again and again", ["Only once", "Never", "As a calendar"], "Repeated equal groups are added repeatedly."),
                 ("Which is the same as 4 + 4 + 4?", "3 × 4", ["4 - 3", "3 + 4", "4 ÷ 3"], "Three groups of four is 3 × 4."),
                 ("Multiplication is useful when groups are ____.", "Equal", ["Unequal", "Hidden only", "Curved"], "Equal groups can be multiplied."),
             ]),
        ],
    },
    {
        "chapter_name": "Fair Share",
        "pdf": "cemm108.pdf",
        "modules": [
            ("Equal Sharing and Halves", "Medium", "Fair sharing means everyone gets an equal part. Shabnam and Mukta fold a paratha to check whether two pieces are equal. When one whole is shared equally between two people, each share is called a half.",
             [
                 ("When one whole is shared equally between two people, each share is a ____.", "Half", ["Third", "Hundred", "Week"], "The PDF states each equal share is called a half."),
                 ("Two halves make ____ whole.", "1", ["2", "3", "0"], "Two equal halves join to make one whole."),
                 ("The children share a paratha and ____.", "Chocolate", ["Calendar", "Juice", "Saplings"], "The PDF asks about sharing chocolate and paratha equally."),
                 ("Fair sharing means parts are ____.", "Equal", ["Unequal", "Hidden", "Longer only"], "The story says unequal parts are not fair."),
                 ("Folding a paratha helps check if pieces are ____.", "Equal", ["Hundreds", "Dates", "Litres"], "The PDF asks why Shabnam folds the paratha over itself."),
             ]),
            ("Whole, Half and Equal Parts", "Medium", "A whole is the complete object. A half is one of two equal parts of a whole. Children circle shapes where half is coloured and draw lines to show one-half. Fractions begin with seeing equal parts.",
             [
                 ("A complete paratha is called a ____.", "Whole", ["Half only", "Calendar", "Line"], "The PDF labels a whole paratha."),
                 ("A half must be one of two ____ parts.", "Equal", ["Unequal", "Hidden", "Heavy"], "Half means equal sharing into two parts."),
                 ("If only one of two equal parts is coloured, the coloured part is ____.", "Half", ["Whole", "Hundred", "Month"], "One of two equal parts is a half."),
                 ("A line can divide a shape into ____ halves.", "Two", ["Three unequal", "Ten always", "Zero"], "One-half is made by splitting into two equal parts."),
                 ("Fractions should be based on equal ____.", "Parts", ["Names", "Festivals", "Crows"], "Equal parts are essential for fractions."),
             ]),
        ],
    },
    {
        "chapter_name": "House of Hundreds - II",
        "pdf": "cemm109.pdf",
        "modules": [
            ("Numbers from 500 to 1000", "Medium", "Akbar and Birbal's crow story introduces larger three-digit numbers like 963. Children draw tiles for numbers such as 832, 947, 726, 504, 620, and 700, and learn to read hundreds, tens, and ones.",
             [
                 ("Birbal said there were exactly ____ crows.", "963", ["936", "693", "396"], "The story states nine hundred and sixty three crows."),
                 ("832 has ____ hundreds.", "8", ["3", "2", "32"], "832 = 8 hundreds, 3 tens, 2 ones."),
                 ("947 has ____ tens.", "4", ["9", "7", "47"], "947 = 9 hundreds, 4 tens, 7 ones."),
                 ("700 has ____ ones.", "0", ["7", "70", "100"], "700 has no loose ones."),
                 ("504 has 5 hundreds, 0 tens and ____ ones.", "4", ["5", "0", "9"], "504 = 500 + 4."),
             ]),
            ("Number Lines Beyond 500", "Medium", "The chapter asks children to locate numbers like 530, 540, 628, 696, 703, 721, 759, 810, 855, and 887 on number lines. A number line helps us see which numbers are smaller, bigger, nearer, or farther.",
             [
                 ("Which number is between 500 and 600?", "530", ["703", "810", "887"], "530 lies between 500 and 600."),
                 ("Which number is greater: 696 or 628?", "696", ["628", "Both equal", "600"], "696 is greater than 628."),
                 ("Which number comes after 703?", "721", ["696", "590", "530"], "Among the listed numbers, 721 is after 703."),
                 ("887 is closer to ____ than to 800.", "900", ["500", "600", "700"], "887 is near 900."),
                 ("A number line helps us locate ____.", "Numbers", ["Only juice", "Only halves", "Only beads"], "The PDF asks children to locate numbers on a number line."),
             ]),
        ],
    },
    {
        "chapter_name": "Fun at Class Party!",
        "pdf": "cemm110.pdf",
        "modules": [
            ("Informal Length Measurement", "Medium", "Children measure a classroom using hand spans, footsteps, and paper strings. These are informal tools. Because children's hand spans may differ, the same table may give different measurements. Measurement becomes clearer when the unit is chosen carefully.",
             [
                 ("Children use hand spans to measure ____.", "Length", ["Time", "Money", "Capacity"], "The chapter picture includes measurement using hand spans."),
                 ("Two children using different hand spans may get ____ measurements.", "Different", ["Always same", "No", "Calendar"], "The PDF asks whether Leena and Adi get the same measurement."),
                 ("Paper strings can measure the height of a ____.", "Window", ["Crow", "Rakhi", "Glass"], "The page asks to tick strings as long as the window height."),
                 ("Footsteps can measure ____ between walls.", "Distance", ["Juice", "Months", "Halves"], "The PDF asks for distance between two walls."),
                 ("A better unit should be ____.", "Consistent", ["Changing always", "Hidden", "Unequal"], "Consistent units make measurement fair."),
             ]),
            ("Comparing Longest and Shortest", "Easy", "Paper strings help children compare length visually. They colour the shortest string red and the longest string green, then discuss how they identified them. Comparing length is the first step before measuring exactly.",
             [
                 ("The shortest paper string is coloured ____.", "Red", ["Green", "Blue", "Yellow"], "The PDF says colour the shortest paper string with red."),
                 ("The longest paper string is coloured ____.", "Green", ["Red", "Black", "White"], "The PDF says colour the longest paper string with green."),
                 ("Longest means having the ____ length.", "Greatest", ["Smallest", "Equal always", "No"], "Longest is greatest in length."),
                 ("Shortest means having the ____ length.", "Smallest", ["Greatest", "Equal always", "Heavy"], "Shortest is smallest in length."),
                 ("Comparing strings helps us learn ____.", "Length", ["Only crows", "Only money", "Only calendars"], "The activity is about length measurement."),
             ]),
        ],
    },
    {
        "chapter_name": "Filling and Lifting",
        "pdf": "cemm111.pdf",
        "modules": [
            ("Capacity with Glasses", "Medium", "Capacity tells how much a container can hold. Chintu refuses the juice challenge because six big glasses are much more than six small glasses. Same number of glasses can hold different amounts if the glass sizes are different.",
             [
                 ("Capacity tells how much a container can ____.", "Hold", ["Fold", "Count days", "Make marks"], "Capacity is how much a container holds."),
                 ("Chintu can drink 6 ____ glasses.", "Smaller", ["Bigger", "Huge", "Calendar"], "The story says he can drink six smaller glasses."),
                 ("Six bigger glasses hold ____ juice than six smaller glasses.", "More", ["Less", "Equal always", "No"], "Bigger glasses have more capacity."),
                 ("A fair capacity comparison uses same-sized ____.", "Containers", ["Calendars", "Rakhis", "Crows"], "The sister pours milk into same-sized glasses to compare."),
                 ("The chapter asks: whose glass holds ____?", "More", ["Older", "Longer only", "Symmetric"], "The sampled page says 'Whose glass holds more?'"),
             ]),
            ("Weight and Lifting", "Medium", "Lifting helps children feel weight. Some objects are easy to lift because they are light, while some need more effort because they are heavy. This chapter connects filling with capacity and lifting with weight.",
             [
                 ("An object that is difficult to lift may be ____.", "Heavy", ["Empty always", "A month", "A half"], "Heavy objects need more effort to lift."),
                 ("An object easy to lift may be ____.", "Light", ["Heaviest", "Calendar", "Hundred"], "Light objects are easier to lift."),
                 ("A full bucket is usually heavier than an ____ bucket.", "Empty", ["Equal always", "Invisible", "Folded"], "Filling increases weight."),
                 ("Filling is connected to ____.", "Capacity", ["Symmetry only", "Calendar only", "Number line only"], "Filling tells how much a container holds."),
                 ("Lifting is connected to ____.", "Weight", ["Days", "Months", "Halves only"], "Lifting helps compare heaviness."),
             ]),
        ],
    },
    {
        "chapter_name": "Give and Take",
        "pdf": "cemm112.pdf",
        "modules": [
            ("Three-Digit Addition", "Hard", "Kishan's nursery story uses three-digit addition. When 364 saplings and 52 saplings are combined, ones, tens, and hundreds are added carefully. Sometimes 10 tens combine to form 1 hundred. Place value keeps the work organised.",
             [
                 ("364 + 52 = ____.", "416", ["406", "426", "312"], "The PDF explains 364 saplings plus 52 saplings equals 416."),
                 ("In 364, the digit 3 means 3 ____.", "Hundreds", ["Tens", "Ones", "Thousands"], "364 has 3 hundreds."),
                 ("In 52, the digit 5 means 5 ____.", "Tens", ["Hundreds", "Ones", "Thousands"], "52 has 5 tens."),
                 ("10 tens combine to form 1 ____.", "Hundred", ["One", "Ten", "Month"], "The PDF says combine 10 tens to form 1 hundred."),
                 ("Addition puts amounts ____.", "Together", ["Apart", "In halves only", "On a calendar"], "Kishan adds saplings together."),
             ]),
            ("Add and Subtract Number Paths", "Hard", "The chapter opens with number paths such as add 2, add 5, subtract 5, add 6, add 9, subtract 6, and subtract 9. These small jumps build mental maths for larger numbers.",
             [
                 ("334 + 2 = ____.", "336", ["332", "346", "334"], "The PDF shows add 2 from 334 to 336."),
                 ("288 - 6 = ____.", "282", ["294", "288", "292"], "Subtracting 6 from 288 gives 282."),
                 ("357 + 9 = ____.", "366", ["348", "357", "376"], "357 + 9 = 366."),
                 ("331 - 9 = ____.", "322", ["340", "331", "312"], "331 - 9 = 322."),
                 ("A number path uses jumps to practise ____ maths.", "Mental", ["Only calendar", "Only capacity", "Only symmetry"], "Add/subtract paths strengthen mental calculation."),
             ]),
        ],
    },
    {
        "chapter_name": "Time Goes On",
        "pdf": "cemm113.pdf",
        "modules": [
            ("Calendar Months and Days", "Medium", "A calendar shows months, weeks, days, and dates. In this chapter, July is missing, so children make the July 2024 calendar and count Sundays, Thursdays, and dates after a given day.",
             [
                 ("The missing month in the poem is ____.", "July", ["January", "March", "December"], "The poem says the month of July was missing."),
                 ("A week has ____ days.", "7", ["5", "12", "30"], "Calendars arrange days in weeks of seven."),
                 ("Three days after July 22 is July ____.", "25", ["23", "24", "26"], "22 + 3 = 25."),
                 ("The PDF asks children to make the calendar for July ____.", "2024", ["2023", "2025", "2026"], "The page says make the calendar for July 2024."),
                 ("Calendar dates help us know ____ events happen.", "When", ["How heavy", "How much capacity", "Which shape"], "Calendars organize time."),
             ]),
            ("Years, Weeks and Festivals", "Medium", "Children compare calendars from different years and notice what stays the same or changes. Month names stay the same, but dates and weekdays can change. The chapter also connects time with festivals like Deepawali and Makar Sankranti.",
             [
                 ("A year has ____ months.", "12", ["7", "30", "52"], "The PDF asks children to write the names of the 12 months."),
                 ("The month with less than 30 days is ____.", "February", ["July", "August", "December"], "February has fewer than 30 days."),
                 ("A year usually has ____ days.", "365", ["52", "100", "12"], "The chapter asks for number of days in a year."),
                 ("Deepawali and Makar Sankranti are ____.", "Festivals", ["Shapes", "Capacities", "Number lines"], "The page lists festivals."),
                 ("Names of the months generally stay the ____ each year.", "Same", ["Always different", "Hidden", "Unequal"], "The calendar comparison asks what is same/changing."),
             ]),
        ],
    },
    {
        "chapter_name": "The Surajkund Fair",
        "pdf": "cemm114.pdf",
        "modules": [
            ("Symmetry at the Fair", "Medium", "At Surajkund Fair, children spot things that look the same from the left and right side. This is symmetry. A symmetric shape can be folded so both sides match like mirror partners.",
             [
                 ("Things that look same from left and right show ____.", "Symmetry", ["Capacity", "Subtraction", "Calendar"], "The PDF asks children to spot things that look the same from left and right."),
                 ("A line that divides matching halves is a line of ____.", "Symmetry", ["Hundreds", "Juice", "Weight"], "A symmetry line makes two matching sides."),
                 ("A butterfly picture often has left-right ____.", "Symmetry", ["Capacity", "Time", "Addition only"], "Butterflies commonly show mirror-like sides."),
                 ("If two sides match like a mirror, they are ____.", "Symmetric", ["Unequal", "Heavy", "Hidden"], "Mirror matching is symmetry."),
                 ("The chapter setting is the Surajkund ____.", "Fair", ["Nursery", "Calendar", "Classroom only"], "The chapter title is The Surajkund Fair."),
             ]),
            ("Malas, Patterns and Beads", "Medium", "Soni and Avi make malas using 8 beads: 4 of one colour and 4 of another. Different arrangements create different patterns. Recording the bead colours helps children compare and count possible malas.",
             [
                 ("Each mala uses ____ beads.", "8", ["4", "12", "2"], "The PDF says make malas with 8 beads."),
                 ("The mala uses 4 beads of one colour and ____ of another.", "4", ["8", "2", "0"], "The PDF says 4 of one colour and 4 of another."),
                 ("Changing bead order creates a different ____.", "Pattern", ["Month", "Capacity", "Number line"], "Different arrangements make different patterns."),
                 ("Soni and Avi take beads from a ____.", "Basket", ["Calendar", "Glass", "Nursery"], "The stall holders say take beads from the basket."),
                 ("Colouring bead strings records the malas children have ____.", "Made", ["Measured in litres", "Subtracted", "Lost"], "The activity asks children to colour beads to show malas."),
             ]),
        ],
    },
]


def build():
    output = []
    manifest = {
        "source": "NCERT Maths Mela Class 3 PDFs, reprint 2026-27",
        "syllabus": "CBSE",
        "class": "Class 3",
        "subject": "Mathematics",
        "chapters": [],
        "module_total": 0,
        "question_total": 0,
    }
    counter = 1
    for chapter in CHAPTERS:
        chapter_obj = {"chapter_name": chapter["chapter_name"], "modules": []}
        chapter_manifest = {"chapter_name": chapter["chapter_name"], "pdf": chapter["pdf"], "modules": []}
        for topic, difficulty, explanation, facts in chapter["modules"]:
            timer = {"Easy": 30, "Medium": 45, "Hard": 60}[difficulty]
            questions = [q(i + 1, *fact, timer) for i, fact in enumerate(facts)]
            module_id = f"cbse_c3_m{counter:03d}_{slug(topic)}"
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
                "source_basis": "PDF chapter title, sampled activity text, and textbook problem context",
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
    assert len(output) == 14
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
