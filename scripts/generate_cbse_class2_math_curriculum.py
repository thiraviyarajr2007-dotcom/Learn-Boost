import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "src" / "data"
OUTPUT_JSON = DATA_DIR / "cbse_class2_mathematics_learning_journey.json"
OUTPUT_MANIFEST = DATA_DIR / "cbse_class2_mathematics_validation_manifest.json"


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
        "chapter_name": "A Day at the Beach (Counting in Groups)",
        "page": 1,
        "modules": [
            ("Counting in Bunches and Groups", "Easy", "Counting in groups is like picking up many things with one smart look. At the beach, children count coconuts, boats, children, oranges, balloons, bananas, and seashells. Sometimes we count one by one, and sometimes we count in bunches or groups. Groups of ten are especially helpful because they make big numbers friendly.",
             [
                 ("What does Chapter 1 ask children to count at the beach?", "Coconuts and boats", ["Only clocks", "Only coins", "Only shadows"], "The opening picture asks for coconuts, boats, children, and oranges."),
                 ("Counting in groups means counting things in ____.", "Bunches", ["Seasons", "Lines only", "Coins only"], "The chapter asks whether children counted one by one or in bunches/groups."),
                 ("A necklace in the shop has 10 ____.", "Shells", ["Days", "Months", "Lines"], "The PDF says necklaces of shells with 10 shells in each necklace."),
                 ("Balloons in the shop are counted as groups and ____ balloons.", "Loose", ["Hidden", "Morning", "Heavy"], "The activity asks for groups of balloons and loose balloons."),
                 ("Counting groups helps us count ____ numbers.", "Bigger", ["Only smaller", "No", "Sleeping"], "Groups make larger counts easier."),
             ]),
            ("Tens and Ones", "Medium", "A ten strip or a bundle of sticks is a shortcut for ten ones. In this chapter, children arrange chikoos in trays of ten and write numbers as tens and ones, such as 24 as 2 tens and 4 ones. Tens and ones help us understand numbers up to 100.",
             [
                 ("One ten strip has how many units?", "10", ["1", "5", "100"], "The PDF asks children to write that 1 ten strip has 10 units."),
                 ("24 means ____ tens and 4 ones.", "2", ["4", "6", "10"], "The table shows 24 as 2 tens and 4 units."),
                 ("43 chikoos can be shown as 4 trays of ten and ____ loose chikoos.", "3", ["4", "10", "30"], "43 is 4 tens and 3 ones."),
                 ("10 ten strips make ____ units.", "100", ["10", "50", "20"], "The page says 10 strips joined together make 100 units."),
                 ("Tens and ones help us understand numbers up to ____.", "100", ["9", "5", "3"], "This chapter builds number sense to 100."),
             ]),
        ],
    },
    {
        "chapter_name": "Shapes Around Us (3D Shapes)",
        "page": 16,
        "modules": [
            ("Solid Shapes Around Us", "Easy", "3D shapes are solid shapes we can hold, like boxes, balls, bottles, and dice. They have faces and can look different from different sides. This chapter asks children to notice shapes in daily life and match objects that look alike.",
             [
                 ("Chapter 2 is about which kind of shapes?", "3D shapes", ["Only money", "Only time", "Only data"], "The contents page names Shapes Around Us as 3D Shapes."),
                 ("Which object is like a ball?", "Sphere", ["Cube", "Cone", "Line"], "A ball is a sphere-like solid."),
                 ("Which object is like a dice?", "Cube", ["Sphere", "Circle", "Slanting line"], "A dice is cube-shaped."),
                 ("A solid shape can be ____.", "Held", ["Only heard", "Only a day", "Only a season"], "3D shapes are objects children can hold."),
                 ("Boxes, balls and bottles are examples of ____.", "Objects with shapes", ["Only numbers", "Only months", "Only rupees"], "The chapter connects objects to 3D shapes."),
             ]),
            ("Roll, Slide and Stack", "Easy", "Some solid shapes roll, some slide, and some can be stacked. Round objects roll easily, flat-faced objects slide, and box-like objects stack well. The chapter helps children learn shape properties by playing with real objects.",
             [
                 ("A ball can usually ____.", "Roll", ["Only stack", "Only count", "Only spend"], "Round objects like balls roll."),
                 ("A box can usually ____ well.", "Stack", ["Melt", "Tell time", "Become a coin"], "Flat-faced box-like objects can stack."),
                 ("Objects with flat faces can ____.", "Slide", ["Sleep", "Read", "Vanish"], "Flat faces help objects slide."),
                 ("Trying objects by hand helps us learn their ____.", "Shape properties", ["Festivals", "Prices", "Ages"], "The chapter uses hands-on shape exploration."),
                 ("Which object is more likely to roll?", "Bottle", ["Notebook", "Mat", "Paper sheet"], "A bottle has a curved surface and can roll."),
             ]),
        ],
    },
    {
        "chapter_name": "Fun with Numbers (Numbers 1 to 100)",
        "page": 23,
        "modules": [
            ("Number Line and Guess My Number", "Medium", "A number line is like a path where numbers stand in order. In Guess My Number, children ask yes/no questions like 'Is it more than 50?' or 'Is it less than 20?' These games help children compare numbers and locate them between 1 and 100.",
             [
                 ("In Guess My Number, children ask questions answered by ____.", "Yes or no", ["Long stories", "Only money", "Only shapes"], "The PDF says questions can be answered in yes/no."),
                 ("Which question matches the game?", "Is it more than 50?", ["Is it a season?", "Is it a rupee?", "Is it a fruit only?"], "The PDF gives 'Is it more than 50?' as an example."),
                 ("65 is drawn on a ____.", "Number line", ["Clock", "Coin", "Garland"], "The activity asks children to draw an ant on 65 on the number line."),
                 ("79 is marked with a ____ cube.", "Sugar", ["Wood", "Gold", "Water"], "The PDF asks children to draw a sugar cube on number 79."),
                 ("30 is less than ____.", "40", ["20", "10", "5"], "The game uses more than/less than comparisons."),
             ]),
            ("Number Chart Patterns", "Medium", "Numbers from 1 to 100 form helpful patterns. When we move forward, numbers grow. When we move backward, numbers become smaller. The book also mentions games like Let us Make 100, passing paths, flash cards, and patterns in number charts.",
             [
                 ("The chapter practises numbers from 1 to ____.", "100", ["9", "20", "1000"], "The contents page says Numbers 1 to 100."),
                 ("What comes after 68?", "69", ["67", "78", "86"], "Counting forward from 68 gives 69."),
                 ("What comes before 80?", "79", ["81", "70", "89"], "79 comes just before 80."),
                 ("Numbers grow when we count ____.", "Forward", ["Backward", "Sideways", "Under"], "Forward counting increases numbers."),
                 ("A number chart helps us see ____.", "Patterns", ["Only seasons", "Only coins", "Only shadows"], "The book mentions patterns in number charts."),
             ]),
        ],
    },
    {
        "chapter_name": "Shadow Story (Togalu) (2D Shapes)",
        "page": 32,
        "modules": [
            ("Flat Shapes and Shadows", "Easy", "2D shapes are flat shapes like triangles, squares, rectangles, and circles. In Shadow Story, children meet shapes through shadows and games. A shadow can show the outline of a shape, helping us see corners, sides, and curves.",
             [
                 ("Chapter 4 is about ____ shapes.", "2D", ["3D only", "Money", "Time"], "The contents page names Shadow Story as 2D Shapes."),
                 ("Which shape joins the game with Square?", "Triangle", ["Clock", "Rupee", "Season"], "The sampled page says Triangle and Square joined the game."),
                 ("A square has ____ sides.", "4", ["3", "1", "0"], "A square is a flat shape with four sides."),
                 ("A triangle has ____ corners.", "3", ["4", "2", "0"], "A triangle has three corners."),
                 ("A shadow can show a shape's ____.", "Outline", ["Price", "Month", "Weight only"], "Shadow activities reveal flat outlines."),
             ]),
            ("Position Words in Hide and Seek", "Easy", "The shape story uses hide-and-seek words like behind, near, and under. Children read clues such as 'Are you behind the TV?' and 'You are behind the shoe box.' Position words help us describe exactly where a shape or object is hiding.",
             [
                 ("The story asks, 'Are you behind the ____?'", "TV", ["River", "Moon", "Clock only"], "The PDF line says, 'Are you behind the TV?'"),
                 ("The child says, 'You are behind the shoe ____.'", "Box", ["Tree", "Coin", "Train"], "The PDF says behind the shoe box."),
                 ("Behind is a ____ word.", "Position", ["Money", "Number name", "Season"], "Behind tells where something is."),
                 ("In hide and seek, counting goes 1, 2, 3... ____.", "10", ["100", "50", "2"], "The story page shows '1, 2, 3...10'."),
                 ("Position words help us describe ____ something is.", "Where", ["How much", "How old", "Which month"], "Words like behind tell location."),
             ]),
        ],
    },
    {
        "chapter_name": "Playing with Lines (Orientations of a Line)",
        "page": 44,
        "modules": [
            ("Standing, Sleeping and Slanting Lines", "Easy", "Lines can stand, sleep, or lean. A standing line is vertical, a sleeping line is horizontal, and a slanting line leans like a slide. In this chapter, children look at yoga asanas and spot different kinds of lines in body positions.",
             [
                 ("A standing line is also called ____.", "Vertical", ["Curved", "Round", "Money"], "The PDF says standing or vertical lines."),
                 ("A sleeping line is also called ____.", "Horizontal", ["Vertical", "Rupee", "Season"], "The PDF says sleeping or horizontal lines."),
                 ("A leaning line is called ____.", "Slanting", ["Data", "Money", "Month"], "The chapter asks for vertical and slanting lines."),
                 ("The chapter uses yoga ____ to find lines.", "Asanas", ["Coins", "Buses", "Fruits only"], "The activity asks children to circle aasanas with lines."),
                 ("Children put a star on aasanas with ____ lines.", "Sleeping or horizontal", ["Money", "Only curved", "Only data"], "The PDF says put a star along sleeping/horizontal lines."),
             ]),
            ("Curved Lines and Dot Play", "Easy", "Not all lines are straight. Some lines curve like a smile or a circle edge. The chapter asks children to cross the aasanas that have curved lines and includes playful line activities with dots. Lines help us draw shapes, paths, and pictures.",
             [
                 ("A smile has a ____ line.", "Curved", ["Vertical only", "Rupee", "Ten"], "A smile is a common curved line."),
                 ("The PDF asks children to cross aasanas with ____ lines.", "Curved", ["Money", "Data", "Season"], "The activity says cross the aasanas which have curved lines."),
                 ("Lines help us draw ____.", "Shapes", ["Only coins", "Only days", "Only prices"], "Shapes are made with lines and curves."),
                 ("A circle edge is ____.", "Curved", ["Sleeping only", "Standing only", "Slanting only"], "A circle is made of a curve."),
                 ("Playing with dots can help children make ____.", "Lines and shapes", ["Only rupees", "Only seasons", "Only fruits"], "The book mentions Let us Play with Dots."),
             ]),
        ],
    },
    {
        "chapter_name": "Decoration for Festival (Addition and Subtraction)",
        "page": 50,
        "modules": [
            ("Addition with Tens and Ones", "Medium", "Festival decorations use garlands, flowers, and numbers. Each garland has 10 flowers, so 10 plus loose flowers makes a two-digit number. The chapter shows sums like 10 + 2 = 12 and 30 + 7 = 37. Tens and ones make addition easier.",
             [
                 ("Each garland has ____ flowers.", "10", ["2", "5", "100"], "The PDF says each garland has 10 flowers."),
                 ("10 + 2 = ____.", "12", ["10", "20", "8"], "The page shows 10 + 2 = 12."),
                 ("30 + 7 = ____.", "37", ["73", "30", "27"], "The page shows 30 + 7 = 37."),
                 ("40 + 8 = ____.", "48", ["84", "38", "58"], "The page shows 40 + 8 = 48."),
                 ("50 + 3 = ____.", "53", ["35", "50", "43"], "The page shows 50 + 3 = 53."),
             ]),
            ("Subtraction with Blocks", "Medium", "Subtraction means finding what is left. The chapter uses tens and ones blocks to subtract, such as 45 - 12. We subtract ones from ones and tens from tens. Story questions also use money, such as buying pencils or notebooks and finding the amount left.",
             [
                 ("45 - 12 = ____.", "33", ["57", "23", "45"], "The block example shows 45 minus 12 leaves 33."),
                 ("Subtract 24 from 37 gives ____.", "13", ["61", "23", "11"], "37 - 24 = 13."),
                 ("If Shikha has ₹82 and spends ₹22, she has ₹____ left.", "60", ["104", "22", "50"], "82 - 22 = 60."),
                 ("If Ruby has ₹60 and spends ₹20, she has ₹____ left.", "40", ["80", "20", "30"], "60 - 20 = 40."),
                 ("In tens and ones subtraction, ones are subtracted from ____.", "Ones", ["Months", "Shapes", "Seasons"], "Place value keeps ones with ones and tens with tens."),
             ]),
        ],
    },
    {
        "chapter_name": "Rani's Gift (Measurement)",
        "page": 71,
        "modules": [
            ("Length and Paths", "Medium", "Measurement helps us compare how long, short, near, or far things are. The chapter includes activities like choosing the longest path and counting blocks. Children learn that measurement can be done with simple classroom objects before using standard tools.",
             [
                 ("Measurement helps compare ____.", "Length", ["Only seasons", "Only colours", "Only stories"], "This chapter is listed as Measurement."),
                 ("The book mentions choosing the longest ____.", "Path", ["Coin", "Month", "Shape only"], "The About the Book section mentions Choose the Longest Path in Chapter 7."),
                 ("Blocks can help measure ____.", "Length or height", ["Only time", "Only money", "Only fruits"], "The book mentions How Many Blocks?"),
                 ("A longer path has ____ length.", "More", ["Less", "No", "Only curved"], "Longer means greater length."),
                 ("Measurement can begin with ____ objects.", "Simple classroom", ["Invisible", "Only digital", "Only money"], "Children use local materials and objects."),
             ]),
            ("Heavier and Lighter", "Medium", "Weight tells how heavy or light something is. In Pumpkin's Chaupal, children compare vegetables like pumpkin, watermelon, carrot, capsicum, cauliflower, and bottle gourd. Words like heavier, lighter, heaviest, and lightest help children compare weight.",
             [
                 ("Pumpkin's Chaupal asks children to compare vegetables as lighter or ____.", "Heavier", ["Earlier", "Rounder only", "Richer"], "The page asks which vegetables are lighter or heavier."),
                 ("Muskmelon is heavier than ____.", "Carrot", ["A clock", "A coin", "A line"], "The sampled page states muskmelon is heavier than carrot."),
                 ("Which word means most heavy?", "Heaviest", ["Lightest", "Shortest", "Earliest"], "Heaviest means the greatest weight."),
                 ("Which word means least heavy?", "Lightest", ["Heaviest", "Longest", "Latest"], "Lightest means the smallest weight."),
                 ("Vegetables in this activity include pumpkin and ____.", "Watermelon", ["Train", "Notebook", "Rupee"], "The page asks whether pumpkin or watermelon is heavier."),
             ]),
        ],
    },
    {
        "chapter_name": "Grouping and Sharing (Multiplication and Division)",
        "page": 83,
        "modules": [
            ("Equal Groups and Multiplication", "Medium", "Multiplication is quick counting of equal groups. The chapter shows groups of flowers, bindis, buttons, and shirts. For example, 6 groups of 4 can be written as 6 × 4. When each group has the same number, multiplication helps us find the total.",
             [
                 ("6 groups of 4 is written as ____.", "6 × 4", ["6 + 0", "4 - 6", "6 ₹ 4"], "The PDF shows 6 groups of 4 and 6 × 4."),
                 ("6 × 4 = ____.", "24", ["10", "20", "64"], "Six groups of four make twenty-four."),
                 ("4 groups of 6 is written as ____.", "4 × 6", ["4 - 6", "6 - 4", "4 + 0"], "The PDF shows 4 groups of 6 and 4 × 6."),
                 ("8 packets with 5 bindis each gives ____ bindis.", "40", ["13", "35", "8"], "8 × 5 = 40."),
                 ("7 shirts with 4 buttons each need ____ buttons.", "28", ["11", "24", "74"], "7 × 4 = 28."),
             ]),
            ("Sharing and Division", "Medium", "Division begins with fair sharing. If we share objects equally, each group should get the same number. The chapter connects grouping and sharing, helping children see that multiplication makes groups and division shares them equally.",
             [
                 ("Division begins with fair ____.", "Sharing", ["Hiding", "Spending", "Drawing only"], "The chapter title includes Grouping and Sharing."),
                 ("Equal sharing means each group gets the ____ number.", "Same", ["Different", "Largest", "Hidden"], "Fair sharing gives equal amounts."),
                 ("20 objects shared into 4 equal groups gives ____ in each group.", "5", ["4", "10", "24"], "20 divided into four equal groups is five each."),
                 ("Grouping and sharing are linked to multiplication and ____.", "Division", ["Seasons", "Money only", "Lines only"], "The contents page says Multiplication and Division."),
                 ("If one group has more, sharing is not ____.", "Equal", ["Colourful", "Round", "Vertical"], "Fair sharing needs equal groups."),
             ]),
        ],
    },
    {
        "chapter_name": "Which Season is it? (Measurement of Time)",
        "page": 98,
        "modules": [
            ("Seasons, Dates and Daily Events", "Easy", "Time helps us tell when things happen. This chapter includes seasons, dates, train travel, sightseeing, and family events. Children read simple date and time clues like 24 Nov, 8:25 AM, 1:15 PM, and 10:00 PM.",
             [
                 ("Chapter 9 is about measurement of ____.", "Time", ["Money", "Weight", "Data"], "The contents page says Measurement of Time."),
                 ("The trip story shows the date 24 ____.", "Nov.", ["Jan.", "May", "Aug."], "The sampled page shows Date: 24 Nov."),
                 ("The train time shown is 8:25 ____.", "AM", ["PM only", "₹", "kg"], "The sampled page shows Time: 8:25 AM."),
                 ("10:00 PM is a ____ time.", "Night", ["Morning", "Noon", "Before sunrise only"], "PM late evening/night time is used in the story."),
                 ("Seasons are also connected to ____.", "Time", ["Only money", "Only shapes", "Only blocks"], "Seasons show changes over the year."),
             ]),
            ("Reading Hours and Sequence", "Medium", "A day is a sequence of events. The trip page says 'just 1 more hour' and shows different times. Children learn to read time words, order events, and understand before, after, today, tomorrow, and day after tomorrow.",
             [
                 ("'Just 1 more hour' tells a length of ____.", "Time", ["Money", "Shape", "Data"], "An hour measures time."),
                 ("Day after tomorrow means two days ____ today.", "After", ["Before", "Inside", "Under"], "It comes after tomorrow."),
                 ("Which comes earlier: 8:25 AM or 1:15 PM?", "8:25 AM", ["1:15 PM", "10:00 PM", "Both same"], "Morning AM time comes before afternoon PM time."),
                 ("Events in a trip can be placed in ____.", "Order", ["Only shapes", "Only coins", "Only colours"], "Time sequence helps order events."),
                 ("A clock helps us read ____.", "Time", ["Vegetable weight only", "Toy data only", "Number of flowers only"], "Clocks show time."),
             ]),
        ],
    },
    {
        "chapter_name": "Fun at the Fair (Money)",
        "page": 113,
        "modules": [
            ("Spending Money at a Fair", "Medium", "Money is used to buy things and enjoy activities at a fair. Rupal's mother gives her ₹50, and she spends most of it on rides. The chapter asks children to talk about what they buy, how much they spend, and how money is used in daily life.",
             [
                 ("Rupal's mother gave her ₹____.", "50", ["5", "100", "10"], "The sampled page says her mother gave her ₹50."),
                 ("Rupal spent most money on ____.", "Rides", ["Books only", "Vegetables", "Pencils"], "The PDF says she spent most of it on her favourite rides."),
                 ("Money is used to ____ things.", "Buy", ["Only sleep", "Only draw lines", "Only tell seasons"], "The chapter context is spending at a fair."),
                 ("The chapter asks children how much money they ____.", "Spend", ["Hide", "Roll", "Stack"], "The page discusses how much children spend at fairs."),
                 ("A fair is a place where children may enjoy ____.", "Rides", ["Only homework", "Only sleeping", "Only measuring blocks"], "Rides are named in the chapter."),
             ]),
            ("Adding and Subtracting Rupees", "Medium", "Money problems use addition and subtraction. If Jayant spends ₹25 on pens and ₹40 on notebooks, we add to find the total. If Ajay has ₹58 and spends ₹48, we subtract to find what is left. The chapter also mentions paying with mobile phones.",
             [
                 ("₹25 + ₹40 = ₹____.", "65", ["55", "15", "75"], "Jayant's total is 25 + 40 = 65."),
                 ("₹43 plus ₹14 more is ₹____.", "57", ["29", "47", "67"], "Kanika has 43 + 14 = 57."),
                 ("₹30 + ₹60 = ₹____.", "90", ["30", "60", "100"], "Bread and chocolate cost 30 + 60 = 90."),
                 ("₹58 - ₹48 = ₹____.", "10", ["16", "20", "48"], "Ajay has 10 rupees left."),
                 ("The PDF mentions paying using ____ phones.", "Mobile", ["Toy", "Paper", "Shadow"], "The page asks if children have seen payment using mobile phones."),
             ]),
        ],
    },
    {
        "chapter_name": "Data Handling",
        "page": 123,
        "modules": [
            ("Tables for Colours and Fruits", "Medium", "Data handling means collecting answers, counting them, and reading the result. The chapter starts with favourite colours and picnic fruits. Children complete tables and answer which colour or fruit is most liked, least liked, more than, less than, or equal to.",
             [
                 ("The favourite colours table includes red, green, blue and ____.", "Yellow", ["Black only", "Orange only", "White only"], "The PDF lists red, green, blue, and yellow."),
                 ("Data tables help us count number of ____.", "Children", ["Months only", "Rupees only", "Lines only"], "The table heading says Number of Children."),
                 ("Most liked means liked by the ____ number.", "Greatest", ["Smallest", "Same always", "Hidden"], "Most means greatest count."),
                 ("Least liked means liked by the ____ number.", "Smallest", ["Greatest", "Same always", "Last page only"], "Least means smallest count."),
                 ("Picnic Day data is about favourite ____.", "Fruits", ["Trains", "Coins", "Lines"], "The page says children are eating their favourite fruits."),
             ]),
            ("Charts for School, Games and Families", "Medium", "Charts make data easy to see. The chapter uses modes of coming to school, games children play, vegetables they like, grandparents at home, and number of family members. Children read tables, draw faces, and compare counts.",
             [
                 ("One chart shows mode of coming to ____.", "School", ["Beach", "Fair only", "Moon"], "The PDF table is about coming to school."),
                 ("The transport chart includes bus, bike and ____.", "Bicycle", ["Pumpkin", "Rupee", "Triangle"], "The PDF lists bus, bike, bicycle, and more."),
                 ("Games data includes cricket and ____.", "Kabaddi", ["Clock", "Bottle", "Garland"], "The PDF table lists games including Kabaddi."),
                 ("The project asks about families living with ____.", "Grandparents", ["Only toys", "Only fruits", "Only lines"], "The project records grandparents in families."),
                 ("Drawing faces in a chart means each face can stand for ____ student.", "1", ["10 always", "100", "0"], "The PDF says one face equals one student."),
             ]),
        ],
    },
]


def build():
    output = []
    manifest = {
        "source": "NCERT Joyful Mathematics Class 2 PDF, first edition 2023",
        "syllabus": "CBSE",
        "class": "Class 2",
        "subject": "Mathematics",
        "chapters": [],
        "module_total": 0,
        "question_total": 0,
    }
    counter = 1
    for chapter in CHAPTERS:
        chapter_obj = {"chapter_name": chapter["chapter_name"], "modules": []}
        chapter_manifest = {"chapter_name": chapter["chapter_name"], "page": chapter["page"], "modules": []}
        for topic, difficulty, explanation, facts in chapter["modules"]:
            timer = 45 if difficulty == "Medium" else 30
            questions = [q(i + 1, *fact, timer) for i, fact in enumerate(facts)]
            module_id = f"cbse_c2_m{counter:03d}_{slug(topic)}"
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
                "source_basis": "PDF contents page and chapter activity text",
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
    assert len(output) == 11
    ids = set()
    for chapter in output:
        assert chapter["chapter_name"]
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
