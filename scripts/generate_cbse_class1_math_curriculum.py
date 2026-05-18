import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "src" / "data"
OUTPUT_JSON = DATA_DIR / "cbse_class1_mathematics_learning_journey.json"
OUTPUT_MANIFEST = DATA_DIR / "cbse_class1_mathematics_validation_manifest.json"


def opt(correct, wrongs):
    values = [correct]
    for wrong in wrongs:
        if wrong != correct and wrong not in values:
            values.append(wrong)
        if len(values) == 4:
            break
    while len(values) < 4:
        values.append(["Not sure", "Both", "None"][len(values) - 1])
    return [values[i] for i in [1, 3, 0, 2]]


def q(question_id, text, correct, wrongs, rationale, timer=30):
    return {
        "question_id": question_id,
        "question_text": text,
        "options": opt(correct, wrongs),
        "correct_answer": correct,
        "rationale": rationale,
        "timer_per_question_seconds": timer,
    }


def slug(value):
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


CHAPTERS = [
    {
        "chapter_name": "Finding the Furry Cat! (Pre-number Concepts)",
        "page": 1,
        "modules": [
            {
                "topic_name": "Inside and Outside",
                "explanation": "Imagine your school bag is a tiny room. A pencil kept in the bag is inside, and a pencil kept on the table is outside. In the furry cat poem, the cat hides inside a backpack and outside the red rack. This module helps you use position words while looking carefully at pictures and real objects around you.",
                "facts": [
                    ("Where was the furry cat hiding in one line of the poem?", "Inside the backpack", ["On the moon", "Under the sea", "Behind the sun"], "The poem asks, 'Are you inside the backpack?'"),
                    ("If a ball goes into a basket, children say ____.", "IN", ["OUT", "TOP", "BEFORE"], "The textbook ball game says children say IN when the ball goes inside."),
                    ("Where should garbage be thrown?", "Inside the dustbin", ["Outside the dustbin", "On the bed", "Under the book"], "The activity asks children to choose inside the dustbin."),
                    ("A thing kept outside the classroom is ____ the classroom.", "Outside", ["Inside", "Between", "After"], "Outside means not in the room or object."),
                    ("Which word tells that something is in a box?", "Inside", ["Outside", "After", "Before"], "Inside means within something."),
                ],
            },
            {
                "topic_name": "Above, Below, On and Under",
                "explanation": "Position words are like clues in a treasure hunt. Above means higher, below means lower, on means touching the top, and under means beneath. In the chapter, children look for the furry cat under the bed, above the hat, below the mat, and on the car. These words help you describe where things are.",
                "facts": [
                    ("In the poem, the cat is sleeping under ____.", "My bed", ["The sun", "The clock", "The tree top"], "The poem asks, 'Are you sleeping under my bed?'"),
                    ("The red ball is above, under, or on the bed?", "On the bed", ["Inside the dustbin", "After the bed", "Before the bed"], "The textbook picture activity uses the word on for objects placed on something."),
                    ("Eyebrows are drawn ____ the eyes.", "Above", ["Below", "Inside", "After"], "The activity asks children to draw eyebrows above the eyes."),
                    ("A smile is drawn ____ the nose.", "Below", ["Above", "Inside", "Before"], "The activity asks children to draw a smile below the nose."),
                    ("Birds sitting on a tree are ____ the tree.", "On", ["Inside", "After", "Before"], "The chapter asks children to choose words such as on or under for tree pictures."),
                ],
            },
            {
                "topic_name": "Before, After and Grouping",
                "explanation": "A train game helps us learn before and after. If you stand in a line, one friend may be before you and another may be after you. The chapter also shows grouping: leaves in one group, pebbles in another, and chalk pieces in another. Grouping helps us sort things that are alike.",
                "facts": [
                    ("In the train rhyme game, children tell who is ____ and after each child.", "Before", ["Inside", "Round", "Heavy"], "The textbook train game practises before and after."),
                    ("Putting all leaves together is called making a ____.", "Group", ["Clock", "Coin", "Season"], "The chapter shows leaves placed in one group."),
                    ("Pebbles kept together form one ____.", "Group", ["Day", "Shape", "Number name"], "The textbook asks children to sort objects like pebbles."),
                    ("Which pair of words tells order in a line?", "Before and after", ["Inside and round", "Heavy and money", "Tall and coin"], "Before and after describe order."),
                    ("Which objects does the chapter suggest for sorting?", "Seeds and leaves", ["Stars and planets", "Cars and trains only", "Months only"], "The teacher note mentions seeds, leaves, beads, and similar objects."),
                ],
            },
        ],
    },
    {
        "chapter_name": "What is Long? What is Round? (Shapes)",
        "page": 10,
        "modules": [
            {
                "topic_name": "Long, Round and Shape Words",
                "explanation": "Shapes are everywhere. Some things are long like a stick, some are round like a bangle, and some have corners like a box. This chapter invites children to look at objects, talk about what is long or round, and notice how things are shaped in the home, school, and playground.",
                "facts": [
                    ("Which word can describe a stick?", "Long", ["Today", "Rupee", "Before"], "A stick is a common long object."),
                    ("Which word can describe a bangle?", "Round", ["After", "Heavy", "Evening"], "A bangle is round in shape."),
                    ("What do we observe in this chapter?", "Shapes of objects", ["Only festivals", "Only money", "Only seasons"], "The chapter title is about long and round shapes."),
                    ("A ball is usually ____.", "Round", ["Flat only", "Before", "After"], "Balls are used as round objects in early shape learning."),
                    ("Looking at classroom things helps us learn ____.", "Shapes", ["Months only", "Coins only", "Stories only"], "Children identify shapes from nearby objects."),
                ],
            },
            {
                "topic_name": "Rolling and Sliding",
                "explanation": "Some objects roll because they are round. Some objects slide because they have flat faces. A ball rolls easily, while a book can slide on a table. The textbook asks children to collect objects and check whether they roll, slide, or do both. Learning by trying makes shapes easy to remember.",
                "facts": [
                    ("The textbook asks children to write R for ____ objects.", "Rolling", ["Reading", "Rupee", "Red only"], "The activity says write R for rolling objects."),
                    ("The textbook asks children to write S for ____ objects.", "Sliding", ["Singing", "Saving", "Summer"], "The activity says write S for sliding objects."),
                    ("A striker in carrom usually ____ on the board.", "Slides", ["Drinks", "Counts", "Sleeps"], "The chapter says a striker slides to reach the corner."),
                    ("Which object is more likely to roll?", "Ball", ["Book", "Mat", "Notebook"], "Round objects like balls roll."),
                    ("What should children collect to test rolling and sliding?", "Different objects", ["Only flowers", "Only numbers", "Only days"], "The activity asks children to collect different objects from surroundings."),
                ],
            },
        ],
    },
    {
        "chapter_name": "Mango Treat (Numbers 1 to 9)",
        "page": 18,
        "modules": [
            {
                "topic_name": "Counting 1 to 9",
                "explanation": "Counting tells us how many things we have. In Mango Treat, children count objects like mangoes, jamuns, sheep, and boxes. Start with one object, touch or point to each item once, and say the numbers in order. Counting slowly helps you avoid missing or counting the same thing twice.",
                "facts": [
                    ("Which numbers are practised in Mango Treat?", "1 to 9", ["21 to 99", "Only 100", "Only 0"], "The chapter title says Numbers 1 to 9."),
                    ("What should you do when counting objects?", "Count each object once", ["Skip objects", "Count only colours", "Close your eyes"], "Counting works best when each item is counted once."),
                    ("The PDF asks children to count yellow ____.", "Boxes", ["Rupees", "Weeks", "Seasons"], "One activity asks how many yellow boxes are there."),
                    ("The PDF asks children to count ____ in a picture.", "Jamuns", ["Clocks", "Coins", "Shoes only"], "One question asks how many jamuns are there."),
                    ("The PDF asks children to write the number of ____.", "Sheep", ["Months", "Wheels only", "Notes"], "The page asks for the number of sheep seen in the picture."),
                ],
            },
            {
                "topic_name": "Number Names and Quantity",
                "explanation": "A number and a group are partners. The number 5 can match five mangoes, five fingers, or five dots. The chapter helps children see that a written number tells the size of a group. When you match a number to objects, you are reading quantity like a little mathematician.",
                "facts": [
                    ("What does a number tell us?", "How many", ["How cold", "Which season", "Which festival"], "Numbers show quantity."),
                    ("Which group matches the number 4?", "Four objects", ["One object", "Nine objects", "No objects"], "The number 4 names a group of four."),
                    ("Which number comes just after 5?", "6", ["4", "2", "9"], "Counting order goes 5, 6."),
                    ("Which number comes just before 8?", "7", ["9", "1", "5"], "Counting order goes 7, 8."),
                    ("If there are 3 mangoes, the matching number is ____.", "3", ["7", "9", "1"], "Three objects match the number 3."),
                ],
            },
        ],
    },
    {
        "chapter_name": "Making 10 (Numbers 10 to 20)",
        "page": 33,
        "modules": [
            {
                "topic_name": "Making a Group of 10",
                "explanation": "Ten is a friendly bundle. When we collect 10 things together, counting bigger numbers becomes easier. The textbook asks children to recognise a group of 10 while counting beyond 10 and to find things around them that come in groups of 10, like bindi cards.",
                "facts": [
                    ("The chapter asks children to recognise a group of ____.", "10", ["3", "50", "100"], "The project work focuses on groups of 10."),
                    ("A bindi card can show bindis in groups of ____.", "10", ["2", "7", "99"], "The PDF gives bindi cards as an example of groups of 10."),
                    ("Making 10 helps when counting numbers beyond ____.", "10", ["1 only", "2 only", "5 only"], "The teacher note says recognise a group of 10 while counting beyond 10."),
                    ("Which number comes after 10?", "11", ["9", "20", "1"], "Counting order goes 10, 11."),
                    ("Which number comes before 20?", "19", ["21", "10", "9"], "Counting order goes 19, 20."),
                ],
            },
            {
                "topic_name": "Counting 10 to 20",
                "explanation": "Numbers from 10 to 20 are like a small number train. We start from 10 and move one step at a time: 11, 12, 13, and so on. The textbook asks children to make number cards from 10 to 20 and join numbers from 1 to 20.",
                "facts": [
                    ("Which number cards does the project ask children to make?", "10 to 20", ["1 to 5", "50 to 60", "Only 100"], "The PDF says children can make number cards 10 to 20."),
                    ("The join-the-numbers activity goes from 1 to ____.", "20", ["5", "9", "100"], "The PDF asks children to join numbers from 1 to 20."),
                    ("What comes after 14?", "15", ["13", "11", "20"], "Counting order goes 14, 15."),
                    ("What comes before 17?", "16", ["18", "10", "20"], "Counting order goes 16, 17."),
                    ("Which number is in the group 10 to 20?", "18", ["8", "28", "99"], "18 is between 10 and 20."),
                ],
            },
        ],
    },
    {
        "chapter_name": "How Many? (Addition and Subtraction of Single Digit Numbers)",
        "page": 48,
        "modules": [
            {
                "topic_name": "Adding Single Digit Numbers",
                "explanation": "Addition means putting groups together. If you have 3 mangoes and get 2 more, you count all of them to get 5. In this chapter, children use pictures, number strips, and small objects to understand how many altogether.",
                "difficulty": "Medium",
                "facts": [
                    ("What does addition mean?", "Putting together", ["Taking away", "Sleeping", "Sorting only"], "Addition combines groups."),
                    ("3 + 2 = ____.", "5", ["4", "6", "1"], "Three and two together make five."),
                    ("4 + 1 = ____.", "5", ["3", "6", "9"], "Four and one more make five."),
                    ("When we add, the number usually becomes ____.", "More", ["Less", "A season", "A coin"], "Adding more objects increases the count."),
                    ("Which sign is used for addition?", "+", ["-", "=", "x"], "The plus sign shows addition."),
                ],
            },
            {
                "topic_name": "Subtracting with a Number Strip",
                "explanation": "Subtraction means taking away or moving back. The textbook shows hopping backwards on a number strip. If you jump 3 steps back from 9, you reach 6, so 9 - 3 = 6. A number strip makes subtraction feel like walking backwards.",
                "difficulty": "Medium",
                "facts": [
                    ("Subtraction means ____.", "Taking away", ["Putting together", "Making patterns", "Counting seasons"], "Subtraction removes or moves back."),
                    ("The textbook says jump 3 steps back from 9 gives ____.", "6", ["7", "9", "3"], "The PDF shows 9 - 3 = 6."),
                    ("7 - 4 = ____.", "3", ["11", "4", "7"], "Jumping four steps back from 7 reaches 3."),
                    ("8 - 2 = ____.", "6", ["10", "5", "2"], "Taking away two from eight leaves six."),
                    ("Which sign is used for subtraction?", "-", ["+", "=", "R"], "The minus sign shows subtraction."),
                ],
            },
        ],
    },
    {
        "chapter_name": "Vegetable Farm (Addition and Subtraction up to 20)",
        "page": 64,
        "modules": [
            {
                "topic_name": "Addition up to 20",
                "explanation": "Bigger addition still means putting groups together. In Vegetable Farm, children solve stories with buses, diyas, bananas, and other familiar objects. Read the story slowly, find what is added, and count the total carefully.",
                "difficulty": "Medium",
                "facts": [
                    ("In the bus story, 6 children sit first and 8 more board. What operation is used first?", "Addition", ["Subtraction only", "Pattern", "Money"], "More children board the bus, so we add."),
                    ("6 + 8 = ____.", "14", ["12", "6", "20"], "Six and eight together make fourteen."),
                    ("9 diyas and 7 more diyas make ____ diyas.", "16", ["2", "14", "20"], "Nine plus seven equals sixteen."),
                    ("When more children board a bus, the number becomes ____.", "More", ["Less", "Zero always", "A shape"], "Boarding adds children."),
                    ("Addition stories ask us to find the ____.", "Total", ["Colour", "Season", "Coin name"], "Addition finds how many altogether."),
                ],
            },
            {
                "topic_name": "Subtraction up to 20",
                "explanation": "Subtraction stories tell us that something was used, sold, eaten, or shared. In the chapter, a potter sells diyas and children get down from a bus. Look for action words like sold, left, ate, and shared. These words help you decide to subtract.",
                "difficulty": "Medium",
                "facts": [
                    ("If a potter had 9 diyas and sold 5, which operation is used?", "Subtraction", ["Addition", "Pattern", "Rolling"], "Selling diyas takes them away."),
                    ("18 seats and 9 children sitting leaves ____ seats.", "9", ["27", "18", "6"], "18 - 9 = 9."),
                    ("12 bananas, 5 left. How many were eaten?", "7", ["17", "5", "12"], "12 - 5 = 7."),
                    ("Which word often signals subtraction?", "Left", ["Altogether", "More board", "Pattern"], "Left tells what remains after taking away."),
                    ("When children get down from a bus, the number becomes ____.", "Less", ["More", "Round", "Before"], "Getting down removes children from the bus."),
                ],
            },
        ],
    },
    {
        "chapter_name": "Lina's Family (Measurement)",
        "page": 72,
        "modules": [
            {
                "topic_name": "Longer and Shorter",
                "explanation": "Measurement begins with comparing. A ribbon can be longer than another ribbon, and a paper strip can be shorter than another strip. The textbook asks children to paste colourful strips and notice which portion is shorter and which is longer.",
                "facts": [
                    ("Which word tells that a strip has more length?", "Longer", ["Shorter", "Inside", "After"], "Longer means it has more length."),
                    ("Which word tells that a strip has less length?", "Shorter", ["Longer", "Round", "Before"], "Shorter means it has less length."),
                    ("The textbook asks children to paste colourful paper ____.", "Strips", ["Coins", "Clocks", "Buses"], "The activity uses paper strips."),
                    ("Comparing two pencils can tell which is ____.", "Longer", ["A month", "A rupee", "A pattern only"], "Length comparison shows longer or shorter."),
                    ("Measurement starts by ____ objects.", "Comparing", ["Hiding", "Spending", "Sleeping"], "Children compare size, length, and capacity."),
                ],
            },
            {
                "topic_name": "Capacity and Carrying",
                "explanation": "Some containers hold more water and some hold less. The textbook asks children to use bottles, bowls, and glasses to see how many glasses fill a bottle. It also asks which things are easier or difficult to carry. Measurement helps us talk about size, weight, and capacity.",
                "facts": [
                    ("Which container can be used to test water capacity?", "Bottle", ["Calendar", "Coin", "Number card only"], "The PDF mentions bottles, bowls, and glasses."),
                    ("The textbook asks how many glasses or bowls can fill a ____.", "Bottle", ["Tree", "Shoe", "Clock"], "The activity fills a bottle with glasses or bowls."),
                    ("A thing that holds more water has more ____.", "Capacity", ["Pattern", "Before", "After"], "Capacity is how much a container can hold."),
                    ("The chapter discusses things easier and difficult to ____.", "Carry", ["Read upside down", "Spend only", "Hide"], "The PDF asks children to list things easier or difficult to carry."),
                    ("Using a bucket for bathing can save ____.", "Water", ["Time only", "Coins only", "Patterns"], "The teacher note discusses avoiding water waste."),
                ],
            },
        ],
    },
    {
        "chapter_name": "Fun with Numbers (Numbers 21 to 99)",
        "page": 84,
        "modules": [
            {
                "topic_name": "Counting 21 to 99",
                "explanation": "Numbers after 20 grow in families: twenties, thirties, forties, and more. When children count from 21 to 99, they practise saying numbers in order and seeing tens and ones. The chapter also includes number arrangements and drawings to make counting playful.",
                "difficulty": "Medium",
                "facts": [
                    ("Which number is just after 20?", "21", ["19", "10", "99"], "Counting goes 20, 21."),
                    ("Which number is just before 40?", "39", ["41", "30", "14"], "39 comes before 40."),
                    ("Which number is between 50 and 54 and has digit sum 7?", "52", ["51", "53", "54"], "5 + 2 = 7, and 52 is between 50 and 54."),
                    ("Numbers 21 to 99 include ____.", "Two-digit numbers", ["Only one-digit numbers", "Only coins", "Only seasons"], "21 to 99 are two-digit numbers."),
                    ("Which number is after 35?", "36", ["34", "30", "53"], "Counting order goes 35, 36."),
                ],
            },
            {
                "topic_name": "Number Puzzles and Arrangements",
                "explanation": "Number puzzles train the eyes and mind. The textbook includes hidden number cards, missing pieces, shadow images, and questions like 'Who am I?' These activities help children recognise numbers, compare them, and think carefully before answering.",
                "difficulty": "Medium",
                "facts": [
                    ("The puzzle asks children to find numbers from 1 to ____.", "10", ["5", "20", "99"], "The word-search puzzle says find numbers from 1 to 10."),
                    ("Gillu's favourite number is ____.", "8", ["5", "10", "25"], "The PDF says Gillu's favourite number is 8."),
                    ("The puzzle asks what happens when 5 is added to a number to get ____.", "24", ["8", "10", "40"], "One clue says add 5 to me and you will get 24."),
                    ("Which activity hides number cards with bowls?", "Recognising numbers", ["Spending money", "Measuring water", "Making seasons"], "The puzzle asks children to recognise hidden numbers."),
                    ("Number puzzles help us ____.", "Think carefully", ["Ignore numbers", "Only sing", "Only spend"], "Puzzles build number sense and reasoning."),
                ],
            },
        ],
    },
    {
        "chapter_name": "Utsav (Patterns)",
        "page": 98,
        "modules": [
            {
                "topic_name": "Patterns Around Us",
                "explanation": "A pattern is something that repeats in a special way. The Utsav chapter asks children to observe patterns in leaves, butterflies, animal skins, curtains, sarees, tiles, and beehives. Once you notice the repeat, you can guess what comes next.",
                "facts": [
                    ("What is a pattern?", "Something that repeats", ["Something that disappears", "Only a coin", "Only a clock"], "Patterns repeat in an order."),
                    ("Which natural object can show a pattern?", "Leaves", ["Rupee note only", "Bus stop only", "Dustbin only"], "The PDF mentions leaves and butterflies."),
                    ("The textbook mentions patterns on animal skins like ____.", "Zebra", ["Cup", "Clock", "Bottle"], "The PDF lists cat, dog, zebra, and tiger skins."),
                    ("What can we do after seeing a pattern?", "Guess what comes next", ["Forget the order", "Spend money", "Drink water"], "Recognising repetition helps predict the next item."),
                    ("Which home item may have patterns?", "Curtains", ["Only water", "Only time", "Only subtraction"], "The PDF mentions curtains, sarees, dupattas, and tiles."),
                ],
            },
            {
                "topic_name": "Making Patterns",
                "explanation": "Patterns can be made with objects and actions. The textbook asks children to arrange pebbles, flowers, leaves, glasses, bowls, sticks, bangles, coins, and caps. It also suggests clapping, snapping fingers, and stamping feet. Patterns can be seen, heard, and acted.",
                "facts": [
                    ("Which object can be arranged into a pattern?", "Pebbles", ["Only clouds", "Only calendars", "Only buses"], "The PDF suggests pebbles, flowers, leaves, and more."),
                    ("Which action can make a pattern?", "Clapping", ["Sleeping", "Losing", "Erasing only"], "The PDF mentions clapping, snapping, and stamping."),
                    ("Kolam or rangoli is used in this chapter for ____.", "Patterns", ["Money", "Subtraction only", "Capacity"], "The PDF shows completing a kolam/rangoli pattern."),
                    ("A pattern made with sounds may use ____.", "Snapping fingers", ["Coins only", "Bottle only", "Dustbin only"], "The PDF suggests snapping fingers."),
                    ("To continue a pattern, we look at the ____.", "Repeating order", ["Price", "Season name", "Page number only"], "The repeat tells what comes next."),
                ],
            },
        ],
    },
    {
        "chapter_name": "How do I Spend my Day? (Time)",
        "page": 105,
        "modules": [
            {
                "topic_name": "Daily Routine and Time",
                "explanation": "Time helps us talk about our day. We wake up, eat, study, play, and sleep at different times. This chapter asks children to think about how they spend the day. A routine is like a story in order: first morning activities, then daytime work, then evening and night.",
                "facts": [
                    ("What does a daily routine show?", "Order of activities in a day", ["Only money", "Only shapes", "Only toys"], "The chapter asks how children spend the day."),
                    ("Which activity usually happens at night?", "Sleeping", ["Morning assembly", "Breakfast before waking", "Buying vegetables only"], "Children usually sleep at night."),
                    ("Which comes first in a school day?", "Waking up", ["Going to sleep", "Evening play", "Dinner"], "A day usually starts with waking up."),
                    ("Time helps us know ____.", "When things happen", ["Only how much money", "Only which toy", "Only colour"], "Time tells when activities happen."),
                    ("A routine should be in ____.", "Order", ["Random hiding", "Only circles", "Only coins"], "Daily events happen in sequence."),
                ],
            },
            {
                "topic_name": "Seasons and Activities",
                "explanation": "The time chapter also asks children to name seasons and match them with pictures. We eat, wear, and do different things in different seasons. For example, children may like cool foods in summer and warm clothes in winter. Seasons help us notice changes through the year.",
                "facts": [
                    ("The PDF asks children to write the name of the ____.", "Seasons", ["Coins", "Buses", "Shapes only"], "The page says write the name of the seasons."),
                    ("The chapter asks what children like to eat in ____.", "Summer", ["Only Monday", "Only night", "Only subtraction"], "The PDF asks what you like to eat in summer."),
                    ("The chapter asks what children like to wear in ____.", "Winter", ["Only morning", "Only a bus", "Only a basket"], "The PDF asks what you like to wear in winter."),
                    ("Summer and winter are examples of ____.", "Seasons", ["Coins", "Patterns only", "Number signs"], "Summer and winter are seasons."),
                    ("Pictures can be matched with season ____.", "Names", ["Prices only", "Answers only", "Roll numbers only"], "The activity asks children to match seasons with pictures."),
                ],
            },
        ],
    },
    {
        "chapter_name": "How Many Times? (Multiplication)",
        "page": 111,
        "modules": [
            {
                "topic_name": "Repeated Addition",
                "explanation": "Multiplication begins as repeated addition. If there are 5 groups of 3 pencils, we can add 3 again and again. The textbook shows erasers, pencils, and apples in packs and asks children to find the total using 'times'.",
                "difficulty": "Medium",
                "facts": [
                    ("Multiplication in this chapter begins as ____.", "Repeated addition", ["Taking away only", "Telling seasons", "Buying only"], "The page shows repeated addition with times."),
                    ("5 times 3 means adding ____ five times.", "3", ["5", "8", "2"], "5 times 3 is 3 + 3 + 3 + 3 + 3."),
                    ("3 times 3 = ____.", "9", ["6", "12", "3"], "3 + 3 + 3 = 9."),
                    ("4 times 2 = ____.", "8", ["6", "10", "2"], "2 + 2 + 2 + 2 = 8."),
                    ("The chapter uses packs of erasers, pencils and ____.", "Apples", ["Seasons", "Clocks", "Dolls"], "The PDF mentions erasers, pencils, and apples."),
                ],
            },
            {
                "topic_name": "Equal Groups",
                "explanation": "Equal groups make counting faster. If every cycle has 2 wheels, you can count wheels by twos. The project asks children to find how many cycles are at home and then find the total number of wheels. Equal groups are the first step toward multiplication.",
                "difficulty": "Medium",
                "facts": [
                    ("A cycle has ____ wheels.", "2", ["1", "3", "5"], "A usual cycle has two wheels."),
                    ("The project asks children to find the total number of cycle ____.", "Wheels", ["Flowers", "Coins", "Days"], "The PDF cycle project asks for total wheels."),
                    ("Equal groups help us count ____.", "Faster", ["Slower always", "Only seasons", "Only money"], "Equal groups support repeated addition."),
                    ("If 2 cycles each have 2 wheels, total wheels are ____.", "4", ["2", "6", "8"], "2 + 2 = 4."),
                    ("Groups with the same number are called ____ groups.", "Equal", ["Different", "Hidden", "Season"], "Equal groups have the same count."),
                ],
            },
        ],
    },
    {
        "chapter_name": "How Much Can We Spend? (Money)",
        "page": 115,
        "modules": [
            {
                "topic_name": "Coins, Notes and Amounts",
                "explanation": "Money helps us buy things and compare amounts. In this chapter, children use play money and match the same amount. A coin or note has a value. When values are put together, they make an amount we can spend or save.",
                "difficulty": "Medium",
                "facts": [
                    ("This chapter is about ____.", "Money", ["Patterns only", "Seasons only", "Rolling only"], "The chapter title asks how much can we spend."),
                    ("The PDF asks children to use play ____.", "Money", ["Water", "Leaves", "Wheels"], "The teacher note says use play money."),
                    ("A coin or note has a ____.", "Value", ["Season", "Shadow", "Bed"], "Money pieces have values."),
                    ("The activity asks children to match the same ____.", "Amount", ["Animal", "Season", "Shape only"], "The page says match the same amount."),
                    ("Money can be used to ____ things.", "Buy", ["Only sleep", "Only roll", "Only clap"], "Spending money is used for buying."),
                ],
            },
            {
                "topic_name": "Saving Money",
                "explanation": "Saving means keeping money for later. The textbook says saving money is a good habit and asks children to make a gullak with a spare box. A gullak is like a small home for saved coins and notes. Saving teaches care and planning.",
                "facts": [
                    ("The PDF says saving money is a good ____.", "Habit", ["Mistake", "Shape", "Subtraction sign"], "The page says saving money is a good habit."),
                    ("Children are asked to make a ____.", "Gullak", ["Clock", "Train", "Bottle only"], "The project asks children to make a gullak."),
                    ("A gullak can be made with a spare ____.", "Box", ["River", "Tree", "Bus"], "The PDF says use a spare box at home."),
                    ("Saving means keeping money for ____.", "Later", ["Throwing away", "Forgetting", "Only drawing"], "Saving keeps money for future use."),
                    ("Who may help children make a gullak?", "Siblings or elders", ["Only strangers", "Only shopkeepers", "Only clouds"], "The PDF says with help of siblings or elders."),
                ],
            },
        ],
    },
    {
        "chapter_name": "So Many Toys (Data Handling)",
        "page": 120,
        "modules": [
            {
                "topic_name": "Counting and Comparing Toys",
                "explanation": "Data handling starts with counting and comparing. In So Many Toys, children count dolls, cars, elephants, and teddy bears. Then they use words like more than, less than, and equal to. Data becomes easy when we count carefully and compare one group with another.",
                "difficulty": "Medium",
                "facts": [
                    ("Which chapter is about data handling?", "So Many Toys", ["Mango Treat", "Making 10", "Utsav"], "The contents page lists So Many Toys as Data Handling."),
                    ("The toy picture includes dolls and ____.", "Cars", ["Seasons", "Notes", "Bottles"], "The PDF asks children to compare dolls and cars."),
                    ("Which phrase compares bigger groups?", "More than", ["Inside", "Before", "Round"], "The activity uses more than, less than, and equal to."),
                    ("Which phrase compares smaller groups?", "Less than", ["Above", "After", "Rolling"], "Less than tells a group has fewer items."),
                    ("If two groups have the same number, they are ____.", "Equal to", ["More than", "Less than", "Under"], "Equal to means the counts are the same."),
                ],
            },
            {
                "topic_name": "Colourful Flowers Data",
                "explanation": "The colourful flowers activity asks children to count flowers by colour and tell which colour is most or least. This is data handling with pictures. When we count red, blue, orange, and purple flowers, we can answer questions using numbers instead of guessing.",
                "difficulty": "Medium",
                "facts": [
                    ("The flower activity asks children to write the number of ____.", "Flowers", ["Coins", "Buses", "Days"], "The PDF says write the number of flowers."),
                    ("Which word means greatest in number?", "Most", ["Least", "Under", "Before"], "Most means the largest count."),
                    ("Which word means smallest in number?", "Least", ["Most", "More than", "On"], "Least means the smallest count."),
                    ("The flowers are grouped by ____.", "Colour", ["Weight only", "Time only", "Money only"], "The activity names colours of flowers."),
                    ("The PDF uses true or false statements to compare flower ____.", "Numbers", ["Stories", "Seasons", "Cars only"], "The page compares counts of red, blue, orange, and purple flowers."),
                ],
            },
        ],
    },
]


