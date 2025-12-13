"""
Writing Assessment Module
Aligned with Ontario Language Curriculum Grade 7-8
"""

from app.curriculum import WRITING_EXPECTATIONS, WRITING_RUBRIC, ACHIEVEMENT_LEVELS


class WritingAssessment:
    """Handles writing assessments with curriculum-aligned rubrics."""

    def __init__(self):
        self.prompts = self._load_prompts()
        self.rubric = WRITING_RUBRIC

    def _load_prompts(self):
        """Load writing prompts aligned with Ontario curriculum."""
        return {
            "narrative_1": {
                "id": "narrative_1",
                "title": "A Moment That Changed Everything",
                "grade": "7-8",
                "type": "Narrative Writing",
                "prompt": """
Write a narrative about a moment when you (or a character) faced a difficult decision
that changed everything. Your story should include:

- A clear beginning, middle, and end
- A well-developed main character facing a conflict
- Descriptive details that help the reader visualize the setting and events
- Dialogue that reveals character and moves the story forward
- A resolution that shows how the character changed or learned something

Your narrative should be 3-5 paragraphs in length.
                """,
                "planning_questions": [
                    "What is the difficult decision your character faces?",
                    "What makes this decision hard?",
                    "How does your character change by the end?",
                    "What sensory details will you include?"
                ],
                "success_criteria": [
                    "Engaging opening that hooks the reader",
                    "Clear conflict or problem",
                    "Well-developed characters with thoughts and feelings",
                    "Vivid descriptive language and sensory details",
                    "Effective dialogue",
                    "Satisfying resolution",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 250,
                "word_maximum": 500
            },
            "persuasive_1": {
                "id": "persuasive_1",
                "title": "Screen Time: Help or Harm?",
                "grade": "7-8",
                "type": "Opinion/Persuasive Writing",
                "prompt": """
Many adults worry that teenagers spend too much time on screens (phones, tablets,
computers, gaming consoles). However, some argue that screen time can be educational
and beneficial.

Write a persuasive essay arguing your position on whether screen time helps or harms
teenagers. Your essay should include:

- A clear thesis statement expressing your opinion
- At least three strong arguments supporting your position
- Evidence or examples for each argument
- Acknowledgment of the opposing viewpoint
- A strong conclusion that reinforces your position

Your essay should be 4-5 paragraphs in length.
                """,
                "planning_questions": [
                    "What is your position on this issue?",
                    "What are your three strongest arguments?",
                    "What evidence supports each argument?",
                    "What might someone who disagrees say?"
                ],
                "success_criteria": [
                    "Clear thesis statement in introduction",
                    "Well-organized paragraphs with topic sentences",
                    "Strong supporting arguments with evidence",
                    "Addresses counterargument",
                    "Persuasive language and tone",
                    "Strong concluding statement",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 300,
                "word_maximum": 600
            },
            "informational_1": {
                "id": "informational_1",
                "title": "Explaining a Process",
                "grade": "7-8",
                "type": "Informational/Explanatory Writing",
                "prompt": """
Think of something you know how to do well—it could be a hobby, a skill, a game,
or any process you can explain clearly to someone who has never done it before.

Write an informational essay that explains this process step by step. Your essay
should include:

- An engaging introduction that explains what the process is and why it's useful
- Clear, sequential steps that are easy to follow
- Specific details and tips for success
- Transition words that guide the reader through the process
- A conclusion that summarizes key points

Your essay should be 4-5 paragraphs in length.
                """,
                "planning_questions": [
                    "What process will you explain?",
                    "What materials or preparation are needed?",
                    "What are the main steps in order?",
                    "What tips would help a beginner succeed?"
                ],
                "success_criteria": [
                    "Clear introduction of the topic",
                    "Logical, sequential organization",
                    "Specific, detailed steps",
                    "Helpful tips and warnings",
                    "Effective transition words",
                    "Appropriate informational tone",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 250,
                "word_maximum": 500
            },
            "response_1": {
                "id": "response_1",
                "title": "Response to Text",
                "grade": "7-8",
                "type": "Response to Reading",
                "prompt": """
Think about a book, article, movie, or other text that made you think deeply about
an important issue or changed your perspective on something.

Write a response essay that:

- Identifies the text and briefly summarizes the relevant part
- Explains the main idea or theme you want to discuss
- Shares your personal response and connections to the text
- Uses specific evidence (quotes or details) from the text to support your ideas
- Reflects on how the text affected your thinking

Your response should be 3-4 paragraphs in length.
                """,
                "planning_questions": [
                    "What text will you respond to?",
                    "What idea or theme stood out to you?",
                    "How did this connect to your own life or thinking?",
                    "What specific quotes or details will you reference?"
                ],
                "success_criteria": [
                    "Clear identification of the text",
                    "Focused discussion of theme or idea",
                    "Personal connections and reflections",
                    "Specific textual evidence",
                    "Thoughtful analysis",
                    "Appropriate academic tone",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 200,
                "word_maximum": 400
            }
        }

    def get_available_prompts(self):
        """Return list of available writing prompts."""
        return [
            {
                "id": p["id"],
                "title": p["title"],
                "type": p["type"],
                "grade": p["grade"],
                "word_minimum": p["word_minimum"],
                "word_maximum": p["word_maximum"]
            }
            for p in self.prompts.values()
        ]

    def get_prompt(self, prompt_id):
        """Get a specific prompt by ID."""
        return self.prompts.get(prompt_id)

    def evaluate_writing(self, prompt_id, response_text):
        """
        Provide writing assessment framework.

        Note: Full automated scoring would require NLP/AI integration.
        This provides structure for teacher evaluation or self-assessment.

        Args:
            prompt_id: ID of the writing prompt
            response_text: Student's written response

        Returns:
            Assessment framework with rubric and basic metrics
        """
        prompt = self.prompts.get(prompt_id)
        if not prompt:
            return {"error": "Prompt not found"}

        # Basic text analysis
        words = response_text.split()
        word_count = len(words)
        sentences = response_text.replace('!', '.').replace('?', '.').split('.')
        sentence_count = len([s for s in sentences if s.strip()])
        paragraphs = response_text.split('\n\n')
        paragraph_count = len([p for p in paragraphs if p.strip()])

        # Check word count requirements
        meets_minimum = word_count >= prompt["word_minimum"]
        exceeds_maximum = word_count > prompt["word_maximum"]

        results = {
            "prompt_id": prompt_id,
            "prompt_title": prompt["title"],
            "prompt_type": prompt["type"],
            "text_metrics": {
                "word_count": word_count,
                "sentence_count": sentence_count,
                "paragraph_count": paragraph_count,
                "average_sentence_length": round(word_count / max(sentence_count, 1), 1),
                "meets_word_minimum": meets_minimum,
                "exceeds_word_maximum": exceeds_maximum,
                "word_minimum": prompt["word_minimum"],
                "word_maximum": prompt["word_maximum"]
            },
            "rubric": self._get_rubric_for_type(prompt["type"]),
            "success_criteria": prompt["success_criteria"],
            "self_assessment_questions": self._get_self_assessment_questions(prompt["type"]),
            "feedback_areas": []
        }

        # Generate basic feedback based on metrics
        if not meets_minimum:
            results["feedback_areas"].append({
                "area": "Length",
                "feedback": f"Your response has {word_count} words. "
                           f"Try to expand your writing to at least {prompt['word_minimum']} words."
            })

        if exceeds_maximum:
            results["feedback_areas"].append({
                "area": "Length",
                "feedback": f"Your response has {word_count} words. "
                           f"Consider editing to stay within {prompt['word_maximum']} words."
            })

        if paragraph_count < 3:
            results["feedback_areas"].append({
                "area": "Organization",
                "feedback": "Consider organizing your writing into more paragraphs "
                           "for better structure."
            })

        avg_sentence = results["text_metrics"]["average_sentence_length"]
        if avg_sentence > 25:
            results["feedback_areas"].append({
                "area": "Sentence Variety",
                "feedback": "Your sentences are quite long on average. "
                           "Consider varying sentence length for better readability."
            })
        elif avg_sentence < 10:
            results["feedback_areas"].append({
                "area": "Sentence Variety",
                "feedback": "Your sentences are quite short on average. "
                           "Consider combining some sentences for better flow."
            })

        return results

    def _get_rubric_for_type(self, prompt_type):
        """Get assessment rubric formatted for display."""
        return {
            "categories": [
                {
                    "name": "Ideas and Content",
                    "weight": "25%",
                    "levels": {
                        "Level 4 (80-100%)": "Ideas are insightful, original, and fully developed with rich, relevant details",
                        "Level 3 (70-79%)": "Ideas are clear, focused, and well-developed with relevant details",
                        "Level 2 (60-69%)": "Ideas are present but may lack focus or sufficient development",
                        "Level 1 (50-59%)": "Ideas are unclear, unfocused, or minimally developed"
                    }
                },
                {
                    "name": "Organization",
                    "weight": "25%",
                    "levels": {
                        "Level 4 (80-100%)": "Exceptional organization with sophisticated transitions and logical flow",
                        "Level 3 (70-79%)": "Clear organization with effective transitions and coherent structure",
                        "Level 2 (60-69%)": "Some organization present but may have weak transitions",
                        "Level 1 (50-59%)": "Little or no organization; difficult to follow"
                    }
                },
                {
                    "name": "Voice and Style",
                    "weight": "25%",
                    "levels": {
                        "Level 4 (80-100%)": "Distinctive voice; sophisticated word choice and varied sentences",
                        "Level 3 (70-79%)": "Appropriate voice; effective word choice and sentence variety",
                        "Level 2 (60-69%)": "Inconsistent voice; limited word choice or sentence variety",
                        "Level 1 (50-59%)": "No clear voice; basic word choice and repetitive sentences"
                    }
                },
                {
                    "name": "Conventions",
                    "weight": "25%",
                    "levels": {
                        "Level 4 (80-100%)": "Virtually no errors in spelling, grammar, or punctuation",
                        "Level 3 (70-79%)": "Few errors that don't impede understanding",
                        "Level 2 (60-69%)": "Some errors that may impede understanding",
                        "Level 1 (50-59%)": "Frequent errors that significantly impede understanding"
                    }
                }
            ]
        }

    def _get_self_assessment_questions(self, prompt_type):
        """Get self-assessment questions based on writing type."""
        base_questions = [
            "Did I fully address all parts of the prompt?",
            "Is my writing organized with clear paragraphs?",
            "Did I use specific details and examples?",
            "Did I vary my sentence structure?",
            "Did I proofread for spelling and grammar errors?"
        ]

        type_specific = {
            "Narrative Writing": [
                "Does my story have a clear beginning, middle, and end?",
                "Did I develop my character's thoughts and feelings?",
                "Did I use descriptive language to help readers visualize the story?",
                "Does my dialogue sound natural and move the story forward?"
            ],
            "Opinion/Persuasive Writing": [
                "Is my thesis statement clear and arguable?",
                "Did I provide strong evidence for each argument?",
                "Did I address what someone who disagrees might say?",
                "Is my conclusion convincing?"
            ],
            "Informational/Explanatory Writing": [
                "Are my steps in logical order?",
                "Did I include all necessary information?",
                "Did I use transition words to guide the reader?",
                "Would someone unfamiliar with this topic understand my explanation?"
            ],
            "Response to Reading": [
                "Did I clearly identify the text I'm responding to?",
                "Did I include specific evidence from the text?",
                "Did I explain my personal connections to the text?",
                "Did I reflect on how the text affected my thinking?"
            ]
        }

        return base_questions + type_specific.get(prompt_type, [])
