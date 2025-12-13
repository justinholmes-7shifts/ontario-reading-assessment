"""
Reading Assessment Module
Aligned with Ontario Language Curriculum Grade 7-8

Includes passages thematically connected to notable Canadian and world literature:
- Indigenous experiences and healing (Richard Wagamese themes)
- Dystopian societies and individual freedom (Atwood, Lowry, Orwell themes)
- Power of stories and words (Markus Zusak themes)
- Education activism (Malala Yousafzai themes)
"""

from app.curriculum import READING_EXPECTATIONS, ACHIEVEMENT_LEVELS


class ReadingAssessment:
    """Handles reading comprehension assessments."""

    def __init__(self):
        self.passages = self._load_passages()

    def _load_passages(self):
        """Load reading passages with questions."""
        return {
            # Original passages
            "fiction_1": {
                "id": "fiction_1",
                "title": "The Last Light",
                "grade": "7-8",
                "type": "Fiction - Short Story",
                "themes": ["Technology vs. humanity", "Experience and wisdom"],
                "text": """
The old lighthouse keeper climbed the spiral stairs one last time, his weathered hands
gripping the iron railing. For forty-seven years, he had made this journey twice daily,
ensuring the beacon guided ships safely through the treacherous waters of Georgian Bay.

Tonight was different. The automation system would take over at midnight, rendering
his position obsolete. Progress, they called it. Efficiency. But Marcus knew what would
be lost—the human element, the watchful eye that could spot a struggling vessel before
any sensor could.

He reached the lamp room and gazed out at the darkening horizon. A storm was brewing
in the west, purple clouds gathering like an approaching army. His practiced eye noted
the barometric pressure, the wind direction, the unusual chop of the waves.

Below, the new control panel blinked with green lights, assuring everyone that all was
well. But Marcus had learned to trust his instincts over machinery. He picked up his
binoculars and scanned the water.

There—barely visible against the grey sky—a small sailboat, its mast tilting at a
dangerous angle. The automated system hadn't detected it; the vessel was too small,
too insignificant for its sensors.

Marcus reached for the radio and made the call that would save three lives that night.
The rescue helicopter arrived twenty minutes before the sailboat would have capsized.

As midnight approached, Marcus descended the stairs slowly. The automation system
hummed to life behind him, efficient and tireless. But for one more night, the human
lighthouse keeper had proven irreplaceable.
                """,
                "questions": [
                    {
                        "id": "q1",
                        "type": "comprehension",
                        "skill": "Main idea and theme",
                        "question": "What is the central theme of this passage?",
                        "options": [
                            "Technology is always superior to human abilities",
                            "The importance of experience and human judgment",
                            "Lighthouses are no longer needed in modern times",
                            "Older workers should resist retirement"
                        ],
                        "correct": 1,
                        "explanation": "The story emphasizes how Marcus's human experience and instincts detected something the automated system missed, highlighting the value of human judgment."
                    },
                    {
                        "id": "q2",
                        "type": "inference",
                        "skill": "Making inferences",
                        "question": "What can you infer about Marcus's feelings toward the automation system?",
                        "options": [
                            "He is excited about the new technology",
                            "He feels the system is completely unreliable",
                            "He has mixed feelings - accepting change but aware of its limitations",
                            "He plans to sabotage the system"
                        ],
                        "correct": 2,
                        "explanation": "Marcus doesn't fight the change but demonstrates through his actions that he sees limitations in relying solely on automation."
                    },
                    {
                        "id": "q3",
                        "type": "vocabulary",
                        "skill": "Context clues",
                        "question": "In the passage, what does 'treacherous' most likely mean?",
                        "options": [
                            "Deep",
                            "Dangerous",
                            "Cold",
                            "Beautiful"
                        ],
                        "correct": 1,
                        "explanation": "The context suggests the waters are dangerous, requiring a lighthouse to guide ships safely."
                    },
                    {
                        "id": "q4",
                        "type": "analysis",
                        "skill": "Author's craft",
                        "question": "Why does the author describe the storm clouds as 'gathering like an approaching army'?",
                        "options": [
                            "To show that a war is about to begin",
                            "To create a sense of danger and tension",
                            "To explain military history",
                            "To describe the colour of the clouds"
                        ],
                        "correct": 1,
                        "explanation": "This simile creates tension and foreshadows the danger that Marcus will need to address."
                    },
                    {
                        "id": "q5",
                        "type": "critical_thinking",
                        "skill": "Evaluating evidence",
                        "question": "Which detail from the text best supports the idea that human skills remain valuable in an automated world?",
                        "options": [
                            "Marcus had worked for forty-seven years",
                            "The automation system blinked with green lights",
                            "The automated system hadn't detected the small sailboat",
                            "The lighthouse is located on Georgian Bay"
                        ],
                        "correct": 2,
                        "explanation": "This detail directly shows a limitation of automation that human observation overcame."
                    }
                ],
                "curriculum_alignment": ["comprehension", "critical_literacy", "vocabulary"]
            },

            # NEW: Indigenous Identity and Healing - themed like "Indian Horse"
            "indigenous_1": {
                "id": "indigenous_1",
                "title": "Finding Home on the Ice",
                "grade": "7-8",
                "type": "Fiction - Short Story",
                "themes": ["Indigenous identity", "Healing", "Cultural reclamation", "Residential schools"],
                "related_texts": ["Indian Horse by Richard Wagamese"],
                "text": """
Thomas hadn't spoken his grandfather's language in years. At the residential school,
they had punished him for it—made him feel shame for the words that had once felt
like home in his mouth. Now, at seventeen, those words felt like strangers.

But here, on the frozen lake behind his grandmother's cabin in Northern Ontario,
something was stirring. His grandmother had brought him here after he'd been expelled
from his third school in the city. "The land remembers you," she'd said, "even when
you've forgotten yourself."

She handed him a hockey stick—not a new composite one, but an old wooden stick,
worn smooth by generations of hands. "Your great-grandfather carved this," she said.
"Before the schools. Before they tried to make us forget."

Thomas took the stick. It felt solid, real, connected to something deeper than
anything he'd felt in years. He skated out onto the ice, the sound of his blades
cutting through the silence.

At first, he just moved—no drills, no plays, no coaches screaming from the bench.
Just movement. The ice held him up. The wind carried the smell of pine and wood
smoke. And somewhere in his chest, something frozen began to thaw.

His grandmother watched from the shore, singing softly in their language—the
morning song her own mother had taught her. Thomas found himself skating to its
rhythm, his movements flowing like the words he couldn't yet speak but somehow
still remembered.

He wasn't playing hockey anymore. He was dancing. He was praying. He was finding
his way back to himself through the ice, through the stick in his hands, through
the voice of his grandmother carrying across the frozen lake.

When he finally stopped, breathing hard, tears freezing on his cheeks, his
grandmother was there with a blanket and hot tea. She didn't ask what he was
feeling. She didn't need to.

"The ice doesn't judge," she said simply. "It just holds you up while you
remember who you are."

Over the following weeks, Thomas began to learn the words again—slowly, stumbling
at first, then with growing confidence. Each word was a small act of reclamation.
Each morning on the ice was a step toward healing.

He wasn't the same boy who had arrived, angry and lost. He was becoming someone
new—someone who could hold both the pain of what had been taken and the hope of
what could be rebuilt. Someone who understood that healing isn't about forgetting
the wounds, but about finding the strength to carry them forward.
                """,
                "questions": [
                    {
                        "id": "q1",
                        "type": "comprehension",
                        "skill": "Central message",
                        "question": "What is the main message of this story?",
                        "options": [
                            "Hockey is an important Canadian sport",
                            "Healing from cultural trauma comes through reconnecting with identity and heritage",
                            "Grandparents always know best",
                            "Living in the city is harmful for Indigenous youth"
                        ],
                        "correct": 1,
                        "explanation": "The story shows Thomas healing by reconnecting with his language, land, and cultural practices after the trauma of residential school."
                    },
                    {
                        "id": "q2",
                        "type": "inference",
                        "skill": "Making inferences",
                        "question": "Why does the grandmother give Thomas the old wooden hockey stick instead of a new one?",
                        "options": [
                            "She couldn't afford a new stick",
                            "The connection to ancestors and cultural continuity is more important than modern equipment",
                            "New sticks are harder to use",
                            "She doesn't understand modern hockey"
                        ],
                        "correct": 1,
                        "explanation": "The stick represents generational connection and cultural heritage—it links Thomas to his great-grandfather and traditions that existed 'before the schools.'"
                    },
                    {
                        "id": "q3",
                        "type": "analysis",
                        "skill": "Symbolic meaning",
                        "question": "What does the frozen lake symbolize in this story?",
                        "options": [
                            "The danger of Canadian winters",
                            "A place of healing that holds Thomas up while he recovers his identity",
                            "The difficulty of life in Northern Ontario",
                            "Thomas's cold emotions"
                        ],
                        "correct": 1,
                        "explanation": "The grandmother explicitly states 'The ice doesn't judge. It just holds you up while you remember who you are.' The lake represents a supportive space for healing."
                    },
                    {
                        "id": "q4",
                        "type": "critical_thinking",
                        "skill": "Understanding historical context",
                        "question": "The story references residential schools. Based on context clues, what can you infer about their impact?",
                        "options": [
                            "They provided good education for Indigenous children",
                            "They separated children from their culture, language, and created lasting trauma",
                            "They taught Indigenous children to play hockey",
                            "They were located in Northern Ontario"
                        ],
                        "correct": 1,
                        "explanation": "The text shows Thomas was 'punished' for speaking his language and 'made to feel shame,' indicating cultural suppression and trauma."
                    },
                    {
                        "id": "q5",
                        "type": "analysis",
                        "skill": "Text structure and argument",
                        "question": "How does the author structure the story to support the theme of healing?",
                        "options": [
                            "Random events with no clear connection",
                            "A journey from pain and disconnection → reconnection with culture → transformation and hope",
                            "Comparison between city life and rural life",
                            "A list of hockey techniques"
                        ],
                        "correct": 1,
                        "explanation": "The story follows a clear arc: Thomas arrives angry and disconnected, reconnects through language and cultural practice, and transforms into someone who can 'carry wounds forward' with hope."
                    },
                    {
                        "id": "q6",
                        "type": "vocabulary",
                        "skill": "Context clues",
                        "question": "What does 'reclamation' mean in the context of 'Each word was a small act of reclamation'?",
                        "options": [
                            "Destruction",
                            "Taking back something that was lost or stolen",
                            "Learning something new",
                            "Forgetting the past"
                        ],
                        "correct": 1,
                        "explanation": "Reclamation means reclaiming or taking back. Thomas is reclaiming his language that was suppressed by the residential school."
                    }
                ],
                "curriculum_alignment": ["comprehension", "critical_literacy", "vocabulary", "Canadian_literature"]
            },

            # NEW: Dystopia and Conformity - themed like The Giver, Handmaid's Tale, Animal Farm
            "dystopia_1": {
                "id": "dystopia_1",
                "title": "The Colour Grey",
                "grade": "7-8",
                "type": "Fiction - Short Story",
                "themes": ["Conformity", "Individual freedom", "Dystopia", "Choice"],
                "related_texts": ["The Giver by Lois Lowry", "The Handmaid's Tale by Margaret Atwood", "Animal Farm by George Orwell"],
                "text": """
In Community 7, everything was grey. The buildings, the clothes, the sky—even
the food came in identical grey cubes, nutritionally optimized, emotionally
neutral. The Founders had designed it this way. Colour, they said, led to
preference. Preference led to inequality. Inequality led to conflict.

Maya had never questioned it. None of them did. Questions weren't forbidden
exactly—they were just... unnecessary. The Community provided everything they
needed. The Algorithm assigned their jobs, their housing, their recreation
time. It was efficient. It was fair. It was safe.

But last week, Maya had found something. Behind the recycling centre, half-buried
in composted paper, a small rectangle. She'd almost thrown it away, but something
made her pause.

It was a photograph. Old, faded, but unmistakably showing something she'd never
seen: a sky that wasn't grey but a brilliant, impossible blue. Trees that were
green. And people—wearing clothes of red, yellow, purple—standing together,
their faces doing something Maya didn't have a word for.

Later, she learned the word from the archives: smiling. They were smiling.

Now the photograph was hidden under her mattress, and Maya couldn't stop thinking
about it. She looked at the grey walls of her quarters differently. She noticed,
for the first time, that the birds outside her window never sang.

"The old world was chaos," her instructor had taught them. "People fought over
resources, over beliefs, over colours of skin. We have evolved beyond that.
We have chosen peace."

But had they chosen? Maya wondered. Or had someone chosen for them?

She thought about the Algorithm that had assigned her to Food Production. She
was good at it, efficient, never complained. But she had never been asked what
she wanted. None of them had.

That night, Maya did something dangerous. She took out the photograph and really
looked at it. At the blue sky. At the smiling faces. At a world that had colour
and chaos and choice.

It wasn't perfect. The archives showed her that clearly—the wars, the suffering,
the inequality. But it was real. People had laughed and cried, fought and
forgiven, made terrible mistakes and beautiful art.

In Community 7, no one made mistakes. No one made anything at all.

Maya carefully tucked the photograph away. She didn't know what she would do
with this new feeling—this uncomfortable awareness that safety and living
weren't the same thing. But for the first time in her life, she understood
that not knowing was sometimes more honest than having all the answers given
to you.

The grey walls looked different now. They looked like a choice that someone
else had made.
                """,
                "questions": [
                    {
                        "id": "q1",
                        "type": "comprehension",
                        "skill": "Central theme",
                        "question": "What is the central theme of this story?",
                        "options": [
                            "Grey is a calming colour",
                            "The cost of safety and conformity is the loss of individual choice and genuine human experience",
                            "Technology always makes life better",
                            "Photographs are important historical artifacts"
                        ],
                        "correct": 1,
                        "explanation": "The story contrasts the 'safe' but grey, choiceless Community with the colourful, chaotic but real old world, questioning what is lost when freedom is traded for security."
                    },
                    {
                        "id": "q2",
                        "type": "analysis",
                        "skill": "Identifying author's argument",
                        "question": "What argument is the author making about perfect societies?",
                        "options": [
                            "They are achievable and desirable",
                            "They require eliminating what makes us human—choice, emotion, and individuality",
                            "They only work with the right technology",
                            "They existed in the past"
                        ],
                        "correct": 1,
                        "explanation": "The story suggests that Community 7's 'perfection' came at the cost of human elements: colour, music (birds don't sing), smiling, and most importantly, choice."
                    },
                    {
                        "id": "q3",
                        "type": "critical_thinking",
                        "skill": "Evaluating reasoning",
                        "question": "The Founders argue: 'Colour led to preference. Preference led to inequality. Inequality led to conflict.' What is the flaw in this reasoning?",
                        "options": [
                            "Colour doesn't actually lead to preference",
                            "It assumes eliminating choice is better than teaching people to handle differences",
                            "Inequality isn't always bad",
                            "Conflict is actually good"
                        ],
                        "correct": 1,
                        "explanation": "The argument's flaw is that it addresses human conflict by eliminating human experience rather than developing better ways to handle differences."
                    },
                    {
                        "id": "q4",
                        "type": "inference",
                        "skill": "Drawing conclusions",
                        "question": "What does Maya realize when she thinks 'safety and living weren't the same thing'?",
                        "options": [
                            "Community 7 is dangerous",
                            "Being protected from all risk means missing the experiences that make life meaningful",
                            "She needs to find a safer place",
                            "Living in the old world was safer"
                        ],
                        "correct": 1,
                        "explanation": "Maya understands that the Community's total safety has eliminated not just danger but also joy, choice, and authentic human experience."
                    },
                    {
                        "id": "q5",
                        "type": "analysis",
                        "skill": "Text structure",
                        "question": "How does the author organize the argument against conformity in this story?",
                        "options": [
                            "By listing facts about dystopian societies",
                            "By showing Maya's journey from acceptance → discovery → questioning → new awareness",
                            "By comparing different communities",
                            "By presenting a debate between characters"
                        ],
                        "correct": 1,
                        "explanation": "The story structures its argument through Maya's transformation: she starts accepting the system, discovers evidence of alternatives, questions what she's been taught, and reaches new understanding."
                    },
                    {
                        "id": "q6",
                        "type": "connection",
                        "skill": "Text-to-text connections",
                        "question": "This story shares themes with famous novels like 'The Giver' and 'Animal Farm.' What theme do these stories have in common?",
                        "options": [
                            "The importance of farming",
                            "Warnings about societies that sacrifice individual freedom for collective control",
                            "The benefits of technology",
                            "How to build better communities"
                        ],
                        "correct": 1,
                        "explanation": "These dystopian works all warn readers about the dangers of trading freedom for security or equality enforced through control rather than choice."
                    }
                ],
                "curriculum_alignment": ["comprehension", "critical_literacy", "vocabulary", "Canadian_literature"]
            },

            # NEW: Power of Words - themed like The Book Thief
            "words_1": {
                "id": "words_1",
                "title": "The Library in the Basement",
                "grade": "7-8",
                "type": "Fiction - Short Story",
                "themes": ["Power of words", "Resistance through stories", "Hope in dark times"],
                "related_texts": ["The Book Thief by Markus Zusak"],
                "text": """
During the war, words became weapons. The government controlled what could be
printed, spoken, taught. History was rewritten. Poems disappeared. Stories that
didn't serve the state were burned.

But in the basement of 47 Maple Street, twelve-year-old Anna had a secret.

It had started with a single book—a collection of fairy tales her grandmother
had hidden in the walls before she was taken away. Anna found it by accident,
knocked loose when a bomb shook their neighbourhood. The cover was singed, some
pages missing, but the words inside were magic.

She read about children who outsmarted giants. About girls who were brave when
everyone told them to be quiet. About a world where good could triumph over evil,
even when evil seemed impossibly strong.

"You shouldn't have that," her mother had said when she found Anna reading by
candlelight. But instead of taking it away, her mother had brought her another
book—a slim volume of poems she'd kept hidden in her mattress for years.

"Words are the most powerful thing we have," her mother whispered. "They can't
bomb our thoughts. They can't burn what we remember."

Soon, others came. Mrs. Chen from the apartment above, carrying a philosophy
book wrapped in a bread cloth. Mr. Torres from the grocery, with a banned novel
tucked inside a bag of flour. The Okonkwo twins, who had memorized poems their
father used to read, each twin knowing alternate verses.

Every Tuesday night, they gathered in Anna's basement. Someone would read. Others
would listen. Sometimes they argued about what a poem meant. Sometimes they cried.
Sometimes they laughed at jokes in stories written a hundred years ago.

They were committing a crime, Anna knew. The punishment for possessing banned
books was severe. For gathering to discuss them? Worse.

But in that basement, surrounded by words that had survived fires and wars and
time itself, Anna felt something stronger than fear.

"Why do they hate books so much?" she asked her mother one night.

Her mother thought for a long moment. "Because stories remind us who we were
before they told us who to be. Because poems prove that other people have felt
what we feel. Because every book is evidence that the world could be different
than it is."

Anna looked at the small collection on their hidden shelf. A fairy tale book.
Some poems. A philosophy text. A novel. Verses living in the memory of twins.

It wasn't much. A library of perhaps twenty books, half of them incomplete.

But in a world trying to make everyone think the same way, believe the same things,
forget the same history—these words were a rebellion. These pages were proof that
different thoughts were possible. This basement was the most dangerous place in
the city.

Anna picked up the fairy tale book and began to read aloud. Around her, the
small group leaned in, hungry for words the government had tried to kill.

The stories survived. And as long as they survived, so did hope.
                """,
                "questions": [
                    {
                        "id": "q1",
                        "type": "comprehension",
                        "skill": "Central message",
                        "question": "What is the central message of this story?",
                        "options": [
                            "Libraries are important buildings",
                            "Books and stories preserve freedom, identity, and hope even in oppressive times",
                            "Children should read more fairy tales",
                            "War destroys buildings"
                        ],
                        "correct": 1,
                        "explanation": "The story shows how books represent freedom of thought and preserve hope and identity when governments try to control thinking."
                    },
                    {
                        "id": "q2",
                        "type": "analysis",
                        "skill": "Understanding author's argument",
                        "question": "According to Anna's mother, why does the government hate books?",
                        "options": [
                            "Books are expensive to produce",
                            "Books remind people of alternatives to the current reality and prove different thoughts are possible",
                            "Too many people were reading instead of working",
                            "Books take up too much space"
                        ],
                        "correct": 1,
                        "explanation": "The mother explains that stories 'remind us who we were before they told us who to be' and 'prove the world could be different'—books threaten control by preserving alternative thinking."
                    },
                    {
                        "id": "q3",
                        "type": "inference",
                        "skill": "Making inferences",
                        "question": "Why do the Okonkwo twins each memorize alternate verses of their father's poems?",
                        "options": [
                            "They couldn't agree on who would memorize which poem",
                            "To preserve the poems even if one twin was caught or lost—the knowledge is shared for survival",
                            "They have bad memories individually",
                            "Their father asked them to"
                        ],
                        "correct": 1,
                        "explanation": "By splitting the verses between them, the poems survive even if one twin is lost. This shows how precious and endangered the words are."
                    },
                    {
                        "id": "q4",
                        "type": "critical_thinking",
                        "skill": "Evaluating theme",
                        "question": "The story calls the basement 'the most dangerous place in the city.' Why is gathering to read books considered dangerous by the government?",
                        "options": [
                            "The basement might collapse",
                            "Shared reading creates community and independent thinking that threatens authoritarian control",
                            "Books can catch fire easily",
                            "Too many people might want to come"
                        ],
                        "correct": 1,
                        "explanation": "The danger isn't physical—it's that reading together builds community and preserves ways of thinking that challenge the government's control over thought and history."
                    },
                    {
                        "id": "q5",
                        "type": "analysis",
                        "skill": "Text structure",
                        "question": "How does the author build the argument that words have power?",
                        "options": [
                            "By stating facts about literacy rates",
                            "By showing multiple examples: fairy tales inspire courage, poems connect emotions across time, the community risks everything to preserve them",
                            "By comparing books to weapons directly",
                            "By describing the government's laws"
                        ],
                        "correct": 1,
                        "explanation": "The author builds evidence through specific examples: fairy tales teaching courage, poems connecting feelings, different community members contributing, and everyone risking severe punishment to preserve words."
                    },
                    {
                        "id": "q6",
                        "type": "vocabulary",
                        "skill": "Figurative language",
                        "question": "When Anna's mother says 'They can't bomb our thoughts. They can't burn what we remember,' she means:",
                        "options": [
                            "Thoughts are literally fireproof",
                            "Physical destruction cannot destroy ideas and memories that live in people's minds",
                            "The government's bombs don't work well",
                            "Remembering things is difficult"
                        ],
                        "correct": 1,
                        "explanation": "This is a metaphor explaining that while physical books can be destroyed, the ideas and stories they contain survive through memory and cannot be physically attacked."
                    }
                ],
                "curriculum_alignment": ["comprehension", "critical_literacy", "vocabulary", "Canadian_literature"]
            },

            # NEW: Education Activism - themed like I Am Malala
            "activism_1": {
                "id": "activism_1",
                "title": "The Voice That Wouldn't Be Silenced",
                "grade": "7-8",
                "type": "Non-Fiction Style - Biographical Essay",
                "themes": ["Education activism", "Courage", "Youth voice", "Human rights"],
                "related_texts": ["I Am Malala by Malala Yousafzai"],
                "text": """
Amara was fourteen when they closed her school.

It happened overnight. One day, she walked through the blue gates, sat at her
desk, and learned about the water cycle. The next day, the gates were chained
shut. A sign declared that education for girls was "no longer permitted in
this district."

For many girls, that was the end. They stayed home, helped with housework,
waited to be married off. Their dreams of becoming doctors, teachers, engineers
folded up and tucked away like outgrown clothes.

But Amara couldn't fold up her dreams. They were too big, too alive, too necessary.

She started small. A notebook, shared between her and three friends. They met
in her family's storage shed, teaching each other what they remembered from
school. Amara taught math. Fatima taught reading. Zainab recited history from
memory. Sara drew diagrams of the human body she'd traced from her brother's
biology textbook.

Word spread. By the third week, twelve girls were crowding into the shed.
By the fifth week, twenty-three.

"You're being reckless," her father warned. "If they find out—"

"If they find out, they'll know that closing the school didn't work," Amara
answered. "They'll know that you can't stop people from learning by locking
a door."

She knew the risks. She'd heard stories of girls punished for reading, families
threatened for teaching daughters. Fear lived in her chest constantly, a cold
weight that never fully went away.

But there was something stronger than fear: the conviction that she mattered.
That her mind mattered. That the minds of every girl in that cramped shed
mattered just as much as any boy's.

When a reporter from the capital heard about the secret school, she asked
Amara why she took such risks.

Amara thought carefully before answering. "They have guns and laws and power.
We have pencils and notebooks and each other. It seems unequal. But here's
what they don't understand: you can threaten someone into silence once, twice,
a hundred times. But you can't threaten an idea. You can't arrest curiosity.
You can't make a person un-know something she's already learned."

She paused, then added: "Every girl I teach will teach others. Every book we
read together multiplies. They can close one school, but they can't close
every mind. They've already lost. They just don't know it yet."

The article was published internationally. It brought attention, support, and
new dangers. Amara's family had to relocate twice.

But the shed schools had already spread to three other districts. The idea had
taken root.

Today, Amara studies at a university—the first woman from her village to do so.
She's studying education, planning to return home and fight for every girl who
was told her mind didn't matter.

"They told us to be quiet," she says now. "But silence only works if everyone
agrees to it. And we didn't."
                """,
                "questions": [
                    {
                        "id": "q1",
                        "type": "comprehension",
                        "skill": "Central argument",
                        "question": "What is Amara's main argument for why continuing to learn is important?",
                        "options": [
                            "Education helps you get a good job",
                            "Ideas and knowledge multiply and can't be stopped by force—they're more powerful than oppression",
                            "Schools are fun places to be",
                            "Her parents wanted her to continue"
                        ],
                        "correct": 1,
                        "explanation": "Amara argues that while oppressors have 'guns and laws,' education creates ideas that spread and multiply. 'You can't threaten an idea. You can't arrest curiosity.'"
                    },
                    {
                        "id": "q2",
                        "type": "analysis",
                        "skill": "Identifying supporting evidence",
                        "question": "Which detail from the text best supports the claim that education activism can succeed despite opposition?",
                        "options": [
                            "Amara's father was worried about her safety",
                            "The shed schools spread to three other districts, showing the idea multiplied as Amara predicted",
                            "The school gates were chained shut",
                            "Amara taught math"
                        ],
                        "correct": 1,
                        "explanation": "The spread to three districts directly proves Amara's argument that 'every girl I teach will teach others' and ideas multiply faster than they can be suppressed."
                    },
                    {
                        "id": "q3",
                        "type": "inference",
                        "skill": "Drawing conclusions",
                        "question": "When Amara says 'They've already lost. They just don't know it yet,' what does she mean?",
                        "options": [
                            "The authorities have run out of money",
                            "By trying to stop education, they've inspired a movement that's now too widespread to control",
                            "The girls have defeated them in a competition",
                            "The authorities will soon change their minds"
                        ],
                        "correct": 1,
                        "explanation": "The attempt to suppress education backfired—it created a decentralized movement of secret schools that spread further than formal education might have."
                    },
                    {
                        "id": "q4",
                        "type": "critical_thinking",
                        "skill": "Evaluating structure of argument",
                        "question": "Amara's argument to the reporter follows a clear structure. What is it?",
                        "options": [
                            "She tells a story, then asks questions",
                            "She acknowledges the opposition's power → states her counterclaim (ideas are stronger) → provides reasoning (ideas multiply, can't be un-learned)",
                            "She lists facts about education",
                            "She compares different schools"
                        ],
                        "correct": 1,
                        "explanation": "Amara builds a structured argument: she acknowledges 'they have guns and laws,' then counterclaims with 'you can't threaten an idea,' then supports with specific reasons why education spreads."
                    },
                    {
                        "id": "q5",
                        "type": "connection",
                        "skill": "Real-world connections",
                        "question": "This story shares themes with Malala Yousafzai's memoir 'I Am Malala.' What lesson do both stories teach?",
                        "options": [
                            "Violence always defeats peaceful protest",
                            "Young people should stay quiet about political issues",
                            "Individual courage combined with education can challenge oppression and inspire movements",
                            "Schools are the only place to learn"
                        ],
                        "correct": 2,
                        "explanation": "Both stories show young women refusing to be silenced, using education as resistance, and inspiring others through their courage."
                    },
                    {
                        "id": "q6",
                        "type": "vocabulary",
                        "skill": "Context clues",
                        "question": "In the context of this passage, what does 'conviction' mean in 'the conviction that she mattered'?",
                        "options": [
                            "A criminal sentence",
                            "A firm belief held with certainty",
                            "A type of notebook",
                            "Permission from authorities"
                        ],
                        "correct": 1,
                        "explanation": "Here, conviction means a strong, firmly held belief—Amara's certainty that her mind and education have value despite what authorities say."
                    }
                ],
                "curriculum_alignment": ["comprehension", "critical_literacy", "vocabulary", "Canadian_literature"]
            },

            # NEW: Hope in Hiding - themed like The Diary of Anne Frank
            "diary_1": {
                "id": "diary_1",
                "title": "Pages in the Dark",
                "grade": "7-8",
                "type": "Fiction - Diary Entries",
                "themes": ["Hope during persecution", "Personal narrative", "Humanity in crisis", "Youth perspective"],
                "related_texts": ["The Diary of Anne Frank"],
                "text": '''
March 12th

It's been forty-seven days since we came to the hidden room above Mr. Okonkwo's
shop. Forty-seven days of whispered conversations, of walking in socks so the
floor doesn't creak, of watching the same four walls close in a little more
each day.

Mama says I shouldn't write. "What if they find it?" she asks. But I can't stop.
These pages are the only place I can be loud. The only place I can be fully myself.

Today I watched a bird through the small window—the one we keep covered except
for a tiny gap. It was building a nest, carrying twigs back and forth, completely
free. I wonder if it knows how lucky it is.

---

March 28th

Mr. Okonkwo brought us books today, hidden under vegetables in a basket. Real books!
I've already read the first one twice. It's about a girl who discovers she has
magic powers. Silly, I know—there's no magic that could help us now. But for a few
hours, I wasn't in a hidden room. I was somewhere else entirely.

That's the magic of books, I suppose. They let you escape without going anywhere.

Papa was angry when he saw me reading. "You should be studying practical things,"
he said. "Mathematics. Languages."

But I think stories are practical. They remind me that other people have survived
hard times. They remind me that this isn't the whole world, even when it feels
like it.

---

April 15th

The soldiers searched the shop today. We could hear them through the floor—boots
on wood, harsh voices, things being thrown around. Mama held her hand over my
little brother's mouth. We didn't breathe for what felt like hours.

They didn't find the hidden door.

After they left, I couldn't stop shaking. But then I thought about all the people
who must be hiding just like us. In attics and cellars and secret rooms across
the city. We're all terrified. But we're all still here. There's something
powerful in that—in existing when they want you to disappear.

---

April 23rd

I've decided something important: when this is over—and it will be over, it has
to be—I'm going to become a writer.

Not because I think my stories will be great literature. But because someone
needs to remember this. Someone needs to write down what it feels like to be
thirteen and hidden, to watch your parents try to be brave when they're
terrified, to measure your whole world by the dust motes in a single beam of
light.

If I don't survive, maybe these pages will. And then people will know we were
here. We existed. We hoped and feared and laughed quietly at bad jokes and
cried when we thought no one was watching.

We were human. We are human. No one can take that from us.

---

May 3rd

Sometimes I imagine the people who will read this someday. Will they be sitting
in bright rooms, safe and free? Will they wonder what it felt like? Will they
believe that this really happened?

I want to tell them: believe it. Remember it. And never let it happen again.

That's why I keep writing, even when Mama says it's dangerous. Because forgetting
is dangerous too. Silence is how they win.

As long as I have a pencil and paper, I have a voice. And as long as I have a
voice, I'm not powerless.

Tomorrow might be better. Tomorrow might be worse. But tonight, I'm still here,
still writing, still hoping. And that's enough.
                ''',
                "questions": [
                    {
                        "id": "q1",
                        "type": "comprehension",
                        "skill": "Central theme",
                        "question": "What is the central theme of these diary entries?",
                        "options": [
                            "The importance of mathematics education",
                            "Maintaining hope, humanity, and voice during persecution",
                            "The difficulties of living in small spaces",
                            "How to survive without food"
                        ],
                        "correct": 1,
                        "explanation": "The diary shows how writing, reading, and hope help the narrator maintain her humanity and sense of self during hiding and persecution."
                    },
                    {
                        "id": "q2",
                        "type": "analysis",
                        "skill": "Understanding author's purpose",
                        "question": "Why does the narrator continue to write even though her mother says it's dangerous?",
                        "options": [
                            "She wants to become famous",
                            "She believes documenting their experience matters and writing gives her a voice when she has no other power",
                            "She has nothing else to do",
                            "Her teacher assigned it for homework"
                        ],
                        "correct": 1,
                        "explanation": "The narrator writes because 'forgetting is dangerous too' and 'as long as I have a voice, I'm not powerless.' Writing is resistance and preservation."
                    },
                    {
                        "id": "q3",
                        "type": "inference",
                        "skill": "Making inferences",
                        "question": "Based on the diary entries, what can you infer about why the family is hiding?",
                        "options": [
                            "They are playing hide and seek",
                            "They are being persecuted by authorities because of who they are",
                            "They owe money to someone",
                            "Their house is being renovated"
                        ],
                        "correct": 1,
                        "explanation": "Details like soldiers searching, existing 'when they want you to disappear,' and 'never let it happen again' indicate systematic persecution based on identity."
                    },
                    {
                        "id": "q4",
                        "type": "analysis",
                        "skill": "Symbolic meaning",
                        "question": "What does the free bird building a nest symbolize for the narrator?",
                        "options": [
                            "The changing seasons",
                            "Freedom and normal life that she cannot have",
                            "The need for better housing",
                            "Her interest in biology"
                        ],
                        "correct": 1,
                        "explanation": "The bird represents freedom of movement and the ordinary life the narrator has lost—she watches it and thinks 'I wonder if it knows how lucky it is.'"
                    },
                    {
                        "id": "q5",
                        "type": "critical_thinking",
                        "skill": "Evaluating argument",
                        "question": "The narrator says 'There's something powerful in that—in existing when they want you to disappear.' What argument is she making?",
                        "options": [
                            "Hiding is fun",
                            "Simply surviving and remaining human is itself an act of resistance against persecution",
                            "They should stop hiding",
                            "The soldiers will eventually give up"
                        ],
                        "correct": 1,
                        "explanation": "The narrator argues that their continued existence, hope, and humanity—despite attempts to destroy them—is a form of defiance and resistance."
                    },
                    {
                        "id": "q6",
                        "type": "connection",
                        "skill": "Text-to-text connections",
                        "question": "This passage shares themes with 'The Diary of Anne Frank.' What common message do both texts convey?",
                        "options": [
                            "Young people should not write during wars",
                            "Personal narratives preserve humanity and serve as witness to history, even during the worst circumstances",
                            "Hiding is always the best strategy",
                            "Books are better than movies"
                        ],
                        "correct": 1,
                        "explanation": "Both texts show how personal writing during persecution preserves the humanity of victims and serves as historical witness, ensuring they are remembered as real people."
                    }
                ],
                "curriculum_alignment": ["comprehension", "critical_literacy", "vocabulary", "Canadian_literature"]
            },

            # NEW: Speaking Up - themed like The Hate U Give
            "justice_1": {
                "id": "justice_1",
                "title": "Finding My Voice",
                "grade": "7-8",
                "type": "Fiction - First Person Narrative",
                "themes": ["Racial justice", "Finding voice", "Identity", "Activism", "Code-switching"],
                "related_texts": ["The Hate U Give by Angie Thomas"],
                "text": '''
I live in two worlds.

In my neighbourhood—Garden Heights—I'm just Tia. I talk the way my grandmother
taught me, wear my hair in the braids my cousin does every Sunday, know everyone
by name from the corner store to the community centre.

At Riverside Academy, I'm "Tiana." I straighten my hair, modulate my voice, work
twice as hard to prove I belong. The scholarship kid. The one who doesn't quite fit.

I've gotten good at switching between them. So good that sometimes I forget which
one is really me.

But last Tuesday, everything changed.

My cousin Marcus was walking home from work. His crime? Being a Black man in the
wrong neighbourhood at the wrong time. The police said he "matched a description."
They pushed him against a wall, searched him, called for backup as if he was
dangerous instead of a twenty-year-old accounting student who volunteers at the
church.

Someone filmed it. The video went viral. Suddenly my two worlds collided.

At Riverside, my classmates watched the video on their phones between classes.
"This is so sad," one girl said. "Why didn't he just comply?"

I wanted to scream. I wanted to explain that compliance doesn't always save you.
That Marcus did everything right and it still wasn't enough. That the fear I saw
in his eyes on that video is a fear I've known my whole life—a fear these kids
will never have to understand.

But I stayed silent. Smiled. Nodded. Went back to being "Tiana."

That night, I couldn't sleep. I kept thinking about Marcus. About my little brother
who's only twelve. About all the times I've code-switched my way through Riverside,
hiding parts of myself to make other people comfortable.

What was the point of that education if I was too afraid to use my voice?

The next morning, I stood up in current events class. My heart was pounding so hard
I could hear it.

"The video everyone's been watching?" I said. "That's my cousin. His name is Marcus.
He's not a 'suspect' or a 'viral video.' He's a person. And what happened to him
happens to people in my community every day. If we're going to talk about it, we
need to actually listen to the people it affects."

The room went silent. My hands were shaking. I'd just blown up every careful wall
I'd built between my two lives.

But then something unexpected happened. My friend Jordan stood up. "Tia's right,"
she said. "We've been talking about this like it's entertainment, not someone's
actual life."

One by one, other kids started asking real questions. Not to challenge me—to learn.
For the first time at Riverside, I felt like they were seeing the real me.

I'm still figuring out how to exist in both worlds. But I've learned something:
when you only show people part of yourself, you're giving them permission to
ignore the rest. Speaking up is terrifying. But silence is a kind of dying too.

Marcus is okay. The charges were dropped. But nothing really changed—not officially.

Except me. I changed.

Now when I speak, I don't code-switch. I don't hide. My voice might shake, but at
least it's mine.
                ''',
                "questions": [
                    {
                        "id": "q1",
                        "type": "comprehension",
                        "skill": "Central theme",
                        "question": "What is the central theme of this narrative?",
                        "options": [
                            "How to get a scholarship to a good school",
                            "Finding the courage to speak authentically about injustice, even when it's uncomfortable",
                            "The importance of current events class",
                            "Why video cameras are important"
                        ],
                        "correct": 1,
                        "explanation": "The story follows Tia's journey from hiding her authentic self and staying silent to finding her voice and speaking up about injustice despite her fear."
                    },
                    {
                        "id": "q2",
                        "type": "vocabulary",
                        "skill": "Context clues",
                        "question": "What does 'code-switching' mean in this context?",
                        "options": [
                            "Changing computer passwords",
                            "Changing how you speak and present yourself to fit into different environments",
                            "Switching classes at school",
                            "Learning a new language"
                        ],
                        "correct": 1,
                        "explanation": "Tia describes changing her voice, hair, and behavior between Garden Heights (where she's 'Tia') and Riverside Academy (where she's 'Tiana') to fit in."
                    },
                    {
                        "id": "q3",
                        "type": "inference",
                        "skill": "Drawing conclusions",
                        "question": "Why does Tia initially stay silent when her classmates discuss the video?",
                        "options": [
                            "She didn't see the video",
                            "She agrees with what they're saying",
                            "She's protecting the identity she's built at school and fears the consequences of speaking up",
                            "She doesn't care about Marcus"
                        ],
                        "correct": 2,
                        "explanation": "Tia has carefully constructed 'Tiana' at Riverside by hiding parts of herself. Speaking up would collapse the walls between her two identities."
                    },
                    {
                        "id": "q4",
                        "type": "analysis",
                        "skill": "Understanding argument",
                        "question": "What is Tia's argument when she says 'silence is a kind of dying too'?",
                        "options": [
                            "Being quiet can make you sick",
                            "Suppressing your authentic voice and staying silent about injustice kills a part of who you are",
                            "You should always talk loudly",
                            "Death is caused by not speaking"
                        ],
                        "correct": 1,
                        "explanation": "Tia realizes that constantly hiding her true self and staying silent about things that matter is its own form of loss—she loses her authentic identity."
                    },
                    {
                        "id": "q5",
                        "type": "critical_thinking",
                        "skill": "Evaluating perspective",
                        "question": "When a classmate asks 'Why didn't he just comply?' what does this reveal about their perspective?",
                        "options": [
                            "They fully understand the situation",
                            "They don't understand that compliance doesn't guarantee safety for Black people, revealing a gap in perspective",
                            "They are giving good advice",
                            "They watched the whole video carefully"
                        ],
                        "correct": 1,
                        "explanation": "The question assumes compliance equals safety, which Tia knows isn't true for people in her community. This reveals how privilege creates blind spots in understanding."
                    },
                    {
                        "id": "q6",
                        "type": "connection",
                        "skill": "Text-to-text connections",
                        "question": "This story shares themes with 'The Hate U Give' by Angie Thomas. What message do both texts communicate about finding your voice?",
                        "options": [
                            "It's better to stay quiet about difficult topics",
                            "Only adults should speak up about injustice",
                            "Speaking up about injustice is necessary even when terrifying, and young people's voices matter",
                            "Code-switching is always wrong"
                        ],
                        "correct": 2,
                        "explanation": "Both stories show young Black protagonists who must decide whether to speak up about injustice despite fear, ultimately showing that their voices have power to create change."
                    }
                ],
                "curriculum_alignment": ["comprehension", "critical_literacy", "vocabulary", "Canadian_literature"]
            },

            # Original passages kept
            "nonfiction_1": {
                "id": "nonfiction_1",
                "title": "The Science of Sleep",
                "grade": "7-8",
                "type": "Non-Fiction - Informational",
                "themes": ["Health", "Science", "Teen development"],
                "text": """
Sleep is not simply a time when your body shuts down. While you rest, your brain
stays remarkably active, performing crucial functions that affect every aspect of
your physical and mental health.

During sleep, your brain cycles through different stages approximately every 90
minutes. The first stages involve light sleep, where you can be easily awakened.
As you progress into deeper stages, your brain waves slow dramatically, and your
body focuses on physical repair and growth.

The most fascinating stage is REM (Rapid Eye Movement) sleep, which typically
begins about 90 minutes after you fall asleep. During REM sleep, your brain
becomes almost as active as when you're awake, yet your body remains essentially
paralyzed. This is when most dreaming occurs, and researchers believe this stage
is essential for memory consolidation and emotional processing.

For teenagers, sleep is particularly critical. Adolescent brains are undergoing
significant development, and research shows that teens need 8-10 hours of sleep
per night—more than adults require. However, biological changes during puberty
shift the natural sleep-wake cycle later, making it difficult for teens to fall
asleep before 11 p.m.

This biological reality conflicts with early school start times, leading many
health organizations to advocate for later start times for middle and high schools.
Studies have shown that when schools delay their start times, students show
improved academic performance, better mental health, and reduced rates of car
accidents among teen drivers.

Insufficient sleep affects more than just tiredness. It impairs decision-making,
reduces immune function, and has been linked to increased risk of obesity and
depression. For students, sleep deprivation can significantly impact learning, as
the brain consolidates new information during sleep.

Understanding the science of sleep empowers you to make better choices about your
rest. Establishing consistent sleep schedules, limiting screen time before bed,
and creating a dark, cool sleeping environment can all improve sleep quality.
                """,
                "questions": [
                    {
                        "id": "q1",
                        "type": "comprehension",
                        "skill": "Identifying main ideas",
                        "question": "What is the main purpose of this article?",
                        "options": [
                            "To explain why schools should start later",
                            "To inform readers about the importance and science of sleep",
                            "To convince readers to sleep more than 10 hours",
                            "To describe different types of dreams"
                        ],
                        "correct": 1,
                        "explanation": "The article comprehensively covers sleep science, its stages, importance for teens, and practical advice."
                    },
                    {
                        "id": "q2",
                        "type": "comprehension",
                        "skill": "Identifying details",
                        "question": "According to the passage, how much sleep do teenagers need per night?",
                        "options": [
                            "6-8 hours",
                            "7-9 hours",
                            "8-10 hours",
                            "10-12 hours"
                        ],
                        "correct": 2,
                        "explanation": "The passage explicitly states that teens need 8-10 hours of sleep per night."
                    },
                    {
                        "id": "q3",
                        "type": "inference",
                        "skill": "Drawing conclusions",
                        "question": "Based on the passage, why might a teenager who regularly sleeps only 6 hours struggle in school?",
                        "options": [
                            "They won't have enough REM sleep for memory consolidation",
                            "They will sleep during class",
                            "Teachers will be upset with them",
                            "Their parents will be worried"
                        ],
                        "correct": 0,
                        "explanation": "The passage explains that the brain consolidates new information during sleep, particularly REM sleep."
                    },
                    {
                        "id": "q4",
                        "type": "text_structure",
                        "skill": "Understanding text organization",
                        "question": "How is this article primarily organized?",
                        "options": [
                            "Problem and solution",
                            "Chronological order",
                            "Compare and contrast",
                            "Topic and supporting details"
                        ],
                        "correct": 3,
                        "explanation": "The article presents the topic of sleep and supports it with scientific details, statistics, and practical advice."
                    },
                    {
                        "id": "q5",
                        "type": "critical_thinking",
                        "skill": "Evaluating evidence",
                        "question": "Which type of evidence does the author use to support the argument for later school start times?",
                        "options": [
                            "Personal stories from students",
                            "Research studies showing improved outcomes",
                            "Opinions from teachers",
                            "Historical examples from other countries"
                        ],
                        "correct": 1,
                        "explanation": "The author cites studies showing improved academic performance, mental health, and reduced accidents."
                    }
                ],
                "curriculum_alignment": ["comprehension", "critical_literacy", "vocabulary"]
            },

            "media_1": {
                "id": "media_1",
                "title": "Analyzing Social Media Influence",
                "grade": "7-8",
                "type": "Media Literacy",
                "themes": ["Media literacy", "Critical thinking", "Advertising"],
                "text": """
SPONSORED POST @HealthyLifeNow

Start your morning RIGHT with PowerBoost Energy Drink!

"I used to struggle to get through my day, but ever since I started drinking PowerBoost
every morning, I have SO much energy! It's made from all-natural ingredients and tastes
amazing. Use my code HEALTHY20 for 20% off your first order! Link in bio.

#ad #sponsored #PowerBoost #EnergyDrink #HealthyLiving #MorningRoutine #Wellness
#NaturalEnergy #FitLife"

[Image shows influencer with 2.3 million followers holding bright green drink bottle,
smiling in an expensive-looking kitchen. Professional lighting and photography visible.]

---

PRODUCT LABEL (fine print):
PowerBoost Energy Drink
Serving Size: 1 can (250mL)
Caffeine: 150mg (equivalent to 1.5 cups of coffee)
Sugar: 27g
Other ingredients: Taurine, B-vitamins, natural and artificial flavours, citric acid

Warning: Not recommended for children, pregnant women, or people sensitive to caffeine.
Consume no more than 2 cans per day.

---

CONSUMER REVIEW EXCERPT (from independent website):
"I tried PowerBoost after seeing it promoted by several influencers. While it does
provide an energy boost, the effect wears off quickly and I experienced an energy
crash a few hours later. Also, the 'all-natural' claim is misleading—it contains
artificial flavours according to the label. The price is significantly higher than
similar energy drinks." - Verified Purchaser
                """,
                "questions": [
                    {
                        "id": "q1",
                        "type": "media_literacy",
                        "skill": "Identifying persuasive techniques",
                        "question": "What persuasive technique is primarily used in the sponsored post?",
                        "options": [
                            "Appeal to authority (expert opinion)",
                            "Testimonial and personal endorsement",
                            "Statistical evidence",
                            "Fear of missing out"
                        ],
                        "correct": 1,
                        "explanation": "The influencer shares their personal experience as a form of testimonial to persuade followers."
                    },
                    {
                        "id": "q2",
                        "type": "critical_thinking",
                        "skill": "Identifying bias and perspective",
                        "question": "Why is it important that the post includes '#ad #sponsored' hashtags?",
                        "options": [
                            "It makes the post more popular",
                            "It's trendy on social media",
                            "It legally discloses that the influencer was paid to promote the product",
                            "It shows the influencer is professional"
                        ],
                        "correct": 2,
                        "explanation": "These hashtags are required disclosures indicating the influencer received compensation, which affects their objectivity."
                    },
                    {
                        "id": "q3",
                        "type": "analysis",
                        "skill": "Comparing sources",
                        "question": "What contradiction exists between the influencer's post and the product information?",
                        "options": [
                            "The price is different",
                            "The influencer claims it's 'all-natural' but the label shows artificial flavours",
                            "The caffeine content is wrong",
                            "The serving size is incorrect"
                        ],
                        "correct": 1,
                        "explanation": "The influencer claims 'all-natural ingredients' but the label clearly lists 'artificial flavours.'"
                    },
                    {
                        "id": "q4",
                        "type": "media_literacy",
                        "skill": "Evaluating credibility",
                        "question": "Which source would be most reliable for making a purchasing decision?",
                        "options": [
                            "The influencer's post because they have many followers",
                            "The product label because it contains regulated information",
                            "The kitchen in the photo because it looks expensive",
                            "The hashtags because there are many of them"
                        ],
                        "correct": 1,
                        "explanation": "Product labels are regulated and must be accurate, unlike paid promotional content."
                    },
                    {
                        "id": "q5",
                        "type": "critical_thinking",
                        "skill": "Media analysis",
                        "question": "What is the most likely reason the photo shows professional lighting and an expensive kitchen?",
                        "options": [
                            "The influencer happens to live there",
                            "To create an aspirational image that associates the product with success",
                            "The lighting helps show the product colour",
                            "It was the only available location"
                        ],
                        "correct": 1,
                        "explanation": "Professional, aspirational imagery is a marketing technique to make viewers associate the product with a desirable lifestyle."
                    }
                ],
                "curriculum_alignment": ["critical_literacy", "comprehension"]
            }
        }

    def get_available_passages(self):
        """Return list of available passages for selection."""
        return [
            {
                "id": p["id"],
                "title": p["title"],
                "type": p["type"],
                "grade": p["grade"],
                "question_count": len(p["questions"]),
                "themes": p.get("themes", []),
                "related_texts": p.get("related_texts", [])
            }
            for p in self.passages.values()
        ]

    def get_passage(self, passage_id):
        """Get a specific passage by ID."""
        return self.passages.get(passage_id)

    def evaluate_answers(self, passage_id, answers):
        """
        Evaluate student answers and provide feedback.

        Args:
            passage_id: ID of the passage
            answers: Dict mapping question_id to selected answer index

        Returns:
            Results dict with score, feedback, and curriculum alignment
        """
        passage = self.passages.get(passage_id)
        if not passage:
            return {"error": "Passage not found"}

        results = {
            "passage_id": passage_id,
            "passage_title": passage["title"],
            "total_questions": len(passage["questions"]),
            "correct_count": 0,
            "score_percentage": 0,
            "achievement_level": "",
            "question_results": [],
            "skill_breakdown": {},
            "curriculum_feedback": []
        }

        skill_correct = {}
        skill_total = {}

        for question in passage["questions"]:
            qid = question["id"]
            skill = question["skill"]

            # Track skills
            skill_total[skill] = skill_total.get(skill, 0) + 1

            student_answer = answers.get(qid)
            is_correct = student_answer == question["correct"]

            if is_correct:
                results["correct_count"] += 1
                skill_correct[skill] = skill_correct.get(skill, 0) + 1

            results["question_results"].append({
                "question_id": qid,
                "question": question["question"],
                "skill": skill,
                "correct": is_correct,
                "student_answer": student_answer,
                "correct_answer": question["correct"],
                "explanation": question["explanation"]
            })

        # Calculate overall score
        results["score_percentage"] = round(
            (results["correct_count"] / results["total_questions"]) * 100
        )

        # Determine achievement level
        score = results["score_percentage"]
        if score >= 80:
            results["achievement_level"] = "Level 4"
        elif score >= 70:
            results["achievement_level"] = "Level 3"
        elif score >= 60:
            results["achievement_level"] = "Level 2"
        else:
            results["achievement_level"] = "Level 1"

        # Calculate skill breakdown
        for skill in skill_total:
            correct = skill_correct.get(skill, 0)
            total = skill_total[skill]
            results["skill_breakdown"][skill] = {
                "correct": correct,
                "total": total,
                "percentage": round((correct / total) * 100)
            }

        # Generate curriculum-aligned feedback
        results["curriculum_feedback"] = self._generate_feedback(results)

        return results

    def _generate_feedback(self, results):
        """Generate curriculum-aligned feedback based on results."""
        feedback = []

        for skill, data in results["skill_breakdown"].items():
            if data["percentage"] < 70:
                feedback.append({
                    "skill": skill,
                    "status": "needs_improvement",
                    "message": f"Consider practicing {skill.lower()}. "
                              f"Review strategies for this skill area."
                })
            elif data["percentage"] >= 80:
                feedback.append({
                    "skill": skill,
                    "status": "strength",
                    "message": f"Strong performance in {skill.lower()}!"
                })

        return feedback