def build():
    output = []
    manifest = {
        "source": "NCERT Joyful Mathematics Class 1 PDF, first edition 2023",
        "syllabus": "CBSE",
        "class": "Class 1",
        "subject": "Mathematics",
        "chapters": [],
        "module_total": 0,
        "question_total": 0,
    }

    module_counter = 1
    for chapter_index, chapter in enumerate(CHAPTERS, start=1):
        chapter_out = {"chapter_name": chapter["chapter_name"], "modules": []}
        chapter_manifest = {
            "chapter_name": chapter["chapter_name"],
            "page": chapter["page"],
            "modules": [],
        }

        for module in chapter["modules"]:
            difficulty = module.get("difficulty", "Easy")
            timer = 45 if difficulty == "Medium" else 30
            questions = [
                q(i + 1, fact[0], fact[1], fact[2], fact[3], timer)
                for i, fact in enumerate(module["facts"])
            ]
            module_id = f"cbse_c1_m{module_counter:03d}_{slug(module['topic_name'])}"
            module_counter += 1
            module_out = {
                "module_id": module_id,
                "topic_name": module["topic_name"],
                "explanation": module["explanation"],
                "difficulty": difficulty,
                "total_timer_minutes": max(4, round((len(questions) * timer) / 60)),
                "questions": questions,
            }
            chapter_out["modules"].append(module_out)
            chapter_manifest["modules"].append({
                "module_id": module_id,
                "topic_name": module["topic_name"],
                "question_count": len(questions),
                "source_basis": "PDF contents page and chapter activity text",
            })
            manifest["module_total"] += 1
            manifest["question_total"] += len(questions)

        output.append(chapter_out)
        manifest["chapters"].append(chapter_manifest)

    validate(output)
    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MANIFEST}")
    print(f"Chapters: {len(output)}; Modules: {manifest['module_total']}; Questions: {manifest['question_total']}")


def validate(output):
    assert len(output) == 13
    seen = set()
    for chapter in output:
        assert chapter["chapter_name"]
        assert chapter["modules"]
        for module in chapter["modules"]:
            assert module["module_id"] not in seen
            seen.add(module["module_id"])
            assert module["difficulty"] in {"Easy", "Medium", "Hard"}
            assert len(module["explanation"].split()) <= 150
            assert 5 <= len(module["questions"]) <= 15
            for question in module["questions"]:
                assert len(question["options"]) == 4
                assert question["correct_answer"] in question["options"]
                assert question["timer_per_question_seconds"] in {30, 45, 60}


if __name__ == "__main__":
    build()
