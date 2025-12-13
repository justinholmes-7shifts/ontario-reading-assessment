"""
Reading Assessment Module
Aligned with Ontario Language Curriculum Grade 7-8
"""

from app.curriculum import READING_EXPECTATIONS, ACHIEVEMENT_LEVELS


class ReadingAssessment:
    """Handles reading comprehension assessments."""

    def __init__(self):
        self.passages = self._load_passages()

    def _load_passages(self):
        """Load reading passages with questions."""
        return {
            "fiction_1": {
                "id": "fiction_1",
                "title": "The Last Light",
                "grade": "7-8",
                "type": "Fiction - Short Story",
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
                        "skill": "Evaluating arguments",
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
            "nonfiction_1": {
                "id": "nonfiction_1",
                "title": "The Science of Sleep",
                "grade": "7-8",
                "type": "Non-Fiction - Informational",
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
                "question_count": len(p["questions"])
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
