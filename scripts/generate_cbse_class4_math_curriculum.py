import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "src" / "data"
OUTPUT_JSON = DATA_DIR / "cbse_class4_mathematics_learning_journey.json"
OUTPUT_MANIFEST = DATA_DIR / "cbse_class4_mathematics_validation_manifest.json"


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
    ("Shapes Around Us", "demm101.pdf", [
        ("Models, Prisms and Pyramids", "Medium", "Buildings can be understood by making models with blocks. In this chapter, children model India Gate and Qutub Minar using cubes, cuboids, cylinders, prisms, and pyramids. A good model keeps the important parts, like base, pillars, roof, and storeys, even if it is simpler than the real building.", [
            ("Which building model is made using wooden blocks in Chapter 1?", "India Gate", ["Surajkund Fair", "Mawlynnong", "Transport Museum"], "The opening activity says the child is trying to make India Gate with wooden blocks."),
            ("Qutub Minar has ____ storeys.", "5", ["3", "10", "379"], "The PDF note states Qutub Minar has 5 storeys and 379 stairs."),
            ("Qutub Minar has ____ stairs.", "379", ["5", "1000", "77"], "The chapter fact says it has 379 stairs."),
            ("A model of a building should show important ____.", "Parts", ["Dates", "Prices", "Responses"], "The activity asks which parts of the building are shown in the model."),
            ("A cube is also discussed as a kind of ____.", "Prism", ["Calendar", "Data table", "Fraction"], "The chapter asks, 'Is a cube also a prism?'"),
        ]),
        ("Nets of Solids", "Medium", "A net is a flat pattern that can fold into a solid shape. The chapter asks children to use nets at the end of the book to make models. Nets help us see how flat faces join to make cubes, prisms, pyramids, and other 3D shapes.", [
            ("A flat pattern that folds into a solid is called a ____.", "Net", ["Leap year", "Multiple", "Response"], "The chapter asks children to use nets to make models."),
            ("A cube has ____ square faces.", "6", ["4", "5", "8"], "A cube is made of six square faces."),
            ("A pyramid has a base and faces that meet at a ____.", "Point", ["Calendar", "Litre", "Rupee"], "Pyramid side faces meet at one top point."),
            ("Nets help connect flat shapes to ____ shapes.", "Solid", ["Time only", "Money only", "Data only"], "Nets fold into 3D solids."),
            ("Removing one piece from a model may change its ____.", "Shape", ["Date", "Price", "Weight unit"], "The chapter asks what happens if one piece is removed."),
        ]),
    ]),
    ("Hide and Seek", "demm102.pdf", [
        ("Top, Front and Side Views", "Easy", "The same object can look different from different places. In Hide and Seek, children compare top view, front view, and side view. Mini, Bholu, and Rani draw the same brick differently because each child sees it from a different direction.", [
            ("The chapter asks children to identify top, front and ____ views.", "Side", ["Calendar", "Money", "Weight"], "The teacher note names top view, side view, and front view."),
            ("Mini, Bholu and Rani draw the same ____.", "Brick", ["Calendar", "Mala", "Pumpkin"], "The chapter asks why their drawings of the same brick differ."),
            ("A view from above is called the ____ view.", "Top", ["Front", "Side", "Bottom only"], "Top view means looking from above."),
            ("A picture clicked from the front shows the ____ view.", "Front", ["Top", "Back only", "Leap"], "The chapter mentions a tree picture from the front."),
            ("Different views happen because we look from different ____.", "Directions", ["Prices", "Months", "Subjects"], "Direction changes the visible shape."),
        ]),
        ("Visibility and Position", "Easy", "Hide and seek is a playful way to learn position and visibility. A child may or may not see others depending on where they stand and which way they face. This develops spatial thinking: front, back, near, far, left, right, and behind.", [
            ("The children are playing ____.", "Hide and seek", ["NIM", "Market shopping", "Calendar game"], "The opening page asks which game the children are playing."),
            ("If Rani faces the hut, she may see children near the ____.", "Hut", ["Calendar", "Scale", "Bottle"], "The question asks if Rani can see who is hiding near the hut."),
            ("Seeing depends on where we ____.", "Stand", ["Spend", "Multiply only", "Weigh"], "Position affects visibility."),
            ("Behind is a ____ word.", "Position", ["Capacity", "Data", "Leap"], "Behind describes location."),
            ("A top view can reveal things hidden from a ____ view.", "Front", ["Month", "Rupee", "Kilogram"], "Different views reveal different information."),
        ]),
    ]),
    ("Pattern Around Us", "demm103.pdf", [
        ("Counting Arrangements", "Medium", "Patterns help us count faster. Muniamma arranges cups, plates, laddoos, and pedas in trays. When rows, columns, or stacks repeat the same arrangement, we can count one group and multiply or add groups instead of counting every object one by one.", [
            ("Muniamma makes plates and ____.", "Cups", ["Calendars", "Bricks", "Airplanes"], "The PDF says Muniamma makes plates and cups."),
            ("Gundappa has tall ____ trees.", "Coconut", ["Mango only", "Pine", "Banana only"], "The chapter mentions tall coconut trees."),
            ("If 5 coconuts are plucked from each of 4 trees, total coconuts are ____.", "20", ["9", "45", "10"], "4 × 5 = 20."),
            ("Repeated equal trays can be counted using ____.", "Multiplication", ["Leap years", "Views", "Symmetry only"], "Equal arrangements support multiplication."),
            ("A top view can help count stacked ____.", "Trays", ["Months", "Subjects", "Litres"], "The page labels a top view of arranged trays."),
        ]),
        ("Patterns with Money", "Medium", "Money can also make patterns. Shirley and Shiv arrange play money and coins to show amounts like ₹36, ₹125, and ₹183. When notes and coins are grouped carefully, we can read the total amount quickly.", [
            ("The money activity asks children to arrange play money to show ₹36, ₹125 and ₹____.", "183", ["18", "300", "45"], "The PDF lists ₹36, ₹125, and ₹183."),
            ("A ₹10 note repeated 3 times gives ₹____.", "30", ["13", "300", "3"], "3 tens make 30."),
            ("₹100 + ₹20 + ₹5 = ₹____.", "125", ["152", "25", "105"], "The amount is one hundred twenty-five."),
            ("Coins arranged in triangles make a ____.", "Pattern", ["Calendar", "View", "Capacity"], "The PDF asks for numbers of coins in triangular arrangements."),
            ("Counting money patterns helps find the total ____.", "Amount", ["Height", "Date", "View"], "Money arrangements represent amounts."),
        ]),
    ]),
    ("Thousands Around Us", "demm104.pdf", [
        ("Thousands, Hundreds, Tens and Ones", "Hard", "The langar story introduces numbers around one thousand. Donations and lunch counts are written in different forms: ones, tens, hundreds, expressions, and words. HTO blocks help children see how many hundreds, tens, and ones a number has.", [
            ("The langar expected around ____ people.", "1000", ["100", "55", "508"], "The PDF says around one thousand people are expected."),
            ("Fifty-five people volunteered to ____.", "Serve", ["Measure", "Fold", "Hide"], "The story says 55 people volunteer to serve."),
            ("4 ones + 7 tens equals ____.", "74", ["47", "11", "407"], "7 tens are 70 and 4 ones make 74."),
            ("100 - 7 equals ____.", "93", ["107", "97", "73"], "100 minus 7 is 93."),
            ("HTO blocks stand for hundreds, tens and ____.", "Ones", ["Orders", "Objects", "Options"], "HTO represents place value."),
        ]),
        ("Comparing and Forming 3-Digit Numbers", "Hard", "Children make 3-digit numbers using digits and compare the smallest and largest. They also read lunch counts like 52, 145, 325, and 508. Place value decides which number is bigger: hundreds first, then tens, then ones.", [
            ("Which is largest: 333, 373, 737, 777?", "777", ["333", "373", "737"], "777 has the greatest hundreds, tens, and ones among these."),
            ("Which is smallest: 333, 337, 373, 733?", "333", ["337", "373", "733"], "333 is the smallest of the listed numbers."),
            ("508 has ____ hundreds.", "5", ["0", "8", "50"], "508 has 5 hundreds."),
            ("145 has ____ tens.", "4", ["1", "5", "14"], "145 has 4 tens."),
            ("To compare 3-digit numbers, check ____ first.", "Hundreds", ["Ones", "Days", "Subjects"], "Hundreds place has the greatest value."),
        ]),
    ]),
    ("Sharing and Measuring", "demm105.pdf", [
        ("Halves and Quarters", "Medium", "Fractions are fair parts of a whole. Ikra asks whether half a paper or two quarters should be used. One half and two quarters can cover the same amount if the parts are equal. Fractions make sense only when the whole is divided equally.", [
            ("When an object is divided into two equal parts, each part is a ____.", "Half", ["Quarter", "Third", "Thousand"], "The PDF defines a half as one of two equal parts."),
            ("Half is written as ____.", "1/2", ["1/4", "2/4 only", "4/1"], "The page writes half as 1/2."),
            ("When an object is divided into four equal parts, each part is a ____.", "Quarter", ["Half", "Hundred", "View"], "The PDF defines a quarter."),
            ("Quarter is written as ____.", "1/4", ["1/2", "4/4 only", "2/1"], "The page writes quarter as 1/4."),
            ("Two quarters are equal to ____ half.", "One", ["Zero", "Three", "Four"], "2/4 equals 1/2."),
        ]),
        ("Measuring Fractional Lengths", "Medium", "The chapter connects sharing with measuring. A strip, paper, or object may be split into halves and quarters to compare or measure parts. Equal folding is a simple test: if parts match exactly, the sharing is fair.", [
            ("Fraction parts must be ____.", "Equal", ["Unequal", "Hidden", "Longer always"], "The chapter asks how to know the paper is divided equally."),
            ("Folding paper can check whether two parts ____.", "Match", ["Cost more", "Show data", "Become litres"], "Folding helps compare equal parts."),
            ("Four quarters make ____ whole.", "1", ["2", "4", "0"], "Four equal quarters complete one whole."),
            ("A shape divided into unequal parts does not show correct ____.", "Fractions", ["Calendars", "Weights", "Views"], "Fractional parts should be equal."),
            ("Samina chose two quarters because it sounded ____.", "Bigger", ["Smaller", "Empty", "Symmetric"], "The story says one half seemed smaller but two quarters sounded bigger."),
        ]),
    ]),
    ("Measuring Length", "demm106.pdf", [
        ("Metres and Half Metres", "Medium", "Length tells how long, tall, wide, or deep something is. The chapter revises metre and half metre, then asks learners to walk, jump, and crawl on 1 m, 5 m, and 10 m lines. Using metre ropes builds a body-feel for length.", [
            ("Lengths are measured in ____.", "Metres", ["Kilograms", "Litres", "Rupees"], "The PDF recalls that lengths are measured in metres."),
            ("The classroom activity makes lines of 1 m, 5 m and ____ m.", "10", ["2", "100", "50"], "The PDF says draw lines of 1 m, 5 m, and 10 m."),
            ("Half metre is written as ____ m.", "1/2", ["1/4", "10", "100"], "The page recalls half metre as 1/2 m."),
            ("A metre rope helps measure ____.", "Length", ["Weight", "Temperature only", "Data"], "The activity uses metre rope for length."),
            ("Walking on a 5 m line helps estimate how long ____ m is.", "5", ["1/4", "1000", "365"], "The note says this develops estimates of 5 m and 10 m."),
        ]),
        ("Length, Height, Breadth and Depth", "Medium", "Measurement words tell us what is being measured. Height is how tall, length is how long, breadth is how wide, and depth is how deep. The chapter asks children to tick what is being measured and identify tools for height.", [
            ("Height tells how ____ something is.", "Tall", ["Heavy", "Much it holds", "Popular"], "The teacher note mentions tall and height."),
            ("Breadth tells how ____ something is.", "Wide", ["Old", "Costly", "Symmetric"], "Breadth is width."),
            ("Depth tells how ____ something is.", "Deep", ["Light", "Many", "Liked"], "Depth measures deepness."),
            ("Temperature is not a measure of ____.", "Length", ["Heat", "Warmth", "Coldness"], "Temperature is listed separately from length measures."),
            ("The door height being less or more than a metre is a ____ check.", "Measurement", ["Data", "Pattern", "Money"], "The chapter asks learners to check classroom measurements."),
        ]),
    ]),
    ("The Cleanest Village", "demm107.pdf", [
        ("Trip Data and Distances", "Medium", "The school trip poster gives mathematical information: date, departure, arrival, cost, distance, families, people, and location. Reading posters carefully helps solve real-life maths problems about distance, time, money, and population.", [
            ("The school trip is to ____.", "Mawlynnong", ["Qutub Minar", "Surajkund", "Transport Museum"], "The poster is for Mawlynnong, Asia's Cleanest Village."),
            ("Mawlynnong is ____ km from Shillong.", "79", ["77", "414", "500"], "The poster says NH206, 79 km from Shillong."),
            ("The trip cost is ₹____ per child.", "500", ["79", "414", "77"], "The poster says register now, ₹500 per child."),
            ("The village has 77 families and ____ people.", "414", ["500", "79", "206"], "The poster lists 77 families, 414 people."),
            ("Departure from school is at ____.", "7 am", ["4 pm", "11 pm", "12 noon"], "The poster says departure from school 7 am."),
        ]),
        ("Price Lists and Total Cost", "Medium", "Sapan Dada's price list helps children calculate costs of fruits, vegetables, biscuits, bottles, and dry fruits. A price list is a table for shopping maths: choose items, multiply by quantity, add costs, and compare totals.", [
            ("Custard apple costs ₹____.", "45", ["95", "23", "32"], "The sampled price list says custard apple: ₹45."),
            ("Beans cost ₹____.", "95", ["45", "23", "37"], "The price list says beans: ₹95."),
            ("Radish costs ₹____.", "23", ["32", "37", "95"], "The price list says radish: ₹23."),
            ("Onion costs ₹____.", "32", ["23", "45", "95"], "The price list says onion: ₹32."),
            ("Potato costs ₹____.", "37", ["32", "23", "45"], "The price list says potato: ₹37."),
        ]),
    ]),
    ("Weigh it, Pour it", "demm108.pdf", [
        ("Kilograms and Grams", "Medium", "Weight tells how heavy something is. The chapter uses fruits, vegetables, school bags, and packets to compare less than 1 kg or more than 1 kg. It also shows that 2 packets of 500 grams make 1000 grams, which is 1 kilogram.", [
            ("We often write kilogram as ____.", "kg", ["g only", "m", "L"], "The PDF says we often write kg for kilogram."),
            ("We often write gram as ____.", "g", ["kg only", "m", "L"], "The PDF says g for gram."),
            ("2 packets of 500 grams make ____ grams.", "1000", ["500", "1500", "100"], "The page states 2 packets of 500 grams = 1000 g."),
            ("1000 g equals ____ kg.", "1", ["10", "100", "2"], "The PDF states 1000 g = 1 kg."),
            ("A weighing balance verifies ____.", "Weight", ["Calendar", "View", "Favourite subject"], "The activity asks children to verify guesses using a weighing balance."),
        ]),
        ("Capacity and Litres", "Medium", "Capacity tells how much a container can hold. The chapter connects Grade 3 learning about a 1 litre bottle with more measurement practice. Pouring, filling, and comparing containers helps children understand litres and millilitres in daily life.", [
            ("Capacity tells how much a container can ____.", "Hold", ["Weigh only", "Cost", "Reflect"], "Capacity is about how much a container holds."),
            ("The chapter recalls a 1 ____ bottle.", "Litre", ["Kilogram", "Metre", "Rupee"], "The opening text mentions a 1 litre bottle."),
            ("Pouring is connected with measuring ____.", "Capacity", ["Symmetry", "Views", "Multiples"], "The title says Weigh it, Pour it."),
            ("A bigger bottle usually holds ____ water.", "More", ["Less always", "No", "Equal always"], "Larger capacity means more can be held."),
            ("A 1 litre bottle is a tool for understanding ____.", "Capacity", ["Data responses", "Top view", "Fractions only"], "Litres measure capacity."),
        ]),
    ]),
    ("Equal Groups", "demm109.pdf", [
        ("Multiples with Animal Jumps", "Medium", "Animal jumps make multiples visible. A frog jumping 3 steps touches multiples of 3, a squirrel jumping 4 steps touches multiples of 4, a rabbit jumping 6 steps touches multiples of 6, and a kangaroo jumping 8 steps touches multiples of 8.", [
            ("The frog jumps ____ steps at a time.", "3", ["4", "6", "8"], "The PDF states the frog jumps 3 steps at a time."),
            ("The squirrel jumps ____ steps at a time.", "4", ["3", "6", "8"], "The PDF states the squirrel jumps 4 steps at a time."),
            ("The rabbit jumps ____ steps at a time.", "6", ["3", "4", "8"], "The PDF states the rabbit jumps 6 steps at a time."),
            ("The kangaroo jumps ____ steps at a time.", "8", ["3", "4", "6"], "The PDF states the kangaroo jumps 8 steps at a time."),
            ("Numbers touched by jumps of 3 are multiples of ____.", "3", ["4", "6", "8"], "The PDF says these numbers are multiples of 3."),
        ]),
        ("Common Multiples", "Hard", "When two animals land on the same number, that number is a common multiple. For example, both frog jumps of 3 and squirrel jumps of 4 touch 12, 24, 36, and so on. Common multiples help compare repeated groups.", [
            ("A common multiple of 3 and 4 is ____.", "12", ["7", "10", "14"], "12 is divisible by both 3 and 4."),
            ("To reach 48, the rabbit jumping 6 steps jumps ____ times.", "8", ["6", "4", "12"], "48 ÷ 6 = 8."),
            ("To reach 48, the kangaroo jumping 8 steps jumps ____ times.", "6", ["8", "4", "12"], "48 ÷ 8 = 6."),
            ("To reach 60, the frog jumping 3 steps jumps ____ times.", "20", ["10", "15", "18"], "60 ÷ 3 = 20."),
            ("A number touched by both jump patterns is a ____ multiple.", "Common", ["Hidden", "Leap", "Symmetric"], "Shared landing numbers are common multiples."),
        ]),
    ]),
    ("Elephants, Tigers, and Leopards", "demm110.pdf", [
        ("NIM Game Strategy", "Medium", "In the NIM game, players add either 1 or 2 to reach a target number such as 10. The game is not just luck; children look for winning totals. Thinking backward from the target helps decide whether choosing 1 or 2 is better.",
             [
                 ("In the NIM game, players add either 1 or ____.", "2", ["3", "5", "10"], "The PDF says choose either 1 or 2 each time."),
                 ("The first target number in the game is ____.", "10", ["12", "24", "100"], "The rules say reach target number 10."),
                 ("The player who reaches 10 first is the ____.", "Winner", ["Teacher", "Data", "View"], "The rule says the player who reaches 10 first wins."),
                 ("If the previous total is 8, adding 2 reaches ____.", "10", ["9", "11", "12"], "8 + 2 = 10."),
                 ("Thinking backward from the target helps find a ____ strategy.", "Winning", ["Weight", "Calendar", "Capacity"], "The task asks if you can win from totals 6, 7, or 8."),
             ]),
        ("Addition Chart Patterns", "Medium", "The addition chart shows sums in rows and columns. Children look for patterns, where 9 appears, which rows or columns are even or odd, and how small windows in the table behave. Tables reveal hidden regularity in addition.", [
            ("The chapter includes an ____ chart.", "Addition", ["Calendar", "Weight", "Subject"], "The sampled page is titled Addition Chart."),
            ("In an addition chart, 4 + 5 = ____.", "9", ["1", "20", "45"], "4 plus 5 equals 9."),
            ("Rows and columns in the chart contain ____.", "Sums", ["Weights only", "Views only", "Months only"], "Each cell is an addition result."),
            ("Even plus even gives an ____ number.", "Even", ["Odd", "Fraction", "Leap"], "The sum of two even numbers is even."),
            ("Odd plus odd gives an ____ number.", "Even", ["Odd", "View", "Kilogram"], "The sum of two odd numbers is even."),
        ]),
    ]),
    ("Fun with Symmetry", "demm111.pdf", [
        ("Lines of Symmetry", "Medium", "A line of symmetry divides a design into two matching halves. Ink designs, masks, rangolis, and folded paper show symmetry beautifully. If one side matches the other like a mirror, the design is symmetrical.", [
            ("A line that divides a design into matching halves is a line of ____.", "Symmetry", ["Capacity", "Data", "Weight"], "The PDF asks where to draw the line of symmetry."),
            ("The ink design begins by folding paper in ____.", "Half", ["Quarters only", "Ten parts", "Unequal parts"], "Step 1 says take a sheet and fold it in half."),
            ("Symmetry can be checked using a ____.", "Mirror", ["Price list", "Scale only", "Calendar only"], "The paper airplane task asks where to place a mirror."),
            ("A symmetrical design has two ____ halves.", "Equal", ["Unequal", "Hidden", "Heavy"], "Symmetry means matching halves."),
            ("Rangolis and masks were explored for ____ in earlier grades.", "Symmetry", ["Capacity", "Weight", "Money"], "The PDF mentions symmetry in rangolis and masks."),
        ]),
        ("Symmetry in Paper Airplanes", "Medium", "Paper airplanes use symmetry. If the two sides are balanced, the airplane is more likely to fly well. The chapter asks children to mark symmetry lines, try an asymmetrical plane, and compare which flies longer.",
             [
                 ("The chapter asks children to make a paper ____.", "Airplane", ["Bottle", "Calendar", "Price list"], "The PDF has a paper airplane activity."),
                 ("A balanced paper airplane usually has ____.", "Symmetry", ["Unequal sides", "No folds", "Only data"], "A symmetric plane has matching sides."),
                 ("An asymmetrical plane has sides that do not ____.", "Match", ["Fly", "Fold", "Cost"], "Asymmetry means sides are not matching."),
                 ("The activity asks which plane flies for a ____ time.", "Longer", ["Heavier", "Costlier", "Earlier"], "The PDF asks children to compare flight time."),
                 ("Folding helps create a central ____.", "Line of symmetry", ["Price list", "Kilogram", "Response"], "Paper folding can form symmetry lines."),
             ]),
    ]),
    ("Ticking Clocks and Turning Calendar", "demm112.pdf", [
        ("Leap Years and February", "Medium", "A leap year has one extra day and includes 29 February. Parv was born on 29 February 2016. The chapter compares February 2024 and February 2025 to show that leap years occur every four years.",
             [
                 ("Years having 29 February are called ____ years.", "Leap", ["Data", "Symmetry", "Market"], "The PDF defines years with 29 February as leap years."),
                 ("February 2024 has ____ days.", "29", ["28", "30", "31"], "The calendar shown for Feb 2024 includes 29."),
                 ("February 2025 has ____ days.", "28", ["29", "30", "31"], "The calendar shown for Feb 2025 ends at 28."),
                 ("A leap year has ____ days.", "366", ["365", "364", "360"], "A leap year has one additional day."),
                 ("Leap years occur every ____ years.", "4", ["2", "5", "10"], "The PDF says they occur every four years."),
             ]),
        ("Calendar Days and Dates", "Medium", "Calendars help answer today, yesterday, tomorrow, festival months, and day-of-week questions. Children use calendars to move forward or backward in time and connect dates with real events.", [
            ("The day before today is called ____.", "Yesterday", ["Tomorrow", "Leap year", "Quarter"], "The chapter asks for today and yesterday."),
            ("The day after today is called ____.", "Tomorrow", ["Yesterday", "Last year", "Data"], "Tomorrow is the next day."),
            ("A calendar helps us find days of the ____.", "Week", ["Kilogram", "Shape only", "Price"], "Calendar questions use days of the week."),
            ("Festival names are matched with names of ____.", "Months", ["Weights", "Views", "Multiples"], "The activity asks for festival and month names."),
            ("If today is Wednesday, yesterday was ____.", "Tuesday", ["Thursday", "Friday", "Monday only"], "Tuesday comes before Wednesday."),
        ]),
    ]),
    ("The Transport Museum", "demm113.pdf", [
        ("Times-10 and Hundreds", "Medium", "Multiplying by 10 makes tens. The chapter shows 2 × 10, 5 × 10, 8 × 10, and 10 × 10 using pictorial representations. Ten tens make one hundred, so times-10 is a bridge to larger numbers.",
             [
                 ("2 × 10 = ____.", "20", ["12", "2", "200"], "2 tens equal 20."),
                 ("5 × 10 = ____.", "50", ["15", "5", "500"], "5 tens equal 50."),
                 ("8 × 10 = ____.", "80", ["18", "8", "800"], "8 tens equal 80."),
                 ("10 × 10 = ____.", "100", ["10", "20", "1000"], "10 tens make 100."),
                 ("10 tens equal 1 ____.", "Hundred", ["One", "Thousand", "Quarter"], "The PDF states 10 tens = 1 hundred = 100."),
             ]),
        ("Constructing Tables and Products", "Hard", "Arrays help build multiplication tables. A 5 × 15 arrangement can be split into 5 × 10 and 5 × 5. This makes hard products easier because we break them into friendly parts and add the results.",
             [
                 ("A 5 × 15 arrangement can be split into 5 × 10 and 5 × ____.", "5", ["10", "15", "20"], "The PDF shows 5 × 15 = 5 × 10 and 5 × 5."),
                 ("5 × 10 = ____.", "50", ["15", "5", "100"], "Five groups of ten make fifty."),
                 ("5 × 5 = ____.", "25", ["10", "15", "55"], "Five groups of five make twenty-five."),
                 ("5 × 15 = ____.", "75", ["50", "25", "100"], "50 + 25 = 75."),
                 ("Splitting an array helps find a ____.", "Product", ["Calendar date", "Weight", "View"], "Multiplication answers are products."),
             ]),
    ]),
    ("Data Handling", "demm114.pdf", [
        ("Asking a Good Data Question", "Medium", "Data handling begins with a clear question. Rohan and Anjali want to find the most liked subject, so the question must collect subject choices clearly. A good data question gives useful options and helps everyone answer in the same way.",
             [
                 ("Rohan and Anjali want to find the most liked ____.", "Subject", ["Building", "Bottle", "Leap year"], "The PDF asks for the most liked subject."),
                 ("The subjects include Mathematics, Languages, Arts and ____.", "The World Around Us", ["Only Transport", "Only Weight", "Only Fractions"], "The PDF lists these subject options."),
                 ("A good data question should be ____.", "Clear", ["Confusing", "Hidden", "Unequal"], "Clear questions collect better responses."),
                 ("Data handling starts by asking a ____.", "Question", ["Weight", "Shape only", "Leap"], "The chapter opens with choosing the most appropriate question."),
                 ("Physical Education is recorded as ____.", "P.E.", ["M", "L", "T"], "The PDF says P.E. for Physical Education."),
             ]),
        ("Recording and Reading Responses", "Medium", "Anjali and Rohan record 45 children's responses using short forms: M, L, T, A, and P.E. After recording, they count each response and compare which subject is most or least liked. Data becomes meaningful only after organising it.",
             [
                 ("They recorded responses from ____ children.", "45", ["14", "100", "5"], "The PDF says there are a total of 45 children in the grade."),
                 ("M stands for ____.", "Mathematics", ["Months", "Market", "Metre"], "The PDF says M for Mathematics."),
                 ("L stands for ____.", "Languages", ["Length", "Leap", "Litre"], "The PDF says L for Languages."),
                 ("A stands for ____.", "Arts", ["Animals", "Amount", "Area only"], "The PDF says A for Arts."),
                 ("Counting responses helps find the ____ liked subject.", "Most", ["Heaviest", "Tallest", "Deepest"], "The purpose is to find the most liked subject."),
             ]),
    ]),
]


def build():
    output = []
    manifest = {
        "source": "NCERT Maths Mela Grade 4 PDFs, reprint 2026-27",
        "syllabus": "CBSE",
        "class": "Class 4",
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
            module_id = f"cbse_c4_m{counter:03d}_{slug(topic)}"
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
